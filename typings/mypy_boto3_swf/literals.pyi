"""
Type annotations for swf service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/literals.html)

Usage::

    ```python
    from mypy_boto3_swf.literals import ActivityTaskTimeoutTypeType

    data: ActivityTaskTimeoutTypeType = "HEARTBEAT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActivityTaskTimeoutTypeType",
    "CancelTimerFailedCauseType",
    "CancelWorkflowExecutionFailedCauseType",
    "ChildPolicyType",
    "CloseStatusType",
    "CompleteWorkflowExecutionFailedCauseType",
    "ContinueAsNewWorkflowExecutionFailedCauseType",
    "DecisionTaskTimeoutTypeType",
    "DecisionTypeType",
    "EventTypeType",
    "ExecutionStatusType",
    "FailWorkflowExecutionFailedCauseType",
    "GetWorkflowExecutionHistoryPaginatorName",
    "LambdaFunctionTimeoutTypeType",
    "ListActivityTypesPaginatorName",
    "ListClosedWorkflowExecutionsPaginatorName",
    "ListDomainsPaginatorName",
    "ListOpenWorkflowExecutionsPaginatorName",
    "ListWorkflowTypesPaginatorName",
    "PollForDecisionTaskPaginatorName",
    "RecordMarkerFailedCauseType",
    "RegistrationStatusType",
    "RequestCancelActivityTaskFailedCauseType",
    "RequestCancelExternalWorkflowExecutionFailedCauseType",
    "ScheduleActivityTaskFailedCauseType",
    "ScheduleLambdaFunctionFailedCauseType",
    "SignalExternalWorkflowExecutionFailedCauseType",
    "StartChildWorkflowExecutionFailedCauseType",
    "StartLambdaFunctionFailedCauseType",
    "StartTimerFailedCauseType",
    "WorkflowExecutionCancelRequestedCauseType",
    "WorkflowExecutionTerminatedCauseType",
    "WorkflowExecutionTimeoutTypeType",
)

ActivityTaskTimeoutTypeType = Literal[
    "HEARTBEAT", "SCHEDULE_TO_CLOSE", "SCHEDULE_TO_START", "START_TO_CLOSE"
]
CancelTimerFailedCauseType = Literal["OPERATION_NOT_PERMITTED", "TIMER_ID_UNKNOWN"]
CancelWorkflowExecutionFailedCauseType = Literal["OPERATION_NOT_PERMITTED", "UNHANDLED_DECISION"]
ChildPolicyType = Literal["ABANDON", "REQUEST_CANCEL", "TERMINATE"]
CloseStatusType = Literal[
    "CANCELED", "COMPLETED", "CONTINUED_AS_NEW", "FAILED", "TERMINATED", "TIMED_OUT"
]
CompleteWorkflowExecutionFailedCauseType = Literal["OPERATION_NOT_PERMITTED", "UNHANDLED_DECISION"]
ContinueAsNewWorkflowExecutionFailedCauseType = Literal[
    "CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED",
    "DEFAULT_CHILD_POLICY_UNDEFINED",
    "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "DEFAULT_TASK_LIST_UNDEFINED",
    "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "OPERATION_NOT_PERMITTED",
    "UNHANDLED_DECISION",
    "WORKFLOW_TYPE_DEPRECATED",
    "WORKFLOW_TYPE_DOES_NOT_EXIST",
]
DecisionTaskTimeoutTypeType = Literal["START_TO_CLOSE"]
DecisionTypeType = Literal[
    "CancelTimer",
    "CancelWorkflowExecution",
    "CompleteWorkflowExecution",
    "ContinueAsNewWorkflowExecution",
    "FailWorkflowExecution",
    "RecordMarker",
    "RequestCancelActivityTask",
    "RequestCancelExternalWorkflowExecution",
    "ScheduleActivityTask",
    "ScheduleLambdaFunction",
    "SignalExternalWorkflowExecution",
    "StartChildWorkflowExecution",
    "StartTimer",
]
EventTypeType = Literal[
    "ActivityTaskCancelRequested",
    "ActivityTaskCanceled",
    "ActivityTaskCompleted",
    "ActivityTaskFailed",
    "ActivityTaskScheduled",
    "ActivityTaskStarted",
    "ActivityTaskTimedOut",
    "CancelTimerFailed",
    "CancelWorkflowExecutionFailed",
    "ChildWorkflowExecutionCanceled",
    "ChildWorkflowExecutionCompleted",
    "ChildWorkflowExecutionFailed",
    "ChildWorkflowExecutionStarted",
    "ChildWorkflowExecutionTerminated",
    "ChildWorkflowExecutionTimedOut",
    "CompleteWorkflowExecutionFailed",
    "ContinueAsNewWorkflowExecutionFailed",
    "DecisionTaskCompleted",
    "DecisionTaskScheduled",
    "DecisionTaskStarted",
    "DecisionTaskTimedOut",
    "ExternalWorkflowExecutionCancelRequested",
    "ExternalWorkflowExecutionSignaled",
    "FailWorkflowExecutionFailed",
    "LambdaFunctionCompleted",
    "LambdaFunctionFailed",
    "LambdaFunctionScheduled",
    "LambdaFunctionStarted",
    "LambdaFunctionTimedOut",
    "MarkerRecorded",
    "RecordMarkerFailed",
    "RequestCancelActivityTaskFailed",
    "RequestCancelExternalWorkflowExecutionFailed",
    "RequestCancelExternalWorkflowExecutionInitiated",
    "ScheduleActivityTaskFailed",
    "ScheduleLambdaFunctionFailed",
    "SignalExternalWorkflowExecutionFailed",
    "SignalExternalWorkflowExecutionInitiated",
    "StartChildWorkflowExecutionFailed",
    "StartChildWorkflowExecutionInitiated",
    "StartLambdaFunctionFailed",
    "StartTimerFailed",
    "TimerCanceled",
    "TimerFired",
    "TimerStarted",
    "WorkflowExecutionCancelRequested",
    "WorkflowExecutionCanceled",
    "WorkflowExecutionCompleted",
    "WorkflowExecutionContinuedAsNew",
    "WorkflowExecutionFailed",
    "WorkflowExecutionSignaled",
    "WorkflowExecutionStarted",
    "WorkflowExecutionTerminated",
    "WorkflowExecutionTimedOut",
]
ExecutionStatusType = Literal["CLOSED", "OPEN"]
FailWorkflowExecutionFailedCauseType = Literal["OPERATION_NOT_PERMITTED", "UNHANDLED_DECISION"]
GetWorkflowExecutionHistoryPaginatorName = Literal["get_workflow_execution_history"]
LambdaFunctionTimeoutTypeType = Literal["START_TO_CLOSE"]
ListActivityTypesPaginatorName = Literal["list_activity_types"]
ListClosedWorkflowExecutionsPaginatorName = Literal["list_closed_workflow_executions"]
ListDomainsPaginatorName = Literal["list_domains"]
ListOpenWorkflowExecutionsPaginatorName = Literal["list_open_workflow_executions"]
ListWorkflowTypesPaginatorName = Literal["list_workflow_types"]
PollForDecisionTaskPaginatorName = Literal["poll_for_decision_task"]
RecordMarkerFailedCauseType = Literal["OPERATION_NOT_PERMITTED"]
RegistrationStatusType = Literal["DEPRECATED", "REGISTERED"]
RequestCancelActivityTaskFailedCauseType = Literal["ACTIVITY_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"]
RequestCancelExternalWorkflowExecutionFailedCauseType = Literal[
    "OPERATION_NOT_PERMITTED",
    "REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
    "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
]
ScheduleActivityTaskFailedCauseType = Literal[
    "ACTIVITY_CREATION_RATE_EXCEEDED",
    "ACTIVITY_ID_ALREADY_IN_USE",
    "ACTIVITY_TYPE_DEPRECATED",
    "ACTIVITY_TYPE_DOES_NOT_EXIST",
    "DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED",
    "DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED",
    "DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED",
    "DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "DEFAULT_TASK_LIST_UNDEFINED",
    "OPEN_ACTIVITIES_LIMIT_EXCEEDED",
    "OPERATION_NOT_PERMITTED",
]
ScheduleLambdaFunctionFailedCauseType = Literal[
    "ID_ALREADY_IN_USE",
    "LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED",
    "LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION",
    "OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED",
]
SignalExternalWorkflowExecutionFailedCauseType = Literal[
    "OPERATION_NOT_PERMITTED",
    "SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
    "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
]
StartChildWorkflowExecutionFailedCauseType = Literal[
    "CHILD_CREATION_RATE_EXCEEDED",
    "DEFAULT_CHILD_POLICY_UNDEFINED",
    "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "DEFAULT_TASK_LIST_UNDEFINED",
    "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "OPEN_CHILDREN_LIMIT_EXCEEDED",
    "OPEN_WORKFLOWS_LIMIT_EXCEEDED",
    "OPERATION_NOT_PERMITTED",
    "WORKFLOW_ALREADY_RUNNING",
    "WORKFLOW_TYPE_DEPRECATED",
    "WORKFLOW_TYPE_DOES_NOT_EXIST",
]
StartLambdaFunctionFailedCauseType = Literal["ASSUME_ROLE_FAILED"]
StartTimerFailedCauseType = Literal[
    "OPEN_TIMERS_LIMIT_EXCEEDED",
    "OPERATION_NOT_PERMITTED",
    "TIMER_CREATION_RATE_EXCEEDED",
    "TIMER_ID_ALREADY_IN_USE",
]
WorkflowExecutionCancelRequestedCauseType = Literal["CHILD_POLICY_APPLIED"]
WorkflowExecutionTerminatedCauseType = Literal[
    "CHILD_POLICY_APPLIED", "EVENT_LIMIT_EXCEEDED", "OPERATOR_INITIATED"
]
WorkflowExecutionTimeoutTypeType = Literal["START_TO_CLOSE"]
