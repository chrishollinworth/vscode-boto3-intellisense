# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for swf service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_swf import SWFClient
    from mypy_boto3_swf.paginator import (
        GetWorkflowExecutionHistoryPaginator,
        ListActivityTypesPaginator,
        ListClosedWorkflowExecutionsPaginator,
        ListDomainsPaginator,
        ListOpenWorkflowExecutionsPaginator,
        ListWorkflowTypesPaginator,
        PollForDecisionTaskPaginator,
    )

    client: SWFClient = boto3.client("swf")

    get_workflow_execution_history_paginator: GetWorkflowExecutionHistoryPaginator = client.get_paginator("get_workflow_execution_history")
    list_activity_types_paginator: ListActivityTypesPaginator = client.get_paginator("list_activity_types")
    list_closed_workflow_executions_paginator: ListClosedWorkflowExecutionsPaginator = client.get_paginator("list_closed_workflow_executions")
    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_open_workflow_executions_paginator: ListOpenWorkflowExecutionsPaginator = client.get_paginator("list_open_workflow_executions")
    list_workflow_types_paginator: ListWorkflowTypesPaginator = client.get_paginator("list_workflow_types")
    poll_for_decision_task_paginator: PollForDecisionTaskPaginator = client.get_paginator("poll_for_decision_task")
    ```
"""
import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_swf.type_defs import (
    ActivityTypeInfosTypeDef,
    CloseStatusFilterTypeDef,
    DecisionTaskTypeDef,
    DomainInfosTypeDef,
    ExecutionTimeFilterTypeDef,
    HistoryTypeDef,
    PaginatorConfigTypeDef,
    TagFilterTypeDef,
    TaskListTypeDef,
    WorkflowExecutionFilterTypeDef,
    WorkflowExecutionInfosTypeDef,
    WorkflowExecutionTypeDef,
    WorkflowTypeFilterTypeDef,
    WorkflowTypeInfosTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetWorkflowExecutionHistoryPaginator",
    "ListActivityTypesPaginator",
    "ListClosedWorkflowExecutionsPaginator",
    "ListDomainsPaginator",
    "ListOpenWorkflowExecutionsPaginator",
    "ListWorkflowTypesPaginator",
    "PollForDecisionTaskPaginator",
)


class GetWorkflowExecutionHistoryPaginator(Boto3Paginator):
    """
    [Paginator.GetWorkflowExecutionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.GetWorkflowExecutionHistory)
    """

    def paginate(
        self,
        domain: str,
        execution: "WorkflowExecutionTypeDef",
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[HistoryTypeDef]:
        """
        [GetWorkflowExecutionHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.GetWorkflowExecutionHistory.paginate)
        """


class ListActivityTypesPaginator(Boto3Paginator):
    """
    [Paginator.ListActivityTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.ListActivityTypes)
    """

    def paginate(
        self,
        domain: str,
        registrationStatus: Literal["REGISTERED", "DEPRECATED"],
        name: str = None,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ActivityTypeInfosTypeDef]:
        """
        [ListActivityTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.ListActivityTypes.paginate)
        """


class ListClosedWorkflowExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListClosedWorkflowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.ListClosedWorkflowExecutions)
    """

    def paginate(
        self,
        domain: str,
        startTimeFilter: ExecutionTimeFilterTypeDef = None,
        closeTimeFilter: ExecutionTimeFilterTypeDef = None,
        executionFilter: WorkflowExecutionFilterTypeDef = None,
        closeStatusFilter: CloseStatusFilterTypeDef = None,
        typeFilter: WorkflowTypeFilterTypeDef = None,
        tagFilter: TagFilterTypeDef = None,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[WorkflowExecutionInfosTypeDef]:
        """
        [ListClosedWorkflowExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.ListClosedWorkflowExecutions.paginate)
        """


class ListDomainsPaginator(Boto3Paginator):
    """
    [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.ListDomains)
    """

    def paginate(
        self,
        registrationStatus: Literal["REGISTERED", "DEPRECATED"],
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DomainInfosTypeDef]:
        """
        [ListDomains.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.ListDomains.paginate)
        """


class ListOpenWorkflowExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListOpenWorkflowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.ListOpenWorkflowExecutions)
    """

    def paginate(
        self,
        domain: str,
        startTimeFilter: ExecutionTimeFilterTypeDef,
        typeFilter: WorkflowTypeFilterTypeDef = None,
        tagFilter: TagFilterTypeDef = None,
        reverseOrder: bool = None,
        executionFilter: WorkflowExecutionFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[WorkflowExecutionInfosTypeDef]:
        """
        [ListOpenWorkflowExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.ListOpenWorkflowExecutions.paginate)
        """


class ListWorkflowTypesPaginator(Boto3Paginator):
    """
    [Paginator.ListWorkflowTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.ListWorkflowTypes)
    """

    def paginate(
        self,
        domain: str,
        registrationStatus: Literal["REGISTERED", "DEPRECATED"],
        name: str = None,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[WorkflowTypeInfosTypeDef]:
        """
        [ListWorkflowTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.ListWorkflowTypes.paginate)
        """


class PollForDecisionTaskPaginator(Boto3Paginator):
    """
    [Paginator.PollForDecisionTask documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.PollForDecisionTask)
    """

    def paginate(
        self,
        domain: str,
        taskList: "TaskListTypeDef",
        identity: str = None,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DecisionTaskTypeDef]:
        """
        [PollForDecisionTask.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/swf.html#SWF.Paginator.PollForDecisionTask.paginate)
        """
