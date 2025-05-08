"""
Main interface for swf service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_swf import (
        Client,
        GetWorkflowExecutionHistoryPaginator,
        ListActivityTypesPaginator,
        ListClosedWorkflowExecutionsPaginator,
        ListDomainsPaginator,
        ListOpenWorkflowExecutionsPaginator,
        ListWorkflowTypesPaginator,
        PollForDecisionTaskPaginator,
        SWFClient,
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

from .client import SWFClient
from .paginator import (
    GetWorkflowExecutionHistoryPaginator,
    ListActivityTypesPaginator,
    ListClosedWorkflowExecutionsPaginator,
    ListDomainsPaginator,
    ListOpenWorkflowExecutionsPaginator,
    ListWorkflowTypesPaginator,
    PollForDecisionTaskPaginator,
)

Client = SWFClient

__all__ = (
    "Client",
    "GetWorkflowExecutionHistoryPaginator",
    "ListActivityTypesPaginator",
    "ListClosedWorkflowExecutionsPaginator",
    "ListDomainsPaginator",
    "ListOpenWorkflowExecutionsPaginator",
    "ListWorkflowTypesPaginator",
    "PollForDecisionTaskPaginator",
    "SWFClient",
)
