"""
Type annotations for mwaa-serverless service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_mwaa_serverless.client import MWAAServerlessClient
    from mypy_boto3_mwaa_serverless.paginator import (
        ListTaskInstancesPaginator,
        ListWorkflowRunsPaginator,
        ListWorkflowVersionsPaginator,
        ListWorkflowsPaginator,
    )

    session = Session()
    client: MWAAServerlessClient = session.client("mwaa-serverless")

    list_task_instances_paginator: ListTaskInstancesPaginator = client.get_paginator("list_task_instances")
    list_workflow_runs_paginator: ListWorkflowRunsPaginator = client.get_paginator("list_workflow_runs")
    list_workflow_versions_paginator: ListWorkflowVersionsPaginator = client.get_paginator("list_workflow_versions")
    list_workflows_paginator: ListWorkflowsPaginator = client.get_paginator("list_workflows")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListTaskInstancesRequestPaginateTypeDef,
    ListTaskInstancesResponseTypeDef,
    ListWorkflowRunsRequestPaginateTypeDef,
    ListWorkflowRunsResponseTypeDef,
    ListWorkflowsRequestPaginateTypeDef,
    ListWorkflowsResponseTypeDef,
    ListWorkflowVersionsRequestPaginateTypeDef,
    ListWorkflowVersionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListTaskInstancesPaginator",
    "ListWorkflowRunsPaginator",
    "ListWorkflowVersionsPaginator",
    "ListWorkflowsPaginator",
)

if TYPE_CHECKING:
    _ListTaskInstancesPaginatorBase = Paginator[ListTaskInstancesResponseTypeDef]
else:
    _ListTaskInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTaskInstancesPaginator(_ListTaskInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/paginator/ListTaskInstances.html#MWAAServerless.Paginator.ListTaskInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/paginators/#listtaskinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTaskInstancesRequestPaginateTypeDef]
    ) -> PageIterator[ListTaskInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/paginator/ListTaskInstances.html#MWAAServerless.Paginator.ListTaskInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/paginators/#listtaskinstancespaginator)
        """

if TYPE_CHECKING:
    _ListWorkflowRunsPaginatorBase = Paginator[ListWorkflowRunsResponseTypeDef]
else:
    _ListWorkflowRunsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkflowRunsPaginator(_ListWorkflowRunsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/paginator/ListWorkflowRuns.html#MWAAServerless.Paginator.ListWorkflowRuns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/paginators/#listworkflowrunspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkflowRunsRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkflowRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/paginator/ListWorkflowRuns.html#MWAAServerless.Paginator.ListWorkflowRuns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/paginators/#listworkflowrunspaginator)
        """

if TYPE_CHECKING:
    _ListWorkflowVersionsPaginatorBase = Paginator[ListWorkflowVersionsResponseTypeDef]
else:
    _ListWorkflowVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkflowVersionsPaginator(_ListWorkflowVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/paginator/ListWorkflowVersions.html#MWAAServerless.Paginator.ListWorkflowVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/paginators/#listworkflowversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkflowVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkflowVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/paginator/ListWorkflowVersions.html#MWAAServerless.Paginator.ListWorkflowVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/paginators/#listworkflowversionspaginator)
        """

if TYPE_CHECKING:
    _ListWorkflowsPaginatorBase = Paginator[ListWorkflowsResponseTypeDef]
else:
    _ListWorkflowsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkflowsPaginator(_ListWorkflowsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/paginator/ListWorkflows.html#MWAAServerless.Paginator.ListWorkflows)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/paginators/#listworkflowspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkflowsRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkflowsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/paginator/ListWorkflows.html#MWAAServerless.Paginator.ListWorkflows.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/paginators/#listworkflowspaginator)
        """
