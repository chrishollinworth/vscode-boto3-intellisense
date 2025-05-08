"""
Main interface for migrationhuborchestrator service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_migrationhuborchestrator import (
        Client,
        ListPluginsPaginator,
        ListTemplateStepGroupsPaginator,
        ListTemplateStepsPaginator,
        ListTemplatesPaginator,
        ListWorkflowStepGroupsPaginator,
        ListWorkflowStepsPaginator,
        ListWorkflowsPaginator,
        MigrationHubOrchestratorClient,
    )

    session = Session()
    client: MigrationHubOrchestratorClient = session.client("migrationhuborchestrator")

    list_plugins_paginator: ListPluginsPaginator = client.get_paginator("list_plugins")
    list_template_step_groups_paginator: ListTemplateStepGroupsPaginator = client.get_paginator("list_template_step_groups")
    list_template_steps_paginator: ListTemplateStepsPaginator = client.get_paginator("list_template_steps")
    list_templates_paginator: ListTemplatesPaginator = client.get_paginator("list_templates")
    list_workflow_step_groups_paginator: ListWorkflowStepGroupsPaginator = client.get_paginator("list_workflow_step_groups")
    list_workflow_steps_paginator: ListWorkflowStepsPaginator = client.get_paginator("list_workflow_steps")
    list_workflows_paginator: ListWorkflowsPaginator = client.get_paginator("list_workflows")
    ```
"""

from .client import MigrationHubOrchestratorClient
from .paginator import (
    ListPluginsPaginator,
    ListTemplatesPaginator,
    ListTemplateStepGroupsPaginator,
    ListTemplateStepsPaginator,
    ListWorkflowsPaginator,
    ListWorkflowStepGroupsPaginator,
    ListWorkflowStepsPaginator,
)

Client = MigrationHubOrchestratorClient

__all__ = (
    "Client",
    "ListPluginsPaginator",
    "ListTemplateStepGroupsPaginator",
    "ListTemplateStepsPaginator",
    "ListTemplatesPaginator",
    "ListWorkflowStepGroupsPaginator",
    "ListWorkflowStepsPaginator",
    "ListWorkflowsPaginator",
    "MigrationHubOrchestratorClient",
)
