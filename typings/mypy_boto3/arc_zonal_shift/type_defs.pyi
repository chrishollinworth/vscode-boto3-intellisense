"""
Type annotations for arc-zonal-shift service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_arc_zonal_shift.type_defs import AutoshiftInResourceTypeDef

    data: AutoshiftInResourceTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    AppliedStatusType,
    AutoshiftAppliedStatusType,
    AutoshiftExecutionStatusType,
    AutoshiftObserverNotificationStatusType,
    PracticeRunOutcomeType,
    ShiftTypeType,
    ZonalAutoshiftStatusType,
    ZonalShiftStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AutoshiftInResourceTypeDef",
    "AutoshiftSummaryTypeDef",
    "CancelPracticeRunRequestTypeDef",
    "CancelPracticeRunResponseTypeDef",
    "CancelZonalShiftRequestTypeDef",
    "ControlConditionTypeDef",
    "CreatePracticeRunConfigurationRequestTypeDef",
    "CreatePracticeRunConfigurationResponseTypeDef",
    "DeletePracticeRunConfigurationRequestTypeDef",
    "DeletePracticeRunConfigurationResponseTypeDef",
    "GetAutoshiftObserverNotificationStatusResponseTypeDef",
    "GetManagedResourceRequestTypeDef",
    "GetManagedResourceResponseTypeDef",
    "ListAutoshiftsRequestPaginateTypeDef",
    "ListAutoshiftsRequestTypeDef",
    "ListAutoshiftsResponseTypeDef",
    "ListManagedResourcesRequestPaginateTypeDef",
    "ListManagedResourcesRequestTypeDef",
    "ListManagedResourcesResponseTypeDef",
    "ListZonalShiftsRequestPaginateTypeDef",
    "ListZonalShiftsRequestTypeDef",
    "ListZonalShiftsResponseTypeDef",
    "ManagedResourceSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "PracticeRunConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "StartPracticeRunRequestTypeDef",
    "StartPracticeRunResponseTypeDef",
    "StartZonalShiftRequestTypeDef",
    "UpdateAutoshiftObserverNotificationStatusRequestTypeDef",
    "UpdateAutoshiftObserverNotificationStatusResponseTypeDef",
    "UpdatePracticeRunConfigurationRequestTypeDef",
    "UpdatePracticeRunConfigurationResponseTypeDef",
    "UpdateZonalAutoshiftConfigurationRequestTypeDef",
    "UpdateZonalAutoshiftConfigurationResponseTypeDef",
    "UpdateZonalShiftRequestTypeDef",
    "ZonalShiftInResourceTypeDef",
    "ZonalShiftSummaryTypeDef",
    "ZonalShiftTypeDef",
)

class AutoshiftInResourceTypeDef(TypedDict):
    appliedStatus: AutoshiftAppliedStatusType
    awayFrom: str
    startTime: datetime

class AutoshiftSummaryTypeDef(TypedDict):
    awayFrom: str
    startTime: datetime
    status: AutoshiftExecutionStatusType
    endTime: NotRequired[datetime]

class CancelPracticeRunRequestTypeDef(TypedDict):
    zonalShiftId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CancelZonalShiftRequestTypeDef(TypedDict):
    zonalShiftId: str

ControlConditionTypeDef = TypedDict(
    "ControlConditionTypeDef",
    {
        "type": Literal["CLOUDWATCH"],
        "alarmIdentifier": str,
    },
)

class DeletePracticeRunConfigurationRequestTypeDef(TypedDict):
    resourceIdentifier: str

class GetManagedResourceRequestTypeDef(TypedDict):
    resourceIdentifier: str

class ZonalShiftInResourceTypeDef(TypedDict):
    appliedStatus: AppliedStatusType
    zonalShiftId: str
    resourceIdentifier: str
    awayFrom: str
    expiryTime: datetime
    startTime: datetime
    comment: str
    shiftType: NotRequired[ShiftTypeType]
    practiceRunOutcome: NotRequired[PracticeRunOutcomeType]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAutoshiftsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    status: NotRequired[AutoshiftExecutionStatusType]
    maxResults: NotRequired[int]

class ListManagedResourcesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListZonalShiftsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    status: NotRequired[ZonalShiftStatusType]
    maxResults: NotRequired[int]
    resourceIdentifier: NotRequired[str]

class ZonalShiftSummaryTypeDef(TypedDict):
    zonalShiftId: str
    resourceIdentifier: str
    awayFrom: str
    expiryTime: datetime
    startTime: datetime
    status: ZonalShiftStatusType
    comment: str
    shiftType: NotRequired[ShiftTypeType]
    practiceRunOutcome: NotRequired[PracticeRunOutcomeType]

class StartPracticeRunRequestTypeDef(TypedDict):
    resourceIdentifier: str
    awayFrom: str
    comment: str

class StartZonalShiftRequestTypeDef(TypedDict):
    resourceIdentifier: str
    awayFrom: str
    expiresIn: str
    comment: str

class UpdateAutoshiftObserverNotificationStatusRequestTypeDef(TypedDict):
    status: AutoshiftObserverNotificationStatusType

class UpdateZonalAutoshiftConfigurationRequestTypeDef(TypedDict):
    resourceIdentifier: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType

class UpdateZonalShiftRequestTypeDef(TypedDict):
    zonalShiftId: str
    comment: NotRequired[str]
    expiresIn: NotRequired[str]

class CancelPracticeRunResponseTypeDef(TypedDict):
    zonalShiftId: str
    resourceIdentifier: str
    awayFrom: str
    expiryTime: datetime
    startTime: datetime
    status: ZonalShiftStatusType
    comment: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePracticeRunConfigurationResponseTypeDef(TypedDict):
    arn: str
    name: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetAutoshiftObserverNotificationStatusResponseTypeDef(TypedDict):
    status: AutoshiftObserverNotificationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListAutoshiftsResponseTypeDef(TypedDict):
    items: List[AutoshiftSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartPracticeRunResponseTypeDef(TypedDict):
    zonalShiftId: str
    resourceIdentifier: str
    awayFrom: str
    expiryTime: datetime
    startTime: datetime
    status: ZonalShiftStatusType
    comment: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAutoshiftObserverNotificationStatusResponseTypeDef(TypedDict):
    status: AutoshiftObserverNotificationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateZonalAutoshiftConfigurationResponseTypeDef(TypedDict):
    resourceIdentifier: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ZonalShiftTypeDef(TypedDict):
    zonalShiftId: str
    resourceIdentifier: str
    awayFrom: str
    expiryTime: datetime
    startTime: datetime
    status: ZonalShiftStatusType
    comment: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePracticeRunConfigurationRequestTypeDef(TypedDict):
    resourceIdentifier: str
    outcomeAlarms: Sequence[ControlConditionTypeDef]
    blockedWindows: NotRequired[Sequence[str]]
    blockedDates: NotRequired[Sequence[str]]
    blockingAlarms: NotRequired[Sequence[ControlConditionTypeDef]]
    allowedWindows: NotRequired[Sequence[str]]

class PracticeRunConfigurationTypeDef(TypedDict):
    outcomeAlarms: List[ControlConditionTypeDef]
    blockingAlarms: NotRequired[List[ControlConditionTypeDef]]
    blockedWindows: NotRequired[List[str]]
    allowedWindows: NotRequired[List[str]]
    blockedDates: NotRequired[List[str]]

class UpdatePracticeRunConfigurationRequestTypeDef(TypedDict):
    resourceIdentifier: str
    blockedWindows: NotRequired[Sequence[str]]
    blockedDates: NotRequired[Sequence[str]]
    blockingAlarms: NotRequired[Sequence[ControlConditionTypeDef]]
    allowedWindows: NotRequired[Sequence[str]]
    outcomeAlarms: NotRequired[Sequence[ControlConditionTypeDef]]

class ManagedResourceSummaryTypeDef(TypedDict):
    availabilityZones: List[str]
    arn: NotRequired[str]
    name: NotRequired[str]
    appliedWeights: NotRequired[Dict[str, float]]
    zonalShifts: NotRequired[List[ZonalShiftInResourceTypeDef]]
    autoshifts: NotRequired[List[AutoshiftInResourceTypeDef]]
    zonalAutoshiftStatus: NotRequired[ZonalAutoshiftStatusType]
    practiceRunStatus: NotRequired[ZonalAutoshiftStatusType]

class ListAutoshiftsRequestPaginateTypeDef(TypedDict):
    status: NotRequired[AutoshiftExecutionStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListManagedResourcesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListZonalShiftsRequestPaginateTypeDef(TypedDict):
    status: NotRequired[ZonalShiftStatusType]
    resourceIdentifier: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListZonalShiftsResponseTypeDef(TypedDict):
    items: List[ZonalShiftSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreatePracticeRunConfigurationResponseTypeDef(TypedDict):
    arn: str
    name: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    practiceRunConfiguration: PracticeRunConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetManagedResourceResponseTypeDef(TypedDict):
    arn: str
    name: str
    appliedWeights: Dict[str, float]
    zonalShifts: List[ZonalShiftInResourceTypeDef]
    autoshifts: List[AutoshiftInResourceTypeDef]
    practiceRunConfiguration: PracticeRunConfigurationTypeDef
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePracticeRunConfigurationResponseTypeDef(TypedDict):
    arn: str
    name: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    practiceRunConfiguration: PracticeRunConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListManagedResourcesResponseTypeDef(TypedDict):
    items: List[ManagedResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
