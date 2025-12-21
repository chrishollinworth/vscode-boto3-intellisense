"""
Type annotations for workspaces-instances service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_workspaces_instances.client import WorkspacesInstancesClient
    from mypy_boto3_workspaces_instances.paginator import (
        ListInstanceTypesPaginator,
        ListRegionsPaginator,
        ListWorkspaceInstancesPaginator,
    )

    session = Session()
    client: WorkspacesInstancesClient = session.client("workspaces-instances")

    list_instance_types_paginator: ListInstanceTypesPaginator = client.get_paginator("list_instance_types")
    list_regions_paginator: ListRegionsPaginator = client.get_paginator("list_regions")
    list_workspace_instances_paginator: ListWorkspaceInstancesPaginator = client.get_paginator("list_workspace_instances")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListInstanceTypesRequestPaginateTypeDef,
    ListInstanceTypesResponseTypeDef,
    ListRegionsRequestPaginateTypeDef,
    ListRegionsResponseTypeDef,
    ListWorkspaceInstancesRequestPaginateTypeDef,
    ListWorkspaceInstancesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListInstanceTypesPaginator", "ListRegionsPaginator", "ListWorkspaceInstancesPaginator")

if TYPE_CHECKING:
    _ListInstanceTypesPaginatorBase = Paginator[ListInstanceTypesResponseTypeDef]
else:
    _ListInstanceTypesPaginatorBase = Paginator  # type: ignore[assignment]

class ListInstanceTypesPaginator(_ListInstanceTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/paginator/ListInstanceTypes.html#WorkspacesInstances.Paginator.ListInstanceTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/paginators/#listinstancetypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInstanceTypesRequestPaginateTypeDef]
    ) -> PageIterator[ListInstanceTypesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/paginator/ListInstanceTypes.html#WorkspacesInstances.Paginator.ListInstanceTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/paginators/#listinstancetypespaginator)
        """

if TYPE_CHECKING:
    _ListRegionsPaginatorBase = Paginator[ListRegionsResponseTypeDef]
else:
    _ListRegionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRegionsPaginator(_ListRegionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/paginator/ListRegions.html#WorkspacesInstances.Paginator.ListRegions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/paginators/#listregionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRegionsRequestPaginateTypeDef]
    ) -> PageIterator[ListRegionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/paginator/ListRegions.html#WorkspacesInstances.Paginator.ListRegions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/paginators/#listregionspaginator)
        """

if TYPE_CHECKING:
    _ListWorkspaceInstancesPaginatorBase = Paginator[ListWorkspaceInstancesResponseTypeDef]
else:
    _ListWorkspaceInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkspaceInstancesPaginator(_ListWorkspaceInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/paginator/ListWorkspaceInstances.html#WorkspacesInstances.Paginator.ListWorkspaceInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/paginators/#listworkspaceinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkspaceInstancesRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkspaceInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-instances/paginator/ListWorkspaceInstances.html#WorkspacesInstances.Paginator.ListWorkspaceInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/paginators/#listworkspaceinstancespaginator)
        """
