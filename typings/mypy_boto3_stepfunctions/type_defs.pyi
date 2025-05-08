"""
Type annotations for stepfunctions service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_stepfunctions.type_defs import ActivityFailedEventDetailsTypeDef

    data: ActivityFailedEventDetailsTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    EncryptionTypeType,
    ExecutionRedriveFilterType,
    ExecutionRedriveStatusType,
    ExecutionStatusType,
    HistoryEventTypeType,
    IncludedDataType,
    InspectionLevelType,
    LogLevelType,
    MapRunStatusType,
    StateMachineStatusType,
    StateMachineTypeType,
    SyncExecutionStatusType,
    TestExecutionStatusType,
    ValidateStateMachineDefinitionResultCodeType,
    ValidateStateMachineDefinitionSeverityType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ActivityFailedEventDetailsTypeDef",
    "ActivityListItemTypeDef",
    "ActivityScheduleFailedEventDetailsTypeDef",
    "ActivityScheduledEventDetailsTypeDef",
    "ActivityStartedEventDetailsTypeDef",
    "ActivitySucceededEventDetailsTypeDef",
    "ActivityTimedOutEventDetailsTypeDef",
    "AssignedVariablesDetailsTypeDef",
    "BillingDetailsTypeDef",
    "CloudWatchEventsExecutionDataDetailsTypeDef",
    "CloudWatchLogsLogGroupTypeDef",
    "CreateActivityInputTypeDef",
    "CreateActivityOutputTypeDef",
    "CreateStateMachineAliasInputTypeDef",
    "CreateStateMachineAliasOutputTypeDef",
    "CreateStateMachineInputTypeDef",
    "CreateStateMachineOutputTypeDef",
    "DeleteActivityInputTypeDef",
    "DeleteStateMachineAliasInputTypeDef",
    "DeleteStateMachineInputTypeDef",
    "DeleteStateMachineVersionInputTypeDef",
    "DescribeActivityInputTypeDef",
    "DescribeActivityOutputTypeDef",
    "DescribeExecutionInputTypeDef",
    "DescribeExecutionOutputTypeDef",
    "DescribeMapRunInputTypeDef",
    "DescribeMapRunOutputTypeDef",
    "DescribeStateMachineAliasInputTypeDef",
    "DescribeStateMachineAliasOutputTypeDef",
    "DescribeStateMachineForExecutionInputTypeDef",
    "DescribeStateMachineForExecutionOutputTypeDef",
    "DescribeStateMachineInputTypeDef",
    "DescribeStateMachineOutputTypeDef",
    "EncryptionConfigurationTypeDef",
    "EvaluationFailedEventDetailsTypeDef",
    "ExecutionAbortedEventDetailsTypeDef",
    "ExecutionFailedEventDetailsTypeDef",
    "ExecutionListItemTypeDef",
    "ExecutionRedrivenEventDetailsTypeDef",
    "ExecutionStartedEventDetailsTypeDef",
    "ExecutionSucceededEventDetailsTypeDef",
    "ExecutionTimedOutEventDetailsTypeDef",
    "GetActivityTaskInputTypeDef",
    "GetActivityTaskOutputTypeDef",
    "GetExecutionHistoryInputPaginateTypeDef",
    "GetExecutionHistoryInputTypeDef",
    "GetExecutionHistoryOutputTypeDef",
    "HistoryEventExecutionDataDetailsTypeDef",
    "HistoryEventTypeDef",
    "InspectionDataRequestTypeDef",
    "InspectionDataResponseTypeDef",
    "InspectionDataTypeDef",
    "LambdaFunctionFailedEventDetailsTypeDef",
    "LambdaFunctionScheduleFailedEventDetailsTypeDef",
    "LambdaFunctionScheduledEventDetailsTypeDef",
    "LambdaFunctionStartFailedEventDetailsTypeDef",
    "LambdaFunctionSucceededEventDetailsTypeDef",
    "LambdaFunctionTimedOutEventDetailsTypeDef",
    "ListActivitiesInputPaginateTypeDef",
    "ListActivitiesInputTypeDef",
    "ListActivitiesOutputTypeDef",
    "ListExecutionsInputPaginateTypeDef",
    "ListExecutionsInputTypeDef",
    "ListExecutionsOutputTypeDef",
    "ListMapRunsInputPaginateTypeDef",
    "ListMapRunsInputTypeDef",
    "ListMapRunsOutputTypeDef",
    "ListStateMachineAliasesInputTypeDef",
    "ListStateMachineAliasesOutputTypeDef",
    "ListStateMachineVersionsInputTypeDef",
    "ListStateMachineVersionsOutputTypeDef",
    "ListStateMachinesInputPaginateTypeDef",
    "ListStateMachinesInputTypeDef",
    "ListStateMachinesOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LogDestinationTypeDef",
    "LoggingConfigurationOutputTypeDef",
    "LoggingConfigurationTypeDef",
    "LoggingConfigurationUnionTypeDef",
    "MapIterationEventDetailsTypeDef",
    "MapRunExecutionCountsTypeDef",
    "MapRunFailedEventDetailsTypeDef",
    "MapRunItemCountsTypeDef",
    "MapRunListItemTypeDef",
    "MapRunRedrivenEventDetailsTypeDef",
    "MapRunStartedEventDetailsTypeDef",
    "MapStateStartedEventDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "PublishStateMachineVersionInputTypeDef",
    "PublishStateMachineVersionOutputTypeDef",
    "RedriveExecutionInputTypeDef",
    "RedriveExecutionOutputTypeDef",
    "ResponseMetadataTypeDef",
    "RoutingConfigurationListItemTypeDef",
    "SendTaskFailureInputTypeDef",
    "SendTaskHeartbeatInputTypeDef",
    "SendTaskSuccessInputTypeDef",
    "StartExecutionInputTypeDef",
    "StartExecutionOutputTypeDef",
    "StartSyncExecutionInputTypeDef",
    "StartSyncExecutionOutputTypeDef",
    "StateEnteredEventDetailsTypeDef",
    "StateExitedEventDetailsTypeDef",
    "StateMachineAliasListItemTypeDef",
    "StateMachineListItemTypeDef",
    "StateMachineVersionListItemTypeDef",
    "StopExecutionInputTypeDef",
    "StopExecutionOutputTypeDef",
    "TagResourceInputTypeDef",
    "TagTypeDef",
    "TaskCredentialsTypeDef",
    "TaskFailedEventDetailsTypeDef",
    "TaskScheduledEventDetailsTypeDef",
    "TaskStartFailedEventDetailsTypeDef",
    "TaskStartedEventDetailsTypeDef",
    "TaskSubmitFailedEventDetailsTypeDef",
    "TaskSubmittedEventDetailsTypeDef",
    "TaskSucceededEventDetailsTypeDef",
    "TaskTimedOutEventDetailsTypeDef",
    "TestStateInputTypeDef",
    "TestStateOutputTypeDef",
    "TracingConfigurationTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateMapRunInputTypeDef",
    "UpdateStateMachineAliasInputTypeDef",
    "UpdateStateMachineAliasOutputTypeDef",
    "UpdateStateMachineInputTypeDef",
    "UpdateStateMachineOutputTypeDef",
    "ValidateStateMachineDefinitionDiagnosticTypeDef",
    "ValidateStateMachineDefinitionInputTypeDef",
    "ValidateStateMachineDefinitionOutputTypeDef",
)

class ActivityFailedEventDetailsTypeDef(TypedDict):
    error: NotRequired[str]
    cause: NotRequired[str]

class ActivityListItemTypeDef(TypedDict):
    activityArn: str
    name: str
    creationDate: datetime

class ActivityScheduleFailedEventDetailsTypeDef(TypedDict):
    error: NotRequired[str]
    cause: NotRequired[str]

class HistoryEventExecutionDataDetailsTypeDef(TypedDict):
    truncated: NotRequired[bool]

class ActivityStartedEventDetailsTypeDef(TypedDict):
    workerName: NotRequired[str]

class ActivityTimedOutEventDetailsTypeDef(TypedDict):
    error: NotRequired[str]
    cause: NotRequired[str]

class AssignedVariablesDetailsTypeDef(TypedDict):
    truncated: NotRequired[bool]

class BillingDetailsTypeDef(TypedDict):
    billedMemoryUsedInMB: NotRequired[int]
    billedDurationInMilliseconds: NotRequired[int]

class CloudWatchEventsExecutionDataDetailsTypeDef(TypedDict):
    included: NotRequired[bool]

class CloudWatchLogsLogGroupTypeDef(TypedDict):
    logGroupArn: NotRequired[str]

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "type": EncryptionTypeType,
        "kmsKeyId": NotRequired[str],
        "kmsDataKeyReusePeriodSeconds": NotRequired[int],
    },
)

class TagTypeDef(TypedDict):
    key: NotRequired[str]
    value: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class RoutingConfigurationListItemTypeDef(TypedDict):
    stateMachineVersionArn: str
    weight: int

class TracingConfigurationTypeDef(TypedDict):
    enabled: NotRequired[bool]

class DeleteActivityInputTypeDef(TypedDict):
    activityArn: str

class DeleteStateMachineAliasInputTypeDef(TypedDict):
    stateMachineAliasArn: str

class DeleteStateMachineInputTypeDef(TypedDict):
    stateMachineArn: str

class DeleteStateMachineVersionInputTypeDef(TypedDict):
    stateMachineVersionArn: str

class DescribeActivityInputTypeDef(TypedDict):
    activityArn: str

class DescribeExecutionInputTypeDef(TypedDict):
    executionArn: str
    includedData: NotRequired[IncludedDataType]

class DescribeMapRunInputTypeDef(TypedDict):
    mapRunArn: str

class MapRunExecutionCountsTypeDef(TypedDict):
    pending: int
    running: int
    succeeded: int
    failed: int
    timedOut: int
    aborted: int
    total: int
    resultsWritten: int
    failuresNotRedrivable: NotRequired[int]
    pendingRedrive: NotRequired[int]

class MapRunItemCountsTypeDef(TypedDict):
    pending: int
    running: int
    succeeded: int
    failed: int
    timedOut: int
    aborted: int
    total: int
    resultsWritten: int
    failuresNotRedrivable: NotRequired[int]
    pendingRedrive: NotRequired[int]

class DescribeStateMachineAliasInputTypeDef(TypedDict):
    stateMachineAliasArn: str

class DescribeStateMachineForExecutionInputTypeDef(TypedDict):
    executionArn: str
    includedData: NotRequired[IncludedDataType]

class DescribeStateMachineInputTypeDef(TypedDict):
    stateMachineArn: str
    includedData: NotRequired[IncludedDataType]

class EvaluationFailedEventDetailsTypeDef(TypedDict):
    state: str
    error: NotRequired[str]
    cause: NotRequired[str]
    location: NotRequired[str]

class ExecutionAbortedEventDetailsTypeDef(TypedDict):
    error: NotRequired[str]
    cause: NotRequired[str]

class ExecutionFailedEventDetailsTypeDef(TypedDict):
    error: NotRequired[str]
    cause: NotRequired[str]

class ExecutionListItemTypeDef(TypedDict):
    executionArn: str
    stateMachineArn: str
    name: str
    status: ExecutionStatusType
    startDate: datetime
    stopDate: NotRequired[datetime]
    mapRunArn: NotRequired[str]
    itemCount: NotRequired[int]
    stateMachineVersionArn: NotRequired[str]
    stateMachineAliasArn: NotRequired[str]
    redriveCount: NotRequired[int]
    redriveDate: NotRequired[datetime]

class ExecutionRedrivenEventDetailsTypeDef(TypedDict):
    redriveCount: NotRequired[int]

class ExecutionTimedOutEventDetailsTypeDef(TypedDict):
    error: NotRequired[str]
    cause: NotRequired[str]

class GetActivityTaskInputTypeDef(TypedDict):
    activityArn: str
    workerName: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetExecutionHistoryInputTypeDef(TypedDict):
    executionArn: str
    maxResults: NotRequired[int]
    reverseOrder: NotRequired[bool]
    nextToken: NotRequired[str]
    includeExecutionData: NotRequired[bool]

class LambdaFunctionFailedEventDetailsTypeDef(TypedDict):
    error: NotRequired[str]
    cause: NotRequired[str]

class LambdaFunctionScheduleFailedEventDetailsTypeDef(TypedDict):
    error: NotRequired[str]
    cause: NotRequired[str]

class LambdaFunctionStartFailedEventDetailsTypeDef(TypedDict):
    error: NotRequired[str]
    cause: NotRequired[str]

class LambdaFunctionTimedOutEventDetailsTypeDef(TypedDict):
    error: NotRequired[str]
    cause: NotRequired[str]

class MapIterationEventDetailsTypeDef(TypedDict):
    name: NotRequired[str]
    index: NotRequired[int]

class MapRunFailedEventDetailsTypeDef(TypedDict):
    error: NotRequired[str]
    cause: NotRequired[str]

class MapRunRedrivenEventDetailsTypeDef(TypedDict):
    mapRunArn: NotRequired[str]
    redriveCount: NotRequired[int]

class MapRunStartedEventDetailsTypeDef(TypedDict):
    mapRunArn: NotRequired[str]

class MapStateStartedEventDetailsTypeDef(TypedDict):
    length: NotRequired[int]

class TaskFailedEventDetailsTypeDef(TypedDict):
    resourceType: str
    resource: str
    error: NotRequired[str]
    cause: NotRequired[str]

class TaskStartFailedEventDetailsTypeDef(TypedDict):
    resourceType: str
    resource: str
    error: NotRequired[str]
    cause: NotRequired[str]

class TaskStartedEventDetailsTypeDef(TypedDict):
    resourceType: str
    resource: str

class TaskSubmitFailedEventDetailsTypeDef(TypedDict):
    resourceType: str
    resource: str
    error: NotRequired[str]
    cause: NotRequired[str]

class TaskTimedOutEventDetailsTypeDef(TypedDict):
    resourceType: str
    resource: str
    error: NotRequired[str]
    cause: NotRequired[str]

class InspectionDataRequestTypeDef(TypedDict):
    protocol: NotRequired[str]
    method: NotRequired[str]
    url: NotRequired[str]
    headers: NotRequired[str]
    body: NotRequired[str]

class InspectionDataResponseTypeDef(TypedDict):
    protocol: NotRequired[str]
    statusCode: NotRequired[str]
    statusMessage: NotRequired[str]
    headers: NotRequired[str]
    body: NotRequired[str]

class TaskCredentialsTypeDef(TypedDict):
    roleArn: NotRequired[str]

class ListActivitiesInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListExecutionsInputTypeDef(TypedDict):
    stateMachineArn: NotRequired[str]
    statusFilter: NotRequired[ExecutionStatusType]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    mapRunArn: NotRequired[str]
    redriveFilter: NotRequired[ExecutionRedriveFilterType]

class ListMapRunsInputTypeDef(TypedDict):
    executionArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class MapRunListItemTypeDef(TypedDict):
    executionArn: str
    mapRunArn: str
    stateMachineArn: str
    startDate: datetime
    stopDate: NotRequired[datetime]

class ListStateMachineAliasesInputTypeDef(TypedDict):
    stateMachineArn: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class StateMachineAliasListItemTypeDef(TypedDict):
    stateMachineAliasArn: str
    creationDate: datetime

class ListStateMachineVersionsInputTypeDef(TypedDict):
    stateMachineArn: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class StateMachineVersionListItemTypeDef(TypedDict):
    stateMachineVersionArn: str
    creationDate: datetime

class ListStateMachinesInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

StateMachineListItemTypeDef = TypedDict(
    "StateMachineListItemTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "type": StateMachineTypeType,
        "creationDate": datetime,
    },
)

class ListTagsForResourceInputTypeDef(TypedDict):
    resourceArn: str

class PublishStateMachineVersionInputTypeDef(TypedDict):
    stateMachineArn: str
    revisionId: NotRequired[str]
    description: NotRequired[str]

class RedriveExecutionInputTypeDef(TypedDict):
    executionArn: str
    clientToken: NotRequired[str]

class SendTaskFailureInputTypeDef(TypedDict):
    taskToken: str
    error: NotRequired[str]
    cause: NotRequired[str]

class SendTaskHeartbeatInputTypeDef(TypedDict):
    taskToken: str

class SendTaskSuccessInputTypeDef(TypedDict):
    taskToken: str
    output: str

StartExecutionInputTypeDef = TypedDict(
    "StartExecutionInputTypeDef",
    {
        "stateMachineArn": str,
        "name": NotRequired[str],
        "input": NotRequired[str],
        "traceHeader": NotRequired[str],
    },
)
StartSyncExecutionInputTypeDef = TypedDict(
    "StartSyncExecutionInputTypeDef",
    {
        "stateMachineArn": str,
        "name": NotRequired[str],
        "input": NotRequired[str],
        "traceHeader": NotRequired[str],
        "includedData": NotRequired[IncludedDataType],
    },
)

class StopExecutionInputTypeDef(TypedDict):
    executionArn: str
    error: NotRequired[str]
    cause: NotRequired[str]

TestStateInputTypeDef = TypedDict(
    "TestStateInputTypeDef",
    {
        "definition": str,
        "roleArn": NotRequired[str],
        "input": NotRequired[str],
        "inspectionLevel": NotRequired[InspectionLevelType],
        "revealSecrets": NotRequired[bool],
        "variables": NotRequired[str],
    },
)

class UntagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateMapRunInputTypeDef(TypedDict):
    mapRunArn: str
    maxConcurrency: NotRequired[int]
    toleratedFailurePercentage: NotRequired[float]
    toleratedFailureCount: NotRequired[int]

class ValidateStateMachineDefinitionDiagnosticTypeDef(TypedDict):
    severity: ValidateStateMachineDefinitionSeverityType
    code: str
    message: str
    location: NotRequired[str]

ValidateStateMachineDefinitionInputTypeDef = TypedDict(
    "ValidateStateMachineDefinitionInputTypeDef",
    {
        "definition": str,
        "type": NotRequired[StateMachineTypeType],
        "severity": NotRequired[ValidateStateMachineDefinitionSeverityType],
        "maxResults": NotRequired[int],
    },
)
ActivityScheduledEventDetailsTypeDef = TypedDict(
    "ActivityScheduledEventDetailsTypeDef",
    {
        "resource": str,
        "input": NotRequired[str],
        "inputDetails": NotRequired[HistoryEventExecutionDataDetailsTypeDef],
        "timeoutInSeconds": NotRequired[int],
        "heartbeatInSeconds": NotRequired[int],
    },
)

class ActivitySucceededEventDetailsTypeDef(TypedDict):
    output: NotRequired[str]
    outputDetails: NotRequired[HistoryEventExecutionDataDetailsTypeDef]

ExecutionStartedEventDetailsTypeDef = TypedDict(
    "ExecutionStartedEventDetailsTypeDef",
    {
        "input": NotRequired[str],
        "inputDetails": NotRequired[HistoryEventExecutionDataDetailsTypeDef],
        "roleArn": NotRequired[str],
        "stateMachineAliasArn": NotRequired[str],
        "stateMachineVersionArn": NotRequired[str],
    },
)

class ExecutionSucceededEventDetailsTypeDef(TypedDict):
    output: NotRequired[str]
    outputDetails: NotRequired[HistoryEventExecutionDataDetailsTypeDef]

class LambdaFunctionSucceededEventDetailsTypeDef(TypedDict):
    output: NotRequired[str]
    outputDetails: NotRequired[HistoryEventExecutionDataDetailsTypeDef]

StateEnteredEventDetailsTypeDef = TypedDict(
    "StateEnteredEventDetailsTypeDef",
    {
        "name": str,
        "input": NotRequired[str],
        "inputDetails": NotRequired[HistoryEventExecutionDataDetailsTypeDef],
    },
)

class TaskSubmittedEventDetailsTypeDef(TypedDict):
    resourceType: str
    resource: str
    output: NotRequired[str]
    outputDetails: NotRequired[HistoryEventExecutionDataDetailsTypeDef]

class TaskSucceededEventDetailsTypeDef(TypedDict):
    resourceType: str
    resource: str
    output: NotRequired[str]
    outputDetails: NotRequired[HistoryEventExecutionDataDetailsTypeDef]

class StateExitedEventDetailsTypeDef(TypedDict):
    name: str
    output: NotRequired[str]
    outputDetails: NotRequired[HistoryEventExecutionDataDetailsTypeDef]
    assignedVariables: NotRequired[Dict[str, str]]
    assignedVariablesDetails: NotRequired[AssignedVariablesDetailsTypeDef]

class LogDestinationTypeDef(TypedDict):
    cloudWatchLogsLogGroup: NotRequired[CloudWatchLogsLogGroupTypeDef]

class CreateActivityInputTypeDef(TypedDict):
    name: str
    tags: NotRequired[Sequence[TagTypeDef]]
    encryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]

class TagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateActivityOutputTypeDef(TypedDict):
    activityArn: str
    creationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStateMachineAliasOutputTypeDef(TypedDict):
    stateMachineAliasArn: str
    creationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStateMachineOutputTypeDef(TypedDict):
    stateMachineArn: str
    creationDate: datetime
    stateMachineVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeActivityOutputTypeDef(TypedDict):
    activityArn: str
    name: str
    creationDate: datetime
    encryptionConfiguration: EncryptionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

DescribeExecutionOutputTypeDef = TypedDict(
    "DescribeExecutionOutputTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": ExecutionStatusType,
        "startDate": datetime,
        "input": str,
        "inputDetails": CloudWatchEventsExecutionDataDetailsTypeDef,
        "redriveCount": int,
        "redriveStatus": ExecutionRedriveStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "stopDate": NotRequired[datetime],
        "output": NotRequired[str],
        "outputDetails": NotRequired[CloudWatchEventsExecutionDataDetailsTypeDef],
        "traceHeader": NotRequired[str],
        "mapRunArn": NotRequired[str],
        "error": NotRequired[str],
        "cause": NotRequired[str],
        "stateMachineVersionArn": NotRequired[str],
        "stateMachineAliasArn": NotRequired[str],
        "redriveDate": NotRequired[datetime],
        "redriveStatusReason": NotRequired[str],
    },
)
GetActivityTaskOutputTypeDef = TypedDict(
    "GetActivityTaskOutputTypeDef",
    {
        "taskToken": str,
        "input": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListActivitiesOutputTypeDef(TypedDict):
    activities: List[ActivityListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PublishStateMachineVersionOutputTypeDef(TypedDict):
    creationDate: datetime
    stateMachineVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RedriveExecutionOutputTypeDef(TypedDict):
    redriveDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartExecutionOutputTypeDef(TypedDict):
    executionArn: str
    startDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

StartSyncExecutionOutputTypeDef = TypedDict(
    "StartSyncExecutionOutputTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "startDate": datetime,
        "stopDate": datetime,
        "status": SyncExecutionStatusType,
        "error": str,
        "cause": str,
        "input": str,
        "inputDetails": CloudWatchEventsExecutionDataDetailsTypeDef,
        "output": str,
        "outputDetails": CloudWatchEventsExecutionDataDetailsTypeDef,
        "traceHeader": str,
        "billingDetails": BillingDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class StopExecutionOutputTypeDef(TypedDict):
    stopDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStateMachineAliasOutputTypeDef(TypedDict):
    updateDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStateMachineOutputTypeDef(TypedDict):
    updateDate: datetime
    revisionId: str
    stateMachineVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStateMachineAliasInputTypeDef(TypedDict):
    name: str
    routingConfiguration: Sequence[RoutingConfigurationListItemTypeDef]
    description: NotRequired[str]

class DescribeStateMachineAliasOutputTypeDef(TypedDict):
    stateMachineAliasArn: str
    name: str
    description: str
    routingConfiguration: List[RoutingConfigurationListItemTypeDef]
    creationDate: datetime
    updateDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStateMachineAliasInputTypeDef(TypedDict):
    stateMachineAliasArn: str
    description: NotRequired[str]
    routingConfiguration: NotRequired[Sequence[RoutingConfigurationListItemTypeDef]]

class DescribeMapRunOutputTypeDef(TypedDict):
    mapRunArn: str
    executionArn: str
    status: MapRunStatusType
    startDate: datetime
    stopDate: datetime
    maxConcurrency: int
    toleratedFailurePercentage: float
    toleratedFailureCount: int
    itemCounts: MapRunItemCountsTypeDef
    executionCounts: MapRunExecutionCountsTypeDef
    redriveCount: int
    redriveDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListExecutionsOutputTypeDef(TypedDict):
    executions: List[ExecutionListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetExecutionHistoryInputPaginateTypeDef(TypedDict):
    executionArn: str
    reverseOrder: NotRequired[bool]
    includeExecutionData: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListActivitiesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListExecutionsInputPaginateTypeDef(TypedDict):
    stateMachineArn: NotRequired[str]
    statusFilter: NotRequired[ExecutionStatusType]
    mapRunArn: NotRequired[str]
    redriveFilter: NotRequired[ExecutionRedriveFilterType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMapRunsInputPaginateTypeDef(TypedDict):
    executionArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStateMachinesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

InspectionDataTypeDef = TypedDict(
    "InspectionDataTypeDef",
    {
        "input": NotRequired[str],
        "afterArguments": NotRequired[str],
        "afterInputPath": NotRequired[str],
        "afterParameters": NotRequired[str],
        "result": NotRequired[str],
        "afterResultSelector": NotRequired[str],
        "afterResultPath": NotRequired[str],
        "request": NotRequired[InspectionDataRequestTypeDef],
        "response": NotRequired[InspectionDataResponseTypeDef],
        "variables": NotRequired[str],
    },
)
LambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "LambdaFunctionScheduledEventDetailsTypeDef",
    {
        "resource": str,
        "input": NotRequired[str],
        "inputDetails": NotRequired[HistoryEventExecutionDataDetailsTypeDef],
        "timeoutInSeconds": NotRequired[int],
        "taskCredentials": NotRequired[TaskCredentialsTypeDef],
    },
)

class TaskScheduledEventDetailsTypeDef(TypedDict):
    resourceType: str
    resource: str
    region: str
    parameters: str
    timeoutInSeconds: NotRequired[int]
    heartbeatInSeconds: NotRequired[int]
    taskCredentials: NotRequired[TaskCredentialsTypeDef]

class ListMapRunsOutputTypeDef(TypedDict):
    mapRuns: List[MapRunListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListStateMachineAliasesOutputTypeDef(TypedDict):
    stateMachineAliases: List[StateMachineAliasListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListStateMachineVersionsOutputTypeDef(TypedDict):
    stateMachineVersions: List[StateMachineVersionListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListStateMachinesOutputTypeDef(TypedDict):
    stateMachines: List[StateMachineListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ValidateStateMachineDefinitionOutputTypeDef(TypedDict):
    result: ValidateStateMachineDefinitionResultCodeType
    diagnostics: List[ValidateStateMachineDefinitionDiagnosticTypeDef]
    truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class LoggingConfigurationOutputTypeDef(TypedDict):
    level: NotRequired[LogLevelType]
    includeExecutionData: NotRequired[bool]
    destinations: NotRequired[List[LogDestinationTypeDef]]

class LoggingConfigurationTypeDef(TypedDict):
    level: NotRequired[LogLevelType]
    includeExecutionData: NotRequired[bool]
    destinations: NotRequired[Sequence[LogDestinationTypeDef]]

class TestStateOutputTypeDef(TypedDict):
    output: str
    error: str
    cause: str
    inspectionData: InspectionDataTypeDef
    nextState: str
    status: TestExecutionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

HistoryEventTypeDef = TypedDict(
    "HistoryEventTypeDef",
    {
        "timestamp": datetime,
        "type": HistoryEventTypeType,
        "id": int,
        "previousEventId": NotRequired[int],
        "activityFailedEventDetails": NotRequired[ActivityFailedEventDetailsTypeDef],
        "activityScheduleFailedEventDetails": NotRequired[
            ActivityScheduleFailedEventDetailsTypeDef
        ],
        "activityScheduledEventDetails": NotRequired[ActivityScheduledEventDetailsTypeDef],
        "activityStartedEventDetails": NotRequired[ActivityStartedEventDetailsTypeDef],
        "activitySucceededEventDetails": NotRequired[ActivitySucceededEventDetailsTypeDef],
        "activityTimedOutEventDetails": NotRequired[ActivityTimedOutEventDetailsTypeDef],
        "taskFailedEventDetails": NotRequired[TaskFailedEventDetailsTypeDef],
        "taskScheduledEventDetails": NotRequired[TaskScheduledEventDetailsTypeDef],
        "taskStartFailedEventDetails": NotRequired[TaskStartFailedEventDetailsTypeDef],
        "taskStartedEventDetails": NotRequired[TaskStartedEventDetailsTypeDef],
        "taskSubmitFailedEventDetails": NotRequired[TaskSubmitFailedEventDetailsTypeDef],
        "taskSubmittedEventDetails": NotRequired[TaskSubmittedEventDetailsTypeDef],
        "taskSucceededEventDetails": NotRequired[TaskSucceededEventDetailsTypeDef],
        "taskTimedOutEventDetails": NotRequired[TaskTimedOutEventDetailsTypeDef],
        "executionFailedEventDetails": NotRequired[ExecutionFailedEventDetailsTypeDef],
        "executionStartedEventDetails": NotRequired[ExecutionStartedEventDetailsTypeDef],
        "executionSucceededEventDetails": NotRequired[ExecutionSucceededEventDetailsTypeDef],
        "executionAbortedEventDetails": NotRequired[ExecutionAbortedEventDetailsTypeDef],
        "executionTimedOutEventDetails": NotRequired[ExecutionTimedOutEventDetailsTypeDef],
        "executionRedrivenEventDetails": NotRequired[ExecutionRedrivenEventDetailsTypeDef],
        "mapStateStartedEventDetails": NotRequired[MapStateStartedEventDetailsTypeDef],
        "mapIterationStartedEventDetails": NotRequired[MapIterationEventDetailsTypeDef],
        "mapIterationSucceededEventDetails": NotRequired[MapIterationEventDetailsTypeDef],
        "mapIterationFailedEventDetails": NotRequired[MapIterationEventDetailsTypeDef],
        "mapIterationAbortedEventDetails": NotRequired[MapIterationEventDetailsTypeDef],
        "lambdaFunctionFailedEventDetails": NotRequired[LambdaFunctionFailedEventDetailsTypeDef],
        "lambdaFunctionScheduleFailedEventDetails": NotRequired[
            LambdaFunctionScheduleFailedEventDetailsTypeDef
        ],
        "lambdaFunctionScheduledEventDetails": NotRequired[
            LambdaFunctionScheduledEventDetailsTypeDef
        ],
        "lambdaFunctionStartFailedEventDetails": NotRequired[
            LambdaFunctionStartFailedEventDetailsTypeDef
        ],
        "lambdaFunctionSucceededEventDetails": NotRequired[
            LambdaFunctionSucceededEventDetailsTypeDef
        ],
        "lambdaFunctionTimedOutEventDetails": NotRequired[
            LambdaFunctionTimedOutEventDetailsTypeDef
        ],
        "stateEnteredEventDetails": NotRequired[StateEnteredEventDetailsTypeDef],
        "stateExitedEventDetails": NotRequired[StateExitedEventDetailsTypeDef],
        "mapRunStartedEventDetails": NotRequired[MapRunStartedEventDetailsTypeDef],
        "mapRunFailedEventDetails": NotRequired[MapRunFailedEventDetailsTypeDef],
        "mapRunRedrivenEventDetails": NotRequired[MapRunRedrivenEventDetailsTypeDef],
        "evaluationFailedEventDetails": NotRequired[EvaluationFailedEventDetailsTypeDef],
    },
)

class DescribeStateMachineForExecutionOutputTypeDef(TypedDict):
    stateMachineArn: str
    name: str
    definition: str
    roleArn: str
    updateDate: datetime
    loggingConfiguration: LoggingConfigurationOutputTypeDef
    tracingConfiguration: TracingConfigurationTypeDef
    mapRunArn: str
    label: str
    revisionId: str
    encryptionConfiguration: EncryptionConfigurationTypeDef
    variableReferences: Dict[str, List[str]]
    ResponseMetadata: ResponseMetadataTypeDef

DescribeStateMachineOutputTypeDef = TypedDict(
    "DescribeStateMachineOutputTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "status": StateMachineStatusType,
        "definition": str,
        "roleArn": str,
        "type": StateMachineTypeType,
        "creationDate": datetime,
        "loggingConfiguration": LoggingConfigurationOutputTypeDef,
        "tracingConfiguration": TracingConfigurationTypeDef,
        "label": str,
        "revisionId": str,
        "description": str,
        "encryptionConfiguration": EncryptionConfigurationTypeDef,
        "variableReferences": Dict[str, List[str]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LoggingConfigurationUnionTypeDef = Union[
    LoggingConfigurationTypeDef, LoggingConfigurationOutputTypeDef
]

class GetExecutionHistoryOutputTypeDef(TypedDict):
    events: List[HistoryEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

CreateStateMachineInputTypeDef = TypedDict(
    "CreateStateMachineInputTypeDef",
    {
        "name": str,
        "definition": str,
        "roleArn": str,
        "type": NotRequired[StateMachineTypeType],
        "loggingConfiguration": NotRequired[LoggingConfigurationUnionTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "tracingConfiguration": NotRequired[TracingConfigurationTypeDef],
        "publish": NotRequired[bool],
        "versionDescription": NotRequired[str],
        "encryptionConfiguration": NotRequired[EncryptionConfigurationTypeDef],
    },
)

class UpdateStateMachineInputTypeDef(TypedDict):
    stateMachineArn: str
    definition: NotRequired[str]
    roleArn: NotRequired[str]
    loggingConfiguration: NotRequired[LoggingConfigurationUnionTypeDef]
    tracingConfiguration: NotRequired[TracingConfigurationTypeDef]
    publish: NotRequired[bool]
    versionDescription: NotRequired[str]
    encryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]
