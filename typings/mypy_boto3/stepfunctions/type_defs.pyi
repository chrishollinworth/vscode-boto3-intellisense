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
    ExecutionRedriveFilterType,
    ExecutionRedriveStatusType,
    ExecutionStatusType,
    HistoryEventTypeType,
    InspectionLevelType,
    LogLevelType,
    MapRunStatusType,
    StateMachineStatusType,
    StateMachineTypeType,
    SyncExecutionStatusType,
    TestExecutionStatusType,
    ValidateStateMachineDefinitionResultCodeType,
)

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
    "CreateActivityInputRequestTypeDef",
    "CreateActivityOutputTypeDef",
    "CreateStateMachineAliasInputRequestTypeDef",
    "CreateStateMachineAliasOutputTypeDef",
    "CreateStateMachineInputRequestTypeDef",
    "CreateStateMachineOutputTypeDef",
    "DeleteActivityInputRequestTypeDef",
    "DeleteStateMachineAliasInputRequestTypeDef",
    "DeleteStateMachineInputRequestTypeDef",
    "DeleteStateMachineVersionInputRequestTypeDef",
    "DescribeActivityInputRequestTypeDef",
    "DescribeActivityOutputTypeDef",
    "DescribeExecutionInputRequestTypeDef",
    "DescribeExecutionOutputTypeDef",
    "DescribeMapRunInputRequestTypeDef",
    "DescribeMapRunOutputTypeDef",
    "DescribeStateMachineAliasInputRequestTypeDef",
    "DescribeStateMachineAliasOutputTypeDef",
    "DescribeStateMachineForExecutionInputRequestTypeDef",
    "DescribeStateMachineForExecutionOutputTypeDef",
    "DescribeStateMachineInputRequestTypeDef",
    "DescribeStateMachineOutputTypeDef",
    "ExecutionAbortedEventDetailsTypeDef",
    "ExecutionFailedEventDetailsTypeDef",
    "ExecutionListItemTypeDef",
    "ExecutionRedrivenEventDetailsTypeDef",
    "ExecutionStartedEventDetailsTypeDef",
    "ExecutionSucceededEventDetailsTypeDef",
    "ExecutionTimedOutEventDetailsTypeDef",
    "GetActivityTaskInputRequestTypeDef",
    "GetActivityTaskOutputTypeDef",
    "GetExecutionHistoryInputRequestTypeDef",
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
    "ListActivitiesInputRequestTypeDef",
    "ListActivitiesOutputTypeDef",
    "ListExecutionsInputRequestTypeDef",
    "ListExecutionsOutputTypeDef",
    "ListMapRunsInputRequestTypeDef",
    "ListMapRunsOutputTypeDef",
    "ListStateMachineAliasesInputRequestTypeDef",
    "ListStateMachineAliasesOutputTypeDef",
    "ListStateMachineVersionsInputRequestTypeDef",
    "ListStateMachineVersionsOutputTypeDef",
    "ListStateMachinesInputRequestTypeDef",
    "ListStateMachinesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LogDestinationTypeDef",
    "LoggingConfigurationTypeDef",
    "MapIterationEventDetailsTypeDef",
    "MapRunExecutionCountsTypeDef",
    "MapRunFailedEventDetailsTypeDef",
    "MapRunItemCountsTypeDef",
    "MapRunListItemTypeDef",
    "MapRunRedrivenEventDetailsTypeDef",
    "MapRunStartedEventDetailsTypeDef",
    "MapStateStartedEventDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "PublishStateMachineVersionInputRequestTypeDef",
    "PublishStateMachineVersionOutputTypeDef",
    "RedriveExecutionInputRequestTypeDef",
    "RedriveExecutionOutputTypeDef",
    "ResponseMetadataTypeDef",
    "RoutingConfigurationListItemTypeDef",
    "SendTaskFailureInputRequestTypeDef",
    "SendTaskHeartbeatInputRequestTypeDef",
    "SendTaskSuccessInputRequestTypeDef",
    "StartExecutionInputRequestTypeDef",
    "StartExecutionOutputTypeDef",
    "StartSyncExecutionInputRequestTypeDef",
    "StartSyncExecutionOutputTypeDef",
    "StateEnteredEventDetailsTypeDef",
    "StateExitedEventDetailsTypeDef",
    "StateMachineAliasListItemTypeDef",
    "StateMachineListItemTypeDef",
    "StateMachineVersionListItemTypeDef",
    "StopExecutionInputRequestTypeDef",
    "StopExecutionOutputTypeDef",
    "TagResourceInputRequestTypeDef",
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
    "TestStateInputRequestTypeDef",
    "TestStateOutputTypeDef",
    "TracingConfigurationTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateMapRunInputRequestTypeDef",
    "UpdateStateMachineAliasInputRequestTypeDef",
    "UpdateStateMachineAliasOutputTypeDef",
    "UpdateStateMachineInputRequestTypeDef",
    "UpdateStateMachineOutputTypeDef",
    "ValidateStateMachineDefinitionDiagnosticTypeDef",
    "ValidateStateMachineDefinitionInputRequestTypeDef",
    "ValidateStateMachineDefinitionOutputTypeDef",
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

