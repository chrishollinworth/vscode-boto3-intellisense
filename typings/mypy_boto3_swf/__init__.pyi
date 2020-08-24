"""
Main interface for swf service.

Usage::

    ```python
    import boto3
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

    session = boto3.Session()

    client: SWFClient = boto3.client("swf")
    session_client: SWFClient = session.client("swf")

    get_workflow_execution_history_paginator: GetWorkflowExecutionHistoryPaginator = client.get_paginator("get_workflow_execution_history")
    list_activity_types_paginator: ListActivityTypesPaginator = client.get_paginator("list_activity_types")
    list_closed_workflow_executions_paginator: ListClosedWorkflowExecutionsPaginator = client.get_paginator("list_closed_workflow_executions")
    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_open_workflow_executions_paginator: ListOpenWorkflowExecutionsPaginator = client.get_paginator("list_open_workflow_executions")
    list_workflow_types_paginator: ListWorkflowTypesPaginator = client.get_paginator("list_workflow_types")
    poll_for_decision_task_paginator: PollForDecisionTaskPaginator = client.get_paginator("poll_for_decision_task")
    ```
"""
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
