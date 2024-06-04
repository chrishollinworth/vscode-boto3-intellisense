"""
Type annotations for controltower service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/type_defs.html)

Usage::

    ```python
    from mypy_boto3_controltower.type_defs import BaselineOperationTypeDef

    data: BaselineOperationTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    BaselineOperationStatusType,
    BaselineOperationTypeType,
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
    "BaselineOperationTypeDef",
    "BaselineSummaryTypeDef",
    "ControlOperationFilterTypeDef",
    "ControlOperationSummaryTypeDef",
    "ControlOperationTypeDef",
    "CreateLandingZoneInputRequestTypeDef",
    "CreateLandingZoneOutputTypeDef",
    "DeleteLandingZoneInputRequestTypeDef",
    "DeleteLandingZoneOutputTypeDef",
    "DisableBaselineInputRequestTypeDef",
    "DisableBaselineOutputTypeDef",
    "DisableControlInputRequestTypeDef",
    "DisableControlOutputTypeDef",
    "DriftStatusSummaryTypeDef",
    "EnableBaselineInputRequestTypeDef",
    "EnableBaselineOutputTypeDef",
    "EnableControlInputRequestTypeDef",
    "EnableControlOutputTypeDef",
    "EnabledBaselineDetailsTypeDef",
    "EnabledBaselineFilterTypeDef",
    "EnabledBaselineParameterSummaryTypeDef",
    "EnabledBaselineParameterTypeDef",
    "EnabledBaselineSummaryTypeDef",
    "EnabledControlDetailsTypeDef",
    "EnabledControlFilterTypeDef",
    "EnabledControlParameterSummaryTypeDef",
    "EnabledControlParameterTypeDef",
    "EnabledControlSummaryTypeDef",
    "EnablementStatusSummaryTypeDef",
    "GetBaselineInputRequestTypeDef",
    "GetBaselineOperationInputRequestTypeDef",
    "GetBaselineOperationOutputTypeDef",
    "GetBaselineOutputTypeDef",
    "GetControlOperationInputRequestTypeDef",
    "GetControlOperationOutputTypeDef",
    "GetEnabledBaselineInputRequestTypeDef",
    "GetEnabledBaselineOutputTypeDef",
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
    "ListBaselinesInputRequestTypeDef",
    "ListBaselinesOutputTypeDef",
    "ListControlOperationsInputRequestTypeDef",
    "ListControlOperationsOutputTypeDef",
    "ListEnabledBaselinesInputRequestTypeDef",
    "ListEnabledBaselinesOutputTypeDef",
    "ListEnabledControlsInputRequestTypeDef",
    "ListEnabledControlsOutputTypeDef",
    "ListLandingZonesInputRequestTypeDef",
    "ListLandingZonesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "PaginatorConfigTypeDef",
    "RegionTypeDef",
    "ResetEnabledBaselineInputRequestTypeDef",
    "ResetEnabledBaselineOutputTypeDef",
    "ResetLandingZoneInputRequestTypeDef",
    "ResetLandingZoneOutputTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateEnabledBaselineInputRequestTypeDef",
    "UpdateEnabledBaselineOutputTypeDef",
    "UpdateEnabledControlInputRequestTypeDef",
    "UpdateEnabledControlOutputTypeDef",
    "UpdateLandingZoneInputRequestTypeDef",
    "UpdateLandingZoneOutputTypeDef",
)

BaselineOperationTypeDef = TypedDict(
    "BaselineOperationTypeDef",
    {
        "endTime": datetime,
        "operationIdentifier": str,
        "operationType": BaselineOperationTypeType,
        "startTime": datetime,
        "status": BaselineOperationStatusType,
        "statusMessage": str,
    },
    total=False,
)

_RequiredBaselineSummaryTypeDef = TypedDict(
    "_RequiredBaselineSummaryTypeDef",
    {
        "arn": str,
        "name": str,
    },
)
_OptionalBaselineSummaryTypeDef = TypedDict(
    "_OptionalBaselineSummaryTypeDef",
    {
        "description": str,
    },
    total=False,
)

class BaselineSummaryTypeDef(_RequiredBaselineSummaryTypeDef, _OptionalBaselineSummaryTypeDef):
    pass

ControlOperationFilterTypeDef = TypedDict(
    "ControlOperationFilterTypeDef",
    {
        "controlIdentifiers": List[str],
        "controlOperationTypes": List[ControlOperationTypeType],
        "enabledControlIdentifiers": List[str],
        "statuses": List[ControlOperationStatusType],
        "targetIdentifiers": List[str],
    },
    total=False,
)

ControlOperationSummaryTypeDef = TypedDict(
    "ControlOperationSummaryTypeDef",
    {
        "controlIdentifier": str,
        "enabledControlIdentifier": str,
        "endTime": datetime,
        "operationIdentifier": str,
        "operationType": ControlOperationTypeType,
        "startTime": datetime,
        "status": ControlOperationStatusType,
        "statusMessage": str,
        "targetIdentifier": str,
    },
    total=False,
)

ControlOperationTypeDef = TypedDict(
    "ControlOperationTypeDef",
    {
        "controlIdentifier": str,
        "enabledControlIdentifier": str,
        "endTime": datetime,
        "operationIdentifier": str,
        "operationType": ControlOperationTypeType,
        "startTime": datetime,
        "status": ControlOperationStatusType,
        "statusMessage": str,
        "targetIdentifier": str,
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

DisableBaselineInputRequestTypeDef = TypedDict(
    "DisableBaselineInputRequestTypeDef",
    {
        "enabledBaselineIdentifier": str,
    },
)

DisableBaselineOutputTypeDef = TypedDict(
    "DisableBaselineOutputTypeDef",
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

_RequiredEnableBaselineInputRequestTypeDef = TypedDict(
    "_RequiredEnableBaselineInputRequestTypeDef",
    {
        "baselineIdentifier": str,
        "baselineVersion": str,
        "targetIdentifier": str,
    },
)
_OptionalEnableBaselineInputRequestTypeDef = TypedDict(
    "_OptionalEnableBaselineInputRequestTypeDef",
    {
        "parameters": List["EnabledBaselineParameterTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)

class EnableBaselineInputRequestTypeDef(
    _RequiredEnableBaselineInputRequestTypeDef, _OptionalEnableBaselineInputRequestTypeDef
):
    pass

EnableBaselineOutputTypeDef = TypedDict(
    "EnableBaselineOutputTypeDef",
    {
        "arn": str,
        "operationIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "parameters": List["EnabledControlParameterTypeDef"],
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

_RequiredEnabledBaselineDetailsTypeDef = TypedDict(
    "_RequiredEnabledBaselineDetailsTypeDef",
    {
        "arn": str,
        "baselineIdentifier": str,
        "statusSummary": "EnablementStatusSummaryTypeDef",
        "targetIdentifier": str,
    },
)
_OptionalEnabledBaselineDetailsTypeDef = TypedDict(
    "_OptionalEnabledBaselineDetailsTypeDef",
    {
        "baselineVersion": str,
        "parameters": List["EnabledBaselineParameterSummaryTypeDef"],
    },
    total=False,
)

class EnabledBaselineDetailsTypeDef(
    _RequiredEnabledBaselineDetailsTypeDef, _OptionalEnabledBaselineDetailsTypeDef
):
    pass

EnabledBaselineFilterTypeDef = TypedDict(
    "EnabledBaselineFilterTypeDef",
    {
        "baselineIdentifiers": List[str],
        "targetIdentifiers": List[str],
    },
    total=False,
)

EnabledBaselineParameterSummaryTypeDef = TypedDict(
    "EnabledBaselineParameterSummaryTypeDef",
    {
        "key": str,
        "value": Dict[str, Any],
    },
)

EnabledBaselineParameterTypeDef = TypedDict(
    "EnabledBaselineParameterTypeDef",
    {
        "key": str,
        "value": Dict[str, Any],
    },
)

_RequiredEnabledBaselineSummaryTypeDef = TypedDict(
    "_RequiredEnabledBaselineSummaryTypeDef",
    {
        "arn": str,
        "baselineIdentifier": str,
        "statusSummary": "EnablementStatusSummaryTypeDef",
        "targetIdentifier": str,
    },
)
_OptionalEnabledBaselineSummaryTypeDef = TypedDict(
    "_OptionalEnabledBaselineSummaryTypeDef",
    {
        "baselineVersion": str,
    },
    total=False,
)

class EnabledBaselineSummaryTypeDef(
    _RequiredEnabledBaselineSummaryTypeDef, _OptionalEnabledBaselineSummaryTypeDef
):
    pass

EnabledControlDetailsTypeDef = TypedDict(
    "EnabledControlDetailsTypeDef",
    {
        "arn": str,
        "controlIdentifier": str,
        "driftStatusSummary": "DriftStatusSummaryTypeDef",
        "parameters": List["EnabledControlParameterSummaryTypeDef"],
        "statusSummary": "EnablementStatusSummaryTypeDef",
        "targetIdentifier": str,
        "targetRegions": List["RegionTypeDef"],
    },
    total=False,
)

EnabledControlFilterTypeDef = TypedDict(
    "EnabledControlFilterTypeDef",
    {
        "controlIdentifiers": List[str],
        "driftStatuses": List[DriftStatusType],
        "statuses": List[EnablementStatusType],
    },
    total=False,
)

EnabledControlParameterSummaryTypeDef = TypedDict(
    "EnabledControlParameterSummaryTypeDef",
    {
        "key": str,
        "value": Dict[str, Any],
    },
)

EnabledControlParameterTypeDef = TypedDict(
    "EnabledControlParameterTypeDef",
    {
        "key": str,
        "value": Dict[str, Any],
    },
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

GetBaselineInputRequestTypeDef = TypedDict(
    "GetBaselineInputRequestTypeDef",
    {
        "baselineIdentifier": str,
    },
)

GetBaselineOperationInputRequestTypeDef = TypedDict(
    "GetBaselineOperationInputRequestTypeDef",
    {
        "operationIdentifier": str,
    },
)

GetBaselineOperationOutputTypeDef = TypedDict(
    "GetBaselineOperationOutputTypeDef",
    {
        "baselineOperation": "BaselineOperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBaselineOutputTypeDef = TypedDict(
    "GetBaselineOutputTypeDef",
    {
        "arn": str,
        "description": str,
        "name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

GetEnabledBaselineInputRequestTypeDef = TypedDict(
    "GetEnabledBaselineInputRequestTypeDef",
    {
        "enabledBaselineIdentifier": str,
    },
)

GetEnabledBaselineOutputTypeDef = TypedDict(
    "GetEnabledBaselineOutputTypeDef",
    {
        "enabledBaselineDetails": "EnabledBaselineDetailsTypeDef",
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

ListBaselinesInputRequestTypeDef = TypedDict(
    "ListBaselinesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListBaselinesOutputTypeDef = TypedDict(
    "ListBaselinesOutputTypeDef",
    {
        "baselines": List["BaselineSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListControlOperationsInputRequestTypeDef = TypedDict(
    "ListControlOperationsInputRequestTypeDef",
    {
        "filter": "ControlOperationFilterTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListControlOperationsOutputTypeDef = TypedDict(
    "ListControlOperationsOutputTypeDef",
    {
        "controlOperations": List["ControlOperationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEnabledBaselinesInputRequestTypeDef = TypedDict(
    "ListEnabledBaselinesInputRequestTypeDef",
    {
        "filter": "EnabledBaselineFilterTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListEnabledBaselinesOutputTypeDef = TypedDict(
    "ListEnabledBaselinesOutputTypeDef",
    {
        "enabledBaselines": List["EnabledBaselineSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEnabledControlsInputRequestTypeDef = TypedDict(
    "ListEnabledControlsInputRequestTypeDef",
    {
        "filter": "EnabledControlFilterTypeDef",
        "maxResults": int,
        "nextToken": str,
        "targetIdentifier": str,
    },
    total=False,
)

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

ResetEnabledBaselineInputRequestTypeDef = TypedDict(
    "ResetEnabledBaselineInputRequestTypeDef",
    {
        "enabledBaselineIdentifier": str,
    },
)

ResetEnabledBaselineOutputTypeDef = TypedDict(
    "ResetEnabledBaselineOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredUpdateEnabledBaselineInputRequestTypeDef = TypedDict(
    "_RequiredUpdateEnabledBaselineInputRequestTypeDef",
    {
        "baselineVersion": str,
        "enabledBaselineIdentifier": str,
    },
)
_OptionalUpdateEnabledBaselineInputRequestTypeDef = TypedDict(
    "_OptionalUpdateEnabledBaselineInputRequestTypeDef",
    {
        "parameters": List["EnabledBaselineParameterTypeDef"],
    },
    total=False,
)

class UpdateEnabledBaselineInputRequestTypeDef(
    _RequiredUpdateEnabledBaselineInputRequestTypeDef,
    _OptionalUpdateEnabledBaselineInputRequestTypeDef,
):
    pass

UpdateEnabledBaselineOutputTypeDef = TypedDict(
    "UpdateEnabledBaselineOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEnabledControlInputRequestTypeDef = TypedDict(
    "UpdateEnabledControlInputRequestTypeDef",
    {
        "enabledControlIdentifier": str,
        "parameters": List["EnabledControlParameterTypeDef"],
    },
)

UpdateEnabledControlOutputTypeDef = TypedDict(
    "UpdateEnabledControlOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
