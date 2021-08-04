"""
Type annotations for stepfunctions service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/literals.html)

Usage::

    ```python
    from mypy_boto3_stepfunctions.literals import ExecutionStatusType

    data: ExecutionStatusType = "ABORTED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ExecutionStatusType",
    "GetExecutionHistoryPaginatorName",
    "HistoryEventTypeType",
    "ListActivitiesPaginatorName",
    "ListExecutionsPaginatorName",
    "ListStateMachinesPaginatorName",
    "LogLevelType",
    "StateMachineStatusType",
    "StateMachineTypeType",
    "SyncExecutionStatusType",
)

ExecutionStatusType = Literal["ABORTED", "FAILED", "RUNNING", "SUCCEEDED", "TIMED_OUT"]
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
ListActivitiesPaginatorName = Literal["list_activities"]
ListExecutionsPaginatorName = Literal["list_executions"]
ListStateMachinesPaginatorName = Literal["list_state_machines"]
LogLevelType = Literal["ALL", "ERROR", "FATAL", "OFF"]
StateMachineStatusType = Literal["ACTIVE", "DELETING"]
StateMachineTypeType = Literal["EXPRESS", "STANDARD"]
SyncExecutionStatusType = Literal["FAILED", "SUCCEEDED", "TIMED_OUT"]
