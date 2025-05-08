"""
Type annotations for discovery service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_discovery.client import ApplicationDiscoveryServiceClient
    from mypy_boto3_discovery.paginator import (
        DescribeAgentsPaginator,
        DescribeContinuousExportsPaginator,
        DescribeExportConfigurationsPaginator,
        DescribeExportTasksPaginator,
        DescribeImportTasksPaginator,
        DescribeTagsPaginator,
        ListConfigurationsPaginator,
    )

    session = Session()
    client: ApplicationDiscoveryServiceClient = session.client("discovery")

    describe_agents_paginator: DescribeAgentsPaginator = client.get_paginator("describe_agents")
    describe_continuous_exports_paginator: DescribeContinuousExportsPaginator = client.get_paginator("describe_continuous_exports")
    describe_export_configurations_paginator: DescribeExportConfigurationsPaginator = client.get_paginator("describe_export_configurations")
    describe_export_tasks_paginator: DescribeExportTasksPaginator = client.get_paginator("describe_export_tasks")
    describe_import_tasks_paginator: DescribeImportTasksPaginator = client.get_paginator("describe_import_tasks")
    describe_tags_paginator: DescribeTagsPaginator = client.get_paginator("describe_tags")
    list_configurations_paginator: ListConfigurationsPaginator = client.get_paginator("list_configurations")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeAgentsRequestPaginateTypeDef,
    DescribeAgentsResponseTypeDef,
    DescribeContinuousExportsRequestPaginateTypeDef,
    DescribeContinuousExportsResponseTypeDef,
    DescribeExportConfigurationsRequestPaginateTypeDef,
    DescribeExportConfigurationsResponseTypeDef,
    DescribeExportTasksRequestPaginateTypeDef,
    DescribeExportTasksResponseTypeDef,
    DescribeImportTasksRequestPaginateTypeDef,
    DescribeImportTasksResponseTypeDef,
    DescribeTagsRequestPaginateTypeDef,
    DescribeTagsResponseTypeDef,
    ListConfigurationsRequestPaginateTypeDef,
    ListConfigurationsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeAgentsPaginator",
    "DescribeContinuousExportsPaginator",
    "DescribeExportConfigurationsPaginator",
    "DescribeExportTasksPaginator",
    "DescribeImportTasksPaginator",
    "DescribeTagsPaginator",
    "ListConfigurationsPaginator",
)

if TYPE_CHECKING:
    _DescribeAgentsPaginatorBase = Paginator[DescribeAgentsResponseTypeDef]
else:
    _DescribeAgentsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAgentsPaginator(_DescribeAgentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery/paginator/DescribeAgents.html#ApplicationDiscoveryService.Paginator.DescribeAgents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators/#describeagentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAgentsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeAgentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery/paginator/DescribeAgents.html#ApplicationDiscoveryService.Paginator.DescribeAgents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators/#describeagentspaginator)
        """

if TYPE_CHECKING:
    _DescribeContinuousExportsPaginatorBase = Paginator[DescribeContinuousExportsResponseTypeDef]
else:
    _DescribeContinuousExportsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeContinuousExportsPaginator(_DescribeContinuousExportsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery/paginator/DescribeContinuousExports.html#ApplicationDiscoveryService.Paginator.DescribeContinuousExports)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators/#describecontinuousexportspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeContinuousExportsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeContinuousExportsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery/paginator/DescribeContinuousExports.html#ApplicationDiscoveryService.Paginator.DescribeContinuousExports.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators/#describecontinuousexportspaginator)
        """

if TYPE_CHECKING:
    _DescribeExportConfigurationsPaginatorBase = Paginator[
        DescribeExportConfigurationsResponseTypeDef
    ]
else:
    _DescribeExportConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeExportConfigurationsPaginator(_DescribeExportConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery/paginator/DescribeExportConfigurations.html#ApplicationDiscoveryService.Paginator.DescribeExportConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators/#describeexportconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeExportConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeExportConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery/paginator/DescribeExportConfigurations.html#ApplicationDiscoveryService.Paginator.DescribeExportConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators/#describeexportconfigurationspaginator)
        """

if TYPE_CHECKING:
    _DescribeExportTasksPaginatorBase = Paginator[DescribeExportTasksResponseTypeDef]
else:
    _DescribeExportTasksPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeExportTasksPaginator(_DescribeExportTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery/paginator/DescribeExportTasks.html#ApplicationDiscoveryService.Paginator.DescribeExportTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators/#describeexporttaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeExportTasksRequestPaginateTypeDef]
    ) -> PageIterator[DescribeExportTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery/paginator/DescribeExportTasks.html#ApplicationDiscoveryService.Paginator.DescribeExportTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators/#describeexporttaskspaginator)
        """

if TYPE_CHECKING:
    _DescribeImportTasksPaginatorBase = Paginator[DescribeImportTasksResponseTypeDef]
else:
    _DescribeImportTasksPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeImportTasksPaginator(_DescribeImportTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery/paginator/DescribeImportTasks.html#ApplicationDiscoveryService.Paginator.DescribeImportTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators/#describeimporttaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeImportTasksRequestPaginateTypeDef]
    ) -> PageIterator[DescribeImportTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery/paginator/DescribeImportTasks.html#ApplicationDiscoveryService.Paginator.DescribeImportTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators/#describeimporttaskspaginator)
        """

if TYPE_CHECKING:
    _DescribeTagsPaginatorBase = Paginator[DescribeTagsResponseTypeDef]
else:
    _DescribeTagsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTagsPaginator(_DescribeTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery/paginator/DescribeTags.html#ApplicationDiscoveryService.Paginator.DescribeTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators/#describetagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTagsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery/paginator/DescribeTags.html#ApplicationDiscoveryService.Paginator.DescribeTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators/#describetagspaginator)
        """

if TYPE_CHECKING:
    _ListConfigurationsPaginatorBase = Paginator[ListConfigurationsResponseTypeDef]
else:
    _ListConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConfigurationsPaginator(_ListConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery/paginator/ListConfigurations.html#ApplicationDiscoveryService.Paginator.ListConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators/#listconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery/paginator/ListConfigurations.html#ApplicationDiscoveryService.Paginator.ListConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_discovery/paginators/#listconfigurationspaginator)
        """
