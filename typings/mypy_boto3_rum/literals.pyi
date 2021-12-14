"""
Type annotations for rum service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/literals.html)

Usage::

    ```python
    from mypy_boto3_rum.literals import GetAppMonitorDataPaginatorName

    data: GetAppMonitorDataPaginatorName = "get_app_monitor_data"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "GetAppMonitorDataPaginatorName",
    "ListAppMonitorsPaginatorName",
    "StateEnumType",
    "TelemetryType",
)

GetAppMonitorDataPaginatorName = Literal["get_app_monitor_data"]
ListAppMonitorsPaginatorName = Literal["list_app_monitors"]
StateEnumType = Literal["ACTIVE", "CREATED", "DELETING"]
TelemetryType = Literal["errors", "http", "performance"]
