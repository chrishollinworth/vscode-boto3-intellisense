"""
Type annotations for codeguruprofiler service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_codeguruprofiler import CodeGuruProfilerClient

    client: CodeGuruProfilerClient = boto3.client("codeguruprofiler")
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import (
    AggregationPeriodType,
    ComputePlatformType,
    FeedbackTypeType,
    MetadataFieldType,
    OrderByType,
)
from .paginator import ListProfileTimesPaginator
from .type_defs import (
    AddNotificationChannelsResponseTypeDef,
    AgentOrchestrationConfigTypeDef,
    BatchGetFrameMetricDataResponseTypeDef,
    ChannelTypeDef,
    ConfigureAgentResponseTypeDef,
    CreateProfilingGroupResponseTypeDef,
    DescribeProfilingGroupResponseTypeDef,
    FrameMetricTypeDef,
    GetFindingsReportAccountSummaryResponseTypeDef,
    GetNotificationConfigurationResponseTypeDef,
    GetPolicyResponseTypeDef,
    GetProfileResponseTypeDef,
    GetRecommendationsResponseTypeDef,
    ListFindingsReportsResponseTypeDef,
    ListProfileTimesResponseTypeDef,
    ListProfilingGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutPermissionResponseTypeDef,
    RemoveNotificationChannelResponseTypeDef,
    RemovePermissionResponseTypeDef,
    UpdateProfilingGroupResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CodeGuruProfilerClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CodeGuruProfilerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CodeGuruProfilerClient exceptions.
        """
    def add_notification_channels(
        self, *, channels: List["ChannelTypeDef"], profilingGroupName: str
    ) -> AddNotificationChannelsResponseTypeDef:
        """
        Add up to 2 anomaly notifications channels for a profiling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.add_notification_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#add_notification_channels)
        """
    def batch_get_frame_metric_data(
        self,
        *,
        profilingGroupName: str,
        endTime: Union[datetime, str] = None,
        frameMetrics: List["FrameMetricTypeDef"] = None,
        period: str = None,
        startTime: Union[datetime, str] = None,
        targetResolution: AggregationPeriodType = None
    ) -> BatchGetFrameMetricDataResponseTypeDef:
        """
        Returns the time series of values for a requested list of frame metrics from a
        time period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.batch_get_frame_metric_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#batch_get_frame_metric_data)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#close)
        """
    def configure_agent(
        self,
        *,
        profilingGroupName: str,
        fleetInstanceId: str = None,
        metadata: Dict[MetadataFieldType, str] = None
    ) -> ConfigureAgentResponseTypeDef:
        """
        Used by profiler agents to report their current state and to receive remote
        configuration updates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.configure_agent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#configure_agent)
        """
    def create_profiling_group(
        self,
        *,
        clientToken: str,
        profilingGroupName: str,
        agentOrchestrationConfig: "AgentOrchestrationConfigTypeDef" = None,
        computePlatform: ComputePlatformType = None,
        tags: Dict[str, str] = None
    ) -> CreateProfilingGroupResponseTypeDef:
        """
        Creates a profiling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.create_profiling_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#create_profiling_group)
        """
    def delete_profiling_group(self, *, profilingGroupName: str) -> Dict[str, Any]:
        """
        Deletes a profiling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.delete_profiling_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#delete_profiling_group)
        """
    def describe_profiling_group(
        self, *, profilingGroupName: str
    ) -> DescribeProfilingGroupResponseTypeDef:
        """
        Returns a `ProfilingGroupDescription
        <https://docs.aws.amazon.com/codeguru/latest/profiler-
        api/API_ProfilingGroupDescription.html>`__ object that contains information
        about the requested profiling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.describe_profiling_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#describe_profiling_group)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#generate_presigned_url)
        """
    def get_findings_report_account_summary(
        self, *, dailyReportsOnly: bool = None, maxResults: int = None, nextToken: str = None
    ) -> GetFindingsReportAccountSummaryResponseTypeDef:
        """
        Returns a list of `FindingsReportSummary
        <https://docs.aws.amazon.com/codeguru/latest/profiler-
        api/API_FindingsReportSummary.html>`__ objects that contain analysis results for
        all profiling groups in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_findings_report_account_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#get_findings_report_account_summary)
        """
    def get_notification_configuration(
        self, *, profilingGroupName: str
    ) -> GetNotificationConfigurationResponseTypeDef:
        """
        Get the current configuration for anomaly notifications for a profiling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_notification_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#get_notification_configuration)
        """
    def get_policy(self, *, profilingGroupName: str) -> GetPolicyResponseTypeDef:
        """
        Returns the JSON-formatted resource-based policy on a profiling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#get_policy)
        """
    def get_profile(
        self,
        *,
        profilingGroupName: str,
        accept: str = None,
        endTime: Union[datetime, str] = None,
        maxDepth: int = None,
        period: str = None,
        startTime: Union[datetime, str] = None
    ) -> GetProfileResponseTypeDef:
        """
        Gets the aggregated profile of a profiling group for a specified time range.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#get_profile)
        """
    def get_recommendations(
        self,
        *,
        endTime: Union[datetime, str],
        profilingGroupName: str,
        startTime: Union[datetime, str],
        locale: str = None
    ) -> GetRecommendationsResponseTypeDef:
        """
        Returns a list of `Recommendation
        <https://docs.aws.amazon.com/codeguru/latest/profiler-
        api/API_Recommendation.html>`__ objects that contain recommendations for a
        profiling group for a given time period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#get_recommendations)
        """
    def list_findings_reports(
        self,
        *,
        endTime: Union[datetime, str],
        profilingGroupName: str,
        startTime: Union[datetime, str],
        dailyReportsOnly: bool = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListFindingsReportsResponseTypeDef:
        """
        List the available reports for a given profiling group and time range.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_findings_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#list_findings_reports)
        """
    def list_profile_times(
        self,
        *,
        endTime: Union[datetime, str],
        period: AggregationPeriodType,
        profilingGroupName: str,
        startTime: Union[datetime, str],
        maxResults: int = None,
        nextToken: str = None,
        orderBy: OrderByType = None
    ) -> ListProfileTimesResponseTypeDef:
        """
        Lists the start times of the available aggregated profiles of a profiling group
        for an aggregation period within the specified time range.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_profile_times)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#list_profile_times)
        """
    def list_profiling_groups(
        self, *, includeDescription: bool = None, maxResults: int = None, nextToken: str = None
    ) -> ListProfilingGroupsResponseTypeDef:
        """
        Returns a list of profiling groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_profiling_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#list_profiling_groups)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of the tags that are assigned to a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#list_tags_for_resource)
        """
    def post_agent_profile(
        self,
        *,
        agentProfile: Union[bytes, IO[bytes], StreamingBody],
        contentType: str,
        profilingGroupName: str,
        profileToken: str = None
    ) -> Dict[str, Any]:
        """
        Submits profiling data to an aggregated profile of a profiling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.post_agent_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#post_agent_profile)
        """
    def put_permission(
        self,
        *,
        actionGroup: Literal["agentPermissions"],
        principals: List[str],
        profilingGroupName: str,
        revisionId: str = None
    ) -> PutPermissionResponseTypeDef:
        """
        Adds permissions to a profiling group's resource-based policy that are provided
        using an action group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.put_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#put_permission)
        """
    def remove_notification_channel(
        self, *, channelId: str, profilingGroupName: str
    ) -> RemoveNotificationChannelResponseTypeDef:
        """
        Remove one anomaly notifications channel for a profiling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.remove_notification_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#remove_notification_channel)
        """
    def remove_permission(
        self, *, actionGroup: Literal["agentPermissions"], profilingGroupName: str, revisionId: str
    ) -> RemovePermissionResponseTypeDef:
        """
        Removes permissions from a profiling group's resource-based policy that are
        provided using an action group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.remove_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#remove_permission)
        """
    def submit_feedback(
        self,
        *,
        anomalyInstanceId: str,
        profilingGroupName: str,
        type: FeedbackTypeType,
        comment: str = None
    ) -> Dict[str, Any]:
        """
        Sends feedback to CodeGuru Profiler about whether the anomaly detected by the
        analysis is useful or not.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.submit_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#submit_feedback)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Use to assign one or more tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Use to remove one or more tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#untag_resource)
        """
    def update_profiling_group(
        self,
        *,
        agentOrchestrationConfig: "AgentOrchestrationConfigTypeDef",
        profilingGroupName: str
    ) -> UpdateProfilingGroupResponseTypeDef:
        """
        Updates a profiling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.update_profiling_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#update_profiling_group)
        """
    def get_paginator(
        self, operation_name: Literal["list_profile_times"]
    ) -> ListProfileTimesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/codeguruprofiler.html#CodeGuruProfiler.Paginator.ListProfileTimes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/paginators.html#listprofiletimespaginator)
        """
