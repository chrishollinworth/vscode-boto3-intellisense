"""
Main interface for codeguruprofiler service type definitions.

Usage::

    ```python
    from mypy_boto3_codeguruprofiler.type_defs import AgentConfigurationTypeDef

    data: AgentConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AgentConfigurationTypeDef",
    "AgentOrchestrationConfigTypeDef",
    "AggregatedProfileTimeTypeDef",
    "AnomalyInstanceTypeDef",
    "AnomalyTypeDef",
    "ChannelTypeDef",
    "FindingsReportSummaryTypeDef",
    "FrameMetricDatumTypeDef",
    "FrameMetricTypeDef",
    "MatchTypeDef",
    "MetricTypeDef",
    "NotificationConfigurationTypeDef",
    "PatternTypeDef",
    "ProfileTimeTypeDef",
    "ProfilingGroupDescriptionTypeDef",
    "ProfilingStatusTypeDef",
    "RecommendationTypeDef",
    "TimestampStructureTypeDef",
    "UserFeedbackTypeDef",
    "AddNotificationChannelsResponseTypeDef",
    "BatchGetFrameMetricDataResponseTypeDef",
    "ConfigureAgentResponseTypeDef",
    "CreateProfilingGroupResponseTypeDef",
    "DescribeProfilingGroupResponseTypeDef",
    "GetFindingsReportAccountSummaryResponseTypeDef",
    "GetNotificationConfigurationResponseTypeDef",
    "GetPolicyResponseTypeDef",
    "GetProfileResponseTypeDef",
    "GetRecommendationsResponseTypeDef",
    "ListFindingsReportsResponseTypeDef",
    "ListProfileTimesResponseTypeDef",
    "ListProfilingGroupsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutPermissionResponseTypeDef",
    "RemoveNotificationChannelResponseTypeDef",
    "RemovePermissionResponseTypeDef",
    "UpdateProfilingGroupResponseTypeDef",
)

_RequiredAgentConfigurationTypeDef = TypedDict(
    "_RequiredAgentConfigurationTypeDef", {"periodInSeconds": int, "shouldProfile": bool}
)
_OptionalAgentConfigurationTypeDef = TypedDict(
    "_OptionalAgentConfigurationTypeDef",
    {
        "agentParameters": Dict[
            Literal[
                "MaxStackDepth",
                "MemoryUsageLimitPercent",
                "MinimumTimeForReportingInMilliseconds",
                "ReportingIntervalInMilliseconds",
                "SamplingIntervalInMilliseconds",
            ],
            str,
        ]
    },
    total=False,
)


class AgentConfigurationTypeDef(
    _RequiredAgentConfigurationTypeDef, _OptionalAgentConfigurationTypeDef
):
    pass


AgentOrchestrationConfigTypeDef = TypedDict(
    "AgentOrchestrationConfigTypeDef", {"profilingEnabled": bool}
)

AggregatedProfileTimeTypeDef = TypedDict(
    "AggregatedProfileTimeTypeDef",
    {"period": Literal["P1D", "PT1H", "PT5M"], "start": datetime},
    total=False,
)

_RequiredAnomalyInstanceTypeDef = TypedDict(
    "_RequiredAnomalyInstanceTypeDef", {"id": str, "startTime": datetime}
)
_OptionalAnomalyInstanceTypeDef = TypedDict(
    "_OptionalAnomalyInstanceTypeDef",
    {"endTime": datetime, "userFeedback": "UserFeedbackTypeDef"},
    total=False,
)


class AnomalyInstanceTypeDef(_RequiredAnomalyInstanceTypeDef, _OptionalAnomalyInstanceTypeDef):
    pass


AnomalyTypeDef = TypedDict(
    "AnomalyTypeDef",
    {"instances": List["AnomalyInstanceTypeDef"], "metric": "MetricTypeDef", "reason": str},
)

_RequiredChannelTypeDef = TypedDict(
    "_RequiredChannelTypeDef", {"eventPublishers": List[Literal["AnomalyDetection"]], "uri": str}
)
_OptionalChannelTypeDef = TypedDict("_OptionalChannelTypeDef", {"id": str}, total=False)


class ChannelTypeDef(_RequiredChannelTypeDef, _OptionalChannelTypeDef):
    pass


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
    "FrameMetricDatumTypeDef", {"frameMetric": "FrameMetricTypeDef", "values": List[float]}
)

FrameMetricTypeDef = TypedDict(
    "FrameMetricTypeDef",
    {"frameName": str, "threadStates": List[str], "type": Literal["AggregatedRelativeTotalTime"]},
)

MatchTypeDef = TypedDict(
    "MatchTypeDef",
    {"frameAddress": str, "targetFramesIndex": int, "thresholdBreachValue": float},
    total=False,
)

MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {"frameName": str, "threadStates": List[str], "type": Literal["AggregatedRelativeTotalTime"]},
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef", {"channels": List["ChannelTypeDef"]}, total=False
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

ProfileTimeTypeDef = TypedDict("ProfileTimeTypeDef", {"start": datetime}, total=False)

ProfilingGroupDescriptionTypeDef = TypedDict(
    "ProfilingGroupDescriptionTypeDef",
    {
        "agentOrchestrationConfig": "AgentOrchestrationConfigTypeDef",
        "arn": str,
        "computePlatform": Literal["AWSLambda", "Default"],
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

TimestampStructureTypeDef = TypedDict("TimestampStructureTypeDef", {"value": datetime})

UserFeedbackTypeDef = TypedDict("UserFeedbackTypeDef", {"type": Literal["Negative", "Positive"]})

AddNotificationChannelsResponseTypeDef = TypedDict(
    "AddNotificationChannelsResponseTypeDef",
    {"notificationConfiguration": "NotificationConfigurationTypeDef"},
    total=False,
)

BatchGetFrameMetricDataResponseTypeDef = TypedDict(
    "BatchGetFrameMetricDataResponseTypeDef",
    {
        "endTime": datetime,
        "endTimes": List["TimestampStructureTypeDef"],
        "frameMetricData": List["FrameMetricDatumTypeDef"],
        "resolution": Literal["P1D", "PT1H", "PT5M"],
        "startTime": datetime,
        "unprocessedEndTimes": Dict[str, List["TimestampStructureTypeDef"]],
    },
)

ConfigureAgentResponseTypeDef = TypedDict(
    "ConfigureAgentResponseTypeDef", {"configuration": "AgentConfigurationTypeDef"}
)

CreateProfilingGroupResponseTypeDef = TypedDict(
    "CreateProfilingGroupResponseTypeDef", {"profilingGroup": "ProfilingGroupDescriptionTypeDef"}
)

DescribeProfilingGroupResponseTypeDef = TypedDict(
    "DescribeProfilingGroupResponseTypeDef", {"profilingGroup": "ProfilingGroupDescriptionTypeDef"}
)

_RequiredGetFindingsReportAccountSummaryResponseTypeDef = TypedDict(
    "_RequiredGetFindingsReportAccountSummaryResponseTypeDef",
    {"reportSummaries": List["FindingsReportSummaryTypeDef"]},
)
_OptionalGetFindingsReportAccountSummaryResponseTypeDef = TypedDict(
    "_OptionalGetFindingsReportAccountSummaryResponseTypeDef", {"nextToken": str}, total=False
)


class GetFindingsReportAccountSummaryResponseTypeDef(
    _RequiredGetFindingsReportAccountSummaryResponseTypeDef,
    _OptionalGetFindingsReportAccountSummaryResponseTypeDef,
):
    pass


GetNotificationConfigurationResponseTypeDef = TypedDict(
    "GetNotificationConfigurationResponseTypeDef",
    {"notificationConfiguration": "NotificationConfigurationTypeDef"},
)

GetPolicyResponseTypeDef = TypedDict("GetPolicyResponseTypeDef", {"policy": str, "revisionId": str})

_RequiredGetProfileResponseTypeDef = TypedDict(
    "_RequiredGetProfileResponseTypeDef", {"contentType": str, "profile": bytes}
)
_OptionalGetProfileResponseTypeDef = TypedDict(
    "_OptionalGetProfileResponseTypeDef", {"contentEncoding": str}, total=False
)


class GetProfileResponseTypeDef(
    _RequiredGetProfileResponseTypeDef, _OptionalGetProfileResponseTypeDef
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
    },
)

_RequiredListFindingsReportsResponseTypeDef = TypedDict(
    "_RequiredListFindingsReportsResponseTypeDef",
    {"findingsReportSummaries": List["FindingsReportSummaryTypeDef"]},
)
_OptionalListFindingsReportsResponseTypeDef = TypedDict(
    "_OptionalListFindingsReportsResponseTypeDef", {"nextToken": str}, total=False
)


class ListFindingsReportsResponseTypeDef(
    _RequiredListFindingsReportsResponseTypeDef, _OptionalListFindingsReportsResponseTypeDef
):
    pass


_RequiredListProfileTimesResponseTypeDef = TypedDict(
    "_RequiredListProfileTimesResponseTypeDef", {"profileTimes": List["ProfileTimeTypeDef"]}
)
_OptionalListProfileTimesResponseTypeDef = TypedDict(
    "_OptionalListProfileTimesResponseTypeDef", {"nextToken": str}, total=False
)


class ListProfileTimesResponseTypeDef(
    _RequiredListProfileTimesResponseTypeDef, _OptionalListProfileTimesResponseTypeDef
):
    pass


_RequiredListProfilingGroupsResponseTypeDef = TypedDict(
    "_RequiredListProfilingGroupsResponseTypeDef", {"profilingGroupNames": List[str]}
)
_OptionalListProfilingGroupsResponseTypeDef = TypedDict(
    "_OptionalListProfilingGroupsResponseTypeDef",
    {"nextToken": str, "profilingGroups": List["ProfilingGroupDescriptionTypeDef"]},
    total=False,
)


class ListProfilingGroupsResponseTypeDef(
    _RequiredListProfilingGroupsResponseTypeDef, _OptionalListProfilingGroupsResponseTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutPermissionResponseTypeDef = TypedDict(
    "PutPermissionResponseTypeDef", {"policy": str, "revisionId": str}
)

RemoveNotificationChannelResponseTypeDef = TypedDict(
    "RemoveNotificationChannelResponseTypeDef",
    {"notificationConfiguration": "NotificationConfigurationTypeDef"},
    total=False,
)

RemovePermissionResponseTypeDef = TypedDict(
    "RemovePermissionResponseTypeDef", {"policy": str, "revisionId": str}
)

UpdateProfilingGroupResponseTypeDef = TypedDict(
    "UpdateProfilingGroupResponseTypeDef", {"profilingGroup": "ProfilingGroupDescriptionTypeDef"}
)
