"""
Type annotations for controltower service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/literals.html)

Usage::

    ```python
    from mypy_boto3_controltower.literals import BaselineOperationStatusType

    data: BaselineOperationStatusType = "FAILED"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BaselineOperationStatusType",
    "BaselineOperationTypeType",
    "ControlOperationStatusType",
    "ControlOperationTypeType",
    "DriftStatusType",
    "EnablementStatusType",
    "LandingZoneDriftStatusType",
    "LandingZoneOperationStatusType",
    "LandingZoneOperationTypeType",
    "LandingZoneStatusType",
    "ListBaselinesPaginatorName",
    "ListControlOperationsPaginatorName",
    "ListEnabledBaselinesPaginatorName",
    "ListEnabledControlsPaginatorName",
    "ListLandingZonesPaginatorName",
)

BaselineOperationStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
BaselineOperationTypeType = Literal[
    "DISABLE_BASELINE", "ENABLE_BASELINE", "RESET_ENABLED_BASELINE", "UPDATE_ENABLED_BASELINE"
]
ControlOperationStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
ControlOperationTypeType = Literal["DISABLE_CONTROL", "ENABLE_CONTROL", "UPDATE_ENABLED_CONTROL"]
DriftStatusType = Literal["DRIFTED", "IN_SYNC", "NOT_CHECKING", "UNKNOWN"]
EnablementStatusType = Literal["FAILED", "SUCCEEDED", "UNDER_CHANGE"]
LandingZoneDriftStatusType = Literal["DRIFTED", "IN_SYNC"]
LandingZoneOperationStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
LandingZoneOperationTypeType = Literal["CREATE", "DELETE", "RESET", "UPDATE"]
LandingZoneStatusType = Literal["ACTIVE", "FAILED", "PROCESSING"]
ListBaselinesPaginatorName = Literal["list_baselines"]
ListControlOperationsPaginatorName = Literal["list_control_operations"]
ListEnabledBaselinesPaginatorName = Literal["list_enabled_baselines"]
ListEnabledControlsPaginatorName = Literal["list_enabled_controls"]
ListLandingZonesPaginatorName = Literal["list_landing_zones"]
