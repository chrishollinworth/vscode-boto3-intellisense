"""
Type annotations for nova-act service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_nova_act.client import NovaActServiceClient
    from mypy_boto3_nova_act.paginator import (
        ListActsPaginator,
        ListSessionsPaginator,
        ListWorkflowDefinitionsPaginator,
        ListWorkflowRunsPaginator,
    )

    session = Session()
    client: NovaActServiceClient = session.client("nova-act")

    list_acts_paginator: ListActsPaginator = client.get_paginator("list_acts")
    list_sessions_paginator: ListSessionsPaginator = client.get_paginator("list_sessions")
    list_workflow_definitions_paginator: ListWorkflowDefinitionsPaginator = client.get_paginator("list_workflow_definitions")
    list_workflow_runs_paginator: ListWorkflowRunsPaginator = client.get_paginator("list_workflow_runs")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListActsRequestPaginateTypeDef,
    ListActsResponseTypeDef,
    ListSessionsRequestPaginateTypeDef,
    ListSessionsResponseTypeDef,
    ListWorkflowDefinitionsRequestPaginateTypeDef,
    ListWorkflowDefinitionsResponseTypeDef,
    ListWorkflowRunsRequestPaginateTypeDef,
    ListWorkflowRunsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListActsPaginator",
    "ListSessionsPaginator",
    "ListWorkflowDefinitionsPaginator",
    "ListWorkflowRunsPaginator",
)

if TYPE_CHECKING:
    _ListActsPaginatorBase = Paginator[ListActsResponseTypeDef]
else:
    _ListActsPaginatorBase = Paginator  # type: ignore[assignment]

class ListActsPaginator(_ListActsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/paginator/ListActs.html#NovaActService.Paginator.ListActs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/paginators/#listactspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListActsRequestPaginateTypeDef]
    ) -> PageIterator[ListActsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/paginator/ListActs.html#NovaActService.Paginator.ListActs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/paginators/#listactspaginator)
        """

if TYPE_CHECKING:
    _ListSessionsPaginatorBase = Paginator[ListSessionsResponseTypeDef]
else:
    _ListSessionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSessionsPaginator(_ListSessionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/paginator/ListSessions.html#NovaActService.Paginator.ListSessions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/paginators/#listsessionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSessionsRequestPaginateTypeDef]
    ) -> PageIterator[ListSessionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/paginator/ListSessions.html#NovaActService.Paginator.ListSessions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/paginators/#listsessionspaginator)
        """

if TYPE_CHECKING:
    _ListWorkflowDefinitionsPaginatorBase = Paginator[ListWorkflowDefinitionsResponseTypeDef]
else:
    _ListWorkflowDefinitionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkflowDefinitionsPaginator(_ListWorkflowDefinitionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/paginator/ListWorkflowDefinitions.html#NovaActService.Paginator.ListWorkflowDefinitions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/paginators/#listworkflowdefinitionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkflowDefinitionsRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkflowDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/paginator/ListWorkflowDefinitions.html#NovaActService.Paginator.ListWorkflowDefinitions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/paginators/#listworkflowdefinitionspaginator)
        """

if TYPE_CHECKING:
    _ListWorkflowRunsPaginatorBase = Paginator[ListWorkflowRunsResponseTypeDef]
else:
    _ListWorkflowRunsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkflowRunsPaginator(_ListWorkflowRunsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/paginator/ListWorkflowRuns.html#NovaActService.Paginator.ListWorkflowRuns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/paginators/#listworkflowrunspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkflowRunsRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkflowRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/paginator/ListWorkflowRuns.html#NovaActService.Paginator.ListWorkflowRuns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/paginators/#listworkflowrunspaginator)
        """
