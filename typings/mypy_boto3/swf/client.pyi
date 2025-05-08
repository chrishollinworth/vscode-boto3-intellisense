"""
Type annotations for swf service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_swf.client import SWFClient

    session = Session()
    client: SWFClient = session.client("swf")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
    CountClosedWorkflowExecutionsInputTypeDef,
    CountOpenWorkflowExecutionsInputTypeDef,
    CountPendingActivityTasksInputTypeDef,
    CountPendingDecisionTasksInputTypeDef,
    DecisionTaskTypeDef,
    DeleteActivityTypeInputTypeDef,
    DeleteWorkflowTypeInputTypeDef,
    DeprecateActivityTypeInputTypeDef,
    DeprecateDomainInputTypeDef,
    DeprecateWorkflowTypeInputTypeDef,
    DescribeActivityTypeInputTypeDef,
    DescribeDomainInputTypeDef,
    DescribeWorkflowExecutionInputTypeDef,
    DescribeWorkflowTypeInputTypeDef,
    DomainDetailTypeDef,
    DomainInfosTypeDef,
    EmptyResponseMetadataTypeDef,
    GetWorkflowExecutionHistoryInputTypeDef,
    HistoryTypeDef,
    ListActivityTypesInputTypeDef,
    ListClosedWorkflowExecutionsInputTypeDef,
    ListDomainsInputTypeDef,
    ListOpenWorkflowExecutionsInputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListWorkflowTypesInputTypeDef,
    PendingTaskCountTypeDef,
    PollForActivityTaskInputTypeDef,
    PollForDecisionTaskInputTypeDef,
    RecordActivityTaskHeartbeatInputTypeDef,
    RegisterActivityTypeInputTypeDef,
    RegisterDomainInputTypeDef,
    RegisterWorkflowTypeInputTypeDef,
    RequestCancelWorkflowExecutionInputTypeDef,
    RespondActivityTaskCanceledInputTypeDef,
    RespondActivityTaskCompletedInputTypeDef,
    RespondActivityTaskFailedInputTypeDef,
    RespondDecisionTaskCompletedInputTypeDef,
    RunTypeDef,
    SignalWorkflowExecutionInputTypeDef,
    StartWorkflowExecutionInputTypeDef,
    TagResourceInputTypeDef,
    TerminateWorkflowExecutionInputTypeDef,
    UndeprecateActivityTypeInputTypeDef,
    UndeprecateDomainInputTypeDef,
    UndeprecateWorkflowTypeInputTypeDef,
    UntagResourceInputTypeDef,
    WorkflowExecutionCountTypeDef,
    WorkflowExecutionDetailTypeDef,
    WorkflowExecutionInfosTypeDef,
    WorkflowTypeDetailTypeDef,
    WorkflowTypeInfosTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("SWFClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    DefaultUndefinedFault: Type[BotocoreClientError]
    DomainAlreadyExistsFault: Type[BotocoreClientError]
    DomainDeprecatedFault: Type[BotocoreClientError]
    LimitExceededFault: Type[BotocoreClientError]
    OperationNotPermittedFault: Type[BotocoreClientError]
    TooManyTagsFault: Type[BotocoreClientError]
    TypeAlreadyExistsFault: Type[BotocoreClientError]
    TypeDeprecatedFault: Type[BotocoreClientError]
    TypeNotDeprecatedFault: Type[BotocoreClientError]
    UnknownResourceFault: Type[BotocoreClientError]
    WorkflowExecutionAlreadyStartedFault: Type[BotocoreClientError]

class SWFClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SWFClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#generate_presigned_url)
        """

    def count_closed_workflow_executions(
        self, **kwargs: Unpack[CountClosedWorkflowExecutionsInputTypeDef]
    ) -> WorkflowExecutionCountTypeDef:
        """
        Returns the number of closed workflow executions within the given domain that
        meet the specified filtering criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/count_closed_workflow_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#count_closed_workflow_executions)
        """

    def count_open_workflow_executions(
        self, **kwargs: Unpack[CountOpenWorkflowExecutionsInputTypeDef]
    ) -> WorkflowExecutionCountTypeDef:
        """
        Returns the number of open workflow executions within the given domain that
        meet the specified filtering criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/count_open_workflow_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#count_open_workflow_executions)
        """

    def count_pending_activity_tasks(
        self, **kwargs: Unpack[CountPendingActivityTasksInputTypeDef]
    ) -> PendingTaskCountTypeDef:
        """
        Returns the estimated number of activity tasks in the specified task list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/count_pending_activity_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#count_pending_activity_tasks)
        """

    def count_pending_decision_tasks(
        self, **kwargs: Unpack[CountPendingDecisionTasksInputTypeDef]
    ) -> PendingTaskCountTypeDef:
        """
        Returns the estimated number of decision tasks in the specified task list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/count_pending_decision_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#count_pending_decision_tasks)
        """

    def delete_activity_type(
        self, **kwargs: Unpack[DeleteActivityTypeInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified <i>activity type</i>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/delete_activity_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#delete_activity_type)
        """

    def delete_workflow_type(
        self, **kwargs: Unpack[DeleteWorkflowTypeInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified <i>workflow type</i>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/delete_workflow_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#delete_workflow_type)
        """

    def deprecate_activity_type(
        self, **kwargs: Unpack[DeprecateActivityTypeInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deprecates the specified <i>activity type</i>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/deprecate_activity_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#deprecate_activity_type)
        """

    def deprecate_domain(
        self, **kwargs: Unpack[DeprecateDomainInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deprecates the specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/deprecate_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#deprecate_domain)
        """

    def deprecate_workflow_type(
        self, **kwargs: Unpack[DeprecateWorkflowTypeInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deprecates the specified <i>workflow type</i>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/deprecate_workflow_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#deprecate_workflow_type)
        """

    def describe_activity_type(
        self, **kwargs: Unpack[DescribeActivityTypeInputTypeDef]
    ) -> ActivityTypeDetailTypeDef:
        """
        Returns information about the specified activity type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/describe_activity_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#describe_activity_type)
        """

    def describe_domain(self, **kwargs: Unpack[DescribeDomainInputTypeDef]) -> DomainDetailTypeDef:
        """
        Returns information about the specified domain, including description and
        status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/describe_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#describe_domain)
        """

    def describe_workflow_execution(
        self, **kwargs: Unpack[DescribeWorkflowExecutionInputTypeDef]
    ) -> WorkflowExecutionDetailTypeDef:
        """
        Returns information about the specified workflow execution including its type
        and some statistics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/describe_workflow_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#describe_workflow_execution)
        """

    def describe_workflow_type(
        self, **kwargs: Unpack[DescribeWorkflowTypeInputTypeDef]
    ) -> WorkflowTypeDetailTypeDef:
        """
        Returns information about the specified <i>workflow type</i>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/describe_workflow_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#describe_workflow_type)
        """

    def get_workflow_execution_history(
        self, **kwargs: Unpack[GetWorkflowExecutionHistoryInputTypeDef]
    ) -> HistoryTypeDef:
        """
        Returns the history of the specified workflow execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/get_workflow_execution_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#get_workflow_execution_history)
        """

    def list_activity_types(
        self, **kwargs: Unpack[ListActivityTypesInputTypeDef]
    ) -> ActivityTypeInfosTypeDef:
        """
        Returns information about all activities registered in the specified domain
        that match the specified name and registration status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/list_activity_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#list_activity_types)
        """

    def list_closed_workflow_executions(
        self, **kwargs: Unpack[ListClosedWorkflowExecutionsInputTypeDef]
    ) -> WorkflowExecutionInfosTypeDef:
        """
        Returns a list of closed workflow executions in the specified domain that meet
        the filtering criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/list_closed_workflow_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#list_closed_workflow_executions)
        """

    def list_domains(self, **kwargs: Unpack[ListDomainsInputTypeDef]) -> DomainInfosTypeDef:
        """
        Returns the list of domains registered in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/list_domains.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#list_domains)
        """

    def list_open_workflow_executions(
        self, **kwargs: Unpack[ListOpenWorkflowExecutionsInputTypeDef]
    ) -> WorkflowExecutionInfosTypeDef:
        """
        Returns a list of open workflow executions in the specified domain that meet
        the filtering criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/list_open_workflow_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#list_open_workflow_executions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        List tags for a given domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#list_tags_for_resource)
        """

    def list_workflow_types(
        self, **kwargs: Unpack[ListWorkflowTypesInputTypeDef]
    ) -> WorkflowTypeInfosTypeDef:
        """
        Returns information about workflow types in the specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/list_workflow_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#list_workflow_types)
        """

    def poll_for_activity_task(
        self, **kwargs: Unpack[PollForActivityTaskInputTypeDef]
    ) -> ActivityTaskTypeDef:
        """
        Used by workers to get an <a>ActivityTask</a> from the specified activity
        <code>taskList</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/poll_for_activity_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#poll_for_activity_task)
        """

    def poll_for_decision_task(
        self, **kwargs: Unpack[PollForDecisionTaskInputTypeDef]
    ) -> DecisionTaskTypeDef:
        """
        Used by deciders to get a <a>DecisionTask</a> from the specified decision
        <code>taskList</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/poll_for_decision_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#poll_for_decision_task)
        """

    def record_activity_task_heartbeat(
        self, **kwargs: Unpack[RecordActivityTaskHeartbeatInputTypeDef]
    ) -> ActivityTaskStatusTypeDef:
        """
        Used by activity workers to report to the service that the <a>ActivityTask</a>
        represented by the specified <code>taskToken</code> is still making progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/record_activity_task_heartbeat.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#record_activity_task_heartbeat)
        """

    def register_activity_type(
        self, **kwargs: Unpack[RegisterActivityTypeInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Registers a new <i>activity type</i> along with its configuration settings in
        the specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/register_activity_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#register_activity_type)
        """

    def register_domain(
        self, **kwargs: Unpack[RegisterDomainInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Registers a new domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/register_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#register_domain)
        """

    def register_workflow_type(
        self, **kwargs: Unpack[RegisterWorkflowTypeInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Registers a new <i>workflow type</i> and its configuration settings in the
        specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/register_workflow_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#register_workflow_type)
        """

    def request_cancel_workflow_execution(
        self, **kwargs: Unpack[RequestCancelWorkflowExecutionInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Records a <code>WorkflowExecutionCancelRequested</code> event in the currently
        running workflow execution identified by the given domain, workflowId, and
        runId.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/request_cancel_workflow_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#request_cancel_workflow_execution)
        """

    def respond_activity_task_canceled(
        self, **kwargs: Unpack[RespondActivityTaskCanceledInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Used by workers to tell the service that the <a>ActivityTask</a> identified by
        the <code>taskToken</code> was successfully canceled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/respond_activity_task_canceled.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#respond_activity_task_canceled)
        """

    def respond_activity_task_completed(
        self, **kwargs: Unpack[RespondActivityTaskCompletedInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Used by workers to tell the service that the <a>ActivityTask</a> identified by
        the <code>taskToken</code> completed successfully with a <code>result</code>
        (if provided).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/respond_activity_task_completed.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#respond_activity_task_completed)
        """

    def respond_activity_task_failed(
        self, **kwargs: Unpack[RespondActivityTaskFailedInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Used by workers to tell the service that the <a>ActivityTask</a> identified by
        the <code>taskToken</code> has failed with <code>reason</code> (if specified).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/respond_activity_task_failed.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#respond_activity_task_failed)
        """

    def respond_decision_task_completed(
        self, **kwargs: Unpack[RespondDecisionTaskCompletedInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Used by deciders to tell the service that the <a>DecisionTask</a> identified by
        the <code>taskToken</code> has successfully completed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/respond_decision_task_completed.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#respond_decision_task_completed)
        """

    def signal_workflow_execution(
        self, **kwargs: Unpack[SignalWorkflowExecutionInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Records a <code>WorkflowExecutionSignaled</code> event in the workflow
        execution history and creates a decision task for the workflow execution
        identified by the given domain, workflowId and runId.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/signal_workflow_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#signal_workflow_execution)
        """

    def start_workflow_execution(
        self, **kwargs: Unpack[StartWorkflowExecutionInputTypeDef]
    ) -> RunTypeDef:
        """
        Starts an execution of the workflow type in the specified domain using the
        provided <code>workflowId</code> and input data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/start_workflow_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#start_workflow_execution)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Add a tag to a Amazon SWF domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#tag_resource)
        """

    def terminate_workflow_execution(
        self, **kwargs: Unpack[TerminateWorkflowExecutionInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Records a <code>WorkflowExecutionTerminated</code> event and forces closure of
        the workflow execution identified by the given domain, runId, and workflowId.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/terminate_workflow_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#terminate_workflow_execution)
        """

    def undeprecate_activity_type(
        self, **kwargs: Unpack[UndeprecateActivityTypeInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Undeprecates a previously deprecated <i>activity type</i>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/undeprecate_activity_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#undeprecate_activity_type)
        """

    def undeprecate_domain(
        self, **kwargs: Unpack[UndeprecateDomainInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Undeprecates a previously deprecated domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/undeprecate_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#undeprecate_domain)
        """

    def undeprecate_workflow_type(
        self, **kwargs: Unpack[UndeprecateWorkflowTypeInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Undeprecates a previously deprecated <i>workflow type</i>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/undeprecate_workflow_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#undeprecate_workflow_type)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Remove a tag from a Amazon SWF domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#untag_resource)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_workflow_execution_history"]
    ) -> GetWorkflowExecutionHistoryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_activity_types"]
    ) -> ListActivityTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_closed_workflow_executions"]
    ) -> ListClosedWorkflowExecutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_domains"]
    ) -> ListDomainsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_open_workflow_executions"]
    ) -> ListOpenWorkflowExecutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workflow_types"]
    ) -> ListWorkflowTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["poll_for_decision_task"]
    ) -> PollForDecisionTaskPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/client/#get_paginator)
        """
