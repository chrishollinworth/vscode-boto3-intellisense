"""
Type annotations for migrationhuborchestrator service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_migrationhuborchestrator.client import MigrationHubOrchestratorClient

    session = Session()
    client: MigrationHubOrchestratorClient = session.client("migrationhuborchestrator")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListPluginsPaginator,
    ListTemplatesPaginator,
    ListTemplateStepGroupsPaginator,
    ListTemplateStepsPaginator,
    ListWorkflowsPaginator,
    ListWorkflowStepGroupsPaginator,
    ListWorkflowStepsPaginator,
)
from .type_defs import (
    CreateMigrationWorkflowRequestTypeDef,
    CreateMigrationWorkflowResponseTypeDef,
    CreateTemplateRequestTypeDef,
    CreateTemplateResponseTypeDef,
    CreateWorkflowStepGroupRequestTypeDef,
    CreateWorkflowStepGroupResponseTypeDef,
    CreateWorkflowStepRequestTypeDef,
    CreateWorkflowStepResponseTypeDef,
    DeleteMigrationWorkflowRequestTypeDef,
    DeleteMigrationWorkflowResponseTypeDef,
    DeleteTemplateRequestTypeDef,
    DeleteWorkflowStepGroupRequestTypeDef,
    DeleteWorkflowStepRequestTypeDef,
    GetMigrationWorkflowRequestTypeDef,
    GetMigrationWorkflowResponseTypeDef,
    GetMigrationWorkflowTemplateRequestTypeDef,
    GetMigrationWorkflowTemplateResponseTypeDef,
    GetTemplateStepGroupRequestTypeDef,
    GetTemplateStepGroupResponseTypeDef,
    GetTemplateStepRequestTypeDef,
    GetTemplateStepResponseTypeDef,
    GetWorkflowStepGroupRequestTypeDef,
    GetWorkflowStepGroupResponseTypeDef,
    GetWorkflowStepRequestTypeDef,
    GetWorkflowStepResponseTypeDef,
    ListMigrationWorkflowsRequestTypeDef,
    ListMigrationWorkflowsResponseTypeDef,
    ListMigrationWorkflowTemplatesRequestTypeDef,
    ListMigrationWorkflowTemplatesResponseTypeDef,
    ListPluginsRequestTypeDef,
    ListPluginsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTemplateStepGroupsRequestTypeDef,
    ListTemplateStepGroupsResponseTypeDef,
    ListTemplateStepsRequestTypeDef,
    ListTemplateStepsResponseTypeDef,
    ListWorkflowStepGroupsRequestTypeDef,
    ListWorkflowStepGroupsResponseTypeDef,
    ListWorkflowStepsRequestTypeDef,
    ListWorkflowStepsResponseTypeDef,
    RetryWorkflowStepRequestTypeDef,
    RetryWorkflowStepResponseTypeDef,
    StartMigrationWorkflowRequestTypeDef,
    StartMigrationWorkflowResponseTypeDef,
    StopMigrationWorkflowRequestTypeDef,
    StopMigrationWorkflowResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateMigrationWorkflowRequestTypeDef,
    UpdateMigrationWorkflowResponseTypeDef,
    UpdateTemplateRequestTypeDef,
    UpdateTemplateResponseTypeDef,
    UpdateWorkflowStepGroupRequestTypeDef,
    UpdateWorkflowStepGroupResponseTypeDef,
    UpdateWorkflowStepRequestTypeDef,
    UpdateWorkflowStepResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("MigrationHubOrchestratorClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class MigrationHubOrchestratorClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MigrationHubOrchestratorClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#generate_presigned_url)
        """

    def create_template(
        self, **kwargs: Unpack[CreateTemplateRequestTypeDef]
    ) -> CreateTemplateResponseTypeDef:
        """
        Creates a migration workflow template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/create_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#create_template)
        """

    def create_workflow(
        self, **kwargs: Unpack[CreateMigrationWorkflowRequestTypeDef]
    ) -> CreateMigrationWorkflowResponseTypeDef:
        """
        Create a workflow to orchestrate your migrations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/create_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#create_workflow)
        """

    def create_workflow_step(
        self, **kwargs: Unpack[CreateWorkflowStepRequestTypeDef]
    ) -> CreateWorkflowStepResponseTypeDef:
        """
        Create a step in the migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/create_workflow_step.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#create_workflow_step)
        """

    def create_workflow_step_group(
        self, **kwargs: Unpack[CreateWorkflowStepGroupRequestTypeDef]
    ) -> CreateWorkflowStepGroupResponseTypeDef:
        """
        Create a step group in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/create_workflow_step_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#create_workflow_step_group)
        """

    def delete_template(self, **kwargs: Unpack[DeleteTemplateRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a migration workflow template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/delete_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#delete_template)
        """

    def delete_workflow(
        self, **kwargs: Unpack[DeleteMigrationWorkflowRequestTypeDef]
    ) -> DeleteMigrationWorkflowResponseTypeDef:
        """
        Delete a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/delete_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#delete_workflow)
        """

    def delete_workflow_step(
        self, **kwargs: Unpack[DeleteWorkflowStepRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete a step in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/delete_workflow_step.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#delete_workflow_step)
        """

    def delete_workflow_step_group(
        self, **kwargs: Unpack[DeleteWorkflowStepGroupRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete a step group in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/delete_workflow_step_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#delete_workflow_step_group)
        """

    def get_template(
        self, **kwargs: Unpack[GetMigrationWorkflowTemplateRequestTypeDef]
    ) -> GetMigrationWorkflowTemplateResponseTypeDef:
        """
        Get the template you want to use for creating a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/get_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_template)
        """

    def get_template_step(
        self, **kwargs: Unpack[GetTemplateStepRequestTypeDef]
    ) -> GetTemplateStepResponseTypeDef:
        """
        Get a specific step in a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/get_template_step.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_template_step)
        """

    def get_template_step_group(
        self, **kwargs: Unpack[GetTemplateStepGroupRequestTypeDef]
    ) -> GetTemplateStepGroupResponseTypeDef:
        """
        Get a step group in a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/get_template_step_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_template_step_group)
        """

    def get_workflow(
        self, **kwargs: Unpack[GetMigrationWorkflowRequestTypeDef]
    ) -> GetMigrationWorkflowResponseTypeDef:
        """
        Get migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/get_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_workflow)
        """

    def get_workflow_step(
        self, **kwargs: Unpack[GetWorkflowStepRequestTypeDef]
    ) -> GetWorkflowStepResponseTypeDef:
        """
        Get a step in the migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/get_workflow_step.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_workflow_step)
        """

    def get_workflow_step_group(
        self, **kwargs: Unpack[GetWorkflowStepGroupRequestTypeDef]
    ) -> GetWorkflowStepGroupResponseTypeDef:
        """
        Get the step group of a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/get_workflow_step_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_workflow_step_group)
        """

    def list_plugins(
        self, **kwargs: Unpack[ListPluginsRequestTypeDef]
    ) -> ListPluginsResponseTypeDef:
        """
        List AWS Migration Hub Orchestrator plugins.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/list_plugins.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#list_plugins)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List the tags added to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#list_tags_for_resource)
        """

    def list_template_step_groups(
        self, **kwargs: Unpack[ListTemplateStepGroupsRequestTypeDef]
    ) -> ListTemplateStepGroupsResponseTypeDef:
        """
        List the step groups in a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/list_template_step_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#list_template_step_groups)
        """

    def list_template_steps(
        self, **kwargs: Unpack[ListTemplateStepsRequestTypeDef]
    ) -> ListTemplateStepsResponseTypeDef:
        """
        List the steps in a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/list_template_steps.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#list_template_steps)
        """

    def list_templates(
        self, **kwargs: Unpack[ListMigrationWorkflowTemplatesRequestTypeDef]
    ) -> ListMigrationWorkflowTemplatesResponseTypeDef:
        """
        List the templates available in Migration Hub Orchestrator to create a
        migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/list_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#list_templates)
        """

    def list_workflow_step_groups(
        self, **kwargs: Unpack[ListWorkflowStepGroupsRequestTypeDef]
    ) -> ListWorkflowStepGroupsResponseTypeDef:
        """
        List the step groups in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/list_workflow_step_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#list_workflow_step_groups)
        """

    def list_workflow_steps(
        self, **kwargs: Unpack[ListWorkflowStepsRequestTypeDef]
    ) -> ListWorkflowStepsResponseTypeDef:
        """
        List the steps in a workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/list_workflow_steps.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#list_workflow_steps)
        """

    def list_workflows(
        self, **kwargs: Unpack[ListMigrationWorkflowsRequestTypeDef]
    ) -> ListMigrationWorkflowsResponseTypeDef:
        """
        List the migration workflows.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/list_workflows.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#list_workflows)
        """

    def retry_workflow_step(
        self, **kwargs: Unpack[RetryWorkflowStepRequestTypeDef]
    ) -> RetryWorkflowStepResponseTypeDef:
        """
        Retry a failed step in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/retry_workflow_step.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#retry_workflow_step)
        """

    def start_workflow(
        self, **kwargs: Unpack[StartMigrationWorkflowRequestTypeDef]
    ) -> StartMigrationWorkflowResponseTypeDef:
        """
        Start a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/start_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#start_workflow)
        """

    def stop_workflow(
        self, **kwargs: Unpack[StopMigrationWorkflowRequestTypeDef]
    ) -> StopMigrationWorkflowResponseTypeDef:
        """
        Stop an ongoing migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/stop_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#stop_workflow)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Tag a resource by specifying its Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#untag_resource)
        """

    def update_template(
        self, **kwargs: Unpack[UpdateTemplateRequestTypeDef]
    ) -> UpdateTemplateResponseTypeDef:
        """
        Updates a migration workflow template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/update_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#update_template)
        """

    def update_workflow(
        self, **kwargs: Unpack[UpdateMigrationWorkflowRequestTypeDef]
    ) -> UpdateMigrationWorkflowResponseTypeDef:
        """
        Update a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/update_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#update_workflow)
        """

    def update_workflow_step(
        self, **kwargs: Unpack[UpdateWorkflowStepRequestTypeDef]
    ) -> UpdateWorkflowStepResponseTypeDef:
        """
        Update a step in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/update_workflow_step.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#update_workflow_step)
        """

    def update_workflow_step_group(
        self, **kwargs: Unpack[UpdateWorkflowStepGroupRequestTypeDef]
    ) -> UpdateWorkflowStepGroupResponseTypeDef:
        """
        Update the step group in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/update_workflow_step_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#update_workflow_step_group)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_plugins"]
    ) -> ListPluginsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_template_step_groups"]
    ) -> ListTemplateStepGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_template_steps"]
    ) -> ListTemplateStepsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_templates"]
    ) -> ListTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workflow_step_groups"]
    ) -> ListWorkflowStepGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workflow_steps"]
    ) -> ListWorkflowStepsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workflows"]
    ) -> ListWorkflowsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client/#get_paginator)
        """
