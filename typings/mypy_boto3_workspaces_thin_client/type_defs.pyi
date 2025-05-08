"""
Type annotations for workspaces-thin-client service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_workspaces_thin_client.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

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

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "CreateEnvironmentRequestTypeDef",
    "CreateEnvironmentResponseTypeDef",
    "DeleteDeviceRequestTypeDef",
    "DeleteEnvironmentRequestTypeDef",
    "DeregisterDeviceRequestTypeDef",
    "DeviceSummaryTypeDef",
    "DeviceTypeDef",
    "EnvironmentSummaryTypeDef",
    "EnvironmentTypeDef",
    "GetDeviceRequestTypeDef",
    "GetDeviceResponseTypeDef",
    "GetEnvironmentRequestTypeDef",
    "GetEnvironmentResponseTypeDef",
    "GetSoftwareSetRequestTypeDef",
    "GetSoftwareSetResponseTypeDef",
    "ListDevicesRequestPaginateTypeDef",
    "ListDevicesRequestTypeDef",
    "ListDevicesResponseTypeDef",
    "ListEnvironmentsRequestPaginateTypeDef",
    "ListEnvironmentsRequestTypeDef",
    "ListEnvironmentsResponseTypeDef",
    "ListSoftwareSetsRequestPaginateTypeDef",
    "ListSoftwareSetsRequestTypeDef",
    "ListSoftwareSetsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MaintenanceWindowOutputTypeDef",
    "MaintenanceWindowTypeDef",
    "MaintenanceWindowUnionTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SoftwareSetSummaryTypeDef",
    "SoftwareSetTypeDef",
    "SoftwareTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDeviceRequestTypeDef",
    "UpdateDeviceResponseTypeDef",
    "UpdateEnvironmentRequestTypeDef",
    "UpdateEnvironmentResponseTypeDef",
    "UpdateSoftwareSetRequestTypeDef",
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

DeleteDeviceRequestTypeDef = TypedDict(
    "DeleteDeviceRequestTypeDef",
    {
        "id": str,
        "clientToken": NotRequired[str],
    },
)
DeleteEnvironmentRequestTypeDef = TypedDict(
    "DeleteEnvironmentRequestTypeDef",
    {
        "id": str,
        "clientToken": NotRequired[str],
    },
)
DeregisterDeviceRequestTypeDef = TypedDict(
    "DeregisterDeviceRequestTypeDef",
    {
        "id": str,
        "targetDeviceStatus": NotRequired[TargetDeviceStatusType],
        "clientToken": NotRequired[str],
    },
)
DeviceSummaryTypeDef = TypedDict(
    "DeviceSummaryTypeDef",
    {
        "id": NotRequired[str],
        "serialNumber": NotRequired[str],
        "name": NotRequired[str],
        "model": NotRequired[str],
        "environmentId": NotRequired[str],
        "status": NotRequired[DeviceStatusType],
        "currentSoftwareSetId": NotRequired[str],
        "desiredSoftwareSetId": NotRequired[str],
        "pendingSoftwareSetId": NotRequired[str],
        "softwareSetUpdateSchedule": NotRequired[SoftwareSetUpdateScheduleType],
        "lastConnectedAt": NotRequired[datetime],
        "lastPostureAt": NotRequired[datetime],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "arn": NotRequired[str],
    },
)
DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "id": NotRequired[str],
        "serialNumber": NotRequired[str],
        "name": NotRequired[str],
        "model": NotRequired[str],
        "environmentId": NotRequired[str],
        "status": NotRequired[DeviceStatusType],
        "currentSoftwareSetId": NotRequired[str],
        "currentSoftwareSetVersion": NotRequired[str],
        "desiredSoftwareSetId": NotRequired[str],
        "pendingSoftwareSetId": NotRequired[str],
        "pendingSoftwareSetVersion": NotRequired[str],
        "softwareSetUpdateSchedule": NotRequired[SoftwareSetUpdateScheduleType],
        "softwareSetComplianceStatus": NotRequired[DeviceSoftwareSetComplianceStatusType],
        "softwareSetUpdateStatus": NotRequired[SoftwareSetUpdateStatusType],
        "lastConnectedAt": NotRequired[datetime],
        "lastPostureAt": NotRequired[datetime],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "arn": NotRequired[str],
        "kmsKeyArn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
MaintenanceWindowOutputTypeDef = TypedDict(
    "MaintenanceWindowOutputTypeDef",
    {
        "type": MaintenanceWindowTypeType,
        "startTimeHour": NotRequired[int],
        "startTimeMinute": NotRequired[int],
        "endTimeHour": NotRequired[int],
        "endTimeMinute": NotRequired[int],
        "daysOfTheWeek": NotRequired[List[DayOfWeekType]],
        "applyTimeOf": NotRequired[ApplyTimeOfType],
    },
)
GetDeviceRequestTypeDef = TypedDict(
    "GetDeviceRequestTypeDef",
    {
        "id": str,
    },
)
GetEnvironmentRequestTypeDef = TypedDict(
    "GetEnvironmentRequestTypeDef",
    {
        "id": str,
    },
)
GetSoftwareSetRequestTypeDef = TypedDict(
    "GetSoftwareSetRequestTypeDef",
    {
        "id": str,
    },
)

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListDevicesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListEnvironmentsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListSoftwareSetsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

SoftwareSetSummaryTypeDef = TypedDict(
    "SoftwareSetSummaryTypeDef",
    {
        "id": NotRequired[str],
        "version": NotRequired[str],
        "releasedAt": NotRequired[datetime],
        "supportedUntil": NotRequired[datetime],
        "validationStatus": NotRequired[SoftwareSetValidationStatusType],
        "arn": NotRequired[str],
    },
)

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

MaintenanceWindowTypeDef = TypedDict(
    "MaintenanceWindowTypeDef",
    {
        "type": MaintenanceWindowTypeType,
        "startTimeHour": NotRequired[int],
        "startTimeMinute": NotRequired[int],
        "endTimeHour": NotRequired[int],
        "endTimeMinute": NotRequired[int],
        "daysOfTheWeek": NotRequired[Sequence[DayOfWeekType]],
        "applyTimeOf": NotRequired[ApplyTimeOfType],
    },
)

class SoftwareTypeDef(TypedDict):
    name: NotRequired[str]
    version: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

UpdateDeviceRequestTypeDef = TypedDict(
    "UpdateDeviceRequestTypeDef",
    {
        "id": str,
        "name": NotRequired[str],
        "desiredSoftwareSetId": NotRequired[str],
        "softwareSetUpdateSchedule": NotRequired[SoftwareSetUpdateScheduleType],
    },
)
UpdateSoftwareSetRequestTypeDef = TypedDict(
    "UpdateSoftwareSetRequestTypeDef",
    {
        "id": str,
        "validationStatus": SoftwareSetValidationStatusType,
    },
)

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDevicesResponseTypeDef(TypedDict):
    devices: List[DeviceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateDeviceResponseTypeDef(TypedDict):
    device: DeviceSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeviceResponseTypeDef(TypedDict):
    device: DeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

EnvironmentSummaryTypeDef = TypedDict(
    "EnvironmentSummaryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "desktopArn": NotRequired[str],
        "desktopEndpoint": NotRequired[str],
        "desktopType": NotRequired[DesktopTypeType],
        "activationCode": NotRequired[str],
        "softwareSetUpdateSchedule": NotRequired[SoftwareSetUpdateScheduleType],
        "maintenanceWindow": NotRequired[MaintenanceWindowOutputTypeDef],
        "softwareSetUpdateMode": NotRequired[SoftwareSetUpdateModeType],
        "desiredSoftwareSetId": NotRequired[str],
        "pendingSoftwareSetId": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "arn": NotRequired[str],
    },
)
EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "desktopArn": NotRequired[str],
        "desktopEndpoint": NotRequired[str],
        "desktopType": NotRequired[DesktopTypeType],
        "activationCode": NotRequired[str],
        "registeredDevicesCount": NotRequired[int],
        "softwareSetUpdateSchedule": NotRequired[SoftwareSetUpdateScheduleType],
        "maintenanceWindow": NotRequired[MaintenanceWindowOutputTypeDef],
        "softwareSetUpdateMode": NotRequired[SoftwareSetUpdateModeType],
        "desiredSoftwareSetId": NotRequired[str],
        "pendingSoftwareSetId": NotRequired[str],
        "pendingSoftwareSetVersion": NotRequired[str],
        "softwareSetComplianceStatus": NotRequired[EnvironmentSoftwareSetComplianceStatusType],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "arn": NotRequired[str],
        "kmsKeyArn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "deviceCreationTags": NotRequired[Dict[str, str]],
    },
)

class ListDevicesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEnvironmentsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSoftwareSetsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSoftwareSetsResponseTypeDef(TypedDict):
    softwareSets: List[SoftwareSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

MaintenanceWindowUnionTypeDef = Union[MaintenanceWindowTypeDef, MaintenanceWindowOutputTypeDef]
SoftwareSetTypeDef = TypedDict(
    "SoftwareSetTypeDef",
    {
        "id": NotRequired[str],
        "version": NotRequired[str],
        "releasedAt": NotRequired[datetime],
        "supportedUntil": NotRequired[datetime],
        "validationStatus": NotRequired[SoftwareSetValidationStatusType],
        "software": NotRequired[List[SoftwareTypeDef]],
        "arn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

class CreateEnvironmentResponseTypeDef(TypedDict):
    environment: EnvironmentSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentsResponseTypeDef(TypedDict):
    environments: List[EnvironmentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateEnvironmentResponseTypeDef(TypedDict):
    environment: EnvironmentSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentResponseTypeDef(TypedDict):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentRequestTypeDef(TypedDict):
    desktopArn: str
    name: NotRequired[str]
    desktopEndpoint: NotRequired[str]
    softwareSetUpdateSchedule: NotRequired[SoftwareSetUpdateScheduleType]
    maintenanceWindow: NotRequired[MaintenanceWindowUnionTypeDef]
    softwareSetUpdateMode: NotRequired[SoftwareSetUpdateModeType]
    desiredSoftwareSetId: NotRequired[str]
    kmsKeyArn: NotRequired[str]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    deviceCreationTags: NotRequired[Mapping[str, str]]

UpdateEnvironmentRequestTypeDef = TypedDict(
    "UpdateEnvironmentRequestTypeDef",
    {
        "id": str,
        "name": NotRequired[str],
        "desktopArn": NotRequired[str],
        "desktopEndpoint": NotRequired[str],
        "softwareSetUpdateSchedule": NotRequired[SoftwareSetUpdateScheduleType],
        "maintenanceWindow": NotRequired[MaintenanceWindowUnionTypeDef],
        "softwareSetUpdateMode": NotRequired[SoftwareSetUpdateModeType],
        "desiredSoftwareSetId": NotRequired[str],
        "deviceCreationTags": NotRequired[Mapping[str, str]],
    },
)

class GetSoftwareSetResponseTypeDef(TypedDict):
    softwareSet: SoftwareSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
