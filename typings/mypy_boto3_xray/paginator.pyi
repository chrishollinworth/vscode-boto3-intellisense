"""
Type annotations for xray service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_xray.client import XRayClient
    from mypy_boto3_xray.paginator import (
        BatchGetTracesPaginator,
        GetGroupsPaginator,
        GetSamplingRulesPaginator,
        GetSamplingStatisticSummariesPaginator,
        GetServiceGraphPaginator,
        GetTimeSeriesServiceStatisticsPaginator,
        GetTraceGraphPaginator,
        GetTraceSummariesPaginator,
        ListResourcePoliciesPaginator,
        ListTagsForResourcePaginator,
    )

    session = Session()
    client: XRayClient = session.client("xray")

    batch_get_traces_paginator: BatchGetTracesPaginator = client.get_paginator("batch_get_traces")
    get_groups_paginator: GetGroupsPaginator = client.get_paginator("get_groups")
    get_sampling_rules_paginator: GetSamplingRulesPaginator = client.get_paginator("get_sampling_rules")
    get_sampling_statistic_summaries_paginator: GetSamplingStatisticSummariesPaginator = client.get_paginator("get_sampling_statistic_summaries")
    get_service_graph_paginator: GetServiceGraphPaginator = client.get_paginator("get_service_graph")
    get_time_series_service_statistics_paginator: GetTimeSeriesServiceStatisticsPaginator = client.get_paginator("get_time_series_service_statistics")
    get_trace_graph_paginator: GetTraceGraphPaginator = client.get_paginator("get_trace_graph")
    get_trace_summaries_paginator: GetTraceSummariesPaginator = client.get_paginator("get_trace_summaries")
    list_resource_policies_paginator: ListResourcePoliciesPaginator = client.get_paginator("list_resource_policies")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    BatchGetTracesRequestPaginateTypeDef,
    BatchGetTracesResultTypeDef,
    GetGroupsRequestPaginateTypeDef,
    GetGroupsResultTypeDef,
    GetSamplingRulesRequestPaginateTypeDef,
    GetSamplingRulesResultTypeDef,
    GetSamplingStatisticSummariesRequestPaginateTypeDef,
    GetSamplingStatisticSummariesResultTypeDef,
    GetServiceGraphRequestPaginateTypeDef,
    GetServiceGraphResultTypeDef,
    GetTimeSeriesServiceStatisticsRequestPaginateTypeDef,
    GetTimeSeriesServiceStatisticsResultTypeDef,
    GetTraceGraphRequestPaginateTypeDef,
    GetTraceGraphResultTypeDef,
    GetTraceSummariesRequestPaginateTypeDef,
    GetTraceSummariesResultTypeDef,
    ListResourcePoliciesRequestPaginateTypeDef,
    ListResourcePoliciesResultTypeDef,
    ListTagsForResourceRequestPaginateTypeDef,
    ListTagsForResourceResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "BatchGetTracesPaginator",
    "GetGroupsPaginator",
    "GetSamplingRulesPaginator",
    "GetSamplingStatisticSummariesPaginator",
    "GetServiceGraphPaginator",
    "GetTimeSeriesServiceStatisticsPaginator",
    "GetTraceGraphPaginator",
    "GetTraceSummariesPaginator",
    "ListResourcePoliciesPaginator",
    "ListTagsForResourcePaginator",
)

if TYPE_CHECKING:
    _BatchGetTracesPaginatorBase = Paginator[BatchGetTracesResultTypeDef]
else:
    _BatchGetTracesPaginatorBase = Paginator  # type: ignore[assignment]

class BatchGetTracesPaginator(_BatchGetTracesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/BatchGetTraces.html#XRay.Paginator.BatchGetTraces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#batchgettracespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[BatchGetTracesRequestPaginateTypeDef]
    ) -> PageIterator[BatchGetTracesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/BatchGetTraces.html#XRay.Paginator.BatchGetTraces.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#batchgettracespaginator)
        """

if TYPE_CHECKING:
    _GetGroupsPaginatorBase = Paginator[GetGroupsResultTypeDef]
