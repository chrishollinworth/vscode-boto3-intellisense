"""
Type annotations for swf service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html)

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
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import RegistrationStatusType
from .type_defs import (
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/swf.html#SWF.Paginator.GetWorkflowExecutionHistory)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#getworkflowexecutionhistorypaginator)
    """

    def paginate(
        self,
        *,
        domain: str,
        execution: "WorkflowExecutionTypeDef",
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[HistoryTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/swf.html#SWF.Paginator.GetWorkflowExecutionHistory.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#getworkflowexecutionhistorypaginator)
        """

class ListActivityTypesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/swf.html#SWF.Paginator.ListActivityTypes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#listactivitytypespaginator)
    """

    def paginate(
        self,
        *,
        domain: str,
        registrationStatus: RegistrationStatusType,
        name: str = None,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ActivityTypeInfosTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/swf.html#SWF.Paginator.ListActivityTypes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#listactivitytypespaginator)
        """

class ListClosedWorkflowExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/swf.html#SWF.Paginator.ListClosedWorkflowExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#listclosedworkflowexecutionspaginator)
    """

    def paginate(
        self,
        *,
        domain: str,
        startTimeFilter: "ExecutionTimeFilterTypeDef" = None,
        closeTimeFilter: "ExecutionTimeFilterTypeDef" = None,
        executionFilter: "WorkflowExecutionFilterTypeDef" = None,
        closeStatusFilter: "CloseStatusFilterTypeDef" = None,
        typeFilter: "WorkflowTypeFilterTypeDef" = None,
        tagFilter: "TagFilterTypeDef" = None,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[WorkflowExecutionInfosTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/swf.html#SWF.Paginator.ListClosedWorkflowExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#listclosedworkflowexecutionspaginator)
        """

class ListDomainsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/swf.html#SWF.Paginator.ListDomains)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#listdomainspaginator)
    """

    def paginate(
        self,
        *,
        registrationStatus: RegistrationStatusType,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DomainInfosTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/swf.html#SWF.Paginator.ListDomains.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#listdomainspaginator)
        """

class ListOpenWorkflowExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/swf.html#SWF.Paginator.ListOpenWorkflowExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#listopenworkflowexecutionspaginator)
    """

    def paginate(
        self,
        *,
        domain: str,
        startTimeFilter: "ExecutionTimeFilterTypeDef",
        typeFilter: "WorkflowTypeFilterTypeDef" = None,
        tagFilter: "TagFilterTypeDef" = None,
        reverseOrder: bool = None,
        executionFilter: "WorkflowExecutionFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[WorkflowExecutionInfosTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/swf.html#SWF.Paginator.ListOpenWorkflowExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#listopenworkflowexecutionspaginator)
        """

class ListWorkflowTypesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/swf.html#SWF.Paginator.ListWorkflowTypes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#listworkflowtypespaginator)
    """

    def paginate(
        self,
        *,
        domain: str,
        registrationStatus: RegistrationStatusType,
        name: str = None,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[WorkflowTypeInfosTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/swf.html#SWF.Paginator.ListWorkflowTypes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#listworkflowtypespaginator)
        """

class PollForDecisionTaskPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/swf.html#SWF.Paginator.PollForDecisionTask)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#pollfordecisiontaskpaginator)
    """

    def paginate(
        self,
        *,
        domain: str,
        taskList: "TaskListTypeDef",
        identity: str = None,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DecisionTaskTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/swf.html#SWF.Paginator.PollForDecisionTask.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators.html#pollfordecisiontaskpaginator)
        """
