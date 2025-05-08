"""
Type annotations for dax service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_dax.client import DAXClient
    from mypy_boto3_dax.paginator import (
        DescribeClustersPaginator,
        DescribeDefaultParametersPaginator,
        DescribeEventsPaginator,
        DescribeParameterGroupsPaginator,
        DescribeParametersPaginator,
        DescribeSubnetGroupsPaginator,
        ListTagsPaginator,
    )

    session = Session()
    client: DAXClient = session.client("dax")

    describe_clusters_paginator: DescribeClustersPaginator = client.get_paginator("describe_clusters")
    describe_default_parameters_paginator: DescribeDefaultParametersPaginator = client.get_paginator("describe_default_parameters")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_parameter_groups_paginator: DescribeParameterGroupsPaginator = client.get_paginator("describe_parameter_groups")
    describe_parameters_paginator: DescribeParametersPaginator = client.get_paginator("describe_parameters")
    describe_subnet_groups_paginator: DescribeSubnetGroupsPaginator = client.get_paginator("describe_subnet_groups")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeClustersRequestPaginateTypeDef,
    DescribeClustersResponseTypeDef,
    DescribeDefaultParametersRequestPaginateTypeDef,
    DescribeDefaultParametersResponseTypeDef,
    DescribeEventsRequestPaginateTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeParameterGroupsRequestPaginateTypeDef,
    DescribeParameterGroupsResponseTypeDef,
    DescribeParametersRequestPaginateTypeDef,
    DescribeParametersResponseTypeDef,
    DescribeSubnetGroupsRequestPaginateTypeDef,
    DescribeSubnetGroupsResponseTypeDef,
    ListTagsRequestPaginateTypeDef,
    ListTagsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeClustersPaginator",
    "DescribeDefaultParametersPaginator",
    "DescribeEventsPaginator",
    "DescribeParameterGroupsPaginator",
    "DescribeParametersPaginator",
    "DescribeSubnetGroupsPaginator",
    "ListTagsPaginator",
)

if TYPE_CHECKING:
    _DescribeClustersPaginatorBase = Paginator[DescribeClustersResponseTypeDef]
else:
    _DescribeClustersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClustersPaginator(_DescribeClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/paginator/DescribeClusters.html#DAX.Paginator.DescribeClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators/#describeclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClustersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeClustersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/paginator/DescribeClusters.html#DAX.Paginator.DescribeClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators/#describeclusterspaginator)
        """

if TYPE_CHECKING:
    _DescribeDefaultParametersPaginatorBase = Paginator[DescribeDefaultParametersResponseTypeDef]
else:
    _DescribeDefaultParametersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDefaultParametersPaginator(_DescribeDefaultParametersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/paginator/DescribeDefaultParameters.html#DAX.Paginator.DescribeDefaultParameters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators/#describedefaultparameterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDefaultParametersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeDefaultParametersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/paginator/DescribeDefaultParameters.html#DAX.Paginator.DescribeDefaultParameters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators/#describedefaultparameterspaginator)
        """

if TYPE_CHECKING:
    _DescribeEventsPaginatorBase = Paginator[DescribeEventsResponseTypeDef]
else:
    _DescribeEventsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEventsPaginator(_DescribeEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/paginator/DescribeEvents.html#DAX.Paginator.DescribeEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators/#describeeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEventsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/paginator/DescribeEvents.html#DAX.Paginator.DescribeEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators/#describeeventspaginator)
        """

if TYPE_CHECKING:
    _DescribeParameterGroupsPaginatorBase = Paginator[DescribeParameterGroupsResponseTypeDef]
else:
    _DescribeParameterGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeParameterGroupsPaginator(_DescribeParameterGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/paginator/DescribeParameterGroups.html#DAX.Paginator.DescribeParameterGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators/#describeparametergroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeParameterGroupsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeParameterGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/paginator/DescribeParameterGroups.html#DAX.Paginator.DescribeParameterGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators/#describeparametergroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeParametersPaginatorBase = Paginator[DescribeParametersResponseTypeDef]
else:
    _DescribeParametersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeParametersPaginator(_DescribeParametersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/paginator/DescribeParameters.html#DAX.Paginator.DescribeParameters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators/#describeparameterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeParametersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeParametersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/paginator/DescribeParameters.html#DAX.Paginator.DescribeParameters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators/#describeparameterspaginator)
        """

if TYPE_CHECKING:
    _DescribeSubnetGroupsPaginatorBase = Paginator[DescribeSubnetGroupsResponseTypeDef]
else:
    _DescribeSubnetGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSubnetGroupsPaginator(_DescribeSubnetGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/paginator/DescribeSubnetGroups.html#DAX.Paginator.DescribeSubnetGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators/#describesubnetgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSubnetGroupsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSubnetGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/paginator/DescribeSubnetGroups.html#DAX.Paginator.DescribeSubnetGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators/#describesubnetgroupspaginator)
        """

if TYPE_CHECKING:
    _ListTagsPaginatorBase = Paginator[ListTagsResponseTypeDef]
else:
    _ListTagsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsPaginator(_ListTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/paginator/ListTags.html#DAX.Paginator.ListTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators/#listtagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsRequestPaginateTypeDef]
    ) -> PageIterator[ListTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax/paginator/ListTags.html#DAX.Paginator.ListTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators/#listtagspaginator)
        """