else:
    _GetGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class GetGroupsPaginator(_GetGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/GetGroups.html#XRay.Paginator.GetGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#getgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetGroupsRequestPaginateTypeDef]
    ) -> PageIterator[GetGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/GetGroups.html#XRay.Paginator.GetGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#getgroupspaginator)
        """

if TYPE_CHECKING:
    _GetSamplingRulesPaginatorBase = Paginator[GetSamplingRulesResultTypeDef]
else:
    _GetSamplingRulesPaginatorBase = Paginator  # type: ignore[assignment]

class GetSamplingRulesPaginator(_GetSamplingRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/GetSamplingRules.html#XRay.Paginator.GetSamplingRules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#getsamplingrulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetSamplingRulesRequestPaginateTypeDef]
    ) -> PageIterator[GetSamplingRulesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/GetSamplingRules.html#XRay.Paginator.GetSamplingRules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#getsamplingrulespaginator)
        """

if TYPE_CHECKING:
    _GetSamplingStatisticSummariesPaginatorBase = Paginator[
        GetSamplingStatisticSummariesResultTypeDef
    ]
else:
    _GetSamplingStatisticSummariesPaginatorBase = Paginator  # type: ignore[assignment]

class GetSamplingStatisticSummariesPaginator(_GetSamplingStatisticSummariesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/GetSamplingStatisticSummaries.html#XRay.Paginator.GetSamplingStatisticSummaries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#getsamplingstatisticsummariespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetSamplingStatisticSummariesRequestPaginateTypeDef]
    ) -> PageIterator[GetSamplingStatisticSummariesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/GetSamplingStatisticSummaries.html#XRay.Paginator.GetSamplingStatisticSummaries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#getsamplingstatisticsummariespaginator)
        """

if TYPE_CHECKING:
    _GetServiceGraphPaginatorBase = Paginator[GetServiceGraphResultTypeDef]
else:
    _GetServiceGraphPaginatorBase = Paginator  # type: ignore[assignment]

class GetServiceGraphPaginator(_GetServiceGraphPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/GetServiceGraph.html#XRay.Paginator.GetServiceGraph)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#getservicegraphpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetServiceGraphRequestPaginateTypeDef]
    ) -> PageIterator[GetServiceGraphResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/GetServiceGraph.html#XRay.Paginator.GetServiceGraph.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#getservicegraphpaginator)
        """

if TYPE_CHECKING:
    _GetTimeSeriesServiceStatisticsPaginatorBase = Paginator[
        GetTimeSeriesServiceStatisticsResultTypeDef
    ]
else:
    _GetTimeSeriesServiceStatisticsPaginatorBase = Paginator  # type: ignore[assignment]

class GetTimeSeriesServiceStatisticsPaginator(_GetTimeSeriesServiceStatisticsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/GetTimeSeriesServiceStatistics.html#XRay.Paginator.GetTimeSeriesServiceStatistics)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#gettimeseriesservicestatisticspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetTimeSeriesServiceStatisticsRequestPaginateTypeDef]
    ) -> PageIterator[GetTimeSeriesServiceStatisticsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/GetTimeSeriesServiceStatistics.html#XRay.Paginator.GetTimeSeriesServiceStatistics.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#gettimeseriesservicestatisticspaginator)
        """

if TYPE_CHECKING:
    _GetTraceGraphPaginatorBase = Paginator[GetTraceGraphResultTypeDef]
else:
    _GetTraceGraphPaginatorBase = Paginator  # type: ignore[assignment]

class GetTraceGraphPaginator(_GetTraceGraphPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/GetTraceGraph.html#XRay.Paginator.GetTraceGraph)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#gettracegraphpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetTraceGraphRequestPaginateTypeDef]
    ) -> PageIterator[GetTraceGraphResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/GetTraceGraph.html#XRay.Paginator.GetTraceGraph.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#gettracegraphpaginator)
        """

if TYPE_CHECKING:
    _GetTraceSummariesPaginatorBase = Paginator[GetTraceSummariesResultTypeDef]
else:
    _GetTraceSummariesPaginatorBase = Paginator  # type: ignore[assignment]

class GetTraceSummariesPaginator(_GetTraceSummariesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/GetTraceSummaries.html#XRay.Paginator.GetTraceSummaries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#gettracesummariespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetTraceSummariesRequestPaginateTypeDef]
    ) -> PageIterator[GetTraceSummariesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/GetTraceSummaries.html#XRay.Paginator.GetTraceSummaries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#gettracesummariespaginator)
        """

if TYPE_CHECKING:
    _ListResourcePoliciesPaginatorBase = Paginator[ListResourcePoliciesResultTypeDef]
else:
    _ListResourcePoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourcePoliciesPaginator(_ListResourcePoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/ListResourcePolicies.html#XRay.Paginator.ListResourcePolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#listresourcepoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourcePoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListResourcePoliciesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/ListResourcePolicies.html#XRay.Paginator.ListResourcePolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#listresourcepoliciespaginator)
        """

if TYPE_CHECKING:
    _ListTagsForResourcePaginatorBase = Paginator[ListTagsForResourceResponseTypeDef]
else:
    _ListTagsForResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsForResourcePaginator(_ListTagsForResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/ListTagsForResource.html#XRay.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#listtagsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsForResourceRequestPaginateTypeDef]
    ) -> PageIterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray/paginator/ListTagsForResource.html#XRay.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators/#listtagsforresourcepaginator)
        """
