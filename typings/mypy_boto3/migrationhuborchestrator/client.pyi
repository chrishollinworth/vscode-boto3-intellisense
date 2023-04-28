"""
Type annotations for migrationhuborchestrator service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_migrationhuborchestrator import MigrationHubOrchestratorClient

    client: MigrationHubOrchestratorClient = boto3.client("migrationhuborchestrator")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import MigrationWorkflowStatusEnumType, StepActionTypeType, StepStatusType
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
    CreateMigrationWorkflowResponseTypeDef,
    CreateWorkflowStepGroupResponseTypeDef,
    CreateWorkflowStepResponseTypeDef,
    DeleteMigrationWorkflowResponseTypeDef,
    GetMigrationWorkflowResponseTypeDef,
    GetMigrationWorkflowTemplateResponseTypeDef,
    GetTemplateStepGroupResponseTypeDef,
    GetTemplateStepResponseTypeDef,
    GetWorkflowStepGroupResponseTypeDef,
    GetWorkflowStepResponseTypeDef,
    ListMigrationWorkflowsResponseTypeDef,
    ListMigrationWorkflowTemplatesResponseTypeDef,
    ListPluginsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTemplateStepGroupsResponseTypeDef,
    ListTemplateStepsResponseTypeDef,
    ListWorkflowStepGroupsResponseTypeDef,
    ListWorkflowStepsResponseTypeDef,
    RetryWorkflowStepResponseTypeDef,
    StartMigrationWorkflowResponseTypeDef,
    StepInputTypeDef,
    StopMigrationWorkflowResponseTypeDef,
    UpdateMigrationWorkflowResponseTypeDef,
    UpdateWorkflowStepGroupResponseTypeDef,
    UpdateWorkflowStepResponseTypeDef,
    WorkflowStepAutomationConfigurationTypeDef,
    WorkflowStepOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("MigrationHubOrchestratorClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class MigrationHubOrchestratorClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MigrationHubOrchestratorClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#close)
        """
    def create_workflow(
        self,
        *,
        name: str,
        templateId: str,
        applicationConfigurationId: str,
        inputParameters: Dict[str, "StepInputTypeDef"],
        description: str = None,
        stepTargets: List[str] = None,
        tags: Dict[str, str] = None
    ) -> CreateMigrationWorkflowResponseTypeDef:
        """
        Create a workflow to orchestrate your migrations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.create_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#create_workflow)
        """
    def create_workflow_step(
        self,
        *,
        name: str,
        stepGroupId: str,
        workflowId: str,
        stepActionType: StepActionTypeType,
        description: str = None,
        workflowStepAutomationConfiguration: "WorkflowStepAutomationConfigurationTypeDef" = None,
        stepTarget: List[str] = None,
        outputs: List["WorkflowStepOutputTypeDef"] = None,
        previous: List[str] = None,
        next: List[str] = None
    ) -> CreateWorkflowStepResponseTypeDef:
        """
        Create a step in the migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.create_workflow_step)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#create_workflow_step)
        """
    def create_workflow_step_group(
        self,
        *,
        workflowId: str,
        name: str,
        description: str = None,
        next: List[str] = None,
        previous: List[str] = None
    ) -> CreateWorkflowStepGroupResponseTypeDef:
        """
        Create a step group in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.create_workflow_step_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#create_workflow_step_group)
        """
    def delete_workflow(self, *, id: str) -> DeleteMigrationWorkflowResponseTypeDef:
        """
        Delete a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.delete_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#delete_workflow)
        """
    def delete_workflow_step(self, *, id: str, stepGroupId: str, workflowId: str) -> Dict[str, Any]:
        """
        Delete a step in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.delete_workflow_step)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#delete_workflow_step)
        """
    def delete_workflow_step_group(self, *, workflowId: str, id: str) -> Dict[str, Any]:
        """
        Delete a step group in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.delete_workflow_step_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#delete_workflow_step_group)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#generate_presigned_url)
        """
    def get_template(self, *, id: str) -> GetMigrationWorkflowTemplateResponseTypeDef:
        """
        Get the template you want to use for creating a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#get_template)
        """
    def get_template_step(
        self, *, id: str, templateId: str, stepGroupId: str
    ) -> GetTemplateStepResponseTypeDef:
        """
        Get a specific step in a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_template_step)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#get_template_step)
        """
    def get_template_step_group(
        self, *, templateId: str, id: str
    ) -> GetTemplateStepGroupResponseTypeDef:
        """
        Get a step group in a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_template_step_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#get_template_step_group)
        """
    def get_workflow(self, *, id: str) -> GetMigrationWorkflowResponseTypeDef:
        """
        Get migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#get_workflow)
        """
    def get_workflow_step(
        self, *, workflowId: str, stepGroupId: str, id: str
    ) -> GetWorkflowStepResponseTypeDef:
        """
        Get a step in the migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_workflow_step)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#get_workflow_step)
        """
    def get_workflow_step_group(
        self, *, id: str, workflowId: str
    ) -> GetWorkflowStepGroupResponseTypeDef:
        """
        Get the step group of a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.get_workflow_step_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#get_workflow_step_group)
        """
    def list_plugins(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListPluginsResponseTypeDef:
        """
        List AWS Migration Hub Orchestrator plugins.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_plugins)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#list_plugins)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        List the tags added to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#list_tags_for_resource)
        """
    def list_template_step_groups(
        self, *, templateId: str, maxResults: int = None, nextToken: str = None
    ) -> ListTemplateStepGroupsResponseTypeDef:
        """
        List the step groups in a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_template_step_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#list_template_step_groups)
        """
    def list_template_steps(
        self, *, templateId: str, stepGroupId: str, maxResults: int = None, nextToken: str = None
    ) -> ListTemplateStepsResponseTypeDef:
        """
        List the steps in a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_template_steps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#list_template_steps)
        """
    def list_templates(
        self, *, maxResults: int = None, nextToken: str = None, name: str = None
    ) -> ListMigrationWorkflowTemplatesResponseTypeDef:
        """
        List the templates available in Migration Hub Orchestrator to create a migration
        workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#list_templates)
        """
    def list_workflow_step_groups(
        self, *, workflowId: str, nextToken: str = None, maxResults: int = None
    ) -> ListWorkflowStepGroupsResponseTypeDef:
        """
        List the step groups in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_workflow_step_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#list_workflow_step_groups)
        """
    def list_workflow_steps(
        self, *, workflowId: str, stepGroupId: str, nextToken: str = None, maxResults: int = None
    ) -> ListWorkflowStepsResponseTypeDef:
        """
        List the steps in a workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_workflow_steps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#list_workflow_steps)
        """
    def list_workflows(
        self,
        *,
        maxResults: int = None,
        nextToken: str = None,
        templateId: str = None,
        adsApplicationConfigurationName: str = None,
        status: MigrationWorkflowStatusEnumType = None,
        name: str = None
    ) -> ListMigrationWorkflowsResponseTypeDef:
        """
        List the migration workflows.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.list_workflows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#list_workflows)
        """
    def retry_workflow_step(
        self, *, workflowId: str, stepGroupId: str, id: str
    ) -> RetryWorkflowStepResponseTypeDef:
        """
        Retry a failed step in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.retry_workflow_step)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#retry_workflow_step)
        """
    def start_workflow(self, *, id: str) -> StartMigrationWorkflowResponseTypeDef:
        """
        Start a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.start_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#start_workflow)
        """
    def stop_workflow(self, *, id: str) -> StopMigrationWorkflowResponseTypeDef:
        """
        Stop an ongoing migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.stop_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#stop_workflow)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Tag a resource by specifying its Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Deletes the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#untag_resource)
        """
    def update_workflow(
        self,
        *,
        id: str,
        name: str = None,
        description: str = None,
        inputParameters: Dict[str, "StepInputTypeDef"] = None,
        stepTargets: List[str] = None
    ) -> UpdateMigrationWorkflowResponseTypeDef:
        """
        Update a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.update_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#update_workflow)
        """
    def update_workflow_step(
        self,
        *,
        id: str,
        stepGroupId: str,
        workflowId: str,
        name: str = None,
        description: str = None,
        stepActionType: StepActionTypeType = None,
        workflowStepAutomationConfiguration: "WorkflowStepAutomationConfigurationTypeDef" = None,
        stepTarget: List[str] = None,
        outputs: List["WorkflowStepOutputTypeDef"] = None,
        previous: List[str] = None,
        next: List[str] = None,
        status: StepStatusType = None
    ) -> UpdateWorkflowStepResponseTypeDef:
        """
        Update a step in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.update_workflow_step)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#update_workflow_step)
        """
    def update_workflow_step_group(
        self,
        *,
        workflowId: str,
        id: str,
        name: str = None,
        description: str = None,
        next: List[str] = None,
        previous: List[str] = None
    ) -> UpdateWorkflowStepGroupResponseTypeDef:
        """
        Update the step group in a migration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Client.update_workflow_step_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/client.html#update_workflow_step_group)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_plugins"]) -> ListPluginsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListPlugins)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listpluginspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_template_step_groups"]
    ) -> ListTemplateStepGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListTemplateStepGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listtemplatestepgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_template_steps"]
    ) -> ListTemplateStepsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListTemplateSteps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listtemplatestepspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_templates"]) -> ListTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listtemplatespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_workflow_step_groups"]
    ) -> ListWorkflowStepGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListWorkflowStepGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listworkflowstepgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_workflow_steps"]
    ) -> ListWorkflowStepsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListWorkflowSteps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listworkflowstepspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_workflows"]) -> ListWorkflowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListWorkflows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listworkflowspaginator)
        """
