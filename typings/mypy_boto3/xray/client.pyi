"""
Type annotations for xray service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_xray import XRayClient

    client: XRayClient = boto3.client("xray")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import EncryptionTypeType, InsightStateType, TimeRangeTypeType
from .paginator import (
    BatchGetTracesPaginator,
    GetGroupsPaginator,
    GetSamplingRulesPaginator,
    GetSamplingStatisticSummariesPaginator,
    GetServiceGraphPaginator,
    GetTimeSeriesServiceStatisticsPaginator,
    GetTraceGraphPaginator,
    GetTraceSummariesPaginator,
)
from .type_defs import (
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

class XRayClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        XRayClient exceptions.
        """
    def batch_get_traces(
        self, *, TraceIds: List[str], NextToken: str = None
    ) -> BatchGetTracesResultTypeDef:
        """
        Retrieves a list of traces specified by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.batch_get_traces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#batch_get_traces)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#can_paginate)
        """
    def create_group(
        self,
        *,
        GroupName: str,
        FilterExpression: str = None,
        InsightsConfiguration: "InsightsConfigurationTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateGroupResultTypeDef:
        """
        Creates a group resource with a name and a filter expression.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.create_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#create_group)
        """
    def create_sampling_rule(
        self, *, SamplingRule: "SamplingRuleTypeDef", Tags: List["TagTypeDef"] = None
    ) -> CreateSamplingRuleResultTypeDef:
        """
        Creates a rule to control sampling behavior for instrumented applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.create_sampling_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#create_sampling_rule)
        """
    def delete_group(self, *, GroupName: str = None, GroupARN: str = None) -> Dict[str, Any]:
        """
        Deletes a group resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.delete_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#delete_group)
        """
    def delete_sampling_rule(
        self, *, RuleName: str = None, RuleARN: str = None
    ) -> DeleteSamplingRuleResultTypeDef:
        """
        Deletes a sampling rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.delete_sampling_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#delete_sampling_rule)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#generate_presigned_url)
        """
    def get_encryption_config(self) -> GetEncryptionConfigResultTypeDef:
        """
        Retrieves the current encryption configuration for X-Ray data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.get_encryption_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#get_encryption_config)
        """
    def get_group(self, *, GroupName: str = None, GroupARN: str = None) -> GetGroupResultTypeDef:
        """
        Retrieves group resource details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.get_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#get_group)
        """
    def get_groups(self, *, NextToken: str = None) -> GetGroupsResultTypeDef:
        """
        Retrieves all active group details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.get_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#get_groups)
        """
    def get_insight(self, *, InsightId: str) -> GetInsightResultTypeDef:
        """
        Retrieves the summary information of an insight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.get_insight)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#get_insight)
        """
    def get_insight_events(
        self, *, InsightId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetInsightEventsResultTypeDef:
        """
        X-Ray reevaluates insights periodically until they're resolved, and records each
        intermediate state as an event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.get_insight_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#get_insight_events)
        """
    def get_insight_impact_graph(
        self,
        *,
        InsightId: str,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        NextToken: str = None
    ) -> GetInsightImpactGraphResultTypeDef:
        """
        Retrieves a service graph structure filtered by the specified insight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.get_insight_impact_graph)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#get_insight_impact_graph)
        """
    def get_insight_summaries(
        self,
        *,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        States: List[InsightStateType] = None,
        GroupARN: str = None,
        GroupName: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetInsightSummariesResultTypeDef:
        """
        Retrieves the summaries of all insights in the specified group matching the
        provided filter values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.get_insight_summaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#get_insight_summaries)
        """
    def get_sampling_rules(self, *, NextToken: str = None) -> GetSamplingRulesResultTypeDef:
        """
        Retrieves all sampling rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.get_sampling_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#get_sampling_rules)
        """
    def get_sampling_statistic_summaries(
        self, *, NextToken: str = None
    ) -> GetSamplingStatisticSummariesResultTypeDef:
        """
        Retrieves information about recent sampling results for all sampling rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.get_sampling_statistic_summaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#get_sampling_statistic_summaries)
        """
    def get_sampling_targets(
        self, *, SamplingStatisticsDocuments: List["SamplingStatisticsDocumentTypeDef"]
    ) -> GetSamplingTargetsResultTypeDef:
        """
        Requests a sampling quota for rules that the service is using to sample
        requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.get_sampling_targets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#get_sampling_targets)
        """
    def get_service_graph(
        self,
        *,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        GroupName: str = None,
        GroupARN: str = None,
        NextToken: str = None
    ) -> GetServiceGraphResultTypeDef:
        """
        Retrieves a document that describes services that process incoming requests, and
        downstream services that they call as a result.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.get_service_graph)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#get_service_graph)
        """
    def get_time_series_service_statistics(
        self,
        *,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        GroupName: str = None,
        GroupARN: str = None,
        EntitySelectorExpression: str = None,
        Period: int = None,
        ForecastStatistics: bool = None,
        NextToken: str = None
    ) -> GetTimeSeriesServiceStatisticsResultTypeDef:
        """
        Get an aggregation of service statistics defined by a specific time range.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.get_time_series_service_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#get_time_series_service_statistics)
        """
    def get_trace_graph(
        self, *, TraceIds: List[str], NextToken: str = None
    ) -> GetTraceGraphResultTypeDef:
        """
        Retrieves a service graph for one or more specific trace IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.get_trace_graph)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#get_trace_graph)
        """
    def get_trace_summaries(
        self,
        *,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        TimeRangeType: TimeRangeTypeType = None,
        Sampling: bool = None,
        SamplingStrategy: "SamplingStrategyTypeDef" = None,
        FilterExpression: str = None,
        NextToken: str = None
    ) -> GetTraceSummariesResultTypeDef:
        """
        Retrieves IDs and annotations for traces available for a specified time frame
        using an optional filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.get_trace_summaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#get_trace_summaries)
        """
    def list_tags_for_resource(
        self, *, ResourceARN: str, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags that are applied to the specified Amazon Web Services
        X-Ray group or sampling rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#list_tags_for_resource)
        """
    def put_encryption_config(
        self, *, Type: EncryptionTypeType, KeyId: str = None
    ) -> PutEncryptionConfigResultTypeDef:
        """
        Updates the encryption configuration for X-Ray data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.put_encryption_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#put_encryption_config)
        """
    def put_telemetry_records(
        self,
        *,
        TelemetryRecords: List["TelemetryRecordTypeDef"],
        EC2InstanceId: str = None,
        Hostname: str = None,
        ResourceARN: str = None
    ) -> Dict[str, Any]:
        """
        Used by the Amazon Web Services X-Ray daemon to upload telemetry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.put_telemetry_records)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#put_telemetry_records)
        """
    def put_trace_segments(
        self, *, TraceSegmentDocuments: List[str]
    ) -> PutTraceSegmentsResultTypeDef:
        """
        Uploads segment documents to Amazon Web Services X-Ray.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.put_trace_segments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#put_trace_segments)
        """
    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Applies tags to an existing Amazon Web Services X-Ray group or sampling rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from an Amazon Web Services X-Ray group or sampling rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#untag_resource)
        """
    def update_group(
        self,
        *,
        GroupName: str = None,
        GroupARN: str = None,
        FilterExpression: str = None,
        InsightsConfiguration: "InsightsConfigurationTypeDef" = None
    ) -> UpdateGroupResultTypeDef:
        """
        Updates a group resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.update_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#update_group)
        """
    def update_sampling_rule(
        self, *, SamplingRuleUpdate: "SamplingRuleUpdateTypeDef"
    ) -> UpdateSamplingRuleResultTypeDef:
        """
        Modifies a sampling rule's configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Client.update_sampling_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/client.html#update_sampling_rule)
        """
    @overload
    def get_paginator(self, operation_name: Literal["batch_get_traces"]) -> BatchGetTracesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Paginator.BatchGetTraces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators.html#batchgettracespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_groups"]) -> GetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Paginator.GetGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators.html#getgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_sampling_rules"]
    ) -> GetSamplingRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Paginator.GetSamplingRules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators.html#getsamplingrulespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_sampling_statistic_summaries"]
    ) -> GetSamplingStatisticSummariesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Paginator.GetSamplingStatisticSummaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators.html#getsamplingstatisticsummariespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_service_graph"]
    ) -> GetServiceGraphPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Paginator.GetServiceGraph)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators.html#getservicegraphpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_time_series_service_statistics"]
    ) -> GetTimeSeriesServiceStatisticsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Paginator.GetTimeSeriesServiceStatistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators.html#gettimeseriesservicestatisticspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_trace_graph"]) -> GetTraceGraphPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Paginator.GetTraceGraph)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators.html#gettracegraphpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_trace_summaries"]
    ) -> GetTraceSummariesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/xray.html#XRay.Paginator.GetTraceSummaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/paginators.html#gettracesummariespaginator)
        """
