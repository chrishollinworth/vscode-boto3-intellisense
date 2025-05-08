"""
Type annotations for migrationhuborchestrator service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_migrationhuborchestrator.client import MigrationHubOrchestratorClient
    from mypy_boto3_migrationhuborchestrator.paginator import (
        ListPluginsPaginator,
        ListTemplateStepGroupsPaginator,
        ListTemplateStepsPaginator,
        ListTemplatesPaginator,
        ListWorkflowStepGroupsPaginator,
        ListWorkflowStepsPaginator,
        ListWorkflowsPaginator,
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListMigrationWorkflowsRequestPaginateTypeDef,
    ListMigrationWorkflowsResponseTypeDef,
    ListMigrationWorkflowTemplatesRequestPaginateTypeDef,
    ListMigrationWorkflowTemplatesResponseTypeDef,
    ListPluginsRequestPaginateTypeDef,
    ListPluginsResponseTypeDef,
    ListTemplateStepGroupsRequestPaginateTypeDef,
    ListTemplateStepGroupsResponseTypeDef,
    ListTemplateStepsRequestPaginateTypeDef,
    ListTemplateStepsResponseTypeDef,
    ListWorkflowStepGroupsRequestPaginateTypeDef,
    ListWorkflowStepGroupsResponseTypeDef,
    ListWorkflowStepsRequestPaginateTypeDef,
    ListWorkflowStepsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListPluginsPaginator",
    "ListTemplateStepGroupsPaginator",
    "ListTemplateStepsPaginator",
    "ListTemplatesPaginator",
    "ListWorkflowStepGroupsPaginator",
    "ListWorkflowStepsPaginator",
    "ListWorkflowsPaginator",
)

if TYPE_CHECKING:
    _ListPluginsPaginatorBase = Paginator[ListPluginsResponseTypeDef]
else:
    _ListPluginsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPluginsPaginator(_ListPluginsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/paginator/ListPlugins.html#MigrationHubOrchestrator.Paginator.ListPlugins)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators/#listpluginspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPluginsRequestPaginateTypeDef]
    ) -> PageIterator[ListPluginsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/paginator/ListPlugins.html#MigrationHubOrchestrator.Paginator.ListPlugins.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators/#listpluginspaginator)
        """

if TYPE_CHECKING:
    _ListTemplateStepGroupsPaginatorBase = Paginator[ListTemplateStepGroupsResponseTypeDef]
else:
    _ListTemplateStepGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTemplateStepGroupsPaginator(_ListTemplateStepGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/paginator/ListTemplateStepGroups.html#MigrationHubOrchestrator.Paginator.ListTemplateStepGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators/#listtemplatestepgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTemplateStepGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListTemplateStepGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/paginator/ListTemplateStepGroups.html#MigrationHubOrchestrator.Paginator.ListTemplateStepGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators/#listtemplatestepgroupspaginator)
        """

if TYPE_CHECKING:
    _ListTemplateStepsPaginatorBase = Paginator[ListTemplateStepsResponseTypeDef]
else:
    _ListTemplateStepsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTemplateStepsPaginator(_ListTemplateStepsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/paginator/ListTemplateSteps.html#MigrationHubOrchestrator.Paginator.ListTemplateSteps)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators/#listtemplatestepspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTemplateStepsRequestPaginateTypeDef]
    ) -> PageIterator[ListTemplateStepsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/paginator/ListTemplateSteps.html#MigrationHubOrchestrator.Paginator.ListTemplateSteps.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators/#listtemplatestepspaginator)
        """

if TYPE_CHECKING:
    _ListTemplatesPaginatorBase = Paginator[ListMigrationWorkflowTemplatesResponseTypeDef]
else:
    _ListTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTemplatesPaginator(_ListTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/paginator/ListTemplates.html#MigrationHubOrchestrator.Paginator.ListTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators/#listtemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMigrationWorkflowTemplatesRequestPaginateTypeDef]
    ) -> PageIterator[ListMigrationWorkflowTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/paginator/ListTemplates.html#MigrationHubOrchestrator.Paginator.ListTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators/#listtemplatespaginator)
        """

if TYPE_CHECKING:
    _ListWorkflowStepGroupsPaginatorBase = Paginator[ListWorkflowStepGroupsResponseTypeDef]
else:
    _ListWorkflowStepGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkflowStepGroupsPaginator(_ListWorkflowStepGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/paginator/ListWorkflowStepGroups.html#MigrationHubOrchestrator.Paginator.ListWorkflowStepGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators/#listworkflowstepgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkflowStepGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkflowStepGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/paginator/ListWorkflowStepGroups.html#MigrationHubOrchestrator.Paginator.ListWorkflowStepGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators/#listworkflowstepgroupspaginator)
        """

if TYPE_CHECKING:
    _ListWorkflowStepsPaginatorBase = Paginator[ListWorkflowStepsResponseTypeDef]
else:
    _ListWorkflowStepsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkflowStepsPaginator(_ListWorkflowStepsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/paginator/ListWorkflowSteps.html#MigrationHubOrchestrator.Paginator.ListWorkflowSteps)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators/#listworkflowstepspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkflowStepsRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkflowStepsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/paginator/ListWorkflowSteps.html#MigrationHubOrchestrator.Paginator.ListWorkflowSteps.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators/#listworkflowstepspaginator)
        """

if TYPE_CHECKING:
    _ListWorkflowsPaginatorBase = Paginator[ListMigrationWorkflowsResponseTypeDef]
else:
    _ListWorkflowsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkflowsPaginator(_ListWorkflowsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/paginator/ListWorkflows.html#MigrationHubOrchestrator.Paginator.ListWorkflows)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators/#listworkflowspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMigrationWorkflowsRequestPaginateTypeDef]
    ) -> PageIterator[ListMigrationWorkflowsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator/paginator/ListWorkflows.html#MigrationHubOrchestrator.Paginator.ListWorkflows.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/paginators/#listworkflowspaginator)
        """
