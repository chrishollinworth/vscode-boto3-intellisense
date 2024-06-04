"""
Type annotations for arc-zonal-shift service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/type_defs.html)

Usage::

    ```python
    from mypy_boto3_arc_zonal_shift.type_defs import AutoshiftInResourceTypeDef

    data: AutoshiftInResourceTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AppliedStatusType,
    AutoshiftAppliedStatusType,
    AutoshiftExecutionStatusType,
    PracticeRunOutcomeType,
    ZonalAutoshiftStatusType,
    ZonalShiftStatusType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AutoshiftInResourceTypeDef",
    "AutoshiftSummaryTypeDef",
    "CancelZonalShiftRequestRequestTypeDef",
    "ControlConditionTypeDef",
    "CreatePracticeRunConfigurationRequestRequestTypeDef",
    "CreatePracticeRunConfigurationResponseTypeDef",
    "DeletePracticeRunConfigurationRequestRequestTypeDef",
    "DeletePracticeRunConfigurationResponseTypeDef",
    "GetManagedResourceRequestRequestTypeDef",
    "GetManagedResourceResponseTypeDef",
    "ListAutoshiftsRequestRequestTypeDef",
    "ListAutoshiftsResponseTypeDef",
    "ListManagedResourcesRequestRequestTypeDef",
    "ListManagedResourcesResponseTypeDef",
    "ListZonalShiftsRequestRequestTypeDef",
    "ListZonalShiftsResponseTypeDef",
    "ManagedResourceSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "PracticeRunConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "StartZonalShiftRequestRequestTypeDef",
    "UpdatePracticeRunConfigurationRequestRequestTypeDef",
    "UpdatePracticeRunConfigurationResponseTypeDef",
    "UpdateZonalAutoshiftConfigurationRequestRequestTypeDef",
    "UpdateZonalAutoshiftConfigurationResponseTypeDef",
    "UpdateZonalShiftRequestRequestTypeDef",
    "ZonalShiftInResourceTypeDef",
    "ZonalShiftSummaryTypeDef",
    "ZonalShiftTypeDef",
)

AutoshiftInResourceTypeDef = TypedDict(
    "AutoshiftInResourceTypeDef",
    {
        "appliedStatus": AutoshiftAppliedStatusType,
        "awayFrom": str,
        "startTime": datetime,
    },
)

AutoshiftSummaryTypeDef = TypedDict(
    "AutoshiftSummaryTypeDef",
    {
        "awayFrom": str,
        "endTime": datetime,
        "startTime": datetime,
        "status": AutoshiftExecutionStatusType,
    },
)

CancelZonalShiftRequestRequestTypeDef = TypedDict(
    "CancelZonalShiftRequestRequestTypeDef",
    {
        "zonalShiftId": str,
    },
)

ControlConditionTypeDef = TypedDict(
    "ControlConditionTypeDef",
    {
        "alarmIdentifier": str,
        "type": Literal["CLOUDWATCH"],
    },
)

_RequiredCreatePracticeRunConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePracticeRunConfigurationRequestRequestTypeDef",
    {
        "outcomeAlarms": List["ControlConditionTypeDef"],
        "resourceIdentifier": str,
    },
)
_OptionalCreatePracticeRunConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePracticeRunConfigurationRequestRequestTypeDef",
    {
        "blockedDates": List[str],
        "blockedWindows": List[str],
        "blockingAlarms": List["ControlConditionTypeDef"],
    },
    total=False,
)

class CreatePracticeRunConfigurationRequestRequestTypeDef(
    _RequiredCreatePracticeRunConfigurationRequestRequestTypeDef,
    _OptionalCreatePracticeRunConfigurationRequestRequestTypeDef,
):
    pass

CreatePracticeRunConfigurationResponseTypeDef = TypedDict(
    "CreatePracticeRunConfigurationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "practiceRunConfiguration": "PracticeRunConfigurationTypeDef",
        "zonalAutoshiftStatus": ZonalAutoshiftStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePracticeRunConfigurationRequestRequestTypeDef = TypedDict(
    "DeletePracticeRunConfigurationRequestRequestTypeDef",
    {
        "resourceIdentifier": str,
    },
)

DeletePracticeRunConfigurationResponseTypeDef = TypedDict(
    "DeletePracticeRunConfigurationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "zonalAutoshiftStatus": ZonalAutoshiftStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetManagedResourceRequestRequestTypeDef = TypedDict(
    "GetManagedResourceRequestRequestTypeDef",
    {
        "resourceIdentifier": str,
    },
)

GetManagedResourceResponseTypeDef = TypedDict(
    "GetManagedResourceResponseTypeDef",
    {
        "appliedWeights": Dict[str, float],
        "arn": str,
        "autoshifts": List["AutoshiftInResourceTypeDef"],
        "name": str,
        "practiceRunConfiguration": "PracticeRunConfigurationTypeDef",
        "zonalAutoshiftStatus": ZonalAutoshiftStatusType,
        "zonalShifts": List["ZonalShiftInResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAutoshiftsRequestRequestTypeDef = TypedDict(
    "ListAutoshiftsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "status": AutoshiftExecutionStatusType,
    },
    total=False,
)

ListAutoshiftsResponseTypeDef = TypedDict(
    "ListAutoshiftsResponseTypeDef",
    {
        "items": List["AutoshiftSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListManagedResourcesRequestRequestTypeDef = TypedDict(
    "ListManagedResourcesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListManagedResourcesResponseTypeDef = TypedDict(
    "ListManagedResourcesResponseTypeDef",
    {
        "items": List["ManagedResourceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListZonalShiftsRequestRequestTypeDef = TypedDict(
    "ListZonalShiftsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "resourceIdentifier": str,
        "status": ZonalShiftStatusType,
    },
    total=False,
)

ListZonalShiftsResponseTypeDef = TypedDict(
    "ListZonalShiftsResponseTypeDef",
    {
        "items": List["ZonalShiftSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredManagedResourceSummaryTypeDef = TypedDict(
    "_RequiredManagedResourceSummaryTypeDef",
    {
        "availabilityZones": List[str],
    },
)
_OptionalManagedResourceSummaryTypeDef = TypedDict(
    "_OptionalManagedResourceSummaryTypeDef",
    {
        "appliedWeights": Dict[str, float],
        "arn": str,
        "autoshifts": List["AutoshiftInResourceTypeDef"],
        "name": str,
        "practiceRunStatus": ZonalAutoshiftStatusType,
        "zonalAutoshiftStatus": ZonalAutoshiftStatusType,
        "zonalShifts": List["ZonalShiftInResourceTypeDef"],
    },
    total=False,
)

class ManagedResourceSummaryTypeDef(
    _RequiredManagedResourceSummaryTypeDef, _OptionalManagedResourceSummaryTypeDef
):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredPracticeRunConfigurationTypeDef = TypedDict(
    "_RequiredPracticeRunConfigurationTypeDef",
    {
        "outcomeAlarms": List["ControlConditionTypeDef"],
    },
)
_OptionalPracticeRunConfigurationTypeDef = TypedDict(
    "_OptionalPracticeRunConfigurationTypeDef",
    {
        "blockedDates": List[str],
        "blockedWindows": List[str],
        "blockingAlarms": List["ControlConditionTypeDef"],
    },
    total=False,
)

class PracticeRunConfigurationTypeDef(
    _RequiredPracticeRunConfigurationTypeDef, _OptionalPracticeRunConfigurationTypeDef
):
    pass

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

StartZonalShiftRequestRequestTypeDef = TypedDict(
    "StartZonalShiftRequestRequestTypeDef",
    {
        "awayFrom": str,
        "comment": str,
        "expiresIn": str,
        "resourceIdentifier": str,
    },
)

_RequiredUpdatePracticeRunConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePracticeRunConfigurationRequestRequestTypeDef",
    {
        "resourceIdentifier": str,
    },
)
_OptionalUpdatePracticeRunConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePracticeRunConfigurationRequestRequestTypeDef",
    {
        "blockedDates": List[str],
        "blockedWindows": List[str],
        "blockingAlarms": List["ControlConditionTypeDef"],
        "outcomeAlarms": List["ControlConditionTypeDef"],
    },
    total=False,
)

class UpdatePracticeRunConfigurationRequestRequestTypeDef(
    _RequiredUpdatePracticeRunConfigurationRequestRequestTypeDef,
    _OptionalUpdatePracticeRunConfigurationRequestRequestTypeDef,
):
    pass

UpdatePracticeRunConfigurationResponseTypeDef = TypedDict(
    "UpdatePracticeRunConfigurationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "practiceRunConfiguration": "PracticeRunConfigurationTypeDef",
        "zonalAutoshiftStatus": ZonalAutoshiftStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateZonalAutoshiftConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateZonalAutoshiftConfigurationRequestRequestTypeDef",
    {
        "resourceIdentifier": str,
        "zonalAutoshiftStatus": ZonalAutoshiftStatusType,
    },
)

UpdateZonalAutoshiftConfigurationResponseTypeDef = TypedDict(
    "UpdateZonalAutoshiftConfigurationResponseTypeDef",
    {
        "resourceIdentifier": str,
        "zonalAutoshiftStatus": ZonalAutoshiftStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateZonalShiftRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateZonalShiftRequestRequestTypeDef",
    {
        "zonalShiftId": str,
    },
)
_OptionalUpdateZonalShiftRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateZonalShiftRequestRequestTypeDef",
    {
        "comment": str,
        "expiresIn": str,
    },
    total=False,
)

class UpdateZonalShiftRequestRequestTypeDef(
    _RequiredUpdateZonalShiftRequestRequestTypeDef, _OptionalUpdateZonalShiftRequestRequestTypeDef
):
    pass

_RequiredZonalShiftInResourceTypeDef = TypedDict(
    "_RequiredZonalShiftInResourceTypeDef",
    {
        "appliedStatus": AppliedStatusType,
        "awayFrom": str,
        "comment": str,
        "expiryTime": datetime,
        "resourceIdentifier": str,
        "startTime": datetime,
        "zonalShiftId": str,
    },
)
_OptionalZonalShiftInResourceTypeDef = TypedDict(
    "_OptionalZonalShiftInResourceTypeDef",
    {
        "practiceRunOutcome": PracticeRunOutcomeType,
    },
    total=False,
)

class ZonalShiftInResourceTypeDef(
    _RequiredZonalShiftInResourceTypeDef, _OptionalZonalShiftInResourceTypeDef
):
    pass

_RequiredZonalShiftSummaryTypeDef = TypedDict(
    "_RequiredZonalShiftSummaryTypeDef",
    {
        "awayFrom": str,
        "comment": str,
        "expiryTime": datetime,
        "resourceIdentifier": str,
        "startTime": datetime,
        "status": ZonalShiftStatusType,
        "zonalShiftId": str,
    },
)
_OptionalZonalShiftSummaryTypeDef = TypedDict(
    "_OptionalZonalShiftSummaryTypeDef",
    {
        "practiceRunOutcome": PracticeRunOutcomeType,
    },
    total=False,
)

class ZonalShiftSummaryTypeDef(
    _RequiredZonalShiftSummaryTypeDef, _OptionalZonalShiftSummaryTypeDef
):
    pass

ZonalShiftTypeDef = TypedDict(
    "ZonalShiftTypeDef",
    {
        "awayFrom": str,
        "comment": str,
        "expiryTime": datetime,
        "resourceIdentifier": str,
        "startTime": datetime,
        "status": ZonalShiftStatusType,
        "zonalShiftId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
