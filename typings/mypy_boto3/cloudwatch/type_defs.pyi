"""
Type annotations for cloudwatch service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_cloudwatch.type_defs import AlarmHistoryItemTypeDef

    data: AlarmHistoryItemTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ActionsSuppressedByType,
    AlarmTypeType,
    AnomalyDetectorStateValueType,
    AnomalyDetectorTypeType,
    ComparisonOperatorType,
    HistoryItemTypeType,
    MetricStreamOutputFormatType,
    ScanByType,
    StandardUnitType,
    StateValueType,
    StatisticType,
    StatusCodeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AlarmHistoryItemTypeDef",
    "AnomalyDetectorConfigurationOutputTypeDef",
    "AnomalyDetectorConfigurationTypeDef",
    "AnomalyDetectorConfigurationUnionTypeDef",
    "AnomalyDetectorTypeDef",
    "CloudwatchEventDetailConfigurationTypeDef",
    "CloudwatchEventDetailTypeDef",
    "CloudwatchEventMetricStatsMetricTypeDef",
    "CloudwatchEventMetricStatsTypeDef",
    "CloudwatchEventMetricTypeDef",
    "CloudwatchEventStateTypeDef",
    "CloudwatchEventTypeDef",
    "CompositeAlarmTypeDef",
    "DashboardEntryTypeDef",
    "DashboardValidationMessageTypeDef",
    "DatapointTypeDef",
    "DeleteAlarmsInputTypeDef",
    "DeleteAnomalyDetectorInputTypeDef",
    "DeleteDashboardsInputTypeDef",
    "DeleteInsightRulesInputTypeDef",
    "DeleteInsightRulesOutputTypeDef",
    "DeleteMetricStreamInputTypeDef",
    "DescribeAlarmHistoryInputAlarmDescribeHistoryTypeDef",
    "DescribeAlarmHistoryInputPaginateTypeDef",
    "DescribeAlarmHistoryInputTypeDef",
    "DescribeAlarmHistoryOutputTypeDef",
    "DescribeAlarmsForMetricInputTypeDef",
    "DescribeAlarmsForMetricOutputTypeDef",
    "DescribeAlarmsInputPaginateTypeDef",
    "DescribeAlarmsInputTypeDef",
    "DescribeAlarmsInputWaitExtraTypeDef",
    "DescribeAlarmsInputWaitTypeDef",
    "DescribeAlarmsOutputTypeDef",
    "DescribeAnomalyDetectorsInputPaginateTypeDef",
    "DescribeAnomalyDetectorsInputTypeDef",
    "DescribeAnomalyDetectorsOutputTypeDef",
    "DescribeInsightRulesInputTypeDef",
    "DescribeInsightRulesOutputTypeDef",
    "DimensionFilterTypeDef",
    "DimensionTypeDef",
    "DisableAlarmActionsInputTypeDef",
    "DisableInsightRulesInputTypeDef",
    "DisableInsightRulesOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableAlarmActionsInputTypeDef",
    "EnableInsightRulesInputTypeDef",
    "EnableInsightRulesOutputTypeDef",
    "EntityMetricDataTypeDef",
    "EntityTypeDef",
    "GetDashboardInputTypeDef",
    "GetDashboardOutputTypeDef",
    "GetInsightRuleReportInputTypeDef",
    "GetInsightRuleReportOutputTypeDef",
    "GetMetricDataInputPaginateTypeDef",
    "GetMetricDataInputTypeDef",
    "GetMetricDataOutputTypeDef",
    "GetMetricStatisticsInputMetricGetStatisticsTypeDef",
    "GetMetricStatisticsInputTypeDef",
    "GetMetricStatisticsOutputTypeDef",
    "GetMetricStreamInputTypeDef",
    "GetMetricStreamOutputTypeDef",
    "GetMetricWidgetImageInputTypeDef",
    "GetMetricWidgetImageOutputTypeDef",
    "InsightRuleContributorDatapointTypeDef",
    "InsightRuleContributorTypeDef",
    "InsightRuleMetricDatapointTypeDef",
    "InsightRuleTypeDef",
    "LabelOptionsTypeDef",
    "ListDashboardsInputPaginateTypeDef",
    "ListDashboardsInputTypeDef",
    "ListDashboardsOutputTypeDef",
    "ListManagedInsightRulesInputTypeDef",
    "ListManagedInsightRulesOutputTypeDef",
    "ListMetricStreamsInputTypeDef",
    "ListMetricStreamsOutputTypeDef",
    "ListMetricsInputPaginateTypeDef",
    "ListMetricsInputTypeDef",
    "ListMetricsOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ManagedRuleDescriptionTypeDef",
    "ManagedRuleStateTypeDef",
    "ManagedRuleTypeDef",
    "MessageDataTypeDef",
    "MetricAlarmTypeDef",
    "MetricCharacteristicsTypeDef",
    "MetricDataQueryAlarmTypeDef",
    "MetricDataQueryOutputTypeDef",
    "MetricDataQueryTypeDef",
    "MetricDataQueryUnionTypeDef",
    "MetricDataResultTypeDef",
    "MetricDatumTypeDef",
    "MetricMathAnomalyDetectorOutputTypeDef",
    "MetricMathAnomalyDetectorTypeDef",
    "MetricMathAnomalyDetectorUnionTypeDef",
    "MetricOutputTypeDef",
    "MetricStatAlarmTypeDef",
    "MetricStatOutputTypeDef",
    "MetricStatTypeDef",
    "MetricStatUnionTypeDef",
    "MetricStreamEntryTypeDef",
    "MetricStreamFilterOutputTypeDef",
    "MetricStreamFilterTypeDef",
    "MetricStreamFilterUnionTypeDef",
    "MetricStreamStatisticsConfigurationOutputTypeDef",
    "MetricStreamStatisticsConfigurationTypeDef",
    "MetricStreamStatisticsConfigurationUnionTypeDef",
    "MetricStreamStatisticsMetricTypeDef",
    "MetricTypeDef",
    "MetricUnionTypeDef",
    "PaginatorConfigTypeDef",
    "PartialFailureTypeDef",
    "PutAnomalyDetectorInputTypeDef",
    "PutCompositeAlarmInputTypeDef",
    "PutDashboardInputTypeDef",
    "PutDashboardOutputTypeDef",
    "PutInsightRuleInputTypeDef",
    "PutManagedInsightRulesInputTypeDef",
    "PutManagedInsightRulesOutputTypeDef",
    "PutMetricAlarmInputMetricPutAlarmTypeDef",
    "PutMetricAlarmInputTypeDef",
    "PutMetricDataInputMetricPutDataTypeDef",
    "PutMetricDataInputTypeDef",
    "PutMetricStreamInputTypeDef",
    "PutMetricStreamOutputTypeDef",
    "RangeOutputTypeDef",
    "RangeTypeDef",
    "ResponseMetadataTypeDef",
    "SetAlarmStateInputAlarmSetStateTypeDef",
    "SetAlarmStateInputTypeDef",
    "SingleMetricAnomalyDetectorOutputTypeDef",
    "SingleMetricAnomalyDetectorTypeDef",
    "SingleMetricAnomalyDetectorUnionTypeDef",
    "StartMetricStreamsInputTypeDef",
    "StatisticSetTypeDef",
    "StopMetricStreamsInputTypeDef",
    "TagResourceInputTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "UntagResourceInputTypeDef",
    "WaiterConfigTypeDef",
)

class AlarmHistoryItemTypeDef(TypedDict):
    AlarmName: NotRequired[str]
    AlarmType: NotRequired[AlarmTypeType]
    Timestamp: NotRequired[datetime]
    HistoryItemType: NotRequired[HistoryItemTypeType]
    HistorySummary: NotRequired[str]
    HistoryData: NotRequired[str]

class RangeOutputTypeDef(TypedDict):
    StartTime: datetime
    EndTime: datetime

class DimensionTypeDef(TypedDict):
    Name: str
    Value: str

class MetricCharacteristicsTypeDef(TypedDict):
    PeriodicSpikes: NotRequired[bool]

class CloudwatchEventStateTypeDef(TypedDict):
    timestamp: str
    value: str
    reason: NotRequired[str]
    reasonData: NotRequired[str]
    actionsSuppressedBy: NotRequired[str]
    actionsSuppressedReason: NotRequired[str]

class CloudwatchEventMetricStatsMetricTypeDef(TypedDict):
    metricName: str
    namespace: str
    dimensions: Dict[str, str]

class CompositeAlarmTypeDef(TypedDict):
    ActionsEnabled: NotRequired[bool]
    AlarmActions: NotRequired[List[str]]
    AlarmArn: NotRequired[str]
    AlarmConfigurationUpdatedTimestamp: NotRequired[datetime]
    AlarmDescription: NotRequired[str]
    AlarmName: NotRequired[str]
    AlarmRule: NotRequired[str]
    InsufficientDataActions: NotRequired[List[str]]
    OKActions: NotRequired[List[str]]
    StateReason: NotRequired[str]
    StateReasonData: NotRequired[str]
    StateUpdatedTimestamp: NotRequired[datetime]
    StateValue: NotRequired[StateValueType]
    StateTransitionedTimestamp: NotRequired[datetime]
    ActionsSuppressedBy: NotRequired[ActionsSuppressedByType]
    ActionsSuppressedReason: NotRequired[str]
    ActionsSuppressor: NotRequired[str]
    ActionsSuppressorWaitPeriod: NotRequired[int]
    ActionsSuppressorExtensionPeriod: NotRequired[int]

class DashboardEntryTypeDef(TypedDict):
    DashboardName: NotRequired[str]
    DashboardArn: NotRequired[str]
    LastModified: NotRequired[datetime]
    Size: NotRequired[int]

class DashboardValidationMessageTypeDef(TypedDict):
    DataPath: NotRequired[str]
    Message: NotRequired[str]

class DatapointTypeDef(TypedDict):
    Timestamp: NotRequired[datetime]
    SampleCount: NotRequired[float]
    Average: NotRequired[float]
    Sum: NotRequired[float]
    Minimum: NotRequired[float]
    Maximum: NotRequired[float]
    Unit: NotRequired[StandardUnitType]
    ExtendedStatistics: NotRequired[Dict[str, float]]

class DeleteAlarmsInputTypeDef(TypedDict):
    AlarmNames: Sequence[str]

class DeleteDashboardsInputTypeDef(TypedDict):
    DashboardNames: Sequence[str]

class DeleteInsightRulesInputTypeDef(TypedDict):
    RuleNames: Sequence[str]

class PartialFailureTypeDef(TypedDict):
    FailureResource: NotRequired[str]
    ExceptionType: NotRequired[str]
    FailureCode: NotRequired[str]
    FailureDescription: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteMetricStreamInputTypeDef(TypedDict):
    Name: str

TimestampTypeDef = Union[datetime, str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeAlarmsInputTypeDef(TypedDict):
    AlarmNames: NotRequired[Sequence[str]]
    AlarmNamePrefix: NotRequired[str]
    AlarmTypes: NotRequired[Sequence[AlarmTypeType]]
    ChildrenOfAlarmName: NotRequired[str]
    ParentsOfAlarmName: NotRequired[str]
    StateValue: NotRequired[StateValueType]
    ActionPrefix: NotRequired[str]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class DescribeInsightRulesInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class InsightRuleTypeDef(TypedDict):
    Name: str
    State: str
    Schema: str
    Definition: str
    ManagedRule: NotRequired[bool]

class DimensionFilterTypeDef(TypedDict):
    Name: str
    Value: NotRequired[str]

class DisableAlarmActionsInputTypeDef(TypedDict):
    AlarmNames: Sequence[str]

class DisableInsightRulesInputTypeDef(TypedDict):
    RuleNames: Sequence[str]

class EnableAlarmActionsInputTypeDef(TypedDict):
    AlarmNames: Sequence[str]

class EnableInsightRulesInputTypeDef(TypedDict):
    RuleNames: Sequence[str]

class EntityTypeDef(TypedDict):
    KeyAttributes: NotRequired[Mapping[str, str]]
    Attributes: NotRequired[Mapping[str, str]]

class GetDashboardInputTypeDef(TypedDict):
    DashboardName: str

class InsightRuleMetricDatapointTypeDef(TypedDict):
    Timestamp: datetime
    UniqueContributors: NotRequired[float]
    MaxContributorValue: NotRequired[float]
    SampleCount: NotRequired[float]
    Average: NotRequired[float]
    Sum: NotRequired[float]
    Minimum: NotRequired[float]
    Maximum: NotRequired[float]

class LabelOptionsTypeDef(TypedDict):
    Timezone: NotRequired[str]

class MessageDataTypeDef(TypedDict):
    Code: NotRequired[str]
    Value: NotRequired[str]

class GetMetricStreamInputTypeDef(TypedDict):
    Name: str

class MetricStreamFilterOutputTypeDef(TypedDict):
    Namespace: NotRequired[str]
    MetricNames: NotRequired[List[str]]

class GetMetricWidgetImageInputTypeDef(TypedDict):
    MetricWidget: str
    OutputFormat: NotRequired[str]

class InsightRuleContributorDatapointTypeDef(TypedDict):
    Timestamp: datetime
    ApproximateValue: float

class ListDashboardsInputTypeDef(TypedDict):
    DashboardNamePrefix: NotRequired[str]
    NextToken: NotRequired[str]

class ListManagedInsightRulesInputTypeDef(TypedDict):
    ResourceARN: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListMetricStreamsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class MetricStreamEntryTypeDef(TypedDict):
    Arn: NotRequired[str]
    CreationDate: NotRequired[datetime]
    LastUpdateDate: NotRequired[datetime]
    Name: NotRequired[str]
    FirehoseArn: NotRequired[str]
    State: NotRequired[str]
    OutputFormat: NotRequired[MetricStreamOutputFormatType]

class ListTagsForResourceInputTypeDef(TypedDict):
    ResourceARN: str

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class ManagedRuleStateTypeDef(TypedDict):
    RuleName: str
    State: str

class StatisticSetTypeDef(TypedDict):
    SampleCount: float
    Sum: float
    Minimum: float
    Maximum: float

class MetricStreamFilterTypeDef(TypedDict):
    Namespace: NotRequired[str]
    MetricNames: NotRequired[Sequence[str]]

class MetricStreamStatisticsMetricTypeDef(TypedDict):
    Namespace: str
    MetricName: str

class PutDashboardInputTypeDef(TypedDict):
    DashboardName: str
    DashboardBody: str

class SetAlarmStateInputAlarmSetStateTypeDef(TypedDict):
    StateValue: StateValueType
    StateReason: str
    StateReasonData: NotRequired[str]

class SetAlarmStateInputTypeDef(TypedDict):
    AlarmName: str
    StateValue: StateValueType
    StateReason: str
    StateReasonData: NotRequired[str]

class StartMetricStreamsInputTypeDef(TypedDict):
    Names: Sequence[str]

class StopMetricStreamsInputTypeDef(TypedDict):
    Names: Sequence[str]

class UntagResourceInputTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class AnomalyDetectorConfigurationOutputTypeDef(TypedDict):
    ExcludedTimeRanges: NotRequired[List[RangeOutputTypeDef]]
    MetricTimezone: NotRequired[str]

class DescribeAlarmsForMetricInputTypeDef(TypedDict):
    MetricName: str
    Namespace: str
    Statistic: NotRequired[StatisticType]
    ExtendedStatistic: NotRequired[str]
    Dimensions: NotRequired[Sequence[DimensionTypeDef]]
    Period: NotRequired[int]
    Unit: NotRequired[StandardUnitType]

class DescribeAnomalyDetectorsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Namespace: NotRequired[str]
    MetricName: NotRequired[str]
    Dimensions: NotRequired[Sequence[DimensionTypeDef]]
    AnomalyDetectorTypes: NotRequired[Sequence[AnomalyDetectorTypeType]]

class MetricOutputTypeDef(TypedDict):
    Namespace: NotRequired[str]
    MetricName: NotRequired[str]
    Dimensions: NotRequired[List[DimensionTypeDef]]

class MetricTypeDef(TypedDict):
    Namespace: NotRequired[str]
    MetricName: NotRequired[str]
    Dimensions: NotRequired[Sequence[DimensionTypeDef]]

class SingleMetricAnomalyDetectorOutputTypeDef(TypedDict):
    AccountId: NotRequired[str]
    Namespace: NotRequired[str]
    MetricName: NotRequired[str]
    Dimensions: NotRequired[List[DimensionTypeDef]]
    Stat: NotRequired[str]

class SingleMetricAnomalyDetectorTypeDef(TypedDict):
    AccountId: NotRequired[str]
    Namespace: NotRequired[str]
    MetricName: NotRequired[str]
    Dimensions: NotRequired[Sequence[DimensionTypeDef]]
    Stat: NotRequired[str]

class CloudwatchEventMetricStatsTypeDef(TypedDict):
    period: str
    stat: str
    metric: NotRequired[CloudwatchEventMetricStatsMetricTypeDef]

class DeleteInsightRulesOutputTypeDef(TypedDict):
    Failures: List[PartialFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAlarmHistoryOutputTypeDef(TypedDict):
    AlarmHistoryItems: List[AlarmHistoryItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DisableInsightRulesOutputTypeDef(TypedDict):
    Failures: List[PartialFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class EnableInsightRulesOutputTypeDef(TypedDict):
    Failures: List[PartialFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDashboardOutputTypeDef(TypedDict):
    DashboardArn: str
    DashboardBody: str
    DashboardName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMetricStatisticsOutputTypeDef(TypedDict):
    Label: str
    Datapoints: List[DatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMetricWidgetImageOutputTypeDef(TypedDict):
    MetricWidgetImage: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class ListDashboardsOutputTypeDef(TypedDict):
    DashboardEntries: List[DashboardEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutDashboardOutputTypeDef(TypedDict):
    DashboardValidationMessages: List[DashboardValidationMessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutManagedInsightRulesOutputTypeDef(TypedDict):
    Failures: List[PartialFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutMetricStreamOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAlarmHistoryInputAlarmDescribeHistoryTypeDef(TypedDict):
    AlarmTypes: NotRequired[Sequence[AlarmTypeType]]
    HistoryItemType: NotRequired[HistoryItemTypeType]
    StartDate: NotRequired[TimestampTypeDef]
    EndDate: NotRequired[TimestampTypeDef]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]
    ScanBy: NotRequired[ScanByType]

class DescribeAlarmHistoryInputTypeDef(TypedDict):
    AlarmName: NotRequired[str]
    AlarmTypes: NotRequired[Sequence[AlarmTypeType]]
    HistoryItemType: NotRequired[HistoryItemTypeType]
    StartDate: NotRequired[TimestampTypeDef]
    EndDate: NotRequired[TimestampTypeDef]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]
    ScanBy: NotRequired[ScanByType]

class GetInsightRuleReportInputTypeDef(TypedDict):
    RuleName: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Period: int
    MaxContributorCount: NotRequired[int]
    Metrics: NotRequired[Sequence[str]]
    OrderBy: NotRequired[str]

class GetMetricStatisticsInputMetricGetStatisticsTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Period: int
    Dimensions: NotRequired[Sequence[DimensionTypeDef]]
    Statistics: NotRequired[Sequence[StatisticType]]
    ExtendedStatistics: NotRequired[Sequence[str]]
    Unit: NotRequired[StandardUnitType]

class GetMetricStatisticsInputTypeDef(TypedDict):
    Namespace: str
    MetricName: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Period: int
    Dimensions: NotRequired[Sequence[DimensionTypeDef]]
    Statistics: NotRequired[Sequence[StatisticType]]
    ExtendedStatistics: NotRequired[Sequence[str]]
    Unit: NotRequired[StandardUnitType]

class RangeTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef

class DescribeAlarmHistoryInputPaginateTypeDef(TypedDict):
    AlarmName: NotRequired[str]
    AlarmTypes: NotRequired[Sequence[AlarmTypeType]]
    HistoryItemType: NotRequired[HistoryItemTypeType]
    StartDate: NotRequired[TimestampTypeDef]
    EndDate: NotRequired[TimestampTypeDef]
    ScanBy: NotRequired[ScanByType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeAlarmsInputPaginateTypeDef(TypedDict):
    AlarmNames: NotRequired[Sequence[str]]
    AlarmNamePrefix: NotRequired[str]
    AlarmTypes: NotRequired[Sequence[AlarmTypeType]]
    ChildrenOfAlarmName: NotRequired[str]
    ParentsOfAlarmName: NotRequired[str]
    StateValue: NotRequired[StateValueType]
    ActionPrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeAnomalyDetectorsInputPaginateTypeDef(TypedDict):
    Namespace: NotRequired[str]
    MetricName: NotRequired[str]
    Dimensions: NotRequired[Sequence[DimensionTypeDef]]
    AnomalyDetectorTypes: NotRequired[Sequence[AnomalyDetectorTypeType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDashboardsInputPaginateTypeDef(TypedDict):
    DashboardNamePrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeAlarmsInputWaitExtraTypeDef(TypedDict):
    AlarmNames: NotRequired[Sequence[str]]
    AlarmNamePrefix: NotRequired[str]
    AlarmTypes: NotRequired[Sequence[AlarmTypeType]]
    ChildrenOfAlarmName: NotRequired[str]
    ParentsOfAlarmName: NotRequired[str]
    StateValue: NotRequired[StateValueType]
    ActionPrefix: NotRequired[str]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeAlarmsInputWaitTypeDef(TypedDict):
    AlarmNames: NotRequired[Sequence[str]]
    AlarmNamePrefix: NotRequired[str]
    AlarmTypes: NotRequired[Sequence[AlarmTypeType]]
    ChildrenOfAlarmName: NotRequired[str]
    ParentsOfAlarmName: NotRequired[str]
    StateValue: NotRequired[StateValueType]
    ActionPrefix: NotRequired[str]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeInsightRulesOutputTypeDef(TypedDict):
    InsightRules: List[InsightRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListMetricsInputPaginateTypeDef(TypedDict):
    Namespace: NotRequired[str]
    MetricName: NotRequired[str]
    Dimensions: NotRequired[Sequence[DimensionFilterTypeDef]]
    RecentlyActive: NotRequired[Literal["PT3H"]]
    IncludeLinkedAccounts: NotRequired[bool]
    OwningAccount: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMetricsInputTypeDef(TypedDict):
    Namespace: NotRequired[str]
    MetricName: NotRequired[str]
    Dimensions: NotRequired[Sequence[DimensionFilterTypeDef]]
    NextToken: NotRequired[str]
    RecentlyActive: NotRequired[Literal["PT3H"]]
    IncludeLinkedAccounts: NotRequired[bool]
    OwningAccount: NotRequired[str]

class MetricDataResultTypeDef(TypedDict):
    Id: NotRequired[str]
    Label: NotRequired[str]
    Timestamps: NotRequired[List[datetime]]
    Values: NotRequired[List[float]]
    StatusCode: NotRequired[StatusCodeType]
    Messages: NotRequired[List[MessageDataTypeDef]]

class InsightRuleContributorTypeDef(TypedDict):
    Keys: List[str]
    ApproximateAggregateValue: float
    Datapoints: List[InsightRuleContributorDatapointTypeDef]

class ListMetricStreamsOutputTypeDef(TypedDict):
    Entries: List[MetricStreamEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceOutputTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ManagedRuleTypeDef(TypedDict):
    TemplateName: str
    ResourceARN: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class PutCompositeAlarmInputTypeDef(TypedDict):
    AlarmName: str
    AlarmRule: str
    ActionsEnabled: NotRequired[bool]
    AlarmActions: NotRequired[Sequence[str]]
    AlarmDescription: NotRequired[str]
    InsufficientDataActions: NotRequired[Sequence[str]]
    OKActions: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ActionsSuppressor: NotRequired[str]
    ActionsSuppressorWaitPeriod: NotRequired[int]
    ActionsSuppressorExtensionPeriod: NotRequired[int]

class PutInsightRuleInputTypeDef(TypedDict):
    RuleName: str
    RuleDefinition: str
    RuleState: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class TagResourceInputTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class ManagedRuleDescriptionTypeDef(TypedDict):
    TemplateName: NotRequired[str]
    ResourceARN: NotRequired[str]
    RuleState: NotRequired[ManagedRuleStateTypeDef]

class MetricDatumTypeDef(TypedDict):
    MetricName: str
    Dimensions: NotRequired[Sequence[DimensionTypeDef]]
    Timestamp: NotRequired[TimestampTypeDef]
    Value: NotRequired[float]
    StatisticValues: NotRequired[StatisticSetTypeDef]
    Values: NotRequired[Sequence[float]]
    Counts: NotRequired[Sequence[float]]
    Unit: NotRequired[StandardUnitType]
    StorageResolution: NotRequired[int]

MetricStreamFilterUnionTypeDef = Union[MetricStreamFilterTypeDef, MetricStreamFilterOutputTypeDef]

class MetricStreamStatisticsConfigurationOutputTypeDef(TypedDict):
    IncludeMetrics: List[MetricStreamStatisticsMetricTypeDef]
    AdditionalStatistics: List[str]

class MetricStreamStatisticsConfigurationTypeDef(TypedDict):
    IncludeMetrics: Sequence[MetricStreamStatisticsMetricTypeDef]
    AdditionalStatistics: Sequence[str]

class ListMetricsOutputTypeDef(TypedDict):
    Metrics: List[MetricOutputTypeDef]
    OwningAccounts: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class MetricStatOutputTypeDef(TypedDict):
    Metric: MetricOutputTypeDef
    Period: int
    Stat: str
    Unit: NotRequired[StandardUnitType]

MetricUnionTypeDef = Union[MetricTypeDef, MetricOutputTypeDef]
SingleMetricAnomalyDetectorUnionTypeDef = Union[
    SingleMetricAnomalyDetectorTypeDef, SingleMetricAnomalyDetectorOutputTypeDef
]
CloudwatchEventMetricTypeDef = TypedDict(
    "CloudwatchEventMetricTypeDef",
    {
        "id": str,
        "returnData": bool,
        "metricStat": NotRequired[CloudwatchEventMetricStatsTypeDef],
        "expression": NotRequired[str],
        "label": NotRequired[str],
        "period": NotRequired[int],
    },
)

class AnomalyDetectorConfigurationTypeDef(TypedDict):
    ExcludedTimeRanges: NotRequired[Sequence[RangeTypeDef]]
    MetricTimezone: NotRequired[str]

class GetMetricDataOutputTypeDef(TypedDict):
    MetricDataResults: List[MetricDataResultTypeDef]
    Messages: List[MessageDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetInsightRuleReportOutputTypeDef(TypedDict):
    KeyLabels: List[str]
    AggregationStatistic: str
    AggregateValue: float
    ApproximateUniqueCount: int
    Contributors: List[InsightRuleContributorTypeDef]
    MetricDatapoints: List[InsightRuleMetricDatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutManagedInsightRulesInputTypeDef(TypedDict):
    ManagedRules: Sequence[ManagedRuleTypeDef]

class ListManagedInsightRulesOutputTypeDef(TypedDict):
    ManagedRules: List[ManagedRuleDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class EntityMetricDataTypeDef(TypedDict):
    Entity: NotRequired[EntityTypeDef]
    MetricData: NotRequired[Sequence[MetricDatumTypeDef]]

class GetMetricStreamOutputTypeDef(TypedDict):
    Arn: str
    Name: str
    IncludeFilters: List[MetricStreamFilterOutputTypeDef]
    ExcludeFilters: List[MetricStreamFilterOutputTypeDef]
    FirehoseArn: str
    RoleArn: str
    State: str
    CreationDate: datetime
    LastUpdateDate: datetime
    OutputFormat: MetricStreamOutputFormatType
    StatisticsConfigurations: List[MetricStreamStatisticsConfigurationOutputTypeDef]
    IncludeLinkedAccountsMetrics: bool
    ResponseMetadata: ResponseMetadataTypeDef

MetricStreamStatisticsConfigurationUnionTypeDef = Union[
    MetricStreamStatisticsConfigurationTypeDef, MetricStreamStatisticsConfigurationOutputTypeDef
]

class MetricDataQueryOutputTypeDef(TypedDict):
    Id: str
    MetricStat: NotRequired[MetricStatOutputTypeDef]
    Expression: NotRequired[str]
    Label: NotRequired[str]
    ReturnData: NotRequired[bool]
    Period: NotRequired[int]
    AccountId: NotRequired[str]

class MetricStatTypeDef(TypedDict):
    Metric: MetricUnionTypeDef
    Period: int
    Stat: str
    Unit: NotRequired[StandardUnitType]

CloudwatchEventDetailConfigurationTypeDef = TypedDict(
    "CloudwatchEventDetailConfigurationTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
        "metrics": NotRequired[List[CloudwatchEventMetricTypeDef]],
        "actionsSuppressor": NotRequired[str],
        "actionsSuppressorWaitPeriod": NotRequired[int],
        "actionsSuppressorExtensionPeriod": NotRequired[int],
        "threshold": NotRequired[int],
        "evaluationPeriods": NotRequired[int],
        "alarmRule": NotRequired[str],
        "alarmName": NotRequired[str],
        "treatMissingData": NotRequired[str],
        "comparisonOperator": NotRequired[str],
        "timestamp": NotRequired[str],
        "actionsEnabled": NotRequired[bool],
        "okActions": NotRequired[List[str]],
        "alarmActions": NotRequired[List[str]],
        "insufficientDataActions": NotRequired[List[str]],
    },
)
AnomalyDetectorConfigurationUnionTypeDef = Union[
    AnomalyDetectorConfigurationTypeDef, AnomalyDetectorConfigurationOutputTypeDef
]

class PutMetricDataInputMetricPutDataTypeDef(TypedDict):
    EntityMetricData: NotRequired[Sequence[EntityMetricDataTypeDef]]
    StrictEntityValidation: NotRequired[bool]

class PutMetricDataInputTypeDef(TypedDict):
    Namespace: str
    MetricData: NotRequired[Sequence[MetricDatumTypeDef]]
    EntityMetricData: NotRequired[Sequence[EntityMetricDataTypeDef]]
    StrictEntityValidation: NotRequired[bool]

class PutMetricStreamInputTypeDef(TypedDict):
    Name: str
    FirehoseArn: str
    RoleArn: str
    OutputFormat: MetricStreamOutputFormatType
    IncludeFilters: NotRequired[Sequence[MetricStreamFilterUnionTypeDef]]
    ExcludeFilters: NotRequired[Sequence[MetricStreamFilterUnionTypeDef]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    StatisticsConfigurations: NotRequired[Sequence[MetricStreamStatisticsConfigurationUnionTypeDef]]
    IncludeLinkedAccountsMetrics: NotRequired[bool]

class MetricAlarmTypeDef(TypedDict):
    AlarmName: NotRequired[str]
    AlarmArn: NotRequired[str]
    AlarmDescription: NotRequired[str]
    AlarmConfigurationUpdatedTimestamp: NotRequired[datetime]
    ActionsEnabled: NotRequired[bool]
    OKActions: NotRequired[List[str]]
    AlarmActions: NotRequired[List[str]]
    InsufficientDataActions: NotRequired[List[str]]
    StateValue: NotRequired[StateValueType]
    StateReason: NotRequired[str]
    StateReasonData: NotRequired[str]
    StateUpdatedTimestamp: NotRequired[datetime]
    MetricName: NotRequired[str]
    Namespace: NotRequired[str]
    Statistic: NotRequired[StatisticType]
    ExtendedStatistic: NotRequired[str]
    Dimensions: NotRequired[List[DimensionTypeDef]]
    Period: NotRequired[int]
    Unit: NotRequired[StandardUnitType]
    EvaluationPeriods: NotRequired[int]
    DatapointsToAlarm: NotRequired[int]
    Threshold: NotRequired[float]
    ComparisonOperator: NotRequired[ComparisonOperatorType]
    TreatMissingData: NotRequired[str]
    EvaluateLowSampleCountPercentile: NotRequired[str]
    Metrics: NotRequired[List[MetricDataQueryOutputTypeDef]]
    ThresholdMetricId: NotRequired[str]
    EvaluationState: NotRequired[Literal["PARTIAL_DATA"]]
    StateTransitionedTimestamp: NotRequired[datetime]

class MetricMathAnomalyDetectorOutputTypeDef(TypedDict):
    MetricDataQueries: NotRequired[List[MetricDataQueryOutputTypeDef]]

MetricStatUnionTypeDef = Union[MetricStatTypeDef, MetricStatOutputTypeDef]

class CloudwatchEventDetailTypeDef(TypedDict):
    alarmName: str
    state: CloudwatchEventStateTypeDef
    operation: NotRequired[str]
    configuration: NotRequired[CloudwatchEventDetailConfigurationTypeDef]
    previousConfiguration: NotRequired[CloudwatchEventDetailConfigurationTypeDef]
    previousState: NotRequired[CloudwatchEventStateTypeDef]

class DescribeAlarmsForMetricOutputTypeDef(TypedDict):
    MetricAlarms: List[MetricAlarmTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAlarmsOutputTypeDef(TypedDict):
    CompositeAlarms: List[CompositeAlarmTypeDef]
    MetricAlarms: List[MetricAlarmTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class MetricStatAlarmTypeDef(TypedDict):
    Metric: MetricAlarmTypeDef
    Period: int
    Stat: str
    Unit: NotRequired[StandardUnitType]

class AnomalyDetectorTypeDef(TypedDict):
    Namespace: NotRequired[str]
    MetricName: NotRequired[str]
    Dimensions: NotRequired[List[DimensionTypeDef]]
    Stat: NotRequired[str]
    Configuration: NotRequired[AnomalyDetectorConfigurationOutputTypeDef]
    StateValue: NotRequired[AnomalyDetectorStateValueType]
    MetricCharacteristics: NotRequired[MetricCharacteristicsTypeDef]
    SingleMetricAnomalyDetector: NotRequired[SingleMetricAnomalyDetectorOutputTypeDef]
    MetricMathAnomalyDetector: NotRequired[MetricMathAnomalyDetectorOutputTypeDef]

class MetricDataQueryTypeDef(TypedDict):
    Id: str
    MetricStat: NotRequired[MetricStatUnionTypeDef]
    Expression: NotRequired[str]
    Label: NotRequired[str]
    ReturnData: NotRequired[bool]
    Period: NotRequired[int]
    AccountId: NotRequired[str]

CloudwatchEventTypeDef = TypedDict(
    "CloudwatchEventTypeDef",
    {
        "version": str,
        "id": str,
        "detail-type": str,
        "source": str,
        "account": str,
        "time": str,
        "region": str,
        "resources": List[str],
        "detail": CloudwatchEventDetailTypeDef,
    },
)

class MetricDataQueryAlarmTypeDef(TypedDict):
    Id: str
    MetricStat: NotRequired[MetricStatAlarmTypeDef]
    Expression: NotRequired[str]
    Label: NotRequired[str]
    ReturnData: NotRequired[bool]
    Period: NotRequired[int]
    AccountId: NotRequired[str]

class DescribeAnomalyDetectorsOutputTypeDef(TypedDict):
    AnomalyDetectors: List[AnomalyDetectorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

MetricDataQueryUnionTypeDef = Union[MetricDataQueryTypeDef, MetricDataQueryOutputTypeDef]

class MetricMathAnomalyDetectorTypeDef(TypedDict):
    MetricDataQueries: NotRequired[Sequence[MetricDataQueryTypeDef]]

class GetMetricDataInputPaginateTypeDef(TypedDict):
    MetricDataQueries: Sequence[MetricDataQueryUnionTypeDef]
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    ScanBy: NotRequired[ScanByType]
    LabelOptions: NotRequired[LabelOptionsTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetMetricDataInputTypeDef(TypedDict):
    MetricDataQueries: Sequence[MetricDataQueryUnionTypeDef]
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    NextToken: NotRequired[str]
    ScanBy: NotRequired[ScanByType]
    MaxDatapoints: NotRequired[int]
    LabelOptions: NotRequired[LabelOptionsTypeDef]

class PutMetricAlarmInputMetricPutAlarmTypeDef(TypedDict):
    AlarmName: str
    EvaluationPeriods: int
    ComparisonOperator: ComparisonOperatorType
    AlarmDescription: NotRequired[str]
    ActionsEnabled: NotRequired[bool]
    OKActions: NotRequired[Sequence[str]]
    AlarmActions: NotRequired[Sequence[str]]
    InsufficientDataActions: NotRequired[Sequence[str]]
    Statistic: NotRequired[StatisticType]
    ExtendedStatistic: NotRequired[str]
    Dimensions: NotRequired[Sequence[DimensionTypeDef]]
    Period: NotRequired[int]
    Unit: NotRequired[StandardUnitType]
    DatapointsToAlarm: NotRequired[int]
    Threshold: NotRequired[float]
    TreatMissingData: NotRequired[str]
    EvaluateLowSampleCountPercentile: NotRequired[str]
    Metrics: NotRequired[Sequence[MetricDataQueryUnionTypeDef]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ThresholdMetricId: NotRequired[str]

class PutMetricAlarmInputTypeDef(TypedDict):
    AlarmName: str
    EvaluationPeriods: int
    ComparisonOperator: ComparisonOperatorType
    AlarmDescription: NotRequired[str]
    ActionsEnabled: NotRequired[bool]
    OKActions: NotRequired[Sequence[str]]
    AlarmActions: NotRequired[Sequence[str]]
    InsufficientDataActions: NotRequired[Sequence[str]]
    MetricName: NotRequired[str]
    Namespace: NotRequired[str]
    Statistic: NotRequired[StatisticType]
    ExtendedStatistic: NotRequired[str]
    Dimensions: NotRequired[Sequence[DimensionTypeDef]]
    Period: NotRequired[int]
    Unit: NotRequired[StandardUnitType]
    DatapointsToAlarm: NotRequired[int]
    Threshold: NotRequired[float]
    TreatMissingData: NotRequired[str]
    EvaluateLowSampleCountPercentile: NotRequired[str]
    Metrics: NotRequired[Sequence[MetricDataQueryUnionTypeDef]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ThresholdMetricId: NotRequired[str]

MetricMathAnomalyDetectorUnionTypeDef = Union[
    MetricMathAnomalyDetectorTypeDef, MetricMathAnomalyDetectorOutputTypeDef
]

class DeleteAnomalyDetectorInputTypeDef(TypedDict):
    Namespace: NotRequired[str]
    MetricName: NotRequired[str]
    Dimensions: NotRequired[Sequence[DimensionTypeDef]]
    Stat: NotRequired[str]
    SingleMetricAnomalyDetector: NotRequired[SingleMetricAnomalyDetectorUnionTypeDef]
    MetricMathAnomalyDetector: NotRequired[MetricMathAnomalyDetectorUnionTypeDef]

class PutAnomalyDetectorInputTypeDef(TypedDict):
    Namespace: NotRequired[str]
    MetricName: NotRequired[str]
    Dimensions: NotRequired[Sequence[DimensionTypeDef]]
    Stat: NotRequired[str]
    Configuration: NotRequired[AnomalyDetectorConfigurationUnionTypeDef]
    MetricCharacteristics: NotRequired[MetricCharacteristicsTypeDef]
    SingleMetricAnomalyDetector: NotRequired[SingleMetricAnomalyDetectorUnionTypeDef]
    MetricMathAnomalyDetector: NotRequired[MetricMathAnomalyDetectorUnionTypeDef]
