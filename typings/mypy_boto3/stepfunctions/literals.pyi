"""
Type annotations for stepfunctions service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/literals.html)

Usage::

    ```python
    from mypy_boto3_stepfunctions.literals import ExecutionRedriveFilterType

    data: ExecutionRedriveFilterType = "NOT_REDRIVEN"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ExecutionRedriveFilterType",
    "ExecutionRedriveStatusType",
    "ExecutionStatusType",
    "GetExecutionHistoryPaginatorName",
    "HistoryEventTypeType",
    "InspectionLevelType",
    "ListActivitiesPaginatorName",
    "ListExecutionsPaginatorName",
    "ListMapRunsPaginatorName",
    "ListStateMachinesPaginatorName",
    "LogLevelType",
    "MapRunStatusType",
    "StateMachineStatusType",
    "StateMachineTypeType",
    "SyncExecutionStatusType",
    "TestExecutionStatusType",
)

ExecutionRedriveFilterType = Literal["NOT_REDRIVEN", "REDRIVEN"]
ExecutionRedriveStatusType = Literal["NOT_REDRIVABLE", "REDRIVABLE", "REDRIVABLE_BY_MAP_RUN"]
ExecutionStatusType = Literal[
    "ABORTED", "FAILED", "PENDING_REDRIVE", "RUNNING", "SUCCEEDED", "TIMED_OUT"
]
GetExecutionHistoryPaginatorName = Literal["get_execution_history"]
HistoryEventTypeType = Literal[
    "ActivityFailed",
    "ActivityScheduleFailed",
    "ActivityScheduled",
    "ActivityStarted",
    "ActivitySucceeded",
    "ActivityTimedOut",
    "ChoiceStateEntered",
    "ChoiceStateExited",
    "ExecutionAborted",
    "ExecutionFailed",
    "ExecutionRedriven",
    "ExecutionStarted",
    "ExecutionSucceeded",
    "ExecutionTimedOut",
    "FailStateEntered",
    "LambdaFunctionFailed",
    "LambdaFunctionScheduleFailed",
    "LambdaFunctionScheduled",
    "LambdaFunctionStartFailed",
    "LambdaFunctionStarted",
    "LambdaFunctionSucceeded",
    "LambdaFunctionTimedOut",
    "MapIterationAborted",
    "MapIterationFailed",
    "MapIterationStarted",
    "MapIterationSucceeded",
    "MapRunAborted",
    "MapRunFailed",
    "MapRunRedriven",
    "MapRunStarted",
    "MapRunSucceeded",
    "MapStateAborted",
    "MapStateEntered",
    "MapStateExited",
    "MapStateFailed",
    "MapStateStarted",
    "MapStateSucceeded",
    "ParallelStateAborted",
    "ParallelStateEntered",
    "ParallelStateExited",
    "ParallelStateFailed",
    "ParallelStateStarted",
    "ParallelStateSucceeded",
    "PassStateEntered",
    "PassStateExited",
    "SucceedStateEntered",
    "SucceedStateExited",
    "TaskFailed",
    "TaskScheduled",
    "TaskStartFailed",
    "TaskStarted",
    "TaskStateAborted",
    "TaskStateEntered",
    "TaskStateExited",
    "TaskSubmitFailed",
    "TaskSubmitted",
    "TaskSucceeded",
    "TaskTimedOut",
    "WaitStateAborted",
    "WaitStateEntered",
    "WaitStateExited",
]
InspectionLevelType = Literal["DEBUG", "INFO", "TRACE"]
ListActivitiesPaginatorName = Literal["list_activities"]
ListExecutionsPaginatorName = Literal["list_executions"]
ListMapRunsPaginatorName = Literal["list_map_runs"]
ListStateMachinesPaginatorName = Literal["list_state_machines"]
LogLevelType = Literal["ALL", "ERROR", "FATAL", "OFF"]
MapRunStatusType = Literal["ABORTED", "FAILED", "RUNNING", "SUCCEEDED"]
StateMachineStatusType = Literal["ACTIVE", "DELETING"]
StateMachineTypeType = Literal["EXPRESS", "STANDARD"]
SyncExecutionStatusType = Literal["FAILED", "SUCCEEDED", "TIMED_OUT"]
TestExecutionStatusType = Literal["CAUGHT_ERROR", "FAILED", "RETRIABLE", "SUCCEEDED"]
