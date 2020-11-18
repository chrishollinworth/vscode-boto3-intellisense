# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for xray service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_xray import XRayClient
    from mypy_boto3_xray.paginator import (
        BatchGetTracesPaginator,
        GetGroupsPaginator,
        GetSamplingRulesPaginator,
        GetSamplingStatisticSummariesPaginator,
        GetServiceGraphPaginator,
        GetTimeSeriesServiceStatisticsPaginator,
        GetTraceGraphPaginator,
        GetTraceSummariesPaginator,
    )

    client: XRayClient = boto3.client("xray")

    batch_get_traces_paginator: BatchGetTracesPaginator = client.get_paginator("batch_get_traces")
    get_groups_paginator: GetGroupsPaginator = client.get_paginator("get_groups")
    get_sampling_rules_paginator: GetSamplingRulesPaginator = client.get_paginator("get_sampling_rules")
    get_sampling_statistic_summaries_paginator: GetSamplingStatisticSummariesPaginator = client.get_paginator("get_sampling_statistic_summaries")
    get_service_graph_paginator: GetServiceGraphPaginator = client.get_paginator("get_service_graph")
    get_time_series_service_statistics_paginator: GetTimeSeriesServiceStatisticsPaginator = client.get_paginator("get_time_series_service_statistics")
    get_trace_graph_paginator: GetTraceGraphPaginator = client.get_paginator("get_trace_graph")
    get_trace_summaries_paginator: GetTraceSummariesPaginator = client.get_paginator("get_trace_summaries")
    ```
"""
import sys
from datetime import datetime
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_xray.type_defs import (
    BatchGetTracesResultTypeDef,
    GetGroupsResultTypeDef,
    GetSamplingRulesResultTypeDef,
    GetSamplingStatisticSummariesResultTypeDef,
    GetServiceGraphResultTypeDef,
    GetTimeSeriesServiceStatisticsResultTypeDef,
    GetTraceGraphResultTypeDef,
    GetTraceSummariesResultTypeDef,
    PaginatorConfigTypeDef,
    SamplingStrategyTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BatchGetTracesPaginator",
    "GetGroupsPaginator",
    "GetSamplingRulesPaginator",
    "GetSamplingStatisticSummariesPaginator",
    "GetServiceGraphPaginator",
    "GetTimeSeriesServiceStatisticsPaginator",
    "GetTraceGraphPaginator",
    "GetTraceSummariesPaginator",
)


class BatchGetTracesPaginator(Boto3Paginator):
    """
    [Paginator.BatchGetTraces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.BatchGetTraces)
    """

    def paginate(
        self, TraceIds: List[str], PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[BatchGetTracesResultTypeDef]:
        """
        [BatchGetTraces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.BatchGetTraces.paginate)
        """


class GetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.GetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetGroups)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetGroupsResultTypeDef]:
        """
        [GetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetGroups.paginate)
        """


class GetSamplingRulesPaginator(Boto3Paginator):
    """
    [Paginator.GetSamplingRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetSamplingRules)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetSamplingRulesResultTypeDef]:
        """
        [GetSamplingRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetSamplingRules.paginate)
        """


class GetSamplingStatisticSummariesPaginator(Boto3Paginator):
    """
    [Paginator.GetSamplingStatisticSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetSamplingStatisticSummaries)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetSamplingStatisticSummariesResultTypeDef]:
        """
        [GetSamplingStatisticSummaries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetSamplingStatisticSummaries.paginate)
        """


class GetServiceGraphPaginator(Boto3Paginator):
    """
    [Paginator.GetServiceGraph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetServiceGraph)
    """

    def paginate(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: str = None,
        GroupARN: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetServiceGraphResultTypeDef]:
        """
        [GetServiceGraph.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetServiceGraph.paginate)
        """


class GetTimeSeriesServiceStatisticsPaginator(Boto3Paginator):
    """
    [Paginator.GetTimeSeriesServiceStatistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetTimeSeriesServiceStatistics)
    """

    def paginate(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: str = None,
        GroupARN: str = None,
        EntitySelectorExpression: str = None,
        Period: int = None,
        ForecastStatistics: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetTimeSeriesServiceStatisticsResultTypeDef]:
        """
        [GetTimeSeriesServiceStatistics.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetTimeSeriesServiceStatistics.paginate)
        """


class GetTraceGraphPaginator(Boto3Paginator):
    """
    [Paginator.GetTraceGraph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetTraceGraph)
    """

    def paginate(
        self, TraceIds: List[str], PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTraceGraphResultTypeDef]:
        """
        [GetTraceGraph.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetTraceGraph.paginate)
        """


class GetTraceSummariesPaginator(Boto3Paginator):
    """
    [Paginator.GetTraceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetTraceSummaries)
    """

    def paginate(
        self,
        StartTime: datetime,
        EndTime: datetime,
        TimeRangeType: Literal["TraceId", "Event"] = None,
        Sampling: bool = None,
        SamplingStrategy: SamplingStrategyTypeDef = None,
        FilterExpression: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetTraceSummariesResultTypeDef]:
        """
        [GetTraceSummaries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetTraceSummaries.paginate)
        """
