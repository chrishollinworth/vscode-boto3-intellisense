# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for xray service client

Usage::

    ```python
    import boto3
    from mypy_boto3_xray import XRayClient

    client: XRayClient = boto3.client("xray")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

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
from mypy_boto3_xray.type_defs import (
    BatchGetTracesResultTypeDef,
    CreateGroupResultTypeDef,
    CreateSamplingRuleResultTypeDef,
    DeleteSamplingRuleResultTypeDef,
    GetEncryptionConfigResultTypeDef,
    GetGroupResultTypeDef,
    GetGroupsResultTypeDef,
    GetInsightEventsResultTypeDef,
    GetInsightImpactGraphResultTypeDef,
    GetInsightResultTypeDef,
    GetInsightSummariesResultTypeDef,
    GetSamplingRulesResultTypeDef,
    GetSamplingStatisticSummariesResultTypeDef,
    GetSamplingTargetsResultTypeDef,
    GetServiceGraphResultTypeDef,
    GetTimeSeriesServiceStatisticsResultTypeDef,
    GetTraceGraphResultTypeDef,
    GetTraceSummariesResultTypeDef,
    InsightsConfigurationTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutEncryptionConfigResultTypeDef,
    PutTraceSegmentsResultTypeDef,
    SamplingRuleTypeDef,
    SamplingRuleUpdateTypeDef,
    SamplingStatisticsDocumentTypeDef,
    SamplingStrategyTypeDef,
    TagTypeDef,
    TelemetryRecordTypeDef,
    UpdateGroupResultTypeDef,
    UpdateSamplingRuleResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("XRayClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    RuleLimitExceededException: Type[BotocoreClientError]
    ThrottledException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]


class XRayClient:
    """
    [XRay.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_get_traces(
        self, TraceIds: List[str], NextToken: str = None
    ) -> BatchGetTracesResultTypeDef:
        """
        [Client.batch_get_traces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.batch_get_traces)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.can_paginate)
        """

    def create_group(
        self,
        GroupName: str,
        FilterExpression: str = None,
        InsightsConfiguration: "InsightsConfigurationTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateGroupResultTypeDef:
        """
        [Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.create_group)
        """

    def create_sampling_rule(
        self, SamplingRule: "SamplingRuleTypeDef", Tags: List["TagTypeDef"] = None
    ) -> CreateSamplingRuleResultTypeDef:
        """
        [Client.create_sampling_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.create_sampling_rule)
        """

    def delete_group(self, GroupName: str = None, GroupARN: str = None) -> Dict[str, Any]:
        """
        [Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.delete_group)
        """

    def delete_sampling_rule(
        self, RuleName: str = None, RuleARN: str = None
    ) -> DeleteSamplingRuleResultTypeDef:
        """
        [Client.delete_sampling_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.delete_sampling_rule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.generate_presigned_url)
        """

    def get_encryption_config(self) -> GetEncryptionConfigResultTypeDef:
        """
        [Client.get_encryption_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.get_encryption_config)
        """

    def get_group(self, GroupName: str = None, GroupARN: str = None) -> GetGroupResultTypeDef:
        """
        [Client.get_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.get_group)
        """

    def get_groups(self, NextToken: str = None) -> GetGroupsResultTypeDef:
        """
        [Client.get_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.get_groups)
        """

    def get_insight(self, InsightId: str) -> GetInsightResultTypeDef:
        """
        [Client.get_insight documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.get_insight)
        """

    def get_insight_events(
        self, InsightId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetInsightEventsResultTypeDef:
        """
        [Client.get_insight_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.get_insight_events)
        """

    def get_insight_impact_graph(
        self, InsightId: str, StartTime: datetime, EndTime: datetime, NextToken: str = None
    ) -> GetInsightImpactGraphResultTypeDef:
        """
        [Client.get_insight_impact_graph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.get_insight_impact_graph)
        """

    def get_insight_summaries(
        self,
        StartTime: datetime,
        EndTime: datetime,
        States: List[Literal["ACTIVE", "CLOSED"]] = None,
        GroupARN: str = None,
        GroupName: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetInsightSummariesResultTypeDef:
        """
        [Client.get_insight_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.get_insight_summaries)
        """

    def get_sampling_rules(self, NextToken: str = None) -> GetSamplingRulesResultTypeDef:
        """
        [Client.get_sampling_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.get_sampling_rules)
        """

    def get_sampling_statistic_summaries(
        self, NextToken: str = None
    ) -> GetSamplingStatisticSummariesResultTypeDef:
        """
        [Client.get_sampling_statistic_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.get_sampling_statistic_summaries)
        """

    def get_sampling_targets(
        self, SamplingStatisticsDocuments: List[SamplingStatisticsDocumentTypeDef]
    ) -> GetSamplingTargetsResultTypeDef:
        """
        [Client.get_sampling_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.get_sampling_targets)
        """

    def get_service_graph(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: str = None,
        GroupARN: str = None,
        NextToken: str = None,
    ) -> GetServiceGraphResultTypeDef:
        """
        [Client.get_service_graph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.get_service_graph)
        """

    def get_time_series_service_statistics(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: str = None,
        GroupARN: str = None,
        EntitySelectorExpression: str = None,
        Period: int = None,
        ForecastStatistics: bool = None,
        NextToken: str = None,
    ) -> GetTimeSeriesServiceStatisticsResultTypeDef:
        """
        [Client.get_time_series_service_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.get_time_series_service_statistics)
        """

    def get_trace_graph(
        self, TraceIds: List[str], NextToken: str = None
    ) -> GetTraceGraphResultTypeDef:
        """
        [Client.get_trace_graph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.get_trace_graph)
        """

    def get_trace_summaries(
        self,
        StartTime: datetime,
        EndTime: datetime,
        TimeRangeType: Literal["TraceId", "Event"] = None,
        Sampling: bool = None,
        SamplingStrategy: SamplingStrategyTypeDef = None,
        FilterExpression: str = None,
        NextToken: str = None,
    ) -> GetTraceSummariesResultTypeDef:
        """
        [Client.get_trace_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.get_trace_summaries)
        """

    def list_tags_for_resource(
        self, ResourceARN: str, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.list_tags_for_resource)
        """

    def put_encryption_config(
        self, Type: Literal["NONE", "KMS"], KeyId: str = None
    ) -> PutEncryptionConfigResultTypeDef:
        """
        [Client.put_encryption_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.put_encryption_config)
        """

    def put_telemetry_records(
        self,
        TelemetryRecords: List[TelemetryRecordTypeDef],
        EC2InstanceId: str = None,
        Hostname: str = None,
        ResourceARN: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_telemetry_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.put_telemetry_records)
        """

    def put_trace_segments(self, TraceSegmentDocuments: List[str]) -> PutTraceSegmentsResultTypeDef:
        """
        [Client.put_trace_segments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.put_trace_segments)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.untag_resource)
        """

    def update_group(
        self,
        GroupName: str = None,
        GroupARN: str = None,
        FilterExpression: str = None,
        InsightsConfiguration: "InsightsConfigurationTypeDef" = None,
    ) -> UpdateGroupResultTypeDef:
        """
        [Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.update_group)
        """

    def update_sampling_rule(
        self, SamplingRuleUpdate: SamplingRuleUpdateTypeDef
    ) -> UpdateSamplingRuleResultTypeDef:
        """
        [Client.update_sampling_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Client.update_sampling_rule)
        """

    @overload
    def get_paginator(self, operation_name: Literal["batch_get_traces"]) -> BatchGetTracesPaginator:
        """
        [Paginator.BatchGetTraces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.BatchGetTraces)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_groups"]) -> GetGroupsPaginator:
        """
        [Paginator.GetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_sampling_rules"]
    ) -> GetSamplingRulesPaginator:
        """
        [Paginator.GetSamplingRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetSamplingRules)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_sampling_statistic_summaries"]
    ) -> GetSamplingStatisticSummariesPaginator:
        """
        [Paginator.GetSamplingStatisticSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetSamplingStatisticSummaries)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_service_graph"]
    ) -> GetServiceGraphPaginator:
        """
        [Paginator.GetServiceGraph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetServiceGraph)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_time_series_service_statistics"]
    ) -> GetTimeSeriesServiceStatisticsPaginator:
        """
        [Paginator.GetTimeSeriesServiceStatistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetTimeSeriesServiceStatistics)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_trace_graph"]) -> GetTraceGraphPaginator:
        """
        [Paginator.GetTraceGraph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetTraceGraph)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_trace_summaries"]
    ) -> GetTraceSummariesPaginator:
        """
        [Paginator.GetTraceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/xray.html#XRay.Paginator.GetTraceSummaries)
        """
