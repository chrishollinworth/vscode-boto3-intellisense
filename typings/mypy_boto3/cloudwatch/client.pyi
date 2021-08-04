"""
Type annotations for cloudwatch service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudwatch import CloudWatchClient

    client: CloudWatchClient = boto3.client("cloudwatch")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AlarmTypeType,
    ComparisonOperatorType,
    HistoryItemTypeType,
    MetricStreamOutputFormatType,
    ScanByType,
    StandardUnitType,
    StateValueType,
    StatisticType,
)
from .paginator import (
    DescribeAlarmHistoryPaginator,
    DescribeAlarmsPaginator,
    GetMetricDataPaginator,
    ListDashboardsPaginator,
    ListMetricsPaginator,
)
from .type_defs import (
    AnomalyDetectorConfigurationTypeDef,
    DeleteInsightRulesOutputTypeDef,
    DescribeAlarmHistoryOutputTypeDef,
    DescribeAlarmsForMetricOutputTypeDef,
    DescribeAlarmsOutputTypeDef,
    DescribeAnomalyDetectorsOutputTypeDef,
    DescribeInsightRulesOutputTypeDef,
    DimensionFilterTypeDef,
    DimensionTypeDef,
    DisableInsightRulesOutputTypeDef,
    EnableInsightRulesOutputTypeDef,
    GetDashboardOutputTypeDef,
    GetInsightRuleReportOutputTypeDef,
    GetMetricDataOutputTypeDef,
    GetMetricStatisticsOutputTypeDef,
    GetMetricStreamOutputTypeDef,
    GetMetricWidgetImageOutputTypeDef,
    LabelOptionsTypeDef,
    ListDashboardsOutputTypeDef,
    ListMetricsOutputTypeDef,
    ListMetricStreamsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    MetricDataQueryTypeDef,
    MetricDatumTypeDef,
    MetricStreamFilterTypeDef,
    PutDashboardOutputTypeDef,
    PutMetricStreamOutputTypeDef,
    TagTypeDef,
)
from .waiter import AlarmExistsWaiter, CompositeAlarmExistsWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CloudWatchClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    DashboardInvalidInputError: Type[BotocoreClientError]
    DashboardNotFoundError: Type[BotocoreClientError]
    InternalServiceFault: Type[BotocoreClientError]
    InvalidFormatFault: Type[BotocoreClientError]
    InvalidNextToken: Type[BotocoreClientError]
    InvalidParameterCombinationException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    LimitExceededFault: Type[BotocoreClientError]
    MissingRequiredParameterException: Type[BotocoreClientError]
    ResourceNotFound: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class CloudWatchClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        CloudWatchClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#can_paginate)
        """
    def delete_alarms(self, *, AlarmNames: List[str]) -> None:
        """
        Deletes the specified alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.delete_alarms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#delete_alarms)
        """
    def delete_anomaly_detector(
        self,
        *,
        Namespace: str,
        MetricName: str,
        Stat: str,
        Dimensions: List["DimensionTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Deletes the specified anomaly detection model from your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.delete_anomaly_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#delete_anomaly_detector)
        """
    def delete_dashboards(self, *, DashboardNames: List[str]) -> Dict[str, Any]:
        """
        Deletes all dashboards that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.delete_dashboards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#delete_dashboards)
        """
    def delete_insight_rules(self, *, RuleNames: List[str]) -> DeleteInsightRulesOutputTypeDef:
        """
        Permanently deletes the specified Contributor Insights rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.delete_insight_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#delete_insight_rules)
        """
    def delete_metric_stream(self, *, Name: str) -> Dict[str, Any]:
        """
        Permanently deletes the metric stream that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.delete_metric_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#delete_metric_stream)
        """
    def describe_alarm_history(
        self,
        *,
        AlarmName: str = None,
        AlarmTypes: List[AlarmTypeType] = None,
        HistoryItemType: HistoryItemTypeType = None,
        StartDate: Union[datetime, str] = None,
        EndDate: Union[datetime, str] = None,
        MaxRecords: int = None,
        NextToken: str = None,
        ScanBy: ScanByType = None
    ) -> DescribeAlarmHistoryOutputTypeDef:
        """
        Retrieves the history for the specified alarm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.describe_alarm_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#describe_alarm_history)
        """
    def describe_alarms(
        self,
        *,
        AlarmNames: List[str] = None,
        AlarmNamePrefix: str = None,
        AlarmTypes: List[AlarmTypeType] = None,
        ChildrenOfAlarmName: str = None,
        ParentsOfAlarmName: str = None,
        StateValue: StateValueType = None,
        ActionPrefix: str = None,
        MaxRecords: int = None,
        NextToken: str = None
    ) -> DescribeAlarmsOutputTypeDef:
        """
        Retrieves the specified alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.describe_alarms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#describe_alarms)
        """
    def describe_alarms_for_metric(
        self,
        *,
        MetricName: str,
        Namespace: str,
        Statistic: StatisticType = None,
        ExtendedStatistic: str = None,
        Dimensions: List["DimensionTypeDef"] = None,
        Period: int = None,
        Unit: StandardUnitType = None
    ) -> DescribeAlarmsForMetricOutputTypeDef:
        """
        Retrieves the alarms for the specified metric.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.describe_alarms_for_metric)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#describe_alarms_for_metric)
        """
    def describe_anomaly_detectors(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List["DimensionTypeDef"] = None
    ) -> DescribeAnomalyDetectorsOutputTypeDef:
        """
        Lists the anomaly detection models that you have created in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.describe_anomaly_detectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#describe_anomaly_detectors)
        """
    def describe_insight_rules(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> DescribeInsightRulesOutputTypeDef:
        """
        Returns a list of all the Contributor Insights rules in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.describe_insight_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#describe_insight_rules)
        """
    def disable_alarm_actions(self, *, AlarmNames: List[str]) -> None:
        """
        Disables the actions for the specified alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.disable_alarm_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#disable_alarm_actions)
        """
    def disable_insight_rules(self, *, RuleNames: List[str]) -> DisableInsightRulesOutputTypeDef:
        """
        Disables the specified Contributor Insights rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.disable_insight_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#disable_insight_rules)
        """
    def enable_alarm_actions(self, *, AlarmNames: List[str]) -> None:
        """
        Enables the actions for the specified alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.enable_alarm_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#enable_alarm_actions)
        """
    def enable_insight_rules(self, *, RuleNames: List[str]) -> EnableInsightRulesOutputTypeDef:
        """
        Enables the specified Contributor Insights rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.enable_insight_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#enable_insight_rules)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#generate_presigned_url)
        """
    def get_dashboard(self, *, DashboardName: str) -> GetDashboardOutputTypeDef:
        """
        Displays the details of the dashboard that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.get_dashboard)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#get_dashboard)
        """
    def get_insight_rule_report(
        self,
        *,
        RuleName: str,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        Period: int,
        MaxContributorCount: int = None,
        Metrics: List[str] = None,
        OrderBy: str = None
    ) -> GetInsightRuleReportOutputTypeDef:
        """
        This operation returns the time series data collected by a Contributor Insights
        rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.get_insight_rule_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#get_insight_rule_report)
        """
    def get_metric_data(
        self,
        *,
        MetricDataQueries: List["MetricDataQueryTypeDef"],
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        NextToken: str = None,
        ScanBy: ScanByType = None,
        MaxDatapoints: int = None,
        LabelOptions: "LabelOptionsTypeDef" = None
    ) -> GetMetricDataOutputTypeDef:
        """
        You can use the `GetMetricData` API to retrieve as many as 500 different metrics
        in a single request, with a total of as many as 100,800 data points.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#get_metric_data)
        """
    def get_metric_statistics(
        self,
        *,
        Namespace: str,
        MetricName: str,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        Period: int,
        Dimensions: List["DimensionTypeDef"] = None,
        Statistics: List[StatisticType] = None,
        ExtendedStatistics: List[str] = None,
        Unit: StandardUnitType = None
    ) -> GetMetricStatisticsOutputTypeDef:
        """
        Gets statistics for the specified metric.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#get_metric_statistics)
        """
    def get_metric_stream(self, *, Name: str) -> GetMetricStreamOutputTypeDef:
        """
        Returns information about the metric stream that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#get_metric_stream)
        """
    def get_metric_widget_image(
        self, *, MetricWidget: str, OutputFormat: str = None
    ) -> GetMetricWidgetImageOutputTypeDef:
        """
        You can use the `GetMetricWidgetImage` API to retrieve a snapshot graph of one
        or more Amazon CloudWatch metrics as a bitmap image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_widget_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#get_metric_widget_image)
        """
    def list_dashboards(
        self, *, DashboardNamePrefix: str = None, NextToken: str = None
    ) -> ListDashboardsOutputTypeDef:
        """
        Returns a list of the dashboards for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.list_dashboards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#list_dashboards)
        """
    def list_metric_streams(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListMetricStreamsOutputTypeDef:
        """
        Returns a list of metric streams in this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.list_metric_streams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#list_metric_streams)
        """
    def list_metrics(
        self,
        *,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List["DimensionFilterTypeDef"] = None,
        NextToken: str = None,
        RecentlyActive: Literal["PT3H"] = None
    ) -> ListMetricsOutputTypeDef:
        """
        List the specified metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.list_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#list_metrics)
        """
    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceOutputTypeDef:
        """
        Displays the tags associated with a CloudWatch resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#list_tags_for_resource)
        """
    def put_anomaly_detector(
        self,
        *,
        Namespace: str,
        MetricName: str,
        Stat: str,
        Dimensions: List["DimensionTypeDef"] = None,
        Configuration: "AnomalyDetectorConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Creates an anomaly detection model for a CloudWatch metric.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.put_anomaly_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#put_anomaly_detector)
        """
    def put_composite_alarm(
        self,
        *,
        AlarmName: str,
        AlarmRule: str,
        ActionsEnabled: bool = None,
        AlarmActions: List[str] = None,
        AlarmDescription: str = None,
        InsufficientDataActions: List[str] = None,
        OKActions: List[str] = None,
        Tags: List["TagTypeDef"] = None
    ) -> None:
        """
        Creates or updates a *composite alarm*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.put_composite_alarm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#put_composite_alarm)
        """
    def put_dashboard(self, *, DashboardName: str, DashboardBody: str) -> PutDashboardOutputTypeDef:
        """
        Creates a dashboard if it does not already exist, or updates an existing
        dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.put_dashboard)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#put_dashboard)
        """
    def put_insight_rule(
        self,
        *,
        RuleName: str,
        RuleDefinition: str,
        RuleState: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Creates a Contributor Insights rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.put_insight_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#put_insight_rule)
        """
    def put_metric_alarm(
        self,
        *,
        AlarmName: str,
        EvaluationPeriods: int,
        ComparisonOperator: ComparisonOperatorType,
        AlarmDescription: str = None,
        ActionsEnabled: bool = None,
        OKActions: List[str] = None,
        AlarmActions: List[str] = None,
        InsufficientDataActions: List[str] = None,
        MetricName: str = None,
        Namespace: str = None,
        Statistic: StatisticType = None,
        ExtendedStatistic: str = None,
        Dimensions: List["DimensionTypeDef"] = None,
        Period: int = None,
        Unit: StandardUnitType = None,
        DatapointsToAlarm: int = None,
        Threshold: float = None,
        TreatMissingData: str = None,
        EvaluateLowSampleCountPercentile: str = None,
        Metrics: List["MetricDataQueryTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        ThresholdMetricId: str = None
    ) -> None:
        """
        Creates or updates an alarm and associates it with the specified metric, metric
        math expression, or anomaly detection model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_alarm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#put_metric_alarm)
        """
    def put_metric_data(self, *, Namespace: str, MetricData: List["MetricDatumTypeDef"]) -> None:
        """
        Publishes metric data points to Amazon CloudWatch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#put_metric_data)
        """
    def put_metric_stream(
        self,
        *,
        Name: str,
        FirehoseArn: str,
        RoleArn: str,
        OutputFormat: MetricStreamOutputFormatType,
        IncludeFilters: List["MetricStreamFilterTypeDef"] = None,
        ExcludeFilters: List["MetricStreamFilterTypeDef"] = None,
        Tags: List["TagTypeDef"] = None
    ) -> PutMetricStreamOutputTypeDef:
        """
        Creates or updates a metric stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#put_metric_stream)
        """
    def set_alarm_state(
        self,
        *,
        AlarmName: str,
        StateValue: StateValueType,
        StateReason: str,
        StateReasonData: str = None
    ) -> None:
        """
        Temporarily sets the state of an alarm for testing purposes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.set_alarm_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#set_alarm_state)
        """
    def start_metric_streams(self, *, Names: List[str]) -> Dict[str, Any]:
        """
        Starts the streaming of metrics for one or more of your metric streams.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.start_metric_streams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#start_metric_streams)
        """
    def stop_metric_streams(self, *, Names: List[str]) -> Dict[str, Any]:
        """
        Stops the streaming of metrics for one or more of your metric streams.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.stop_metric_streams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#stop_metric_streams)
        """
    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified CloudWatch resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/client.html#untag_resource)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_alarm_history"]
    ) -> DescribeAlarmHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Paginator.DescribeAlarmHistory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators.html#describealarmhistorypaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_alarms"]) -> DescribeAlarmsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Paginator.DescribeAlarms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators.html#describealarmspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_metric_data"]) -> GetMetricDataPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Paginator.GetMetricData)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators.html#getmetricdatapaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_dashboards"]) -> ListDashboardsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Paginator.ListDashboards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators.html#listdashboardspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_metrics"]) -> ListMetricsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Paginator.ListMetrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/paginators.html#listmetricspaginator)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["alarm_exists"]) -> AlarmExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Waiter.AlarmExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/waiters.html#alarmexistswaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["composite_alarm_exists"]
    ) -> CompositeAlarmExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Waiter.CompositeAlarmExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/waiters.html#compositealarmexistswaiter)
        """
