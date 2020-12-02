"""
Main interface for stepfunctions service type definitions.

Usage::

    ```python
    from mypy_boto3_stepfunctions.type_defs import ActivityFailedEventDetailsTypeDef

    data: ActivityFailedEventDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActivityFailedEventDetailsTypeDef",
    "ActivityListItemTypeDef",
    "ActivityScheduleFailedEventDetailsTypeDef",
    "ActivityScheduledEventDetailsTypeDef",
    "ActivityStartedEventDetailsTypeDef",
    "ActivitySucceededEventDetailsTypeDef",
    "ActivityTimedOutEventDetailsTypeDef",
    "BillingDetailsTypeDef",
    "CloudWatchEventsExecutionDataDetailsTypeDef",
    "CloudWatchLogsLogGroupTypeDef",
    "ExecutionAbortedEventDetailsTypeDef",
    "ExecutionFailedEventDetailsTypeDef",
    "ExecutionListItemTypeDef",
    "ExecutionStartedEventDetailsTypeDef",
    "ExecutionSucceededEventDetailsTypeDef",
    "ExecutionTimedOutEventDetailsTypeDef",
    "HistoryEventExecutionDataDetailsTypeDef",
    "HistoryEventTypeDef",
    "LambdaFunctionFailedEventDetailsTypeDef",
    "LambdaFunctionScheduleFailedEventDetailsTypeDef",
    "LambdaFunctionScheduledEventDetailsTypeDef",
    "LambdaFunctionStartFailedEventDetailsTypeDef",
    "LambdaFunctionSucceededEventDetailsTypeDef",
    "LambdaFunctionTimedOutEventDetailsTypeDef",
    "LogDestinationTypeDef",
    "LoggingConfigurationTypeDef",
    "MapIterationEventDetailsTypeDef",
    "MapStateStartedEventDetailsTypeDef",
    "ResponseMetadata",
    "StateEnteredEventDetailsTypeDef",
    "StateExitedEventDetailsTypeDef",
    "StateMachineListItemTypeDef",
    "TagTypeDef",
    "TaskFailedEventDetailsTypeDef",
    "TaskScheduledEventDetailsTypeDef",
    "TaskStartFailedEventDetailsTypeDef",
    "TaskStartedEventDetailsTypeDef",
    "TaskSubmitFailedEventDetailsTypeDef",
    "TaskSubmittedEventDetailsTypeDef",
    "TaskSucceededEventDetailsTypeDef",
    "TaskTimedOutEventDetailsTypeDef",
    "TracingConfigurationTypeDef",
    "CreateActivityOutputTypeDef",
    "CreateStateMachineOutputTypeDef",
    "DescribeActivityOutputTypeDef",
    "DescribeExecutionOutputTypeDef",
    "DescribeStateMachineForExecutionOutputTypeDef",
    "DescribeStateMachineOutputTypeDef",
    "GetActivityTaskOutputTypeDef",
    "GetExecutionHistoryOutputTypeDef",
    "ListActivitiesOutputTypeDef",
    "ListExecutionsOutputTypeDef",
    "ListStateMachinesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "PaginatorConfigTypeDef",
    "StartExecutionOutputTypeDef",
    "StartSyncExecutionOutputTypeDef",
    "StopExecutionOutputTypeDef",
    "UpdateStateMachineOutputTypeDef",
)

ActivityFailedEventDetailsTypeDef = TypedDict(
    "ActivityFailedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

ActivityListItemTypeDef = TypedDict(
    "ActivityListItemTypeDef", {"activityArn": str, "name": str, "creationDate": datetime}
)

ActivityScheduleFailedEventDetailsTypeDef = TypedDict(
    "ActivityScheduleFailedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

_RequiredActivityScheduledEventDetailsTypeDef = TypedDict(
    "_RequiredActivityScheduledEventDetailsTypeDef", {"resource": str}
)
_OptionalActivityScheduledEventDetailsTypeDef = TypedDict(
    "_OptionalActivityScheduledEventDetailsTypeDef",
    {
        "input": str,
        "inputDetails": "HistoryEventExecutionDataDetailsTypeDef",
        "timeoutInSeconds": int,
        "heartbeatInSeconds": int,
    },
    total=False,
)


class ActivityScheduledEventDetailsTypeDef(
    _RequiredActivityScheduledEventDetailsTypeDef, _OptionalActivityScheduledEventDetailsTypeDef
):
    pass


ActivityStartedEventDetailsTypeDef = TypedDict(
    "ActivityStartedEventDetailsTypeDef", {"workerName": str}, total=False
)

ActivitySucceededEventDetailsTypeDef = TypedDict(
    "ActivitySucceededEventDetailsTypeDef",
    {"output": str, "outputDetails": "HistoryEventExecutionDataDetailsTypeDef"},
    total=False,
)

ActivityTimedOutEventDetailsTypeDef = TypedDict(
    "ActivityTimedOutEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

BillingDetailsTypeDef = TypedDict(
    "BillingDetailsTypeDef",
    {"billedMemoryUsedInMB": int, "billedDurationInMilliseconds": int},
    total=False,
)

CloudWatchEventsExecutionDataDetailsTypeDef = TypedDict(
    "CloudWatchEventsExecutionDataDetailsTypeDef", {"included": bool}, total=False
)

CloudWatchLogsLogGroupTypeDef = TypedDict(
    "CloudWatchLogsLogGroupTypeDef", {"logGroupArn": str}, total=False
)

ExecutionAbortedEventDetailsTypeDef = TypedDict(
    "ExecutionAbortedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

ExecutionFailedEventDetailsTypeDef = TypedDict(
    "ExecutionFailedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

_RequiredExecutionListItemTypeDef = TypedDict(
    "_RequiredExecutionListItemTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": Literal["RUNNING", "SUCCEEDED", "FAILED", "TIMED_OUT", "ABORTED"],
        "startDate": datetime,
    },
)
_OptionalExecutionListItemTypeDef = TypedDict(
    "_OptionalExecutionListItemTypeDef", {"stopDate": datetime}, total=False
)


class ExecutionListItemTypeDef(
    _RequiredExecutionListItemTypeDef, _OptionalExecutionListItemTypeDef
):
    pass


ExecutionStartedEventDetailsTypeDef = TypedDict(
    "ExecutionStartedEventDetailsTypeDef",
    {"input": str, "inputDetails": "HistoryEventExecutionDataDetailsTypeDef", "roleArn": str},
    total=False,
)

ExecutionSucceededEventDetailsTypeDef = TypedDict(
    "ExecutionSucceededEventDetailsTypeDef",
    {"output": str, "outputDetails": "HistoryEventExecutionDataDetailsTypeDef"},
    total=False,
)

ExecutionTimedOutEventDetailsTypeDef = TypedDict(
    "ExecutionTimedOutEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

HistoryEventExecutionDataDetailsTypeDef = TypedDict(
    "HistoryEventExecutionDataDetailsTypeDef", {"truncated": bool}, total=False
)

_RequiredHistoryEventTypeDef = TypedDict(
    "_RequiredHistoryEventTypeDef",
    {
        "timestamp": datetime,
        "type": Literal[
            "ActivityFailed",
            "ActivityScheduled",
            "ActivityScheduleFailed",
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
            "LambdaFunctionScheduled",
            "LambdaFunctionScheduleFailed",
            "LambdaFunctionStarted",
            "LambdaFunctionStartFailed",
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
            "TaskStarted",
            "TaskStartFailed",
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
        ],
        "id": int,
    },
)
_OptionalHistoryEventTypeDef = TypedDict(
    "_OptionalHistoryEventTypeDef",
    {
        "previousEventId": int,
        "activityFailedEventDetails": "ActivityFailedEventDetailsTypeDef",
        "activityScheduleFailedEventDetails": "ActivityScheduleFailedEventDetailsTypeDef",
        "activityScheduledEventDetails": "ActivityScheduledEventDetailsTypeDef",
        "activityStartedEventDetails": "ActivityStartedEventDetailsTypeDef",
        "activitySucceededEventDetails": "ActivitySucceededEventDetailsTypeDef",
        "activityTimedOutEventDetails": "ActivityTimedOutEventDetailsTypeDef",
        "taskFailedEventDetails": "TaskFailedEventDetailsTypeDef",
        "taskScheduledEventDetails": "TaskScheduledEventDetailsTypeDef",
        "taskStartFailedEventDetails": "TaskStartFailedEventDetailsTypeDef",
        "taskStartedEventDetails": "TaskStartedEventDetailsTypeDef",
        "taskSubmitFailedEventDetails": "TaskSubmitFailedEventDetailsTypeDef",
        "taskSubmittedEventDetails": "TaskSubmittedEventDetailsTypeDef",
        "taskSucceededEventDetails": "TaskSucceededEventDetailsTypeDef",
        "taskTimedOutEventDetails": "TaskTimedOutEventDetailsTypeDef",
        "executionFailedEventDetails": "ExecutionFailedEventDetailsTypeDef",
        "executionStartedEventDetails": "ExecutionStartedEventDetailsTypeDef",
        "executionSucceededEventDetails": "ExecutionSucceededEventDetailsTypeDef",
        "executionAbortedEventDetails": "ExecutionAbortedEventDetailsTypeDef",
        "executionTimedOutEventDetails": "ExecutionTimedOutEventDetailsTypeDef",
        "mapStateStartedEventDetails": "MapStateStartedEventDetailsTypeDef",
        "mapIterationStartedEventDetails": "MapIterationEventDetailsTypeDef",
        "mapIterationSucceededEventDetails": "MapIterationEventDetailsTypeDef",
        "mapIterationFailedEventDetails": "MapIterationEventDetailsTypeDef",
        "mapIterationAbortedEventDetails": "MapIterationEventDetailsTypeDef",
        "lambdaFunctionFailedEventDetails": "LambdaFunctionFailedEventDetailsTypeDef",
        "lambdaFunctionScheduleFailedEventDetails": "LambdaFunctionScheduleFailedEventDetailsTypeDef",
        "lambdaFunctionScheduledEventDetails": "LambdaFunctionScheduledEventDetailsTypeDef",
        "lambdaFunctionStartFailedEventDetails": "LambdaFunctionStartFailedEventDetailsTypeDef",
        "lambdaFunctionSucceededEventDetails": "LambdaFunctionSucceededEventDetailsTypeDef",
        "lambdaFunctionTimedOutEventDetails": "LambdaFunctionTimedOutEventDetailsTypeDef",
        "stateEnteredEventDetails": "StateEnteredEventDetailsTypeDef",
        "stateExitedEventDetails": "StateExitedEventDetailsTypeDef",
    },
    total=False,
)


class HistoryEventTypeDef(_RequiredHistoryEventTypeDef, _OptionalHistoryEventTypeDef):
    pass


LambdaFunctionFailedEventDetailsTypeDef = TypedDict(
    "LambdaFunctionFailedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

LambdaFunctionScheduleFailedEventDetailsTypeDef = TypedDict(
    "LambdaFunctionScheduleFailedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

_RequiredLambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "_RequiredLambdaFunctionScheduledEventDetailsTypeDef", {"resource": str}
)
_OptionalLambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "_OptionalLambdaFunctionScheduledEventDetailsTypeDef",
    {
        "input": str,
        "inputDetails": "HistoryEventExecutionDataDetailsTypeDef",
        "timeoutInSeconds": int,
    },
    total=False,
)


class LambdaFunctionScheduledEventDetailsTypeDef(
    _RequiredLambdaFunctionScheduledEventDetailsTypeDef,
    _OptionalLambdaFunctionScheduledEventDetailsTypeDef,
):
    pass


LambdaFunctionStartFailedEventDetailsTypeDef = TypedDict(
    "LambdaFunctionStartFailedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

LambdaFunctionSucceededEventDetailsTypeDef = TypedDict(
    "LambdaFunctionSucceededEventDetailsTypeDef",
    {"output": str, "outputDetails": "HistoryEventExecutionDataDetailsTypeDef"},
    total=False,
)

LambdaFunctionTimedOutEventDetailsTypeDef = TypedDict(
    "LambdaFunctionTimedOutEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)

LogDestinationTypeDef = TypedDict(
    "LogDestinationTypeDef",
    {"cloudWatchLogsLogGroup": "CloudWatchLogsLogGroupTypeDef"},
    total=False,
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "level": Literal["ALL", "ERROR", "FATAL", "OFF"],
        "includeExecutionData": bool,
        "destinations": List["LogDestinationTypeDef"],
    },
    total=False,
)

MapIterationEventDetailsTypeDef = TypedDict(
    "MapIterationEventDetailsTypeDef", {"name": str, "index": int}, total=False
)

MapStateStartedEventDetailsTypeDef = TypedDict(
    "MapStateStartedEventDetailsTypeDef", {"length": int}, total=False
)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredStateEnteredEventDetailsTypeDef = TypedDict(
    "_RequiredStateEnteredEventDetailsTypeDef", {"name": str}
)
_OptionalStateEnteredEventDetailsTypeDef = TypedDict(
    "_OptionalStateEnteredEventDetailsTypeDef",
    {"input": str, "inputDetails": "HistoryEventExecutionDataDetailsTypeDef"},
    total=False,
)


class StateEnteredEventDetailsTypeDef(
    _RequiredStateEnteredEventDetailsTypeDef, _OptionalStateEnteredEventDetailsTypeDef
):
    pass


_RequiredStateExitedEventDetailsTypeDef = TypedDict(
    "_RequiredStateExitedEventDetailsTypeDef", {"name": str}
)
_OptionalStateExitedEventDetailsTypeDef = TypedDict(
    "_OptionalStateExitedEventDetailsTypeDef",
    {"output": str, "outputDetails": "HistoryEventExecutionDataDetailsTypeDef"},
    total=False,
)


class StateExitedEventDetailsTypeDef(
    _RequiredStateExitedEventDetailsTypeDef, _OptionalStateExitedEventDetailsTypeDef
):
    pass


StateMachineListItemTypeDef = TypedDict(
    "StateMachineListItemTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "type": Literal["STANDARD", "EXPRESS"],
        "creationDate": datetime,
    },
)

TagTypeDef = TypedDict("TagTypeDef", {"key": str, "value": str}, total=False)

_RequiredTaskFailedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskFailedEventDetailsTypeDef", {"resourceType": str, "resource": str}
)
_OptionalTaskFailedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskFailedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)


class TaskFailedEventDetailsTypeDef(
    _RequiredTaskFailedEventDetailsTypeDef, _OptionalTaskFailedEventDetailsTypeDef
):
    pass


_RequiredTaskScheduledEventDetailsTypeDef = TypedDict(
    "_RequiredTaskScheduledEventDetailsTypeDef",
    {"resourceType": str, "resource": str, "region": str, "parameters": str},
)
_OptionalTaskScheduledEventDetailsTypeDef = TypedDict(
    "_OptionalTaskScheduledEventDetailsTypeDef",
    {"timeoutInSeconds": int, "heartbeatInSeconds": int},
    total=False,
)


class TaskScheduledEventDetailsTypeDef(
    _RequiredTaskScheduledEventDetailsTypeDef, _OptionalTaskScheduledEventDetailsTypeDef
):
    pass


_RequiredTaskStartFailedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskStartFailedEventDetailsTypeDef", {"resourceType": str, "resource": str}
)
_OptionalTaskStartFailedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskStartFailedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)


class TaskStartFailedEventDetailsTypeDef(
    _RequiredTaskStartFailedEventDetailsTypeDef, _OptionalTaskStartFailedEventDetailsTypeDef
):
    pass


TaskStartedEventDetailsTypeDef = TypedDict(
    "TaskStartedEventDetailsTypeDef", {"resourceType": str, "resource": str}
)

_RequiredTaskSubmitFailedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskSubmitFailedEventDetailsTypeDef", {"resourceType": str, "resource": str}
)
_OptionalTaskSubmitFailedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskSubmitFailedEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)


class TaskSubmitFailedEventDetailsTypeDef(
    _RequiredTaskSubmitFailedEventDetailsTypeDef, _OptionalTaskSubmitFailedEventDetailsTypeDef
):
    pass


_RequiredTaskSubmittedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskSubmittedEventDetailsTypeDef", {"resourceType": str, "resource": str}
)
_OptionalTaskSubmittedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskSubmittedEventDetailsTypeDef",
    {"output": str, "outputDetails": "HistoryEventExecutionDataDetailsTypeDef"},
    total=False,
)


class TaskSubmittedEventDetailsTypeDef(
    _RequiredTaskSubmittedEventDetailsTypeDef, _OptionalTaskSubmittedEventDetailsTypeDef
):
    pass


_RequiredTaskSucceededEventDetailsTypeDef = TypedDict(
    "_RequiredTaskSucceededEventDetailsTypeDef", {"resourceType": str, "resource": str}
)
_OptionalTaskSucceededEventDetailsTypeDef = TypedDict(
    "_OptionalTaskSucceededEventDetailsTypeDef",
    {"output": str, "outputDetails": "HistoryEventExecutionDataDetailsTypeDef"},
    total=False,
)


class TaskSucceededEventDetailsTypeDef(
    _RequiredTaskSucceededEventDetailsTypeDef, _OptionalTaskSucceededEventDetailsTypeDef
):
    pass


_RequiredTaskTimedOutEventDetailsTypeDef = TypedDict(
    "_RequiredTaskTimedOutEventDetailsTypeDef", {"resourceType": str, "resource": str}
)
_OptionalTaskTimedOutEventDetailsTypeDef = TypedDict(
    "_OptionalTaskTimedOutEventDetailsTypeDef", {"error": str, "cause": str}, total=False
)


class TaskTimedOutEventDetailsTypeDef(
    _RequiredTaskTimedOutEventDetailsTypeDef, _OptionalTaskTimedOutEventDetailsTypeDef
):
    pass


TracingConfigurationTypeDef = TypedDict(
    "TracingConfigurationTypeDef", {"enabled": bool}, total=False
)

_RequiredCreateActivityOutputTypeDef = TypedDict(
    "_RequiredCreateActivityOutputTypeDef", {"activityArn": str, "creationDate": datetime}
)
_OptionalCreateActivityOutputTypeDef = TypedDict(
    "_OptionalCreateActivityOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class CreateActivityOutputTypeDef(
    _RequiredCreateActivityOutputTypeDef, _OptionalCreateActivityOutputTypeDef
):
    pass


_RequiredCreateStateMachineOutputTypeDef = TypedDict(
    "_RequiredCreateStateMachineOutputTypeDef", {"stateMachineArn": str, "creationDate": datetime}
)
_OptionalCreateStateMachineOutputTypeDef = TypedDict(
    "_OptionalCreateStateMachineOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class CreateStateMachineOutputTypeDef(
    _RequiredCreateStateMachineOutputTypeDef, _OptionalCreateStateMachineOutputTypeDef
):
    pass


_RequiredDescribeActivityOutputTypeDef = TypedDict(
    "_RequiredDescribeActivityOutputTypeDef",
    {"activityArn": str, "name": str, "creationDate": datetime},
)
_OptionalDescribeActivityOutputTypeDef = TypedDict(
    "_OptionalDescribeActivityOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class DescribeActivityOutputTypeDef(
    _RequiredDescribeActivityOutputTypeDef, _OptionalDescribeActivityOutputTypeDef
):
    pass


_RequiredDescribeExecutionOutputTypeDef = TypedDict(
    "_RequiredDescribeExecutionOutputTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "status": Literal["RUNNING", "SUCCEEDED", "FAILED", "TIMED_OUT", "ABORTED"],
        "startDate": datetime,
    },
)
_OptionalDescribeExecutionOutputTypeDef = TypedDict(
    "_OptionalDescribeExecutionOutputTypeDef",
    {
        "name": str,
        "stopDate": datetime,
        "input": str,
        "inputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "output": str,
        "outputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "traceHeader": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class DescribeExecutionOutputTypeDef(
    _RequiredDescribeExecutionOutputTypeDef, _OptionalDescribeExecutionOutputTypeDef
):
    pass


_RequiredDescribeStateMachineForExecutionOutputTypeDef = TypedDict(
    "_RequiredDescribeStateMachineForExecutionOutputTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "definition": str,
        "roleArn": str,
        "updateDate": datetime,
    },
)
_OptionalDescribeStateMachineForExecutionOutputTypeDef = TypedDict(
    "_OptionalDescribeStateMachineForExecutionOutputTypeDef",
    {
        "loggingConfiguration": "LoggingConfigurationTypeDef",
        "tracingConfiguration": "TracingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class DescribeStateMachineForExecutionOutputTypeDef(
    _RequiredDescribeStateMachineForExecutionOutputTypeDef,
    _OptionalDescribeStateMachineForExecutionOutputTypeDef,
):
    pass


_RequiredDescribeStateMachineOutputTypeDef = TypedDict(
    "_RequiredDescribeStateMachineOutputTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "definition": str,
        "roleArn": str,
        "type": Literal["STANDARD", "EXPRESS"],
        "creationDate": datetime,
    },
)
_OptionalDescribeStateMachineOutputTypeDef = TypedDict(
    "_OptionalDescribeStateMachineOutputTypeDef",
    {
        "status": Literal["ACTIVE", "DELETING"],
        "loggingConfiguration": "LoggingConfigurationTypeDef",
        "tracingConfiguration": "TracingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class DescribeStateMachineOutputTypeDef(
    _RequiredDescribeStateMachineOutputTypeDef, _OptionalDescribeStateMachineOutputTypeDef
):
    pass


GetActivityTaskOutputTypeDef = TypedDict(
    "GetActivityTaskOutputTypeDef",
    {"taskToken": str, "input": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredGetExecutionHistoryOutputTypeDef = TypedDict(
    "_RequiredGetExecutionHistoryOutputTypeDef", {"events": List["HistoryEventTypeDef"]}
)
_OptionalGetExecutionHistoryOutputTypeDef = TypedDict(
    "_OptionalGetExecutionHistoryOutputTypeDef",
    {"nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class GetExecutionHistoryOutputTypeDef(
    _RequiredGetExecutionHistoryOutputTypeDef, _OptionalGetExecutionHistoryOutputTypeDef
):
    pass


_RequiredListActivitiesOutputTypeDef = TypedDict(
    "_RequiredListActivitiesOutputTypeDef", {"activities": List["ActivityListItemTypeDef"]}
)
_OptionalListActivitiesOutputTypeDef = TypedDict(
    "_OptionalListActivitiesOutputTypeDef",
    {"nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListActivitiesOutputTypeDef(
    _RequiredListActivitiesOutputTypeDef, _OptionalListActivitiesOutputTypeDef
):
    pass


_RequiredListExecutionsOutputTypeDef = TypedDict(
    "_RequiredListExecutionsOutputTypeDef", {"executions": List["ExecutionListItemTypeDef"]}
)
_OptionalListExecutionsOutputTypeDef = TypedDict(
    "_OptionalListExecutionsOutputTypeDef",
    {"nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListExecutionsOutputTypeDef(
    _RequiredListExecutionsOutputTypeDef, _OptionalListExecutionsOutputTypeDef
):
    pass


_RequiredListStateMachinesOutputTypeDef = TypedDict(
    "_RequiredListStateMachinesOutputTypeDef",
    {"stateMachines": List["StateMachineListItemTypeDef"]},
)
_OptionalListStateMachinesOutputTypeDef = TypedDict(
    "_OptionalListStateMachinesOutputTypeDef",
    {"nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListStateMachinesOutputTypeDef(
    _RequiredListStateMachinesOutputTypeDef, _OptionalListStateMachinesOutputTypeDef
):
    pass


ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {"tags": List["TagTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

_RequiredStartExecutionOutputTypeDef = TypedDict(
    "_RequiredStartExecutionOutputTypeDef", {"executionArn": str, "startDate": datetime}
)
_OptionalStartExecutionOutputTypeDef = TypedDict(
    "_OptionalStartExecutionOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class StartExecutionOutputTypeDef(
    _RequiredStartExecutionOutputTypeDef, _OptionalStartExecutionOutputTypeDef
):
    pass


_RequiredStartSyncExecutionOutputTypeDef = TypedDict(
    "_RequiredStartSyncExecutionOutputTypeDef",
    {
        "executionArn": str,
        "startDate": datetime,
        "stopDate": datetime,
        "status": Literal["SUCCEEDED", "FAILED", "TIMED_OUT"],
    },
)
_OptionalStartSyncExecutionOutputTypeDef = TypedDict(
    "_OptionalStartSyncExecutionOutputTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "error": str,
        "cause": str,
        "input": str,
        "inputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "output": str,
        "outputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "traceHeader": str,
        "billingDetails": "BillingDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class StartSyncExecutionOutputTypeDef(
    _RequiredStartSyncExecutionOutputTypeDef, _OptionalStartSyncExecutionOutputTypeDef
):
    pass


_RequiredStopExecutionOutputTypeDef = TypedDict(
    "_RequiredStopExecutionOutputTypeDef", {"stopDate": datetime}
)
_OptionalStopExecutionOutputTypeDef = TypedDict(
    "_OptionalStopExecutionOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class StopExecutionOutputTypeDef(
    _RequiredStopExecutionOutputTypeDef, _OptionalStopExecutionOutputTypeDef
):
    pass


_RequiredUpdateStateMachineOutputTypeDef = TypedDict(
    "_RequiredUpdateStateMachineOutputTypeDef", {"updateDate": datetime}
)
_OptionalUpdateStateMachineOutputTypeDef = TypedDict(
    "_OptionalUpdateStateMachineOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class UpdateStateMachineOutputTypeDef(
    _RequiredUpdateStateMachineOutputTypeDef, _OptionalUpdateStateMachineOutputTypeDef
):
    pass
