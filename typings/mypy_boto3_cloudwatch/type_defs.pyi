"""
Type annotations for cloudwatch service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudwatch.type_defs import AlarmHistoryItemTypeDef

    data: AlarmHistoryItemTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AlarmTypeType,
    AnomalyDetectorStateValueType,
    ComparisonOperatorType,
    HistoryItemTypeType,
    MetricStreamOutputFormatType,
    ScanByType,
    StandardUnitType,
    StateValueType,
    StatisticType,
    StatusCodeType,
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
    "AlarmHistoryItemTypeDef",
    "AnomalyDetectorConfigurationTypeDef",
    "AnomalyDetectorTypeDef",
    "CompositeAlarmTypeDef",
    "DashboardEntryTypeDef",
    "DashboardValidationMessageTypeDef",
    "DatapointTypeDef",
    "DeleteAlarmsInputRequestTypeDef",
    "DeleteAnomalyDetectorInputRequestTypeDef",
    "DeleteDashboardsInputRequestTypeDef",
    "DeleteInsightRulesInputRequestTypeDef",
    "DeleteInsightRulesOutputTypeDef",
    "DeleteMetricStreamInputRequestTypeDef",
    "DescribeAlarmHistoryInputAlarmTypeDef",
    "DescribeAlarmHistoryInputRequestTypeDef",
    "DescribeAlarmHistoryOutputTypeDef",
    "DescribeAlarmsForMetricInputRequestTypeDef",
    "DescribeAlarmsForMetricOutputTypeDef",
    "DescribeAlarmsInputRequestTypeDef",
    "DescribeAlarmsOutputTypeDef",
    "DescribeAnomalyDetectorsInputRequestTypeDef",
    "DescribeAnomalyDetectorsOutputTypeDef",
    "DescribeInsightRulesInputRequestTypeDef",
    "DescribeInsightRulesOutputTypeDef",
    "DimensionFilterTypeDef",
    "DimensionTypeDef",
    "DisableAlarmActionsInputRequestTypeDef",
    "DisableInsightRulesInputRequestTypeDef",
    "DisableInsightRulesOutputTypeDef",
    "EnableAlarmActionsInputRequestTypeDef",
    "EnableInsightRulesInputRequestTypeDef",
    "EnableInsightRulesOutputTypeDef",
    "GetDashboardInputRequestTypeDef",
    "GetDashboardOutputTypeDef",
    "GetInsightRuleReportInputRequestTypeDef",
    "GetInsightRuleReportOutputTypeDef",
    "GetMetricDataInputRequestTypeDef",
    "GetMetricDataOutputTypeDef",
    "GetMetricStatisticsInputMetricTypeDef",
    "GetMetricStatisticsInputRequestTypeDef",
    "GetMetricStatisticsOutputTypeDef",
    "GetMetricStreamInputRequestTypeDef",
    "GetMetricStreamOutputTypeDef",
    "GetMetricWidgetImageInputRequestTypeDef",
    "GetMetricWidgetImageOutputTypeDef",
    "InsightRuleContributorDatapointTypeDef",
    "InsightRuleContributorTypeDef",
    "InsightRuleMetricDatapointTypeDef",
    "InsightRuleTypeDef",
    "LabelOptionsTypeDef",
    "ListDashboardsInputRequestTypeDef",
    "ListDashboardsOutputTypeDef",
    "ListMetricStreamsInputRequestTypeDef",
    "ListMetricStreamsOutputTypeDef",
    "ListMetricsInputRequestTypeDef",
    "ListMetricsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MessageDataTypeDef",
    "MetricAlarmTypeDef",
    "MetricDataQueryTypeDef",
    "MetricDataResultTypeDef",
    "MetricDatumTypeDef",
    "MetricStatTypeDef",
    "MetricStreamEntryTypeDef",
    "MetricStreamFilterTypeDef",
    "MetricTypeDef",
    "PaginatorConfigTypeDef",
    "PartialFailureTypeDef",
    "PutAnomalyDetectorInputRequestTypeDef",
    "PutCompositeAlarmInputRequestTypeDef",
    "PutDashboardInputRequestTypeDef",
    "PutDashboardOutputTypeDef",
    "PutInsightRuleInputRequestTypeDef",
    "PutMetricAlarmInputMetricTypeDef",
    "PutMetricAlarmInputRequestTypeDef",
    "PutMetricDataInputRequestTypeDef",
    "PutMetricStreamInputRequestTypeDef",
    "PutMetricStreamOutputTypeDef",
    "RangeTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceResourceAlarmRequestTypeDef",
    "ServiceResourceMetricRequestTypeDef",
    "SetAlarmStateInputAlarmTypeDef",
    "SetAlarmStateInputRequestTypeDef",
    "StartMetricStreamsInputRequestTypeDef",
    "StatisticSetTypeDef",
    "StopMetricStreamsInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "UntagResourceInputRequestTypeDef",
    "WaiterConfigTypeDef",
)

AlarmHistoryItemTypeDef = TypedDict(
    "AlarmHistoryItemTypeDef",
    {
        "AlarmName": str,
        "AlarmType": AlarmTypeType,
        "Timestamp": datetime,
        "HistoryItemType": HistoryItemTypeType,
        "HistorySummary": str,
        "HistoryData": str,
    },
    total=False,
)

AnomalyDetectorConfigurationTypeDef = TypedDict(
    "AnomalyDetectorConfigurationTypeDef",
    {
        "ExcludedTimeRanges": List["RangeTypeDef"],
        "MetricTimezone": str,
    },
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
        "StateValue": AnomalyDetectorStateValueType,
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
        "StateValue": StateValueType,
    },
    total=False,
)

DashboardEntryTypeDef = TypedDict(
    "DashboardEntryTypeDef",
    {
        "DashboardName": str,
        "DashboardArn": str,
        "LastModified": datetime,
        "Size": int,
    },
    total=False,
)

DashboardValidationMessageTypeDef = TypedDict(
    "DashboardValidationMessageTypeDef",
    {
        "DataPath": str,
        "Message": str,
    },
    total=False,
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
        "Unit": StandardUnitType,
        "ExtendedStatistics": Dict[str, float],
    },
    total=False,
)

DeleteAlarmsInputRequestTypeDef = TypedDict(
    "DeleteAlarmsInputRequestTypeDef",
    {
        "AlarmNames": List[str],
    },
)

_RequiredDeleteAnomalyDetectorInputRequestTypeDef = TypedDict(
    "_RequiredDeleteAnomalyDetectorInputRequestTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Stat": str,
    },
)
_OptionalDeleteAnomalyDetectorInputRequestTypeDef = TypedDict(
    "_OptionalDeleteAnomalyDetectorInputRequestTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
    },
    total=False,
)

class DeleteAnomalyDetectorInputRequestTypeDef(
    _RequiredDeleteAnomalyDetectorInputRequestTypeDef,
    _OptionalDeleteAnomalyDetectorInputRequestTypeDef,
):
    pass

DeleteDashboardsInputRequestTypeDef = TypedDict(
    "DeleteDashboardsInputRequestTypeDef",
    {
        "DashboardNames": List[str],
    },
)

DeleteInsightRulesInputRequestTypeDef = TypedDict(
    "DeleteInsightRulesInputRequestTypeDef",
    {
        "RuleNames": List[str],
    },
)

DeleteInsightRulesOutputTypeDef = TypedDict(
    "DeleteInsightRulesOutputTypeDef",
    {
        "Failures": List["PartialFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMetricStreamInputRequestTypeDef = TypedDict(
    "DeleteMetricStreamInputRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeAlarmHistoryInputAlarmTypeDef = TypedDict(
    "DescribeAlarmHistoryInputAlarmTypeDef",
    {
        "AlarmTypes": List[AlarmTypeType],
        "HistoryItemType": HistoryItemTypeType,
        "StartDate": Union[datetime, str],
        "EndDate": Union[datetime, str],
        "MaxRecords": int,
        "NextToken": str,
        "ScanBy": ScanByType,
    },
    total=False,
)

DescribeAlarmHistoryInputRequestTypeDef = TypedDict(
    "DescribeAlarmHistoryInputRequestTypeDef",
    {
        "AlarmName": str,
        "AlarmTypes": List[AlarmTypeType],
        "HistoryItemType": HistoryItemTypeType,
        "StartDate": Union[datetime, str],
        "EndDate": Union[datetime, str],
        "MaxRecords": int,
        "NextToken": str,
        "ScanBy": ScanByType,
    },
    total=False,
)

DescribeAlarmHistoryOutputTypeDef = TypedDict(
    "DescribeAlarmHistoryOutputTypeDef",
    {
        "AlarmHistoryItems": List["AlarmHistoryItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAlarmsForMetricInputRequestTypeDef = TypedDict(
    "_RequiredDescribeAlarmsForMetricInputRequestTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
    },
)
_OptionalDescribeAlarmsForMetricInputRequestTypeDef = TypedDict(
    "_OptionalDescribeAlarmsForMetricInputRequestTypeDef",
    {
        "Statistic": StatisticType,
        "ExtendedStatistic": str,
        "Dimensions": List["DimensionTypeDef"],
        "Period": int,
        "Unit": StandardUnitType,
    },
    total=False,
)

class DescribeAlarmsForMetricInputRequestTypeDef(
    _RequiredDescribeAlarmsForMetricInputRequestTypeDef,
    _OptionalDescribeAlarmsForMetricInputRequestTypeDef,
):
    pass

DescribeAlarmsForMetricOutputTypeDef = TypedDict(
    "DescribeAlarmsForMetricOutputTypeDef",
    {
        "MetricAlarms": List["MetricAlarmTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAlarmsInputRequestTypeDef = TypedDict(
    "DescribeAlarmsInputRequestTypeDef",
    {
        "AlarmNames": List[str],
        "AlarmNamePrefix": str,
        "AlarmTypes": List[AlarmTypeType],
        "ChildrenOfAlarmName": str,
        "ParentsOfAlarmName": str,
        "StateValue": StateValueType,
        "ActionPrefix": str,
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeAlarmsOutputTypeDef = TypedDict(
    "DescribeAlarmsOutputTypeDef",
    {
        "CompositeAlarms": List["CompositeAlarmTypeDef"],
        "MetricAlarms": List["MetricAlarmTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAnomalyDetectorsInputRequestTypeDef = TypedDict(
    "DescribeAnomalyDetectorsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List["DimensionTypeDef"],
    },
    total=False,
)

DescribeAnomalyDetectorsOutputTypeDef = TypedDict(
    "DescribeAnomalyDetectorsOutputTypeDef",
    {
        "AnomalyDetectors": List["AnomalyDetectorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInsightRulesInputRequestTypeDef = TypedDict(
    "DescribeInsightRulesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeInsightRulesOutputTypeDef = TypedDict(
    "DescribeInsightRulesOutputTypeDef",
    {
        "NextToken": str,
        "InsightRules": List["InsightRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDimensionFilterTypeDef = TypedDict(
    "_RequiredDimensionFilterTypeDef",
    {
        "Name": str,
    },
)
_OptionalDimensionFilterTypeDef = TypedDict(
    "_OptionalDimensionFilterTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class DimensionFilterTypeDef(_RequiredDimensionFilterTypeDef, _OptionalDimensionFilterTypeDef):
    pass

DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

DisableAlarmActionsInputRequestTypeDef = TypedDict(
    "DisableAlarmActionsInputRequestTypeDef",
    {
        "AlarmNames": List[str],
    },
)

DisableInsightRulesInputRequestTypeDef = TypedDict(
    "DisableInsightRulesInputRequestTypeDef",
    {
        "RuleNames": List[str],
    },
)

DisableInsightRulesOutputTypeDef = TypedDict(
    "DisableInsightRulesOutputTypeDef",
    {
        "Failures": List["PartialFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableAlarmActionsInputRequestTypeDef = TypedDict(
    "EnableAlarmActionsInputRequestTypeDef",
    {
        "AlarmNames": List[str],
    },
)

EnableInsightRulesInputRequestTypeDef = TypedDict(
    "EnableInsightRulesInputRequestTypeDef",
    {
        "RuleNames": List[str],
    },
)

EnableInsightRulesOutputTypeDef = TypedDict(
    "EnableInsightRulesOutputTypeDef",
    {
        "Failures": List["PartialFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDashboardInputRequestTypeDef = TypedDict(
    "GetDashboardInputRequestTypeDef",
    {
        "DashboardName": str,
    },
)

GetDashboardOutputTypeDef = TypedDict(
    "GetDashboardOutputTypeDef",
    {
        "DashboardArn": str,
        "DashboardBody": str,
        "DashboardName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetInsightRuleReportInputRequestTypeDef = TypedDict(
    "_RequiredGetInsightRuleReportInputRequestTypeDef",
    {
        "RuleName": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Period": int,
    },
)
_OptionalGetInsightRuleReportInputRequestTypeDef = TypedDict(
    "_OptionalGetInsightRuleReportInputRequestTypeDef",
    {
        "MaxContributorCount": int,
        "Metrics": List[str],
        "OrderBy": str,
    },
    total=False,
)

class GetInsightRuleReportInputRequestTypeDef(
    _RequiredGetInsightRuleReportInputRequestTypeDef,
    _OptionalGetInsightRuleReportInputRequestTypeDef,
):
    pass

GetInsightRuleReportOutputTypeDef = TypedDict(
    "GetInsightRuleReportOutputTypeDef",
    {
        "KeyLabels": List[str],
        "AggregationStatistic": str,
        "AggregateValue": float,
        "ApproximateUniqueCount": int,
        "Contributors": List["InsightRuleContributorTypeDef"],
        "MetricDatapoints": List["InsightRuleMetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMetricDataInputRequestTypeDef = TypedDict(
    "_RequiredGetMetricDataInputRequestTypeDef",
    {
        "MetricDataQueries": List["MetricDataQueryTypeDef"],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)
_OptionalGetMetricDataInputRequestTypeDef = TypedDict(
    "_OptionalGetMetricDataInputRequestTypeDef",
    {
        "NextToken": str,
        "ScanBy": ScanByType,
        "MaxDatapoints": int,
        "LabelOptions": "LabelOptionsTypeDef",
    },
    total=False,
)

class GetMetricDataInputRequestTypeDef(
    _RequiredGetMetricDataInputRequestTypeDef, _OptionalGetMetricDataInputRequestTypeDef
):
    pass

GetMetricDataOutputTypeDef = TypedDict(
    "GetMetricDataOutputTypeDef",
    {
        "MetricDataResults": List["MetricDataResultTypeDef"],
        "NextToken": str,
        "Messages": List["MessageDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMetricStatisticsInputMetricTypeDef = TypedDict(
    "_RequiredGetMetricStatisticsInputMetricTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Period": int,
    },
)
_OptionalGetMetricStatisticsInputMetricTypeDef = TypedDict(
    "_OptionalGetMetricStatisticsInputMetricTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
        "Statistics": List[StatisticType],
        "ExtendedStatistics": List[str],
        "Unit": StandardUnitType,
    },
    total=False,
)

class GetMetricStatisticsInputMetricTypeDef(
    _RequiredGetMetricStatisticsInputMetricTypeDef, _OptionalGetMetricStatisticsInputMetricTypeDef
):
    pass

_RequiredGetMetricStatisticsInputRequestTypeDef = TypedDict(
    "_RequiredGetMetricStatisticsInputRequestTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Period": int,
    },
)
_OptionalGetMetricStatisticsInputRequestTypeDef = TypedDict(
    "_OptionalGetMetricStatisticsInputRequestTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
        "Statistics": List[StatisticType],
        "ExtendedStatistics": List[str],
        "Unit": StandardUnitType,
    },
    total=False,
)

class GetMetricStatisticsInputRequestTypeDef(
    _RequiredGetMetricStatisticsInputRequestTypeDef, _OptionalGetMetricStatisticsInputRequestTypeDef
):
    pass

GetMetricStatisticsOutputTypeDef = TypedDict(
    "GetMetricStatisticsOutputTypeDef",
    {
        "Label": str,
        "Datapoints": List["DatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMetricStreamInputRequestTypeDef = TypedDict(
    "GetMetricStreamInputRequestTypeDef",
    {
        "Name": str,
    },
)

GetMetricStreamOutputTypeDef = TypedDict(
    "GetMetricStreamOutputTypeDef",
    {
        "Arn": str,
        "Name": str,
        "IncludeFilters": List["MetricStreamFilterTypeDef"],
        "ExcludeFilters": List["MetricStreamFilterTypeDef"],
        "FirehoseArn": str,
        "RoleArn": str,
        "State": str,
        "CreationDate": datetime,
        "LastUpdateDate": datetime,
        "OutputFormat": MetricStreamOutputFormatType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMetricWidgetImageInputRequestTypeDef = TypedDict(
    "_RequiredGetMetricWidgetImageInputRequestTypeDef",
    {
        "MetricWidget": str,
    },
)
_OptionalGetMetricWidgetImageInputRequestTypeDef = TypedDict(
    "_OptionalGetMetricWidgetImageInputRequestTypeDef",
    {
        "OutputFormat": str,
    },
    total=False,
)

class GetMetricWidgetImageInputRequestTypeDef(
    _RequiredGetMetricWidgetImageInputRequestTypeDef,
    _OptionalGetMetricWidgetImageInputRequestTypeDef,
):
    pass

GetMetricWidgetImageOutputTypeDef = TypedDict(
    "GetMetricWidgetImageOutputTypeDef",
    {
        "MetricWidgetImage": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InsightRuleContributorDatapointTypeDef = TypedDict(
    "InsightRuleContributorDatapointTypeDef",
    {
        "Timestamp": datetime,
        "ApproximateValue": float,
    },
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
    "_RequiredInsightRuleMetricDatapointTypeDef",
    {
        "Timestamp": datetime,
    },
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
    "InsightRuleTypeDef",
    {
        "Name": str,
        "State": str,
        "Schema": str,
        "Definition": str,
    },
)

LabelOptionsTypeDef = TypedDict(
    "LabelOptionsTypeDef",
    {
        "Timezone": str,
    },
    total=False,
)

ListDashboardsInputRequestTypeDef = TypedDict(
    "ListDashboardsInputRequestTypeDef",
    {
        "DashboardNamePrefix": str,
        "NextToken": str,
    },
    total=False,
)

ListDashboardsOutputTypeDef = TypedDict(
    "ListDashboardsOutputTypeDef",
    {
        "DashboardEntries": List["DashboardEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMetricStreamsInputRequestTypeDef = TypedDict(
    "ListMetricStreamsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListMetricStreamsOutputTypeDef = TypedDict(
    "ListMetricStreamsOutputTypeDef",
    {
        "NextToken": str,
        "Entries": List["MetricStreamEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMetricsInputRequestTypeDef = TypedDict(
    "ListMetricsInputRequestTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List["DimensionFilterTypeDef"],
        "NextToken": str,
        "RecentlyActive": Literal["PT3H"],
    },
    total=False,
)

ListMetricsOutputTypeDef = TypedDict(
    "ListMetricsOutputTypeDef",
    {
        "Metrics": List["MetricTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MessageDataTypeDef = TypedDict(
    "MessageDataTypeDef",
    {
        "Code": str,
        "Value": str,
    },
    total=False,
)

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
        "StateValue": StateValueType,
        "StateReason": str,
        "StateReasonData": str,
        "StateUpdatedTimestamp": datetime,
        "MetricName": str,
        "Namespace": str,
        "Statistic": StatisticType,
        "ExtendedStatistic": str,
        "Dimensions": List["DimensionTypeDef"],
        "Period": int,
        "Unit": StandardUnitType,
        "EvaluationPeriods": int,
        "DatapointsToAlarm": int,
        "Threshold": float,
        "ComparisonOperator": ComparisonOperatorType,
        "TreatMissingData": str,
        "EvaluateLowSampleCountPercentile": str,
        "Metrics": List["MetricDataQueryTypeDef"],
        "ThresholdMetricId": str,
    },
    total=False,
)

_RequiredMetricDataQueryTypeDef = TypedDict(
    "_RequiredMetricDataQueryTypeDef",
    {
        "Id": str,
    },
)
_OptionalMetricDataQueryTypeDef = TypedDict(
    "_OptionalMetricDataQueryTypeDef",
    {
        "MetricStat": "MetricStatTypeDef",
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
        "AccountId": str,
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
        "StatusCode": StatusCodeType,
        "Messages": List["MessageDataTypeDef"],
    },
    total=False,
)

_RequiredMetricDatumTypeDef = TypedDict(
    "_RequiredMetricDatumTypeDef",
    {
        "MetricName": str,
    },
)
_OptionalMetricDatumTypeDef = TypedDict(
    "_OptionalMetricDatumTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
        "Timestamp": Union[datetime, str],
        "Value": float,
        "StatisticValues": "StatisticSetTypeDef",
        "Values": List[float],
        "Counts": List[float],
        "Unit": StandardUnitType,
        "StorageResolution": int,
    },
    total=False,
)

class MetricDatumTypeDef(_RequiredMetricDatumTypeDef, _OptionalMetricDatumTypeDef):
    pass

_RequiredMetricStatTypeDef = TypedDict(
    "_RequiredMetricStatTypeDef",
    {
        "Metric": "MetricTypeDef",
        "Period": int,
        "Stat": str,
    },
)
_OptionalMetricStatTypeDef = TypedDict(
    "_OptionalMetricStatTypeDef",
    {
        "Unit": StandardUnitType,
    },
    total=False,
)

class MetricStatTypeDef(_RequiredMetricStatTypeDef, _OptionalMetricStatTypeDef):
    pass

MetricStreamEntryTypeDef = TypedDict(
    "MetricStreamEntryTypeDef",
    {
        "Arn": str,
        "CreationDate": datetime,
        "LastUpdateDate": datetime,
        "Name": str,
        "FirehoseArn": str,
        "State": str,
        "OutputFormat": MetricStreamOutputFormatType,
    },
    total=False,
)

MetricStreamFilterTypeDef = TypedDict(
    "MetricStreamFilterTypeDef",
    {
        "Namespace": str,
    },
    total=False,
)

MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List["DimensionTypeDef"],
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

PartialFailureTypeDef = TypedDict(
    "PartialFailureTypeDef",
    {
        "FailureResource": str,
        "ExceptionType": str,
        "FailureCode": str,
        "FailureDescription": str,
    },
    total=False,
)

_RequiredPutAnomalyDetectorInputRequestTypeDef = TypedDict(
    "_RequiredPutAnomalyDetectorInputRequestTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Stat": str,
    },
)
_OptionalPutAnomalyDetectorInputRequestTypeDef = TypedDict(
    "_OptionalPutAnomalyDetectorInputRequestTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
        "Configuration": "AnomalyDetectorConfigurationTypeDef",
    },
    total=False,
)

class PutAnomalyDetectorInputRequestTypeDef(
    _RequiredPutAnomalyDetectorInputRequestTypeDef, _OptionalPutAnomalyDetectorInputRequestTypeDef
):
    pass

_RequiredPutCompositeAlarmInputRequestTypeDef = TypedDict(
    "_RequiredPutCompositeAlarmInputRequestTypeDef",
    {
        "AlarmName": str,
        "AlarmRule": str,
    },
)
_OptionalPutCompositeAlarmInputRequestTypeDef = TypedDict(
    "_OptionalPutCompositeAlarmInputRequestTypeDef",
    {
        "ActionsEnabled": bool,
        "AlarmActions": List[str],
        "AlarmDescription": str,
        "InsufficientDataActions": List[str],
        "OKActions": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class PutCompositeAlarmInputRequestTypeDef(
    _RequiredPutCompositeAlarmInputRequestTypeDef, _OptionalPutCompositeAlarmInputRequestTypeDef
):
    pass

PutDashboardInputRequestTypeDef = TypedDict(
    "PutDashboardInputRequestTypeDef",
    {
        "DashboardName": str,
        "DashboardBody": str,
    },
)

PutDashboardOutputTypeDef = TypedDict(
    "PutDashboardOutputTypeDef",
    {
        "DashboardValidationMessages": List["DashboardValidationMessageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutInsightRuleInputRequestTypeDef = TypedDict(
    "_RequiredPutInsightRuleInputRequestTypeDef",
    {
        "RuleName": str,
        "RuleDefinition": str,
    },
)
_OptionalPutInsightRuleInputRequestTypeDef = TypedDict(
    "_OptionalPutInsightRuleInputRequestTypeDef",
    {
        "RuleState": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class PutInsightRuleInputRequestTypeDef(
    _RequiredPutInsightRuleInputRequestTypeDef, _OptionalPutInsightRuleInputRequestTypeDef
):
    pass

_RequiredPutMetricAlarmInputMetricTypeDef = TypedDict(
    "_RequiredPutMetricAlarmInputMetricTypeDef",
    {
        "AlarmName": str,
        "EvaluationPeriods": int,
        "ComparisonOperator": ComparisonOperatorType,
    },
)
_OptionalPutMetricAlarmInputMetricTypeDef = TypedDict(
    "_OptionalPutMetricAlarmInputMetricTypeDef",
    {
        "AlarmDescription": str,
        "ActionsEnabled": bool,
        "OKActions": List[str],
        "AlarmActions": List[str],
        "InsufficientDataActions": List[str],
        "Statistic": StatisticType,
        "ExtendedStatistic": str,
        "Dimensions": List["DimensionTypeDef"],
        "Period": int,
        "Unit": StandardUnitType,
        "DatapointsToAlarm": int,
        "Threshold": float,
        "TreatMissingData": str,
        "EvaluateLowSampleCountPercentile": str,
        "Metrics": List["MetricDataQueryTypeDef"],
        "Tags": List["TagTypeDef"],
        "ThresholdMetricId": str,
    },
    total=False,
)

class PutMetricAlarmInputMetricTypeDef(
    _RequiredPutMetricAlarmInputMetricTypeDef, _OptionalPutMetricAlarmInputMetricTypeDef
):
    pass

_RequiredPutMetricAlarmInputRequestTypeDef = TypedDict(
    "_RequiredPutMetricAlarmInputRequestTypeDef",
    {
        "AlarmName": str,
        "EvaluationPeriods": int,
        "ComparisonOperator": ComparisonOperatorType,
    },
)
_OptionalPutMetricAlarmInputRequestTypeDef = TypedDict(
    "_OptionalPutMetricAlarmInputRequestTypeDef",
    {
        "AlarmDescription": str,
        "ActionsEnabled": bool,
        "OKActions": List[str],
        "AlarmActions": List[str],
        "InsufficientDataActions": List[str],
        "MetricName": str,
        "Namespace": str,
        "Statistic": StatisticType,
        "ExtendedStatistic": str,
        "Dimensions": List["DimensionTypeDef"],
        "Period": int,
        "Unit": StandardUnitType,
        "DatapointsToAlarm": int,
        "Threshold": float,
        "TreatMissingData": str,
        "EvaluateLowSampleCountPercentile": str,
        "Metrics": List["MetricDataQueryTypeDef"],
        "Tags": List["TagTypeDef"],
        "ThresholdMetricId": str,
    },
    total=False,
)

class PutMetricAlarmInputRequestTypeDef(
    _RequiredPutMetricAlarmInputRequestTypeDef, _OptionalPutMetricAlarmInputRequestTypeDef
):
    pass

PutMetricDataInputRequestTypeDef = TypedDict(
    "PutMetricDataInputRequestTypeDef",
    {
        "Namespace": str,
        "MetricData": List["MetricDatumTypeDef"],
    },
)

_RequiredPutMetricStreamInputRequestTypeDef = TypedDict(
    "_RequiredPutMetricStreamInputRequestTypeDef",
    {
        "Name": str,
        "FirehoseArn": str,
        "RoleArn": str,
        "OutputFormat": MetricStreamOutputFormatType,
    },
)
_OptionalPutMetricStreamInputRequestTypeDef = TypedDict(
    "_OptionalPutMetricStreamInputRequestTypeDef",
    {
        "IncludeFilters": List["MetricStreamFilterTypeDef"],
        "ExcludeFilters": List["MetricStreamFilterTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class PutMetricStreamInputRequestTypeDef(
    _RequiredPutMetricStreamInputRequestTypeDef, _OptionalPutMetricStreamInputRequestTypeDef
):
    pass

PutMetricStreamOutputTypeDef = TypedDict(
    "PutMetricStreamOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
    },
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

ServiceResourceAlarmRequestTypeDef = TypedDict(
    "ServiceResourceAlarmRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceMetricRequestTypeDef = TypedDict(
    "ServiceResourceMetricRequestTypeDef",
    {
        "namespace": str,
        "name": str,
    },
)

_RequiredSetAlarmStateInputAlarmTypeDef = TypedDict(
    "_RequiredSetAlarmStateInputAlarmTypeDef",
    {
        "StateValue": StateValueType,
        "StateReason": str,
    },
)
_OptionalSetAlarmStateInputAlarmTypeDef = TypedDict(
    "_OptionalSetAlarmStateInputAlarmTypeDef",
    {
        "StateReasonData": str,
    },
    total=False,
)

class SetAlarmStateInputAlarmTypeDef(
    _RequiredSetAlarmStateInputAlarmTypeDef, _OptionalSetAlarmStateInputAlarmTypeDef
):
    pass

_RequiredSetAlarmStateInputRequestTypeDef = TypedDict(
    "_RequiredSetAlarmStateInputRequestTypeDef",
    {
        "AlarmName": str,
        "StateValue": StateValueType,
        "StateReason": str,
    },
)
_OptionalSetAlarmStateInputRequestTypeDef = TypedDict(
    "_OptionalSetAlarmStateInputRequestTypeDef",
    {
        "StateReasonData": str,
    },
    total=False,
)

class SetAlarmStateInputRequestTypeDef(
    _RequiredSetAlarmStateInputRequestTypeDef, _OptionalSetAlarmStateInputRequestTypeDef
):
    pass

StartMetricStreamsInputRequestTypeDef = TypedDict(
    "StartMetricStreamsInputRequestTypeDef",
    {
        "Names": List[str],
    },
)

StatisticSetTypeDef = TypedDict(
    "StatisticSetTypeDef",
    {
        "SampleCount": float,
        "Sum": float,
        "Minimum": float,
        "Maximum": float,
    },
)

StopMetricStreamsInputRequestTypeDef = TypedDict(
    "StopMetricStreamsInputRequestTypeDef",
    {
        "Names": List[str],
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
