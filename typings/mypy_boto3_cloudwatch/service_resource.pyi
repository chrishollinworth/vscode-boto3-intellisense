"""
Type annotations for cloudwatch service ServiceResource

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_cloudwatch import CloudWatchServiceResource
    import mypy_boto3_cloudwatch.service_resource as cloudwatch_resources

    resource: CloudWatchServiceResource = boto3.resource("cloudwatch")

    my_alarm: cloudwatch_resources.Alarm = resource.Alarm(...)
    my_metric: cloudwatch_resources.Metric = resource.Metric(...)
```
"""
import sys
from datetime import datetime
from typing import Any, Iterator, List, Union

from boto3.resources.base import ResourceMeta
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

from .client import CloudWatchClient
from .literals import (
    AlarmTypeType,
    ComparisonOperatorType,
    HistoryItemTypeType,
    ScanByType,
    StandardUnitType,
    StateValueType,
    StatisticType,
)
from .type_defs import (
    DescribeAlarmHistoryOutputTypeDef,
    DimensionFilterTypeDef,
    DimensionTypeDef,
    GetMetricStatisticsOutputTypeDef,
    MetricDataQueryTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CloudWatchServiceResource",
    "Alarm",
    "Metric",
    "ServiceResourceAlarmsCollection",
    "ServiceResourceMetricsCollection",
    "MetricAlarmsCollection",
)

class ServiceResourceAlarmsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.ServiceResource.alarms)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#serviceresourcealarmscollection)
    """

    def all(self) -> "ServiceResourceAlarmsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """
    def filter(  # type: ignore
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
    ) -> "ServiceResourceAlarmsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """
    def delete(self) -> None:
        """
        Batch method.
        """
    def disable_actions(self) -> None:
        """
        Batch method.
        """
    def enable_actions(self) -> None:
        """
        Batch method.
        """
    def limit(self, count: int) -> "ServiceResourceAlarmsCollection":
        """
        Return at most this many Alarms.
        """
    def page_size(self, count: int) -> "ServiceResourceAlarmsCollection":
        """
        Fetch at most this many Alarms per service request.
        """
    def pages(self) -> Iterator[List["Alarm"]]:
        """
        A generator which yields pages of Alarms.
        """
    def __iter__(self) -> Iterator["Alarm"]:
        """
        A generator which yields Alarms.
        """

class ServiceResourceMetricsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.ServiceResource.metrics)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#serviceresourcemetricscollection)
    """

    def all(self) -> "ServiceResourceMetricsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """
    def filter(  # type: ignore
        self,
        *,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List["DimensionFilterTypeDef"] = None,
        NextToken: str = None,
        RecentlyActive: Literal["PT3H"] = None
    ) -> "ServiceResourceMetricsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """
    def limit(self, count: int) -> "ServiceResourceMetricsCollection":
        """
        Return at most this many Metrics.
        """
    def page_size(self, count: int) -> "ServiceResourceMetricsCollection":
        """
        Fetch at most this many Metrics per service request.
        """
    def pages(self) -> Iterator[List["Metric"]]:
        """
        A generator which yields pages of Metrics.
        """
    def __iter__(self) -> Iterator["Metric"]:
        """
        A generator which yields Metrics.
        """

class MetricAlarmsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Metric.alarms)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#metricalarmscollection)
    """

    def all(self) -> "MetricAlarmsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """
    def filter(  # type: ignore
        self,
        *,
        Statistic: StatisticType = None,
        ExtendedStatistic: str = None,
        Dimensions: List["DimensionTypeDef"] = None,
        Period: int = None,
        Unit: StandardUnitType = None
    ) -> "MetricAlarmsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """
    def delete(self) -> None:
        """
        Batch method.
        """
    def disable_actions(self) -> None:
        """
        Batch method.
        """
    def enable_actions(self) -> None:
        """
        Batch method.
        """
    def limit(self, count: int) -> "MetricAlarmsCollection":
        """
        Return at most this many Alarms.
        """
    def page_size(self, count: int) -> "MetricAlarmsCollection":
        """
        Fetch at most this many Alarms per service request.
        """
    def pages(self) -> Iterator[List["Alarm"]]:
        """
        A generator which yields pages of Alarms.
        """
    def __iter__(self) -> Iterator["Alarm"]:
        """
        A generator which yields Alarms.
        """

