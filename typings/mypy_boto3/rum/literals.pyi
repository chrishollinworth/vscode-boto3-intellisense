"""
Type annotations for rum service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/literals.html)

Usage::

    ```python
    from mypy_boto3_rum.literals import BatchGetRumMetricDefinitionsPaginatorName

    data: BatchGetRumMetricDefinitionsPaginatorName = "batch_get_rum_metric_definitions"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BatchGetRumMetricDefinitionsPaginatorName",
    "CustomEventsStatusType",
    "GetAppMonitorDataPaginatorName",
    "ListAppMonitorsPaginatorName",
    "ListRumMetricsDestinationsPaginatorName",
    "MetricDestinationType",
    "StateEnumType",
    "TelemetryType",
)

BatchGetRumMetricDefinitionsPaginatorName = Literal["batch_get_rum_metric_definitions"]
CustomEventsStatusType = Literal["DISABLED", "ENABLED"]
GetAppMonitorDataPaginatorName = Literal["get_app_monitor_data"]
ListAppMonitorsPaginatorName = Literal["list_app_monitors"]
ListRumMetricsDestinationsPaginatorName = Literal["list_rum_metrics_destinations"]
MetricDestinationType = Literal["CloudWatch", "Evidently"]
StateEnumType = Literal["ACTIVE", "CREATED", "DELETING"]
TelemetryType = Literal["errors", "http", "performance"]
