"""
Type annotations for stepfunctions service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_stepfunctions import SFNClient

    client: SFNClient = boto3.client("stepfunctions")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ExecutionStatusType, StateMachineTypeType
from .paginator import (
    GetExecutionHistoryPaginator,
    ListActivitiesPaginator,
    ListExecutionsPaginator,
    ListStateMachinesPaginator,
)
from .type_defs import (
    CreateActivityOutputTypeDef,
    CreateStateMachineOutputTypeDef,
    DescribeActivityOutputTypeDef,
    DescribeExecutionOutputTypeDef,
    DescribeStateMachineForExecutionOutputTypeDef,
    DescribeStateMachineOutputTypeDef,
    GetActivityTaskOutputTypeDef,
    GetExecutionHistoryOutputTypeDef,
    ListActivitiesOutputTypeDef,
    ListExecutionsOutputTypeDef,
    ListStateMachinesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    LoggingConfigurationTypeDef,
    StartExecutionOutputTypeDef,
    StartSyncExecutionOutputTypeDef,
    StopExecutionOutputTypeDef,
    TagTypeDef,
    TracingConfigurationTypeDef,
    UpdateStateMachineOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("SFNClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ActivityDoesNotExist: Type[BotocoreClientError]
    ActivityLimitExceeded: Type[BotocoreClientError]
    ActivityWorkerLimitExceeded: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ExecutionAlreadyExists: Type[BotocoreClientError]
    ExecutionDoesNotExist: Type[BotocoreClientError]
    ExecutionLimitExceeded: Type[BotocoreClientError]
    InvalidArn: Type[BotocoreClientError]
    InvalidDefinition: Type[BotocoreClientError]
    InvalidExecutionInput: Type[BotocoreClientError]
    InvalidLoggingConfiguration: Type[BotocoreClientError]
    InvalidName: Type[BotocoreClientError]
    InvalidOutput: Type[BotocoreClientError]
    InvalidToken: Type[BotocoreClientError]
    InvalidTracingConfiguration: Type[BotocoreClientError]
    MissingRequiredParameter: Type[BotocoreClientError]
    ResourceNotFound: Type[BotocoreClientError]
    StateMachineAlreadyExists: Type[BotocoreClientError]
    StateMachineDeleting: Type[BotocoreClientError]
    StateMachineDoesNotExist: Type[BotocoreClientError]
    StateMachineLimitExceeded: Type[BotocoreClientError]
    StateMachineTypeNotSupported: Type[BotocoreClientError]
    TaskDoesNotExist: Type[BotocoreClientError]
    TaskTimedOut: Type[BotocoreClientError]
    TooManyTags: Type[BotocoreClientError]

class SFNClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SFNClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#can_paginate)
        """
    def create_activity(
        self, *, name: str, tags: List["TagTypeDef"] = None
    ) -> CreateActivityOutputTypeDef:
        """
        Creates an activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.create_activity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#create_activity)
        """
    def create_state_machine(
        self,
        *,
        name: str,
        definition: str,
        roleArn: str,
        type: StateMachineTypeType = None,
        loggingConfiguration: "LoggingConfigurationTypeDef" = None,
        tags: List["TagTypeDef"] = None,
        tracingConfiguration: "TracingConfigurationTypeDef" = None
    ) -> CreateStateMachineOutputTypeDef:
        """
        Creates a state machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.create_state_machine)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#create_state_machine)
        """
    def delete_activity(self, *, activityArn: str) -> Dict[str, Any]:
        """
        Deletes an activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.delete_activity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#delete_activity)
        """
    def delete_state_machine(self, *, stateMachineArn: str) -> Dict[str, Any]:
        """
        Deletes a state machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.delete_state_machine)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#delete_state_machine)
        """
    def describe_activity(self, *, activityArn: str) -> DescribeActivityOutputTypeDef:
        """
        Describes an activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.describe_activity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#describe_activity)
        """
    def describe_execution(self, *, executionArn: str) -> DescribeExecutionOutputTypeDef:
        """
        Describes an execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.describe_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#describe_execution)
        """
    def describe_state_machine(self, *, stateMachineArn: str) -> DescribeStateMachineOutputTypeDef:
        """
        Describes a state machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.describe_state_machine)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#describe_state_machine)
        """
    def describe_state_machine_for_execution(
        self, *, executionArn: str
    ) -> DescribeStateMachineForExecutionOutputTypeDef:
        """
        Describes the state machine associated with a specific execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.describe_state_machine_for_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#describe_state_machine_for_execution)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#generate_presigned_url)
        """
    def get_activity_task(
        self, *, activityArn: str, workerName: str = None
    ) -> GetActivityTaskOutputTypeDef:
        """
        Used by workers to retrieve a task (with the specified activity ARN) which has
        been scheduled for execution by a running state machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.get_activity_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#get_activity_task)
        """
    def get_execution_history(
        self,
        *,
        executionArn: str,
        maxResults: int = None,
        reverseOrder: bool = None,
        nextToken: str = None,
        includeExecutionData: bool = None
    ) -> GetExecutionHistoryOutputTypeDef:
        """
        Returns the history of the specified execution as a list of events.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.get_execution_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#get_execution_history)
        """
    def list_activities(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListActivitiesOutputTypeDef:
        """
        Lists the existing activities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.list_activities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#list_activities)
        """
    def list_executions(
        self,
        *,
        stateMachineArn: str,
        statusFilter: ExecutionStatusType = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListExecutionsOutputTypeDef:
        """
        Lists the executions of a state machine that meet the filtering criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.list_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#list_executions)
        """
    def list_state_machines(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListStateMachinesOutputTypeDef:
        """
        Lists the existing state machines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.list_state_machines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#list_state_machines)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        List tags for a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#list_tags_for_resource)
        """
    def send_task_failure(
        self, *, taskToken: str, error: str = None, cause: str = None
    ) -> Dict[str, Any]:
        """
        Used by activity workers and task states using the `callback
        <https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-
        resource.html#connect-wait-token>`__ pattern to report that the task identified
        by the `taskToken` failed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.send_task_failure)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#send_task_failure)
        """
    def send_task_heartbeat(self, *, taskToken: str) -> Dict[str, Any]:
        """
        Used by activity workers and task states using the `callback
        <https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-
        resource.html#connect-wait-token>`__ pattern to report to Step Functions that
        the task represented by the specified `taskToken` is still making progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.send_task_heartbeat)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#send_task_heartbeat)
        """
    def send_task_success(self, *, taskToken: str, output: str) -> Dict[str, Any]:
        """
        Used by activity workers and task states using the `callback
        <https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-
        resource.html#connect-wait-token>`__ pattern to report that the task identified
        by the `taskToken` completed successfully.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.send_task_success)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#send_task_success)
        """
    def start_execution(
        self, *, stateMachineArn: str, name: str = None, input: str = None, traceHeader: str = None
    ) -> StartExecutionOutputTypeDef:
        """
        Starts a state machine execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.start_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#start_execution)
        """
    def start_sync_execution(
        self, *, stateMachineArn: str, name: str = None, input: str = None, traceHeader: str = None
    ) -> StartSyncExecutionOutputTypeDef:
        """
        Starts a Synchronous Express state machine execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.start_sync_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#start_sync_execution)
        """
    def stop_execution(
        self, *, executionArn: str, error: str = None, cause: str = None
    ) -> StopExecutionOutputTypeDef:
        """
        Stops an execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.stop_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#stop_execution)
        """
    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Add a tag to a Step Functions resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Remove a tag from a Step Functions resource See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/UntagResource>`_
        **Request Syntax** response = client.untag_resource( resourceArn='string',
        tagKeys=[ 'string', ] ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#untag_resource)
        """
    def update_state_machine(
        self,
        *,
        stateMachineArn: str,
        definition: str = None,
        roleArn: str = None,
        loggingConfiguration: "LoggingConfigurationTypeDef" = None,
        tracingConfiguration: "TracingConfigurationTypeDef" = None
    ) -> UpdateStateMachineOutputTypeDef:
        """
        Updates an existing state machine by modifying its `definition` , `roleArn` , or
        `loggingConfiguration`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Client.update_state_machine)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#update_state_machine)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_execution_history"]
    ) -> GetExecutionHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Paginator.GetExecutionHistory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html#getexecutionhistorypaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_activities"]) -> ListActivitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Paginator.ListActivities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html#listactivitiespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_executions"]) -> ListExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Paginator.ListExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html#listexecutionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_state_machines"]
    ) -> ListStateMachinesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/stepfunctions.html#SFN.Paginator.ListStateMachines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html#liststatemachinespaginator)
        """
