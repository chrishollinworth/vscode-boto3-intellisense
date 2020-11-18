# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for swf service client

Usage::

    ```python
    import boto3
    from mypy_boto3_swf import SWFClient

    client: SWFClient = boto3.client("swf")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_swf.paginator import (
    GetWorkflowExecutionHistoryPaginator,
    ListActivityTypesPaginator,
    ListClosedWorkflowExecutionsPaginator,
    ListDomainsPaginator,
    ListOpenWorkflowExecutionsPaginator,
    ListWorkflowTypesPaginator,
    PollForDecisionTaskPaginator,
)
from mypy_boto3_swf.type_defs import (
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


class SWFClient:
    """
    [SWF.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.can_paginate)
        """

    def count_closed_workflow_executions(
        self,
        domain: str,
        startTimeFilter: ExecutionTimeFilterTypeDef = None,
        closeTimeFilter: ExecutionTimeFilterTypeDef = None,
        executionFilter: WorkflowExecutionFilterTypeDef = None,
        typeFilter: WorkflowTypeFilterTypeDef = None,
        tagFilter: TagFilterTypeDef = None,
        closeStatusFilter: CloseStatusFilterTypeDef = None,
    ) -> WorkflowExecutionCountTypeDef:
        """
        [Client.count_closed_workflow_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.count_closed_workflow_executions)
        """

    def count_open_workflow_executions(
        self,
        domain: str,
        startTimeFilter: ExecutionTimeFilterTypeDef,
        typeFilter: WorkflowTypeFilterTypeDef = None,
        tagFilter: TagFilterTypeDef = None,
        executionFilter: WorkflowExecutionFilterTypeDef = None,
    ) -> WorkflowExecutionCountTypeDef:
        """
        [Client.count_open_workflow_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.count_open_workflow_executions)
        """

    def count_pending_activity_tasks(
        self, domain: str, taskList: "TaskListTypeDef"
    ) -> PendingTaskCountTypeDef:
        """
        [Client.count_pending_activity_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.count_pending_activity_tasks)
        """

    def count_pending_decision_tasks(
        self, domain: str, taskList: "TaskListTypeDef"
    ) -> PendingTaskCountTypeDef:
        """
        [Client.count_pending_decision_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.count_pending_decision_tasks)
        """

    def deprecate_activity_type(self, domain: str, activityType: "ActivityTypeTypeDef") -> None:
        """
        [Client.deprecate_activity_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.deprecate_activity_type)
        """

    def deprecate_domain(self, name: str) -> None:
        """
        [Client.deprecate_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.deprecate_domain)
        """

    def deprecate_workflow_type(self, domain: str, workflowType: "WorkflowTypeTypeDef") -> None:
        """
        [Client.deprecate_workflow_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.deprecate_workflow_type)
        """

    def describe_activity_type(
        self, domain: str, activityType: "ActivityTypeTypeDef"
    ) -> ActivityTypeDetailTypeDef:
        """
        [Client.describe_activity_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.describe_activity_type)
        """

    def describe_domain(self, name: str) -> DomainDetailTypeDef:
        """
        [Client.describe_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.describe_domain)
        """

    def describe_workflow_execution(
        self, domain: str, execution: "WorkflowExecutionTypeDef"
    ) -> WorkflowExecutionDetailTypeDef:
        """
        [Client.describe_workflow_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.describe_workflow_execution)
        """

    def describe_workflow_type(
        self, domain: str, workflowType: "WorkflowTypeTypeDef"
    ) -> WorkflowTypeDetailTypeDef:
        """
        [Client.describe_workflow_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.describe_workflow_type)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.generate_presigned_url)
        """

    def get_workflow_execution_history(
        self,
        domain: str,
        execution: "WorkflowExecutionTypeDef",
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
    ) -> HistoryTypeDef:
        """
        [Client.get_workflow_execution_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.get_workflow_execution_history)
        """

    def list_activity_types(
        self,
        domain: str,
        registrationStatus: Literal["REGISTERED", "DEPRECATED"],
        name: str = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
    ) -> ActivityTypeInfosTypeDef:
        """
        [Client.list_activity_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.list_activity_types)
        """

    def list_closed_workflow_executions(
        self,
        domain: str,
        startTimeFilter: ExecutionTimeFilterTypeDef = None,
        closeTimeFilter: ExecutionTimeFilterTypeDef = None,
        executionFilter: WorkflowExecutionFilterTypeDef = None,
        closeStatusFilter: CloseStatusFilterTypeDef = None,
        typeFilter: WorkflowTypeFilterTypeDef = None,
        tagFilter: TagFilterTypeDef = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
    ) -> WorkflowExecutionInfosTypeDef:
        """
        [Client.list_closed_workflow_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.list_closed_workflow_executions)
        """

    def list_domains(
        self,
        registrationStatus: Literal["REGISTERED", "DEPRECATED"],
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
    ) -> DomainInfosTypeDef:
        """
        [Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.list_domains)
        """

    def list_open_workflow_executions(
        self,
        domain: str,
        startTimeFilter: ExecutionTimeFilterTypeDef,
        typeFilter: WorkflowTypeFilterTypeDef = None,
        tagFilter: TagFilterTypeDef = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
        executionFilter: WorkflowExecutionFilterTypeDef = None,
    ) -> WorkflowExecutionInfosTypeDef:
        """
        [Client.list_open_workflow_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.list_open_workflow_executions)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.list_tags_for_resource)
        """

    def list_workflow_types(
        self,
        domain: str,
        registrationStatus: Literal["REGISTERED", "DEPRECATED"],
        name: str = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
    ) -> WorkflowTypeInfosTypeDef:
        """
        [Client.list_workflow_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.list_workflow_types)
        """

    def poll_for_activity_task(
        self, domain: str, taskList: "TaskListTypeDef", identity: str = None
    ) -> ActivityTaskTypeDef:
        """
        [Client.poll_for_activity_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.poll_for_activity_task)
        """

    def poll_for_decision_task(
        self,
        domain: str,
        taskList: "TaskListTypeDef",
        identity: str = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
    ) -> DecisionTaskTypeDef:
        """
        [Client.poll_for_decision_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.poll_for_decision_task)
        """

    def record_activity_task_heartbeat(
        self, taskToken: str, details: str = None
    ) -> ActivityTaskStatusTypeDef:
        """
        [Client.record_activity_task_heartbeat documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.record_activity_task_heartbeat)
        """

    def register_activity_type(
        self,
        domain: str,
        name: str,
        version: str,
        description: str = None,
        defaultTaskStartToCloseTimeout: str = None,
        defaultTaskHeartbeatTimeout: str = None,
        defaultTaskList: "TaskListTypeDef" = None,
        defaultTaskPriority: str = None,
        defaultTaskScheduleToStartTimeout: str = None,
        defaultTaskScheduleToCloseTimeout: str = None,
    ) -> None:
        """
        [Client.register_activity_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.register_activity_type)
        """

    def register_domain(
        self,
        name: str,
        workflowExecutionRetentionPeriodInDays: str,
        description: str = None,
        tags: List["ResourceTagTypeDef"] = None,
    ) -> None:
        """
        [Client.register_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.register_domain)
        """

    def register_workflow_type(
        self,
        domain: str,
        name: str,
        version: str,
        description: str = None,
        defaultTaskStartToCloseTimeout: str = None,
        defaultExecutionStartToCloseTimeout: str = None,
        defaultTaskList: "TaskListTypeDef" = None,
        defaultTaskPriority: str = None,
        defaultChildPolicy: Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"] = None,
        defaultLambdaRole: str = None,
    ) -> None:
        """
        [Client.register_workflow_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.register_workflow_type)
        """

    def request_cancel_workflow_execution(
        self, domain: str, workflowId: str, runId: str = None
    ) -> None:
        """
        [Client.request_cancel_workflow_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.request_cancel_workflow_execution)
        """

    def respond_activity_task_canceled(self, taskToken: str, details: str = None) -> None:
        """
        [Client.respond_activity_task_canceled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.respond_activity_task_canceled)
        """

    def respond_activity_task_completed(self, taskToken: str, result: str = None) -> None:
        """
        [Client.respond_activity_task_completed documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.respond_activity_task_completed)
        """

    def respond_activity_task_failed(
        self, taskToken: str, reason: str = None, details: str = None
    ) -> None:
        """
        [Client.respond_activity_task_failed documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.respond_activity_task_failed)
        """

    def respond_decision_task_completed(
        self, taskToken: str, decisions: List[DecisionTypeDef] = None, executionContext: str = None
    ) -> None:
        """
        [Client.respond_decision_task_completed documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.respond_decision_task_completed)
        """

    def signal_workflow_execution(
        self, domain: str, workflowId: str, signalName: str, runId: str = None, input: str = None
    ) -> None:
        """
        [Client.signal_workflow_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.signal_workflow_execution)
        """

    def start_workflow_execution(
        self,
        domain: str,
        workflowId: str,
        workflowType: "WorkflowTypeTypeDef",
        taskList: "TaskListTypeDef" = None,
        taskPriority: str = None,
        input: str = None,
        executionStartToCloseTimeout: str = None,
        tagList: List[str] = None,
        taskStartToCloseTimeout: str = None,
        childPolicy: Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"] = None,
        lambdaRole: str = None,
    ) -> RunTypeDef:
        """
        [Client.start_workflow_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.start_workflow_execution)
        """

    def tag_resource(self, resourceArn: str, tags: List["ResourceTagTypeDef"]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.tag_resource)
        """

    def terminate_workflow_execution(
        self,
        domain: str,
        workflowId: str,
        runId: str = None,
        reason: str = None,
        details: str = None,
        childPolicy: Literal["TERMINATE", "REQUEST_CANCEL", "ABANDON"] = None,
    ) -> None:
        """
        [Client.terminate_workflow_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.terminate_workflow_execution)
        """

    def undeprecate_activity_type(self, domain: str, activityType: "ActivityTypeTypeDef") -> None:
        """
        [Client.undeprecate_activity_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.undeprecate_activity_type)
        """

    def undeprecate_domain(self, name: str) -> None:
        """
        [Client.undeprecate_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.undeprecate_domain)
        """

    def undeprecate_workflow_type(self, domain: str, workflowType: "WorkflowTypeTypeDef") -> None:
        """
        [Client.undeprecate_workflow_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.undeprecate_workflow_type)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Client.untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_workflow_execution_history"]
    ) -> GetWorkflowExecutionHistoryPaginator:
        """
        [Paginator.GetWorkflowExecutionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.GetWorkflowExecutionHistory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_activity_types"]
    ) -> ListActivityTypesPaginator:
        """
        [Paginator.ListActivityTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.ListActivityTypes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_closed_workflow_executions"]
    ) -> ListClosedWorkflowExecutionsPaginator:
        """
        [Paginator.ListClosedWorkflowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.ListClosedWorkflowExecutions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_domains"]) -> ListDomainsPaginator:
        """
        [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.ListDomains)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_open_workflow_executions"]
    ) -> ListOpenWorkflowExecutionsPaginator:
        """
        [Paginator.ListOpenWorkflowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.ListOpenWorkflowExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_workflow_types"]
    ) -> ListWorkflowTypesPaginator:
        """
        [Paginator.ListWorkflowTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.ListWorkflowTypes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["poll_for_decision_task"]
    ) -> PollForDecisionTaskPaginator:
        """
        [Paginator.PollForDecisionTask documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.PollForDecisionTask)
        """
