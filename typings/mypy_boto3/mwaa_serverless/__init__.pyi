"""
Main interface for mwaa-serverless service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mwaa_serverless import (
        Client,
        ListTaskInstancesPaginator,
        ListWorkflowRunsPaginator,
        ListWorkflowVersionsPaginator,
        ListWorkflowsPaginator,
        MWAAServerlessClient,
    )

    session = Session()
    client: MWAAServerlessClient = session.client("mwaa-serverless")

    list_task_instances_paginator: ListTaskInstancesPaginator = client.get_paginator("list_task_instances")
    list_workflow_runs_paginator: ListWorkflowRunsPaginator = client.get_paginator("list_workflow_runs")
    list_workflow_versions_paginator: ListWorkflowVersionsPaginator = client.get_paginator("list_workflow_versions")
    list_workflows_paginator: ListWorkflowsPaginator = client.get_paginator("list_workflows")
    ```
"""

from .client import MWAAServerlessClient
from .paginator import (
    ListTaskInstancesPaginator,
    ListWorkflowRunsPaginator,
    ListWorkflowsPaginator,
    ListWorkflowVersionsPaginator,
)

Client = MWAAServerlessClient

__all__ = (
    "Client",
    "ListTaskInstancesPaginator",
    "ListWorkflowRunsPaginator",
    "ListWorkflowVersionsPaginator",
    "ListWorkflowsPaginator",
    "MWAAServerlessClient",
)