class Alarm(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Alarm)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#alarm)
    """

    alarm_name: str
    alarm_arn: str
    alarm_description: str
    alarm_configuration_updated_timestamp: datetime
    actions_enabled: bool
    ok_actions: List[Any]
    alarm_actions: List[Any]
    insufficient_data_actions: List[Any]
    state_value: str
    state_reason: str
    state_reason_data: str
    state_updated_timestamp: datetime
    metric_name: str
    namespace: str
    statistic: str
    extended_statistic: str
    dimensions: List[Any]
    period: int
    unit: str
    evaluation_periods: int
    datapoints_to_alarm: int
    threshold: float
    comparison_operator: str
    treat_missing_data: str
    evaluate_low_sample_count_percentile: str
    metrics: List[Any]
    threshold_metric_id: str
    name: str
    metric: "Metric"
    def delete(self) -> None:
        """
        Deletes the specified alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Alarm.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#alarmdelete-method)
        """
    def describe_history(
        self,
        *,
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Alarm.describe_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#alarmdescribe_history-method)
        """
    def disable_actions(self) -> None:
        """
        Disables the actions for the specified alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Alarm.disable_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#alarmdisable_actions-method)
        """
    def enable_actions(self) -> None:
        """
        Enables the actions for the specified alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Alarm.enable_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#alarmenable_actions-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Alarm.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#alarmget_available_subresources-method)
        """
    def load(self) -> None:
        """
        Calls :py:meth:`CloudWatch.Client.describe_alarms` to update the attributes of
        the Alarm resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Alarm.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#alarmload-method)
        """
    def reload(self) -> None:
        """
        Calls :py:meth:`CloudWatch.Client.describe_alarms` to update the attributes of
        the Alarm resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Alarm.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#alarmreload-method)
        """
    def set_state(
        self, *, StateValue: StateValueType, StateReason: str, StateReasonData: str = None
    ) -> None:
        """
        Temporarily sets the state of an alarm for testing purposes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Alarm.set_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#alarmset_state-method)
        """

_Alarm = Alarm

class Metric(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Metric)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#metric)
    """

    metric_name: str
    dimensions: List[Any]
    namespace: str
    name: str
    alarms: MetricAlarmsCollection
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Metric.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#metricget_available_subresources-method)
        """
    def get_statistics(
        self,
        *,
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Metric.get_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#metricget_statistics-method)
        """
    def load(self) -> None:
        """
        Calls :py:meth:`CloudWatch.Client.list_metrics` to update the attributes of the
        Metric resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Metric.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#metricload-method)
        """
    def put_alarm(
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
    ) -> _Alarm:
        """
        Creates or updates an alarm and associates it with the specified metric, metric
        math expression, or anomaly detection model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Metric.put_alarm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#metricput_alarm-method)
        """
    def put_data(self) -> None:
        """
        Publishes metric data points to Amazon CloudWatch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Metric.put_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#metricput_data-method)
        """
    def reload(self) -> None:
        """
        Calls :py:meth:`CloudWatch.Client.list_metrics` to update the attributes of the
        Metric resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.Metric.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#metricreload-method)
        """

_Metric = Metric

class CloudWatchResourceMeta(ResourceMeta):
    client: CloudWatchClient

class CloudWatchServiceResource(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.ServiceResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html)
    """

    meta: "CloudWatchResourceMeta"
    alarms: ServiceResourceAlarmsCollection
    metrics: ServiceResourceMetricsCollection
    def Alarm(self, name: str) -> _Alarm:
        """
        Creates a Alarm resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Alarm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#cloudwatchserviceresourcealarm-method)
        """
    def Metric(self, namespace: str, name: str) -> _Metric:
        """
        Creates a Metric resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Metric)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#cloudwatchserviceresourcemetric-method)
        """
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/cloudwatch.html#CloudWatch.ServiceResource.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#cloudwatchserviceresourceget_available_subresources-method)
        """
