"""
Type annotations for application-signals service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/literals.html)

Usage::

    ```python
    from mypy_boto3_application_signals.literals import DurationUnitType

    data: DurationUnitType = "DAY"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DurationUnitType",
    "ListServiceDependenciesPaginatorName",
    "ListServiceDependentsPaginatorName",
    "ListServiceLevelObjectivesPaginatorName",
    "ListServiceOperationsPaginatorName",
    "ListServicesPaginatorName",
    "ServiceLevelIndicatorComparisonOperatorType",
    "ServiceLevelIndicatorMetricTypeType",
    "ServiceLevelObjectiveBudgetStatusType",
    "StandardUnitType",
)

DurationUnitType = Literal["DAY", "MONTH"]
ListServiceDependenciesPaginatorName = Literal["list_service_dependencies"]
ListServiceDependentsPaginatorName = Literal["list_service_dependents"]
ListServiceLevelObjectivesPaginatorName = Literal["list_service_level_objectives"]
ListServiceOperationsPaginatorName = Literal["list_service_operations"]
ListServicesPaginatorName = Literal["list_services"]
ServiceLevelIndicatorComparisonOperatorType = Literal[
    "GreaterThan", "GreaterThanOrEqualTo", "LessThan", "LessThanOrEqualTo"
]
ServiceLevelIndicatorMetricTypeType = Literal["AVAILABILITY", "LATENCY"]
ServiceLevelObjectiveBudgetStatusType = Literal["BREACHED", "INSUFFICIENT_DATA", "OK", "WARNING"]
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
