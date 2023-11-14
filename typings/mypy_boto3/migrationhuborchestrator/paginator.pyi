"""
Type annotations for migrationhuborchestrator service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_migrationhuborchestrator import MigrationHubOrchestratorClient
    from mypy_boto3_migrationhuborchestrator.paginator import (
        ListPluginsPaginator,
        ListTemplateStepGroupsPaginator,
        ListTemplateStepsPaginator,
        ListTemplatesPaginator,
        ListWorkflowStepGroupsPaginator,
        ListWorkflowStepsPaginator,
        ListWorkflowsPaginator,
    )

    client: MigrationHubOrchestratorClient = boto3.client("migrationhuborchestrator")

    list_plugins_paginator: ListPluginsPaginator = client.get_paginator("list_plugins")
    list_template_step_groups_paginator: ListTemplateStepGroupsPaginator = client.get_paginator("list_template_step_groups")
    list_template_steps_paginator: ListTemplateStepsPaginator = client.get_paginator("list_template_steps")
    list_templates_paginator: ListTemplatesPaginator = client.get_paginator("list_templates")
    list_workflow_step_groups_paginator: ListWorkflowStepGroupsPaginator = client.get_paginator("list_workflow_step_groups")
    list_workflow_steps_paginator: ListWorkflowStepsPaginator = client.get_paginator("list_workflow_steps")
    list_workflows_paginator: ListWorkflowsPaginator = client.get_paginator("list_workflows")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import MigrationWorkflowStatusEnumType
from .type_defs import (
    ListMigrationWorkflowsResponseTypeDef,
    ListMigrationWorkflowTemplatesResponseTypeDef,
    ListPluginsResponseTypeDef,
    ListTemplateStepGroupsResponseTypeDef,
    ListTemplateStepsResponseTypeDef,
    ListWorkflowStepGroupsResponseTypeDef,
    ListWorkflowStepsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListPluginsPaginator",
    "ListTemplateStepGroupsPaginator",
    "ListTemplateStepsPaginator",
    "ListTemplatesPaginator",
    "ListWorkflowStepGroupsPaginator",
    "ListWorkflowStepsPaginator",
    "ListWorkflowsPaginator",
)

class ListPluginsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListPlugins)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listpluginspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPluginsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListPlugins.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listpluginspaginator)
        """

class ListTemplateStepGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListTemplateStepGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listtemplatestepgroupspaginator)
    """

    def paginate(
        self, *, templateId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTemplateStepGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListTemplateStepGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listtemplatestepgroupspaginator)
        """

class ListTemplateStepsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListTemplateSteps)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listtemplatestepspaginator)
    """

    def paginate(
        self, *, templateId: str, stepGroupId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTemplateStepsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListTemplateSteps.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listtemplatestepspaginator)
        """

class ListTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listtemplatespaginator)
    """

    def paginate(
        self, *, name: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMigrationWorkflowTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listtemplatespaginator)
        """

class ListWorkflowStepGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListWorkflowStepGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listworkflowstepgroupspaginator)
    """

    def paginate(
        self, *, workflowId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkflowStepGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListWorkflowStepGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listworkflowstepgroupspaginator)
        """

class ListWorkflowStepsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListWorkflowSteps)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listworkflowstepspaginator)
    """

    def paginate(
        self, *, workflowId: str, stepGroupId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkflowStepsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListWorkflowSteps.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listworkflowstepspaginator)
        """

class ListWorkflowsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListWorkflows)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listworkflowspaginator)
    """

    def paginate(
        self,
        *,
        templateId: str = None,
        adsApplicationConfigurationName: str = None,
        status: MigrationWorkflowStatusEnumType = None,
        name: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMigrationWorkflowsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/migrationhuborchestrator.html#MigrationHubOrchestrator.Paginator.ListWorkflows.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators.html#listworkflowspaginator)
        """
