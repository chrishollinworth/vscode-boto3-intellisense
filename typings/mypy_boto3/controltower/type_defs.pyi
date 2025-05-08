"""
Type annotations for controltower service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_controltower.type_defs import BaselineOperationTypeDef

    data: BaselineOperationTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any

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
    "BaselineOperationTypeDef",
    "BaselineSummaryTypeDef",
    "ControlOperationFilterTypeDef",
    "ControlOperationSummaryTypeDef",
    "ControlOperationTypeDef",
    "CreateLandingZoneInputTypeDef",
    "CreateLandingZoneOutputTypeDef",
    "DeleteLandingZoneInputTypeDef",
    "DeleteLandingZoneOutputTypeDef",
    "DisableBaselineInputTypeDef",
    "DisableBaselineOutputTypeDef",
    "DisableControlInputTypeDef",
    "DisableControlOutputTypeDef",
    "DriftStatusSummaryTypeDef",
    "EnableBaselineInputTypeDef",
    "EnableBaselineOutputTypeDef",
    "EnableControlInputTypeDef",
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
    "GetBaselineInputTypeDef",
    "GetBaselineOperationInputTypeDef",
    "GetBaselineOperationOutputTypeDef",
    "GetBaselineOutputTypeDef",
    "GetControlOperationInputTypeDef",
    "GetControlOperationOutputTypeDef",
    "GetEnabledBaselineInputTypeDef",
    "GetEnabledBaselineOutputTypeDef",
    "GetEnabledControlInputTypeDef",
    "GetEnabledControlOutputTypeDef",
    "GetLandingZoneInputTypeDef",
    "GetLandingZoneOperationInputTypeDef",
    "GetLandingZoneOperationOutputTypeDef",
    "GetLandingZoneOutputTypeDef",
    "LandingZoneDetailTypeDef",
    "LandingZoneDriftStatusSummaryTypeDef",
    "LandingZoneOperationDetailTypeDef",
    "LandingZoneOperationFilterTypeDef",
    "LandingZoneOperationSummaryTypeDef",
    "LandingZoneSummaryTypeDef",
    "ListBaselinesInputPaginateTypeDef",
    "ListBaselinesInputTypeDef",
    "ListBaselinesOutputTypeDef",
    "ListControlOperationsInputPaginateTypeDef",
    "ListControlOperationsInputTypeDef",
    "ListControlOperationsOutputTypeDef",
    "ListEnabledBaselinesInputPaginateTypeDef",
    "ListEnabledBaselinesInputTypeDef",
    "ListEnabledBaselinesOutputTypeDef",
    "ListEnabledControlsInputPaginateTypeDef",
    "ListEnabledControlsInputTypeDef",
    "ListEnabledControlsOutputTypeDef",
    "ListLandingZoneOperationsInputPaginateTypeDef",
    "ListLandingZoneOperationsInputTypeDef",
    "ListLandingZoneOperationsOutputTypeDef",
    "ListLandingZonesInputPaginateTypeDef",
    "ListLandingZonesInputTypeDef",
    "ListLandingZonesOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "PaginatorConfigTypeDef",
    "RegionTypeDef",
    "ResetEnabledBaselineInputTypeDef",
    "ResetEnabledBaselineOutputTypeDef",
    "ResetEnabledControlInputTypeDef",
    "ResetEnabledControlOutputTypeDef",
    "ResetLandingZoneInputTypeDef",
    "ResetLandingZoneOutputTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceInputTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateEnabledBaselineInputTypeDef",
    "UpdateEnabledBaselineOutputTypeDef",
    "UpdateEnabledControlInputTypeDef",
    "UpdateEnabledControlOutputTypeDef",
    "UpdateLandingZoneInputTypeDef",
    "UpdateLandingZoneOutputTypeDef",
)

class BaselineOperationTypeDef(TypedDict):
    endTime: NotRequired[datetime]
    operationIdentifier: NotRequired[str]
    operationType: NotRequired[BaselineOperationTypeType]
    startTime: NotRequired[datetime]
    status: NotRequired[BaselineOperationStatusType]
    statusMessage: NotRequired[str]

class BaselineSummaryTypeDef(TypedDict):
    arn: str
    name: str
    description: NotRequired[str]

class ControlOperationFilterTypeDef(TypedDict):
    controlIdentifiers: NotRequired[Sequence[str]]
    controlOperationTypes: NotRequired[Sequence[ControlOperationTypeType]]
    enabledControlIdentifiers: NotRequired[Sequence[str]]
    statuses: NotRequired[Sequence[ControlOperationStatusType]]
    targetIdentifiers: NotRequired[Sequence[str]]

class ControlOperationSummaryTypeDef(TypedDict):
    controlIdentifier: NotRequired[str]
    enabledControlIdentifier: NotRequired[str]
    endTime: NotRequired[datetime]
    operationIdentifier: NotRequired[str]
    operationType: NotRequired[ControlOperationTypeType]
    startTime: NotRequired[datetime]
    status: NotRequired[ControlOperationStatusType]
    statusMessage: NotRequired[str]
    targetIdentifier: NotRequired[str]

class ControlOperationTypeDef(TypedDict):
    controlIdentifier: NotRequired[str]
    enabledControlIdentifier: NotRequired[str]
    endTime: NotRequired[datetime]
    operationIdentifier: NotRequired[str]
    operationType: NotRequired[ControlOperationTypeType]
    startTime: NotRequired[datetime]
    status: NotRequired[ControlOperationStatusType]
    statusMessage: NotRequired[str]
    targetIdentifier: NotRequired[str]

class CreateLandingZoneInputTypeDef(TypedDict):
    manifest: Mapping[str, Any]
    version: str
    tags: NotRequired[Mapping[str, str]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteLandingZoneInputTypeDef(TypedDict):
    landingZoneIdentifier: str

class DisableBaselineInputTypeDef(TypedDict):
    enabledBaselineIdentifier: str

class DisableControlInputTypeDef(TypedDict):
    controlIdentifier: str
    targetIdentifier: str

class DriftStatusSummaryTypeDef(TypedDict):
    driftStatus: NotRequired[DriftStatusType]

class EnabledBaselineParameterTypeDef(TypedDict):
    key: str
    value: Mapping[str, Any]

class EnabledControlParameterTypeDef(TypedDict):
    key: str
    value: Mapping[str, Any]

class EnabledBaselineParameterSummaryTypeDef(TypedDict):
    key: str
    value: Dict[str, Any]

class EnablementStatusSummaryTypeDef(TypedDict):
    lastOperationIdentifier: NotRequired[str]
    status: NotRequired[EnablementStatusType]

class EnabledBaselineFilterTypeDef(TypedDict):
    baselineIdentifiers: NotRequired[Sequence[str]]
    parentIdentifiers: NotRequired[Sequence[str]]
    targetIdentifiers: NotRequired[Sequence[str]]

class EnabledControlParameterSummaryTypeDef(TypedDict):
    key: str
    value: Dict[str, Any]

class RegionTypeDef(TypedDict):
    name: NotRequired[str]

class EnabledControlFilterTypeDef(TypedDict):
    controlIdentifiers: NotRequired[Sequence[str]]
    driftStatuses: NotRequired[Sequence[DriftStatusType]]
    statuses: NotRequired[Sequence[EnablementStatusType]]

class GetBaselineInputTypeDef(TypedDict):
    baselineIdentifier: str

class GetBaselineOperationInputTypeDef(TypedDict):
    operationIdentifier: str

class GetControlOperationInputTypeDef(TypedDict):
    operationIdentifier: str

class GetEnabledBaselineInputTypeDef(TypedDict):
    enabledBaselineIdentifier: str

class GetEnabledControlInputTypeDef(TypedDict):
    enabledControlIdentifier: str

class GetLandingZoneInputTypeDef(TypedDict):
    landingZoneIdentifier: str

class GetLandingZoneOperationInputTypeDef(TypedDict):
    operationIdentifier: str

class LandingZoneOperationDetailTypeDef(TypedDict):
    endTime: NotRequired[datetime]
    operationIdentifier: NotRequired[str]
    operationType: NotRequired[LandingZoneOperationTypeType]
    startTime: NotRequired[datetime]
    status: NotRequired[LandingZoneOperationStatusType]
    statusMessage: NotRequired[str]

class LandingZoneDriftStatusSummaryTypeDef(TypedDict):
    status: NotRequired[LandingZoneDriftStatusType]

LandingZoneOperationFilterTypeDef = TypedDict(
    "LandingZoneOperationFilterTypeDef",
    {
        "statuses": NotRequired[Sequence[LandingZoneOperationStatusType]],
        "types": NotRequired[Sequence[LandingZoneOperationTypeType]],
    },
)

class LandingZoneOperationSummaryTypeDef(TypedDict):
    operationIdentifier: NotRequired[str]
    operationType: NotRequired[LandingZoneOperationTypeType]
    status: NotRequired[LandingZoneOperationStatusType]

class LandingZoneSummaryTypeDef(TypedDict):
    arn: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListBaselinesInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListLandingZonesInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceInputTypeDef(TypedDict):
    resourceArn: str

class ResetEnabledBaselineInputTypeDef(TypedDict):
    enabledBaselineIdentifier: str

class ResetEnabledControlInputTypeDef(TypedDict):
    enabledControlIdentifier: str

class ResetLandingZoneInputTypeDef(TypedDict):
    landingZoneIdentifier: str

class TagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateLandingZoneInputTypeDef(TypedDict):
    landingZoneIdentifier: str
    manifest: Mapping[str, Any]
    version: str

ListControlOperationsInputTypeDef = TypedDict(
    "ListControlOperationsInputTypeDef",
    {
        "filter": NotRequired[ControlOperationFilterTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

class CreateLandingZoneOutputTypeDef(TypedDict):
    arn: str
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLandingZoneOutputTypeDef(TypedDict):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableBaselineOutputTypeDef(TypedDict):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableControlOutputTypeDef(TypedDict):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnableBaselineOutputTypeDef(TypedDict):
    arn: str
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnableControlOutputTypeDef(TypedDict):
    arn: str
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBaselineOperationOutputTypeDef(TypedDict):
    baselineOperation: BaselineOperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBaselineOutputTypeDef(TypedDict):
    arn: str
    description: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetControlOperationOutputTypeDef(TypedDict):
    controlOperation: ControlOperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListBaselinesOutputTypeDef(TypedDict):
    baselines: List[BaselineSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListControlOperationsOutputTypeDef(TypedDict):
    controlOperations: List[ControlOperationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ResetEnabledBaselineOutputTypeDef(TypedDict):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResetEnabledControlOutputTypeDef(TypedDict):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResetLandingZoneOutputTypeDef(TypedDict):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnabledBaselineOutputTypeDef(TypedDict):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnabledControlOutputTypeDef(TypedDict):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLandingZoneOutputTypeDef(TypedDict):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnableBaselineInputTypeDef(TypedDict):
    baselineIdentifier: str
    baselineVersion: str
    targetIdentifier: str
    parameters: NotRequired[Sequence[EnabledBaselineParameterTypeDef]]
    tags: NotRequired[Mapping[str, str]]

class UpdateEnabledBaselineInputTypeDef(TypedDict):
    baselineVersion: str
    enabledBaselineIdentifier: str
    parameters: NotRequired[Sequence[EnabledBaselineParameterTypeDef]]

class EnableControlInputTypeDef(TypedDict):
    controlIdentifier: str
    targetIdentifier: str
    parameters: NotRequired[Sequence[EnabledControlParameterTypeDef]]
    tags: NotRequired[Mapping[str, str]]

class UpdateEnabledControlInputTypeDef(TypedDict):
    enabledControlIdentifier: str
    parameters: Sequence[EnabledControlParameterTypeDef]

class EnabledBaselineDetailsTypeDef(TypedDict):
    arn: str
    baselineIdentifier: str
    statusSummary: EnablementStatusSummaryTypeDef
    targetIdentifier: str
    baselineVersion: NotRequired[str]
    parameters: NotRequired[List[EnabledBaselineParameterSummaryTypeDef]]
    parentIdentifier: NotRequired[str]

class EnabledBaselineSummaryTypeDef(TypedDict):
    arn: str
    baselineIdentifier: str
    statusSummary: EnablementStatusSummaryTypeDef
    targetIdentifier: str
    baselineVersion: NotRequired[str]
    parentIdentifier: NotRequired[str]

class EnabledControlSummaryTypeDef(TypedDict):
    arn: NotRequired[str]
    controlIdentifier: NotRequired[str]
    driftStatusSummary: NotRequired[DriftStatusSummaryTypeDef]
    statusSummary: NotRequired[EnablementStatusSummaryTypeDef]
    targetIdentifier: NotRequired[str]

ListEnabledBaselinesInputTypeDef = TypedDict(
    "ListEnabledBaselinesInputTypeDef",
    {
        "filter": NotRequired[EnabledBaselineFilterTypeDef],
        "includeChildren": NotRequired[bool],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

class EnabledControlDetailsTypeDef(TypedDict):
    arn: NotRequired[str]
    controlIdentifier: NotRequired[str]
    driftStatusSummary: NotRequired[DriftStatusSummaryTypeDef]
    parameters: NotRequired[List[EnabledControlParameterSummaryTypeDef]]
    statusSummary: NotRequired[EnablementStatusSummaryTypeDef]
    targetIdentifier: NotRequired[str]
    targetRegions: NotRequired[List[RegionTypeDef]]

ListEnabledControlsInputTypeDef = TypedDict(
    "ListEnabledControlsInputTypeDef",
    {
        "filter": NotRequired[EnabledControlFilterTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "targetIdentifier": NotRequired[str],
    },
)

class GetLandingZoneOperationOutputTypeDef(TypedDict):
    operationDetails: LandingZoneOperationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LandingZoneDetailTypeDef(TypedDict):
    manifest: Dict[str, Any]
    version: str
    arn: NotRequired[str]
    driftStatus: NotRequired[LandingZoneDriftStatusSummaryTypeDef]
    latestAvailableVersion: NotRequired[str]
    status: NotRequired[LandingZoneStatusType]

ListLandingZoneOperationsInputTypeDef = TypedDict(
    "ListLandingZoneOperationsInputTypeDef",
    {
        "filter": NotRequired[LandingZoneOperationFilterTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

class ListLandingZoneOperationsOutputTypeDef(TypedDict):
    landingZoneOperations: List[LandingZoneOperationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListLandingZonesOutputTypeDef(TypedDict):
    landingZones: List[LandingZoneSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListBaselinesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListControlOperationsInputPaginateTypeDef = TypedDict(
    "ListControlOperationsInputPaginateTypeDef",
    {
        "filter": NotRequired[ControlOperationFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnabledBaselinesInputPaginateTypeDef = TypedDict(
    "ListEnabledBaselinesInputPaginateTypeDef",
    {
        "filter": NotRequired[EnabledBaselineFilterTypeDef],
        "includeChildren": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnabledControlsInputPaginateTypeDef = TypedDict(
    "ListEnabledControlsInputPaginateTypeDef",
    {
        "filter": NotRequired[EnabledControlFilterTypeDef],
        "targetIdentifier": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLandingZoneOperationsInputPaginateTypeDef = TypedDict(
    "ListLandingZoneOperationsInputPaginateTypeDef",
    {
        "filter": NotRequired[LandingZoneOperationFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListLandingZonesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetEnabledBaselineOutputTypeDef(TypedDict):
    enabledBaselineDetails: EnabledBaselineDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnabledBaselinesOutputTypeDef(TypedDict):
    enabledBaselines: List[EnabledBaselineSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListEnabledControlsOutputTypeDef(TypedDict):
    enabledControls: List[EnabledControlSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetEnabledControlOutputTypeDef(TypedDict):
    enabledControlDetails: EnabledControlDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLandingZoneOutputTypeDef(TypedDict):
    landingZone: LandingZoneDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
