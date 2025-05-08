"""
Type annotations for cloudwatch service ServiceResource.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cloudwatch.service_resource import CloudWatchServiceResource
    import mypy_boto3_cloudwatch.service_resource as cloudwatch_resources

    session = Session()
    resource: CloudWatchServiceResource = session.resource("cloudwatch")

    my_alarm: cloudwatch_resources.Alarm = resource.Alarm(...)
    my_metric: cloudwatch_resources.Metric = resource.Metric(...)
```
"""

from __future__ import annotations

import sys
from datetime import datetime

from boto3.resources.base import ResourceMeta, ServiceResource
from boto3.resources.collection import ResourceCollection

from .client import CloudWatchClient
from .literals import (
    AlarmTypeType,
    ComparisonOperatorType,
    StandardUnitType,
    StateValueType,
    StatisticType,
)
from .type_defs import (
    DescribeAlarmHistoryInputAlarmDescribeHistoryTypeDef,
    DescribeAlarmHistoryOutputTypeDef,
    DimensionFilterTypeDef,
    DimensionTypeDef,
    GetMetricStatisticsInputMetricGetStatisticsTypeDef,
    GetMetricStatisticsOutputTypeDef,
    MetricDataQueryAlarmTypeDef,
    PutMetricAlarmInputMetricPutAlarmTypeDef,
    PutMetricDataInputMetricPutDataTypeDef,
    SetAlarmStateInputAlarmSetStateTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import list as List
    from collections.abc import Iterator, Sequence
else:
    from typing import Iterator, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = (
    "Alarm",
    "CloudWatchServiceResource",
    "Metric",
    "MetricAlarmsCollection",
    "ServiceResourceAlarmsCollection",
    "ServiceResourceMetricsCollection",
)

class ServiceResourceAlarmsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/alarms.html#CloudWatch.ServiceResource.alarms)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#serviceresourcealarmscollection)
    """
    def all(self) -> ServiceResourceAlarmsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/alarms.html#CloudWatch.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#serviceresourcealarmscollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        AlarmNames: Sequence[str] = ...,
        AlarmNamePrefix: str = ...,
        AlarmTypes: Sequence[AlarmTypeType] = ...,
        ChildrenOfAlarmName: str = ...,
        ParentsOfAlarmName: str = ...,
        StateValue: StateValueType = ...,
        ActionPrefix: str = ...,
        MaxRecords: int = ...,
        NextToken: str = ...,
    ) -> ServiceResourceAlarmsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/alarms.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#serviceresourcealarmscollection)
        """

    def delete(self) -> None:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/alarms.html#delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#serviceresourcealarmscollection)
        """

    def disable_actions(self) -> None:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/alarms.html#disable_actions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#serviceresourcealarmscollection)
        """

    def enable_actions(self) -> None:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/alarms.html#enable_actions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#serviceresourcealarmscollection)
        """

    def limit(self, count: int) -> ServiceResourceAlarmsCollection:
        """
        Return at most this many Alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/alarms.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#serviceresourcealarmscollection)
        """

    def page_size(self, count: int) -> ServiceResourceAlarmsCollection:
        """
        Fetch at most this many Alarms per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/alarms.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#serviceresourcealarmscollection)
        """

    def pages(self) -> Iterator[List[Alarm]]:
        """
        A generator which yields pages of Alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/alarms.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#serviceresourcealarmscollection)
        """

    def __iter__(self) -> Iterator[Alarm]:
        """
        A generator which yields Alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/alarms.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#serviceresourcealarmscollection)
        """

class ServiceResourceMetricsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/metrics.html#CloudWatch.ServiceResource.metrics)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#serviceresourcemetricscollection)
    """
    def all(self) -> ServiceResourceMetricsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/metrics.html#CloudWatch.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#serviceresourcemetricscollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        Namespace: str = ...,
        MetricName: str = ...,
        Dimensions: Sequence[DimensionFilterTypeDef] = ...,
        NextToken: str = ...,
        RecentlyActive: Literal["PT3H"] = ...,
        IncludeLinkedAccounts: bool = ...,
        OwningAccount: str = ...,
    ) -> ServiceResourceMetricsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/metrics.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#serviceresourcemetricscollection)
        """

    def limit(self, count: int) -> ServiceResourceMetricsCollection:
        """
        Return at most this many Metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/metrics.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#serviceresourcemetricscollection)
        """

    def page_size(self, count: int) -> ServiceResourceMetricsCollection:
        """
        Fetch at most this many Metrics per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/metrics.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#serviceresourcemetricscollection)
        """

    def pages(self) -> Iterator[List[Metric]]:
        """
        A generator which yields pages of Metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/metrics.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#serviceresourcemetricscollection)
        """

    def __iter__(self) -> Iterator[Metric]:
        """
        A generator which yields Metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/metrics.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#serviceresourcemetricscollection)
        """

class MetricAlarmsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/metric/alarms.html#CloudWatch.Metric.alarms)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#metricalarms)
    """
    def all(self) -> MetricAlarmsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/metric/alarms.html#CloudWatch.Metric.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#metricalarms)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        Statistic: StatisticType = ...,
        ExtendedStatistic: str = ...,
        Dimensions: Sequence[DimensionTypeDef] = ...,
        Period: int = ...,
        Unit: StandardUnitType = ...,
    ) -> MetricAlarmsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/metric/alarms.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#metricalarms)
        """

    def delete(self) -> None:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/metric/alarms.html#delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#metricalarms)
        """

    def disable_actions(self) -> None:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/metric/alarms.html#disable_actions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#metricalarms)
        """

    def enable_actions(self) -> None:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/metric/alarms.html#enable_actions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#metricalarms)
        """

    def limit(self, count: int) -> MetricAlarmsCollection:
        """
        Return at most this many Alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/metric/alarms.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#metricalarms)
        """

    def page_size(self, count: int) -> MetricAlarmsCollection:
        """
        Fetch at most this many Alarms per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/metric/alarms.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#metricalarms)
        """

    def pages(self) -> Iterator[List[Alarm]]:
        """
        A generator which yields pages of Alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/metric/alarms.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#metricalarms)
        """

    def __iter__(self) -> Iterator[Alarm]:
        """
        A generator which yields Alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/metric/alarms.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#metricalarms)
        """