_RequiredCreateStateMachineAliasInputRequestTypeDef = TypedDict(
    "_RequiredCreateStateMachineAliasInputRequestTypeDef",
    {
        "name": str,
        "routingConfiguration": List["RoutingConfigurationListItemTypeDef"],
    },
)
_OptionalCreateStateMachineAliasInputRequestTypeDef = TypedDict(
    "_OptionalCreateStateMachineAliasInputRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class CreateStateMachineAliasInputRequestTypeDef(
    _RequiredCreateStateMachineAliasInputRequestTypeDef,
    _OptionalCreateStateMachineAliasInputRequestTypeDef,
):
    pass

CreateStateMachineAliasOutputTypeDef = TypedDict(
    "CreateStateMachineAliasOutputTypeDef",
    {
        "stateMachineAliasArn": str,
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
        "publish": bool,
        "versionDescription": str,
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
        "stateMachineVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteActivityInputRequestTypeDef = TypedDict(
    "DeleteActivityInputRequestTypeDef",
    {
        "activityArn": str,
    },
)

DeleteStateMachineAliasInputRequestTypeDef = TypedDict(
    "DeleteStateMachineAliasInputRequestTypeDef",
    {
        "stateMachineAliasArn": str,
    },
)

DeleteStateMachineInputRequestTypeDef = TypedDict(
    "DeleteStateMachineInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)

DeleteStateMachineVersionInputRequestTypeDef = TypedDict(
    "DeleteStateMachineVersionInputRequestTypeDef",
    {
        "stateMachineVersionArn": str,
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
        "mapRunArn": str,
        "error": str,
        "cause": str,
        "stateMachineVersionArn": str,
        "stateMachineAliasArn": str,
        "redriveCount": int,
        "redriveDate": datetime,
        "redriveStatus": ExecutionRedriveStatusType,
        "redriveStatusReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMapRunInputRequestTypeDef = TypedDict(
    "DescribeMapRunInputRequestTypeDef",
    {
        "mapRunArn": str,
    },
)

DescribeMapRunOutputTypeDef = TypedDict(
    "DescribeMapRunOutputTypeDef",
    {
        "mapRunArn": str,
        "executionArn": str,
        "status": MapRunStatusType,
        "startDate": datetime,
        "stopDate": datetime,
        "maxConcurrency": int,
        "toleratedFailurePercentage": float,
        "toleratedFailureCount": int,
        "itemCounts": "MapRunItemCountsTypeDef",
        "executionCounts": "MapRunExecutionCountsTypeDef",
        "redriveCount": int,
        "redriveDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStateMachineAliasInputRequestTypeDef = TypedDict(
    "DescribeStateMachineAliasInputRequestTypeDef",
    {
        "stateMachineAliasArn": str,
    },
)

DescribeStateMachineAliasOutputTypeDef = TypedDict(
    "DescribeStateMachineAliasOutputTypeDef",
    {
        "stateMachineAliasArn": str,
        "name": str,
        "description": str,
        "routingConfiguration": List["RoutingConfigurationListItemTypeDef"],
        "creationDate": datetime,
        "updateDate": datetime,
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
        "mapRunArn": str,
        "label": str,
        "revisionId": str,
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
        "label": str,
        "revisionId": str,
        "description": str,
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
        "mapRunArn": str,
        "itemCount": int,
        "stateMachineVersionArn": str,
        "stateMachineAliasArn": str,
        "redriveCount": int,
        "redriveDate": datetime,
    },
    total=False,
)

class ExecutionListItemTypeDef(
    _RequiredExecutionListItemTypeDef, _OptionalExecutionListItemTypeDef
):
    pass

ExecutionRedrivenEventDetailsTypeDef = TypedDict(
    "ExecutionRedrivenEventDetailsTypeDef",
    {
        "redriveCount": int,
    },
    total=False,
)

ExecutionStartedEventDetailsTypeDef = TypedDict(
    "ExecutionStartedEventDetailsTypeDef",
    {
        "input": str,
        "inputDetails": "HistoryEventExecutionDataDetailsTypeDef",
        "roleArn": str,
        "stateMachineAliasArn": str,
        "stateMachineVersionArn": str,
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
        "executionRedrivenEventDetails": "ExecutionRedrivenEventDetailsTypeDef",
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
        "mapRunStartedEventDetails": "MapRunStartedEventDetailsTypeDef",
        "mapRunFailedEventDetails": "MapRunFailedEventDetailsTypeDef",
        "mapRunRedrivenEventDetails": "MapRunRedrivenEventDetailsTypeDef",
    },
    total=False,
)

class HistoryEventTypeDef(_RequiredHistoryEventTypeDef, _OptionalHistoryEventTypeDef):
    pass

InspectionDataRequestTypeDef = TypedDict(
    "InspectionDataRequestTypeDef",
    {
        "protocol": str,
        "method": str,
        "url": str,
        "headers": str,
        "body": str,
    },
    total=False,
)

InspectionDataResponseTypeDef = TypedDict(
    "InspectionDataResponseTypeDef",
    {
        "protocol": str,
        "statusCode": str,
        "statusMessage": str,
        "headers": str,
        "body": str,
    },
    total=False,
)

InspectionDataTypeDef = TypedDict(
    "InspectionDataTypeDef",
    {
        "input": str,
        "afterInputPath": str,
        "afterParameters": str,
        "result": str,
        "afterResultSelector": str,
        "afterResultPath": str,
        "request": "InspectionDataRequestTypeDef",
        "response": "InspectionDataResponseTypeDef",
    },
    total=False,
)

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
        "taskCredentials": "TaskCredentialsTypeDef",
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

ListExecutionsInputRequestTypeDef = TypedDict(
    "ListExecutionsInputRequestTypeDef",
    {
        "stateMachineArn": str,
        "statusFilter": ExecutionStatusType,
        "maxResults": int,
        "nextToken": str,
        "mapRunArn": str,
        "redriveFilter": ExecutionRedriveFilterType,
    },
    total=False,
)

ListExecutionsOutputTypeDef = TypedDict(
    "ListExecutionsOutputTypeDef",
    {
        "executions": List["ExecutionListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMapRunsInputRequestTypeDef = TypedDict(
    "_RequiredListMapRunsInputRequestTypeDef",
    {
        "executionArn": str,
    },
)
_OptionalListMapRunsInputRequestTypeDef = TypedDict(
    "_OptionalListMapRunsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListMapRunsInputRequestTypeDef(
    _RequiredListMapRunsInputRequestTypeDef, _OptionalListMapRunsInputRequestTypeDef
):
    pass

ListMapRunsOutputTypeDef = TypedDict(
    "ListMapRunsOutputTypeDef",
    {
        "mapRuns": List["MapRunListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStateMachineAliasesInputRequestTypeDef = TypedDict(
    "_RequiredListStateMachineAliasesInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)
_OptionalListStateMachineAliasesInputRequestTypeDef = TypedDict(
    "_OptionalListStateMachineAliasesInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListStateMachineAliasesInputRequestTypeDef(
    _RequiredListStateMachineAliasesInputRequestTypeDef,
    _OptionalListStateMachineAliasesInputRequestTypeDef,
):
    pass

ListStateMachineAliasesOutputTypeDef = TypedDict(
    "ListStateMachineAliasesOutputTypeDef",
    {
        "stateMachineAliases": List["StateMachineAliasListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStateMachineVersionsInputRequestTypeDef = TypedDict(
    "_RequiredListStateMachineVersionsInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)
_OptionalListStateMachineVersionsInputRequestTypeDef = TypedDict(
    "_OptionalListStateMachineVersionsInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListStateMachineVersionsInputRequestTypeDef(
    _RequiredListStateMachineVersionsInputRequestTypeDef,
    _OptionalListStateMachineVersionsInputRequestTypeDef,
):
    pass

ListStateMachineVersionsOutputTypeDef = TypedDict(
    "ListStateMachineVersionsOutputTypeDef",
    {
        "stateMachineVersions": List["StateMachineVersionListItemTypeDef"],
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

_RequiredMapRunExecutionCountsTypeDef = TypedDict(
    "_RequiredMapRunExecutionCountsTypeDef",
    {
        "pending": int,
        "running": int,
        "succeeded": int,
        "failed": int,
        "timedOut": int,
        "aborted": int,
        "total": int,
        "resultsWritten": int,
    },
)
_OptionalMapRunExecutionCountsTypeDef = TypedDict(
    "_OptionalMapRunExecutionCountsTypeDef",
    {
        "failuresNotRedrivable": int,
        "pendingRedrive": int,
    },
    total=False,
)

class MapRunExecutionCountsTypeDef(
    _RequiredMapRunExecutionCountsTypeDef, _OptionalMapRunExecutionCountsTypeDef
):
    pass

MapRunFailedEventDetailsTypeDef = TypedDict(
    "MapRunFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

_RequiredMapRunItemCountsTypeDef = TypedDict(
    "_RequiredMapRunItemCountsTypeDef",
    {
        "pending": int,
        "running": int,
        "succeeded": int,
        "failed": int,
        "timedOut": int,
        "aborted": int,
        "total": int,
        "resultsWritten": int,
    },
)
_OptionalMapRunItemCountsTypeDef = TypedDict(
    "_OptionalMapRunItemCountsTypeDef",
    {
        "failuresNotRedrivable": int,
        "pendingRedrive": int,
    },
    total=False,
)

class MapRunItemCountsTypeDef(_RequiredMapRunItemCountsTypeDef, _OptionalMapRunItemCountsTypeDef):
    pass

_RequiredMapRunListItemTypeDef = TypedDict(
    "_RequiredMapRunListItemTypeDef",
    {
        "executionArn": str,
        "mapRunArn": str,
        "stateMachineArn": str,
        "startDate": datetime,
    },
)
_OptionalMapRunListItemTypeDef = TypedDict(
    "_OptionalMapRunListItemTypeDef",
    {
        "stopDate": datetime,
    },
    total=False,
)

class MapRunListItemTypeDef(_RequiredMapRunListItemTypeDef, _OptionalMapRunListItemTypeDef):
    pass

MapRunRedrivenEventDetailsTypeDef = TypedDict(
    "MapRunRedrivenEventDetailsTypeDef",
    {
        "mapRunArn": str,
        "redriveCount": int,
    },
    total=False,
)

MapRunStartedEventDetailsTypeDef = TypedDict(
    "MapRunStartedEventDetailsTypeDef",
    {
        "mapRunArn": str,
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

_RequiredPublishStateMachineVersionInputRequestTypeDef = TypedDict(
    "_RequiredPublishStateMachineVersionInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)
_OptionalPublishStateMachineVersionInputRequestTypeDef = TypedDict(
    "_OptionalPublishStateMachineVersionInputRequestTypeDef",
    {
        "revisionId": str,
        "description": str,
    },
    total=False,
)

class PublishStateMachineVersionInputRequestTypeDef(
    _RequiredPublishStateMachineVersionInputRequestTypeDef,
    _OptionalPublishStateMachineVersionInputRequestTypeDef,
):
    pass

PublishStateMachineVersionOutputTypeDef = TypedDict(
    "PublishStateMachineVersionOutputTypeDef",
    {
        "creationDate": datetime,
        "stateMachineVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRedriveExecutionInputRequestTypeDef = TypedDict(
    "_RequiredRedriveExecutionInputRequestTypeDef",
    {
        "executionArn": str,
    },
)
_OptionalRedriveExecutionInputRequestTypeDef = TypedDict(
    "_OptionalRedriveExecutionInputRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class RedriveExecutionInputRequestTypeDef(
    _RequiredRedriveExecutionInputRequestTypeDef, _OptionalRedriveExecutionInputRequestTypeDef
):
    pass

RedriveExecutionOutputTypeDef = TypedDict(
    "RedriveExecutionOutputTypeDef",
    {
        "redriveDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

RoutingConfigurationListItemTypeDef = TypedDict(
    "RoutingConfigurationListItemTypeDef",
    {
        "stateMachineVersionArn": str,
        "weight": int,
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

StateMachineAliasListItemTypeDef = TypedDict(
    "StateMachineAliasListItemTypeDef",
    {
        "stateMachineAliasArn": str,
        "creationDate": datetime,
    },
)

StateMachineListItemTypeDef = TypedDict(
    "StateMachineListItemTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "type": StateMachineTypeType,
        "creationDate": datetime,
    },
)

StateMachineVersionListItemTypeDef = TypedDict(
    "StateMachineVersionListItemTypeDef",
    {
        "stateMachineVersionArn": str,
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

TaskCredentialsTypeDef = TypedDict(
    "TaskCredentialsTypeDef",
    {
        "roleArn": str,
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
        "taskCredentials": "TaskCredentialsTypeDef",
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

_RequiredTestStateInputRequestTypeDef = TypedDict(
    "_RequiredTestStateInputRequestTypeDef",
    {
        "definition": str,
        "roleArn": str,
    },
)
_OptionalTestStateInputRequestTypeDef = TypedDict(
    "_OptionalTestStateInputRequestTypeDef",
    {
        "input": str,
        "inspectionLevel": InspectionLevelType,
        "revealSecrets": bool,
    },
    total=False,
)

class TestStateInputRequestTypeDef(
    _RequiredTestStateInputRequestTypeDef, _OptionalTestStateInputRequestTypeDef
):
    pass

TestStateOutputTypeDef = TypedDict(
    "TestStateOutputTypeDef",
    {
        "output": str,
        "error": str,
        "cause": str,
        "inspectionData": "InspectionDataTypeDef",
        "nextState": str,
        "status": TestExecutionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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

_RequiredUpdateMapRunInputRequestTypeDef = TypedDict(
    "_RequiredUpdateMapRunInputRequestTypeDef",
    {
        "mapRunArn": str,
    },
)
_OptionalUpdateMapRunInputRequestTypeDef = TypedDict(
    "_OptionalUpdateMapRunInputRequestTypeDef",
    {
        "maxConcurrency": int,
        "toleratedFailurePercentage": float,
        "toleratedFailureCount": int,
    },
    total=False,
)

class UpdateMapRunInputRequestTypeDef(
    _RequiredUpdateMapRunInputRequestTypeDef, _OptionalUpdateMapRunInputRequestTypeDef
):
    pass

_RequiredUpdateStateMachineAliasInputRequestTypeDef = TypedDict(
    "_RequiredUpdateStateMachineAliasInputRequestTypeDef",
    {
        "stateMachineAliasArn": str,
    },
)
_OptionalUpdateStateMachineAliasInputRequestTypeDef = TypedDict(
    "_OptionalUpdateStateMachineAliasInputRequestTypeDef",
    {
        "description": str,
        "routingConfiguration": List["RoutingConfigurationListItemTypeDef"],
    },
    total=False,
)

class UpdateStateMachineAliasInputRequestTypeDef(
    _RequiredUpdateStateMachineAliasInputRequestTypeDef,
    _OptionalUpdateStateMachineAliasInputRequestTypeDef,
):
    pass

UpdateStateMachineAliasOutputTypeDef = TypedDict(
    "UpdateStateMachineAliasOutputTypeDef",
    {
        "updateDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "publish": bool,
        "versionDescription": str,
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
        "revisionId": str,
        "stateMachineVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredValidateStateMachineDefinitionDiagnosticTypeDef = TypedDict(
    "_RequiredValidateStateMachineDefinitionDiagnosticTypeDef",
    {
        "severity": Literal["ERROR"],
        "code": str,
        "message": str,
    },
)
_OptionalValidateStateMachineDefinitionDiagnosticTypeDef = TypedDict(
    "_OptionalValidateStateMachineDefinitionDiagnosticTypeDef",
    {
        "location": str,
    },
    total=False,
)

class ValidateStateMachineDefinitionDiagnosticTypeDef(
    _RequiredValidateStateMachineDefinitionDiagnosticTypeDef,
    _OptionalValidateStateMachineDefinitionDiagnosticTypeDef,
):
    pass

_RequiredValidateStateMachineDefinitionInputRequestTypeDef = TypedDict(
    "_RequiredValidateStateMachineDefinitionInputRequestTypeDef",
    {
        "definition": str,
    },
)
_OptionalValidateStateMachineDefinitionInputRequestTypeDef = TypedDict(
    "_OptionalValidateStateMachineDefinitionInputRequestTypeDef",
    {
        "type": StateMachineTypeType,
    },
    total=False,
)

class ValidateStateMachineDefinitionInputRequestTypeDef(
    _RequiredValidateStateMachineDefinitionInputRequestTypeDef,
    _OptionalValidateStateMachineDefinitionInputRequestTypeDef,
):
    pass

ValidateStateMachineDefinitionOutputTypeDef = TypedDict(
    "ValidateStateMachineDefinitionOutputTypeDef",
    {
        "result": ValidateStateMachineDefinitionResultCodeType,
        "diagnostics": List["ValidateStateMachineDefinitionDiagnosticTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
