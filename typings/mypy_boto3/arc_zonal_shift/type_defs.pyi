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

class CancelZonalShiftRequestTypeDef(TypedDict):
    zonalShiftId: str

ControlConditionTypeDef = TypedDict(
    "ControlConditionTypeDef",
    {
        "alarmIdentifier": str,
        "type": Literal["CLOUDWATCH"],
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeletePracticeRunConfigurationRequestTypeDef(TypedDict):
    resourceIdentifier: str

class GetManagedResourceRequestTypeDef(TypedDict):
    resourceIdentifier: str

class ZonalShiftInResourceTypeDef(TypedDict):
    appliedStatus: AppliedStatusType
    awayFrom: str
    comment: str
    expiryTime: datetime
    resourceIdentifier: str
    startTime: datetime
    zonalShiftId: str
    practiceRunOutcome: NotRequired[PracticeRunOutcomeType]
    shiftType: NotRequired[ShiftTypeType]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAutoshiftsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    status: NotRequired[AutoshiftExecutionStatusType]

class ListManagedResourcesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListZonalShiftsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    resourceIdentifier: NotRequired[str]
    status: NotRequired[ZonalShiftStatusType]

class ZonalShiftSummaryTypeDef(TypedDict):
    awayFrom: str
    comment: str
    expiryTime: datetime
    resourceIdentifier: str
    startTime: datetime
    status: ZonalShiftStatusType
    zonalShiftId: str
    practiceRunOutcome: NotRequired[PracticeRunOutcomeType]
    shiftType: NotRequired[ShiftTypeType]

class StartZonalShiftRequestTypeDef(TypedDict):
    awayFrom: str
    comment: str
    expiresIn: str
    resourceIdentifier: str

class UpdateAutoshiftObserverNotificationStatusRequestTypeDef(TypedDict):
    status: AutoshiftObserverNotificationStatusType

class UpdateZonalAutoshiftConfigurationRequestTypeDef(TypedDict):
    resourceIdentifier: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType

class UpdateZonalShiftRequestTypeDef(TypedDict):
    zonalShiftId: str
    comment: NotRequired[str]
    expiresIn: NotRequired[str]

class CreatePracticeRunConfigurationRequestTypeDef(TypedDict):
    outcomeAlarms: Sequence[ControlConditionTypeDef]
    resourceIdentifier: str
    blockedDates: NotRequired[Sequence[str]]
    blockedWindows: NotRequired[Sequence[str]]
    blockingAlarms: NotRequired[Sequence[ControlConditionTypeDef]]

class PracticeRunConfigurationTypeDef(TypedDict):
    outcomeAlarms: List[ControlConditionTypeDef]
    blockedDates: NotRequired[List[str]]
    blockedWindows: NotRequired[List[str]]
    blockingAlarms: NotRequired[List[ControlConditionTypeDef]]

class UpdatePracticeRunConfigurationRequestTypeDef(TypedDict):
    resourceIdentifier: str
    blockedDates: NotRequired[Sequence[str]]
    blockedWindows: NotRequired[Sequence[str]]
    blockingAlarms: NotRequired[Sequence[ControlConditionTypeDef]]
    outcomeAlarms: NotRequired[Sequence[ControlConditionTypeDef]]

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

class UpdateAutoshiftObserverNotificationStatusResponseTypeDef(TypedDict):
    status: AutoshiftObserverNotificationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateZonalAutoshiftConfigurationResponseTypeDef(TypedDict):
    resourceIdentifier: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ZonalShiftTypeDef(TypedDict):
    awayFrom: str
    comment: str
    expiryTime: datetime
    resourceIdentifier: str
    startTime: datetime
    status: ZonalShiftStatusType
    zonalShiftId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ManagedResourceSummaryTypeDef(TypedDict):
    availabilityZones: List[str]
    appliedWeights: NotRequired[Dict[str, float]]
    arn: NotRequired[str]
    autoshifts: NotRequired[List[AutoshiftInResourceTypeDef]]
    name: NotRequired[str]
    practiceRunStatus: NotRequired[ZonalAutoshiftStatusType]
    zonalAutoshiftStatus: NotRequired[ZonalAutoshiftStatusType]
    zonalShifts: NotRequired[List[ZonalShiftInResourceTypeDef]]

class ListAutoshiftsRequestPaginateTypeDef(TypedDict):
    status: NotRequired[AutoshiftExecutionStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListManagedResourcesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListZonalShiftsRequestPaginateTypeDef(TypedDict):
    resourceIdentifier: NotRequired[str]
    status: NotRequired[ZonalShiftStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListZonalShiftsResponseTypeDef(TypedDict):
    items: List[ZonalShiftSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreatePracticeRunConfigurationResponseTypeDef(TypedDict):
    arn: str
    name: str
    practiceRunConfiguration: PracticeRunConfigurationTypeDef
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetManagedResourceResponseTypeDef(TypedDict):
    appliedWeights: Dict[str, float]
    arn: str
    autoshifts: List[AutoshiftInResourceTypeDef]
    name: str
    practiceRunConfiguration: PracticeRunConfigurationTypeDef
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    zonalShifts: List[ZonalShiftInResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePracticeRunConfigurationResponseTypeDef(TypedDict):
    arn: str
    name: str
    practiceRunConfiguration: PracticeRunConfigurationTypeDef
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListManagedResourcesResponseTypeDef(TypedDict):
    items: List[ManagedResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
