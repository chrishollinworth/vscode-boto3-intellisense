# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for discovery service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_discovery import ApplicationDiscoveryServiceClient
    from mypy_boto3_discovery.paginator import (
        DescribeAgentsPaginator,
        DescribeContinuousExportsPaginator,
        DescribeExportConfigurationsPaginator,
        DescribeExportTasksPaginator,
        DescribeTagsPaginator,
        ListConfigurationsPaginator,
    )

    client: ApplicationDiscoveryServiceClient = boto3.client("discovery")

    describe_agents_paginator: DescribeAgentsPaginator = client.get_paginator("describe_agents")
    describe_continuous_exports_paginator: DescribeContinuousExportsPaginator = client.get_paginator("describe_continuous_exports")
    describe_export_configurations_paginator: DescribeExportConfigurationsPaginator = client.get_paginator("describe_export_configurations")
    describe_export_tasks_paginator: DescribeExportTasksPaginator = client.get_paginator("describe_export_tasks")
    describe_tags_paginator: DescribeTagsPaginator = client.get_paginator("describe_tags")
    list_configurations_paginator: ListConfigurationsPaginator = client.get_paginator("list_configurations")
    ```
"""
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_discovery.type_defs import (
    DescribeAgentsResponseTypeDef,
    DescribeContinuousExportsResponseTypeDef,
    DescribeExportConfigurationsResponseTypeDef,
    DescribeExportTasksResponseTypeDef,
    DescribeTagsResponseTypeDef,
    ExportFilterTypeDef,
    FilterTypeDef,
    ListConfigurationsResponseTypeDef,
    OrderByElementTypeDef,
    PaginatorConfigTypeDef,
    TagFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeAgentsPaginator",
    "DescribeContinuousExportsPaginator",
    "DescribeExportConfigurationsPaginator",
    "DescribeExportTasksPaginator",
    "DescribeTagsPaginator",
    "ListConfigurationsPaginator",
)


class DescribeAgentsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeAgents)
    """

    def paginate(
        self,
        agentIds: List[str] = None,
        filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeAgentsResponseTypeDef]:
        """
        [DescribeAgents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeAgents.paginate)
        """


class DescribeContinuousExportsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeContinuousExports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeContinuousExports)
    """

    def paginate(
        self, exportIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeContinuousExportsResponseTypeDef]:
        """
        [DescribeContinuousExports.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeContinuousExports.paginate)
        """


class DescribeExportConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeExportConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportConfigurations)
    """

    def paginate(
        self, exportIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeExportConfigurationsResponseTypeDef]:
        """
        [DescribeExportConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportConfigurations.paginate)
        """


class DescribeExportTasksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeExportTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportTasks)
    """

    def paginate(
        self,
        exportIds: List[str] = None,
        filters: List[ExportFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeExportTasksResponseTypeDef]:
        """
        [DescribeExportTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportTasks.paginate)
        """


class DescribeTagsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeTags)
    """

    def paginate(
        self,
        filters: List[TagFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeTagsResponseTypeDef]:
        """
        [DescribeTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeTags.paginate)
        """


class ListConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.ListConfigurations)
    """

    def paginate(
        self,
        configurationType: Literal["SERVER", "PROCESS", "CONNECTION", "APPLICATION"],
        filters: List[FilterTypeDef] = None,
        orderBy: List[OrderByElementTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListConfigurationsResponseTypeDef]:
        """
        [ListConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.ListConfigurations.paginate)
        """
