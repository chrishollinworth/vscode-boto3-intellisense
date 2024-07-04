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

from .literals import (
    ExecutionRedriveFilterType,
    ExecutionStatusType,
    InspectionLevelType,
    StateMachineTypeType,
)
from .paginator import (
    GetExecutionHistoryPaginator,
    ListActivitiesPaginator,
    ListExecutionsPaginator,
    ListMapRunsPaginator,
    ListStateMachinesPaginator,
)
from .type_defs import (
    CreateActivityOutputTypeDef,
    CreateStateMachineAliasOutputTypeDef,
    CreateStateMachineOutputTypeDef,
    DescribeActivityOutputTypeDef,
    DescribeExecutionOutputTypeDef,
    DescribeMapRunOutputTypeDef,
    DescribeStateMachineAliasOutputTypeDef,
    DescribeStateMachineForExecutionOutputTypeDef,
    DescribeStateMachineOutputTypeDef,
    GetActivityTaskOutputTypeDef,
    GetExecutionHistoryOutputTypeDef,
    ListActivitiesOutputTypeDef,
    ListExecutionsOutputTypeDef,
    ListMapRunsOutputTypeDef,
    ListStateMachineAliasesOutputTypeDef,
    ListStateMachinesOutputTypeDef,
    ListStateMachineVersionsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    LoggingConfigurationTypeDef,
    PublishStateMachineVersionOutputTypeDef,
    RedriveExecutionOutputTypeDef,
    RoutingConfigurationListItemTypeDef,
    StartExecutionOutputTypeDef,
    StartSyncExecutionOutputTypeDef,
    StopExecutionOutputTypeDef,
    TagTypeDef,
    TestStateOutputTypeDef,
    TracingConfigurationTypeDef,
    UpdateStateMachineAliasOutputTypeDef,
    UpdateStateMachineOutputTypeDef,
    ValidateStateMachineDefinitionOutputTypeDef,
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
    ConflictException: Type[BotocoreClientError]
    ExecutionAlreadyExists: Type[BotocoreClientError]
    ExecutionDoesNotExist: Type[BotocoreClientError]
    ExecutionLimitExceeded: Type[BotocoreClientError]
    ExecutionNotRedrivable: Type[BotocoreClientError]
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
    ServiceQuotaExceededException: Type[BotocoreClientError]
    StateMachineAlreadyExists: Type[BotocoreClientError]
    StateMachineDeleting: Type[BotocoreClientError]
    StateMachineDoesNotExist: Type[BotocoreClientError]
    StateMachineLimitExceeded: Type[BotocoreClientError]
    StateMachineTypeNotSupported: Type[BotocoreClientError]
    TaskDoesNotExist: Type[BotocoreClientError]
    TaskTimedOut: Type[BotocoreClientError]
    TooManyTags: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class SFNClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#close)
        """

    def create_activity(
        self, *, name: str, tags: List["TagTypeDef"] = None
    ) -> CreateActivityOutputTypeDef:
        """
        Creates an activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.create_activity)
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
        tracingConfiguration: "TracingConfigurationTypeDef" = None,
        publish: bool = None,
        versionDescription: str = None
    ) -> CreateStateMachineOutputTypeDef:
        """
        Creates a state machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.create_state_machine)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#create_state_machine)
        """

    def create_state_machine_alias(
        self,
        *,
        name: str,
        routingConfiguration: List["RoutingConfigurationListItemTypeDef"],
        description: str = None
    ) -> CreateStateMachineAliasOutputTypeDef:
        """
        Creates an `alias <https://docs.aws.amazon.com/step-
        functions/latest/dg/concepts-state-machine-alias.html>`__ for a state machine
        that points to one or two `versions <https://docs.aws.amazon.com/step-
        functions/latest/dg/concepts-state-machine-version.html>`__ of the same state
        machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.create_state_machine_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#create_state_machine_alias)
        """

    def delete_activity(self, *, activityArn: str) -> Dict[str, Any]:
        """
        Deletes an activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.delete_activity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#delete_activity)
        """

    def delete_state_machine(self, *, stateMachineArn: str) -> Dict[str, Any]:
        """
        Deletes a state machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.delete_state_machine)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#delete_state_machine)
        """

    def delete_state_machine_alias(self, *, stateMachineAliasArn: str) -> Dict[str, Any]:
        """
        Deletes a state machine `alias <https://docs.aws.amazon.com/step-
        functions/latest/dg/concepts-state-machine-alias.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.delete_state_machine_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#delete_state_machine_alias)
        """

    def delete_state_machine_version(self, *, stateMachineVersionArn: str) -> Dict[str, Any]:
        """
        Deletes a state machine `version <https://docs.aws.amazon.com/step-
        functions/latest/dg/concepts-state-machine-version.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.delete_state_machine_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#delete_state_machine_version)
        """

    def describe_activity(self, *, activityArn: str) -> DescribeActivityOutputTypeDef:
        """
        Describes an activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.describe_activity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#describe_activity)
        """

    def describe_execution(self, *, executionArn: str) -> DescribeExecutionOutputTypeDef:
        """
        Provides information about a state machine execution, such as the state machine
        associated with the execution, the execution input and output, and relevant
        execution metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.describe_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#describe_execution)
        """

    def describe_map_run(self, *, mapRunArn: str) -> DescribeMapRunOutputTypeDef:
        """
        Provides information about a Map Run's configuration, progress, and results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.describe_map_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#describe_map_run)
        """

    def describe_state_machine(self, *, stateMachineArn: str) -> DescribeStateMachineOutputTypeDef:
        """
        Provides information about a state machine's definition, its IAM role Amazon
        Resource Name (ARN), and configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.describe_state_machine)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#describe_state_machine)
        """

    def describe_state_machine_alias(
        self, *, stateMachineAliasArn: str
    ) -> DescribeStateMachineAliasOutputTypeDef:
        """
        Returns details about a state machine `alias <https://docs.aws.amazon.com/step-
        functions/latest/dg/concepts-state-machine-alias.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.describe_state_machine_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#describe_state_machine_alias)
        """

    def describe_state_machine_for_execution(
        self, *, executionArn: str
    ) -> DescribeStateMachineForExecutionOutputTypeDef:
        """
        Provides information about a state machine's definition, its execution role ARN,
        and configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.describe_state_machine_for_execution)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#generate_presigned_url)
        """

    def get_activity_task(
        self, *, activityArn: str, workerName: str = None
    ) -> GetActivityTaskOutputTypeDef:
        """
        Used by workers to retrieve a task (with the specified activity ARN) which has
        been scheduled for execution by a running state machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.get_activity_task)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.get_execution_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#get_execution_history)
        """

    def list_activities(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListActivitiesOutputTypeDef:
        """
        Lists the existing activities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.list_activities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#list_activities)
        """

    def list_executions(
        self,
        *,
        stateMachineArn: str = None,
        statusFilter: ExecutionStatusType = None,
        maxResults: int = None,
        nextToken: str = None,
        mapRunArn: str = None,
        redriveFilter: ExecutionRedriveFilterType = None
    ) -> ListExecutionsOutputTypeDef:
        """
        Lists all executions of a state machine or a Map Run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.list_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#list_executions)
        """

    def list_map_runs(
        self, *, executionArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListMapRunsOutputTypeDef:
        """
        Lists all Map Runs that were started by a given state machine execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.list_map_runs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#list_map_runs)
        """

    def list_state_machine_aliases(
        self, *, stateMachineArn: str, nextToken: str = None, maxResults: int = None
    ) -> ListStateMachineAliasesOutputTypeDef:
        """
        Lists `aliases <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-
        state-machine-alias.html>`__ for a specified state machine ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.list_state_machine_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#list_state_machine_aliases)
        """

    def list_state_machine_versions(
        self, *, stateMachineArn: str, nextToken: str = None, maxResults: int = None
    ) -> ListStateMachineVersionsOutputTypeDef:
        """
        Lists `versions <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-
        state-machine-version.html>`__ for the specified state machine Amazon Resource
        Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.list_state_machine_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#list_state_machine_versions)
        """

    def list_state_machines(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListStateMachinesOutputTypeDef:
        """
        Lists the existing state machines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.list_state_machines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#list_state_machines)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        List tags for a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#list_tags_for_resource)
        """

    def publish_state_machine_version(
        self, *, stateMachineArn: str, revisionId: str = None, description: str = None
    ) -> PublishStateMachineVersionOutputTypeDef:
        """
        Creates a `version <https://docs.aws.amazon.com/step-
        functions/latest/dg/concepts-state-machine-version.html>`__ from the current
        revision of a state machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.publish_state_machine_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#publish_state_machine_version)
        """

    def redrive_execution(
        self, *, executionArn: str, clientToken: str = None
    ) -> RedriveExecutionOutputTypeDef:
        """
        Restarts unsuccessful executions of Standard workflows that didn't complete
        successfully in the last 14 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.redrive_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#redrive_execution)
        """

    def send_task_failure(
        self, *, taskToken: str, error: str = None, cause: str = None
    ) -> Dict[str, Any]:
        """
        Used by activity workers, Task states using the `callback
        <https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-
        resource.html#connect-wait-token>`__ pattern, and optionally Task states using
        the `job run <https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-
        resource.html#con...`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.send_task_failure)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#send_task_failure)
        """

    def send_task_heartbeat(self, *, taskToken: str) -> Dict[str, Any]:
        """
        Used by activity workers and Task states using the `callback
        <https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-
        resource.html#connect-wait-token>`__ pattern, and optionally Task states using
        the `job run <https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-
        resource.html#...`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.send_task_heartbeat)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#send_task_heartbeat)
        """

    def send_task_success(self, *, taskToken: str, output: str) -> Dict[str, Any]:
        """
        Used by activity workers, Task states using the `callback
        <https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-
        resource.html#connect-wait-token>`__ pattern, and optionally Task states using
        the `job run <https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-
        resource.html#con...`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.send_task_success)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#send_task_success)
        """

    def start_execution(
        self, *, stateMachineArn: str, name: str = None, input: str = None, traceHeader: str = None
    ) -> StartExecutionOutputTypeDef:
        """
        Starts a state machine execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.start_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#start_execution)
        """

    def start_sync_execution(
        self, *, stateMachineArn: str, name: str = None, input: str = None, traceHeader: str = None
    ) -> StartSyncExecutionOutputTypeDef:
        """
        Starts a Synchronous Express state machine execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.start_sync_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#start_sync_execution)
        """

    def stop_execution(
        self, *, executionArn: str, error: str = None, cause: str = None
    ) -> StopExecutionOutputTypeDef:
        """
        Stops an execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.stop_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#stop_execution)
        """

    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Add a tag to a Step Functions resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#tag_resource)
        """

    def test_state(
        self,
        *,
        definition: str,
        roleArn: str,
        input: str = None,
        inspectionLevel: InspectionLevelType = None,
        revealSecrets: bool = None
    ) -> TestStateOutputTypeDef:
        """
        Accepts the definition of a single state and executes it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.test_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#test_state)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Remove a tag from a Step Functions resource See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/UntagResource>`_
        **Request Syntax** response = client.untag_resource( resourceArn='string',
        tagKeys=[ 'string', ] ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#untag_resource)
        """

    def update_map_run(
        self,
        *,
        mapRunArn: str,
        maxConcurrency: int = None,
        toleratedFailurePercentage: float = None,
        toleratedFailureCount: int = None
    ) -> Dict[str, Any]:
        """
        Updates an in-progress Map Run's configuration to include changes to the
        settings that control maximum concurrency and Map Run failure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.update_map_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#update_map_run)
        """

    def update_state_machine(
        self,
        *,
        stateMachineArn: str,
        definition: str = None,
        roleArn: str = None,
        loggingConfiguration: "LoggingConfigurationTypeDef" = None,
        tracingConfiguration: "TracingConfigurationTypeDef" = None,
        publish: bool = None,
        versionDescription: str = None
    ) -> UpdateStateMachineOutputTypeDef:
        """
        Updates an existing state machine by modifying its `definition`, `roleArn`, or
        `loggingConfiguration`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.update_state_machine)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#update_state_machine)
        """

    def update_state_machine_alias(
        self,
        *,
        stateMachineAliasArn: str,
        description: str = None,
        routingConfiguration: List["RoutingConfigurationListItemTypeDef"] = None
    ) -> UpdateStateMachineAliasOutputTypeDef:
        """
        Updates the configuration of an existing state machine `alias
        <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-
        alias.html>`__ by modifying its `description` or `routingConfiguration`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.update_state_machine_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#update_state_machine_alias)
        """

    def validate_state_machine_definition(
        self, *, definition: str, type: StateMachineTypeType = None
    ) -> ValidateStateMachineDefinitionOutputTypeDef:
        """
        Validates the syntax of a state machine definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Client.validate_state_machine_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client.html#validate_state_machine_definition)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_execution_history"]
    ) -> GetExecutionHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Paginator.GetExecutionHistory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html#getexecutionhistorypaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_activities"]) -> ListActivitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Paginator.ListActivities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html#listactivitiespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_executions"]) -> ListExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Paginator.ListExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html#listexecutionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_map_runs"]) -> ListMapRunsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Paginator.ListMapRuns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html#listmaprunspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_state_machines"]
    ) -> ListStateMachinesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/stepfunctions.html#SFN.Paginator.ListStateMachines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/paginators.html#liststatemachinespaginator)
        """
