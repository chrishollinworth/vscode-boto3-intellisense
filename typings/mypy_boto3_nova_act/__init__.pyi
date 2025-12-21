"""
Main interface for nova-act service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_nova_act import (
        Client,
        ListActsPaginator,
        ListSessionsPaginator,
        ListWorkflowDefinitionsPaginator,
        ListWorkflowRunsPaginator,
        NovaActServiceClient,
    )

    session = Session()
    client: NovaActServiceClient = session.client("nova-act")

    list_acts_paginator: ListActsPaginator = client.get_paginator("list_acts")
    list_sessions_paginator: ListSessionsPaginator = client.get_paginator("list_sessions")
    list_workflow_definitions_paginator: ListWorkflowDefinitionsPaginator = client.get_paginator("list_workflow_definitions")
    list_workflow_runs_paginator: ListWorkflowRunsPaginator = client.get_paginator("list_workflow_runs")
    ```
"""

from .client import NovaActServiceClient
from .paginator import (
    ListActsPaginator,
    ListSessionsPaginator,
    ListWorkflowDefinitionsPaginator,
    ListWorkflowRunsPaginator,
)

Client = NovaActServiceClient

__all__ = (
    "Client",
    "ListActsPaginator",
    "ListSessionsPaginator",
    "ListWorkflowDefinitionsPaginator",
    "ListWorkflowRunsPaginator",
    "NovaActServiceClient",
)
