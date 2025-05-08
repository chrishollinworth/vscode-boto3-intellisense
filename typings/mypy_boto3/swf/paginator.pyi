"""
Type annotations for swf service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_swf.client import SWFClient
    from mypy_boto3_swf.paginator import (
        GetWorkflowExecutionHistoryPaginator,
        ListActivityTypesPaginator,
        ListClosedWorkflowExecutionsPaginator,
        ListDomainsPaginator,
        ListOpenWorkflowExecutionsPaginator,
        ListWorkflowTypesPaginator,
        PollForDecisionTaskPaginator,
    )

    session = Session()
    client: SWFClient = session.client("swf")

    get_workflow_execution_history_paginator: GetWorkflowExecutionHistoryPaginator = client.get_paginator("get_workflow_execution_history")
    list_activity_types_paginator: ListActivityTypesPaginator = client.get_paginator("list_activity_types")
    list_closed_workflow_executions_paginator: ListClosedWorkflowExecutionsPaginator = client.get_paginator("list_closed_workflow_executions")
    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_open_workflow_executions_paginator: ListOpenWorkflowExecutionsPaginator = client.get_paginator("list_open_workflow_executions")
    list_workflow_types_paginator: ListWorkflowTypesPaginator = client.get_paginator("list_workflow_types")
    poll_for_decision_task_paginator: PollForDecisionTaskPaginator = client.get_paginator("poll_for_decision_task")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ActivityTypeInfosTypeDef,
    DecisionTaskTypeDef,
    DomainInfosTypeDef,
    GetWorkflowExecutionHistoryInputPaginateTypeDef,
    HistoryTypeDef,
    ListActivityTypesInputPaginateTypeDef,
    ListClosedWorkflowExecutionsInputPaginateTypeDef,
    ListDomainsInputPaginateTypeDef,
    ListOpenWorkflowExecutionsInputPaginateTypeDef,
    ListWorkflowTypesInputPaginateTypeDef,
    PollForDecisionTaskInputPaginateTypeDef,
    WorkflowExecutionInfosTypeDef,
    WorkflowTypeInfosTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetWorkflowExecutionHistoryPaginator",
    "ListActivityTypesPaginator",
    "ListClosedWorkflowExecutionsPaginator",
    "ListDomainsPaginator",
    "ListOpenWorkflowExecutionsPaginator",
    "ListWorkflowTypesPaginator",
    "PollForDecisionTaskPaginator",
)

if TYPE_CHECKING:
    _GetWorkflowExecutionHistoryPaginatorBase = Paginator[HistoryTypeDef]
else:
    _GetWorkflowExecutionHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class GetWorkflowExecutionHistoryPaginator(_GetWorkflowExecutionHistoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/paginator/GetWorkflowExecutionHistory.html#SWF.Paginator.GetWorkflowExecutionHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators/#getworkflowexecutionhistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetWorkflowExecutionHistoryInputPaginateTypeDef]
    ) -> PageIterator[HistoryTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/paginator/GetWorkflowExecutionHistory.html#SWF.Paginator.GetWorkflowExecutionHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators/#getworkflowexecutionhistorypaginator)
        """

if TYPE_CHECKING:
    _ListActivityTypesPaginatorBase = Paginator[ActivityTypeInfosTypeDef]
else:
    _ListActivityTypesPaginatorBase = Paginator  # type: ignore[assignment]

class ListActivityTypesPaginator(_ListActivityTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/paginator/ListActivityTypes.html#SWF.Paginator.ListActivityTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators/#listactivitytypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListActivityTypesInputPaginateTypeDef]
    ) -> PageIterator[ActivityTypeInfosTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/paginator/ListActivityTypes.html#SWF.Paginator.ListActivityTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators/#listactivitytypespaginator)
        """

if TYPE_CHECKING:
    _ListClosedWorkflowExecutionsPaginatorBase = Paginator[WorkflowExecutionInfosTypeDef]
else:
    _ListClosedWorkflowExecutionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListClosedWorkflowExecutionsPaginator(_ListClosedWorkflowExecutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/paginator/ListClosedWorkflowExecutions.html#SWF.Paginator.ListClosedWorkflowExecutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators/#listclosedworkflowexecutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListClosedWorkflowExecutionsInputPaginateTypeDef]
    ) -> PageIterator[WorkflowExecutionInfosTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/paginator/ListClosedWorkflowExecutions.html#SWF.Paginator.ListClosedWorkflowExecutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators/#listclosedworkflowexecutionspaginator)
        """

if TYPE_CHECKING:
    _ListDomainsPaginatorBase = Paginator[DomainInfosTypeDef]
else:
    _ListDomainsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDomainsPaginator(_ListDomainsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/paginator/ListDomains.html#SWF.Paginator.ListDomains)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators/#listdomainspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDomainsInputPaginateTypeDef]
    ) -> PageIterator[DomainInfosTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/paginator/ListDomains.html#SWF.Paginator.ListDomains.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators/#listdomainspaginator)
        """

if TYPE_CHECKING:
    _ListOpenWorkflowExecutionsPaginatorBase = Paginator[WorkflowExecutionInfosTypeDef]
else:
    _ListOpenWorkflowExecutionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOpenWorkflowExecutionsPaginator(_ListOpenWorkflowExecutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/paginator/ListOpenWorkflowExecutions.html#SWF.Paginator.ListOpenWorkflowExecutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators/#listopenworkflowexecutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOpenWorkflowExecutionsInputPaginateTypeDef]
    ) -> PageIterator[WorkflowExecutionInfosTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/paginator/ListOpenWorkflowExecutions.html#SWF.Paginator.ListOpenWorkflowExecutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators/#listopenworkflowexecutionspaginator)
        """

if TYPE_CHECKING:
    _ListWorkflowTypesPaginatorBase = Paginator[WorkflowTypeInfosTypeDef]
else:
    _ListWorkflowTypesPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkflowTypesPaginator(_ListWorkflowTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/paginator/ListWorkflowTypes.html#SWF.Paginator.ListWorkflowTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators/#listworkflowtypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkflowTypesInputPaginateTypeDef]
    ) -> PageIterator[WorkflowTypeInfosTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/paginator/ListWorkflowTypes.html#SWF.Paginator.ListWorkflowTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators/#listworkflowtypespaginator)
        """

if TYPE_CHECKING:
    _PollForDecisionTaskPaginatorBase = Paginator[DecisionTaskTypeDef]
else:
    _PollForDecisionTaskPaginatorBase = Paginator  # type: ignore[assignment]

class PollForDecisionTaskPaginator(_PollForDecisionTaskPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/paginator/PollForDecisionTask.html#SWF.Paginator.PollForDecisionTask)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators/#pollfordecisiontaskpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[PollForDecisionTaskInputPaginateTypeDef]
    ) -> PageIterator[DecisionTaskTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf/paginator/PollForDecisionTask.html#SWF.Paginator.PollForDecisionTask.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/paginators/#pollfordecisiontaskpaginator)
        """
