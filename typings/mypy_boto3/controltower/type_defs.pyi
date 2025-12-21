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
    EnabledBaselineDriftStatusType,
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
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

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
    "EnabledBaselineDriftStatusSummaryTypeDef",
    "EnabledBaselineDriftTypesTypeDef",
    "EnabledBaselineFilterTypeDef",
    "EnabledBaselineInheritanceDriftTypeDef",
    "EnabledBaselineParameterSummaryTypeDef",
    "EnabledBaselineParameterTypeDef",
    "EnabledBaselineSummaryTypeDef",
    "EnabledControlDetailsTypeDef",
    "EnabledControlDriftTypesTypeDef",
    "EnabledControlFilterTypeDef",
    "EnabledControlInheritanceDriftTypeDef",
    "EnabledControlParameterSummaryTypeDef",
    "EnabledControlParameterTypeDef",
    "EnabledControlResourceDriftTypeDef",
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
    operationIdentifier: NotRequired[str]
    operationType: NotRequired[BaselineOperationTypeType]
    status: NotRequired[BaselineOperationStatusType]
    startTime: NotRequired[datetime]
    endTime: NotRequired[datetime]
    statusMessage: NotRequired[str]

class BaselineSummaryTypeDef(TypedDict):
    arn: str
    name: str
    description: NotRequired[str]

class ControlOperationFilterTypeDef(TypedDict):
    controlIdentifiers: NotRequired[Sequence[str]]
    targetIdentifiers: NotRequired[Sequence[str]]
    enabledControlIdentifiers: NotRequired[Sequence[str]]
    statuses: NotRequired[Sequence[ControlOperationStatusType]]
    controlOperationTypes: NotRequired[Sequence[ControlOperationTypeType]]

class ControlOperationSummaryTypeDef(TypedDict):
    operationType: NotRequired[ControlOperationTypeType]
    startTime: NotRequired[datetime]
    endTime: NotRequired[datetime]
    status: NotRequired[ControlOperationStatusType]
    statusMessage: NotRequired[str]
    operationIdentifier: NotRequired[str]
    controlIdentifier: NotRequired[str]
    targetIdentifier: NotRequired[str]
    enabledControlIdentifier: NotRequired[str]

class ControlOperationTypeDef(TypedDict):
    operationType: NotRequired[ControlOperationTypeType]
    startTime: NotRequired[datetime]
    endTime: NotRequired[datetime]
    status: NotRequired[ControlOperationStatusType]
    statusMessage: NotRequired[str]
    operationIdentifier: NotRequired[str]
    controlIdentifier: NotRequired[str]
    targetIdentifier: NotRequired[str]
    enabledControlIdentifier: NotRequired[str]

class CreateLandingZoneInputTypeDef(TypedDict):
    version: str
    remediationTypes: NotRequired[Sequence[Literal["INHERITANCE_DRIFT"]]]
    tags: NotRequired[Mapping[str, str]]
    manifest: NotRequired[Mapping[str, Any]]

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
    controlIdentifier: NotRequired[str]
    targetIdentifier: NotRequired[str]
    enabledControlIdentifier: NotRequired[str]

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
    status: NotRequired[EnablementStatusType]
    lastOperationIdentifier: NotRequired[str]

class EnabledBaselineInheritanceDriftTypeDef(TypedDict):
    status: NotRequired[EnabledBaselineDriftStatusType]

class EnabledBaselineFilterTypeDef(TypedDict):
    targetIdentifiers: NotRequired[Sequence[str]]
    baselineIdentifiers: NotRequired[Sequence[str]]
    parentIdentifiers: NotRequired[Sequence[str]]
    statuses: NotRequired[Sequence[EnablementStatusType]]
    inheritanceDriftStatuses: NotRequired[Sequence[EnabledBaselineDriftStatusType]]

class EnabledControlParameterSummaryTypeDef(TypedDict):
    key: str
    value: Dict[str, Any]

class RegionTypeDef(TypedDict):
    name: NotRequired[str]

class EnabledControlInheritanceDriftTypeDef(TypedDict):
    status: NotRequired[DriftStatusType]

class EnabledControlResourceDriftTypeDef(TypedDict):
    status: NotRequired[DriftStatusType]

class EnabledControlFilterTypeDef(TypedDict):
    controlIdentifiers: NotRequired[Sequence[str]]
    statuses: NotRequired[Sequence[EnablementStatusType]]
    driftStatuses: NotRequired[Sequence[DriftStatusType]]
    parentIdentifiers: NotRequired[Sequence[str]]
    inheritanceDriftStatuses: NotRequired[Sequence[DriftStatusType]]
    resourceDriftStatuses: NotRequired[Sequence[DriftStatusType]]

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
    operationType: NotRequired[LandingZoneOperationTypeType]
    operationIdentifier: NotRequired[str]
    status: NotRequired[LandingZoneOperationStatusType]
    startTime: NotRequired[datetime]
    endTime: NotRequired[datetime]
    statusMessage: NotRequired[str]

class LandingZoneDriftStatusSummaryTypeDef(TypedDict):
    status: NotRequired[LandingZoneDriftStatusType]

LandingZoneOperationFilterTypeDef = TypedDict(
    "LandingZoneOperationFilterTypeDef",
    {
        "types": NotRequired[Sequence[LandingZoneOperationTypeType]],
        "statuses": NotRequired[Sequence[LandingZoneOperationStatusType]],
    },
)

class LandingZoneOperationSummaryTypeDef(TypedDict):
    operationType: NotRequired[LandingZoneOperationTypeType]
    operationIdentifier: NotRequired[str]
    status: NotRequired[LandingZoneOperationStatusType]

