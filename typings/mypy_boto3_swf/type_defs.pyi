"""
Main interface for swf service type definitions.

Usage::

    ```python
    from mypy_boto3_swf.type_defs import ActivityTaskCancelRequestedEventAttributesTypeDef

    data: ActivityTaskCancelRequestedEventAttributesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActivityTaskCancelRequestedEventAttributesTypeDef",
    "ActivityTaskCanceledEventAttributesTypeDef",
    "ActivityTaskCompletedEventAttributesTypeDef",
    "ActivityTaskFailedEventAttributesTypeDef",
    "ActivityTaskScheduledEventAttributesTypeDef",
    "ActivityTaskStartedEventAttributesTypeDef",
    "ActivityTaskTimedOutEventAttributesTypeDef",
    "ActivityTypeConfigurationTypeDef",
    "ActivityTypeInfoTypeDef",
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
    "CompleteWorkflowExecutionDecisionAttributesTypeDef",
    "CompleteWorkflowExecutionFailedEventAttributesTypeDef",
    "ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef",
    "ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef",
    "DecisionTaskCompletedEventAttributesTypeDef",
    "DecisionTaskScheduledEventAttributesTypeDef",
    "DecisionTaskStartedEventAttributesTypeDef",
    "DecisionTaskTimedOutEventAttributesTypeDef",
    "DomainConfigurationTypeDef",
    "DomainInfoTypeDef",
    "ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef",
    "ExternalWorkflowExecutionSignaledEventAttributesTypeDef",
    "FailWorkflowExecutionDecisionAttributesTypeDef",
    "FailWorkflowExecutionFailedEventAttributesTypeDef",
    "HistoryEventTypeDef",
    "LambdaFunctionCompletedEventAttributesTypeDef",
    "LambdaFunctionFailedEventAttributesTypeDef",
    "LambdaFunctionScheduledEventAttributesTypeDef",
    "LambdaFunctionStartedEventAttributesTypeDef",
    "LambdaFunctionTimedOutEventAttributesTypeDef",
    "MarkerRecordedEventAttributesTypeDef",
    "RecordMarkerDecisionAttributesTypeDef",
    "RecordMarkerFailedEventAttributesTypeDef",
    "RequestCancelActivityTaskDecisionAttributesTypeDef",
    "RequestCancelActivityTaskFailedEventAttributesTypeDef",
    "RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef",
    "RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef",
    "RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    "ResourceTagTypeDef",
    "ScheduleActivityTaskDecisionAttributesTypeDef",
    "ScheduleActivityTaskFailedEventAttributesTypeDef",
    "ScheduleLambdaFunctionDecisionAttributesTypeDef",
    "ScheduleLambdaFunctionFailedEventAttributesTypeDef",
    "SignalExternalWorkflowExecutionDecisionAttributesTypeDef",
    "SignalExternalWorkflowExecutionFailedEventAttributesTypeDef",
    "SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    "StartChildWorkflowExecutionDecisionAttributesTypeDef",
    "StartChildWorkflowExecutionFailedEventAttributesTypeDef",
    "StartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    "StartLambdaFunctionFailedEventAttributesTypeDef",
    "StartTimerDecisionAttributesTypeDef",
    "StartTimerFailedEventAttributesTypeDef",
    "TaskListTypeDef",
    "TimerCanceledEventAttributesTypeDef",
    "TimerFiredEventAttributesTypeDef",
    "TimerStartedEventAttributesTypeDef",
    "WorkflowExecutionCancelRequestedEventAttributesTypeDef",
    "WorkflowExecutionCanceledEventAttributesTypeDef",
    "WorkflowExecutionCompletedEventAttributesTypeDef",
    "WorkflowExecutionConfigurationTypeDef",
    "WorkflowExecutionContinuedAsNewEventAttributesTypeDef",
    "WorkflowExecutionFailedEventAttributesTypeDef",
    "WorkflowExecutionInfoTypeDef",
    "WorkflowExecutionOpenCountsTypeDef",
    "WorkflowExecutionSignaledEventAttributesTypeDef",
    "WorkflowExecutionStartedEventAttributesTypeDef",
    "WorkflowExecutionTerminatedEventAttributesTypeDef",
    "WorkflowExecutionTimedOutEventAttributesTypeDef",
    "WorkflowExecutionTypeDef",
    "WorkflowTypeConfigurationTypeDef",
    "WorkflowTypeInfoTypeDef",
    "WorkflowTypeTypeDef",
    "ActivityTaskStatusTypeDef",
    "ActivityTaskTypeDef",
    "ActivityTypeDetailTypeDef",
    "ActivityTypeInfosTypeDef",
    "CloseStatusFilterTypeDef",
    "DecisionTaskTypeDef",
    "DecisionTypeDef",
    "DomainDetailTypeDef",
    "DomainInfosTypeDef",
    "ExecutionTimeFilterTypeDef",
    "HistoryTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PendingTaskCountTypeDef",
    "RunTypeDef",
    "TagFilterTypeDef",
    "WorkflowExecutionCountTypeDef",
    "WorkflowExecutionDetailTypeDef",
    "WorkflowExecutionFilterTypeDef",
    "WorkflowExecutionInfosTypeDef",
    "WorkflowTypeDetailTypeDef",
    "WorkflowTypeFilterTypeDef",
    "WorkflowTypeInfosTypeDef",
)

ActivityTaskCancelRequestedEventAttributesTypeDef = TypedDict(
    "ActivityTaskCancelRequestedEventAttributesTypeDef",
    {"decisionTaskCompletedEventId": int, "activityId": str},
)

_RequiredActivityTaskCanceledEventAttributesTypeDef = TypedDict(
    "_RequiredActivityTaskCanceledEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int},
)
_OptionalActivityTaskCanceledEventAttributesTypeDef = TypedDict(
    "_OptionalActivityTaskCanceledEventAttributesTypeDef",
    {"details": str, "latestCancelRequestedEventId": int},
    total=False,
)


class ActivityTaskCanceledEventAttributesTypeDef(
    _RequiredActivityTaskCanceledEventAttributesTypeDef,
    _OptionalActivityTaskCanceledEventAttributesTypeDef,
):
    pass


_RequiredActivityTaskCompletedEventAttributesTypeDef = TypedDict(
    "_RequiredActivityTaskCompletedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int},
)
_OptionalActivityTaskCompletedEventAttributesTypeDef = TypedDict(
    "_OptionalActivityTaskCompletedEventAttributesTypeDef", {"result": str}, total=False
)


class ActivityTaskCompletedEventAttributesTypeDef(
    _RequiredActivityTaskCompletedEventAttributesTypeDef,
    _OptionalActivityTaskCompletedEventAttributesTypeDef,
):
    pass


_RequiredActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "_RequiredActivityTaskFailedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int},
)
_OptionalActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "_OptionalActivityTaskFailedEventAttributesTypeDef",
    {"reason": str, "details": str},
    total=False,
)


class ActivityTaskFailedEventAttributesTypeDef(
    _RequiredActivityTaskFailedEventAttributesTypeDef,
    _OptionalActivityTaskFailedEventAttributesTypeDef,
):
    pass


_RequiredActivityTaskScheduledEventAttributesTypeDef = TypedDict(
    "_RequiredActivityTaskScheduledEventAttributesTypeDef",
    {
        "activityType": "ActivityTypeTypeDef",
        "activityId": str,
        "taskList": "TaskListTypeDef",
        "decisionTaskCompletedEventId": int,
    },
)
_OptionalActivityTaskScheduledEventAttributesTypeDef = TypedDict(
    "_OptionalActivityTaskScheduledEventAttributesTypeDef",
    {
        "input": str,
        "control": str,
        "scheduleToStartTimeout": str,
        "scheduleToCloseTimeout": str,
        "startToCloseTimeout": str,
        "taskPriority": str,
        "heartbeatTimeout": str,
    },
    total=False,
)


class ActivityTaskScheduledEventAttributesTypeDef(
    _RequiredActivityTaskScheduledEventAttributesTypeDef,
    _OptionalActivityTaskScheduledEventAttributesTypeDef,
):
    pass


_RequiredActivityTaskStartedEventAttributesTypeDef = TypedDict(
    "_RequiredActivityTaskStartedEventAttributesTypeDef", {"scheduledEventId": int}
)
_OptionalActivityTaskStartedEventAttributesTypeDef = TypedDict(
    "_OptionalActivityTaskStartedEventAttributesTypeDef", {"identity": str}, total=False
)


class ActivityTaskStartedEventAttributesTypeDef(
    _RequiredActivityTaskStartedEventAttributesTypeDef,
    _OptionalActivityTaskStartedEventAttributesTypeDef,
):
    pass


_RequiredActivityTaskTimedOutEventAttributesTypeDef = TypedDict(
    "_RequiredActivityTaskTimedOutEventAttributesTypeDef",
    {
        "timeoutType": Literal[
            "START_TO_CLOSE", "SCHEDULE_TO_START", "SCHEDULE_TO_CLOSE", "HEARTBEAT"
        ],
        "scheduledEventId": int,
        "startedEventId": int,
    },
)
_OptionalActivityTaskTimedOutEventAttributesTypeDef = TypedDict(
    "_OptionalActivityTaskTimedOutEventAttributesTypeDef", {"details": str}, total=False
)


class ActivityTaskTimedOutEventAttributesTypeDef(
    _RequiredActivityTaskTimedOutEventAttributesTypeDef,
    _OptionalActivityTaskTimedOutEventAttributesTypeDef,
):
    pass


ActivityTypeConfigurationTypeDef = TypedDict(
    "ActivityTypeConfigurationTypeDef",
    {
        "defaultTaskStartToCloseTimeout": str,
        "defaultTaskHeartbeatTimeout": str,
        "defaultTaskList": "TaskListTypeDef",
        "defaultTaskPriority": str,
        "defaultTaskScheduleToStartTimeout": str,
        "defaultTaskScheduleToCloseTimeout": str,
    },
    total=False,
)

_RequiredActivityTypeInfoTypeDef = TypedDict(
    "_RequiredActivityTypeInfoTypeDef",
    {
        "activityType": "ActivityTypeTypeDef",
        "status": Literal["REGISTERED", "DEPRECATED"],
        "creationDate": datetime,
    },
)
_OptionalActivityTypeInfoTypeDef = TypedDict(
    "_OptionalActivityTypeInfoTypeDef",
    {"description": str, "deprecationDate": datetime},
    total=False,
)


class ActivityTypeInfoTypeDef(_RequiredActivityTypeInfoTypeDef, _OptionalActivityTypeInfoTypeDef):
    pass


ActivityTypeTypeDef = TypedDict("ActivityTypeTypeDef", {"name": str, "version": str})

CancelTimerDecisionAttributesTypeDef = TypedDict(
    "CancelTimerDecisionAttributesTypeDef", {"timerId": str}
)

CancelTimerFailedEventAttributesTypeDef = TypedDict(
    "CancelTimerFailedEventAttributesTypeDef",
    {
        "timerId": str,
        "cause": Literal["TIMER_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
)

CancelWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "CancelWorkflowExecutionDecisionAttributesTypeDef", {"details": str}, total=False
)

CancelWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "CancelWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
)

_RequiredChildWorkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "_RequiredChildWorkflowExecutionCanceledEventAttributesTypeDef",
    {
        "workflowExecution": "WorkflowExecutionTypeDef",
        "workflowType": "WorkflowTypeTypeDef",
        "initiatedEventId": int,
        "startedEventId": int,
    },
)
_OptionalChildWorkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "_OptionalChildWorkflowExecutionCanceledEventAttributesTypeDef", {"details": str}, total=False
)


class ChildWorkflowExecutionCanceledEventAttributesTypeDef(
    _RequiredChildWorkflowExecutionCanceledEventAttributesTypeDef,
    _OptionalChildWorkflowExecutionCanceledEventAttributesTypeDef,
):
    pass


_RequiredChildWorkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "_RequiredChildWorkflowExecutionCompletedEventAttributesTypeDef",
    {
        "workflowExecution": "WorkflowExecutionTypeDef",
        "workflowType": "WorkflowTypeTypeDef",
        "initiatedEventId": int,
        "startedEventId": int,
    },
)
_OptionalChildWorkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "_OptionalChildWorkflowExecutionCompletedEventAttributesTypeDef", {"result": str}, total=False
)


class ChildWorkflowExecutionCompletedEventAttributesTypeDef(
    _RequiredChildWorkflowExecutionCompletedEventAttributesTypeDef,
    _OptionalChildWorkflowExecutionCompletedEventAttributesTypeDef,
):
    pass


_RequiredChildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_RequiredChildWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowExecution": "WorkflowExecutionTypeDef",
        "workflowType": "WorkflowTypeTypeDef",
        "initiatedEventId": int,
        "startedEventId": int,
    },
)
_OptionalChildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_OptionalChildWorkflowExecutionFailedEventAttributesTypeDef",
    {"reason": str, "details": str},
    total=False,
)


class ChildWorkflowExecutionFailedEventAttributesTypeDef(
    _RequiredChildWorkflowExecutionFailedEventAttributesTypeDef,
    _OptionalChildWorkflowExecutionFailedEventAttributesTypeDef,
):
    pass


ChildWorkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "ChildWorkflowExecutionStartedEventAttributesTypeDef",
    {
        "workflowExecution": "WorkflowExecutionTypeDef",
        "workflowType": "WorkflowTypeTypeDef",
        "initiatedEventId": int,
    },
)

ChildWorkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "ChildWorkflowExecutionTerminatedEventAttributesTypeDef",
    {
        "workflowExecution": "WorkflowExecutionTypeDef",
        "workflowType": "WorkflowTypeTypeDef",
        "initiatedEventId": int,
        "startedEventId": int,
    },
)

ChildWorkflowExecutionTimedOutEventAttributesTypeDef = TypedDict(
    "ChildWorkflowExecutionTimedOutEventAttributesTypeDef",
    {
        "workflowExecution": "WorkflowExecutionTypeDef",
        "workflowType": "WorkflowTypeTypeDef",
        "timeoutType": Literal["START_TO_CLOSE"],
        "initiatedEventId": int,
        "startedEventId": int,
    },
)

CompleteWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "CompleteWorkflowExecutionDecisionAttributesTypeDef", {"result": str}, total=False
)

CompleteWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "CompleteWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
)

ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef",
    {
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskList": "TaskListTypeDef",
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "tagList": List[str],
        "workflowTypeVersion": str,
        "lambdaRole": str,
    },
    total=False,
)

ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal[
            "UNHANDLED_DECISION",
            "WORKFLOW_TYPE_DEPRECATED",
            "WORKFLOW_TYPE_DOES_NOT_EXIST",
            "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_CHILD_POLICY_UNDEFINED",
            "CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
)

_RequiredDecisionTaskCompletedEventAttributesTypeDef = TypedDict(
    "_RequiredDecisionTaskCompletedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int},
)
_OptionalDecisionTaskCompletedEventAttributesTypeDef = TypedDict(
    "_OptionalDecisionTaskCompletedEventAttributesTypeDef", {"executionContext": str}, total=False
)


class DecisionTaskCompletedEventAttributesTypeDef(
    _RequiredDecisionTaskCompletedEventAttributesTypeDef,
    _OptionalDecisionTaskCompletedEventAttributesTypeDef,
):
    pass


_RequiredDecisionTaskScheduledEventAttributesTypeDef = TypedDict(
    "_RequiredDecisionTaskScheduledEventAttributesTypeDef", {"taskList": "TaskListTypeDef"}
)
_OptionalDecisionTaskScheduledEventAttributesTypeDef = TypedDict(
    "_OptionalDecisionTaskScheduledEventAttributesTypeDef",
    {"taskPriority": str, "startToCloseTimeout": str},
    total=False,
)


class DecisionTaskScheduledEventAttributesTypeDef(
    _RequiredDecisionTaskScheduledEventAttributesTypeDef,
    _OptionalDecisionTaskScheduledEventAttributesTypeDef,
):
    pass


_RequiredDecisionTaskStartedEventAttributesTypeDef = TypedDict(
    "_RequiredDecisionTaskStartedEventAttributesTypeDef", {"scheduledEventId": int}
)
_OptionalDecisionTaskStartedEventAttributesTypeDef = TypedDict(
    "_OptionalDecisionTaskStartedEventAttributesTypeDef", {"identity": str}, total=False
)


class DecisionTaskStartedEventAttributesTypeDef(
    _RequiredDecisionTaskStartedEventAttributesTypeDef,
    _OptionalDecisionTaskStartedEventAttributesTypeDef,
):
    pass


DecisionTaskTimedOutEventAttributesTypeDef = TypedDict(
    "DecisionTaskTimedOutEventAttributesTypeDef",
    {"timeoutType": Literal["START_TO_CLOSE"], "scheduledEventId": int, "startedEventId": int},
)

DomainConfigurationTypeDef = TypedDict(
    "DomainConfigurationTypeDef", {"workflowExecutionRetentionPeriodInDays": str}
)

_RequiredDomainInfoTypeDef = TypedDict(
    "_RequiredDomainInfoTypeDef", {"name": str, "status": Literal["REGISTERED", "DEPRECATED"]}
)
_OptionalDomainInfoTypeDef = TypedDict(
    "_OptionalDomainInfoTypeDef", {"description": str, "arn": str}, total=False
)


class DomainInfoTypeDef(_RequiredDomainInfoTypeDef, _OptionalDomainInfoTypeDef):
    pass


ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef = TypedDict(
    "ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef",
    {"workflowExecution": "WorkflowExecutionTypeDef", "initiatedEventId": int},
)

ExternalWorkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "ExternalWorkflowExecutionSignaledEventAttributesTypeDef",
    {"workflowExecution": "WorkflowExecutionTypeDef", "initiatedEventId": int},
)

FailWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "FailWorkflowExecutionDecisionAttributesTypeDef", {"reason": str, "details": str}, total=False
)

FailWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "FailWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": Literal["UNHANDLED_DECISION", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
)

_RequiredHistoryEventTypeDef = TypedDict(
    "_RequiredHistoryEventTypeDef",
    {
        "eventTimestamp": datetime,
        "eventType": Literal[
            "WorkflowExecutionStarted",
            "WorkflowExecutionCancelRequested",
            "WorkflowExecutionCompleted",
            "CompleteWorkflowExecutionFailed",
            "WorkflowExecutionFailed",
            "FailWorkflowExecutionFailed",
            "WorkflowExecutionTimedOut",
            "WorkflowExecutionCanceled",
            "CancelWorkflowExecutionFailed",
            "WorkflowExecutionContinuedAsNew",
            "ContinueAsNewWorkflowExecutionFailed",
            "WorkflowExecutionTerminated",
            "DecisionTaskScheduled",
            "DecisionTaskStarted",
            "DecisionTaskCompleted",
            "DecisionTaskTimedOut",
            "ActivityTaskScheduled",
            "ScheduleActivityTaskFailed",
            "ActivityTaskStarted",
            "ActivityTaskCompleted",
            "ActivityTaskFailed",
            "ActivityTaskTimedOut",
            "ActivityTaskCanceled",
            "ActivityTaskCancelRequested",
            "RequestCancelActivityTaskFailed",
            "WorkflowExecutionSignaled",
            "MarkerRecorded",
            "RecordMarkerFailed",
            "TimerStarted",
            "StartTimerFailed",
            "TimerFired",
            "TimerCanceled",
            "CancelTimerFailed",
            "StartChildWorkflowExecutionInitiated",
            "StartChildWorkflowExecutionFailed",
            "ChildWorkflowExecutionStarted",
            "ChildWorkflowExecutionCompleted",
            "ChildWorkflowExecutionFailed",
            "ChildWorkflowExecutionTimedOut",
            "ChildWorkflowExecutionCanceled",
            "ChildWorkflowExecutionTerminated",
            "SignalExternalWorkflowExecutionInitiated",
            "SignalExternalWorkflowExecutionFailed",
            "ExternalWorkflowExecutionSignaled",
            "RequestCancelExternalWorkflowExecutionInitiated",
            "RequestCancelExternalWorkflowExecutionFailed",
            "ExternalWorkflowExecutionCancelRequested",
            "LambdaFunctionScheduled",
            "LambdaFunctionStarted",
            "LambdaFunctionCompleted",
            "LambdaFunctionFailed",
            "LambdaFunctionTimedOut",
            "ScheduleLambdaFunctionFailed",
            "StartLambdaFunctionFailed",
        ],
        "eventId": int,
    },
)
_OptionalHistoryEventTypeDef = TypedDict(
    "_OptionalHistoryEventTypeDef",
    {
        "workflowExecutionStartedEventAttributes": "WorkflowExecutionStartedEventAttributesTypeDef",
        "workflowExecutionCompletedEventAttributes": "WorkflowExecutionCompletedEventAttributesTypeDef",
        "completeWorkflowExecutionFailedEventAttributes": "CompleteWorkflowExecutionFailedEventAttributesTypeDef",
        "workflowExecutionFailedEventAttributes": "WorkflowExecutionFailedEventAttributesTypeDef",
        "failWorkflowExecutionFailedEventAttributes": "FailWorkflowExecutionFailedEventAttributesTypeDef",
        "workflowExecutionTimedOutEventAttributes": "WorkflowExecutionTimedOutEventAttributesTypeDef",
        "workflowExecutionCanceledEventAttributes": "WorkflowExecutionCanceledEventAttributesTypeDef",
        "cancelWorkflowExecutionFailedEventAttributes": "CancelWorkflowExecutionFailedEventAttributesTypeDef",
        "workflowExecutionContinuedAsNewEventAttributes": "WorkflowExecutionContinuedAsNewEventAttributesTypeDef",
        "continueAsNewWorkflowExecutionFailedEventAttributes": "ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef",
        "workflowExecutionTerminatedEventAttributes": "WorkflowExecutionTerminatedEventAttributesTypeDef",
        "workflowExecutionCancelRequestedEventAttributes": "WorkflowExecutionCancelRequestedEventAttributesTypeDef",
        "decisionTaskScheduledEventAttributes": "DecisionTaskScheduledEventAttributesTypeDef",
        "decisionTaskStartedEventAttributes": "DecisionTaskStartedEventAttributesTypeDef",
        "decisionTaskCompletedEventAttributes": "DecisionTaskCompletedEventAttributesTypeDef",
        "decisionTaskTimedOutEventAttributes": "DecisionTaskTimedOutEventAttributesTypeDef",
        "activityTaskScheduledEventAttributes": "ActivityTaskScheduledEventAttributesTypeDef",
        "activityTaskStartedEventAttributes": "ActivityTaskStartedEventAttributesTypeDef",
        "activityTaskCompletedEventAttributes": "ActivityTaskCompletedEventAttributesTypeDef",
        "activityTaskFailedEventAttributes": "ActivityTaskFailedEventAttributesTypeDef",
        "activityTaskTimedOutEventAttributes": "ActivityTaskTimedOutEventAttributesTypeDef",
        "activityTaskCanceledEventAttributes": "ActivityTaskCanceledEventAttributesTypeDef",
        "activityTaskCancelRequestedEventAttributes": "ActivityTaskCancelRequestedEventAttributesTypeDef",
        "workflowExecutionSignaledEventAttributes": "WorkflowExecutionSignaledEventAttributesTypeDef",
        "markerRecordedEventAttributes": "MarkerRecordedEventAttributesTypeDef",
        "recordMarkerFailedEventAttributes": "RecordMarkerFailedEventAttributesTypeDef",
        "timerStartedEventAttributes": "TimerStartedEventAttributesTypeDef",
        "timerFiredEventAttributes": "TimerFiredEventAttributesTypeDef",
        "timerCanceledEventAttributes": "TimerCanceledEventAttributesTypeDef",
        "startChildWorkflowExecutionInitiatedEventAttributes": "StartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
        "childWorkflowExecutionStartedEventAttributes": "ChildWorkflowExecutionStartedEventAttributesTypeDef",
        "childWorkflowExecutionCompletedEventAttributes": "ChildWorkflowExecutionCompletedEventAttributesTypeDef",
        "childWorkflowExecutionFailedEventAttributes": "ChildWorkflowExecutionFailedEventAttributesTypeDef",
        "childWorkflowExecutionTimedOutEventAttributes": "ChildWorkflowExecutionTimedOutEventAttributesTypeDef",
        "childWorkflowExecutionCanceledEventAttributes": "ChildWorkflowExecutionCanceledEventAttributesTypeDef",
        "childWorkflowExecutionTerminatedEventAttributes": "ChildWorkflowExecutionTerminatedEventAttributesTypeDef",
        "signalExternalWorkflowExecutionInitiatedEventAttributes": "SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
        "externalWorkflowExecutionSignaledEventAttributes": "ExternalWorkflowExecutionSignaledEventAttributesTypeDef",
        "signalExternalWorkflowExecutionFailedEventAttributes": "SignalExternalWorkflowExecutionFailedEventAttributesTypeDef",
        "externalWorkflowExecutionCancelRequestedEventAttributes": "ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef",
        "requestCancelExternalWorkflowExecutionInitiatedEventAttributes": "RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
        "requestCancelExternalWorkflowExecutionFailedEventAttributes": "RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef",
        "scheduleActivityTaskFailedEventAttributes": "ScheduleActivityTaskFailedEventAttributesTypeDef",
        "requestCancelActivityTaskFailedEventAttributes": "RequestCancelActivityTaskFailedEventAttributesTypeDef",
        "startTimerFailedEventAttributes": "StartTimerFailedEventAttributesTypeDef",
        "cancelTimerFailedEventAttributes": "CancelTimerFailedEventAttributesTypeDef",
        "startChildWorkflowExecutionFailedEventAttributes": "StartChildWorkflowExecutionFailedEventAttributesTypeDef",
        "lambdaFunctionScheduledEventAttributes": "LambdaFunctionScheduledEventAttributesTypeDef",
        "lambdaFunctionStartedEventAttributes": "LambdaFunctionStartedEventAttributesTypeDef",
        "lambdaFunctionCompletedEventAttributes": "LambdaFunctionCompletedEventAttributesTypeDef",
        "lambdaFunctionFailedEventAttributes": "LambdaFunctionFailedEventAttributesTypeDef",
        "lambdaFunctionTimedOutEventAttributes": "LambdaFunctionTimedOutEventAttributesTypeDef",
        "scheduleLambdaFunctionFailedEventAttributes": "ScheduleLambdaFunctionFailedEventAttributesTypeDef",
        "startLambdaFunctionFailedEventAttributes": "StartLambdaFunctionFailedEventAttributesTypeDef",
    },
    total=False,
)


class HistoryEventTypeDef(_RequiredHistoryEventTypeDef, _OptionalHistoryEventTypeDef):
    pass


_RequiredLambdaFunctionCompletedEventAttributesTypeDef = TypedDict(
    "_RequiredLambdaFunctionCompletedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int},
)
_OptionalLambdaFunctionCompletedEventAttributesTypeDef = TypedDict(
    "_OptionalLambdaFunctionCompletedEventAttributesTypeDef", {"result": str}, total=False
)


class LambdaFunctionCompletedEventAttributesTypeDef(
    _RequiredLambdaFunctionCompletedEventAttributesTypeDef,
    _OptionalLambdaFunctionCompletedEventAttributesTypeDef,
):
    pass


_RequiredLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "_RequiredLambdaFunctionFailedEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int},
)
_OptionalLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "_OptionalLambdaFunctionFailedEventAttributesTypeDef",
    {"reason": str, "details": str},
    total=False,
)


class LambdaFunctionFailedEventAttributesTypeDef(
    _RequiredLambdaFunctionFailedEventAttributesTypeDef,
    _OptionalLambdaFunctionFailedEventAttributesTypeDef,
):
    pass


_RequiredLambdaFunctionScheduledEventAttributesTypeDef = TypedDict(
    "_RequiredLambdaFunctionScheduledEventAttributesTypeDef",
    {"id": str, "name": str, "decisionTaskCompletedEventId": int},
)
_OptionalLambdaFunctionScheduledEventAttributesTypeDef = TypedDict(
    "_OptionalLambdaFunctionScheduledEventAttributesTypeDef",
    {"control": str, "input": str, "startToCloseTimeout": str},
    total=False,
)


class LambdaFunctionScheduledEventAttributesTypeDef(
    _RequiredLambdaFunctionScheduledEventAttributesTypeDef,
    _OptionalLambdaFunctionScheduledEventAttributesTypeDef,
):
    pass


LambdaFunctionStartedEventAttributesTypeDef = TypedDict(
    "LambdaFunctionStartedEventAttributesTypeDef", {"scheduledEventId": int}
)

_RequiredLambdaFunctionTimedOutEventAttributesTypeDef = TypedDict(
    "_RequiredLambdaFunctionTimedOutEventAttributesTypeDef",
    {"scheduledEventId": int, "startedEventId": int},
)
_OptionalLambdaFunctionTimedOutEventAttributesTypeDef = TypedDict(
    "_OptionalLambdaFunctionTimedOutEventAttributesTypeDef",
    {"timeoutType": Literal["START_TO_CLOSE"]},
    total=False,
)


class LambdaFunctionTimedOutEventAttributesTypeDef(
    _RequiredLambdaFunctionTimedOutEventAttributesTypeDef,
    _OptionalLambdaFunctionTimedOutEventAttributesTypeDef,
):
    pass


_RequiredMarkerRecordedEventAttributesTypeDef = TypedDict(
    "_RequiredMarkerRecordedEventAttributesTypeDef",
    {"markerName": str, "decisionTaskCompletedEventId": int},
)
_OptionalMarkerRecordedEventAttributesTypeDef = TypedDict(
    "_OptionalMarkerRecordedEventAttributesTypeDef", {"details": str}, total=False
)


class MarkerRecordedEventAttributesTypeDef(
    _RequiredMarkerRecordedEventAttributesTypeDef, _OptionalMarkerRecordedEventAttributesTypeDef
):
    pass


_RequiredRecordMarkerDecisionAttributesTypeDef = TypedDict(
    "_RequiredRecordMarkerDecisionAttributesTypeDef", {"markerName": str}
)
_OptionalRecordMarkerDecisionAttributesTypeDef = TypedDict(
    "_OptionalRecordMarkerDecisionAttributesTypeDef", {"details": str}, total=False
)


class RecordMarkerDecisionAttributesTypeDef(
    _RequiredRecordMarkerDecisionAttributesTypeDef, _OptionalRecordMarkerDecisionAttributesTypeDef
):
    pass


RecordMarkerFailedEventAttributesTypeDef = TypedDict(
    "RecordMarkerFailedEventAttributesTypeDef",
    {
        "markerName": str,
        "cause": Literal["OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
)

RequestCancelActivityTaskDecisionAttributesTypeDef = TypedDict(
    "RequestCancelActivityTaskDecisionAttributesTypeDef", {"activityId": str}
)

RequestCancelActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "RequestCancelActivityTaskFailedEventAttributesTypeDef",
    {
        "activityId": str,
        "cause": Literal["ACTIVITY_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
)

_RequiredRequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "_RequiredRequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef", {"workflowId": str}
)
_OptionalRequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "_OptionalRequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef",
    {"runId": str, "control": str},
    total=False,
)


class RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef(
    _RequiredRequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef,
    _OptionalRequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef,
):
    pass


_RequiredRequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_RequiredRequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowId": str,
        "cause": Literal[
            "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
            "REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
    },
)
_OptionalRequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_OptionalRequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {"runId": str, "control": str},
    total=False,
)


class RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef(
    _RequiredRequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef,
    _OptionalRequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef,
):
    pass


_RequiredRequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "_RequiredRequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {"workflowId": str, "decisionTaskCompletedEventId": int},
)
_OptionalRequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "_OptionalRequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {"runId": str, "control": str},
    total=False,
)


class RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef(
    _RequiredRequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
    _OptionalRequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
):
    pass


_RequiredResourceTagTypeDef = TypedDict("_RequiredResourceTagTypeDef", {"key": str})
_OptionalResourceTagTypeDef = TypedDict("_OptionalResourceTagTypeDef", {"value": str}, total=False)


class ResourceTagTypeDef(_RequiredResourceTagTypeDef, _OptionalResourceTagTypeDef):
    pass


_RequiredScheduleActivityTaskDecisionAttributesTypeDef = TypedDict(
    "_RequiredScheduleActivityTaskDecisionAttributesTypeDef",
    {"activityType": "ActivityTypeTypeDef", "activityId": str},
)
_OptionalScheduleActivityTaskDecisionAttributesTypeDef = TypedDict(
    "_OptionalScheduleActivityTaskDecisionAttributesTypeDef",
    {
        "control": str,
        "input": str,
        "scheduleToCloseTimeout": str,
        "taskList": "TaskListTypeDef",
        "taskPriority": str,
        "scheduleToStartTimeout": str,
        "startToCloseTimeout": str,
        "heartbeatTimeout": str,
    },
    total=False,
)


class ScheduleActivityTaskDecisionAttributesTypeDef(
    _RequiredScheduleActivityTaskDecisionAttributesTypeDef,
    _OptionalScheduleActivityTaskDecisionAttributesTypeDef,
):
    pass


ScheduleActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "ScheduleActivityTaskFailedEventAttributesTypeDef",
    {
        "activityType": "ActivityTypeTypeDef",
        "activityId": str,
        "cause": Literal[
            "ACTIVITY_TYPE_DEPRECATED",
            "ACTIVITY_TYPE_DOES_NOT_EXIST",
            "ACTIVITY_ID_ALREADY_IN_USE",
            "OPEN_ACTIVITIES_LIMIT_EXCEEDED",
            "ACTIVITY_CREATION_RATE_EXCEEDED",
            "DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED",
            "DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
)

_RequiredScheduleLambdaFunctionDecisionAttributesTypeDef = TypedDict(
    "_RequiredScheduleLambdaFunctionDecisionAttributesTypeDef", {"id": str, "name": str}
)
_OptionalScheduleLambdaFunctionDecisionAttributesTypeDef = TypedDict(
    "_OptionalScheduleLambdaFunctionDecisionAttributesTypeDef",
    {"control": str, "input": str, "startToCloseTimeout": str},
    total=False,
)


class ScheduleLambdaFunctionDecisionAttributesTypeDef(
    _RequiredScheduleLambdaFunctionDecisionAttributesTypeDef,
    _OptionalScheduleLambdaFunctionDecisionAttributesTypeDef,
):
    pass


ScheduleLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "ScheduleLambdaFunctionFailedEventAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "cause": Literal[
            "ID_ALREADY_IN_USE",
            "OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED",
            "LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED",
            "LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION",
        ],
        "decisionTaskCompletedEventId": int,
    },
)

_RequiredSignalExternalWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "_RequiredSignalExternalWorkflowExecutionDecisionAttributesTypeDef",
    {"workflowId": str, "signalName": str},
)
_OptionalSignalExternalWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "_OptionalSignalExternalWorkflowExecutionDecisionAttributesTypeDef",
    {"runId": str, "input": str, "control": str},
    total=False,
)


class SignalExternalWorkflowExecutionDecisionAttributesTypeDef(
    _RequiredSignalExternalWorkflowExecutionDecisionAttributesTypeDef,
    _OptionalSignalExternalWorkflowExecutionDecisionAttributesTypeDef,
):
    pass


_RequiredSignalExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_RequiredSignalExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowId": str,
        "cause": Literal[
            "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
            "SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
    },
)
_OptionalSignalExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_OptionalSignalExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {"runId": str, "control": str},
    total=False,
)


class SignalExternalWorkflowExecutionFailedEventAttributesTypeDef(
    _RequiredSignalExternalWorkflowExecutionFailedEventAttributesTypeDef,
    _OptionalSignalExternalWorkflowExecutionFailedEventAttributesTypeDef,
):
    pass


_RequiredSignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "_RequiredSignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {"workflowId": str, "signalName": str, "decisionTaskCompletedEventId": int},
)
_OptionalSignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "_OptionalSignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {"runId": str, "input": str, "control": str},
    total=False,
)


class SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef(
    _RequiredSignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
    _OptionalSignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
):
    pass


_RequiredStartChildWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "_RequiredStartChildWorkflowExecutionDecisionAttributesTypeDef",
    {"workflowType": "WorkflowTypeTypeDef", "workflowId": str},
)
_OptionalStartChildWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "_OptionalStartChildWorkflowExecutionDecisionAttributesTypeDef",
    {
        "control": str,
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskList": "TaskListTypeDef",
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "tagList": List[str],
        "lambdaRole": str,
    },
    total=False,
)


class StartChildWorkflowExecutionDecisionAttributesTypeDef(
    _RequiredStartChildWorkflowExecutionDecisionAttributesTypeDef,
    _OptionalStartChildWorkflowExecutionDecisionAttributesTypeDef,
):
    pass


_RequiredStartChildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_RequiredStartChildWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowType": "WorkflowTypeTypeDef",
        "cause": Literal[
            "WORKFLOW_TYPE_DOES_NOT_EXIST",
            "WORKFLOW_TYPE_DEPRECATED",
            "OPEN_CHILDREN_LIMIT_EXCEEDED",
            "OPEN_WORKFLOWS_LIMIT_EXCEEDED",
            "CHILD_CREATION_RATE_EXCEEDED",
            "WORKFLOW_ALREADY_RUNNING",
            "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_TASK_LIST_UNDEFINED",
            "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
            "DEFAULT_CHILD_POLICY_UNDEFINED",
            "OPERATION_NOT_PERMITTED",
        ],
        "workflowId": str,
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
    },
)
_OptionalStartChildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_OptionalStartChildWorkflowExecutionFailedEventAttributesTypeDef",
    {"control": str},
    total=False,
)


class StartChildWorkflowExecutionFailedEventAttributesTypeDef(
    _RequiredStartChildWorkflowExecutionFailedEventAttributesTypeDef,
    _OptionalStartChildWorkflowExecutionFailedEventAttributesTypeDef,
):
    pass


_RequiredStartChildWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "_RequiredStartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "workflowType": "WorkflowTypeTypeDef",
        "taskList": "TaskListTypeDef",
        "decisionTaskCompletedEventId": int,
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
    },
)
_OptionalStartChildWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "_OptionalStartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "control": str,
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "tagList": List[str],
        "lambdaRole": str,
    },
    total=False,
)


class StartChildWorkflowExecutionInitiatedEventAttributesTypeDef(
    _RequiredStartChildWorkflowExecutionInitiatedEventAttributesTypeDef,
    _OptionalStartChildWorkflowExecutionInitiatedEventAttributesTypeDef,
):
    pass


StartLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "StartLambdaFunctionFailedEventAttributesTypeDef",
    {"scheduledEventId": int, "cause": Literal["ASSUME_ROLE_FAILED"], "message": str},
    total=False,
)

_RequiredStartTimerDecisionAttributesTypeDef = TypedDict(
    "_RequiredStartTimerDecisionAttributesTypeDef", {"timerId": str, "startToFireTimeout": str}
)
_OptionalStartTimerDecisionAttributesTypeDef = TypedDict(
    "_OptionalStartTimerDecisionAttributesTypeDef", {"control": str}, total=False
)


class StartTimerDecisionAttributesTypeDef(
    _RequiredStartTimerDecisionAttributesTypeDef, _OptionalStartTimerDecisionAttributesTypeDef
):
    pass


StartTimerFailedEventAttributesTypeDef = TypedDict(
    "StartTimerFailedEventAttributesTypeDef",
    {
        "timerId": str,
        "cause": Literal[
            "TIMER_ID_ALREADY_IN_USE",
            "OPEN_TIMERS_LIMIT_EXCEEDED",
            "TIMER_CREATION_RATE_EXCEEDED",
            "OPERATION_NOT_PERMITTED",
        ],
        "decisionTaskCompletedEventId": int,
    },
)

TaskListTypeDef = TypedDict("TaskListTypeDef", {"name": str})

TimerCanceledEventAttributesTypeDef = TypedDict(
    "TimerCanceledEventAttributesTypeDef",
    {"timerId": str, "startedEventId": int, "decisionTaskCompletedEventId": int},
)

TimerFiredEventAttributesTypeDef = TypedDict(
    "TimerFiredEventAttributesTypeDef", {"timerId": str, "startedEventId": int}
)

_RequiredTimerStartedEventAttributesTypeDef = TypedDict(
    "_RequiredTimerStartedEventAttributesTypeDef",
    {"timerId": str, "startToFireTimeout": str, "decisionTaskCompletedEventId": int},
)
_OptionalTimerStartedEventAttributesTypeDef = TypedDict(
    "_OptionalTimerStartedEventAttributesTypeDef", {"control": str}, total=False
)


class TimerStartedEventAttributesTypeDef(
    _RequiredTimerStartedEventAttributesTypeDef, _OptionalTimerStartedEventAttributesTypeDef
):
    pass


WorkflowExecutionCancelRequestedEventAttributesTypeDef = TypedDict(
    "WorkflowExecutionCancelRequestedEventAttributesTypeDef",
    {
        "externalWorkflowExecution": "WorkflowExecutionTypeDef",
        "externalInitiatedEventId": int,
        "cause": Literal["CHILD_POLICY_APPLIED"],
    },
    total=False,
)

_RequiredWorkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "_RequiredWorkflowExecutionCanceledEventAttributesTypeDef",
    {"decisionTaskCompletedEventId": int},
)
_OptionalWorkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "_OptionalWorkflowExecutionCanceledEventAttributesTypeDef", {"details": str}, total=False
)


class WorkflowExecutionCanceledEventAttributesTypeDef(
    _RequiredWorkflowExecutionCanceledEventAttributesTypeDef,
    _OptionalWorkflowExecutionCanceledEventAttributesTypeDef,
):
    pass


_RequiredWorkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "_RequiredWorkflowExecutionCompletedEventAttributesTypeDef",
    {"decisionTaskCompletedEventId": int},
)
_OptionalWorkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "_OptionalWorkflowExecutionCompletedEventAttributesTypeDef", {"result": str}, total=False
)


class WorkflowExecutionCompletedEventAttributesTypeDef(
    _RequiredWorkflowExecutionCompletedEventAttributesTypeDef,
    _OptionalWorkflowExecutionCompletedEventAttributesTypeDef,
):
    pass


_RequiredWorkflowExecutionConfigurationTypeDef = TypedDict(
    "_RequiredWorkflowExecutionConfigurationTypeDef",
    {
        "taskStartToCloseTimeout": str,
        "executionStartToCloseTimeout": str,
        "taskList": "TaskListTypeDef",
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
    },
)
_OptionalWorkflowExecutionConfigurationTypeDef = TypedDict(
    "_OptionalWorkflowExecutionConfigurationTypeDef",
    {"taskPriority": str, "lambdaRole": str},
    total=False,
)


class WorkflowExecutionConfigurationTypeDef(
    _RequiredWorkflowExecutionConfigurationTypeDef, _OptionalWorkflowExecutionConfigurationTypeDef
):
    pass


_RequiredWorkflowExecutionContinuedAsNewEventAttributesTypeDef = TypedDict(
    "_RequiredWorkflowExecutionContinuedAsNewEventAttributesTypeDef",
    {
        "decisionTaskCompletedEventId": int,
        "newExecutionRunId": str,
        "taskList": "TaskListTypeDef",
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "workflowType": "WorkflowTypeTypeDef",
    },
)
_OptionalWorkflowExecutionContinuedAsNewEventAttributesTypeDef = TypedDict(
    "_OptionalWorkflowExecutionContinuedAsNewEventAttributesTypeDef",
    {
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "tagList": List[str],
        "lambdaRole": str,
    },
    total=False,
)


class WorkflowExecutionContinuedAsNewEventAttributesTypeDef(
    _RequiredWorkflowExecutionContinuedAsNewEventAttributesTypeDef,
    _OptionalWorkflowExecutionContinuedAsNewEventAttributesTypeDef,
):
    pass


_RequiredWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_RequiredWorkflowExecutionFailedEventAttributesTypeDef", {"decisionTaskCompletedEventId": int}
)
_OptionalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "_OptionalWorkflowExecutionFailedEventAttributesTypeDef",
    {"reason": str, "details": str},
    total=False,
)


class WorkflowExecutionFailedEventAttributesTypeDef(
    _RequiredWorkflowExecutionFailedEventAttributesTypeDef,
    _OptionalWorkflowExecutionFailedEventAttributesTypeDef,
):
    pass


_RequiredWorkflowExecutionInfoTypeDef = TypedDict(
    "_RequiredWorkflowExecutionInfoTypeDef",
    {
        "execution": "WorkflowExecutionTypeDef",
        "workflowType": "WorkflowTypeTypeDef",
        "startTimestamp": datetime,
        "executionStatus": Literal["OPEN", "CLOSED"],
    },
)
_OptionalWorkflowExecutionInfoTypeDef = TypedDict(
    "_OptionalWorkflowExecutionInfoTypeDef",
    {
        "closeTimestamp": datetime,
        "closeStatus": Literal[
            "COMPLETED", "FAILED", "CANCELED", "TERMINATED", "CONTINUED_AS_NEW", "TIMED_OUT"
        ],
        "parent": "WorkflowExecutionTypeDef",
        "tagList": List[str],
        "cancelRequested": bool,
    },
    total=False,
)


class WorkflowExecutionInfoTypeDef(
    _RequiredWorkflowExecutionInfoTypeDef, _OptionalWorkflowExecutionInfoTypeDef
):
    pass


_RequiredWorkflowExecutionOpenCountsTypeDef = TypedDict(
    "_RequiredWorkflowExecutionOpenCountsTypeDef",
    {
        "openActivityTasks": int,
        "openDecisionTasks": int,
        "openTimers": int,
        "openChildWorkflowExecutions": int,
    },
)
_OptionalWorkflowExecutionOpenCountsTypeDef = TypedDict(
    "_OptionalWorkflowExecutionOpenCountsTypeDef", {"openLambdaFunctions": int}, total=False
)


class WorkflowExecutionOpenCountsTypeDef(
    _RequiredWorkflowExecutionOpenCountsTypeDef, _OptionalWorkflowExecutionOpenCountsTypeDef
):
    pass


_RequiredWorkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "_RequiredWorkflowExecutionSignaledEventAttributesTypeDef", {"signalName": str}
)
_OptionalWorkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "_OptionalWorkflowExecutionSignaledEventAttributesTypeDef",
    {
        "input": str,
        "externalWorkflowExecution": "WorkflowExecutionTypeDef",
        "externalInitiatedEventId": int,
    },
    total=False,
)


class WorkflowExecutionSignaledEventAttributesTypeDef(
    _RequiredWorkflowExecutionSignaledEventAttributesTypeDef,
    _OptionalWorkflowExecutionSignaledEventAttributesTypeDef,
):
    pass


_RequiredWorkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "_RequiredWorkflowExecutionStartedEventAttributesTypeDef",
    {
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "taskList": "TaskListTypeDef",
        "workflowType": "WorkflowTypeTypeDef",
    },
)
_OptionalWorkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "_OptionalWorkflowExecutionStartedEventAttributesTypeDef",
    {
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskStartToCloseTimeout": str,
        "taskPriority": str,
        "tagList": List[str],
        "continuedExecutionRunId": str,
        "parentWorkflowExecution": "WorkflowExecutionTypeDef",
        "parentInitiatedEventId": int,
        "lambdaRole": str,
    },
    total=False,
)


class WorkflowExecutionStartedEventAttributesTypeDef(
    _RequiredWorkflowExecutionStartedEventAttributesTypeDef,
    _OptionalWorkflowExecutionStartedEventAttributesTypeDef,
):
    pass


_RequiredWorkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "_RequiredWorkflowExecutionTerminatedEventAttributesTypeDef",
    {"childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"]},
)
_OptionalWorkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "_OptionalWorkflowExecutionTerminatedEventAttributesTypeDef",
    {
        "reason": str,
        "details": str,
        "cause": Literal["CHILD_POLICY_APPLIED", "EVENT_LIMIT_EXCEEDED", "OPERATOR_INITIATED"],
    },
    total=False,
)


class WorkflowExecutionTerminatedEventAttributesTypeDef(
    _RequiredWorkflowExecutionTerminatedEventAttributesTypeDef,
    _OptionalWorkflowExecutionTerminatedEventAttributesTypeDef,
):
    pass


WorkflowExecutionTimedOutEventAttributesTypeDef = TypedDict(
    "WorkflowExecutionTimedOutEventAttributesTypeDef",
    {
        "timeoutType": Literal["START_TO_CLOSE"],
        "childPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
    },
)

WorkflowExecutionTypeDef = TypedDict("WorkflowExecutionTypeDef", {"workflowId": str, "runId": str})

WorkflowTypeConfigurationTypeDef = TypedDict(
    "WorkflowTypeConfigurationTypeDef",
    {
        "defaultTaskStartToCloseTimeout": str,
        "defaultExecutionStartToCloseTimeout": str,
        "defaultTaskList": "TaskListTypeDef",
        "defaultTaskPriority": str,
        "defaultChildPolicy": Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"],
        "defaultLambdaRole": str,
    },
    total=False,
)

_RequiredWorkflowTypeInfoTypeDef = TypedDict(
    "_RequiredWorkflowTypeInfoTypeDef",
    {
        "workflowType": "WorkflowTypeTypeDef",
        "status": Literal["REGISTERED", "DEPRECATED"],
        "creationDate": datetime,
    },
)
_OptionalWorkflowTypeInfoTypeDef = TypedDict(
    "_OptionalWorkflowTypeInfoTypeDef",
    {"description": str, "deprecationDate": datetime},
    total=False,
)


class WorkflowTypeInfoTypeDef(_RequiredWorkflowTypeInfoTypeDef, _OptionalWorkflowTypeInfoTypeDef):
    pass


WorkflowTypeTypeDef = TypedDict("WorkflowTypeTypeDef", {"name": str, "version": str})

ActivityTaskStatusTypeDef = TypedDict("ActivityTaskStatusTypeDef", {"cancelRequested": bool})

_RequiredActivityTaskTypeDef = TypedDict(
    "_RequiredActivityTaskTypeDef",
    {
        "taskToken": str,
        "activityId": str,
        "startedEventId": int,
        "workflowExecution": "WorkflowExecutionTypeDef",
        "activityType": "ActivityTypeTypeDef",
    },
)
_OptionalActivityTaskTypeDef = TypedDict(
    "_OptionalActivityTaskTypeDef", {"input": str}, total=False
)


class ActivityTaskTypeDef(_RequiredActivityTaskTypeDef, _OptionalActivityTaskTypeDef):
    pass


ActivityTypeDetailTypeDef = TypedDict(
    "ActivityTypeDetailTypeDef",
    {"typeInfo": "ActivityTypeInfoTypeDef", "configuration": "ActivityTypeConfigurationTypeDef"},
)

_RequiredActivityTypeInfosTypeDef = TypedDict(
    "_RequiredActivityTypeInfosTypeDef", {"typeInfos": List["ActivityTypeInfoTypeDef"]}
)
_OptionalActivityTypeInfosTypeDef = TypedDict(
    "_OptionalActivityTypeInfosTypeDef", {"nextPageToken": str}, total=False
)


class ActivityTypeInfosTypeDef(
    _RequiredActivityTypeInfosTypeDef, _OptionalActivityTypeInfosTypeDef
):
    pass


CloseStatusFilterTypeDef = TypedDict(
    "CloseStatusFilterTypeDef",
    {
        "status": Literal[
            "COMPLETED", "FAILED", "CANCELED", "TERMINATED", "CONTINUED_AS_NEW", "TIMED_OUT"
        ]
    },
)

_RequiredDecisionTaskTypeDef = TypedDict(
    "_RequiredDecisionTaskTypeDef",
    {
        "taskToken": str,
        "startedEventId": int,
        "workflowExecution": "WorkflowExecutionTypeDef",
        "workflowType": "WorkflowTypeTypeDef",
        "events": List["HistoryEventTypeDef"],
    },
)
_OptionalDecisionTaskTypeDef = TypedDict(
    "_OptionalDecisionTaskTypeDef",
    {"nextPageToken": str, "previousStartedEventId": int},
    total=False,
)


class DecisionTaskTypeDef(_RequiredDecisionTaskTypeDef, _OptionalDecisionTaskTypeDef):
    pass


_RequiredDecisionTypeDef = TypedDict(
    "_RequiredDecisionTypeDef",
    {
        "decisionType": Literal[
            "ScheduleActivityTask",
            "RequestCancelActivityTask",
            "CompleteWorkflowExecution",
            "FailWorkflowExecution",
            "CancelWorkflowExecution",
            "ContinueAsNewWorkflowExecution",
            "RecordMarker",
            "StartTimer",
            "CancelTimer",
            "SignalExternalWorkflowExecution",
            "RequestCancelExternalWorkflowExecution",
            "StartChildWorkflowExecution",
            "ScheduleLambdaFunction",
        ]
    },
)
_OptionalDecisionTypeDef = TypedDict(
    "_OptionalDecisionTypeDef",
    {
        "scheduleActivityTaskDecisionAttributes": "ScheduleActivityTaskDecisionAttributesTypeDef",
        "requestCancelActivityTaskDecisionAttributes": "RequestCancelActivityTaskDecisionAttributesTypeDef",
        "completeWorkflowExecutionDecisionAttributes": "CompleteWorkflowExecutionDecisionAttributesTypeDef",
        "failWorkflowExecutionDecisionAttributes": "FailWorkflowExecutionDecisionAttributesTypeDef",
        "cancelWorkflowExecutionDecisionAttributes": "CancelWorkflowExecutionDecisionAttributesTypeDef",
        "continueAsNewWorkflowExecutionDecisionAttributes": "ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef",
        "recordMarkerDecisionAttributes": "RecordMarkerDecisionAttributesTypeDef",
        "startTimerDecisionAttributes": "StartTimerDecisionAttributesTypeDef",
        "cancelTimerDecisionAttributes": "CancelTimerDecisionAttributesTypeDef",
        "signalExternalWorkflowExecutionDecisionAttributes": "SignalExternalWorkflowExecutionDecisionAttributesTypeDef",
        "requestCancelExternalWorkflowExecutionDecisionAttributes": "RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef",
        "startChildWorkflowExecutionDecisionAttributes": "StartChildWorkflowExecutionDecisionAttributesTypeDef",
        "scheduleLambdaFunctionDecisionAttributes": "ScheduleLambdaFunctionDecisionAttributesTypeDef",
    },
    total=False,
)


class DecisionTypeDef(_RequiredDecisionTypeDef, _OptionalDecisionTypeDef):
    pass


DomainDetailTypeDef = TypedDict(
    "DomainDetailTypeDef",
    {"domainInfo": "DomainInfoTypeDef", "configuration": "DomainConfigurationTypeDef"},
)

_RequiredDomainInfosTypeDef = TypedDict(
    "_RequiredDomainInfosTypeDef", {"domainInfos": List["DomainInfoTypeDef"]}
)
_OptionalDomainInfosTypeDef = TypedDict(
    "_OptionalDomainInfosTypeDef", {"nextPageToken": str}, total=False
)


class DomainInfosTypeDef(_RequiredDomainInfosTypeDef, _OptionalDomainInfosTypeDef):
    pass


_RequiredExecutionTimeFilterTypeDef = TypedDict(
    "_RequiredExecutionTimeFilterTypeDef", {"oldestDate": datetime}
)
_OptionalExecutionTimeFilterTypeDef = TypedDict(
    "_OptionalExecutionTimeFilterTypeDef", {"latestDate": datetime}, total=False
)


class ExecutionTimeFilterTypeDef(
    _RequiredExecutionTimeFilterTypeDef, _OptionalExecutionTimeFilterTypeDef
):
    pass


_RequiredHistoryTypeDef = TypedDict(
    "_RequiredHistoryTypeDef", {"events": List["HistoryEventTypeDef"]}
)
_OptionalHistoryTypeDef = TypedDict("_OptionalHistoryTypeDef", {"nextPageToken": str}, total=False)


class HistoryTypeDef(_RequiredHistoryTypeDef, _OptionalHistoryTypeDef):
    pass


ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef", {"tags": List["ResourceTagTypeDef"]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

_RequiredPendingTaskCountTypeDef = TypedDict("_RequiredPendingTaskCountTypeDef", {"count": int})
_OptionalPendingTaskCountTypeDef = TypedDict(
    "_OptionalPendingTaskCountTypeDef", {"truncated": bool}, total=False
)


class PendingTaskCountTypeDef(_RequiredPendingTaskCountTypeDef, _OptionalPendingTaskCountTypeDef):
    pass


RunTypeDef = TypedDict("RunTypeDef", {"runId": str}, total=False)

TagFilterTypeDef = TypedDict("TagFilterTypeDef", {"tag": str})

_RequiredWorkflowExecutionCountTypeDef = TypedDict(
    "_RequiredWorkflowExecutionCountTypeDef", {"count": int}
)
_OptionalWorkflowExecutionCountTypeDef = TypedDict(
    "_OptionalWorkflowExecutionCountTypeDef", {"truncated": bool}, total=False
)


class WorkflowExecutionCountTypeDef(
    _RequiredWorkflowExecutionCountTypeDef, _OptionalWorkflowExecutionCountTypeDef
):
    pass


_RequiredWorkflowExecutionDetailTypeDef = TypedDict(
    "_RequiredWorkflowExecutionDetailTypeDef",
    {
        "executionInfo": "WorkflowExecutionInfoTypeDef",
        "executionConfiguration": "WorkflowExecutionConfigurationTypeDef",
        "openCounts": "WorkflowExecutionOpenCountsTypeDef",
    },
)
_OptionalWorkflowExecutionDetailTypeDef = TypedDict(
    "_OptionalWorkflowExecutionDetailTypeDef",
    {"latestActivityTaskTimestamp": datetime, "latestExecutionContext": str},
    total=False,
)


class WorkflowExecutionDetailTypeDef(
    _RequiredWorkflowExecutionDetailTypeDef, _OptionalWorkflowExecutionDetailTypeDef
):
    pass


WorkflowExecutionFilterTypeDef = TypedDict("WorkflowExecutionFilterTypeDef", {"workflowId": str})

_RequiredWorkflowExecutionInfosTypeDef = TypedDict(
    "_RequiredWorkflowExecutionInfosTypeDef",
    {"executionInfos": List["WorkflowExecutionInfoTypeDef"]},
)
_OptionalWorkflowExecutionInfosTypeDef = TypedDict(
    "_OptionalWorkflowExecutionInfosTypeDef", {"nextPageToken": str}, total=False
)


class WorkflowExecutionInfosTypeDef(
    _RequiredWorkflowExecutionInfosTypeDef, _OptionalWorkflowExecutionInfosTypeDef
):
    pass


WorkflowTypeDetailTypeDef = TypedDict(
    "WorkflowTypeDetailTypeDef",
    {"typeInfo": "WorkflowTypeInfoTypeDef", "configuration": "WorkflowTypeConfigurationTypeDef"},
)

_RequiredWorkflowTypeFilterTypeDef = TypedDict("_RequiredWorkflowTypeFilterTypeDef", {"name": str})
_OptionalWorkflowTypeFilterTypeDef = TypedDict(
    "_OptionalWorkflowTypeFilterTypeDef", {"version": str}, total=False
)


class WorkflowTypeFilterTypeDef(
    _RequiredWorkflowTypeFilterTypeDef, _OptionalWorkflowTypeFilterTypeDef
):
    pass


_RequiredWorkflowTypeInfosTypeDef = TypedDict(
    "_RequiredWorkflowTypeInfosTypeDef", {"typeInfos": List["WorkflowTypeInfoTypeDef"]}
)
_OptionalWorkflowTypeInfosTypeDef = TypedDict(
    "_OptionalWorkflowTypeInfosTypeDef", {"nextPageToken": str}, total=False
)


class WorkflowTypeInfosTypeDef(
    _RequiredWorkflowTypeInfosTypeDef, _OptionalWorkflowTypeInfosTypeDef
):
    pass
