"""
Type annotations for internetmonitor service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/literals.html)

Usage::

    ```python
    from mypy_boto3_internetmonitor.literals import HealthEventImpactTypeType

    data: HealthEventImpactTypeType = "AVAILABILITY"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "HealthEventImpactTypeType",
    "HealthEventStatusType",
    "ListHealthEventsPaginatorName",
    "ListMonitorsPaginatorName",
    "LogDeliveryStatusType",
    "MonitorConfigStateType",
    "MonitorProcessingStatusCodeType",
    "TriangulationEventTypeType",
)

HealthEventImpactTypeType = Literal["AVAILABILITY", "PERFORMANCE"]
HealthEventStatusType = Literal["ACTIVE", "RESOLVED"]
ListHealthEventsPaginatorName = Literal["list_health_events"]
ListMonitorsPaginatorName = Literal["list_monitors"]
LogDeliveryStatusType = Literal["DISABLED", "ENABLED"]
MonitorConfigStateType = Literal["ACTIVE", "ERROR", "INACTIVE", "PENDING"]
MonitorProcessingStatusCodeType = Literal[
    "COLLECTING_DATA",
    "FAULT_ACCESS_CLOUDWATCH",
    "FAULT_SERVICE",
    "INACTIVE",
    "INSUFFICIENT_DATA",
    "OK",
]
TriangulationEventTypeType = Literal["AWS", "Internet"]
