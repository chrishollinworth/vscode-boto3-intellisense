"""
Main interface for iotevents-data service type definitions.

Usage::

    ```python
    from mypy_boto3_iotevents_data.type_defs import BatchPutMessageErrorEntryTypeDef

    data: BatchPutMessageErrorEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchPutMessageErrorEntryTypeDef",
    "BatchUpdateDetectorErrorEntryTypeDef",
    "DetectorStateDefinitionTypeDef",
    "DetectorStateSummaryTypeDef",
    "DetectorStateTypeDef",
    "DetectorSummaryTypeDef",
    "DetectorTypeDef",
    "TimerDefinitionTypeDef",
    "TimerTypeDef",
    "VariableDefinitionTypeDef",
    "VariableTypeDef",
    "BatchPutMessageResponseTypeDef",
    "BatchUpdateDetectorResponseTypeDef",
    "DescribeDetectorResponseTypeDef",
    "ListDetectorsResponseTypeDef",
    "MessageTypeDef",
    "UpdateDetectorRequestTypeDef",
)

BatchPutMessageErrorEntryTypeDef = TypedDict(
    "BatchPutMessageErrorEntryTypeDef",
    {
        "messageId": str,
        "errorCode": Literal[
            "ResourceNotFoundException",
            "InvalidRequestException",
            "InternalFailureException",
            "ServiceUnavailableException",
            "ThrottlingException",
        ],
        "errorMessage": str,
    },
    total=False,
)

BatchUpdateDetectorErrorEntryTypeDef = TypedDict(
    "BatchUpdateDetectorErrorEntryTypeDef",
    {
        "messageId": str,
        "errorCode": Literal[
            "ResourceNotFoundException",
            "InvalidRequestException",
            "InternalFailureException",
            "ServiceUnavailableException",
            "ThrottlingException",
        ],
        "errorMessage": str,
    },
    total=False,
)

DetectorStateDefinitionTypeDef = TypedDict(
    "DetectorStateDefinitionTypeDef",
    {
        "stateName": str,
        "variables": List["VariableDefinitionTypeDef"],
        "timers": List["TimerDefinitionTypeDef"],
    },
)

DetectorStateSummaryTypeDef = TypedDict(
    "DetectorStateSummaryTypeDef", {"stateName": str}, total=False
)

DetectorStateTypeDef = TypedDict(
    "DetectorStateTypeDef",
    {"stateName": str, "variables": List["VariableTypeDef"], "timers": List["TimerTypeDef"]},
)

DetectorSummaryTypeDef = TypedDict(
    "DetectorSummaryTypeDef",
    {
        "detectorModelName": str,
        "keyValue": str,
        "detectorModelVersion": str,
        "state": "DetectorStateSummaryTypeDef",
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

DetectorTypeDef = TypedDict(
    "DetectorTypeDef",
    {
        "detectorModelName": str,
        "keyValue": str,
        "detectorModelVersion": str,
        "state": "DetectorStateTypeDef",
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

TimerDefinitionTypeDef = TypedDict("TimerDefinitionTypeDef", {"name": str, "seconds": int})

TimerTypeDef = TypedDict("TimerTypeDef", {"name": str, "timestamp": datetime})

VariableDefinitionTypeDef = TypedDict("VariableDefinitionTypeDef", {"name": str, "value": str})

VariableTypeDef = TypedDict("VariableTypeDef", {"name": str, "value": str})

BatchPutMessageResponseTypeDef = TypedDict(
    "BatchPutMessageResponseTypeDef",
    {"BatchPutMessageErrorEntries": List["BatchPutMessageErrorEntryTypeDef"]},
    total=False,
)

BatchUpdateDetectorResponseTypeDef = TypedDict(
    "BatchUpdateDetectorResponseTypeDef",
    {"batchUpdateDetectorErrorEntries": List["BatchUpdateDetectorErrorEntryTypeDef"]},
    total=False,
)

DescribeDetectorResponseTypeDef = TypedDict(
    "DescribeDetectorResponseTypeDef", {"detector": "DetectorTypeDef"}, total=False
)

ListDetectorsResponseTypeDef = TypedDict(
    "ListDetectorsResponseTypeDef",
    {"detectorSummaries": List["DetectorSummaryTypeDef"], "nextToken": str},
    total=False,
)

MessageTypeDef = TypedDict(
    "MessageTypeDef", {"messageId": str, "inputName": str, "payload": Union[bytes, IO[bytes]]}
)

_RequiredUpdateDetectorRequestTypeDef = TypedDict(
    "_RequiredUpdateDetectorRequestTypeDef",
    {"messageId": str, "detectorModelName": str, "state": "DetectorStateDefinitionTypeDef"},
)
_OptionalUpdateDetectorRequestTypeDef = TypedDict(
    "_OptionalUpdateDetectorRequestTypeDef", {"keyValue": str}, total=False
)


class UpdateDetectorRequestTypeDef(
    _RequiredUpdateDetectorRequestTypeDef, _OptionalUpdateDetectorRequestTypeDef
):
    pass
