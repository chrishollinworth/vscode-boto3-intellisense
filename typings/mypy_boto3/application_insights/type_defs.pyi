"""
Type annotations for application-insights service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/type_defs.html)

Usage::

    ```python
    from mypy_boto3_application_insights.type_defs import ApplicationComponentTypeDef

    data: ApplicationComponentTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    CloudWatchEventSourceType,
    ConfigurationEventResourceTypeType,
    ConfigurationEventStatusType,
    FeedbackValueType,
    LogFilterType,
    OsTypeType,
    SeverityLevelType,
    StatusType,
    TierType,
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
    "ApplicationComponentTypeDef",
    "ApplicationInfoTypeDef",
    "ConfigurationEventTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateComponentRequestRequestTypeDef",
    "CreateLogPatternRequestRequestTypeDef",
    "CreateLogPatternResponseTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteComponentRequestRequestTypeDef",
    "DeleteLogPatternRequestRequestTypeDef",
    "DescribeApplicationRequestRequestTypeDef",
    "DescribeApplicationResponseTypeDef",
    "DescribeComponentConfigurationRecommendationRequestRequestTypeDef",
    "DescribeComponentConfigurationRecommendationResponseTypeDef",
    "DescribeComponentConfigurationRequestRequestTypeDef",
    "DescribeComponentConfigurationResponseTypeDef",
    "DescribeComponentRequestRequestTypeDef",
    "DescribeComponentResponseTypeDef",
    "DescribeLogPatternRequestRequestTypeDef",
    "DescribeLogPatternResponseTypeDef",
    "DescribeObservationRequestRequestTypeDef",
    "DescribeObservationResponseTypeDef",
    "DescribeProblemObservationsRequestRequestTypeDef",
    "DescribeProblemObservationsResponseTypeDef",
    "DescribeProblemRequestRequestTypeDef",
    "DescribeProblemResponseTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListComponentsRequestRequestTypeDef",
    "ListComponentsResponseTypeDef",
    "ListConfigurationHistoryRequestRequestTypeDef",
    "ListConfigurationHistoryResponseTypeDef",
    "ListLogPatternSetsRequestRequestTypeDef",
    "ListLogPatternSetsResponseTypeDef",
    "ListLogPatternsRequestRequestTypeDef",
    "ListLogPatternsResponseTypeDef",
    "ListProblemsRequestRequestTypeDef",
    "ListProblemsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogPatternTypeDef",
    "ObservationTypeDef",
    "ProblemTypeDef",
    "RelatedObservationsTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateApplicationResponseTypeDef",
    "UpdateComponentConfigurationRequestRequestTypeDef",
    "UpdateComponentRequestRequestTypeDef",
    "UpdateLogPatternRequestRequestTypeDef",
    "UpdateLogPatternResponseTypeDef",
)

ApplicationComponentTypeDef = TypedDict(
    "ApplicationComponentTypeDef",
    {
        "ComponentName": str,
        "ComponentRemarks": str,
        "ResourceType": str,
        "OsType": OsTypeType,
        "Tier": TierType,
        "Monitor": bool,
        "DetectedWorkload": Dict[TierType, Dict[str, str]],
    },
    total=False,
)

ApplicationInfoTypeDef = TypedDict(
    "ApplicationInfoTypeDef",
    {
        "ResourceGroupName": str,
        "LifeCycle": str,
        "OpsItemSNSTopicArn": str,
        "OpsCenterEnabled": bool,
        "CWEMonitorEnabled": bool,
        "Remarks": str,
    },
    total=False,
)

ConfigurationEventTypeDef = TypedDict(
    "ConfigurationEventTypeDef",
    {
        "MonitoredResourceARN": str,
        "EventStatus": ConfigurationEventStatusType,
        "EventResourceType": ConfigurationEventResourceTypeType,
        "EventTime": datetime,
        "EventDetail": str,
        "EventResourceName": str,
    },
    total=False,
)

_RequiredCreateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)
_OptionalCreateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestRequestTypeDef",
    {
        "OpsCenterEnabled": bool,
        "CWEMonitorEnabled": bool,
        "OpsItemSNSTopicArn": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateApplicationRequestRequestTypeDef(
    _RequiredCreateApplicationRequestRequestTypeDef, _OptionalCreateApplicationRequestRequestTypeDef
):
    pass

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "ApplicationInfo": "ApplicationInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateComponentRequestRequestTypeDef = TypedDict(
    "CreateComponentRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
        "ResourceList": List[str],
    },
)

CreateLogPatternRequestRequestTypeDef = TypedDict(
    "CreateLogPatternRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "PatternSetName": str,
        "PatternName": str,
        "Pattern": str,
        "Rank": int,
    },
)

CreateLogPatternResponseTypeDef = TypedDict(
    "CreateLogPatternResponseTypeDef",
    {
        "LogPattern": "LogPatternTypeDef",
        "ResourceGroupName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)

DeleteComponentRequestRequestTypeDef = TypedDict(
    "DeleteComponentRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
    },
)

DeleteLogPatternRequestRequestTypeDef = TypedDict(
    "DeleteLogPatternRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "PatternSetName": str,
        "PatternName": str,
    },
)

DescribeApplicationRequestRequestTypeDef = TypedDict(
    "DescribeApplicationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)

DescribeApplicationResponseTypeDef = TypedDict(
    "DescribeApplicationResponseTypeDef",
    {
        "ApplicationInfo": "ApplicationInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeComponentConfigurationRecommendationRequestRequestTypeDef = TypedDict(
    "DescribeComponentConfigurationRecommendationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
        "Tier": TierType,
    },
)

DescribeComponentConfigurationRecommendationResponseTypeDef = TypedDict(
    "DescribeComponentConfigurationRecommendationResponseTypeDef",
    {
        "ComponentConfiguration": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeComponentConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeComponentConfigurationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
    },
)

DescribeComponentConfigurationResponseTypeDef = TypedDict(
    "DescribeComponentConfigurationResponseTypeDef",
    {
        "Monitor": bool,
        "Tier": TierType,
        "ComponentConfiguration": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeComponentRequestRequestTypeDef = TypedDict(
    "DescribeComponentRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
    },
)

DescribeComponentResponseTypeDef = TypedDict(
    "DescribeComponentResponseTypeDef",
    {
        "ApplicationComponent": "ApplicationComponentTypeDef",
        "ResourceList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLogPatternRequestRequestTypeDef = TypedDict(
    "DescribeLogPatternRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "PatternSetName": str,
        "PatternName": str,
    },
)

DescribeLogPatternResponseTypeDef = TypedDict(
    "DescribeLogPatternResponseTypeDef",
    {
        "ResourceGroupName": str,
        "LogPattern": "LogPatternTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeObservationRequestRequestTypeDef = TypedDict(
    "DescribeObservationRequestRequestTypeDef",
    {
        "ObservationId": str,
    },
)

DescribeObservationResponseTypeDef = TypedDict(
    "DescribeObservationResponseTypeDef",
    {
        "Observation": "ObservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProblemObservationsRequestRequestTypeDef = TypedDict(
    "DescribeProblemObservationsRequestRequestTypeDef",
    {
        "ProblemId": str,
    },
)

DescribeProblemObservationsResponseTypeDef = TypedDict(
    "DescribeProblemObservationsResponseTypeDef",
    {
        "RelatedObservations": "RelatedObservationsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProblemRequestRequestTypeDef = TypedDict(
    "DescribeProblemRequestRequestTypeDef",
    {
        "ProblemId": str,
    },
)

DescribeProblemResponseTypeDef = TypedDict(
    "DescribeProblemResponseTypeDef",
    {
        "Problem": "ProblemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "ApplicationInfoList": List["ApplicationInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListComponentsRequestRequestTypeDef = TypedDict(
    "_RequiredListComponentsRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)
_OptionalListComponentsRequestRequestTypeDef = TypedDict(
    "_OptionalListComponentsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListComponentsRequestRequestTypeDef(
    _RequiredListComponentsRequestRequestTypeDef, _OptionalListComponentsRequestRequestTypeDef
):
    pass

ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {
        "ApplicationComponentList": List["ApplicationComponentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConfigurationHistoryRequestRequestTypeDef = TypedDict(
    "ListConfigurationHistoryRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "EventStatus": ConfigurationEventStatusType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListConfigurationHistoryResponseTypeDef = TypedDict(
    "ListConfigurationHistoryResponseTypeDef",
    {
        "EventList": List["ConfigurationEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLogPatternSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListLogPatternSetsRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)
_OptionalListLogPatternSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListLogPatternSetsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListLogPatternSetsRequestRequestTypeDef(
    _RequiredListLogPatternSetsRequestRequestTypeDef,
    _OptionalListLogPatternSetsRequestRequestTypeDef,
):
    pass

ListLogPatternSetsResponseTypeDef = TypedDict(
    "ListLogPatternSetsResponseTypeDef",
    {
        "ResourceGroupName": str,
        "LogPatternSets": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLogPatternsRequestRequestTypeDef = TypedDict(
    "_RequiredListLogPatternsRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)
_OptionalListLogPatternsRequestRequestTypeDef = TypedDict(
    "_OptionalListLogPatternsRequestRequestTypeDef",
    {
        "PatternSetName": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListLogPatternsRequestRequestTypeDef(
    _RequiredListLogPatternsRequestRequestTypeDef, _OptionalListLogPatternsRequestRequestTypeDef
):
    pass

ListLogPatternsResponseTypeDef = TypedDict(
    "ListLogPatternsResponseTypeDef",
    {
        "ResourceGroupName": str,
        "LogPatterns": List["LogPatternTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProblemsRequestRequestTypeDef = TypedDict(
    "ListProblemsRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListProblemsResponseTypeDef = TypedDict(
    "ListProblemsResponseTypeDef",
    {
        "ProblemList": List["ProblemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogPatternTypeDef = TypedDict(
    "LogPatternTypeDef",
    {
        "PatternSetName": str,
        "PatternName": str,
        "Pattern": str,
        "Rank": int,
    },
    total=False,
)

ObservationTypeDef = TypedDict(
    "ObservationTypeDef",
    {
        "Id": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "SourceType": str,
        "SourceARN": str,
        "LogGroup": str,
        "LineTime": datetime,
        "LogText": str,
        "LogFilter": LogFilterType,
        "MetricNamespace": str,
        "MetricName": str,
        "Unit": str,
        "Value": float,
        "CloudWatchEventId": str,
        "CloudWatchEventSource": CloudWatchEventSourceType,
        "CloudWatchEventDetailType": str,
        "HealthEventArn": str,
        "HealthService": str,
        "HealthEventTypeCode": str,
        "HealthEventTypeCategory": str,
        "HealthEventDescription": str,
        "CodeDeployDeploymentId": str,
        "CodeDeployDeploymentGroup": str,
        "CodeDeployState": str,
        "CodeDeployApplication": str,
        "CodeDeployInstanceGroupId": str,
        "Ec2State": str,
        "RdsEventCategories": str,
        "RdsEventMessage": str,
        "S3EventName": str,
        "StatesExecutionArn": str,
        "StatesArn": str,
        "StatesStatus": str,
        "StatesInput": str,
        "EbsEvent": str,
        "EbsResult": str,
        "EbsCause": str,
        "EbsRequestId": str,
        "XRayFaultPercent": int,
        "XRayThrottlePercent": int,
        "XRayErrorPercent": int,
        "XRayRequestCount": int,
        "XRayRequestAverageLatency": int,
        "XRayNodeName": str,
        "XRayNodeType": str,
    },
    total=False,
)

ProblemTypeDef = TypedDict(
    "ProblemTypeDef",
    {
        "Id": str,
        "Title": str,
        "Insights": str,
        "Status": StatusType,
        "AffectedResource": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "SeverityLevel": SeverityLevelType,
        "ResourceGroupName": str,
        "Feedback": Dict[Literal["INSIGHTS_FEEDBACK"], FeedbackValueType],
    },
    total=False,
)

RelatedObservationsTypeDef = TypedDict(
    "RelatedObservationsTypeDef",
    {
        "ObservationList": List["ObservationTypeDef"],
    },
    total=False,
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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)
_OptionalUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationRequestRequestTypeDef",
    {
        "OpsCenterEnabled": bool,
        "CWEMonitorEnabled": bool,
        "OpsItemSNSTopicArn": str,
        "RemoveSNSTopic": bool,
    },
    total=False,
)

class UpdateApplicationRequestRequestTypeDef(
    _RequiredUpdateApplicationRequestRequestTypeDef, _OptionalUpdateApplicationRequestRequestTypeDef
):
    pass

UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef",
    {
        "ApplicationInfo": "ApplicationInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateComponentConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateComponentConfigurationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
    },
)
_OptionalUpdateComponentConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateComponentConfigurationRequestRequestTypeDef",
    {
        "Monitor": bool,
        "Tier": TierType,
        "ComponentConfiguration": str,
    },
    total=False,
)

class UpdateComponentConfigurationRequestRequestTypeDef(
    _RequiredUpdateComponentConfigurationRequestRequestTypeDef,
    _OptionalUpdateComponentConfigurationRequestRequestTypeDef,
):
    pass

_RequiredUpdateComponentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateComponentRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
    },
)
_OptionalUpdateComponentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateComponentRequestRequestTypeDef",
    {
        "NewComponentName": str,
        "ResourceList": List[str],
    },
    total=False,
)

class UpdateComponentRequestRequestTypeDef(
    _RequiredUpdateComponentRequestRequestTypeDef, _OptionalUpdateComponentRequestRequestTypeDef
):
    pass

_RequiredUpdateLogPatternRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLogPatternRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "PatternSetName": str,
        "PatternName": str,
    },
)
_OptionalUpdateLogPatternRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLogPatternRequestRequestTypeDef",
    {
        "Pattern": str,
        "Rank": int,
    },
    total=False,
)

class UpdateLogPatternRequestRequestTypeDef(
    _RequiredUpdateLogPatternRequestRequestTypeDef, _OptionalUpdateLogPatternRequestRequestTypeDef
):
    pass

UpdateLogPatternResponseTypeDef = TypedDict(
    "UpdateLogPatternResponseTypeDef",
    {
        "ResourceGroupName": str,
        "LogPattern": "LogPatternTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
