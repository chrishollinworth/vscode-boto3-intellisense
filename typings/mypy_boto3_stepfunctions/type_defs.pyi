"""
Type annotations for stepfunctions service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/type_defs.html)

Usage::

    ```python
    from mypy_boto3_stepfunctions.type_defs import ActivityFailedEventDetailsTypeDef

    data: ActivityFailedEventDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ExecutionStatusType,
    HistoryEventTypeType,
    LogLevelType,
    StateMachineStatusType,
    StateMachineTypeType,
    SyncExecutionStatusType,
)

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
    "CreateActivityInputRequestTypeDef",
    "CreateActivityOutputTypeDef",
    "CreateStateMachineInputRequestTypeDef",
    "CreateStateMachineOutputTypeDef",
    "DeleteActivityInputRequestTypeDef",
    "DeleteStateMachineInputRequestTypeDef",
    "DescribeActivityInputRequestTypeDef",
    "DescribeActivityOutputTypeDef",
    "DescribeExecutionInputRequestTypeDef",
    "DescribeExecutionOutputTypeDef",
    "DescribeStateMachineForExecutionInputRequestTypeDef",
    "DescribeStateMachineForExecutionOutputTypeDef",
    "DescribeStateMachineInputRequestTypeDef",
    "DescribeStateMachineOutputTypeDef",
    "ExecutionAbortedEventDetailsTypeDef",
    "ExecutionFailedEventDetailsTypeDef",
    "ExecutionListItemTypeDef",
    "ExecutionStartedEventDetailsTypeDef",
    "ExecutionSucceededEventDetailsTypeDef",
    "ExecutionTimedOutEventDetailsTypeDef",
    "GetActivityTaskInputRequestTypeDef",
    "GetActivityTaskOutputTypeDef",
    "GetExecutionHistoryInputRequestTypeDef",
    "GetExecutionHistoryOutputTypeDef",
    "HistoryEventExecutionDataDetailsTypeDef",
    "HistoryEventTypeDef",
    "LambdaFunctionFailedEventDetailsTypeDef",
    "LambdaFunctionScheduleFailedEventDetailsTypeDef",
    "LambdaFunctionScheduledEventDetailsTypeDef",
    "LambdaFunctionStartFailedEventDetailsTypeDef",
    "LambdaFunctionSucceededEventDetailsTypeDef",
    "LambdaFunctionTimedOutEventDetailsTypeDef",
    "ListActivitiesInputRequestTypeDef",
    "ListActivitiesOutputTypeDef",
    "ListExecutionsInputRequestTypeDef",
    "ListExecutionsOutputTypeDef",
    "ListStateMachinesInputRequestTypeDef",
    "ListStateMachinesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LogDestinationTypeDef",
    "LoggingConfigurationTypeDef",
    "MapIterationEventDetailsTypeDef",
    "MapStateStartedEventDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SendTaskFailureInputRequestTypeDef",
    "SendTaskHeartbeatInputRequestTypeDef",
    "SendTaskSuccessInputRequestTypeDef",
    "StartExecutionInputRequestTypeDef",
    "StartExecutionOutputTypeDef",
    "StartSyncExecutionInputRequestTypeDef",
    "StartSyncExecutionOutputTypeDef",
    "StateEnteredEventDetailsTypeDef",
    "StateExitedEventDetailsTypeDef",
    "StateMachineListItemTypeDef",
    "StopExecutionInputRequestTypeDef",
    "StopExecutionOutputTypeDef",
    "TagResourceInputRequestTypeDef",
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
    "UntagResourceInputRequestTypeDef",
    "UpdateStateMachineInputRequestTypeDef",
    "UpdateStateMachineOutputTypeDef",
)

ActivityFailedEventDetailsTypeDef = TypedDict(
    "ActivityFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

ActivityListItemTypeDef = TypedDict(
    "ActivityListItemTypeDef",
    {
        "activityArn": str,
        "name": str,
        "creationDate": datetime,
    },
)

ActivityScheduleFailedEventDetailsTypeDef = TypedDict(
    "ActivityScheduleFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

_RequiredActivityScheduledEventDetailsTypeDef = TypedDict(
    "_RequiredActivityScheduledEventDetailsTypeDef",
    {
        "resource": str,
    },
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
    "ActivityStartedEventDetailsTypeDef",
    {
        "workerName": str,
    },
    total=False,
)

ActivitySucceededEventDetailsTypeDef = TypedDict(
    "ActivitySucceededEventDetailsTypeDef",
    {
        "output": str,
        "outputDetails": "HistoryEventExecutionDataDetailsTypeDef",
    },
    total=False,
)

ActivityTimedOutEventDetailsTypeDef = TypedDict(
    "ActivityTimedOutEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

BillingDetailsTypeDef = TypedDict(
    "BillingDetailsTypeDef",
    {
        "billedMemoryUsedInMB": int,
        "billedDurationInMilliseconds": int,
    },
    total=False,
)

CloudWatchEventsExecutionDataDetailsTypeDef = TypedDict(
    "CloudWatchEventsExecutionDataDetailsTypeDef",
    {
        "included": bool,
    },
    total=False,
)

CloudWatchLogsLogGroupTypeDef = TypedDict(
    "CloudWatchLogsLogGroupTypeDef",
    {
        "logGroupArn": str,
    },
    total=False,
)

_RequiredCreateActivityInputRequestTypeDef = TypedDict(
    "_RequiredCreateActivityInputRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateActivityInputRequestTypeDef = TypedDict(
    "_OptionalCreateActivityInputRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateActivityInputRequestTypeDef(
    _RequiredCreateActivityInputRequestTypeDef, _OptionalCreateActivityInputRequestTypeDef
):
    pass

CreateActivityOutputTypeDef = TypedDict(
    "CreateActivityOutputTypeDef",
    {
        "activityArn": str,
        "creationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStateMachineInputRequestTypeDef = TypedDict(
    "_RequiredCreateStateMachineInputRequestTypeDef",
    {
        "name": str,
        "definition": str,
        "roleArn": str,
    },
)
_OptionalCreateStateMachineInputRequestTypeDef = TypedDict(
    "_OptionalCreateStateMachineInputRequestTypeDef",
    {
        "type": StateMachineTypeType,
        "loggingConfiguration": "LoggingConfigurationTypeDef",
        "tags": List["TagTypeDef"],
        "tracingConfiguration": "TracingConfigurationTypeDef",
    },
    total=False,
)

class CreateStateMachineInputRequestTypeDef(
    _RequiredCreateStateMachineInputRequestTypeDef, _OptionalCreateStateMachineInputRequestTypeDef
):
    pass

CreateStateMachineOutputTypeDef = TypedDict(
    "CreateStateMachineOutputTypeDef",
    {
        "stateMachineArn": str,
        "creationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteActivityInputRequestTypeDef = TypedDict(
    "DeleteActivityInputRequestTypeDef",
    {
        "activityArn": str,
    },
)

DeleteStateMachineInputRequestTypeDef = TypedDict(
    "DeleteStateMachineInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)

DescribeActivityInputRequestTypeDef = TypedDict(
    "DescribeActivityInputRequestTypeDef",
    {
        "activityArn": str,
    },
)

DescribeActivityOutputTypeDef = TypedDict(
    "DescribeActivityOutputTypeDef",
    {
        "activityArn": str,
        "name": str,
        "creationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExecutionInputRequestTypeDef = TypedDict(
    "DescribeExecutionInputRequestTypeDef",
    {
        "executionArn": str,
    },
)

DescribeExecutionOutputTypeDef = TypedDict(
    "DescribeExecutionOutputTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": ExecutionStatusType,
        "startDate": datetime,
        "stopDate": datetime,
        "input": str,
        "inputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "output": str,
        "outputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "traceHeader": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStateMachineForExecutionInputRequestTypeDef = TypedDict(
    "DescribeStateMachineForExecutionInputRequestTypeDef",
    {
        "executionArn": str,
    },
)

DescribeStateMachineForExecutionOutputTypeDef = TypedDict(
    "DescribeStateMachineForExecutionOutputTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "definition": str,
        "roleArn": str,
        "updateDate": datetime,
        "loggingConfiguration": "LoggingConfigurationTypeDef",
        "tracingConfiguration": "TracingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStateMachineInputRequestTypeDef = TypedDict(
    "DescribeStateMachineInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)

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
        "loggingConfiguration": "LoggingConfigurationTypeDef",
        "tracingConfiguration": "TracingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExecutionAbortedEventDetailsTypeDef = TypedDict(
    "ExecutionAbortedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

ExecutionFailedEventDetailsTypeDef = TypedDict(
    "ExecutionFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

_RequiredExecutionListItemTypeDef = TypedDict(
    "_RequiredExecutionListItemTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": ExecutionStatusType,
        "startDate": datetime,
    },
)
_OptionalExecutionListItemTypeDef = TypedDict(
    "_OptionalExecutionListItemTypeDef",
    {
        "stopDate": datetime,
    },
    total=False,
)

class ExecutionListItemTypeDef(
    _RequiredExecutionListItemTypeDef, _OptionalExecutionListItemTypeDef
):
    pass

ExecutionStartedEventDetailsTypeDef = TypedDict(
    "ExecutionStartedEventDetailsTypeDef",
    {
        "input": str,
        "inputDetails": "HistoryEventExecutionDataDetailsTypeDef",
        "roleArn": str,
    },
    total=False,
)

ExecutionSucceededEventDetailsTypeDef = TypedDict(
    "ExecutionSucceededEventDetailsTypeDef",
    {
        "output": str,
        "outputDetails": "HistoryEventExecutionDataDetailsTypeDef",
    },
    total=False,
)

ExecutionTimedOutEventDetailsTypeDef = TypedDict(
    "ExecutionTimedOutEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

_RequiredGetActivityTaskInputRequestTypeDef = TypedDict(
    "_RequiredGetActivityTaskInputRequestTypeDef",
    {
        "activityArn": str,
    },
)
_OptionalGetActivityTaskInputRequestTypeDef = TypedDict(
    "_OptionalGetActivityTaskInputRequestTypeDef",
    {
        "workerName": str,
    },
    total=False,
)

class GetActivityTaskInputRequestTypeDef(
    _RequiredGetActivityTaskInputRequestTypeDef, _OptionalGetActivityTaskInputRequestTypeDef
):
    pass

GetActivityTaskOutputTypeDef = TypedDict(
    "GetActivityTaskOutputTypeDef",
    {
        "taskToken": str,
        "input": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetExecutionHistoryInputRequestTypeDef = TypedDict(
    "_RequiredGetExecutionHistoryInputRequestTypeDef",
    {
        "executionArn": str,
    },
)
_OptionalGetExecutionHistoryInputRequestTypeDef = TypedDict(
    "_OptionalGetExecutionHistoryInputRequestTypeDef",
    {
        "maxResults": int,
        "reverseOrder": bool,
        "nextToken": str,
        "includeExecutionData": bool,
    },
    total=False,
)

class GetExecutionHistoryInputRequestTypeDef(
    _RequiredGetExecutionHistoryInputRequestTypeDef, _OptionalGetExecutionHistoryInputRequestTypeDef
):
    pass

GetExecutionHistoryOutputTypeDef = TypedDict(
    "GetExecutionHistoryOutputTypeDef",
    {
        "events": List["HistoryEventTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HistoryEventExecutionDataDetailsTypeDef = TypedDict(
    "HistoryEventExecutionDataDetailsTypeDef",
    {
        "truncated": bool,
    },
    total=False,
)

_RequiredHistoryEventTypeDef = TypedDict(
    "_RequiredHistoryEventTypeDef",
    {
        "timestamp": datetime,
        "type": HistoryEventTypeType,
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
    "LambdaFunctionFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

LambdaFunctionScheduleFailedEventDetailsTypeDef = TypedDict(
    "LambdaFunctionScheduleFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

_RequiredLambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "_RequiredLambdaFunctionScheduledEventDetailsTypeDef",
    {
        "resource": str,
    },
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
    "LambdaFunctionStartFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

LambdaFunctionSucceededEventDetailsTypeDef = TypedDict(
    "LambdaFunctionSucceededEventDetailsTypeDef",
    {
        "output": str,
        "outputDetails": "HistoryEventExecutionDataDetailsTypeDef",
    },
    total=False,
)

LambdaFunctionTimedOutEventDetailsTypeDef = TypedDict(
    "LambdaFunctionTimedOutEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

ListActivitiesInputRequestTypeDef = TypedDict(
    "ListActivitiesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListActivitiesOutputTypeDef = TypedDict(
    "ListActivitiesOutputTypeDef",
    {
        "activities": List["ActivityListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListExecutionsInputRequestTypeDef = TypedDict(
    "_RequiredListExecutionsInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)
_OptionalListExecutionsInputRequestTypeDef = TypedDict(
    "_OptionalListExecutionsInputRequestTypeDef",
    {
        "statusFilter": ExecutionStatusType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListExecutionsInputRequestTypeDef(
    _RequiredListExecutionsInputRequestTypeDef, _OptionalListExecutionsInputRequestTypeDef
):
    pass

ListExecutionsOutputTypeDef = TypedDict(
    "ListExecutionsOutputTypeDef",
    {
        "executions": List["ExecutionListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStateMachinesInputRequestTypeDef = TypedDict(
    "ListStateMachinesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListStateMachinesOutputTypeDef = TypedDict(
    "ListStateMachinesOutputTypeDef",
    {
        "stateMachines": List["StateMachineListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogDestinationTypeDef = TypedDict(
    "LogDestinationTypeDef",
    {
        "cloudWatchLogsLogGroup": "CloudWatchLogsLogGroupTypeDef",
    },
    total=False,
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "level": LogLevelType,
        "includeExecutionData": bool,
        "destinations": List["LogDestinationTypeDef"],
    },
    total=False,
)

MapIterationEventDetailsTypeDef = TypedDict(
    "MapIterationEventDetailsTypeDef",
    {
        "name": str,
        "index": int,
    },
    total=False,
)

MapStateStartedEventDetailsTypeDef = TypedDict(
    "MapStateStartedEventDetailsTypeDef",
    {
        "length": int,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

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

_RequiredSendTaskFailureInputRequestTypeDef = TypedDict(
    "_RequiredSendTaskFailureInputRequestTypeDef",
    {
        "taskToken": str,
    },
)
_OptionalSendTaskFailureInputRequestTypeDef = TypedDict(
    "_OptionalSendTaskFailureInputRequestTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

class SendTaskFailureInputRequestTypeDef(
    _RequiredSendTaskFailureInputRequestTypeDef, _OptionalSendTaskFailureInputRequestTypeDef
):
    pass

SendTaskHeartbeatInputRequestTypeDef = TypedDict(
    "SendTaskHeartbeatInputRequestTypeDef",
    {
        "taskToken": str,
    },
)

SendTaskSuccessInputRequestTypeDef = TypedDict(
    "SendTaskSuccessInputRequestTypeDef",
    {
        "taskToken": str,
        "output": str,
    },
)

_RequiredStartExecutionInputRequestTypeDef = TypedDict(
    "_RequiredStartExecutionInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)
_OptionalStartExecutionInputRequestTypeDef = TypedDict(
    "_OptionalStartExecutionInputRequestTypeDef",
    {
        "name": str,
        "input": str,
        "traceHeader": str,
    },
    total=False,
)

class StartExecutionInputRequestTypeDef(
    _RequiredStartExecutionInputRequestTypeDef, _OptionalStartExecutionInputRequestTypeDef
):
    pass

StartExecutionOutputTypeDef = TypedDict(
    "StartExecutionOutputTypeDef",
    {
        "executionArn": str,
        "startDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartSyncExecutionInputRequestTypeDef = TypedDict(
    "_RequiredStartSyncExecutionInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)
_OptionalStartSyncExecutionInputRequestTypeDef = TypedDict(
    "_OptionalStartSyncExecutionInputRequestTypeDef",
    {
        "name": str,
        "input": str,
        "traceHeader": str,
    },
    total=False,
)

class StartSyncExecutionInputRequestTypeDef(
    _RequiredStartSyncExecutionInputRequestTypeDef, _OptionalStartSyncExecutionInputRequestTypeDef
):
    pass

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
        "inputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "output": str,
        "outputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "traceHeader": str,
        "billingDetails": "BillingDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStateEnteredEventDetailsTypeDef = TypedDict(
    "_RequiredStateEnteredEventDetailsTypeDef",
    {
        "name": str,
    },
)
_OptionalStateEnteredEventDetailsTypeDef = TypedDict(
    "_OptionalStateEnteredEventDetailsTypeDef",
    {
        "input": str,
        "inputDetails": "HistoryEventExecutionDataDetailsTypeDef",
    },
    total=False,
)

class StateEnteredEventDetailsTypeDef(
    _RequiredStateEnteredEventDetailsTypeDef, _OptionalStateEnteredEventDetailsTypeDef
):
    pass

_RequiredStateExitedEventDetailsTypeDef = TypedDict(
    "_RequiredStateExitedEventDetailsTypeDef",
    {
        "name": str,
    },
)
_OptionalStateExitedEventDetailsTypeDef = TypedDict(
    "_OptionalStateExitedEventDetailsTypeDef",
    {
        "output": str,
        "outputDetails": "HistoryEventExecutionDataDetailsTypeDef",
    },
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
        "type": StateMachineTypeType,
        "creationDate": datetime,
    },
)

_RequiredStopExecutionInputRequestTypeDef = TypedDict(
    "_RequiredStopExecutionInputRequestTypeDef",
    {
        "executionArn": str,
    },
)
_OptionalStopExecutionInputRequestTypeDef = TypedDict(
    "_OptionalStopExecutionInputRequestTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

class StopExecutionInputRequestTypeDef(
    _RequiredStopExecutionInputRequestTypeDef, _OptionalStopExecutionInputRequestTypeDef
):
    pass

StopExecutionOutputTypeDef = TypedDict(
    "StopExecutionOutputTypeDef",
    {
        "stopDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

_RequiredTaskFailedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskFailedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)
_OptionalTaskFailedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

class TaskFailedEventDetailsTypeDef(
    _RequiredTaskFailedEventDetailsTypeDef, _OptionalTaskFailedEventDetailsTypeDef
):
    pass

_RequiredTaskScheduledEventDetailsTypeDef = TypedDict(
    "_RequiredTaskScheduledEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "region": str,
        "parameters": str,
    },
)
_OptionalTaskScheduledEventDetailsTypeDef = TypedDict(
    "_OptionalTaskScheduledEventDetailsTypeDef",
    {
        "timeoutInSeconds": int,
        "heartbeatInSeconds": int,
    },
    total=False,
)

class TaskScheduledEventDetailsTypeDef(
    _RequiredTaskScheduledEventDetailsTypeDef, _OptionalTaskScheduledEventDetailsTypeDef
):
    pass

_RequiredTaskStartFailedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskStartFailedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)
_OptionalTaskStartFailedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskStartFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

class TaskStartFailedEventDetailsTypeDef(
    _RequiredTaskStartFailedEventDetailsTypeDef, _OptionalTaskStartFailedEventDetailsTypeDef
):
    pass

TaskStartedEventDetailsTypeDef = TypedDict(
    "TaskStartedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)

_RequiredTaskSubmitFailedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskSubmitFailedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)
_OptionalTaskSubmitFailedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskSubmitFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

class TaskSubmitFailedEventDetailsTypeDef(
    _RequiredTaskSubmitFailedEventDetailsTypeDef, _OptionalTaskSubmitFailedEventDetailsTypeDef
):
    pass

_RequiredTaskSubmittedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskSubmittedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)
_OptionalTaskSubmittedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskSubmittedEventDetailsTypeDef",
    {
        "output": str,
        "outputDetails": "HistoryEventExecutionDataDetailsTypeDef",
    },
    total=False,
)

class TaskSubmittedEventDetailsTypeDef(
    _RequiredTaskSubmittedEventDetailsTypeDef, _OptionalTaskSubmittedEventDetailsTypeDef
):
    pass

_RequiredTaskSucceededEventDetailsTypeDef = TypedDict(
    "_RequiredTaskSucceededEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)
_OptionalTaskSucceededEventDetailsTypeDef = TypedDict(
    "_OptionalTaskSucceededEventDetailsTypeDef",
    {
        "output": str,
        "outputDetails": "HistoryEventExecutionDataDetailsTypeDef",
    },
    total=False,
)

class TaskSucceededEventDetailsTypeDef(
    _RequiredTaskSucceededEventDetailsTypeDef, _OptionalTaskSucceededEventDetailsTypeDef
):
    pass

_RequiredTaskTimedOutEventDetailsTypeDef = TypedDict(
    "_RequiredTaskTimedOutEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)
_OptionalTaskTimedOutEventDetailsTypeDef = TypedDict(
    "_OptionalTaskTimedOutEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

class TaskTimedOutEventDetailsTypeDef(
    _RequiredTaskTimedOutEventDetailsTypeDef, _OptionalTaskTimedOutEventDetailsTypeDef
):
    pass

TracingConfigurationTypeDef = TypedDict(
    "TracingConfigurationTypeDef",
    {
        "enabled": bool,
    },
    total=False,
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateStateMachineInputRequestTypeDef = TypedDict(
    "_RequiredUpdateStateMachineInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)
_OptionalUpdateStateMachineInputRequestTypeDef = TypedDict(
    "_OptionalUpdateStateMachineInputRequestTypeDef",
    {
        "definition": str,
        "roleArn": str,
        "loggingConfiguration": "LoggingConfigurationTypeDef",
        "tracingConfiguration": "TracingConfigurationTypeDef",
    },
    total=False,
)

class UpdateStateMachineInputRequestTypeDef(
    _RequiredUpdateStateMachineInputRequestTypeDef, _OptionalUpdateStateMachineInputRequestTypeDef
):
    pass

UpdateStateMachineOutputTypeDef = TypedDict(
    "UpdateStateMachineOutputTypeDef",
    {
        "updateDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
