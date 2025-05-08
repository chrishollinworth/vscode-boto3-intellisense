"""
Type annotations for stepfunctions service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_stepfunctions.client import SFNClient

    session = Session()
    client: SFNClient = session.client("stepfunctions")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    GetExecutionHistoryPaginator,
    ListActivitiesPaginator,
    ListExecutionsPaginator,
    ListMapRunsPaginator,
    ListStateMachinesPaginator,
)
from .type_defs import (
    CreateActivityInputTypeDef,
    CreateActivityOutputTypeDef,
    CreateStateMachineAliasInputTypeDef,
    CreateStateMachineAliasOutputTypeDef,
    CreateStateMachineInputTypeDef,
    CreateStateMachineOutputTypeDef,
    DeleteActivityInputTypeDef,
    DeleteStateMachineAliasInputTypeDef,
    DeleteStateMachineInputTypeDef,
    DeleteStateMachineVersionInputTypeDef,
    DescribeActivityInputTypeDef,
    DescribeActivityOutputTypeDef,
    DescribeExecutionInputTypeDef,
    DescribeExecutionOutputTypeDef,
    DescribeMapRunInputTypeDef,
    DescribeMapRunOutputTypeDef,
    DescribeStateMachineAliasInputTypeDef,
    DescribeStateMachineAliasOutputTypeDef,
    DescribeStateMachineForExecutionInputTypeDef,
    DescribeStateMachineForExecutionOutputTypeDef,
    DescribeStateMachineInputTypeDef,
    DescribeStateMachineOutputTypeDef,
    GetActivityTaskInputTypeDef,
    GetActivityTaskOutputTypeDef,
    GetExecutionHistoryInputTypeDef,
    GetExecutionHistoryOutputTypeDef,
    ListActivitiesInputTypeDef,
    ListActivitiesOutputTypeDef,
    ListExecutionsInputTypeDef,
    ListExecutionsOutputTypeDef,
    ListMapRunsInputTypeDef,
    ListMapRunsOutputTypeDef,
    ListStateMachineAliasesInputTypeDef,
    ListStateMachineAliasesOutputTypeDef,
    ListStateMachinesInputTypeDef,
    ListStateMachinesOutputTypeDef,
    ListStateMachineVersionsInputTypeDef,
    ListStateMachineVersionsOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    PublishStateMachineVersionInputTypeDef,
    PublishStateMachineVersionOutputTypeDef,
    RedriveExecutionInputTypeDef,
    RedriveExecutionOutputTypeDef,
    SendTaskFailureInputTypeDef,
    SendTaskHeartbeatInputTypeDef,
    SendTaskSuccessInputTypeDef,
    StartExecutionInputTypeDef,
    StartExecutionOutputTypeDef,
    StartSyncExecutionInputTypeDef,
    StartSyncExecutionOutputTypeDef,
    StopExecutionInputTypeDef,
    StopExecutionOutputTypeDef,
    TagResourceInputTypeDef,
    TestStateInputTypeDef,
    TestStateOutputTypeDef,
    UntagResourceInputTypeDef,
    UpdateMapRunInputTypeDef,
    UpdateStateMachineAliasInputTypeDef,
    UpdateStateMachineAliasOutputTypeDef,
    UpdateStateMachineInputTypeDef,
    UpdateStateMachineOutputTypeDef,
    ValidateStateMachineDefinitionInputTypeDef,
    ValidateStateMachineDefinitionOutputTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("SFNClient",)

class Exceptions(BaseClientExceptions):
    ActivityAlreadyExists: Type[BotocoreClientError]
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
    InvalidEncryptionConfiguration: Type[BotocoreClientError]
    InvalidExecutionInput: Type[BotocoreClientError]
    InvalidLoggingConfiguration: Type[BotocoreClientError]
    InvalidName: Type[BotocoreClientError]
    InvalidOutput: Type[BotocoreClientError]
    InvalidToken: Type[BotocoreClientError]
    InvalidTracingConfiguration: Type[BotocoreClientError]
    KmsAccessDeniedException: Type[BotocoreClientError]
    KmsInvalidStateException: Type[BotocoreClientError]
    KmsThrottlingException: Type[BotocoreClientError]
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SFNClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#generate_presigned_url)
        """

    def create_activity(
        self, **kwargs: Unpack[CreateActivityInputTypeDef]
    ) -> CreateActivityOutputTypeDef:
        """
        Creates an activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/create_activity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#create_activity)
        """

    def create_state_machine(
        self, **kwargs: Unpack[CreateStateMachineInputTypeDef]
    ) -> CreateStateMachineOutputTypeDef:
        """
        Creates a state machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/create_state_machine.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#create_state_machine)
        """

    def create_state_machine_alias(
        self, **kwargs: Unpack[CreateStateMachineAliasInputTypeDef]
    ) -> CreateStateMachineAliasOutputTypeDef:
        """
        Creates an <a
        href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html">alias</a>
        for a state machine that points to one or two <a
        href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html">versions</a>
        of the same state mac...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/create_state_machine_alias.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#create_state_machine_alias)
        """

    def delete_activity(self, **kwargs: Unpack[DeleteActivityInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes an activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/delete_activity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#delete_activity)
        """

    def delete_state_machine(
        self, **kwargs: Unpack[DeleteStateMachineInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a state machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/delete_state_machine.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#delete_state_machine)
        """

    def delete_state_machine_alias(
        self, **kwargs: Unpack[DeleteStateMachineAliasInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a state machine <a
        href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html">alias</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/delete_state_machine_alias.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#delete_state_machine_alias)
        """

    def delete_state_machine_version(
        self, **kwargs: Unpack[DeleteStateMachineVersionInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a state machine <a
        href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html">version</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/delete_state_machine_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#delete_state_machine_version)
        """

    def describe_activity(
        self, **kwargs: Unpack[DescribeActivityInputTypeDef]
    ) -> DescribeActivityOutputTypeDef:
        """
        Describes an activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/describe_activity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#describe_activity)
        """

    def describe_execution(
        self, **kwargs: Unpack[DescribeExecutionInputTypeDef]
    ) -> DescribeExecutionOutputTypeDef:
        """
        Provides information about a state machine execution, such as the state machine
        associated with the execution, the execution input and output, and relevant
        execution metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/describe_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#describe_execution)
        """

    def describe_map_run(
        self, **kwargs: Unpack[DescribeMapRunInputTypeDef]
    ) -> DescribeMapRunOutputTypeDef:
        """
        Provides information about a Map Run's configuration, progress, and results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/describe_map_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#describe_map_run)
        """

    def describe_state_machine(
        self, **kwargs: Unpack[DescribeStateMachineInputTypeDef]
    ) -> DescribeStateMachineOutputTypeDef:
        """
        Provides information about a state machine's definition, its IAM role Amazon
        Resource Name (ARN), and configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/describe_state_machine.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#describe_state_machine)
        """

    def describe_state_machine_alias(
        self, **kwargs: Unpack[DescribeStateMachineAliasInputTypeDef]
    ) -> DescribeStateMachineAliasOutputTypeDef:
        """
        Returns details about a state machine <a
        href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html">alias</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/describe_state_machine_alias.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#describe_state_machine_alias)
        """

    def describe_state_machine_for_execution(
        self, **kwargs: Unpack[DescribeStateMachineForExecutionInputTypeDef]
    ) -> DescribeStateMachineForExecutionOutputTypeDef:
        """
        Provides information about a state machine's definition, its execution role
        ARN, and configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/describe_state_machine_for_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#describe_state_machine_for_execution)
        """

    def get_activity_task(
        self, **kwargs: Unpack[GetActivityTaskInputTypeDef]
    ) -> GetActivityTaskOutputTypeDef:
        """
        Used by workers to retrieve a task (with the specified activity ARN) which has
        been scheduled for execution by a running state machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/get_activity_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#get_activity_task)
        """

    def get_execution_history(
        self, **kwargs: Unpack[GetExecutionHistoryInputTypeDef]
    ) -> GetExecutionHistoryOutputTypeDef:
        """
        Returns the history of the specified execution as a list of events.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/get_execution_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#get_execution_history)
        """

    def list_activities(
        self, **kwargs: Unpack[ListActivitiesInputTypeDef]
    ) -> ListActivitiesOutputTypeDef:
        """
        Lists the existing activities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/list_activities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#list_activities)
        """

    def list_executions(
        self, **kwargs: Unpack[ListExecutionsInputTypeDef]
    ) -> ListExecutionsOutputTypeDef:
        """
        Lists all executions of a state machine or a Map Run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/list_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#list_executions)
        """

    def list_map_runs(self, **kwargs: Unpack[ListMapRunsInputTypeDef]) -> ListMapRunsOutputTypeDef:
        """
        Lists all Map Runs that were started by a given state machine execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/list_map_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#list_map_runs)
        """

    def list_state_machine_aliases(
        self, **kwargs: Unpack[ListStateMachineAliasesInputTypeDef]
    ) -> ListStateMachineAliasesOutputTypeDef:
        """
        Lists <a
        href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html">aliases</a>
        for a specified state machine ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/list_state_machine_aliases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#list_state_machine_aliases)
        """

    def list_state_machine_versions(
        self, **kwargs: Unpack[ListStateMachineVersionsInputTypeDef]
    ) -> ListStateMachineVersionsOutputTypeDef:
        """
        Lists <a
        href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html">versions</a>
        for the specified state machine Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/list_state_machine_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#list_state_machine_versions)
        """

    def list_state_machines(
        self, **kwargs: Unpack[ListStateMachinesInputTypeDef]
    ) -> ListStateMachinesOutputTypeDef:
        """
        Lists the existing state machines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/list_state_machines.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#list_state_machines)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        List tags for a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#list_tags_for_resource)
        """

    def publish_state_machine_version(
        self, **kwargs: Unpack[PublishStateMachineVersionInputTypeDef]
    ) -> PublishStateMachineVersionOutputTypeDef:
        """
        Creates a <a
        href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html">version</a>
        from the current revision of a state machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/publish_state_machine_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#publish_state_machine_version)
        """

    def redrive_execution(
        self, **kwargs: Unpack[RedriveExecutionInputTypeDef]
    ) -> RedriveExecutionOutputTypeDef:
        """
        Restarts unsuccessful executions of Standard workflows that didn't complete
        successfully in the last 14 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/redrive_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#redrive_execution)
        """

    def send_task_failure(self, **kwargs: Unpack[SendTaskFailureInputTypeDef]) -> Dict[str, Any]:
        """
        Used by activity workers, Task states using the <a
        href="https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token">callback</a>
        pattern, and optionally Task states using the <a
        href="https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.h...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/send_task_failure.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#send_task_failure)
        """

    def send_task_heartbeat(
        self, **kwargs: Unpack[SendTaskHeartbeatInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Used by activity workers and Task states using the <a
        href="https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token">callback</a>
        pattern, and optionally Task states using the <a
        href="https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resourc...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/send_task_heartbeat.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#send_task_heartbeat)
        """

    def send_task_success(self, **kwargs: Unpack[SendTaskSuccessInputTypeDef]) -> Dict[str, Any]:
        """
        Used by activity workers, Task states using the <a
        href="https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token">callback</a>
        pattern, and optionally Task states using the <a
        href="https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.h...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/send_task_success.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#send_task_success)
        """

    def start_execution(
        self, **kwargs: Unpack[StartExecutionInputTypeDef]
    ) -> StartExecutionOutputTypeDef:
        """
        Starts a state machine execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/start_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#start_execution)
        """

    def start_sync_execution(
        self, **kwargs: Unpack[StartSyncExecutionInputTypeDef]
    ) -> StartSyncExecutionOutputTypeDef:
        """
        Starts a Synchronous Express state machine execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/start_sync_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#start_sync_execution)
        """

    def stop_execution(
        self, **kwargs: Unpack[StopExecutionInputTypeDef]
    ) -> StopExecutionOutputTypeDef:
        """
        Stops an execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/stop_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#stop_execution)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Add a tag to a Step Functions resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#tag_resource)
        """

    def test_state(self, **kwargs: Unpack[TestStateInputTypeDef]) -> TestStateOutputTypeDef:
        """
        Accepts the definition of a single state and executes it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/test_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#test_state)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Remove a tag from a Step Functions resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#untag_resource)
        """

    def update_map_run(self, **kwargs: Unpack[UpdateMapRunInputTypeDef]) -> Dict[str, Any]:
        """
        Updates an in-progress Map Run's configuration to include changes to the
        settings that control maximum concurrency and Map Run failure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/update_map_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#update_map_run)
        """

    def update_state_machine(
        self, **kwargs: Unpack[UpdateStateMachineInputTypeDef]
    ) -> UpdateStateMachineOutputTypeDef:
        """
        Updates an existing state machine by modifying its <code>definition</code>,
        <code>roleArn</code>, <code>loggingConfiguration</code>, or
        <code>EncryptionConfiguration</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/update_state_machine.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#update_state_machine)
        """

    def update_state_machine_alias(
        self, **kwargs: Unpack[UpdateStateMachineAliasInputTypeDef]
    ) -> UpdateStateMachineAliasOutputTypeDef:
        """
        Updates the configuration of an existing state machine <a
        href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html">alias</a>
        by modifying its <code>description</code> or <code>routingConfiguration</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/update_state_machine_alias.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#update_state_machine_alias)
        """

    def validate_state_machine_definition(
        self, **kwargs: Unpack[ValidateStateMachineDefinitionInputTypeDef]
    ) -> ValidateStateMachineDefinitionOutputTypeDef:
        """
        Validates the syntax of a state machine definition specified in <a
        href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html">Amazon
        States Language</a> (ASL), a JSON-based, structured language.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/validate_state_machine_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#validate_state_machine_definition)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_execution_history"]
    ) -> GetExecutionHistoryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_activities"]
    ) -> ListActivitiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_executions"]
    ) -> ListExecutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_map_runs"]
    ) -> ListMapRunsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_state_machines"]
    ) -> ListStateMachinesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#get_paginator)
        """
