"""
Type annotations for iotevents-data service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_iotevents_data.type_defs import AcknowledgeActionConfigurationTypeDef

    data: AcknowledgeActionConfigurationTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    AlarmStateNameType,
    ComparisonOperatorType,
    CustomerActionNameType,
    ErrorCodeType,
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
    "AcknowledgeActionConfigurationTypeDef",
    "AcknowledgeAlarmActionRequestTypeDef",
    "AlarmStateTypeDef",
    "AlarmSummaryTypeDef",
    "AlarmTypeDef",
    "BatchAcknowledgeAlarmRequestTypeDef",
    "BatchAcknowledgeAlarmResponseTypeDef",
    "BatchAlarmActionErrorEntryTypeDef",
    "BatchDeleteDetectorErrorEntryTypeDef",
    "BatchDeleteDetectorRequestTypeDef",
    "BatchDeleteDetectorResponseTypeDef",
    "BatchDisableAlarmRequestTypeDef",
    "BatchDisableAlarmResponseTypeDef",
    "BatchEnableAlarmRequestTypeDef",
    "BatchEnableAlarmResponseTypeDef",
    "BatchPutMessageErrorEntryTypeDef",
    "BatchPutMessageRequestTypeDef",
    "BatchPutMessageResponseTypeDef",
    "BatchResetAlarmRequestTypeDef",
    "BatchResetAlarmResponseTypeDef",
    "BatchSnoozeAlarmRequestTypeDef",
    "BatchSnoozeAlarmResponseTypeDef",
    "BatchUpdateDetectorErrorEntryTypeDef",
    "BatchUpdateDetectorRequestTypeDef",
    "BatchUpdateDetectorResponseTypeDef",
    "BlobTypeDef",
    "CustomerActionTypeDef",
    "DeleteDetectorRequestTypeDef",
    "DescribeAlarmRequestTypeDef",
    "DescribeAlarmResponseTypeDef",
    "DescribeDetectorRequestTypeDef",
    "DescribeDetectorResponseTypeDef",
    "DetectorStateDefinitionTypeDef",
    "DetectorStateSummaryTypeDef",
    "DetectorStateTypeDef",
    "DetectorSummaryTypeDef",
    "DetectorTypeDef",
    "DisableActionConfigurationTypeDef",
    "DisableAlarmActionRequestTypeDef",
    "EnableActionConfigurationTypeDef",
    "EnableAlarmActionRequestTypeDef",
    "ListAlarmsRequestTypeDef",
    "ListAlarmsResponseTypeDef",
    "ListDetectorsRequestTypeDef",
    "ListDetectorsResponseTypeDef",
    "MessageTypeDef",
    "ResetActionConfigurationTypeDef",
    "ResetAlarmActionRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RuleEvaluationTypeDef",
    "SimpleRuleEvaluationTypeDef",
    "SnoozeActionConfigurationTypeDef",
    "SnoozeAlarmActionRequestTypeDef",
    "StateChangeConfigurationTypeDef",
    "SystemEventTypeDef",
    "TimerDefinitionTypeDef",
    "TimerTypeDef",
    "TimestampValueTypeDef",
    "UpdateDetectorRequestTypeDef",
    "VariableDefinitionTypeDef",
    "VariableTypeDef",
)

class AcknowledgeActionConfigurationTypeDef(TypedDict):
    note: NotRequired[str]

class AcknowledgeAlarmActionRequestTypeDef(TypedDict):
    requestId: str
    alarmModelName: str
    keyValue: NotRequired[str]
    note: NotRequired[str]

class AlarmSummaryTypeDef(TypedDict):
    alarmModelName: NotRequired[str]
    alarmModelVersion: NotRequired[str]
    keyValue: NotRequired[str]
    stateName: NotRequired[AlarmStateNameType]
    creationTime: NotRequired[datetime]
    lastUpdateTime: NotRequired[datetime]

class BatchAlarmActionErrorEntryTypeDef(TypedDict):
    requestId: NotRequired[str]
    errorCode: NotRequired[ErrorCodeType]
    errorMessage: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BatchDeleteDetectorErrorEntryTypeDef(TypedDict):
    messageId: NotRequired[str]
    errorCode: NotRequired[ErrorCodeType]
    errorMessage: NotRequired[str]

class DeleteDetectorRequestTypeDef(TypedDict):
    messageId: str
    detectorModelName: str
    keyValue: NotRequired[str]

class DisableAlarmActionRequestTypeDef(TypedDict):
    requestId: str
    alarmModelName: str
    keyValue: NotRequired[str]
    note: NotRequired[str]

class EnableAlarmActionRequestTypeDef(TypedDict):
    requestId: str
    alarmModelName: str
    keyValue: NotRequired[str]
    note: NotRequired[str]

class BatchPutMessageErrorEntryTypeDef(TypedDict):
    messageId: NotRequired[str]
    errorCode: NotRequired[ErrorCodeType]
    errorMessage: NotRequired[str]

class ResetAlarmActionRequestTypeDef(TypedDict):
    requestId: str
    alarmModelName: str
    keyValue: NotRequired[str]
    note: NotRequired[str]

class SnoozeAlarmActionRequestTypeDef(TypedDict):
    requestId: str
    alarmModelName: str
    snoozeDuration: int
    keyValue: NotRequired[str]
    note: NotRequired[str]

class BatchUpdateDetectorErrorEntryTypeDef(TypedDict):
    messageId: NotRequired[str]
    errorCode: NotRequired[ErrorCodeType]
    errorMessage: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class DisableActionConfigurationTypeDef(TypedDict):
    note: NotRequired[str]

class EnableActionConfigurationTypeDef(TypedDict):
    note: NotRequired[str]

class ResetActionConfigurationTypeDef(TypedDict):
    note: NotRequired[str]

class SnoozeActionConfigurationTypeDef(TypedDict):
    snoozeDuration: NotRequired[int]
    note: NotRequired[str]

class DescribeAlarmRequestTypeDef(TypedDict):
    alarmModelName: str
    keyValue: NotRequired[str]

class DescribeDetectorRequestTypeDef(TypedDict):
    detectorModelName: str
    keyValue: NotRequired[str]

class TimerDefinitionTypeDef(TypedDict):
    name: str
    seconds: int

class VariableDefinitionTypeDef(TypedDict):
    name: str
    value: str

class DetectorStateSummaryTypeDef(TypedDict):
    stateName: NotRequired[str]

class TimerTypeDef(TypedDict):
    name: str
    timestamp: datetime

class VariableTypeDef(TypedDict):
    name: str
    value: str

class ListAlarmsRequestTypeDef(TypedDict):
    alarmModelName: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListDetectorsRequestTypeDef(TypedDict):
    detectorModelName: str
    stateName: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class TimestampValueTypeDef(TypedDict):
    timeInMillis: NotRequired[int]

SimpleRuleEvaluationTypeDef = TypedDict(
    "SimpleRuleEvaluationTypeDef",
    {
        "inputPropertyValue": NotRequired[str],
        "operator": NotRequired[ComparisonOperatorType],
        "thresholdValue": NotRequired[str],
    },
)

class StateChangeConfigurationTypeDef(TypedDict):
    triggerType: NotRequired[Literal["SNOOZE_TIMEOUT"]]

class BatchAcknowledgeAlarmRequestTypeDef(TypedDict):
    acknowledgeActionRequests: Sequence[AcknowledgeAlarmActionRequestTypeDef]

class BatchAcknowledgeAlarmResponseTypeDef(TypedDict):
    errorEntries: List[BatchAlarmActionErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisableAlarmResponseTypeDef(TypedDict):
    errorEntries: List[BatchAlarmActionErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchEnableAlarmResponseTypeDef(TypedDict):
    errorEntries: List[BatchAlarmActionErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchResetAlarmResponseTypeDef(TypedDict):
    errorEntries: List[BatchAlarmActionErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchSnoozeAlarmResponseTypeDef(TypedDict):
    errorEntries: List[BatchAlarmActionErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAlarmsResponseTypeDef(TypedDict):
    alarmSummaries: List[AlarmSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class BatchDeleteDetectorResponseTypeDef(TypedDict):
    batchDeleteDetectorErrorEntries: List[BatchDeleteDetectorErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteDetectorRequestTypeDef(TypedDict):
    detectors: Sequence[DeleteDetectorRequestTypeDef]

class BatchDisableAlarmRequestTypeDef(TypedDict):
    disableActionRequests: Sequence[DisableAlarmActionRequestTypeDef]

class BatchEnableAlarmRequestTypeDef(TypedDict):
    enableActionRequests: Sequence[EnableAlarmActionRequestTypeDef]

class BatchPutMessageResponseTypeDef(TypedDict):
    BatchPutMessageErrorEntries: List[BatchPutMessageErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchResetAlarmRequestTypeDef(TypedDict):
    resetActionRequests: Sequence[ResetAlarmActionRequestTypeDef]

class BatchSnoozeAlarmRequestTypeDef(TypedDict):
    snoozeActionRequests: Sequence[SnoozeAlarmActionRequestTypeDef]

class BatchUpdateDetectorResponseTypeDef(TypedDict):
    batchUpdateDetectorErrorEntries: List[BatchUpdateDetectorErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CustomerActionTypeDef(TypedDict):
    actionName: NotRequired[CustomerActionNameType]
    snoozeActionConfiguration: NotRequired[SnoozeActionConfigurationTypeDef]
    enableActionConfiguration: NotRequired[EnableActionConfigurationTypeDef]
    disableActionConfiguration: NotRequired[DisableActionConfigurationTypeDef]
    acknowledgeActionConfiguration: NotRequired[AcknowledgeActionConfigurationTypeDef]
    resetActionConfiguration: NotRequired[ResetActionConfigurationTypeDef]

class DetectorStateDefinitionTypeDef(TypedDict):
    stateName: str
    variables: Sequence[VariableDefinitionTypeDef]
    timers: Sequence[TimerDefinitionTypeDef]

class DetectorSummaryTypeDef(TypedDict):
    detectorModelName: NotRequired[str]
    keyValue: NotRequired[str]
    detectorModelVersion: NotRequired[str]
    state: NotRequired[DetectorStateSummaryTypeDef]
    creationTime: NotRequired[datetime]
    lastUpdateTime: NotRequired[datetime]

class DetectorStateTypeDef(TypedDict):
    stateName: str
    variables: List[VariableTypeDef]
    timers: List[TimerTypeDef]

class MessageTypeDef(TypedDict):
    messageId: str
    inputName: str
    payload: BlobTypeDef
    timestamp: NotRequired[TimestampValueTypeDef]

class RuleEvaluationTypeDef(TypedDict):
    simpleRuleEvaluation: NotRequired[SimpleRuleEvaluationTypeDef]

class SystemEventTypeDef(TypedDict):
    eventType: NotRequired[Literal["STATE_CHANGE"]]
    stateChangeConfiguration: NotRequired[StateChangeConfigurationTypeDef]

class UpdateDetectorRequestTypeDef(TypedDict):
    messageId: str
    detectorModelName: str
    state: DetectorStateDefinitionTypeDef
    keyValue: NotRequired[str]

class ListDetectorsResponseTypeDef(TypedDict):
    detectorSummaries: List[DetectorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DetectorTypeDef(TypedDict):
    detectorModelName: NotRequired[str]
    keyValue: NotRequired[str]
    detectorModelVersion: NotRequired[str]
    state: NotRequired[DetectorStateTypeDef]
    creationTime: NotRequired[datetime]
    lastUpdateTime: NotRequired[datetime]

class BatchPutMessageRequestTypeDef(TypedDict):
    messages: Sequence[MessageTypeDef]

class AlarmStateTypeDef(TypedDict):
    stateName: NotRequired[AlarmStateNameType]
    ruleEvaluation: NotRequired[RuleEvaluationTypeDef]
    customerAction: NotRequired[CustomerActionTypeDef]
    systemEvent: NotRequired[SystemEventTypeDef]

class BatchUpdateDetectorRequestTypeDef(TypedDict):
    detectors: Sequence[UpdateDetectorRequestTypeDef]

class DescribeDetectorResponseTypeDef(TypedDict):
    detector: DetectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AlarmTypeDef(TypedDict):
    alarmModelName: NotRequired[str]
    alarmModelVersion: NotRequired[str]
    keyValue: NotRequired[str]
    alarmState: NotRequired[AlarmStateTypeDef]
    severity: NotRequired[int]
    creationTime: NotRequired[datetime]
    lastUpdateTime: NotRequired[datetime]

class DescribeAlarmResponseTypeDef(TypedDict):
    alarm: AlarmTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
