"""
Type annotations for workspaces-thin-client service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/literals.html)

Usage::

    ```python
    from mypy_boto3_workspaces_thin_client.literals import ApplyTimeOfType

    data: ApplyTimeOfType = "DEVICE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ApplyTimeOfType",
    "DayOfWeekType",
    "DesktopTypeType",
    "DeviceSoftwareSetComplianceStatusType",
    "DeviceStatusType",
    "EnvironmentSoftwareSetComplianceStatusType",
    "ListDevicesPaginatorName",
    "ListEnvironmentsPaginatorName",
    "ListSoftwareSetsPaginatorName",
    "MaintenanceWindowTypeType",
    "SoftwareSetUpdateModeType",
    "SoftwareSetUpdateScheduleType",
    "SoftwareSetUpdateStatusType",
    "SoftwareSetValidationStatusType",
    "TargetDeviceStatusType",
)

ApplyTimeOfType = Literal["DEVICE", "UTC"]
DayOfWeekType = Literal[
    "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
]
DesktopTypeType = Literal["appstream", "workspaces", "workspaces-web"]
DeviceSoftwareSetComplianceStatusType = Literal["COMPLIANT", "NONE", "NOT_COMPLIANT"]
DeviceStatusType = Literal["ARCHIVED", "DEREGISTERED", "DEREGISTERING", "REGISTERED"]
EnvironmentSoftwareSetComplianceStatusType = Literal[
    "COMPLIANT", "NOT_COMPLIANT", "NO_REGISTERED_DEVICES"
]
ListDevicesPaginatorName = Literal["list_devices"]
ListEnvironmentsPaginatorName = Literal["list_environments"]
ListSoftwareSetsPaginatorName = Literal["list_software_sets"]
MaintenanceWindowTypeType = Literal["CUSTOM", "SYSTEM"]
SoftwareSetUpdateModeType = Literal["USE_DESIRED", "USE_LATEST"]
SoftwareSetUpdateScheduleType = Literal["APPLY_IMMEDIATELY", "USE_MAINTENANCE_WINDOW"]
SoftwareSetUpdateStatusType = Literal["AVAILABLE", "IN_PROGRESS", "UP_TO_DATE"]
SoftwareSetValidationStatusType = Literal["NOT_VALIDATED", "VALIDATED"]
TargetDeviceStatusType = Literal["ARCHIVED", "DEREGISTERED"]