class Alarm(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/alarm/index.html#CloudWatch.Alarm)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#alarm)
    """

    name: str
    metric: Metric
    alarm_name: str
    alarm_arn: str
    alarm_description: str
    alarm_configuration_updated_timestamp: datetime
    actions_enabled: bool
    ok_actions: List[str]
    alarm_actions: List[str]
    insufficient_data_actions: List[str]
    state_value: StateValueType
    state_reason: str
    state_reason_data: str
    state_updated_timestamp: datetime
    metric_name: str
    namespace: str
    statistic: StatisticType
    extended_statistic: str
    dimensions: List[DimensionTypeDef]
    period: int
    unit: StandardUnitType
    evaluation_periods: int
    datapoints_to_alarm: int
    threshold: float
    comparison_operator: ComparisonOperatorType
    treat_missing_data: str
    evaluate_low_sample_count_percentile: str
    metrics: List[MetricDataQueryAlarmTypeDef]
    threshold_metric_id: str
    evaluation_state: Literal["PARTIAL_DATA"]
    state_transitioned_timestamp: datetime
    meta: CloudWatchResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Alarm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/alarm/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#alarmget_available_subresources-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/alarm/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#alarmdelete-method)
        """

    def describe_history(
        self, **kwargs: Unpack[DescribeAlarmHistoryInputAlarmDescribeHistoryTypeDef]
    ) -> DescribeAlarmHistoryOutputTypeDef:
        """
        Retrieves the history for the specified alarm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/alarm/describe_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#alarmdescribe_history-method)
        """

    def disable_actions(self) -> None:
        """
        Disables the actions for the specified alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/alarm/disable_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#alarmdisable_actions-method)
        """

    def enable_actions(self) -> None:
        """
        Enables the actions for the specified alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/alarm/enable_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#alarmenable_actions-method)
        """

    def set_state(self, **kwargs: Unpack[SetAlarmStateInputAlarmSetStateTypeDef]) -> None:
        """
        Temporarily sets the state of an alarm for testing purposes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/alarm/set_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#alarmset_state-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/alarm/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#alarmload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/alarm/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#alarmreload-method)
        """

_Alarm = Alarm

class Metric(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/metric/index.html#CloudWatch.Metric)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#metric)
    """

    namespace: str
    name: str
    alarms: MetricAlarmsCollection
    metric_name: str
    dimensions: List[DimensionTypeDef]
    meta: CloudWatchResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Metric.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/metric/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#metricget_available_subresources-method)
        """

    def get_statistics(
        self, **kwargs: Unpack[GetMetricStatisticsInputMetricGetStatisticsTypeDef]
    ) -> GetMetricStatisticsOutputTypeDef:
        """
        Gets statistics for the specified metric.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/metric/get_statistics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#metricget_statistics-method)
        """

    def put_alarm(self, **kwargs: Unpack[PutMetricAlarmInputMetricPutAlarmTypeDef]) -> _Alarm:
        """
        Creates or updates an alarm and associates it with the specified metric, metric
        math expression, anomaly detection model, or Metrics Insights query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/metric/put_alarm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#metricput_alarm-method)
        """

    def put_data(self, **kwargs: Unpack[PutMetricDataInputMetricPutDataTypeDef]) -> None:
        """
        Publishes metric data to Amazon CloudWatch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/metric/put_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#metricput_data-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/metric/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#metricload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/metric/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#metricreload-method)
        """

_Metric = Metric

class CloudWatchResourceMeta(ResourceMeta):
    client: CloudWatchClient  # type: ignore[override]

class CloudWatchServiceResource(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/index.html)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/)
    """

    meta: CloudWatchResourceMeta  # type: ignore[override]
    alarms: ServiceResourceAlarmsCollection
    metrics: ServiceResourceMetricsCollection

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#cloudwatchserviceresourceget_available_subresources-method)
        """

    def Alarm(self, name: str) -> _Alarm:
        """
        Creates a Alarm resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/Alarm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#cloudwatchserviceresourcealarm-method)
        """

    def Metric(self, namespace: str, name: str) -> _Metric:
        """
        Creates a Metric resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/service-resource/Metric.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource/#cloudwatchserviceresourcemetric-method)
        """
