# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for stepfunctions service client

Usage::

    ```python
    import boto3
    from mypy_boto3_stepfunctions import SFNClient

    client: SFNClient = boto3.client("stepfunctions")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_stepfunctions.paginator import (
    GetExecutionHistoryPaginator,
    ListActivitiesPaginator,
    ListExecutionsPaginator,
    ListStateMachinesPaginator,
)
from mypy_boto3_stepfunctions.type_defs import (
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


class SFNClient:
    """
    [SFN.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.can_paginate)
        """

    def create_activity(
        self, name: str, tags: List["TagTypeDef"] = None
    ) -> CreateActivityOutputTypeDef:
        """
        [Client.create_activity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.create_activity)
        """

    def create_state_machine(
        self,
        name: str,
        definition: str,
        roleArn: str,
        type: Literal["STANDARD", "EXPRESS"] = None,
        loggingConfiguration: "LoggingConfigurationTypeDef" = None,
        tags: List["TagTypeDef"] = None,
        tracingConfiguration: "TracingConfigurationTypeDef" = None,
    ) -> CreateStateMachineOutputTypeDef:
        """
        [Client.create_state_machine documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.create_state_machine)
        """

    def delete_activity(self, activityArn: str) -> Dict[str, Any]:
        """
        [Client.delete_activity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.delete_activity)
        """

    def delete_state_machine(self, stateMachineArn: str) -> Dict[str, Any]:
        """
        [Client.delete_state_machine documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.delete_state_machine)
        """

    def describe_activity(self, activityArn: str) -> DescribeActivityOutputTypeDef:
        """
        [Client.describe_activity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.describe_activity)
        """

    def describe_execution(self, executionArn: str) -> DescribeExecutionOutputTypeDef:
        """
        [Client.describe_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.describe_execution)
        """

    def describe_state_machine(self, stateMachineArn: str) -> DescribeStateMachineOutputTypeDef:
        """
        [Client.describe_state_machine documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.describe_state_machine)
        """

    def describe_state_machine_for_execution(
        self, executionArn: str
    ) -> DescribeStateMachineForExecutionOutputTypeDef:
        """
        [Client.describe_state_machine_for_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.describe_state_machine_for_execution)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.generate_presigned_url)
        """

    def get_activity_task(
        self, activityArn: str, workerName: str = None
    ) -> GetActivityTaskOutputTypeDef:
        """
        [Client.get_activity_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.get_activity_task)
        """

    def get_execution_history(
        self,
        executionArn: str,
        maxResults: int = None,
        reverseOrder: bool = None,
        nextToken: str = None,
        includeExecutionData: bool = None,
    ) -> GetExecutionHistoryOutputTypeDef:
        """
        [Client.get_execution_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.get_execution_history)
        """

    def list_activities(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListActivitiesOutputTypeDef:
        """
        [Client.list_activities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.list_activities)
        """

    def list_executions(
        self,
        stateMachineArn: str,
        statusFilter: Literal["RUNNING", "SUCCEEDED", "FAILED", "TIMED_OUT", "ABORTED"] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListExecutionsOutputTypeDef:
        """
        [Client.list_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.list_executions)
        """

    def list_state_machines(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListStateMachinesOutputTypeDef:
        """
        [Client.list_state_machines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.list_state_machines)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.list_tags_for_resource)
        """

    def send_task_failure(
        self, taskToken: str, error: str = None, cause: str = None
    ) -> Dict[str, Any]:
        """
        [Client.send_task_failure documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.send_task_failure)
        """

    def send_task_heartbeat(self, taskToken: str) -> Dict[str, Any]:
        """
        [Client.send_task_heartbeat documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.send_task_heartbeat)
        """

    def send_task_success(self, taskToken: str, output: str) -> Dict[str, Any]:
        """
        [Client.send_task_success documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.send_task_success)
        """

    def start_execution(
        self, stateMachineArn: str, name: str = None, input: str = None, traceHeader: str = None
    ) -> StartExecutionOutputTypeDef:
        """
        [Client.start_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.start_execution)
        """

    def stop_execution(
        self, executionArn: str, error: str = None, cause: str = None
    ) -> StopExecutionOutputTypeDef:
        """
        [Client.stop_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.stop_execution)
        """

    def tag_resource(self, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.untag_resource)
        """

    def update_state_machine(
        self,
        stateMachineArn: str,
        definition: str = None,
        roleArn: str = None,
        loggingConfiguration: "LoggingConfigurationTypeDef" = None,
        tracingConfiguration: "TracingConfigurationTypeDef" = None,
    ) -> UpdateStateMachineOutputTypeDef:
        """
        [Client.update_state_machine documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Client.update_state_machine)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_execution_history"]
    ) -> GetExecutionHistoryPaginator:
        """
        [Paginator.GetExecutionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Paginator.GetExecutionHistory)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_activities"]) -> ListActivitiesPaginator:
        """
        [Paginator.ListActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Paginator.ListActivities)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_executions"]) -> ListExecutionsPaginator:
        """
        [Paginator.ListExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Paginator.ListExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_state_machines"]
    ) -> ListStateMachinesPaginator:
        """
        [Paginator.ListStateMachines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/stepfunctions.html#SFN.Paginator.ListStateMachines)
        """
