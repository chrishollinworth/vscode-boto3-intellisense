"""
Type annotations for swf service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_swf.type_defs import ActivityTaskCancelRequestedEventAttributesTypeDef

    data: ActivityTaskCancelRequestedEventAttributesTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ActivityTaskTimeoutTypeType,
    CancelTimerFailedCauseType,
    CancelWorkflowExecutionFailedCauseType,
    ChildPolicyType,
    CloseStatusType,
    CompleteWorkflowExecutionFailedCauseType,
    ContinueAsNewWorkflowExecutionFailedCauseType,
    DecisionTaskTimeoutTypeType,
    DecisionTypeType,
    EventTypeType,
    ExecutionStatusType,
    FailWorkflowExecutionFailedCauseType,
    RegistrationStatusType,
    RequestCancelActivityTaskFailedCauseType,
    RequestCancelExternalWorkflowExecutionFailedCauseType,
    ScheduleActivityTaskFailedCauseType,
    ScheduleLambdaFunctionFailedCauseType,
    SignalExternalWorkflowExecutionFailedCauseType,
    StartChildWorkflowExecutionFailedCauseType,
    StartTimerFailedCauseType,
    WorkflowExecutionTerminatedCauseType,
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
    "ActivityTaskCancelRequestedEventAttributesTypeDef",
    "ActivityTaskCanceledEventAttributesTypeDef",
    "ActivityTaskCompletedEventAttributesTypeDef",
    "ActivityTaskFailedEventAttributesTypeDef",
    "ActivityTaskScheduledEventAttributesTypeDef",
    "ActivityTaskStartedEventAttributesTypeDef",
    "ActivityTaskStatusTypeDef",
    "ActivityTaskTimedOutEventAttributesTypeDef",
    "ActivityTaskTypeDef",
    "ActivityTypeConfigurationTypeDef",
    "ActivityTypeDetailTypeDef",
    "ActivityTypeInfoTypeDef",
    "ActivityTypeInfosTypeDef",
    "ActivityTypeTypeDef",
    "CancelTimerDecisionAttributesTypeDef",
    "CancelTimerFailedEventAttributesTypeDef",
    "CancelWorkflowExecutionDecisionAttributesTypeDef",
    "CancelWorkflowExecutionFailedEventAttributesTypeDef",
    "ChildWorkflowExecutionCanceledEventAttributesTypeDef",
    "ChildWorkflowExecutionCompletedEventAttributesTypeDef",
    "ChildWorkflowExecutionFailedEventAttributesTypeDef",
    "ChildWorkflowExecutionStartedEventAttributesTypeDef",
    "ChildWorkflowExecutionTerminatedEventAttributesTypeDef",
    "ChildWorkflowExecutionTimedOutEventAttributesTypeDef",
    "CloseStatusFilterTypeDef",
    "CompleteWorkflowExecutionDecisionAttributesTypeDef",
    "CompleteWorkflowExecutionFailedEventAttributesTypeDef",
    "ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef",
    "ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef",
    "CountClosedWorkflowExecutionsInputTypeDef",
    "CountOpenWorkflowExecutionsInputTypeDef",
    "CountPendingActivityTasksInputTypeDef",
    "CountPendingDecisionTasksInputTypeDef",
    "DecisionTaskCompletedEventAttributesTypeDef",
    "DecisionTaskScheduledEventAttributesTypeDef",
    "DecisionTaskStartedEventAttributesTypeDef",
    "DecisionTaskTimedOutEventAttributesTypeDef",
    "DecisionTaskTypeDef",
    "DecisionTypeDef",
    "DeleteActivityTypeInputTypeDef",
    "DeleteWorkflowTypeInputTypeDef",
    "DeprecateActivityTypeInputTypeDef",
    "DeprecateDomainInputTypeDef",
    "DeprecateWorkflowTypeInputTypeDef",
    "DescribeActivityTypeInputTypeDef",
    "DescribeDomainInputTypeDef",
    "DescribeWorkflowExecutionInputTypeDef",
    "DescribeWorkflowTypeInputTypeDef",
    "DomainConfigurationTypeDef",
    "DomainDetailTypeDef",
    "DomainInfoTypeDef",
    "DomainInfosTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExecutionTimeFilterTypeDef",
    "ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef",
    "ExternalWorkflowExecutionSignaledEventAttributesTypeDef",
    "FailWorkflowExecutionDecisionAttributesTypeDef",
    "FailWorkflowExecutionFailedEventAttributesTypeDef",
    "GetWorkflowExecutionHistoryInputPaginateTypeDef",
    "GetWorkflowExecutionHistoryInputTypeDef",
    "HistoryEventTypeDef",
    "HistoryTypeDef",
    "LambdaFunctionCompletedEventAttributesTypeDef",
    "LambdaFunctionFailedEventAttributesTypeDef",
    "LambdaFunctionScheduledEventAttributesTypeDef",
    "LambdaFunctionStartedEventAttributesTypeDef",
    "LambdaFunctionTimedOutEventAttributesTypeDef",
    "ListActivityTypesInputPaginateTypeDef",
    "ListActivityTypesInputTypeDef",
    "ListClosedWorkflowExecutionsInputPaginateTypeDef",
    "ListClosedWorkflowExecutionsInputTypeDef",
    "ListDomainsInputPaginateTypeDef",
    "ListDomainsInputTypeDef",
    "ListOpenWorkflowExecutionsInputPaginateTypeDef",
    "ListOpenWorkflowExecutionsInputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListWorkflowTypesInputPaginateTypeDef",
    "ListWorkflowTypesInputTypeDef",
    "MarkerRecordedEventAttributesTypeDef",
    "PaginatorConfigTypeDef",
    "PendingTaskCountTypeDef",
    "PollForActivityTaskInputTypeDef",
    "PollForDecisionTaskInputPaginateTypeDef",
    "PollForDecisionTaskInputTypeDef",
    "RecordActivityTaskHeartbeatInputTypeDef",
    "RecordMarkerDecisionAttributesTypeDef",
    "RecordMarkerFailedEventAttributesTypeDef",
    "RegisterActivityTypeInputTypeDef",
    "RegisterDomainInputTypeDef",
    "RegisterWorkflowTypeInputTypeDef",
    "RequestCancelActivityTaskDecisionAttributesTypeDef",
    "RequestCancelActivityTaskFailedEventAttributesTypeDef",
    "RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef",
    "RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef",
    "RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    "RequestCancelWorkflowExecutionInputTypeDef",
    "ResourceTagTypeDef",
    "RespondActivityTaskCanceledInputTypeDef",
    "RespondActivityTaskCompletedInputTypeDef",
    "RespondActivityTaskFailedInputTypeDef",
    "RespondDecisionTaskCompletedInputTypeDef",
    "ResponseMetadataTypeDef",
    "RunTypeDef",
    "ScheduleActivityTaskDecisionAttributesTypeDef",
    "ScheduleActivityTaskFailedEventAttributesTypeDef",
    "ScheduleLambdaFunctionDecisionAttributesTypeDef",
    "ScheduleLambdaFunctionFailedEventAttributesTypeDef",
    "SignalExternalWorkflowExecutionDecisionAttributesTypeDef",
    "SignalExternalWorkflowExecutionFailedEventAttributesTypeDef",
    "SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    "SignalWorkflowExecutionInputTypeDef",
    "StartChildWorkflowExecutionDecisionAttributesTypeDef",
    "StartChildWorkflowExecutionFailedEventAttributesTypeDef",
    "StartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    "StartLambdaFunctionFailedEventAttributesTypeDef",
    "StartTimerDecisionAttributesTypeDef",
    "StartTimerFailedEventAttributesTypeDef",
    "StartWorkflowExecutionInputTypeDef",
    "TagFilterTypeDef",
    "TagResourceInputTypeDef",
    "TaskListTypeDef",
    "TerminateWorkflowExecutionInputTypeDef",
    "TimerCanceledEventAttributesTypeDef",
    "TimerFiredEventAttributesTypeDef",
    "TimerStartedEventAttributesTypeDef",
    "TimestampTypeDef",
    "UndeprecateActivityTypeInputTypeDef",
    "UndeprecateDomainInputTypeDef",
    "UndeprecateWorkflowTypeInputTypeDef",
    "UntagResourceInputTypeDef",
    "WorkflowExecutionCancelRequestedEventAttributesTypeDef",
    "WorkflowExecutionCanceledEventAttributesTypeDef",
    "WorkflowExecutionCompletedEventAttributesTypeDef",
    "WorkflowExecutionConfigurationTypeDef",
    "WorkflowExecutionContinuedAsNewEventAttributesTypeDef",
    "WorkflowExecutionCountTypeDef",
    "WorkflowExecutionDetailTypeDef",
    "WorkflowExecutionFailedEventAttributesTypeDef",
    "WorkflowExecutionFilterTypeDef",
    "WorkflowExecutionInfoTypeDef",
    "WorkflowExecutionInfosTypeDef",
    "WorkflowExecutionOpenCountsTypeDef",
    "WorkflowExecutionSignaledEventAttributesTypeDef",
    "WorkflowExecutionStartedEventAttributesTypeDef",
    "WorkflowExecutionTerminatedEventAttributesTypeDef",
    "WorkflowExecutionTimedOutEventAttributesTypeDef",
    "WorkflowExecutionTypeDef",
    "WorkflowTypeConfigurationTypeDef",
    "WorkflowTypeDetailTypeDef",
    "WorkflowTypeFilterTypeDef",
    "WorkflowTypeInfoTypeDef",
    "WorkflowTypeInfosTypeDef",
    "WorkflowTypeTypeDef",
)

class ActivityTaskCancelRequestedEventAttributesTypeDef(TypedDict):
    decisionTaskCompletedEventId: int
    activityId: str

class ActivityTaskCanceledEventAttributesTypeDef(TypedDict):
    scheduledEventId: int
    startedEventId: int
    details: NotRequired[str]
    latestCancelRequestedEventId: NotRequired[int]

class ActivityTaskCompletedEventAttributesTypeDef(TypedDict):
    scheduledEventId: int
    startedEventId: int
    result: NotRequired[str]

class ActivityTaskFailedEventAttributesTypeDef(TypedDict):
    scheduledEventId: int
    startedEventId: int
    reason: NotRequired[str]
    details: NotRequired[str]

class ActivityTypeTypeDef(TypedDict):
    name: str
    version: str

class TaskListTypeDef(TypedDict):
    name: str

class ActivityTaskStartedEventAttributesTypeDef(TypedDict):
    scheduledEventId: int
    identity: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ActivityTaskTimedOutEventAttributesTypeDef(TypedDict):
    timeoutType: ActivityTaskTimeoutTypeType
    scheduledEventId: int
    startedEventId: int
    details: NotRequired[str]

class WorkflowExecutionTypeDef(TypedDict):
    workflowId: str
    runId: str

class CancelTimerDecisionAttributesTypeDef(TypedDict):
    timerId: str

class CancelTimerFailedEventAttributesTypeDef(TypedDict):
    timerId: str
    cause: CancelTimerFailedCauseType
    decisionTaskCompletedEventId: int

class CancelWorkflowExecutionDecisionAttributesTypeDef(TypedDict):
    details: NotRequired[str]

class CancelWorkflowExecutionFailedEventAttributesTypeDef(TypedDict):
    cause: CancelWorkflowExecutionFailedCauseType
    decisionTaskCompletedEventId: int

class WorkflowTypeTypeDef(TypedDict):
    name: str
    version: str

class CloseStatusFilterTypeDef(TypedDict):
    status: CloseStatusType

class CompleteWorkflowExecutionDecisionAttributesTypeDef(TypedDict):
    result: NotRequired[str]

class CompleteWorkflowExecutionFailedEventAttributesTypeDef(TypedDict):
    cause: CompleteWorkflowExecutionFailedCauseType
    decisionTaskCompletedEventId: int

class ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef(TypedDict):
    cause: ContinueAsNewWorkflowExecutionFailedCauseType
    decisionTaskCompletedEventId: int

class TagFilterTypeDef(TypedDict):
    tag: str

class WorkflowExecutionFilterTypeDef(TypedDict):
    workflowId: str

class WorkflowTypeFilterTypeDef(TypedDict):
    name: str
    version: NotRequired[str]

class DecisionTaskStartedEventAttributesTypeDef(TypedDict):
    scheduledEventId: int
    identity: NotRequired[str]

class DecisionTaskTimedOutEventAttributesTypeDef(TypedDict):
    timeoutType: DecisionTaskTimeoutTypeType
    scheduledEventId: int
    startedEventId: int

class FailWorkflowExecutionDecisionAttributesTypeDef(TypedDict):
    reason: NotRequired[str]
    details: NotRequired[str]

class RecordMarkerDecisionAttributesTypeDef(TypedDict):
    markerName: str
    details: NotRequired[str]

class RequestCancelActivityTaskDecisionAttributesTypeDef(TypedDict):
    activityId: str

class RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef(TypedDict):
    workflowId: str
    runId: NotRequired[str]
    control: NotRequired[str]

ScheduleLambdaFunctionDecisionAttributesTypeDef = TypedDict(
    "ScheduleLambdaFunctionDecisionAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "control": NotRequired[str],
        "input": NotRequired[str],
        "startToCloseTimeout": NotRequired[str],
    },
)
SignalExternalWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "SignalExternalWorkflowExecutionDecisionAttributesTypeDef",
    {
        "workflowId": str,
        "signalName": str,
        "runId": NotRequired[str],
        "input": NotRequired[str],
        "control": NotRequired[str],
    },
)

class StartTimerDecisionAttributesTypeDef(TypedDict):
    timerId: str
    startToFireTimeout: str
    control: NotRequired[str]

class DeprecateDomainInputTypeDef(TypedDict):
    name: str

class DescribeDomainInputTypeDef(TypedDict):
    name: str

class DomainConfigurationTypeDef(TypedDict):
    workflowExecutionRetentionPeriodInDays: str

class DomainInfoTypeDef(TypedDict):
    name: str
    status: RegistrationStatusType
    description: NotRequired[str]
    arn: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class FailWorkflowExecutionFailedEventAttributesTypeDef(TypedDict):
    cause: FailWorkflowExecutionFailedCauseType
    decisionTaskCompletedEventId: int

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class LambdaFunctionCompletedEventAttributesTypeDef(TypedDict):
    scheduledEventId: int
    startedEventId: int
    result: NotRequired[str]

class LambdaFunctionFailedEventAttributesTypeDef(TypedDict):
    scheduledEventId: int
    startedEventId: int
    reason: NotRequired[str]
    details: NotRequired[str]

LambdaFunctionScheduledEventAttributesTypeDef = TypedDict(
    "LambdaFunctionScheduledEventAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "decisionTaskCompletedEventId": int,
        "control": NotRequired[str],
        "input": NotRequired[str],
        "startToCloseTimeout": NotRequired[str],
    },
)

class LambdaFunctionStartedEventAttributesTypeDef(TypedDict):
    scheduledEventId: int

class LambdaFunctionTimedOutEventAttributesTypeDef(TypedDict):
    scheduledEventId: int
    startedEventId: int
    timeoutType: NotRequired[Literal["START_TO_CLOSE"]]

class MarkerRecordedEventAttributesTypeDef(TypedDict):
    markerName: str
    decisionTaskCompletedEventId: int
    details: NotRequired[str]

class RecordMarkerFailedEventAttributesTypeDef(TypedDict):
    markerName: str
    cause: Literal["OPERATION_NOT_PERMITTED"]
    decisionTaskCompletedEventId: int

class RequestCancelActivityTaskFailedEventAttributesTypeDef(TypedDict):
    activityId: str
    cause: RequestCancelActivityTaskFailedCauseType
    decisionTaskCompletedEventId: int

class RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef(TypedDict):
    workflowId: str
    cause: RequestCancelExternalWorkflowExecutionFailedCauseType
    initiatedEventId: int
    decisionTaskCompletedEventId: int
    runId: NotRequired[str]
    control: NotRequired[str]

class RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef(TypedDict):
    workflowId: str
    decisionTaskCompletedEventId: int
    runId: NotRequired[str]
    control: NotRequired[str]

ScheduleLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "ScheduleLambdaFunctionFailedEventAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "cause": ScheduleLambdaFunctionFailedCauseType,
        "decisionTaskCompletedEventId": int,
    },
)

class SignalExternalWorkflowExecutionFailedEventAttributesTypeDef(TypedDict):
    workflowId: str
    cause: SignalExternalWorkflowExecutionFailedCauseType
    initiatedEventId: int
    decisionTaskCompletedEventId: int
    runId: NotRequired[str]
    control: NotRequired[str]

SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "signalName": str,
        "decisionTaskCompletedEventId": int,
        "runId": NotRequired[str],
        "input": NotRequired[str],
        "control": NotRequired[str],
    },
)

class StartLambdaFunctionFailedEventAttributesTypeDef(TypedDict):
    scheduledEventId: NotRequired[int]
    cause: NotRequired[Literal["ASSUME_ROLE_FAILED"]]
    message: NotRequired[str]

class StartTimerFailedEventAttributesTypeDef(TypedDict):
    timerId: str
    cause: StartTimerFailedCauseType
    decisionTaskCompletedEventId: int

class TimerCanceledEventAttributesTypeDef(TypedDict):
    timerId: str
    startedEventId: int
    decisionTaskCompletedEventId: int

class TimerFiredEventAttributesTypeDef(TypedDict):
    timerId: str
    startedEventId: int

class TimerStartedEventAttributesTypeDef(TypedDict):
    timerId: str
    startToFireTimeout: str
    decisionTaskCompletedEventId: int
    control: NotRequired[str]

class WorkflowExecutionCanceledEventAttributesTypeDef(TypedDict):
    decisionTaskCompletedEventId: int
    details: NotRequired[str]

class WorkflowExecutionCompletedEventAttributesTypeDef(TypedDict):
    decisionTaskCompletedEventId: int
    result: NotRequired[str]

class WorkflowExecutionFailedEventAttributesTypeDef(TypedDict):
    decisionTaskCompletedEventId: int
    reason: NotRequired[str]
    details: NotRequired[str]

class WorkflowExecutionTerminatedEventAttributesTypeDef(TypedDict):
    childPolicy: ChildPolicyType
    reason: NotRequired[str]
    details: NotRequired[str]
    cause: NotRequired[WorkflowExecutionTerminatedCauseType]

class WorkflowExecutionTimedOutEventAttributesTypeDef(TypedDict):
    timeoutType: Literal["START_TO_CLOSE"]
    childPolicy: ChildPolicyType

class ListActivityTypesInputTypeDef(TypedDict):
    domain: str
    registrationStatus: RegistrationStatusType
    name: NotRequired[str]
    nextPageToken: NotRequired[str]
    maximumPageSize: NotRequired[int]
    reverseOrder: NotRequired[bool]

class ListDomainsInputTypeDef(TypedDict):
    registrationStatus: RegistrationStatusType
    nextPageToken: NotRequired[str]
    maximumPageSize: NotRequired[int]
    reverseOrder: NotRequired[bool]

class ListTagsForResourceInputTypeDef(TypedDict):
    resourceArn: str

class ResourceTagTypeDef(TypedDict):
    key: str
    value: NotRequired[str]

class ListWorkflowTypesInputTypeDef(TypedDict):
    domain: str
    registrationStatus: RegistrationStatusType
    name: NotRequired[str]
    nextPageToken: NotRequired[str]
    maximumPageSize: NotRequired[int]
    reverseOrder: NotRequired[bool]

class RecordActivityTaskHeartbeatInputTypeDef(TypedDict):
    taskToken: str
    details: NotRequired[str]

class RequestCancelWorkflowExecutionInputTypeDef(TypedDict):
    domain: str
    workflowId: str
    runId: NotRequired[str]

class RespondActivityTaskCanceledInputTypeDef(TypedDict):
    taskToken: str
    details: NotRequired[str]

class RespondActivityTaskCompletedInputTypeDef(TypedDict):
    taskToken: str
    result: NotRequired[str]

class RespondActivityTaskFailedInputTypeDef(TypedDict):
    taskToken: str
    reason: NotRequired[str]
    details: NotRequired[str]

SignalWorkflowExecutionInputTypeDef = TypedDict(
    "SignalWorkflowExecutionInputTypeDef",
    {
        "domain": str,
        "workflowId": str,
        "signalName": str,
        "runId": NotRequired[str],
        "input": NotRequired[str],
    },
)

class TerminateWorkflowExecutionInputTypeDef(TypedDict):
    domain: str
    workflowId: str
    runId: NotRequired[str]
    reason: NotRequired[str]
    details: NotRequired[str]
    childPolicy: NotRequired[ChildPolicyType]

class UndeprecateDomainInputTypeDef(TypedDict):
    name: str

class UntagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class WorkflowExecutionOpenCountsTypeDef(TypedDict):
    openActivityTasks: int
    openDecisionTasks: int
    openTimers: int
    openChildWorkflowExecutions: int
    openLambdaFunctions: NotRequired[int]

class ActivityTypeInfoTypeDef(TypedDict):
    activityType: ActivityTypeTypeDef
    status: RegistrationStatusType
    creationDate: datetime
    description: NotRequired[str]
    deprecationDate: NotRequired[datetime]

class DeleteActivityTypeInputTypeDef(TypedDict):
    domain: str
    activityType: ActivityTypeTypeDef

class DeprecateActivityTypeInputTypeDef(TypedDict):
    domain: str
    activityType: ActivityTypeTypeDef

class DescribeActivityTypeInputTypeDef(TypedDict):
    domain: str
    activityType: ActivityTypeTypeDef

class ScheduleActivityTaskFailedEventAttributesTypeDef(TypedDict):
    activityType: ActivityTypeTypeDef
    activityId: str
    cause: ScheduleActivityTaskFailedCauseType
    decisionTaskCompletedEventId: int

class UndeprecateActivityTypeInputTypeDef(TypedDict):
    domain: str
    activityType: ActivityTypeTypeDef

ActivityTaskScheduledEventAttributesTypeDef = TypedDict(
    "ActivityTaskScheduledEventAttributesTypeDef",
    {
        "activityType": ActivityTypeTypeDef,
        "activityId": str,
        "taskList": TaskListTypeDef,
        "decisionTaskCompletedEventId": int,
        "input": NotRequired[str],
        "control": NotRequired[str],
        "scheduleToStartTimeout": NotRequired[str],
        "scheduleToCloseTimeout": NotRequired[str],
        "startToCloseTimeout": NotRequired[str],
        "taskPriority": NotRequired[str],
        "heartbeatTimeout": NotRequired[str],
    },
)

class ActivityTypeConfigurationTypeDef(TypedDict):
    defaultTaskStartToCloseTimeout: NotRequired[str]
    defaultTaskHeartbeatTimeout: NotRequired[str]
    defaultTaskList: NotRequired[TaskListTypeDef]
    defaultTaskPriority: NotRequired[str]
    defaultTaskScheduleToStartTimeout: NotRequired[str]
    defaultTaskScheduleToCloseTimeout: NotRequired[str]

ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef",
    {
        "input": NotRequired[str],
        "executionStartToCloseTimeout": NotRequired[str],
        "taskList": NotRequired[TaskListTypeDef],
        "taskPriority": NotRequired[str],
        "taskStartToCloseTimeout": NotRequired[str],
        "childPolicy": NotRequired[ChildPolicyType],
        "tagList": NotRequired[Sequence[str]],
        "workflowTypeVersion": NotRequired[str],
        "lambdaRole": NotRequired[str],
    },
)

class CountPendingActivityTasksInputTypeDef(TypedDict):
    domain: str
    taskList: TaskListTypeDef

class CountPendingDecisionTasksInputTypeDef(TypedDict):
    domain: str
    taskList: TaskListTypeDef

class DecisionTaskCompletedEventAttributesTypeDef(TypedDict):
    scheduledEventId: int
    startedEventId: int
    executionContext: NotRequired[str]
    taskList: NotRequired[TaskListTypeDef]
    taskListScheduleToStartTimeout: NotRequired[str]

class DecisionTaskScheduledEventAttributesTypeDef(TypedDict):
    taskList: TaskListTypeDef
    taskPriority: NotRequired[str]
    startToCloseTimeout: NotRequired[str]
    scheduleToStartTimeout: NotRequired[str]

class PollForActivityTaskInputTypeDef(TypedDict):
    domain: str
    taskList: TaskListTypeDef
    identity: NotRequired[str]

class PollForDecisionTaskInputTypeDef(TypedDict):
    domain: str
    taskList: TaskListTypeDef
    identity: NotRequired[str]
    nextPageToken: NotRequired[str]
    maximumPageSize: NotRequired[int]
    reverseOrder: NotRequired[bool]
    startAtPreviousStartedEvent: NotRequired[bool]

class RegisterActivityTypeInputTypeDef(TypedDict):
    domain: str
    name: str
    version: str
    description: NotRequired[str]
    defaultTaskStartToCloseTimeout: NotRequired[str]
    defaultTaskHeartbeatTimeout: NotRequired[str]
    defaultTaskList: NotRequired[TaskListTypeDef]
    defaultTaskPriority: NotRequired[str]
    defaultTaskScheduleToStartTimeout: NotRequired[str]
    defaultTaskScheduleToCloseTimeout: NotRequired[str]

class RegisterWorkflowTypeInputTypeDef(TypedDict):
    domain: str
    name: str
    version: str
    description: NotRequired[str]
    defaultTaskStartToCloseTimeout: NotRequired[str]
    defaultExecutionStartToCloseTimeout: NotRequired[str]
    defaultTaskList: NotRequired[TaskListTypeDef]
    defaultTaskPriority: NotRequired[str]
    defaultChildPolicy: NotRequired[ChildPolicyType]
    defaultLambdaRole: NotRequired[str]

ScheduleActivityTaskDecisionAttributesTypeDef = TypedDict(
    "ScheduleActivityTaskDecisionAttributesTypeDef",
    {
        "activityType": ActivityTypeTypeDef,
        "activityId": str,
        "control": NotRequired[str],
        "input": NotRequired[str],
        "scheduleToCloseTimeout": NotRequired[str],
        "taskList": NotRequired[TaskListTypeDef],
        "taskPriority": NotRequired[str],
        "scheduleToStartTimeout": NotRequired[str],
        "startToCloseTimeout": NotRequired[str],
        "heartbeatTimeout": NotRequired[str],
    },
)

class WorkflowExecutionConfigurationTypeDef(TypedDict):
    taskStartToCloseTimeout: str
    executionStartToCloseTimeout: str
    taskList: TaskListTypeDef
    childPolicy: ChildPolicyType
    taskPriority: NotRequired[str]
    lambdaRole: NotRequired[str]

class WorkflowTypeConfigurationTypeDef(TypedDict):
    defaultTaskStartToCloseTimeout: NotRequired[str]
    defaultExecutionStartToCloseTimeout: NotRequired[str]
    defaultTaskList: NotRequired[TaskListTypeDef]
    defaultTaskPriority: NotRequired[str]
    defaultChildPolicy: NotRequired[ChildPolicyType]
    defaultLambdaRole: NotRequired[str]

class ActivityTaskStatusTypeDef(TypedDict):
    cancelRequested: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class PendingTaskCountTypeDef(TypedDict):
    count: int
    truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class RunTypeDef(TypedDict):
    runId: str
    ResponseMetadata: ResponseMetadataTypeDef

class WorkflowExecutionCountTypeDef(TypedDict):
    count: int
    truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

ActivityTaskTypeDef = TypedDict(
    "ActivityTaskTypeDef",
    {
        "taskToken": str,
        "activityId": str,
        "startedEventId": int,
        "workflowExecution": WorkflowExecutionTypeDef,
        "activityType": ActivityTypeTypeDef,
        "input": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class DescribeWorkflowExecutionInputTypeDef(TypedDict):
    domain: str
    execution: WorkflowExecutionTypeDef

class ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef(TypedDict):
    workflowExecution: WorkflowExecutionTypeDef
    initiatedEventId: int

class ExternalWorkflowExecutionSignaledEventAttributesTypeDef(TypedDict):
    workflowExecution: WorkflowExecutionTypeDef
    initiatedEventId: int

class GetWorkflowExecutionHistoryInputTypeDef(TypedDict):
    domain: str
    execution: WorkflowExecutionTypeDef
    nextPageToken: NotRequired[str]
    maximumPageSize: NotRequired[int]
    reverseOrder: NotRequired[bool]

class WorkflowExecutionCancelRequestedEventAttributesTypeDef(TypedDict):
    externalWorkflowExecution: NotRequired[WorkflowExecutionTypeDef]
    externalInitiatedEventId: NotRequired[int]
    cause: NotRequired[Literal["CHILD_POLICY_APPLIED"]]

WorkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "WorkflowExecutionSignaledEventAttributesTypeDef",
    {
        "signalName": str,
        "input": NotRequired[str],
        "externalWorkflowExecution": NotRequired[WorkflowExecutionTypeDef],
        "externalInitiatedEventId": NotRequired[int],
    },
)

class ChildWorkflowExecutionCanceledEventAttributesTypeDef(TypedDict):
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    initiatedEventId: int
    startedEventId: int
    details: NotRequired[str]

class ChildWorkflowExecutionCompletedEventAttributesTypeDef(TypedDict):
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    initiatedEventId: int
    startedEventId: int
    result: NotRequired[str]

class ChildWorkflowExecutionFailedEventAttributesTypeDef(TypedDict):
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    initiatedEventId: int
    startedEventId: int
    reason: NotRequired[str]
    details: NotRequired[str]

class ChildWorkflowExecutionStartedEventAttributesTypeDef(TypedDict):
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    initiatedEventId: int

class ChildWorkflowExecutionTerminatedEventAttributesTypeDef(TypedDict):
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    initiatedEventId: int
    startedEventId: int

class ChildWorkflowExecutionTimedOutEventAttributesTypeDef(TypedDict):
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    timeoutType: Literal["START_TO_CLOSE"]
    initiatedEventId: int
    startedEventId: int

class DeleteWorkflowTypeInputTypeDef(TypedDict):
    domain: str
    workflowType: WorkflowTypeTypeDef

class DeprecateWorkflowTypeInputTypeDef(TypedDict):
    domain: str
    workflowType: WorkflowTypeTypeDef

class DescribeWorkflowTypeInputTypeDef(TypedDict):
    domain: str
    workflowType: WorkflowTypeTypeDef

StartChildWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "StartChildWorkflowExecutionDecisionAttributesTypeDef",
    {
        "workflowType": WorkflowTypeTypeDef,
        "workflowId": str,
        "control": NotRequired[str],
        "input": NotRequired[str],
        "executionStartToCloseTimeout": NotRequired[str],
        "taskList": NotRequired[TaskListTypeDef],
        "taskPriority": NotRequired[str],
        "taskStartToCloseTimeout": NotRequired[str],
        "childPolicy": NotRequired[ChildPolicyType],
        "tagList": NotRequired[Sequence[str]],
        "lambdaRole": NotRequired[str],
    },
)

class StartChildWorkflowExecutionFailedEventAttributesTypeDef(TypedDict):
    workflowType: WorkflowTypeTypeDef
    cause: StartChildWorkflowExecutionFailedCauseType
    workflowId: str
    initiatedEventId: int
    decisionTaskCompletedEventId: int
    control: NotRequired[str]

StartChildWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "StartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "workflowType": WorkflowTypeTypeDef,
        "taskList": TaskListTypeDef,
        "decisionTaskCompletedEventId": int,
        "childPolicy": ChildPolicyType,
        "control": NotRequired[str],
        "input": NotRequired[str],
        "executionStartToCloseTimeout": NotRequired[str],
        "taskPriority": NotRequired[str],
        "taskStartToCloseTimeout": NotRequired[str],
        "tagList": NotRequired[List[str]],
        "lambdaRole": NotRequired[str],
    },
)
StartWorkflowExecutionInputTypeDef = TypedDict(
    "StartWorkflowExecutionInputTypeDef",
    {
        "domain": str,
        "workflowId": str,
        "workflowType": WorkflowTypeTypeDef,
        "taskList": NotRequired[TaskListTypeDef],
        "taskPriority": NotRequired[str],
        "input": NotRequired[str],
        "executionStartToCloseTimeout": NotRequired[str],
        "tagList": NotRequired[Sequence[str]],
        "taskStartToCloseTimeout": NotRequired[str],
        "childPolicy": NotRequired[ChildPolicyType],
        "lambdaRole": NotRequired[str],
    },
)

class UndeprecateWorkflowTypeInputTypeDef(TypedDict):
    domain: str
    workflowType: WorkflowTypeTypeDef

WorkflowExecutionContinuedAsNewEventAttributesTypeDef = TypedDict(
    "WorkflowExecutionContinuedAsNewEventAttributesTypeDef",
    {
        "decisionTaskCompletedEventId": int,
        "newExecutionRunId": str,
        "taskList": TaskListTypeDef,
        "childPolicy": ChildPolicyType,
        "workflowType": WorkflowTypeTypeDef,
        "input": NotRequired[str],
        "executionStartToCloseTimeout": NotRequired[str],
        "taskPriority": NotRequired[str],
        "taskStartToCloseTimeout": NotRequired[str],
        "tagList": NotRequired[List[str]],
        "lambdaRole": NotRequired[str],
    },
)

class WorkflowExecutionInfoTypeDef(TypedDict):
    execution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    startTimestamp: datetime
    executionStatus: ExecutionStatusType
    closeTimestamp: NotRequired[datetime]
    closeStatus: NotRequired[CloseStatusType]
    parent: NotRequired[WorkflowExecutionTypeDef]
    tagList: NotRequired[List[str]]
    cancelRequested: NotRequired[bool]

WorkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "WorkflowExecutionStartedEventAttributesTypeDef",
    {
        "childPolicy": ChildPolicyType,
        "taskList": TaskListTypeDef,
        "workflowType": WorkflowTypeTypeDef,
        "input": NotRequired[str],
        "executionStartToCloseTimeout": NotRequired[str],
        "taskStartToCloseTimeout": NotRequired[str],
        "taskPriority": NotRequired[str],
        "tagList": NotRequired[List[str]],
        "continuedExecutionRunId": NotRequired[str],
        "parentWorkflowExecution": NotRequired[WorkflowExecutionTypeDef],
        "parentInitiatedEventId": NotRequired[int],
        "lambdaRole": NotRequired[str],
    },
)

class WorkflowTypeInfoTypeDef(TypedDict):
    workflowType: WorkflowTypeTypeDef
    status: RegistrationStatusType
    creationDate: datetime
    description: NotRequired[str]
    deprecationDate: NotRequired[datetime]

class DomainDetailTypeDef(TypedDict):
    domainInfo: DomainInfoTypeDef
    configuration: DomainConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DomainInfosTypeDef(TypedDict):
    domainInfos: List[DomainInfoTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExecutionTimeFilterTypeDef(TypedDict):
    oldestDate: TimestampTypeDef
    latestDate: NotRequired[TimestampTypeDef]

class GetWorkflowExecutionHistoryInputPaginateTypeDef(TypedDict):
    domain: str
    execution: WorkflowExecutionTypeDef
    reverseOrder: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListActivityTypesInputPaginateTypeDef(TypedDict):
    domain: str
    registrationStatus: RegistrationStatusType
    name: NotRequired[str]
    reverseOrder: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDomainsInputPaginateTypeDef(TypedDict):
    registrationStatus: RegistrationStatusType
    reverseOrder: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkflowTypesInputPaginateTypeDef(TypedDict):
    domain: str
    registrationStatus: RegistrationStatusType
    name: NotRequired[str]
    reverseOrder: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class PollForDecisionTaskInputPaginateTypeDef(TypedDict):
    domain: str
    taskList: TaskListTypeDef
    identity: NotRequired[str]
    reverseOrder: NotRequired[bool]
    startAtPreviousStartedEvent: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterDomainInputTypeDef(TypedDict):
    name: str
    workflowExecutionRetentionPeriodInDays: str
    description: NotRequired[str]
    tags: NotRequired[Sequence[ResourceTagTypeDef]]

class TagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[ResourceTagTypeDef]

class ActivityTypeInfosTypeDef(TypedDict):
    typeInfos: List[ActivityTypeInfoTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ActivityTypeDetailTypeDef(TypedDict):
    typeInfo: ActivityTypeInfoTypeDef
    configuration: ActivityTypeConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DecisionTypeDef(TypedDict):
    decisionType: DecisionTypeType
    scheduleActivityTaskDecisionAttributes: NotRequired[
        ScheduleActivityTaskDecisionAttributesTypeDef
    ]
    requestCancelActivityTaskDecisionAttributes: NotRequired[
        RequestCancelActivityTaskDecisionAttributesTypeDef
    ]
    completeWorkflowExecutionDecisionAttributes: NotRequired[
        CompleteWorkflowExecutionDecisionAttributesTypeDef
    ]
    failWorkflowExecutionDecisionAttributes: NotRequired[
        FailWorkflowExecutionDecisionAttributesTypeDef
    ]
    cancelWorkflowExecutionDecisionAttributes: NotRequired[
        CancelWorkflowExecutionDecisionAttributesTypeDef
    ]
    continueAsNewWorkflowExecutionDecisionAttributes: NotRequired[
        ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef
    ]
    recordMarkerDecisionAttributes: NotRequired[RecordMarkerDecisionAttributesTypeDef]
    startTimerDecisionAttributes: NotRequired[StartTimerDecisionAttributesTypeDef]
    cancelTimerDecisionAttributes: NotRequired[CancelTimerDecisionAttributesTypeDef]
    signalExternalWorkflowExecutionDecisionAttributes: NotRequired[
        SignalExternalWorkflowExecutionDecisionAttributesTypeDef
    ]
    requestCancelExternalWorkflowExecutionDecisionAttributes: NotRequired[
        RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef
    ]
    startChildWorkflowExecutionDecisionAttributes: NotRequired[
        StartChildWorkflowExecutionDecisionAttributesTypeDef
    ]
    scheduleLambdaFunctionDecisionAttributes: NotRequired[
        ScheduleLambdaFunctionDecisionAttributesTypeDef
    ]

class WorkflowExecutionDetailTypeDef(TypedDict):
    executionInfo: WorkflowExecutionInfoTypeDef
    executionConfiguration: WorkflowExecutionConfigurationTypeDef
    openCounts: WorkflowExecutionOpenCountsTypeDef
    latestActivityTaskTimestamp: datetime
    latestExecutionContext: str
    ResponseMetadata: ResponseMetadataTypeDef

class WorkflowExecutionInfosTypeDef(TypedDict):
    executionInfos: List[WorkflowExecutionInfoTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class HistoryEventTypeDef(TypedDict):
    eventTimestamp: datetime
    eventType: EventTypeType
    eventId: int
    workflowExecutionStartedEventAttributes: NotRequired[
        WorkflowExecutionStartedEventAttributesTypeDef
    ]
    workflowExecutionCompletedEventAttributes: NotRequired[
        WorkflowExecutionCompletedEventAttributesTypeDef
    ]
    completeWorkflowExecutionFailedEventAttributes: NotRequired[
        CompleteWorkflowExecutionFailedEventAttributesTypeDef
    ]
    workflowExecutionFailedEventAttributes: NotRequired[
        WorkflowExecutionFailedEventAttributesTypeDef
    ]
    failWorkflowExecutionFailedEventAttributes: NotRequired[
        FailWorkflowExecutionFailedEventAttributesTypeDef
    ]
    workflowExecutionTimedOutEventAttributes: NotRequired[
        WorkflowExecutionTimedOutEventAttributesTypeDef
    ]
    workflowExecutionCanceledEventAttributes: NotRequired[
        WorkflowExecutionCanceledEventAttributesTypeDef
    ]
    cancelWorkflowExecutionFailedEventAttributes: NotRequired[
        CancelWorkflowExecutionFailedEventAttributesTypeDef
    ]
    workflowExecutionContinuedAsNewEventAttributes: NotRequired[
        WorkflowExecutionContinuedAsNewEventAttributesTypeDef
    ]
    continueAsNewWorkflowExecutionFailedEventAttributes: NotRequired[
        ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef
    ]
    workflowExecutionTerminatedEventAttributes: NotRequired[
        WorkflowExecutionTerminatedEventAttributesTypeDef
    ]
    workflowExecutionCancelRequestedEventAttributes: NotRequired[
        WorkflowExecutionCancelRequestedEventAttributesTypeDef
    ]
    decisionTaskScheduledEventAttributes: NotRequired[DecisionTaskScheduledEventAttributesTypeDef]
    decisionTaskStartedEventAttributes: NotRequired[DecisionTaskStartedEventAttributesTypeDef]
    decisionTaskCompletedEventAttributes: NotRequired[DecisionTaskCompletedEventAttributesTypeDef]
    decisionTaskTimedOutEventAttributes: NotRequired[DecisionTaskTimedOutEventAttributesTypeDef]
    activityTaskScheduledEventAttributes: NotRequired[ActivityTaskScheduledEventAttributesTypeDef]
    activityTaskStartedEventAttributes: NotRequired[ActivityTaskStartedEventAttributesTypeDef]
    activityTaskCompletedEventAttributes: NotRequired[ActivityTaskCompletedEventAttributesTypeDef]
    activityTaskFailedEventAttributes: NotRequired[ActivityTaskFailedEventAttributesTypeDef]
    activityTaskTimedOutEventAttributes: NotRequired[ActivityTaskTimedOutEventAttributesTypeDef]
    activityTaskCanceledEventAttributes: NotRequired[ActivityTaskCanceledEventAttributesTypeDef]
    activityTaskCancelRequestedEventAttributes: NotRequired[
        ActivityTaskCancelRequestedEventAttributesTypeDef
    ]
    workflowExecutionSignaledEventAttributes: NotRequired[
        WorkflowExecutionSignaledEventAttributesTypeDef
    ]
    markerRecordedEventAttributes: NotRequired[MarkerRecordedEventAttributesTypeDef]
    recordMarkerFailedEventAttributes: NotRequired[RecordMarkerFailedEventAttributesTypeDef]
    timerStartedEventAttributes: NotRequired[TimerStartedEventAttributesTypeDef]
    timerFiredEventAttributes: NotRequired[TimerFiredEventAttributesTypeDef]
    timerCanceledEventAttributes: NotRequired[TimerCanceledEventAttributesTypeDef]
    startChildWorkflowExecutionInitiatedEventAttributes: NotRequired[
        StartChildWorkflowExecutionInitiatedEventAttributesTypeDef
    ]
    childWorkflowExecutionStartedEventAttributes: NotRequired[
        ChildWorkflowExecutionStartedEventAttributesTypeDef
    ]
    childWorkflowExecutionCompletedEventAttributes: NotRequired[
        ChildWorkflowExecutionCompletedEventAttributesTypeDef
    ]
    childWorkflowExecutionFailedEventAttributes: NotRequired[
        ChildWorkflowExecutionFailedEventAttributesTypeDef
    ]
    childWorkflowExecutionTimedOutEventAttributes: NotRequired[
        ChildWorkflowExecutionTimedOutEventAttributesTypeDef
    ]
    childWorkflowExecutionCanceledEventAttributes: NotRequired[
        ChildWorkflowExecutionCanceledEventAttributesTypeDef
    ]
    childWorkflowExecutionTerminatedEventAttributes: NotRequired[
        ChildWorkflowExecutionTerminatedEventAttributesTypeDef
    ]
    signalExternalWorkflowExecutionInitiatedEventAttributes: NotRequired[
        SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef
    ]
    externalWorkflowExecutionSignaledEventAttributes: NotRequired[
        ExternalWorkflowExecutionSignaledEventAttributesTypeDef
    ]
    signalExternalWorkflowExecutionFailedEventAttributes: NotRequired[
        SignalExternalWorkflowExecutionFailedEventAttributesTypeDef
    ]
    externalWorkflowExecutionCancelRequestedEventAttributes: NotRequired[
        ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef
    ]
    requestCancelExternalWorkflowExecutionInitiatedEventAttributes: NotRequired[
        RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef
    ]
    requestCancelExternalWorkflowExecutionFailedEventAttributes: NotRequired[
        RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef
    ]
    scheduleActivityTaskFailedEventAttributes: NotRequired[
        ScheduleActivityTaskFailedEventAttributesTypeDef
    ]
    requestCancelActivityTaskFailedEventAttributes: NotRequired[
        RequestCancelActivityTaskFailedEventAttributesTypeDef
    ]
    startTimerFailedEventAttributes: NotRequired[StartTimerFailedEventAttributesTypeDef]
    cancelTimerFailedEventAttributes: NotRequired[CancelTimerFailedEventAttributesTypeDef]
    startChildWorkflowExecutionFailedEventAttributes: NotRequired[
        StartChildWorkflowExecutionFailedEventAttributesTypeDef
    ]
    lambdaFunctionScheduledEventAttributes: NotRequired[
        LambdaFunctionScheduledEventAttributesTypeDef
    ]
    lambdaFunctionStartedEventAttributes: NotRequired[LambdaFunctionStartedEventAttributesTypeDef]
    lambdaFunctionCompletedEventAttributes: NotRequired[
        LambdaFunctionCompletedEventAttributesTypeDef
    ]
    lambdaFunctionFailedEventAttributes: NotRequired[LambdaFunctionFailedEventAttributesTypeDef]
    lambdaFunctionTimedOutEventAttributes: NotRequired[LambdaFunctionTimedOutEventAttributesTypeDef]
    scheduleLambdaFunctionFailedEventAttributes: NotRequired[
        ScheduleLambdaFunctionFailedEventAttributesTypeDef
    ]
    startLambdaFunctionFailedEventAttributes: NotRequired[
        StartLambdaFunctionFailedEventAttributesTypeDef
    ]

class WorkflowTypeDetailTypeDef(TypedDict):
    typeInfo: WorkflowTypeInfoTypeDef
    configuration: WorkflowTypeConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class WorkflowTypeInfosTypeDef(TypedDict):
    typeInfos: List[WorkflowTypeInfoTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CountClosedWorkflowExecutionsInputTypeDef(TypedDict):
    domain: str
    startTimeFilter: NotRequired[ExecutionTimeFilterTypeDef]
    closeTimeFilter: NotRequired[ExecutionTimeFilterTypeDef]
    executionFilter: NotRequired[WorkflowExecutionFilterTypeDef]
    typeFilter: NotRequired[WorkflowTypeFilterTypeDef]
    tagFilter: NotRequired[TagFilterTypeDef]
    closeStatusFilter: NotRequired[CloseStatusFilterTypeDef]

class CountOpenWorkflowExecutionsInputTypeDef(TypedDict):
    domain: str
    startTimeFilter: ExecutionTimeFilterTypeDef
    typeFilter: NotRequired[WorkflowTypeFilterTypeDef]
    tagFilter: NotRequired[TagFilterTypeDef]
    executionFilter: NotRequired[WorkflowExecutionFilterTypeDef]

class ListClosedWorkflowExecutionsInputPaginateTypeDef(TypedDict):
    domain: str
    startTimeFilter: NotRequired[ExecutionTimeFilterTypeDef]
    closeTimeFilter: NotRequired[ExecutionTimeFilterTypeDef]
    executionFilter: NotRequired[WorkflowExecutionFilterTypeDef]
    closeStatusFilter: NotRequired[CloseStatusFilterTypeDef]
    typeFilter: NotRequired[WorkflowTypeFilterTypeDef]
    tagFilter: NotRequired[TagFilterTypeDef]
    reverseOrder: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListClosedWorkflowExecutionsInputTypeDef(TypedDict):
    domain: str
    startTimeFilter: NotRequired[ExecutionTimeFilterTypeDef]
    closeTimeFilter: NotRequired[ExecutionTimeFilterTypeDef]
    executionFilter: NotRequired[WorkflowExecutionFilterTypeDef]
    closeStatusFilter: NotRequired[CloseStatusFilterTypeDef]
    typeFilter: NotRequired[WorkflowTypeFilterTypeDef]
    tagFilter: NotRequired[TagFilterTypeDef]
    nextPageToken: NotRequired[str]
    maximumPageSize: NotRequired[int]
    reverseOrder: NotRequired[bool]

class ListOpenWorkflowExecutionsInputPaginateTypeDef(TypedDict):
    domain: str
    startTimeFilter: ExecutionTimeFilterTypeDef
    typeFilter: NotRequired[WorkflowTypeFilterTypeDef]
    tagFilter: NotRequired[TagFilterTypeDef]
    reverseOrder: NotRequired[bool]
    executionFilter: NotRequired[WorkflowExecutionFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOpenWorkflowExecutionsInputTypeDef(TypedDict):
    domain: str
    startTimeFilter: ExecutionTimeFilterTypeDef
    typeFilter: NotRequired[WorkflowTypeFilterTypeDef]
    tagFilter: NotRequired[TagFilterTypeDef]
    nextPageToken: NotRequired[str]
    maximumPageSize: NotRequired[int]
    reverseOrder: NotRequired[bool]
    executionFilter: NotRequired[WorkflowExecutionFilterTypeDef]

class RespondDecisionTaskCompletedInputTypeDef(TypedDict):
    taskToken: str
    decisions: NotRequired[Sequence[DecisionTypeDef]]
    executionContext: NotRequired[str]
    taskList: NotRequired[TaskListTypeDef]
    taskListScheduleToStartTimeout: NotRequired[str]

class DecisionTaskTypeDef(TypedDict):
    taskToken: str
    startedEventId: int
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    events: List[HistoryEventTypeDef]
    nextPageToken: str
    previousStartedEventId: int
    ResponseMetadata: ResponseMetadataTypeDef

class HistoryTypeDef(TypedDict):
    events: List[HistoryEventTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef
