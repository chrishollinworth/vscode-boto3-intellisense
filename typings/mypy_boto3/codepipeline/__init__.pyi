"""
Main interface for codepipeline service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_codepipeline import (
        Client,
        CodePipelineClient,
        ListActionExecutionsPaginator,
        ListActionTypesPaginator,
        ListDeployActionExecutionTargetsPaginator,
        ListPipelineExecutionsPaginator,
        ListPipelinesPaginator,
        ListRuleExecutionsPaginator,
        ListTagsForResourcePaginator,
        ListWebhooksPaginator,
    )

    session = Session()
    client: CodePipelineClient = session.client("codepipeline")

    list_action_executions_paginator: ListActionExecutionsPaginator = client.get_paginator("list_action_executions")
    list_action_types_paginator: ListActionTypesPaginator = client.get_paginator("list_action_types")
    list_deploy_action_execution_targets_paginator: ListDeployActionExecutionTargetsPaginator = client.get_paginator("list_deploy_action_execution_targets")
    list_pipeline_executions_paginator: ListPipelineExecutionsPaginator = client.get_paginator("list_pipeline_executions")
    list_pipelines_paginator: ListPipelinesPaginator = client.get_paginator("list_pipelines")
    list_rule_executions_paginator: ListRuleExecutionsPaginator = client.get_paginator("list_rule_executions")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_webhooks_paginator: ListWebhooksPaginator = client.get_paginator("list_webhooks")
    ```
"""

from .client import CodePipelineClient
from .paginator import (
    ListActionExecutionsPaginator,
    ListActionTypesPaginator,
    ListDeployActionExecutionTargetsPaginator,
    ListPipelineExecutionsPaginator,
    ListPipelinesPaginator,
    ListRuleExecutionsPaginator,
    ListTagsForResourcePaginator,
    ListWebhooksPaginator,
)

Client = CodePipelineClient

__all__ = (
    "Client",
    "CodePipelineClient",
    "ListActionExecutionsPaginator",
    "ListActionTypesPaginator",
    "ListDeployActionExecutionTargetsPaginator",
    "ListPipelineExecutionsPaginator",
    "ListPipelinesPaginator",
    "ListRuleExecutionsPaginator",
    "ListTagsForResourcePaginator",
    "ListWebhooksPaginator",
)
