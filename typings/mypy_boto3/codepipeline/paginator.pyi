"""
Type annotations for codepipeline service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_codepipeline.client import CodePipelineClient
    from mypy_boto3_codepipeline.paginator import (
        ListActionExecutionsPaginator,
        ListActionTypesPaginator,
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
    list_pipeline_executions_paginator: ListPipelineExecutionsPaginator = client.get_paginator("list_pipeline_executions")
    list_pipelines_paginator: ListPipelinesPaginator = client.get_paginator("list_pipelines")
    list_rule_executions_paginator: ListRuleExecutionsPaginator = client.get_paginator("list_rule_executions")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_webhooks_paginator: ListWebhooksPaginator = client.get_paginator("list_webhooks")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListActionExecutionsInputPaginateTypeDef,
    ListActionExecutionsOutputTypeDef,
    ListActionTypesInputPaginateTypeDef,
    ListActionTypesOutputTypeDef,
    ListPipelineExecutionsInputPaginateTypeDef,
    ListPipelineExecutionsOutputTypeDef,
    ListPipelinesInputPaginateTypeDef,
    ListPipelinesOutputTypeDef,
    ListRuleExecutionsInputPaginateTypeDef,
    ListRuleExecutionsOutputTypeDef,
    ListTagsForResourceInputPaginateTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListWebhooksInputPaginateTypeDef,
    ListWebhooksOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListActionExecutionsPaginator",
    "ListActionTypesPaginator",
    "ListPipelineExecutionsPaginator",
    "ListPipelinesPaginator",
    "ListRuleExecutionsPaginator",
    "ListTagsForResourcePaginator",
    "ListWebhooksPaginator",
)

if TYPE_CHECKING:
    _ListActionExecutionsPaginatorBase = Paginator[ListActionExecutionsOutputTypeDef]
else:
    _ListActionExecutionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListActionExecutionsPaginator(_ListActionExecutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/paginator/ListActionExecutions.html#CodePipeline.Paginator.ListActionExecutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators/#listactionexecutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListActionExecutionsInputPaginateTypeDef]
    ) -> PageIterator[ListActionExecutionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/paginator/ListActionExecutions.html#CodePipeline.Paginator.ListActionExecutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators/#listactionexecutionspaginator)
        """

if TYPE_CHECKING:
    _ListActionTypesPaginatorBase = Paginator[ListActionTypesOutputTypeDef]
else:
    _ListActionTypesPaginatorBase = Paginator  # type: ignore[assignment]

class ListActionTypesPaginator(_ListActionTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/paginator/ListActionTypes.html#CodePipeline.Paginator.ListActionTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators/#listactiontypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListActionTypesInputPaginateTypeDef]
    ) -> PageIterator[ListActionTypesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/paginator/ListActionTypes.html#CodePipeline.Paginator.ListActionTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators/#listactiontypespaginator)
        """

if TYPE_CHECKING:
    _ListPipelineExecutionsPaginatorBase = Paginator[ListPipelineExecutionsOutputTypeDef]
else:
    _ListPipelineExecutionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPipelineExecutionsPaginator(_ListPipelineExecutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/paginator/ListPipelineExecutions.html#CodePipeline.Paginator.ListPipelineExecutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators/#listpipelineexecutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPipelineExecutionsInputPaginateTypeDef]
    ) -> PageIterator[ListPipelineExecutionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/paginator/ListPipelineExecutions.html#CodePipeline.Paginator.ListPipelineExecutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators/#listpipelineexecutionspaginator)
        """

if TYPE_CHECKING:
    _ListPipelinesPaginatorBase = Paginator[ListPipelinesOutputTypeDef]
else:
    _ListPipelinesPaginatorBase = Paginator  # type: ignore[assignment]

class ListPipelinesPaginator(_ListPipelinesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/paginator/ListPipelines.html#CodePipeline.Paginator.ListPipelines)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators/#listpipelinespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPipelinesInputPaginateTypeDef]
    ) -> PageIterator[ListPipelinesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/paginator/ListPipelines.html#CodePipeline.Paginator.ListPipelines.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators/#listpipelinespaginator)
        """

if TYPE_CHECKING:
    _ListRuleExecutionsPaginatorBase = Paginator[ListRuleExecutionsOutputTypeDef]
else:
    _ListRuleExecutionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRuleExecutionsPaginator(_ListRuleExecutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/paginator/ListRuleExecutions.html#CodePipeline.Paginator.ListRuleExecutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators/#listruleexecutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRuleExecutionsInputPaginateTypeDef]
    ) -> PageIterator[ListRuleExecutionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/paginator/ListRuleExecutions.html#CodePipeline.Paginator.ListRuleExecutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators/#listruleexecutionspaginator)
        """

if TYPE_CHECKING:
    _ListTagsForResourcePaginatorBase = Paginator[ListTagsForResourceOutputTypeDef]
else:
    _ListTagsForResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsForResourcePaginator(_ListTagsForResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/paginator/ListTagsForResource.html#CodePipeline.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators/#listtagsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsForResourceInputPaginateTypeDef]
    ) -> PageIterator[ListTagsForResourceOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/paginator/ListTagsForResource.html#CodePipeline.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators/#listtagsforresourcepaginator)
        """

if TYPE_CHECKING:
    _ListWebhooksPaginatorBase = Paginator[ListWebhooksOutputTypeDef]
else:
    _ListWebhooksPaginatorBase = Paginator  # type: ignore[assignment]

class ListWebhooksPaginator(_ListWebhooksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/paginator/ListWebhooks.html#CodePipeline.Paginator.ListWebhooks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators/#listwebhookspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWebhooksInputPaginateTypeDef]
    ) -> PageIterator[ListWebhooksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/paginator/ListWebhooks.html#CodePipeline.Paginator.ListWebhooks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators/#listwebhookspaginator)
        """
