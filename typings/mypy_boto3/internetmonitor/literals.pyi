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
    "InternetEventStatusType",
    "InternetEventTypeType",
    "ListHealthEventsPaginatorName",
    "ListInternetEventsPaginatorName",
    "ListMonitorsPaginatorName",
    "LocalHealthEventsConfigStatusType",
    "LogDeliveryStatusType",
    "MonitorConfigStateType",
    "MonitorProcessingStatusCodeType",
    "OperatorType",
    "QueryStatusType",
    "QueryTypeType",
    "TriangulationEventTypeType",
)

HealthEventImpactTypeType = Literal[
    "AVAILABILITY", "LOCAL_AVAILABILITY", "LOCAL_PERFORMANCE", "PERFORMANCE"
]
HealthEventStatusType = Literal["ACTIVE", "RESOLVED"]
InternetEventStatusType = Literal["ACTIVE", "RESOLVED"]
InternetEventTypeType = Literal["AVAILABILITY", "PERFORMANCE"]
ListHealthEventsPaginatorName = Literal["list_health_events"]
ListInternetEventsPaginatorName = Literal["list_internet_events"]
ListMonitorsPaginatorName = Literal["list_monitors"]
LocalHealthEventsConfigStatusType = Literal["DISABLED", "ENABLED"]
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
OperatorType = Literal["EQUALS", "NOT_EQUALS"]
QueryStatusType = Literal["CANCELED", "FAILED", "QUEUED", "RUNNING", "SUCCEEDED"]
QueryTypeType = Literal["MEASUREMENTS", "TOP_LOCATIONS", "TOP_LOCATION_DETAILS"]
TriangulationEventTypeType = Literal["AWS", "Internet"]
