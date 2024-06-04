"""
Type annotations for workspaces-thin-client service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/type_defs.html)

Usage::

    ```python
    from mypy_boto3_workspaces_thin_client.type_defs import CreateEnvironmentRequestRequestTypeDef

    data: CreateEnvironmentRequestRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ApplyTimeOfType,
    DayOfWeekType,
    DesktopTypeType,
    DeviceSoftwareSetComplianceStatusType,
    DeviceStatusType,
    EnvironmentSoftwareSetComplianceStatusType,
    MaintenanceWindowTypeType,
    SoftwareSetUpdateModeType,
    SoftwareSetUpdateScheduleType,
    SoftwareSetUpdateStatusType,
    SoftwareSetValidationStatusType,
    TargetDeviceStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateEnvironmentRequestRequestTypeDef",
    "CreateEnvironmentResponseTypeDef",
    "DeleteDeviceRequestRequestTypeDef",
    "DeleteEnvironmentRequestRequestTypeDef",
    "DeregisterDeviceRequestRequestTypeDef",
    "DeviceSummaryTypeDef",
    "DeviceTypeDef",
    "EnvironmentSummaryTypeDef",
    "EnvironmentTypeDef",
    "GetDeviceRequestRequestTypeDef",
    "GetDeviceResponseTypeDef",
    "GetEnvironmentRequestRequestTypeDef",
    "GetEnvironmentResponseTypeDef",
    "GetSoftwareSetRequestRequestTypeDef",
    "GetSoftwareSetResponseTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListDevicesResponseTypeDef",
    "ListEnvironmentsRequestRequestTypeDef",
    "ListEnvironmentsResponseTypeDef",
    "ListSoftwareSetsRequestRequestTypeDef",
    "ListSoftwareSetsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MaintenanceWindowTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SoftwareSetSummaryTypeDef",
    "SoftwareSetTypeDef",
    "SoftwareTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDeviceRequestRequestTypeDef",
    "UpdateDeviceResponseTypeDef",
    "UpdateEnvironmentRequestRequestTypeDef",
    "UpdateEnvironmentResponseTypeDef",
    "UpdateSoftwareSetRequestRequestTypeDef",
)

_RequiredCreateEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEnvironmentRequestRequestTypeDef",
    {
        "desktopArn": str,
    },
)
_OptionalCreateEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEnvironmentRequestRequestTypeDef",
    {
        "name": str,
        "desktopEndpoint": str,
        "softwareSetUpdateSchedule": SoftwareSetUpdateScheduleType,
        "maintenanceWindow": "MaintenanceWindowTypeDef",
        "softwareSetUpdateMode": SoftwareSetUpdateModeType,
        "desiredSoftwareSetId": str,
        "kmsKeyArn": str,
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateEnvironmentRequestRequestTypeDef(
    _RequiredCreateEnvironmentRequestRequestTypeDef, _OptionalCreateEnvironmentRequestRequestTypeDef
):
    pass

CreateEnvironmentResponseTypeDef = TypedDict(
    "CreateEnvironmentResponseTypeDef",
    {
        "environment": "EnvironmentSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDeviceRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalDeleteDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDeviceRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteDeviceRequestRequestTypeDef(
    _RequiredDeleteDeviceRequestRequestTypeDef, _OptionalDeleteDeviceRequestRequestTypeDef
):
    pass

_RequiredDeleteEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteEnvironmentRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalDeleteEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteEnvironmentRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteEnvironmentRequestRequestTypeDef(
    _RequiredDeleteEnvironmentRequestRequestTypeDef, _OptionalDeleteEnvironmentRequestRequestTypeDef
):
    pass

_RequiredDeregisterDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredDeregisterDeviceRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalDeregisterDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalDeregisterDeviceRequestRequestTypeDef",
    {
        "targetDeviceStatus": TargetDeviceStatusType,
        "clientToken": str,
    },
    total=False,
)

class DeregisterDeviceRequestRequestTypeDef(
    _RequiredDeregisterDeviceRequestRequestTypeDef, _OptionalDeregisterDeviceRequestRequestTypeDef
):
    pass

DeviceSummaryTypeDef = TypedDict(
    "DeviceSummaryTypeDef",
    {
        "id": str,
        "serialNumber": str,
        "name": str,
        "model": str,
        "environmentId": str,
        "status": DeviceStatusType,
        "currentSoftwareSetId": str,
        "desiredSoftwareSetId": str,
        "pendingSoftwareSetId": str,
        "softwareSetUpdateSchedule": SoftwareSetUpdateScheduleType,
        "lastConnectedAt": datetime,
        "lastPostureAt": datetime,
        "createdAt": datetime,
        "updatedAt": datetime,
        "arn": str,
    },
    total=False,
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "id": str,
        "serialNumber": str,
        "name": str,
        "model": str,
        "environmentId": str,
        "status": DeviceStatusType,
        "currentSoftwareSetId": str,
        "currentSoftwareSetVersion": str,
        "desiredSoftwareSetId": str,
        "pendingSoftwareSetId": str,
        "pendingSoftwareSetVersion": str,
        "softwareSetUpdateSchedule": SoftwareSetUpdateScheduleType,
        "softwareSetComplianceStatus": DeviceSoftwareSetComplianceStatusType,
        "softwareSetUpdateStatus": SoftwareSetUpdateStatusType,
        "lastConnectedAt": datetime,
        "lastPostureAt": datetime,
        "createdAt": datetime,
        "updatedAt": datetime,
        "arn": str,
        "kmsKeyArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

EnvironmentSummaryTypeDef = TypedDict(
    "EnvironmentSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "desktopArn": str,
        "desktopEndpoint": str,
        "desktopType": DesktopTypeType,
        "activationCode": str,
        "softwareSetUpdateSchedule": SoftwareSetUpdateScheduleType,
        "maintenanceWindow": "MaintenanceWindowTypeDef",
        "softwareSetUpdateMode": SoftwareSetUpdateModeType,
        "desiredSoftwareSetId": str,
        "pendingSoftwareSetId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "arn": str,
    },
    total=False,
)

EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "id": str,
        "name": str,
        "desktopArn": str,
        "desktopEndpoint": str,
        "desktopType": DesktopTypeType,
        "activationCode": str,
        "registeredDevicesCount": int,
        "softwareSetUpdateSchedule": SoftwareSetUpdateScheduleType,
        "maintenanceWindow": "MaintenanceWindowTypeDef",
        "softwareSetUpdateMode": SoftwareSetUpdateModeType,
        "desiredSoftwareSetId": str,
        "pendingSoftwareSetId": str,
        "pendingSoftwareSetVersion": str,
        "softwareSetComplianceStatus": EnvironmentSoftwareSetComplianceStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "arn": str,
        "kmsKeyArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

GetDeviceRequestRequestTypeDef = TypedDict(
    "GetDeviceRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetDeviceResponseTypeDef = TypedDict(
    "GetDeviceResponseTypeDef",
    {
        "device": "DeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentRequestRequestTypeDef = TypedDict(
    "GetEnvironmentRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetEnvironmentResponseTypeDef = TypedDict(
    "GetEnvironmentResponseTypeDef",
    {
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSoftwareSetRequestRequestTypeDef = TypedDict(
    "GetSoftwareSetRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetSoftwareSetResponseTypeDef = TypedDict(
    "GetSoftwareSetResponseTypeDef",
    {
        "softwareSet": "SoftwareSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicesRequestRequestTypeDef = TypedDict(
    "ListDevicesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {
        "devices": List["DeviceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEnvironmentsRequestRequestTypeDef = TypedDict(
    "ListEnvironmentsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListEnvironmentsResponseTypeDef = TypedDict(
    "ListEnvironmentsResponseTypeDef",
    {
        "environments": List["EnvironmentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSoftwareSetsRequestRequestTypeDef = TypedDict(
    "ListSoftwareSetsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListSoftwareSetsResponseTypeDef = TypedDict(
    "ListSoftwareSetsResponseTypeDef",
    {
        "softwareSets": List["SoftwareSetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MaintenanceWindowTypeDef = TypedDict(
    "MaintenanceWindowTypeDef",
    {
        "type": MaintenanceWindowTypeType,
        "startTimeHour": int,
        "startTimeMinute": int,
        "endTimeHour": int,
        "endTimeMinute": int,
        "daysOfTheWeek": List[DayOfWeekType],
        "applyTimeOf": ApplyTimeOfType,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

SoftwareSetSummaryTypeDef = TypedDict(
    "SoftwareSetSummaryTypeDef",
    {
        "id": str,
        "version": str,
        "releasedAt": datetime,
        "supportedUntil": datetime,
        "validationStatus": SoftwareSetValidationStatusType,
        "arn": str,
    },
    total=False,
)

SoftwareSetTypeDef = TypedDict(
    "SoftwareSetTypeDef",
    {
        "id": str,
        "version": str,
        "releasedAt": datetime,
        "supportedUntil": datetime,
        "validationStatus": SoftwareSetValidationStatusType,
        "software": List["SoftwareTypeDef"],
        "arn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

SoftwareTypeDef = TypedDict(
    "SoftwareTypeDef",
    {
        "name": str,
        "version": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDeviceRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDeviceRequestRequestTypeDef",
    {
        "name": str,
        "desiredSoftwareSetId": str,
        "softwareSetUpdateSchedule": SoftwareSetUpdateScheduleType,
    },
    total=False,
)

class UpdateDeviceRequestRequestTypeDef(
    _RequiredUpdateDeviceRequestRequestTypeDef, _OptionalUpdateDeviceRequestRequestTypeDef
):
    pass

UpdateDeviceResponseTypeDef = TypedDict(
    "UpdateDeviceResponseTypeDef",
    {
        "device": "DeviceSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEnvironmentRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEnvironmentRequestRequestTypeDef",
    {
        "name": str,
        "desktopArn": str,
        "desktopEndpoint": str,
        "softwareSetUpdateSchedule": SoftwareSetUpdateScheduleType,
        "maintenanceWindow": "MaintenanceWindowTypeDef",
        "softwareSetUpdateMode": SoftwareSetUpdateModeType,
        "desiredSoftwareSetId": str,
    },
    total=False,
)

class UpdateEnvironmentRequestRequestTypeDef(
    _RequiredUpdateEnvironmentRequestRequestTypeDef, _OptionalUpdateEnvironmentRequestRequestTypeDef
):
    pass

UpdateEnvironmentResponseTypeDef = TypedDict(
    "UpdateEnvironmentResponseTypeDef",
    {
        "environment": "EnvironmentSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSoftwareSetRequestRequestTypeDef = TypedDict(
    "UpdateSoftwareSetRequestRequestTypeDef",
    {
        "id": str,
        "validationStatus": SoftwareSetValidationStatusType,
    },
)