class LandingZoneSummaryTypeDef(TypedDict):
    arn: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListBaselinesInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListLandingZonesInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

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
    version: str
    landingZoneIdentifier: str
    remediationTypes: NotRequired[Sequence[Literal["INHERITANCE_DRIFT"]]]
    manifest: NotRequired[Mapping[str, Any]]

ListControlOperationsInputTypeDef = TypedDict(
    "ListControlOperationsInputTypeDef",
    {
        "filter": NotRequired[ControlOperationFilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
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
    operationIdentifier: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnableControlOutputTypeDef(TypedDict):
    operationIdentifier: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBaselineOperationOutputTypeDef(TypedDict):
    baselineOperation: BaselineOperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBaselineOutputTypeDef(TypedDict):
    arn: str
    name: str
    description: str
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
    baselineVersion: str
    baselineIdentifier: str
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
    tags: NotRequired[Mapping[str, str]]
    parameters: NotRequired[Sequence[EnabledControlParameterTypeDef]]

class UpdateEnabledControlInputTypeDef(TypedDict):
    parameters: Sequence[EnabledControlParameterTypeDef]
    enabledControlIdentifier: str

class EnabledBaselineDriftTypesTypeDef(TypedDict):
    inheritance: NotRequired[EnabledBaselineInheritanceDriftTypeDef]

ListEnabledBaselinesInputTypeDef = TypedDict(
    "ListEnabledBaselinesInputTypeDef",
    {
        "filter": NotRequired[EnabledBaselineFilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "includeChildren": NotRequired[bool],
    },
)

class EnabledControlDriftTypesTypeDef(TypedDict):
    inheritance: NotRequired[EnabledControlInheritanceDriftTypeDef]
    resource: NotRequired[EnabledControlResourceDriftTypeDef]

ListEnabledControlsInputTypeDef = TypedDict(
    "ListEnabledControlsInputTypeDef",
    {
        "targetIdentifier": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filter": NotRequired[EnabledControlFilterTypeDef],
        "includeChildren": NotRequired[bool],
    },
)

class GetLandingZoneOperationOutputTypeDef(TypedDict):
    operationDetails: LandingZoneOperationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LandingZoneDetailTypeDef(TypedDict):
    version: str
    manifest: Dict[str, Any]
    remediationTypes: NotRequired[List[Literal["INHERITANCE_DRIFT"]]]
    arn: NotRequired[str]
    status: NotRequired[LandingZoneStatusType]
    latestAvailableVersion: NotRequired[str]
    driftStatus: NotRequired[LandingZoneDriftStatusSummaryTypeDef]

ListLandingZoneOperationsInputTypeDef = TypedDict(
    "ListLandingZoneOperationsInputTypeDef",
    {
        "filter": NotRequired[LandingZoneOperationFilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
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
        "targetIdentifier": NotRequired[str],
        "filter": NotRequired[EnabledControlFilterTypeDef],
        "includeChildren": NotRequired[bool],
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

EnabledBaselineDriftStatusSummaryTypeDef = TypedDict(
    "EnabledBaselineDriftStatusSummaryTypeDef",
    {
        "types": NotRequired[EnabledBaselineDriftTypesTypeDef],
    },
)
DriftStatusSummaryTypeDef = TypedDict(
    "DriftStatusSummaryTypeDef",
    {
        "driftStatus": NotRequired[DriftStatusType],
        "types": NotRequired[EnabledControlDriftTypesTypeDef],
    },
)

class GetLandingZoneOutputTypeDef(TypedDict):
    landingZone: LandingZoneDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnabledBaselineDetailsTypeDef(TypedDict):
    arn: str
    baselineIdentifier: str
    targetIdentifier: str
    statusSummary: EnablementStatusSummaryTypeDef
    baselineVersion: NotRequired[str]
    driftStatusSummary: NotRequired[EnabledBaselineDriftStatusSummaryTypeDef]
    parentIdentifier: NotRequired[str]
    parameters: NotRequired[List[EnabledBaselineParameterSummaryTypeDef]]

class EnabledBaselineSummaryTypeDef(TypedDict):
    arn: str
    baselineIdentifier: str
    targetIdentifier: str
    statusSummary: EnablementStatusSummaryTypeDef
    baselineVersion: NotRequired[str]
    driftStatusSummary: NotRequired[EnabledBaselineDriftStatusSummaryTypeDef]
    parentIdentifier: NotRequired[str]

class EnabledControlDetailsTypeDef(TypedDict):
    arn: NotRequired[str]
    controlIdentifier: NotRequired[str]
    targetIdentifier: NotRequired[str]
    statusSummary: NotRequired[EnablementStatusSummaryTypeDef]
    driftStatusSummary: NotRequired[DriftStatusSummaryTypeDef]
    parentIdentifier: NotRequired[str]
    targetRegions: NotRequired[List[RegionTypeDef]]
    parameters: NotRequired[List[EnabledControlParameterSummaryTypeDef]]

class EnabledControlSummaryTypeDef(TypedDict):
    arn: NotRequired[str]
    controlIdentifier: NotRequired[str]
    targetIdentifier: NotRequired[str]
    statusSummary: NotRequired[EnablementStatusSummaryTypeDef]
    driftStatusSummary: NotRequired[DriftStatusSummaryTypeDef]
    parentIdentifier: NotRequired[str]

class GetEnabledBaselineOutputTypeDef(TypedDict):
    enabledBaselineDetails: EnabledBaselineDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnabledBaselinesOutputTypeDef(TypedDict):
    enabledBaselines: List[EnabledBaselineSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetEnabledControlOutputTypeDef(TypedDict):
    enabledControlDetails: EnabledControlDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnabledControlsOutputTypeDef(TypedDict):
    enabledControls: List[EnabledControlSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
