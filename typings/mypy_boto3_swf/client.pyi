"""
Type annotations for swf service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_swf import SWFClient

    client: SWFClient = boto3.client("swf")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ChildPolicyType, RegistrationStatusType
from .paginator import (
    GetWorkflowExecutionHistoryPaginator,
    ListActivityTypesPaginator,
    ListClosedWorkflowExecutionsPaginator,
    ListDomainsPaginator,
    ListOpenWorkflowExecutionsPaginator,
    ListWorkflowTypesPaginator,
    PollForDecisionTaskPaginator,
)
from .type_defs import (
    ActivityTaskStatusTypeDef,
    ActivityTaskTypeDef,
    ActivityTypeDetailTypeDef,
    ActivityTypeInfosTypeDef,
    ActivityTypeTypeDef,
    CloseStatusFilterTypeDef,
    DecisionTaskTypeDef,
    DecisionTypeDef,
    DomainDetailTypeDef,
    DomainInfosTypeDef,
    ExecutionTimeFilterTypeDef,
    HistoryTypeDef,
    ListTagsForResourceOutputTypeDef,
    PendingTaskCountTypeDef,
    ResourceTagTypeDef,
    RunTypeDef,
    TagFilterTypeDef,
    TaskListTypeDef,
    WorkflowExecutionCountTypeDef,
    WorkflowExecutionDetailTypeDef,
    WorkflowExecutionFilterTypeDef,
    WorkflowExecutionInfosTypeDef,
    WorkflowExecutionTypeDef,
    WorkflowTypeDetailTypeDef,
    WorkflowTypeFilterTypeDef,
    WorkflowTypeInfosTypeDef,
    WorkflowTypeTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("SWFClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    DefaultUndefinedFault: Type[BotocoreClientError]
    DomainAlreadyExistsFault: Type[BotocoreClientError]
    DomainDeprecatedFault: Type[BotocoreClientError]
    LimitExceededFault: Type[BotocoreClientError]
    OperationNotPermittedFault: Type[BotocoreClientError]
    TooManyTagsFault: Type[BotocoreClientError]
    TypeAlreadyExistsFault: Type[BotocoreClientError]
    TypeDeprecatedFault: Type[BotocoreClientError]
    UnknownResourceFault: Type[BotocoreClientError]
    WorkflowExecutionAlreadyStartedFault: Type[BotocoreClientError]

class SWFClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        SWFClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#can_paginate)
        """
    def count_closed_workflow_executions(
        self,
        *,
        domain: str,
        startTimeFilter: "ExecutionTimeFilterTypeDef" = None,
        closeTimeFilter: "ExecutionTimeFilterTypeDef" = None,
        executionFilter: "WorkflowExecutionFilterTypeDef" = None,
        typeFilter: "WorkflowTypeFilterTypeDef" = None,
        tagFilter: "TagFilterTypeDef" = None,
        closeStatusFilter: "CloseStatusFilterTypeDef" = None
    ) -> WorkflowExecutionCountTypeDef:
        """
        Returns the number of closed workflow executions within the given domain that
        meet the specified filtering criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.count_closed_workflow_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#count_closed_workflow_executions)
        """
    def count_open_workflow_executions(
        self,
        *,
        domain: str,
        startTimeFilter: "ExecutionTimeFilterTypeDef",
        typeFilter: "WorkflowTypeFilterTypeDef" = None,
        tagFilter: "TagFilterTypeDef" = None,
        executionFilter: "WorkflowExecutionFilterTypeDef" = None
    ) -> WorkflowExecutionCountTypeDef:
        """
        Returns the number of open workflow executions within the given domain that meet
        the specified filtering criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.count_open_workflow_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#count_open_workflow_executions)
        """
    def count_pending_activity_tasks(
        self, *, domain: str, taskList: "TaskListTypeDef"
    ) -> PendingTaskCountTypeDef:
        """
        Returns the estimated number of activity tasks in the specified task list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.count_pending_activity_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#count_pending_activity_tasks)
        """
    def count_pending_decision_tasks(
        self, *, domain: str, taskList: "TaskListTypeDef"
    ) -> PendingTaskCountTypeDef:
        """
        Returns the estimated number of decision tasks in the specified task list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.count_pending_decision_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#count_pending_decision_tasks)
        """
    def deprecate_activity_type(self, *, domain: str, activityType: "ActivityTypeTypeDef") -> None:
        """
        Deprecates the specified *activity type*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.deprecate_activity_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#deprecate_activity_type)
        """
    def deprecate_domain(self, *, name: str) -> None:
        """
        Deprecates the specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.deprecate_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#deprecate_domain)
        """
    def deprecate_workflow_type(self, *, domain: str, workflowType: "WorkflowTypeTypeDef") -> None:
        """
        Deprecates the specified *workflow type*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.deprecate_workflow_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#deprecate_workflow_type)
        """
    def describe_activity_type(
        self, *, domain: str, activityType: "ActivityTypeTypeDef"
    ) -> ActivityTypeDetailTypeDef:
        """
        Returns information about the specified activity type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.describe_activity_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#describe_activity_type)
        """
    def describe_domain(self, *, name: str) -> DomainDetailTypeDef:
        """
        Returns information about the specified domain, including description and
        status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.describe_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#describe_domain)
        """
    def describe_workflow_execution(
        self, *, domain: str, execution: "WorkflowExecutionTypeDef"
    ) -> WorkflowExecutionDetailTypeDef:
        """
        Returns information about the specified workflow execution including its type
        and some statistics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.describe_workflow_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#describe_workflow_execution)
        """
    def describe_workflow_type(
        self, *, domain: str, workflowType: "WorkflowTypeTypeDef"
    ) -> WorkflowTypeDetailTypeDef:
        """
        Returns information about the specified *workflow type*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.describe_workflow_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#describe_workflow_type)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#generate_presigned_url)
        """
    def get_workflow_execution_history(
        self,
        *,
        domain: str,
        execution: "WorkflowExecutionTypeDef",
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None
    ) -> HistoryTypeDef:
        """
        Returns the history of the specified workflow execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.get_workflow_execution_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#get_workflow_execution_history)
        """
    def list_activity_types(
        self,
        *,
        domain: str,
        registrationStatus: RegistrationStatusType,
        name: str = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None
    ) -> ActivityTypeInfosTypeDef:
        """
        Returns information about all activities registered in the specified domain that
        match the specified name and registration status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.list_activity_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#list_activity_types)
        """
    def list_closed_workflow_executions(
        self,
        *,
        domain: str,
        startTimeFilter: "ExecutionTimeFilterTypeDef" = None,
        closeTimeFilter: "ExecutionTimeFilterTypeDef" = None,
        executionFilter: "WorkflowExecutionFilterTypeDef" = None,
        closeStatusFilter: "CloseStatusFilterTypeDef" = None,
        typeFilter: "WorkflowTypeFilterTypeDef" = None,
        tagFilter: "TagFilterTypeDef" = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None
    ) -> WorkflowExecutionInfosTypeDef:
        """
        Returns a list of closed workflow executions in the specified domain that meet
        the filtering criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.list_closed_workflow_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#list_closed_workflow_executions)
        """
    def list_domains(
        self,
        *,
        registrationStatus: RegistrationStatusType,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None
    ) -> DomainInfosTypeDef:
        """
        Returns the list of domains registered in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.list_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#list_domains)
        """
    def list_open_workflow_executions(
        self,
        *,
        domain: str,
        startTimeFilter: "ExecutionTimeFilterTypeDef",
        typeFilter: "WorkflowTypeFilterTypeDef" = None,
        tagFilter: "TagFilterTypeDef" = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
        executionFilter: "WorkflowExecutionFilterTypeDef" = None
    ) -> WorkflowExecutionInfosTypeDef:
        """
        Returns a list of open workflow executions in the specified domain that meet the
        filtering criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.list_open_workflow_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#list_open_workflow_executions)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        List tags for a given domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#list_tags_for_resource)
        """
    def list_workflow_types(
        self,
        *,
        domain: str,
        registrationStatus: RegistrationStatusType,
        name: str = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None
    ) -> WorkflowTypeInfosTypeDef:
        """
        Returns information about workflow types in the specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.list_workflow_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#list_workflow_types)
        """
    def poll_for_activity_task(
        self, *, domain: str, taskList: "TaskListTypeDef", identity: str = None
    ) -> ActivityTaskTypeDef:
        """
        Used by workers to get an  ActivityTask from the specified activity `taskList`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.poll_for_activity_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#poll_for_activity_task)
        """
    def poll_for_decision_task(
        self,
        *,
        domain: str,
        taskList: "TaskListTypeDef",
        identity: str = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None
    ) -> DecisionTaskTypeDef:
        """
        Used by deciders to get a  DecisionTask from the specified decision `taskList`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.poll_for_decision_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#poll_for_decision_task)
        """
    def record_activity_task_heartbeat(
        self, *, taskToken: str, details: str = None
    ) -> ActivityTaskStatusTypeDef:
        """
        Used by activity workers to report to the service that the  ActivityTask
        represented by the specified `taskToken` is still making progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.record_activity_task_heartbeat)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#record_activity_task_heartbeat)
        """
    def register_activity_type(
        self,
        *,
        domain: str,
        name: str,
        version: str,
        description: str = None,
        defaultTaskStartToCloseTimeout: str = None,
        defaultTaskHeartbeatTimeout: str = None,
        defaultTaskList: "TaskListTypeDef" = None,
        defaultTaskPriority: str = None,
        defaultTaskScheduleToStartTimeout: str = None,
        defaultTaskScheduleToCloseTimeout: str = None
    ) -> None:
        """
        Registers a new *activity type* along with its configuration settings in the
        specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.register_activity_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#register_activity_type)
        """
    def register_domain(
        self,
        *,
        name: str,
        workflowExecutionRetentionPeriodInDays: str,
        description: str = None,
        tags: List["ResourceTagTypeDef"] = None
    ) -> None:
        """
        Registers a new domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.register_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#register_domain)
        """
    def register_workflow_type(
        self,
        *,
        domain: str,
        name: str,
        version: str,
        description: str = None,
        defaultTaskStartToCloseTimeout: str = None,
        defaultExecutionStartToCloseTimeout: str = None,
        defaultTaskList: "TaskListTypeDef" = None,
        defaultTaskPriority: str = None,
        defaultChildPolicy: ChildPolicyType = None,
        defaultLambdaRole: str = None
    ) -> None:
        """
        Registers a new *workflow type* and its configuration settings in the specified
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.register_workflow_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#register_workflow_type)
        """
    def request_cancel_workflow_execution(
        self, *, domain: str, workflowId: str, runId: str = None
    ) -> None:
        """
        Records a `WorkflowExecutionCancelRequested` event in the currently running
        workflow execution identified by the given domain, workflowId, and runId.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.request_cancel_workflow_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#request_cancel_workflow_execution)
        """
    def respond_activity_task_canceled(self, *, taskToken: str, details: str = None) -> None:
        """
        Used by workers to tell the service that the  ActivityTask identified by the
        `taskToken` was successfully canceled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.respond_activity_task_canceled)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#respond_activity_task_canceled)
        """
    def respond_activity_task_completed(self, *, taskToken: str, result: str = None) -> None:
        """
        Used by workers to tell the service that the  ActivityTask identified by the
        `taskToken` completed successfully with a `result` (if provided).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.respond_activity_task_completed)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#respond_activity_task_completed)
        """
    def respond_activity_task_failed(
        self, *, taskToken: str, reason: str = None, details: str = None
    ) -> None:
        """
        Used by workers to tell the service that the  ActivityTask identified by the
        `taskToken` has failed with `reason` (if specified).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.respond_activity_task_failed)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#respond_activity_task_failed)
        """
    def respond_decision_task_completed(
        self,
        *,
        taskToken: str,
        decisions: List["DecisionTypeDef"] = None,
        executionContext: str = None
    ) -> None:
        """
        Used by deciders to tell the service that the  DecisionTask identified by the
        `taskToken` has successfully completed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.respond_decision_task_completed)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#respond_decision_task_completed)
        """
    def signal_workflow_execution(
        self, *, domain: str, workflowId: str, signalName: str, runId: str = None, input: str = None
    ) -> None:
        """
        Records a `WorkflowExecutionSignaled` event in the workflow execution history
        and creates a decision task for the workflow execution identified by the given
        domain, workflowId and runId.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.signal_workflow_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#signal_workflow_execution)
        """
    def start_workflow_execution(
        self,
        *,
        domain: str,
        workflowId: str,
        workflowType: "WorkflowTypeTypeDef",
        taskList: "TaskListTypeDef" = None,
        taskPriority: str = None,
        input: str = None,
        executionStartToCloseTimeout: str = None,
        tagList: List[str] = None,
        taskStartToCloseTimeout: str = None,
        childPolicy: ChildPolicyType = None,
        lambdaRole: str = None
    ) -> RunTypeDef:
        """
        Starts an execution of the workflow type in the specified domain using the
        provided `workflowId` and input data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.start_workflow_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#start_workflow_execution)
        """
    def tag_resource(self, *, resourceArn: str, tags: List["ResourceTagTypeDef"]) -> None:
        """
        Add a tag to a Amazon SWF domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#tag_resource)
        """
    def terminate_workflow_execution(
        self,
        *,
        domain: str,
        workflowId: str,
        runId: str = None,
        reason: str = None,
        details: str = None,
        childPolicy: ChildPolicyType = None
    ) -> None:
        """
        Records a `WorkflowExecutionTerminated` event and forces closure of the workflow
        execution identified by the given domain, runId, and workflowId.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.terminate_workflow_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#terminate_workflow_execution)
        """
    def undeprecate_activity_type(
        self, *, domain: str, activityType: "ActivityTypeTypeDef"
    ) -> None:
        """
        Undeprecates a previously deprecated *activity type*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.undeprecate_activity_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#undeprecate_activity_type)
        """
    def undeprecate_domain(self, *, name: str) -> None:
        """
        Undeprecates a previously deprecated domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.undeprecate_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#undeprecate_domain)
        """
    def undeprecate_workflow_type(
        self, *, domain: str, workflowType: "WorkflowTypeTypeDef"
    ) -> None:
        """
        Undeprecates a previously deprecated *workflow type*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.undeprecate_workflow_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#undeprecate_workflow_type)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> None:
        """
        Remove a tag from a Amazon SWF domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/client.html#untag_resource)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_workflow_execution_history"]
    ) -> GetWorkflowExecutionHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Paginator.GetWorkflowExecutionHistory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#getworkflowexecutionhistorypaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_activity_types"]
    ) -> ListActivityTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Paginator.ListActivityTypes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#listactivitytypespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_closed_workflow_executions"]
    ) -> ListClosedWorkflowExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Paginator.ListClosedWorkflowExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#listclosedworkflowexecutionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_domains"]) -> ListDomainsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Paginator.ListDomains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#listdomainspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_open_workflow_executions"]
    ) -> ListOpenWorkflowExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Paginator.ListOpenWorkflowExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#listopenworkflowexecutionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_workflow_types"]
    ) -> ListWorkflowTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Paginator.ListWorkflowTypes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#listworkflowtypespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["poll_for_decision_task"]
    ) -> PollForDecisionTaskPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/swf.html#SWF.Paginator.PollForDecisionTask)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#pollfordecisiontaskpaginator)
        """
