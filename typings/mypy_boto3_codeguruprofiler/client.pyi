# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for codeguruprofiler service client

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

from botocore.client import ClientMeta

from mypy_boto3_codeguruprofiler.paginator import ListProfileTimesPaginator
from mypy_boto3_codeguruprofiler.type_defs import (
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


class CodeGuruProfilerClient:
    """
    [CodeGuruProfiler.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_notification_channels(
        self, channels: List["ChannelTypeDef"], profilingGroupName: str
    ) -> AddNotificationChannelsResponseTypeDef:
        """
        [Client.add_notification_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.add_notification_channels)
        """

    def batch_get_frame_metric_data(
        self,
        profilingGroupName: str,
        endTime: datetime = None,
        frameMetrics: List["FrameMetricTypeDef"] = None,
        period: str = None,
        startTime: datetime = None,
        targetResolution: Literal["P1D", "PT1H", "PT5M"] = None,
    ) -> BatchGetFrameMetricDataResponseTypeDef:
        """
        [Client.batch_get_frame_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.batch_get_frame_metric_data)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.can_paginate)
        """

    def configure_agent(
        self,
        profilingGroupName: str,
        fleetInstanceId: str = None,
        metadata: Dict[
            Literal[
                "AgentId",
                "AwsRequestId",
                "ComputePlatform",
                "ExecutionEnvironment",
                "LambdaFunctionArn",
                "LambdaMemoryLimitInMB",
                "LambdaPreviousExecutionTimeInMilliseconds",
                "LambdaRemainingTimeInMilliseconds",
                "LambdaTimeGapBetweenInvokesInMilliseconds",
            ],
            str,
        ] = None,
    ) -> ConfigureAgentResponseTypeDef:
        """
        [Client.configure_agent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.configure_agent)
        """

    def create_profiling_group(
        self,
        clientToken: str,
        profilingGroupName: str,
        agentOrchestrationConfig: "AgentOrchestrationConfigTypeDef" = None,
        computePlatform: Literal["AWSLambda", "Default"] = None,
        tags: Dict[str, str] = None,
    ) -> CreateProfilingGroupResponseTypeDef:
        """
        [Client.create_profiling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.create_profiling_group)
        """

    def delete_profiling_group(self, profilingGroupName: str) -> Dict[str, Any]:
        """
        [Client.delete_profiling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.delete_profiling_group)
        """

    def describe_profiling_group(
        self, profilingGroupName: str
    ) -> DescribeProfilingGroupResponseTypeDef:
        """
        [Client.describe_profiling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.describe_profiling_group)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.generate_presigned_url)
        """

    def get_findings_report_account_summary(
        self, dailyReportsOnly: bool = None, maxResults: int = None, nextToken: str = None
    ) -> GetFindingsReportAccountSummaryResponseTypeDef:
        """
        [Client.get_findings_report_account_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_findings_report_account_summary)
        """

    def get_notification_configuration(
        self, profilingGroupName: str
    ) -> GetNotificationConfigurationResponseTypeDef:
        """
        [Client.get_notification_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_notification_configuration)
        """

    def get_policy(self, profilingGroupName: str) -> GetPolicyResponseTypeDef:
        """
        [Client.get_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_policy)
        """

    def get_profile(
        self,
        profilingGroupName: str,
        accept: str = None,
        endTime: datetime = None,
        maxDepth: int = None,
        period: str = None,
        startTime: datetime = None,
    ) -> GetProfileResponseTypeDef:
        """
        [Client.get_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_profile)
        """

    def get_recommendations(
        self, endTime: datetime, profilingGroupName: str, startTime: datetime, locale: str = None
    ) -> GetRecommendationsResponseTypeDef:
        """
        [Client.get_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_recommendations)
        """

    def list_findings_reports(
        self,
        endTime: datetime,
        profilingGroupName: str,
        startTime: datetime,
        dailyReportsOnly: bool = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListFindingsReportsResponseTypeDef:
        """
        [Client.list_findings_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_findings_reports)
        """

    def list_profile_times(
        self,
        endTime: datetime,
        period: Literal["P1D", "PT1H", "PT5M"],
        profilingGroupName: str,
        startTime: datetime,
        maxResults: int = None,
        nextToken: str = None,
        orderBy: Literal["TimestampAscending", "TimestampDescending"] = None,
    ) -> ListProfileTimesResponseTypeDef:
        """
        [Client.list_profile_times documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_profile_times)
        """

    def list_profiling_groups(
        self, includeDescription: bool = None, maxResults: int = None, nextToken: str = None
    ) -> ListProfilingGroupsResponseTypeDef:
        """
        [Client.list_profiling_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_profiling_groups)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_tags_for_resource)
        """

    def post_agent_profile(
        self,
        agentProfile: Union[bytes, IO[bytes]],
        contentType: str,
        profilingGroupName: str,
        profileToken: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.post_agent_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.post_agent_profile)
        """

    def put_permission(
        self,
        actionGroup: Literal["agentPermissions"],
        principals: List[str],
        profilingGroupName: str,
        revisionId: str = None,
    ) -> PutPermissionResponseTypeDef:
        """
        [Client.put_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.put_permission)
        """

    def remove_notification_channel(
        self, channelId: str, profilingGroupName: str
    ) -> RemoveNotificationChannelResponseTypeDef:
        """
        [Client.remove_notification_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.remove_notification_channel)
        """

    def remove_permission(
        self, actionGroup: Literal["agentPermissions"], profilingGroupName: str, revisionId: str
    ) -> RemovePermissionResponseTypeDef:
        """
        [Client.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.remove_permission)
        """

    def submit_feedback(
        self,
        anomalyInstanceId: str,
        profilingGroupName: str,
        type: Literal["Negative", "Positive"],
        comment: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.submit_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.submit_feedback)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.untag_resource)
        """

    def update_profiling_group(
        self, agentOrchestrationConfig: "AgentOrchestrationConfigTypeDef", profilingGroupName: str
    ) -> UpdateProfilingGroupResponseTypeDef:
        """
        [Client.update_profiling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.update_profiling_group)
        """

    def get_paginator(
        self, operation_name: Literal["list_profile_times"]
    ) -> ListProfileTimesPaginator:
        """
        [Paginator.ListProfileTimes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeguruprofiler.html#CodeGuruProfiler.Paginator.ListProfileTimes)
        """
