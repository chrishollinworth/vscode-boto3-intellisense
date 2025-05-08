"""
Type annotations for application-insights service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_application_insights.type_defs import WorkloadConfigurationTypeDef

    data: WorkloadConfigurationTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    CloudWatchEventSourceType,
    ConfigurationEventResourceTypeType,
    ConfigurationEventStatusType,
    DiscoveryTypeType,
    FeedbackValueType,
    LogFilterType,
    OsTypeType,
    RecommendationTypeType,
    ResolutionMethodType,
    SeverityLevelType,
    StatusType,
    TierType,
    VisibilityType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AddWorkloadRequestTypeDef",
    "AddWorkloadResponseTypeDef",
    "ApplicationComponentTypeDef",
    "ApplicationInfoTypeDef",
    "ConfigurationEventTypeDef",
    "CreateApplicationRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateComponentRequestTypeDef",
    "CreateLogPatternRequestTypeDef",
    "CreateLogPatternResponseTypeDef",
    "DeleteApplicationRequestTypeDef",
    "DeleteComponentRequestTypeDef",
    "DeleteLogPatternRequestTypeDef",
    "DescribeApplicationRequestTypeDef",
    "DescribeApplicationResponseTypeDef",
    "DescribeComponentConfigurationRecommendationRequestTypeDef",
    "DescribeComponentConfigurationRecommendationResponseTypeDef",
    "DescribeComponentConfigurationRequestTypeDef",
    "DescribeComponentConfigurationResponseTypeDef",
    "DescribeComponentRequestTypeDef",
    "DescribeComponentResponseTypeDef",
    "DescribeLogPatternRequestTypeDef",
    "DescribeLogPatternResponseTypeDef",
    "DescribeObservationRequestTypeDef",
    "DescribeObservationResponseTypeDef",
    "DescribeProblemObservationsRequestTypeDef",
    "DescribeProblemObservationsResponseTypeDef",
    "DescribeProblemRequestTypeDef",
    "DescribeProblemResponseTypeDef",
    "DescribeWorkloadRequestTypeDef",
    "DescribeWorkloadResponseTypeDef",
    "ListApplicationsRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListComponentsRequestTypeDef",
    "ListComponentsResponseTypeDef",
    "ListConfigurationHistoryRequestTypeDef",
    "ListConfigurationHistoryResponseTypeDef",
    "ListLogPatternSetsRequestTypeDef",
    "ListLogPatternSetsResponseTypeDef",
    "ListLogPatternsRequestTypeDef",
    "ListLogPatternsResponseTypeDef",
    "ListProblemsRequestTypeDef",
    "ListProblemsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorkloadsRequestTypeDef",
    "ListWorkloadsResponseTypeDef",
    "LogPatternTypeDef",
    "ObservationTypeDef",
    "ProblemTypeDef",
    "RelatedObservationsTypeDef",
    "RemoveWorkloadRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateApplicationRequestTypeDef",
    "UpdateApplicationResponseTypeDef",
    "UpdateComponentConfigurationRequestTypeDef",
    "UpdateComponentRequestTypeDef",
    "UpdateLogPatternRequestTypeDef",
    "UpdateLogPatternResponseTypeDef",
    "UpdateProblemRequestTypeDef",
    "UpdateWorkloadRequestTypeDef",
    "UpdateWorkloadResponseTypeDef",
    "WorkloadConfigurationTypeDef",
    "WorkloadTypeDef",
)

class WorkloadConfigurationTypeDef(TypedDict):
    WorkloadName: NotRequired[str]
    Tier: NotRequired[TierType]
    Configuration: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ApplicationComponentTypeDef(TypedDict):
    ComponentName: NotRequired[str]
    ComponentRemarks: NotRequired[str]
    ResourceType: NotRequired[str]
    OsType: NotRequired[OsTypeType]
    Tier: NotRequired[TierType]
    Monitor: NotRequired[bool]
    DetectedWorkload: NotRequired[Dict[TierType, Dict[str, str]]]

class ApplicationInfoTypeDef(TypedDict):
    AccountId: NotRequired[str]
    ResourceGroupName: NotRequired[str]
    LifeCycle: NotRequired[str]
    OpsItemSNSTopicArn: NotRequired[str]
    SNSNotificationArn: NotRequired[str]
    OpsCenterEnabled: NotRequired[bool]
    CWEMonitorEnabled: NotRequired[bool]
    Remarks: NotRequired[str]
    AutoConfigEnabled: NotRequired[bool]
    DiscoveryType: NotRequired[DiscoveryTypeType]
    AttachMissingPermission: NotRequired[bool]

class ConfigurationEventTypeDef(TypedDict):
    ResourceGroupName: NotRequired[str]
    AccountId: NotRequired[str]
    MonitoredResourceARN: NotRequired[str]
    EventStatus: NotRequired[ConfigurationEventStatusType]
    EventResourceType: NotRequired[ConfigurationEventResourceTypeType]
    EventTime: NotRequired[datetime]
    EventDetail: NotRequired[str]
    EventResourceName: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class CreateComponentRequestTypeDef(TypedDict):
    ResourceGroupName: str
    ComponentName: str
    ResourceList: Sequence[str]

CreateLogPatternRequestTypeDef = TypedDict(
    "CreateLogPatternRequestTypeDef",
    {
        "ResourceGroupName": str,
        "PatternSetName": str,
        "PatternName": str,
        "Pattern": str,
        "Rank": int,
    },
)
LogPatternTypeDef = TypedDict(
    "LogPatternTypeDef",
    {
        "PatternSetName": NotRequired[str],
        "PatternName": NotRequired[str],
        "Pattern": NotRequired[str],
        "Rank": NotRequired[int],
    },
)

class DeleteApplicationRequestTypeDef(TypedDict):
    ResourceGroupName: str

class DeleteComponentRequestTypeDef(TypedDict):
    ResourceGroupName: str
    ComponentName: str

class DeleteLogPatternRequestTypeDef(TypedDict):
    ResourceGroupName: str
    PatternSetName: str
    PatternName: str

class DescribeApplicationRequestTypeDef(TypedDict):
    ResourceGroupName: str
    AccountId: NotRequired[str]

class DescribeComponentConfigurationRecommendationRequestTypeDef(TypedDict):
    ResourceGroupName: str
    ComponentName: str
    Tier: TierType
    WorkloadName: NotRequired[str]
    RecommendationType: NotRequired[RecommendationTypeType]

class DescribeComponentConfigurationRequestTypeDef(TypedDict):
    ResourceGroupName: str
    ComponentName: str
    AccountId: NotRequired[str]

class DescribeComponentRequestTypeDef(TypedDict):
    ResourceGroupName: str
    ComponentName: str
    AccountId: NotRequired[str]

class DescribeLogPatternRequestTypeDef(TypedDict):
    ResourceGroupName: str
    PatternSetName: str
    PatternName: str
    AccountId: NotRequired[str]

class DescribeObservationRequestTypeDef(TypedDict):
    ObservationId: str
    AccountId: NotRequired[str]

class ObservationTypeDef(TypedDict):
    Id: NotRequired[str]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    SourceType: NotRequired[str]
    SourceARN: NotRequired[str]
    LogGroup: NotRequired[str]
    LineTime: NotRequired[datetime]
    LogText: NotRequired[str]
    LogFilter: NotRequired[LogFilterType]
    MetricNamespace: NotRequired[str]
    MetricName: NotRequired[str]
    Unit: NotRequired[str]
    Value: NotRequired[float]
    CloudWatchEventId: NotRequired[str]
    CloudWatchEventSource: NotRequired[CloudWatchEventSourceType]
    CloudWatchEventDetailType: NotRequired[str]
    HealthEventArn: NotRequired[str]
    HealthService: NotRequired[str]
    HealthEventTypeCode: NotRequired[str]
    HealthEventTypeCategory: NotRequired[str]
    HealthEventDescription: NotRequired[str]
    CodeDeployDeploymentId: NotRequired[str]
    CodeDeployDeploymentGroup: NotRequired[str]
    CodeDeployState: NotRequired[str]
    CodeDeployApplication: NotRequired[str]
    CodeDeployInstanceGroupId: NotRequired[str]
    Ec2State: NotRequired[str]
    RdsEventCategories: NotRequired[str]
    RdsEventMessage: NotRequired[str]
    S3EventName: NotRequired[str]
    StatesExecutionArn: NotRequired[str]
    StatesArn: NotRequired[str]
    StatesStatus: NotRequired[str]
    StatesInput: NotRequired[str]
    EbsEvent: NotRequired[str]
    EbsResult: NotRequired[str]
    EbsCause: NotRequired[str]
    EbsRequestId: NotRequired[str]
    XRayFaultPercent: NotRequired[int]
    XRayThrottlePercent: NotRequired[int]
    XRayErrorPercent: NotRequired[int]
    XRayRequestCount: NotRequired[int]
    XRayRequestAverageLatency: NotRequired[int]
    XRayNodeName: NotRequired[str]
    XRayNodeType: NotRequired[str]

class DescribeProblemObservationsRequestTypeDef(TypedDict):
    ProblemId: str
    AccountId: NotRequired[str]

class DescribeProblemRequestTypeDef(TypedDict):
    ProblemId: str
    AccountId: NotRequired[str]

class ProblemTypeDef(TypedDict):
    Id: NotRequired[str]
    Title: NotRequired[str]
    ShortName: NotRequired[str]
    Insights: NotRequired[str]
    Status: NotRequired[StatusType]
    AffectedResource: NotRequired[str]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    SeverityLevel: NotRequired[SeverityLevelType]
    AccountId: NotRequired[str]
    ResourceGroupName: NotRequired[str]
    Feedback: NotRequired[Dict[Literal["INSIGHTS_FEEDBACK"], FeedbackValueType]]
    RecurringCount: NotRequired[int]
    LastRecurrenceTime: NotRequired[datetime]
    Visibility: NotRequired[VisibilityType]
    ResolutionMethod: NotRequired[ResolutionMethodType]

class DescribeWorkloadRequestTypeDef(TypedDict):
    ResourceGroupName: str
    ComponentName: str
    WorkloadId: str
    AccountId: NotRequired[str]

class ListApplicationsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    AccountId: NotRequired[str]

class ListComponentsRequestTypeDef(TypedDict):
    ResourceGroupName: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    AccountId: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class ListLogPatternSetsRequestTypeDef(TypedDict):
    ResourceGroupName: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    AccountId: NotRequired[str]

class ListLogPatternsRequestTypeDef(TypedDict):
    ResourceGroupName: str
    PatternSetName: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    AccountId: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class ListWorkloadsRequestTypeDef(TypedDict):
    ResourceGroupName: str
    ComponentName: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    AccountId: NotRequired[str]

class WorkloadTypeDef(TypedDict):
    WorkloadId: NotRequired[str]
    ComponentName: NotRequired[str]
    WorkloadName: NotRequired[str]
    Tier: NotRequired[TierType]
    WorkloadRemarks: NotRequired[str]
    MissingWorkloadConfig: NotRequired[bool]

class RemoveWorkloadRequestTypeDef(TypedDict):
    ResourceGroupName: str
    ComponentName: str
    WorkloadId: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateApplicationRequestTypeDef(TypedDict):
    ResourceGroupName: str
    OpsCenterEnabled: NotRequired[bool]
    CWEMonitorEnabled: NotRequired[bool]
    OpsItemSNSTopicArn: NotRequired[str]
    SNSNotificationArn: NotRequired[str]
    RemoveSNSTopic: NotRequired[bool]
    AutoConfigEnabled: NotRequired[bool]
    AttachMissingPermission: NotRequired[bool]

class UpdateComponentConfigurationRequestTypeDef(TypedDict):
    ResourceGroupName: str
    ComponentName: str
    Monitor: NotRequired[bool]
    Tier: NotRequired[TierType]
    ComponentConfiguration: NotRequired[str]
    AutoConfigEnabled: NotRequired[bool]

class UpdateComponentRequestTypeDef(TypedDict):
    ResourceGroupName: str
    ComponentName: str
    NewComponentName: NotRequired[str]
    ResourceList: NotRequired[Sequence[str]]

UpdateLogPatternRequestTypeDef = TypedDict(
    "UpdateLogPatternRequestTypeDef",
    {
        "ResourceGroupName": str,
        "PatternSetName": str,
        "PatternName": str,
        "Pattern": NotRequired[str],
        "Rank": NotRequired[int],
    },
)

class UpdateProblemRequestTypeDef(TypedDict):
    ProblemId: str
    UpdateStatus: NotRequired[Literal["RESOLVED"]]
    Visibility: NotRequired[VisibilityType]

class AddWorkloadRequestTypeDef(TypedDict):
    ResourceGroupName: str
    ComponentName: str
    WorkloadConfiguration: WorkloadConfigurationTypeDef

class UpdateWorkloadRequestTypeDef(TypedDict):
    ResourceGroupName: str
    ComponentName: str
    WorkloadConfiguration: WorkloadConfigurationTypeDef
    WorkloadId: NotRequired[str]

class AddWorkloadResponseTypeDef(TypedDict):
    WorkloadId: str
    WorkloadConfiguration: WorkloadConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeComponentConfigurationRecommendationResponseTypeDef(TypedDict):
    ComponentConfiguration: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeComponentConfigurationResponseTypeDef(TypedDict):
    Monitor: bool
    Tier: TierType
    ComponentConfiguration: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkloadResponseTypeDef(TypedDict):
    WorkloadId: str
    WorkloadRemarks: str
    WorkloadConfiguration: WorkloadConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLogPatternSetsResponseTypeDef(TypedDict):
    ResourceGroupName: str
    AccountId: str
    LogPatternSets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateWorkloadResponseTypeDef(TypedDict):
    WorkloadId: str
    WorkloadConfiguration: WorkloadConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeComponentResponseTypeDef(TypedDict):
    ApplicationComponent: ApplicationComponentTypeDef
    ResourceList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListComponentsResponseTypeDef(TypedDict):
    ApplicationComponentList: List[ApplicationComponentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateApplicationResponseTypeDef(TypedDict):
    ApplicationInfo: ApplicationInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationResponseTypeDef(TypedDict):
    ApplicationInfo: ApplicationInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsResponseTypeDef(TypedDict):
    ApplicationInfoList: List[ApplicationInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateApplicationResponseTypeDef(TypedDict):
    ApplicationInfo: ApplicationInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigurationHistoryResponseTypeDef(TypedDict):
    EventList: List[ConfigurationEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateApplicationRequestTypeDef(TypedDict):
    ResourceGroupName: NotRequired[str]
    OpsCenterEnabled: NotRequired[bool]
    CWEMonitorEnabled: NotRequired[bool]
    OpsItemSNSTopicArn: NotRequired[str]
    SNSNotificationArn: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    AutoConfigEnabled: NotRequired[bool]
    AutoCreate: NotRequired[bool]
    GroupingType: NotRequired[Literal["ACCOUNT_BASED"]]
    AttachMissingPermission: NotRequired[bool]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateLogPatternResponseTypeDef(TypedDict):
    LogPattern: LogPatternTypeDef
    ResourceGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLogPatternResponseTypeDef(TypedDict):
    ResourceGroupName: str
    AccountId: str
    LogPattern: LogPatternTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLogPatternsResponseTypeDef(TypedDict):
    ResourceGroupName: str
    AccountId: str
    LogPatterns: List[LogPatternTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateLogPatternResponseTypeDef(TypedDict):
    ResourceGroupName: str
    LogPattern: LogPatternTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeObservationResponseTypeDef(TypedDict):
    Observation: ObservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RelatedObservationsTypeDef(TypedDict):
    ObservationList: NotRequired[List[ObservationTypeDef]]

class DescribeProblemResponseTypeDef(TypedDict):
    Problem: ProblemTypeDef
    SNSNotificationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProblemsResponseTypeDef(TypedDict):
    ProblemList: List[ProblemTypeDef]
    ResourceGroupName: str
    AccountId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListConfigurationHistoryRequestTypeDef(TypedDict):
    ResourceGroupName: NotRequired[str]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    EventStatus: NotRequired[ConfigurationEventStatusType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    AccountId: NotRequired[str]

class ListProblemsRequestTypeDef(TypedDict):
    AccountId: NotRequired[str]
    ResourceGroupName: NotRequired[str]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    ComponentName: NotRequired[str]
    Visibility: NotRequired[VisibilityType]

class ListWorkloadsResponseTypeDef(TypedDict):
    WorkloadList: List[WorkloadTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeProblemObservationsResponseTypeDef(TypedDict):
    RelatedObservations: RelatedObservationsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
