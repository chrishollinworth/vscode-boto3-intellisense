"""
Type annotations for codeguruprofiler service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_codeguruprofiler.client import CodeGuruProfilerClient

    session = Session()
    client: CodeGuruProfilerClient = session.client("codeguruprofiler")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListProfileTimesPaginator
from .type_defs import (
    AddNotificationChannelsRequestTypeDef,
    AddNotificationChannelsResponseTypeDef,
    BatchGetFrameMetricDataRequestTypeDef,
    BatchGetFrameMetricDataResponseTypeDef,
    ConfigureAgentRequestTypeDef,
    ConfigureAgentResponseTypeDef,
    CreateProfilingGroupRequestTypeDef,
    CreateProfilingGroupResponseTypeDef,
    DeleteProfilingGroupRequestTypeDef,
    DescribeProfilingGroupRequestTypeDef,
    DescribeProfilingGroupResponseTypeDef,
    GetFindingsReportAccountSummaryRequestTypeDef,
    GetFindingsReportAccountSummaryResponseTypeDef,
    GetNotificationConfigurationRequestTypeDef,
    GetNotificationConfigurationResponseTypeDef,
    GetPolicyRequestTypeDef,
    GetPolicyResponseTypeDef,
    GetProfileRequestTypeDef,
    GetProfileResponseTypeDef,
    GetRecommendationsRequestTypeDef,
    GetRecommendationsResponseTypeDef,
    ListFindingsReportsRequestTypeDef,
    ListFindingsReportsResponseTypeDef,
    ListProfileTimesRequestTypeDef,
    ListProfileTimesResponseTypeDef,
    ListProfilingGroupsRequestTypeDef,
    ListProfilingGroupsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PostAgentProfileRequestTypeDef,
    PutPermissionRequestTypeDef,
    PutPermissionResponseTypeDef,
    RemoveNotificationChannelRequestTypeDef,
    RemoveNotificationChannelResponseTypeDef,
    RemovePermissionRequestTypeDef,
    RemovePermissionResponseTypeDef,
    SubmitFeedbackRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateProfilingGroupRequestTypeDef,
    UpdateProfilingGroupResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("CodeGuruProfilerClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CodeGuruProfilerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CodeGuruProfilerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#generate_presigned_url)
        """

    def add_notification_channels(
        self, **kwargs: Unpack[AddNotificationChannelsRequestTypeDef]
    ) -> AddNotificationChannelsResponseTypeDef:
        """
        Add up to 2 anomaly notifications channels for a profiling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/add_notification_channels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#add_notification_channels)
        """

    def batch_get_frame_metric_data(
        self, **kwargs: Unpack[BatchGetFrameMetricDataRequestTypeDef]
    ) -> BatchGetFrameMetricDataResponseTypeDef:
        """
        Returns the time series of values for a requested list of frame metrics from a
        time period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/batch_get_frame_metric_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#batch_get_frame_metric_data)
        """

    def configure_agent(
        self, **kwargs: Unpack[ConfigureAgentRequestTypeDef]
    ) -> ConfigureAgentResponseTypeDef:
        """
        Used by profiler agents to report their current state and to receive remote
        configuration updates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/configure_agent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#configure_agent)
        """

    def create_profiling_group(
        self, **kwargs: Unpack[CreateProfilingGroupRequestTypeDef]
    ) -> CreateProfilingGroupResponseTypeDef:
        """
        Creates a profiling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/create_profiling_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#create_profiling_group)
        """

    def delete_profiling_group(
        self, **kwargs: Unpack[DeleteProfilingGroupRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a profiling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/delete_profiling_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#delete_profiling_group)
        """

    def describe_profiling_group(
        self, **kwargs: Unpack[DescribeProfilingGroupRequestTypeDef]
    ) -> DescribeProfilingGroupResponseTypeDef:
        """
        Returns a <a
        href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html">
        <code>ProfilingGroupDescription</code> </a> object that contains information
        about the requested profiling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/describe_profiling_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#describe_profiling_group)
        """

    def get_findings_report_account_summary(
        self, **kwargs: Unpack[GetFindingsReportAccountSummaryRequestTypeDef]
    ) -> GetFindingsReportAccountSummaryResponseTypeDef:
        """
        Returns a list of <a
        href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_FindingsReportSummary.html">
        <code>FindingsReportSummary</code> </a> objects that contain analysis results
        for all profiling groups in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/get_findings_report_account_summary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#get_findings_report_account_summary)
        """

    def get_notification_configuration(
        self, **kwargs: Unpack[GetNotificationConfigurationRequestTypeDef]
    ) -> GetNotificationConfigurationResponseTypeDef:
        """
        Get the current configuration for anomaly notifications for a profiling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/get_notification_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#get_notification_configuration)
        """

    def get_policy(self, **kwargs: Unpack[GetPolicyRequestTypeDef]) -> GetPolicyResponseTypeDef:
        """
        Returns the JSON-formatted resource-based policy on a profiling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/get_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#get_policy)
        """

    def get_profile(self, **kwargs: Unpack[GetProfileRequestTypeDef]) -> GetProfileResponseTypeDef:
        """
        Gets the aggregated profile of a profiling group for a specified time range.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/get_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#get_profile)
        """

    def get_recommendations(
        self, **kwargs: Unpack[GetRecommendationsRequestTypeDef]
    ) -> GetRecommendationsResponseTypeDef:
        """
        Returns a list of <a
        href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Recommendation.html">
        <code>Recommendation</code> </a> objects that contain recommendations for a
        profiling group for a given time period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/get_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#get_recommendations)
        """

    def list_findings_reports(
        self, **kwargs: Unpack[ListFindingsReportsRequestTypeDef]
    ) -> ListFindingsReportsResponseTypeDef:
        """
        List the available reports for a given profiling group and time range.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/list_findings_reports.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#list_findings_reports)
        """

    def list_profile_times(
        self, **kwargs: Unpack[ListProfileTimesRequestTypeDef]
    ) -> ListProfileTimesResponseTypeDef:
        """
        Lists the start times of the available aggregated profiles of a profiling group
        for an aggregation period within the specified time range.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/list_profile_times.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#list_profile_times)
        """

    def list_profiling_groups(
        self, **kwargs: Unpack[ListProfilingGroupsRequestTypeDef]
    ) -> ListProfilingGroupsResponseTypeDef:
        """
        Returns a list of profiling groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/list_profiling_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#list_profiling_groups)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of the tags that are assigned to a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#list_tags_for_resource)
        """

    def post_agent_profile(
        self, **kwargs: Unpack[PostAgentProfileRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Submits profiling data to an aggregated profile of a profiling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/post_agent_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#post_agent_profile)
        """

    def put_permission(
        self, **kwargs: Unpack[PutPermissionRequestTypeDef]
    ) -> PutPermissionResponseTypeDef:
        """
        Adds permissions to a profiling group's resource-based policy that are provided
        using an action group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/put_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#put_permission)
        """

    def remove_notification_channel(
        self, **kwargs: Unpack[RemoveNotificationChannelRequestTypeDef]
    ) -> RemoveNotificationChannelResponseTypeDef:
        """
        Remove one anomaly notifications channel for a profiling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/remove_notification_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#remove_notification_channel)
        """

    def remove_permission(
        self, **kwargs: Unpack[RemovePermissionRequestTypeDef]
    ) -> RemovePermissionResponseTypeDef:
        """
        Removes permissions from a profiling group's resource-based policy that are
        provided using an action group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/remove_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#remove_permission)
        """

    def submit_feedback(self, **kwargs: Unpack[SubmitFeedbackRequestTypeDef]) -> Dict[str, Any]:
        """
        Sends feedback to CodeGuru Profiler about whether the anomaly detected by the
        analysis is useful or not.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/submit_feedback.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#submit_feedback)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Use to assign one or more tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Use to remove one or more tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#untag_resource)
        """

    def update_profiling_group(
        self, **kwargs: Unpack[UpdateProfilingGroupRequestTypeDef]
    ) -> UpdateProfilingGroupResponseTypeDef:
        """
        Updates a profiling group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/update_profiling_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#update_profiling_group)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_profile_times"]
    ) -> ListProfileTimesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client/#get_paginator)
        """
