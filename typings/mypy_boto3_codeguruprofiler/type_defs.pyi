"""
Type annotations for codeguruprofiler service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codeguruprofiler.type_defs import AddNotificationChannelsRequestRequestTypeDef

    data: AddNotificationChannelsRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AgentParameterFieldType,
    AggregationPeriodType,
    ComputePlatformType,
    FeedbackTypeType,
    MetadataFieldType,
    OrderByType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddNotificationChannelsRequestRequestTypeDef",
    "AddNotificationChannelsResponseTypeDef",
    "AgentConfigurationTypeDef",
    "AgentOrchestrationConfigTypeDef",
    "AggregatedProfileTimeTypeDef",
    "AnomalyInstanceTypeDef",
    "AnomalyTypeDef",
    "BatchGetFrameMetricDataRequestRequestTypeDef",
    "BatchGetFrameMetricDataResponseTypeDef",
    "ChannelTypeDef",
    "ConfigureAgentRequestRequestTypeDef",
    "ConfigureAgentResponseTypeDef",
    "CreateProfilingGroupRequestRequestTypeDef",
    "CreateProfilingGroupResponseTypeDef",
    "DeleteProfilingGroupRequestRequestTypeDef",
    "DescribeProfilingGroupRequestRequestTypeDef",
    "DescribeProfilingGroupResponseTypeDef",
    "FindingsReportSummaryTypeDef",
    "FrameMetricDatumTypeDef",
    "FrameMetricTypeDef",
    "GetFindingsReportAccountSummaryRequestRequestTypeDef",
    "GetFindingsReportAccountSummaryResponseTypeDef",
    "GetNotificationConfigurationRequestRequestTypeDef",
    "GetNotificationConfigurationResponseTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "GetPolicyResponseTypeDef",
    "GetProfileRequestRequestTypeDef",
    "GetProfileResponseTypeDef",
    "GetRecommendationsRequestRequestTypeDef",
    "GetRecommendationsResponseTypeDef",
    "ListFindingsReportsRequestRequestTypeDef",
    "ListFindingsReportsResponseTypeDef",
    "ListProfileTimesRequestRequestTypeDef",
    "ListProfileTimesResponseTypeDef",
    "ListProfilingGroupsRequestRequestTypeDef",
    "ListProfilingGroupsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MatchTypeDef",
    "MetricTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PatternTypeDef",
    "PostAgentProfileRequestRequestTypeDef",
    "ProfileTimeTypeDef",
    "ProfilingGroupDescriptionTypeDef",
    "ProfilingStatusTypeDef",
    "PutPermissionRequestRequestTypeDef",
    "PutPermissionResponseTypeDef",
    "RecommendationTypeDef",
    "RemoveNotificationChannelRequestRequestTypeDef",
    "RemoveNotificationChannelResponseTypeDef",
    "RemovePermissionRequestRequestTypeDef",
    "RemovePermissionResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SubmitFeedbackRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TimestampStructureTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateProfilingGroupRequestRequestTypeDef",
    "UpdateProfilingGroupResponseTypeDef",
    "UserFeedbackTypeDef",
)

AddNotificationChannelsRequestRequestTypeDef = TypedDict(
    "AddNotificationChannelsRequestRequestTypeDef",
    {
        "channels": List["ChannelTypeDef"],
        "profilingGroupName": str,
    },
)

AddNotificationChannelsResponseTypeDef = TypedDict(
    "AddNotificationChannelsResponseTypeDef",
    {
        "notificationConfiguration": "NotificationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAgentConfigurationTypeDef = TypedDict(
    "_RequiredAgentConfigurationTypeDef",
    {
        "periodInSeconds": int,
        "shouldProfile": bool,
    },
)
_OptionalAgentConfigurationTypeDef = TypedDict(
    "_OptionalAgentConfigurationTypeDef",
    {
        "agentParameters": Dict[AgentParameterFieldType, str],
    },
    total=False,
)

class AgentConfigurationTypeDef(
    _RequiredAgentConfigurationTypeDef, _OptionalAgentConfigurationTypeDef
):
    pass

AgentOrchestrationConfigTypeDef = TypedDict(
    "AgentOrchestrationConfigTypeDef",
    {
        "profilingEnabled": bool,
    },
)

AggregatedProfileTimeTypeDef = TypedDict(
    "AggregatedProfileTimeTypeDef",
    {
        "period": AggregationPeriodType,
        "start": datetime,
    },
    total=False,
)

_RequiredAnomalyInstanceTypeDef = TypedDict(
    "_RequiredAnomalyInstanceTypeDef",
    {
        "id": str,
        "startTime": datetime,
    },
)
_OptionalAnomalyInstanceTypeDef = TypedDict(
    "_OptionalAnomalyInstanceTypeDef",
    {
        "endTime": datetime,
        "userFeedback": "UserFeedbackTypeDef",
    },
    total=False,
)

class AnomalyInstanceTypeDef(_RequiredAnomalyInstanceTypeDef, _OptionalAnomalyInstanceTypeDef):
    pass

AnomalyTypeDef = TypedDict(
    "AnomalyTypeDef",
    {
        "instances": List["AnomalyInstanceTypeDef"],
        "metric": "MetricTypeDef",
        "reason": str,
    },
)

_RequiredBatchGetFrameMetricDataRequestRequestTypeDef = TypedDict(
    "_RequiredBatchGetFrameMetricDataRequestRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)
_OptionalBatchGetFrameMetricDataRequestRequestTypeDef = TypedDict(
    "_OptionalBatchGetFrameMetricDataRequestRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "frameMetrics": List["FrameMetricTypeDef"],
        "period": str,
        "startTime": Union[datetime, str],
        "targetResolution": AggregationPeriodType,
    },
    total=False,
)

class BatchGetFrameMetricDataRequestRequestTypeDef(
    _RequiredBatchGetFrameMetricDataRequestRequestTypeDef,
    _OptionalBatchGetFrameMetricDataRequestRequestTypeDef,
):
    pass

BatchGetFrameMetricDataResponseTypeDef = TypedDict(
    "BatchGetFrameMetricDataResponseTypeDef",
    {
        "endTime": datetime,
        "endTimes": List["TimestampStructureTypeDef"],
        "frameMetricData": List["FrameMetricDatumTypeDef"],
        "resolution": AggregationPeriodType,
        "startTime": datetime,
        "unprocessedEndTimes": Dict[str, List["TimestampStructureTypeDef"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredChannelTypeDef = TypedDict(
    "_RequiredChannelTypeDef",
    {
        "eventPublishers": List[Literal["AnomalyDetection"]],
        "uri": str,
    },
)
_OptionalChannelTypeDef = TypedDict(
    "_OptionalChannelTypeDef",
    {
        "id": str,
    },
    total=False,
)

class ChannelTypeDef(_RequiredChannelTypeDef, _OptionalChannelTypeDef):
    pass

_RequiredConfigureAgentRequestRequestTypeDef = TypedDict(
    "_RequiredConfigureAgentRequestRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)
_OptionalConfigureAgentRequestRequestTypeDef = TypedDict(
    "_OptionalConfigureAgentRequestRequestTypeDef",
    {
        "fleetInstanceId": str,
        "metadata": Dict[MetadataFieldType, str],
    },
    total=False,
)

class ConfigureAgentRequestRequestTypeDef(
    _RequiredConfigureAgentRequestRequestTypeDef, _OptionalConfigureAgentRequestRequestTypeDef
):
    pass

ConfigureAgentResponseTypeDef = TypedDict(
    "ConfigureAgentResponseTypeDef",
    {
        "configuration": "AgentConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProfilingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProfilingGroupRequestRequestTypeDef",
    {
        "clientToken": str,
        "profilingGroupName": str,
    },
)
_OptionalCreateProfilingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProfilingGroupRequestRequestTypeDef",
    {
        "agentOrchestrationConfig": "AgentOrchestrationConfigTypeDef",
        "computePlatform": ComputePlatformType,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateProfilingGroupRequestRequestTypeDef(
    _RequiredCreateProfilingGroupRequestRequestTypeDef,
    _OptionalCreateProfilingGroupRequestRequestTypeDef,
):
    pass

CreateProfilingGroupResponseTypeDef = TypedDict(
    "CreateProfilingGroupResponseTypeDef",
    {
        "profilingGroup": "ProfilingGroupDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProfilingGroupRequestRequestTypeDef = TypedDict(
    "DeleteProfilingGroupRequestRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)

DescribeProfilingGroupRequestRequestTypeDef = TypedDict(
    "DescribeProfilingGroupRequestRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)

DescribeProfilingGroupResponseTypeDef = TypedDict(
    "DescribeProfilingGroupResponseTypeDef",
    {
        "profilingGroup": "ProfilingGroupDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FindingsReportSummaryTypeDef = TypedDict(
    "FindingsReportSummaryTypeDef",
    {
        "id": str,
        "profileEndTime": datetime,
        "profileStartTime": datetime,
        "profilingGroupName": str,
        "totalNumberOfFindings": int,
    },
    total=False,
)

FrameMetricDatumTypeDef = TypedDict(
    "FrameMetricDatumTypeDef",
    {
        "frameMetric": "FrameMetricTypeDef",
        "values": List[float],
    },
)

FrameMetricTypeDef = TypedDict(
    "FrameMetricTypeDef",
    {
        "frameName": str,
        "threadStates": List[str],
        "type": Literal["AggregatedRelativeTotalTime"],
    },
)

GetFindingsReportAccountSummaryRequestRequestTypeDef = TypedDict(
    "GetFindingsReportAccountSummaryRequestRequestTypeDef",
    {
        "dailyReportsOnly": bool,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

GetFindingsReportAccountSummaryResponseTypeDef = TypedDict(
    "GetFindingsReportAccountSummaryResponseTypeDef",
    {
        "nextToken": str,
        "reportSummaries": List["FindingsReportSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNotificationConfigurationRequestRequestTypeDef = TypedDict(
    "GetNotificationConfigurationRequestRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)

GetNotificationConfigurationResponseTypeDef = TypedDict(
    "GetNotificationConfigurationResponseTypeDef",
    {
        "notificationConfiguration": "NotificationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyRequestRequestTypeDef = TypedDict(
    "GetPolicyRequestRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)

GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "policy": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetProfileRequestRequestTypeDef = TypedDict(
    "_RequiredGetProfileRequestRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)
_OptionalGetProfileRequestRequestTypeDef = TypedDict(
    "_OptionalGetProfileRequestRequestTypeDef",
    {
        "accept": str,
        "endTime": Union[datetime, str],
        "maxDepth": int,
        "period": str,
        "startTime": Union[datetime, str],
    },
    total=False,
)

class GetProfileRequestRequestTypeDef(
    _RequiredGetProfileRequestRequestTypeDef, _OptionalGetProfileRequestRequestTypeDef
):
    pass

GetProfileResponseTypeDef = TypedDict(
    "GetProfileResponseTypeDef",
    {
        "contentEncoding": str,
        "contentType": str,
        "profile": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRecommendationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetRecommendationsRequestRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "profilingGroupName": str,
        "startTime": Union[datetime, str],
    },
)
_OptionalGetRecommendationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetRecommendationsRequestRequestTypeDef",
    {
        "locale": str,
    },
    total=False,
)

class GetRecommendationsRequestRequestTypeDef(
    _RequiredGetRecommendationsRequestRequestTypeDef,
    _OptionalGetRecommendationsRequestRequestTypeDef,
):
    pass

GetRecommendationsResponseTypeDef = TypedDict(
    "GetRecommendationsResponseTypeDef",
    {
        "anomalies": List["AnomalyTypeDef"],
        "profileEndTime": datetime,
        "profileStartTime": datetime,
        "profilingGroupName": str,
        "recommendations": List["RecommendationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFindingsReportsRequestRequestTypeDef = TypedDict(
    "_RequiredListFindingsReportsRequestRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "profilingGroupName": str,
        "startTime": Union[datetime, str],
    },
)
_OptionalListFindingsReportsRequestRequestTypeDef = TypedDict(
    "_OptionalListFindingsReportsRequestRequestTypeDef",
    {
        "dailyReportsOnly": bool,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListFindingsReportsRequestRequestTypeDef(
    _RequiredListFindingsReportsRequestRequestTypeDef,
    _OptionalListFindingsReportsRequestRequestTypeDef,
):
    pass

ListFindingsReportsResponseTypeDef = TypedDict(
    "ListFindingsReportsResponseTypeDef",
    {
        "findingsReportSummaries": List["FindingsReportSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProfileTimesRequestRequestTypeDef = TypedDict(
    "_RequiredListProfileTimesRequestRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "period": AggregationPeriodType,
        "profilingGroupName": str,
        "startTime": Union[datetime, str],
    },
)
_OptionalListProfileTimesRequestRequestTypeDef = TypedDict(
    "_OptionalListProfileTimesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "orderBy": OrderByType,
    },
    total=False,
)

class ListProfileTimesRequestRequestTypeDef(
    _RequiredListProfileTimesRequestRequestTypeDef, _OptionalListProfileTimesRequestRequestTypeDef
):
    pass

ListProfileTimesResponseTypeDef = TypedDict(
    "ListProfileTimesResponseTypeDef",
    {
        "nextToken": str,
        "profileTimes": List["ProfileTimeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProfilingGroupsRequestRequestTypeDef = TypedDict(
    "ListProfilingGroupsRequestRequestTypeDef",
    {
        "includeDescription": bool,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListProfilingGroupsResponseTypeDef = TypedDict(
    "ListProfilingGroupsResponseTypeDef",
    {
        "nextToken": str,
        "profilingGroupNames": List[str],
        "profilingGroups": List["ProfilingGroupDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MatchTypeDef = TypedDict(
    "MatchTypeDef",
    {
        "frameAddress": str,
        "targetFramesIndex": int,
        "thresholdBreachValue": float,
    },
    total=False,
)

MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "frameName": str,
        "threadStates": List[str],
        "type": Literal["AggregatedRelativeTotalTime"],
    },
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "channels": List["ChannelTypeDef"],
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PatternTypeDef = TypedDict(
    "PatternTypeDef",
    {
        "countersToAggregate": List[str],
        "description": str,
        "id": str,
        "name": str,
        "resolutionSteps": str,
        "targetFrames": List[List[str]],
        "thresholdPercent": float,
    },
    total=False,
)

_RequiredPostAgentProfileRequestRequestTypeDef = TypedDict(
    "_RequiredPostAgentProfileRequestRequestTypeDef",
    {
        "agentProfile": Union[bytes, IO[bytes], StreamingBody],
        "contentType": str,
        "profilingGroupName": str,
    },
)
_OptionalPostAgentProfileRequestRequestTypeDef = TypedDict(
    "_OptionalPostAgentProfileRequestRequestTypeDef",
    {
        "profileToken": str,
    },
    total=False,
)

class PostAgentProfileRequestRequestTypeDef(
    _RequiredPostAgentProfileRequestRequestTypeDef, _OptionalPostAgentProfileRequestRequestTypeDef
):
    pass

ProfileTimeTypeDef = TypedDict(
    "ProfileTimeTypeDef",
    {
        "start": datetime,
    },
    total=False,
)

ProfilingGroupDescriptionTypeDef = TypedDict(
    "ProfilingGroupDescriptionTypeDef",
    {
        "agentOrchestrationConfig": "AgentOrchestrationConfigTypeDef",
        "arn": str,
        "computePlatform": ComputePlatformType,
        "createdAt": datetime,
        "name": str,
        "profilingStatus": "ProfilingStatusTypeDef",
        "tags": Dict[str, str],
        "updatedAt": datetime,
    },
    total=False,
)

ProfilingStatusTypeDef = TypedDict(
    "ProfilingStatusTypeDef",
    {
        "latestAgentOrchestratedAt": datetime,
        "latestAgentProfileReportedAt": datetime,
        "latestAggregatedProfile": "AggregatedProfileTimeTypeDef",
    },
    total=False,
)

_RequiredPutPermissionRequestRequestTypeDef = TypedDict(
    "_RequiredPutPermissionRequestRequestTypeDef",
    {
        "actionGroup": Literal["agentPermissions"],
        "principals": List[str],
        "profilingGroupName": str,
    },
)
_OptionalPutPermissionRequestRequestTypeDef = TypedDict(
    "_OptionalPutPermissionRequestRequestTypeDef",
    {
        "revisionId": str,
    },
    total=False,
)

class PutPermissionRequestRequestTypeDef(
    _RequiredPutPermissionRequestRequestTypeDef, _OptionalPutPermissionRequestRequestTypeDef
):
    pass

PutPermissionResponseTypeDef = TypedDict(
    "PutPermissionResponseTypeDef",
    {
        "policy": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "allMatchesCount": int,
        "allMatchesSum": float,
        "endTime": datetime,
        "pattern": "PatternTypeDef",
        "startTime": datetime,
        "topMatches": List["MatchTypeDef"],
    },
)

RemoveNotificationChannelRequestRequestTypeDef = TypedDict(
    "RemoveNotificationChannelRequestRequestTypeDef",
    {
        "channelId": str,
        "profilingGroupName": str,
    },
)

RemoveNotificationChannelResponseTypeDef = TypedDict(
    "RemoveNotificationChannelResponseTypeDef",
    {
        "notificationConfiguration": "NotificationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemovePermissionRequestRequestTypeDef = TypedDict(
    "RemovePermissionRequestRequestTypeDef",
    {
        "actionGroup": Literal["agentPermissions"],
        "profilingGroupName": str,
        "revisionId": str,
    },
)

RemovePermissionResponseTypeDef = TypedDict(
    "RemovePermissionResponseTypeDef",
    {
        "policy": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredSubmitFeedbackRequestRequestTypeDef = TypedDict(
    "_RequiredSubmitFeedbackRequestRequestTypeDef",
    {
        "anomalyInstanceId": str,
        "profilingGroupName": str,
        "type": FeedbackTypeType,
    },
)
_OptionalSubmitFeedbackRequestRequestTypeDef = TypedDict(
    "_OptionalSubmitFeedbackRequestRequestTypeDef",
    {
        "comment": str,
    },
    total=False,
)

class SubmitFeedbackRequestRequestTypeDef(
    _RequiredSubmitFeedbackRequestRequestTypeDef, _OptionalSubmitFeedbackRequestRequestTypeDef
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TimestampStructureTypeDef = TypedDict(
    "TimestampStructureTypeDef",
    {
        "value": datetime,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateProfilingGroupRequestRequestTypeDef = TypedDict(
    "UpdateProfilingGroupRequestRequestTypeDef",
    {
        "agentOrchestrationConfig": "AgentOrchestrationConfigTypeDef",
        "profilingGroupName": str,
    },
)

UpdateProfilingGroupResponseTypeDef = TypedDict(
    "UpdateProfilingGroupResponseTypeDef",
    {
        "profilingGroup": "ProfilingGroupDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserFeedbackTypeDef = TypedDict(
    "UserFeedbackTypeDef",
    {
        "type": FeedbackTypeType,
    },
)
