"""
Type annotations for controltower service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/type_defs.html)

Usage::

    ```python
    from mypy_boto3_controltower.type_defs import ControlOperationTypeDef

    data: ControlOperationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ControlOperationStatusType,
    ControlOperationTypeType,
    DriftStatusType,
    EnablementStatusType,
    LandingZoneDriftStatusType,
    LandingZoneOperationStatusType,
    LandingZoneOperationTypeType,
    LandingZoneStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ControlOperationTypeDef",
    "CreateLandingZoneInputRequestTypeDef",
    "CreateLandingZoneOutputTypeDef",
    "DeleteLandingZoneInputRequestTypeDef",
    "DeleteLandingZoneOutputTypeDef",
    "DisableControlInputRequestTypeDef",
    "DisableControlOutputTypeDef",
    "DriftStatusSummaryTypeDef",
    "EnableControlInputRequestTypeDef",
    "EnableControlOutputTypeDef",
    "EnabledControlDetailsTypeDef",
    "EnabledControlSummaryTypeDef",
    "EnablementStatusSummaryTypeDef",
    "GetControlOperationInputRequestTypeDef",
    "GetControlOperationOutputTypeDef",
    "GetEnabledControlInputRequestTypeDef",
    "GetEnabledControlOutputTypeDef",
    "GetLandingZoneInputRequestTypeDef",
    "GetLandingZoneOperationInputRequestTypeDef",
    "GetLandingZoneOperationOutputTypeDef",
    "GetLandingZoneOutputTypeDef",
    "LandingZoneDetailTypeDef",
    "LandingZoneDriftStatusSummaryTypeDef",
    "LandingZoneOperationDetailTypeDef",
    "LandingZoneSummaryTypeDef",
    "ListEnabledControlsInputRequestTypeDef",
    "ListEnabledControlsOutputTypeDef",
    "ListLandingZonesInputRequestTypeDef",
    "ListLandingZonesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "PaginatorConfigTypeDef",
    "RegionTypeDef",
    "ResetLandingZoneInputRequestTypeDef",
    "ResetLandingZoneOutputTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateLandingZoneInputRequestTypeDef",
    "UpdateLandingZoneOutputTypeDef",
)

ControlOperationTypeDef = TypedDict(
    "ControlOperationTypeDef",
    {
        "endTime": datetime,
        "operationType": ControlOperationTypeType,
        "startTime": datetime,
        "status": ControlOperationStatusType,
        "statusMessage": str,
    },
    total=False,
)

_RequiredCreateLandingZoneInputRequestTypeDef = TypedDict(
    "_RequiredCreateLandingZoneInputRequestTypeDef",
    {
        "manifest": Dict[str, Any],
        "version": str,
    },
)
_OptionalCreateLandingZoneInputRequestTypeDef = TypedDict(
    "_OptionalCreateLandingZoneInputRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateLandingZoneInputRequestTypeDef(
    _RequiredCreateLandingZoneInputRequestTypeDef, _OptionalCreateLandingZoneInputRequestTypeDef
):
    pass

CreateLandingZoneOutputTypeDef = TypedDict(
    "CreateLandingZoneOutputTypeDef",
    {
        "arn": str,
        "operationIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLandingZoneInputRequestTypeDef = TypedDict(
    "DeleteLandingZoneInputRequestTypeDef",
    {
        "landingZoneIdentifier": str,
    },
)

DeleteLandingZoneOutputTypeDef = TypedDict(
    "DeleteLandingZoneOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableControlInputRequestTypeDef = TypedDict(
    "DisableControlInputRequestTypeDef",
    {
        "controlIdentifier": str,
        "targetIdentifier": str,
    },
)

DisableControlOutputTypeDef = TypedDict(
    "DisableControlOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DriftStatusSummaryTypeDef = TypedDict(
    "DriftStatusSummaryTypeDef",
    {
        "driftStatus": DriftStatusType,
    },
    total=False,
)

_RequiredEnableControlInputRequestTypeDef = TypedDict(
    "_RequiredEnableControlInputRequestTypeDef",
    {
        "controlIdentifier": str,
        "targetIdentifier": str,
    },
)
_OptionalEnableControlInputRequestTypeDef = TypedDict(
    "_OptionalEnableControlInputRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class EnableControlInputRequestTypeDef(
    _RequiredEnableControlInputRequestTypeDef, _OptionalEnableControlInputRequestTypeDef
):
    pass

EnableControlOutputTypeDef = TypedDict(
    "EnableControlOutputTypeDef",
    {
        "arn": str,
        "operationIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnabledControlDetailsTypeDef = TypedDict(
    "EnabledControlDetailsTypeDef",
    {
        "arn": str,
        "controlIdentifier": str,
        "driftStatusSummary": "DriftStatusSummaryTypeDef",
        "statusSummary": "EnablementStatusSummaryTypeDef",
        "targetIdentifier": str,
        "targetRegions": List["RegionTypeDef"],
    },
    total=False,
)

EnabledControlSummaryTypeDef = TypedDict(
    "EnabledControlSummaryTypeDef",
    {
        "arn": str,
        "controlIdentifier": str,
        "driftStatusSummary": "DriftStatusSummaryTypeDef",
        "statusSummary": "EnablementStatusSummaryTypeDef",
        "targetIdentifier": str,
    },
    total=False,
)

EnablementStatusSummaryTypeDef = TypedDict(
    "EnablementStatusSummaryTypeDef",
    {
        "lastOperationIdentifier": str,
        "status": EnablementStatusType,
    },
    total=False,
)

GetControlOperationInputRequestTypeDef = TypedDict(
    "GetControlOperationInputRequestTypeDef",
    {
        "operationIdentifier": str,
    },
)

GetControlOperationOutputTypeDef = TypedDict(
    "GetControlOperationOutputTypeDef",
    {
        "controlOperation": "ControlOperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnabledControlInputRequestTypeDef = TypedDict(
    "GetEnabledControlInputRequestTypeDef",
    {
        "enabledControlIdentifier": str,
    },
)

GetEnabledControlOutputTypeDef = TypedDict(
    "GetEnabledControlOutputTypeDef",
    {
        "enabledControlDetails": "EnabledControlDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLandingZoneInputRequestTypeDef = TypedDict(
    "GetLandingZoneInputRequestTypeDef",
    {
        "landingZoneIdentifier": str,
    },
)

GetLandingZoneOperationInputRequestTypeDef = TypedDict(
    "GetLandingZoneOperationInputRequestTypeDef",
    {
        "operationIdentifier": str,
    },
)

GetLandingZoneOperationOutputTypeDef = TypedDict(
    "GetLandingZoneOperationOutputTypeDef",
    {
        "operationDetails": "LandingZoneOperationDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLandingZoneOutputTypeDef = TypedDict(
    "GetLandingZoneOutputTypeDef",
    {
        "landingZone": "LandingZoneDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLandingZoneDetailTypeDef = TypedDict(
    "_RequiredLandingZoneDetailTypeDef",
    {
        "manifest": Dict[str, Any],
        "version": str,
    },
)
_OptionalLandingZoneDetailTypeDef = TypedDict(
    "_OptionalLandingZoneDetailTypeDef",
    {
        "arn": str,
        "driftStatus": "LandingZoneDriftStatusSummaryTypeDef",
        "latestAvailableVersion": str,
        "status": LandingZoneStatusType,
    },
    total=False,
)

class LandingZoneDetailTypeDef(
    _RequiredLandingZoneDetailTypeDef, _OptionalLandingZoneDetailTypeDef
):
    pass

LandingZoneDriftStatusSummaryTypeDef = TypedDict(
    "LandingZoneDriftStatusSummaryTypeDef",
    {
        "status": LandingZoneDriftStatusType,
    },
    total=False,
)

LandingZoneOperationDetailTypeDef = TypedDict(
    "LandingZoneOperationDetailTypeDef",
    {
        "endTime": datetime,
        "operationType": LandingZoneOperationTypeType,
        "startTime": datetime,
        "status": LandingZoneOperationStatusType,
        "statusMessage": str,
    },
    total=False,
)

LandingZoneSummaryTypeDef = TypedDict(
    "LandingZoneSummaryTypeDef",
    {
        "arn": str,
    },
    total=False,
)

_RequiredListEnabledControlsInputRequestTypeDef = TypedDict(
    "_RequiredListEnabledControlsInputRequestTypeDef",
    {
        "targetIdentifier": str,
    },
)
_OptionalListEnabledControlsInputRequestTypeDef = TypedDict(
    "_OptionalListEnabledControlsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListEnabledControlsInputRequestTypeDef(
    _RequiredListEnabledControlsInputRequestTypeDef, _OptionalListEnabledControlsInputRequestTypeDef
):
    pass

ListEnabledControlsOutputTypeDef = TypedDict(
    "ListEnabledControlsOutputTypeDef",
    {
        "enabledControls": List["EnabledControlSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLandingZonesInputRequestTypeDef = TypedDict(
    "ListLandingZonesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListLandingZonesOutputTypeDef = TypedDict(
    "ListLandingZonesOutputTypeDef",
    {
        "landingZones": List["LandingZoneSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

RegionTypeDef = TypedDict(
    "RegionTypeDef",
    {
        "name": str,
    },
    total=False,
)

ResetLandingZoneInputRequestTypeDef = TypedDict(
    "ResetLandingZoneInputRequestTypeDef",
    {
        "landingZoneIdentifier": str,
    },
)

ResetLandingZoneOutputTypeDef = TypedDict(
    "ResetLandingZoneOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateLandingZoneInputRequestTypeDef = TypedDict(
    "UpdateLandingZoneInputRequestTypeDef",
    {
        "landingZoneIdentifier": str,
        "manifest": Dict[str, Any],
        "version": str,
    },
)

UpdateLandingZoneOutputTypeDef = TypedDict(
    "UpdateLandingZoneOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
