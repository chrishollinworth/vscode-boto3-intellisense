"""
Main interface for cloudwatch service type definitions.

Usage::

    ```python
    from mypy_boto3_cloudwatch.type_defs import AlarmHistoryItemTypeDef

    data: AlarmHistoryItemTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AlarmHistoryItemTypeDef",
    "AnomalyDetectorConfigurationTypeDef",
    "AnomalyDetectorTypeDef",
    "CompositeAlarmTypeDef",
    "DashboardEntryTypeDef",
    "DashboardValidationMessageTypeDef",
    "DatapointTypeDef",
    "DimensionTypeDef",
    "InsightRuleContributorDatapointTypeDef",
    "InsightRuleContributorTypeDef",
    "InsightRuleMetricDatapointTypeDef",
    "InsightRuleTypeDef",
    "MessageDataTypeDef",
    "MetricAlarmTypeDef",
    "MetricDataQueryTypeDef",
    "MetricDataResultTypeDef",
    "MetricStatTypeDef",
    "MetricTypeDef",
    "PartialFailureTypeDef",
    "RangeTypeDef",
    "ResponseMetadata",
    "StatisticSetTypeDef",
    "TagTypeDef",
    "DeleteInsightRulesOutputTypeDef",
    "DescribeAlarmHistoryOutputTypeDef",
    "DescribeAlarmsForMetricOutputTypeDef",
    "DescribeAlarmsOutputTypeDef",
    "DescribeAnomalyDetectorsOutputTypeDef",
    "DescribeInsightRulesOutputTypeDef",
    "DimensionFilterTypeDef",
    "DisableInsightRulesOutputTypeDef",
    "EnableInsightRulesOutputTypeDef",
    "GetDashboardOutputTypeDef",
    "GetInsightRuleReportOutputTypeDef",
    "GetMetricDataOutputTypeDef",
    "GetMetricStatisticsOutputTypeDef",
    "GetMetricWidgetImageOutputTypeDef",
    "LabelOptionsTypeDef",
    "ListDashboardsOutputTypeDef",
    "ListMetricsOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MetricDatumTypeDef",
    "PaginatorConfigTypeDef",
    "PutDashboardOutputTypeDef",
    "WaiterConfigTypeDef",
)

AlarmHistoryItemTypeDef = TypedDict(
    "AlarmHistoryItemTypeDef",
    {
        "AlarmName": str,
        "AlarmType": Literal["CompositeAlarm", "MetricAlarm"],
        "Timestamp": datetime,
        "HistoryItemType": Literal["ConfigurationUpdate", "StateUpdate", "Action"],
        "HistorySummary": str,
        "HistoryData": str,
    },
    total=False,
)

AnomalyDetectorConfigurationTypeDef = TypedDict(
    "AnomalyDetectorConfigurationTypeDef",
    {"ExcludedTimeRanges": List["RangeTypeDef"], "MetricTimezone": str},
    total=False,
)

AnomalyDetectorTypeDef = TypedDict(
    "AnomalyDetectorTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List["DimensionTypeDef"],
        "Stat": str,
        "Configuration": "AnomalyDetectorConfigurationTypeDef",
        "StateValue": Literal["PENDING_TRAINING", "TRAINED_INSUFFICIENT_DATA", "TRAINED"],
    },
    total=False,
)

CompositeAlarmTypeDef = TypedDict(
    "CompositeAlarmTypeDef",
    {
        "ActionsEnabled": bool,
        "AlarmActions": List[str],
        "AlarmArn": str,
        "AlarmConfigurationUpdatedTimestamp": datetime,
        "AlarmDescription": str,
        "AlarmName": str,
        "AlarmRule": str,
        "InsufficientDataActions": List[str],
        "OKActions": List[str],
        "StateReason": str,
        "StateReasonData": str,
        "StateUpdatedTimestamp": datetime,
        "StateValue": Literal["OK", "ALARM", "INSUFFICIENT_DATA"],
    },
    total=False,
)

DashboardEntryTypeDef = TypedDict(
    "DashboardEntryTypeDef",
    {"DashboardName": str, "DashboardArn": str, "LastModified": datetime, "Size": int},
    total=False,
)

DashboardValidationMessageTypeDef = TypedDict(
    "DashboardValidationMessageTypeDef", {"DataPath": str, "Message": str}, total=False
)

DatapointTypeDef = TypedDict(
    "DatapointTypeDef",
    {
        "Timestamp": datetime,
        "SampleCount": float,
        "Average": float,
        "Sum": float,
        "Minimum": float,
        "Maximum": float,
        "Unit": Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ],
        "ExtendedStatistics": Dict[str, float],
    },
    total=False,
)

DimensionTypeDef = TypedDict("DimensionTypeDef", {"Name": str, "Value": str})

InsightRuleContributorDatapointTypeDef = TypedDict(
    "InsightRuleContributorDatapointTypeDef", {"Timestamp": datetime, "ApproximateValue": float}
)

InsightRuleContributorTypeDef = TypedDict(
    "InsightRuleContributorTypeDef",
    {
        "Keys": List[str],
        "ApproximateAggregateValue": float,
        "Datapoints": List["InsightRuleContributorDatapointTypeDef"],
    },
)

_RequiredInsightRuleMetricDatapointTypeDef = TypedDict(
    "_RequiredInsightRuleMetricDatapointTypeDef", {"Timestamp": datetime}
)
_OptionalInsightRuleMetricDatapointTypeDef = TypedDict(
    "_OptionalInsightRuleMetricDatapointTypeDef",
    {
        "UniqueContributors": float,
        "MaxContributorValue": float,
        "SampleCount": float,
        "Average": float,
        "Sum": float,
        "Minimum": float,
        "Maximum": float,
    },
    total=False,
)


class InsightRuleMetricDatapointTypeDef(
    _RequiredInsightRuleMetricDatapointTypeDef, _OptionalInsightRuleMetricDatapointTypeDef
):
    pass


InsightRuleTypeDef = TypedDict(
    "InsightRuleTypeDef", {"Name": str, "State": str, "Schema": str, "Definition": str}
)

MessageDataTypeDef = TypedDict("MessageDataTypeDef", {"Code": str, "Value": str}, total=False)

MetricAlarmTypeDef = TypedDict(
    "MetricAlarmTypeDef",
    {
        "AlarmName": str,
        "AlarmArn": str,
        "AlarmDescription": str,
        "AlarmConfigurationUpdatedTimestamp": datetime,
        "ActionsEnabled": bool,
        "OKActions": List[str],
        "AlarmActions": List[str],
        "InsufficientDataActions": List[str],
        "StateValue": Literal["OK", "ALARM", "INSUFFICIENT_DATA"],
        "StateReason": str,
        "StateReasonData": str,
        "StateUpdatedTimestamp": datetime,
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["SampleCount", "Average", "Sum", "Minimum", "Maximum"],
        "ExtendedStatistic": str,
        "Dimensions": List["DimensionTypeDef"],
        "Period": int,
        "Unit": Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ],
        "EvaluationPeriods": int,
        "DatapointsToAlarm": int,
        "Threshold": float,
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
            "LessThanLowerOrGreaterThanUpperThreshold",
            "LessThanLowerThreshold",
            "GreaterThanUpperThreshold",
        ],
        "TreatMissingData": str,
        "EvaluateLowSampleCountPercentile": str,
        "Metrics": List["MetricDataQueryTypeDef"],
        "ThresholdMetricId": str,
    },
    total=False,
)

_RequiredMetricDataQueryTypeDef = TypedDict("_RequiredMetricDataQueryTypeDef", {"Id": str})
_OptionalMetricDataQueryTypeDef = TypedDict(
    "_OptionalMetricDataQueryTypeDef",
    {
        "MetricStat": "MetricStatTypeDef",
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)


class MetricDataQueryTypeDef(_RequiredMetricDataQueryTypeDef, _OptionalMetricDataQueryTypeDef):
    pass


MetricDataResultTypeDef = TypedDict(
    "MetricDataResultTypeDef",
    {
        "Id": str,
        "Label": str,
        "Timestamps": List[datetime],
        "Values": List[float],
        "StatusCode": Literal["Complete", "InternalError", "PartialData"],
        "Messages": List["MessageDataTypeDef"],
    },
    total=False,
)

_RequiredMetricStatTypeDef = TypedDict(
    "_RequiredMetricStatTypeDef", {"Metric": "MetricTypeDef", "Period": int, "Stat": str}
)
_OptionalMetricStatTypeDef = TypedDict(
    "_OptionalMetricStatTypeDef",
    {
        "Unit": Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ]
    },
    total=False,
)


class MetricStatTypeDef(_RequiredMetricStatTypeDef, _OptionalMetricStatTypeDef):
    pass


MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {"Namespace": str, "MetricName": str, "Dimensions": List["DimensionTypeDef"]},
    total=False,
)

PartialFailureTypeDef = TypedDict(
    "PartialFailureTypeDef",
    {"FailureResource": str, "ExceptionType": str, "FailureCode": str, "FailureDescription": str},
    total=False,
)

RangeTypeDef = TypedDict("RangeTypeDef", {"StartTime": datetime, "EndTime": datetime})

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

StatisticSetTypeDef = TypedDict(
    "StatisticSetTypeDef", {"SampleCount": float, "Sum": float, "Minimum": float, "Maximum": float}
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

DeleteInsightRulesOutputTypeDef = TypedDict(
    "DeleteInsightRulesOutputTypeDef",
    {"Failures": List["PartialFailureTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeAlarmHistoryOutputTypeDef = TypedDict(
    "DescribeAlarmHistoryOutputTypeDef",
    {
        "AlarmHistoryItems": List["AlarmHistoryItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeAlarmsForMetricOutputTypeDef = TypedDict(
    "DescribeAlarmsForMetricOutputTypeDef",
    {"MetricAlarms": List["MetricAlarmTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeAlarmsOutputTypeDef = TypedDict(
    "DescribeAlarmsOutputTypeDef",
    {
        "CompositeAlarms": List["CompositeAlarmTypeDef"],
        "MetricAlarms": List["MetricAlarmTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeAnomalyDetectorsOutputTypeDef = TypedDict(
    "DescribeAnomalyDetectorsOutputTypeDef",
    {
        "AnomalyDetectors": List["AnomalyDetectorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeInsightRulesOutputTypeDef = TypedDict(
    "DescribeInsightRulesOutputTypeDef",
    {
        "NextToken": str,
        "InsightRules": List["InsightRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredDimensionFilterTypeDef = TypedDict("_RequiredDimensionFilterTypeDef", {"Name": str})
_OptionalDimensionFilterTypeDef = TypedDict(
    "_OptionalDimensionFilterTypeDef", {"Value": str}, total=False
)


class DimensionFilterTypeDef(_RequiredDimensionFilterTypeDef, _OptionalDimensionFilterTypeDef):
    pass


DisableInsightRulesOutputTypeDef = TypedDict(
    "DisableInsightRulesOutputTypeDef",
    {"Failures": List["PartialFailureTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

EnableInsightRulesOutputTypeDef = TypedDict(
    "EnableInsightRulesOutputTypeDef",
    {"Failures": List["PartialFailureTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetDashboardOutputTypeDef = TypedDict(
    "GetDashboardOutputTypeDef",
    {
        "DashboardArn": str,
        "DashboardBody": str,
        "DashboardName": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetInsightRuleReportOutputTypeDef = TypedDict(
    "GetInsightRuleReportOutputTypeDef",
    {
        "KeyLabels": List[str],
        "AggregationStatistic": str,
        "AggregateValue": float,
        "ApproximateUniqueCount": int,
        "Contributors": List["InsightRuleContributorTypeDef"],
        "MetricDatapoints": List["InsightRuleMetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetMetricDataOutputTypeDef = TypedDict(
    "GetMetricDataOutputTypeDef",
    {
        "MetricDataResults": List["MetricDataResultTypeDef"],
        "NextToken": str,
        "Messages": List["MessageDataTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetMetricStatisticsOutputTypeDef = TypedDict(
    "GetMetricStatisticsOutputTypeDef",
    {"Label": str, "Datapoints": List["DatapointTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetMetricWidgetImageOutputTypeDef = TypedDict(
    "GetMetricWidgetImageOutputTypeDef",
    {"MetricWidgetImage": Union[bytes, IO[bytes]], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

LabelOptionsTypeDef = TypedDict("LabelOptionsTypeDef", {"Timezone": str}, total=False)

ListDashboardsOutputTypeDef = TypedDict(
    "ListDashboardsOutputTypeDef",
    {
        "DashboardEntries": List["DashboardEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListMetricsOutputTypeDef = TypedDict(
    "ListMetricsOutputTypeDef",
    {"Metrics": List["MetricTypeDef"], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {"Tags": List["TagTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredMetricDatumTypeDef = TypedDict("_RequiredMetricDatumTypeDef", {"MetricName": str})
_OptionalMetricDatumTypeDef = TypedDict(
    "_OptionalMetricDatumTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
        "Timestamp": datetime,
        "Value": float,
        "StatisticValues": "StatisticSetTypeDef",
        "Values": List[float],
        "Counts": List[float],
        "Unit": Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ],
        "StorageResolution": int,
    },
    total=False,
)


class MetricDatumTypeDef(_RequiredMetricDatumTypeDef, _OptionalMetricDatumTypeDef):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutDashboardOutputTypeDef = TypedDict(
    "PutDashboardOutputTypeDef",
    {
        "DashboardValidationMessages": List["DashboardValidationMessageTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
