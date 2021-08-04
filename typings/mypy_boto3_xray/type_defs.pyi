"""
Type annotations for xray service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/type_defs.html)

Usage::

    ```python
    from mypy_boto3_xray.type_defs import AliasTypeDef

    data: AliasTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    EncryptionStatusType,
    EncryptionTypeType,
    InsightStateType,
    SamplingStrategyNameType,
    TimeRangeTypeType,
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
    "AliasTypeDef",
    "AnnotationValueTypeDef",
    "AnomalousServiceTypeDef",
    "AvailabilityZoneDetailTypeDef",
    "BackendConnectionErrorsTypeDef",
    "BatchGetTracesRequestRequestTypeDef",
    "BatchGetTracesResultTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "CreateGroupResultTypeDef",
    "CreateSamplingRuleRequestRequestTypeDef",
    "CreateSamplingRuleResultTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteSamplingRuleRequestRequestTypeDef",
    "DeleteSamplingRuleResultTypeDef",
    "EdgeStatisticsTypeDef",
    "EdgeTypeDef",
    "EncryptionConfigTypeDef",
    "ErrorRootCauseEntityTypeDef",
    "ErrorRootCauseServiceTypeDef",
    "ErrorRootCauseTypeDef",
    "ErrorStatisticsTypeDef",
    "FaultRootCauseEntityTypeDef",
    "FaultRootCauseServiceTypeDef",
    "FaultRootCauseTypeDef",
    "FaultStatisticsTypeDef",
    "ForecastStatisticsTypeDef",
    "GetEncryptionConfigResultTypeDef",
    "GetGroupRequestRequestTypeDef",
    "GetGroupResultTypeDef",
    "GetGroupsRequestRequestTypeDef",
    "GetGroupsResultTypeDef",
    "GetInsightEventsRequestRequestTypeDef",
    "GetInsightEventsResultTypeDef",
    "GetInsightImpactGraphRequestRequestTypeDef",
    "GetInsightImpactGraphResultTypeDef",
    "GetInsightRequestRequestTypeDef",
    "GetInsightResultTypeDef",
    "GetInsightSummariesRequestRequestTypeDef",
    "GetInsightSummariesResultTypeDef",
    "GetSamplingRulesRequestRequestTypeDef",
    "GetSamplingRulesResultTypeDef",
    "GetSamplingStatisticSummariesRequestRequestTypeDef",
    "GetSamplingStatisticSummariesResultTypeDef",
    "GetSamplingTargetsRequestRequestTypeDef",
    "GetSamplingTargetsResultTypeDef",
    "GetServiceGraphRequestRequestTypeDef",
    "GetServiceGraphResultTypeDef",
    "GetTimeSeriesServiceStatisticsRequestRequestTypeDef",
    "GetTimeSeriesServiceStatisticsResultTypeDef",
    "GetTraceGraphRequestRequestTypeDef",
    "GetTraceGraphResultTypeDef",
    "GetTraceSummariesRequestRequestTypeDef",
    "GetTraceSummariesResultTypeDef",
    "GroupSummaryTypeDef",
    "GroupTypeDef",
    "HistogramEntryTypeDef",
    "HttpTypeDef",
    "InsightEventTypeDef",
    "InsightImpactGraphEdgeTypeDef",
    "InsightImpactGraphServiceTypeDef",
    "InsightSummaryTypeDef",
    "InsightTypeDef",
    "InsightsConfigurationTypeDef",
    "InstanceIdDetailTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutEncryptionConfigRequestRequestTypeDef",
    "PutEncryptionConfigResultTypeDef",
    "PutTelemetryRecordsRequestRequestTypeDef",
    "PutTraceSegmentsRequestRequestTypeDef",
    "PutTraceSegmentsResultTypeDef",
    "RequestImpactStatisticsTypeDef",
    "ResourceARNDetailTypeDef",
    "ResponseMetadataTypeDef",
    "ResponseTimeRootCauseEntityTypeDef",
    "ResponseTimeRootCauseServiceTypeDef",
    "ResponseTimeRootCauseTypeDef",
    "RootCauseExceptionTypeDef",
    "SamplingRuleRecordTypeDef",
    "SamplingRuleTypeDef",
    "SamplingRuleUpdateTypeDef",
    "SamplingStatisticSummaryTypeDef",
    "SamplingStatisticsDocumentTypeDef",
    "SamplingStrategyTypeDef",
    "SamplingTargetDocumentTypeDef",
    "SegmentTypeDef",
    "ServiceIdTypeDef",
    "ServiceStatisticsTypeDef",
    "ServiceTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TelemetryRecordTypeDef",
    "TimeSeriesServiceStatisticsTypeDef",
    "TraceSummaryTypeDef",
    "TraceTypeDef",
    "TraceUserTypeDef",
    "UnprocessedStatisticsTypeDef",
    "UnprocessedTraceSegmentTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateGroupResultTypeDef",
    "UpdateSamplingRuleRequestRequestTypeDef",
    "UpdateSamplingRuleResultTypeDef",
    "ValueWithServiceIdsTypeDef",
)

AliasTypeDef = TypedDict(
    "AliasTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
    },
    total=False,
)

AnnotationValueTypeDef = TypedDict(
    "AnnotationValueTypeDef",
    {
        "NumberValue": float,
        "BooleanValue": bool,
        "StringValue": str,
    },
    total=False,
)

AnomalousServiceTypeDef = TypedDict(
    "AnomalousServiceTypeDef",
    {
        "ServiceId": "ServiceIdTypeDef",
    },
    total=False,
)

AvailabilityZoneDetailTypeDef = TypedDict(
    "AvailabilityZoneDetailTypeDef",
    {
        "Name": str,
    },
    total=False,
)

BackendConnectionErrorsTypeDef = TypedDict(
    "BackendConnectionErrorsTypeDef",
    {
        "TimeoutCount": int,
        "ConnectionRefusedCount": int,
        "HTTPCode4XXCount": int,
        "HTTPCode5XXCount": int,
        "UnknownHostCount": int,
        "OtherCount": int,
    },
    total=False,
)

_RequiredBatchGetTracesRequestRequestTypeDef = TypedDict(
    "_RequiredBatchGetTracesRequestRequestTypeDef",
    {
        "TraceIds": List[str],
    },
)
_OptionalBatchGetTracesRequestRequestTypeDef = TypedDict(
    "_OptionalBatchGetTracesRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class BatchGetTracesRequestRequestTypeDef(
    _RequiredBatchGetTracesRequestRequestTypeDef, _OptionalBatchGetTracesRequestRequestTypeDef
):
    pass

BatchGetTracesResultTypeDef = TypedDict(
    "BatchGetTracesResultTypeDef",
    {
        "Traces": List["TraceTypeDef"],
        "UnprocessedTraceIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
    },
)
_OptionalCreateGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGroupRequestRequestTypeDef",
    {
        "FilterExpression": str,
        "InsightsConfiguration": "InsightsConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateGroupRequestRequestTypeDef(
    _RequiredCreateGroupRequestRequestTypeDef, _OptionalCreateGroupRequestRequestTypeDef
):
    pass

CreateGroupResultTypeDef = TypedDict(
    "CreateGroupResultTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSamplingRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSamplingRuleRequestRequestTypeDef",
    {
        "SamplingRule": "SamplingRuleTypeDef",
    },
)
_OptionalCreateSamplingRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSamplingRuleRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateSamplingRuleRequestRequestTypeDef(
    _RequiredCreateSamplingRuleRequestRequestTypeDef,
    _OptionalCreateSamplingRuleRequestRequestTypeDef,
):
    pass

CreateSamplingRuleResultTypeDef = TypedDict(
    "CreateSamplingRuleResultTypeDef",
    {
        "SamplingRuleRecord": "SamplingRuleRecordTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "GroupARN": str,
    },
    total=False,
)

DeleteSamplingRuleRequestRequestTypeDef = TypedDict(
    "DeleteSamplingRuleRequestRequestTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
    },
    total=False,
)

DeleteSamplingRuleResultTypeDef = TypedDict(
    "DeleteSamplingRuleResultTypeDef",
    {
        "SamplingRuleRecord": "SamplingRuleRecordTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EdgeStatisticsTypeDef = TypedDict(
    "EdgeStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": "ErrorStatisticsTypeDef",
        "FaultStatistics": "FaultStatisticsTypeDef",
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

EdgeTypeDef = TypedDict(
    "EdgeTypeDef",
    {
        "ReferenceId": int,
        "StartTime": datetime,
        "EndTime": datetime,
        "SummaryStatistics": "EdgeStatisticsTypeDef",
        "ResponseTimeHistogram": List["HistogramEntryTypeDef"],
        "Aliases": List["AliasTypeDef"],
    },
    total=False,
)

EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "KeyId": str,
        "Status": EncryptionStatusType,
        "Type": EncryptionTypeType,
    },
    total=False,
)

ErrorRootCauseEntityTypeDef = TypedDict(
    "ErrorRootCauseEntityTypeDef",
    {
        "Name": str,
        "Exceptions": List["RootCauseExceptionTypeDef"],
        "Remote": bool,
    },
    total=False,
)

ErrorRootCauseServiceTypeDef = TypedDict(
    "ErrorRootCauseServiceTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List["ErrorRootCauseEntityTypeDef"],
        "Inferred": bool,
    },
    total=False,
)

ErrorRootCauseTypeDef = TypedDict(
    "ErrorRootCauseTypeDef",
    {
        "Services": List["ErrorRootCauseServiceTypeDef"],
        "ClientImpacting": bool,
    },
    total=False,
)

ErrorStatisticsTypeDef = TypedDict(
    "ErrorStatisticsTypeDef",
    {
        "ThrottleCount": int,
        "OtherCount": int,
        "TotalCount": int,
    },
    total=False,
)

FaultRootCauseEntityTypeDef = TypedDict(
    "FaultRootCauseEntityTypeDef",
    {
        "Name": str,
        "Exceptions": List["RootCauseExceptionTypeDef"],
        "Remote": bool,
    },
    total=False,
)

FaultRootCauseServiceTypeDef = TypedDict(
    "FaultRootCauseServiceTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List["FaultRootCauseEntityTypeDef"],
        "Inferred": bool,
    },
    total=False,
)

FaultRootCauseTypeDef = TypedDict(
    "FaultRootCauseTypeDef",
    {
        "Services": List["FaultRootCauseServiceTypeDef"],
        "ClientImpacting": bool,
    },
    total=False,
)

FaultStatisticsTypeDef = TypedDict(
    "FaultStatisticsTypeDef",
    {
        "OtherCount": int,
        "TotalCount": int,
    },
    total=False,
)

ForecastStatisticsTypeDef = TypedDict(
    "ForecastStatisticsTypeDef",
    {
        "FaultCountHigh": int,
        "FaultCountLow": int,
    },
    total=False,
)

GetEncryptionConfigResultTypeDef = TypedDict(
    "GetEncryptionConfigResultTypeDef",
    {
        "EncryptionConfig": "EncryptionConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupRequestRequestTypeDef = TypedDict(
    "GetGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "GroupARN": str,
    },
    total=False,
)

GetGroupResultTypeDef = TypedDict(
    "GetGroupResultTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupsRequestRequestTypeDef = TypedDict(
    "GetGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

GetGroupsResultTypeDef = TypedDict(
    "GetGroupsResultTypeDef",
    {
        "Groups": List["GroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetInsightEventsRequestRequestTypeDef = TypedDict(
    "_RequiredGetInsightEventsRequestRequestTypeDef",
    {
        "InsightId": str,
    },
)
_OptionalGetInsightEventsRequestRequestTypeDef = TypedDict(
    "_OptionalGetInsightEventsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetInsightEventsRequestRequestTypeDef(
    _RequiredGetInsightEventsRequestRequestTypeDef, _OptionalGetInsightEventsRequestRequestTypeDef
):
    pass

GetInsightEventsResultTypeDef = TypedDict(
    "GetInsightEventsResultTypeDef",
    {
        "InsightEvents": List["InsightEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetInsightImpactGraphRequestRequestTypeDef = TypedDict(
    "_RequiredGetInsightImpactGraphRequestRequestTypeDef",
    {
        "InsightId": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)
_OptionalGetInsightImpactGraphRequestRequestTypeDef = TypedDict(
    "_OptionalGetInsightImpactGraphRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class GetInsightImpactGraphRequestRequestTypeDef(
    _RequiredGetInsightImpactGraphRequestRequestTypeDef,
    _OptionalGetInsightImpactGraphRequestRequestTypeDef,
):
    pass

GetInsightImpactGraphResultTypeDef = TypedDict(
    "GetInsightImpactGraphResultTypeDef",
    {
        "InsightId": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "ServiceGraphStartTime": datetime,
        "ServiceGraphEndTime": datetime,
        "Services": List["InsightImpactGraphServiceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInsightRequestRequestTypeDef = TypedDict(
    "GetInsightRequestRequestTypeDef",
    {
        "InsightId": str,
    },
)

GetInsightResultTypeDef = TypedDict(
    "GetInsightResultTypeDef",
    {
        "Insight": "InsightTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetInsightSummariesRequestRequestTypeDef = TypedDict(
    "_RequiredGetInsightSummariesRequestRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)
_OptionalGetInsightSummariesRequestRequestTypeDef = TypedDict(
    "_OptionalGetInsightSummariesRequestRequestTypeDef",
    {
        "States": List[InsightStateType],
        "GroupARN": str,
        "GroupName": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetInsightSummariesRequestRequestTypeDef(
    _RequiredGetInsightSummariesRequestRequestTypeDef,
    _OptionalGetInsightSummariesRequestRequestTypeDef,
):
    pass

GetInsightSummariesResultTypeDef = TypedDict(
    "GetInsightSummariesResultTypeDef",
    {
        "InsightSummaries": List["InsightSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSamplingRulesRequestRequestTypeDef = TypedDict(
    "GetSamplingRulesRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

GetSamplingRulesResultTypeDef = TypedDict(
    "GetSamplingRulesResultTypeDef",
    {
        "SamplingRuleRecords": List["SamplingRuleRecordTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSamplingStatisticSummariesRequestRequestTypeDef = TypedDict(
    "GetSamplingStatisticSummariesRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

GetSamplingStatisticSummariesResultTypeDef = TypedDict(
    "GetSamplingStatisticSummariesResultTypeDef",
    {
        "SamplingStatisticSummaries": List["SamplingStatisticSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSamplingTargetsRequestRequestTypeDef = TypedDict(
    "GetSamplingTargetsRequestRequestTypeDef",
    {
        "SamplingStatisticsDocuments": List["SamplingStatisticsDocumentTypeDef"],
    },
)

GetSamplingTargetsResultTypeDef = TypedDict(
    "GetSamplingTargetsResultTypeDef",
    {
        "SamplingTargetDocuments": List["SamplingTargetDocumentTypeDef"],
        "LastRuleModification": datetime,
        "UnprocessedStatistics": List["UnprocessedStatisticsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetServiceGraphRequestRequestTypeDef = TypedDict(
    "_RequiredGetServiceGraphRequestRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)
_OptionalGetServiceGraphRequestRequestTypeDef = TypedDict(
    "_OptionalGetServiceGraphRequestRequestTypeDef",
    {
        "GroupName": str,
        "GroupARN": str,
        "NextToken": str,
    },
    total=False,
)

class GetServiceGraphRequestRequestTypeDef(
    _RequiredGetServiceGraphRequestRequestTypeDef, _OptionalGetServiceGraphRequestRequestTypeDef
):
    pass

GetServiceGraphResultTypeDef = TypedDict(
    "GetServiceGraphResultTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "Services": List["ServiceTypeDef"],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTimeSeriesServiceStatisticsRequestRequestTypeDef = TypedDict(
    "_RequiredGetTimeSeriesServiceStatisticsRequestRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)
_OptionalGetTimeSeriesServiceStatisticsRequestRequestTypeDef = TypedDict(
    "_OptionalGetTimeSeriesServiceStatisticsRequestRequestTypeDef",
    {
        "GroupName": str,
        "GroupARN": str,
        "EntitySelectorExpression": str,
        "Period": int,
        "ForecastStatistics": bool,
        "NextToken": str,
    },
    total=False,
)

class GetTimeSeriesServiceStatisticsRequestRequestTypeDef(
    _RequiredGetTimeSeriesServiceStatisticsRequestRequestTypeDef,
    _OptionalGetTimeSeriesServiceStatisticsRequestRequestTypeDef,
):
    pass

GetTimeSeriesServiceStatisticsResultTypeDef = TypedDict(
    "GetTimeSeriesServiceStatisticsResultTypeDef",
    {
        "TimeSeriesServiceStatistics": List["TimeSeriesServiceStatisticsTypeDef"],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTraceGraphRequestRequestTypeDef = TypedDict(
    "_RequiredGetTraceGraphRequestRequestTypeDef",
    {
        "TraceIds": List[str],
    },
)
_OptionalGetTraceGraphRequestRequestTypeDef = TypedDict(
    "_OptionalGetTraceGraphRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class GetTraceGraphRequestRequestTypeDef(
    _RequiredGetTraceGraphRequestRequestTypeDef, _OptionalGetTraceGraphRequestRequestTypeDef
):
    pass

GetTraceGraphResultTypeDef = TypedDict(
    "GetTraceGraphResultTypeDef",
    {
        "Services": List["ServiceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTraceSummariesRequestRequestTypeDef = TypedDict(
    "_RequiredGetTraceSummariesRequestRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)
_OptionalGetTraceSummariesRequestRequestTypeDef = TypedDict(
    "_OptionalGetTraceSummariesRequestRequestTypeDef",
    {
        "TimeRangeType": TimeRangeTypeType,
        "Sampling": bool,
        "SamplingStrategy": "SamplingStrategyTypeDef",
        "FilterExpression": str,
        "NextToken": str,
    },
    total=False,
)

class GetTraceSummariesRequestRequestTypeDef(
    _RequiredGetTraceSummariesRequestRequestTypeDef, _OptionalGetTraceSummariesRequestRequestTypeDef
):
    pass

GetTraceSummariesResultTypeDef = TypedDict(
    "GetTraceSummariesResultTypeDef",
    {
        "TraceSummaries": List["TraceSummaryTypeDef"],
        "ApproximateTime": datetime,
        "TracesProcessedCount": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupSummaryTypeDef = TypedDict(
    "GroupSummaryTypeDef",
    {
        "GroupName": str,
        "GroupARN": str,
        "FilterExpression": str,
        "InsightsConfiguration": "InsightsConfigurationTypeDef",
    },
    total=False,
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "GroupName": str,
        "GroupARN": str,
        "FilterExpression": str,
        "InsightsConfiguration": "InsightsConfigurationTypeDef",
    },
    total=False,
)

HistogramEntryTypeDef = TypedDict(
    "HistogramEntryTypeDef",
    {
        "Value": float,
        "Count": int,
    },
    total=False,
)

HttpTypeDef = TypedDict(
    "HttpTypeDef",
    {
        "HttpURL": str,
        "HttpStatus": int,
        "HttpMethod": str,
        "UserAgent": str,
        "ClientIp": str,
    },
    total=False,
)

InsightEventTypeDef = TypedDict(
    "InsightEventTypeDef",
    {
        "Summary": str,
        "EventTime": datetime,
        "ClientRequestImpactStatistics": "RequestImpactStatisticsTypeDef",
        "RootCauseServiceRequestImpactStatistics": "RequestImpactStatisticsTypeDef",
        "TopAnomalousServices": List["AnomalousServiceTypeDef"],
    },
    total=False,
)

InsightImpactGraphEdgeTypeDef = TypedDict(
    "InsightImpactGraphEdgeTypeDef",
    {
        "ReferenceId": int,
    },
    total=False,
)

InsightImpactGraphServiceTypeDef = TypedDict(
    "InsightImpactGraphServiceTypeDef",
    {
        "ReferenceId": int,
        "Type": str,
        "Name": str,
        "Names": List[str],
        "AccountId": str,
        "Edges": List["InsightImpactGraphEdgeTypeDef"],
    },
    total=False,
)

InsightSummaryTypeDef = TypedDict(
    "InsightSummaryTypeDef",
    {
        "InsightId": str,
        "GroupARN": str,
        "GroupName": str,
        "RootCauseServiceId": "ServiceIdTypeDef",
        "Categories": List[Literal["FAULT"]],
        "State": InsightStateType,
        "StartTime": datetime,
        "EndTime": datetime,
        "Summary": str,
        "ClientRequestImpactStatistics": "RequestImpactStatisticsTypeDef",
        "RootCauseServiceRequestImpactStatistics": "RequestImpactStatisticsTypeDef",
        "TopAnomalousServices": List["AnomalousServiceTypeDef"],
        "LastUpdateTime": datetime,
    },
    total=False,
)

InsightTypeDef = TypedDict(
    "InsightTypeDef",
    {
        "InsightId": str,
        "GroupARN": str,
        "GroupName": str,
        "RootCauseServiceId": "ServiceIdTypeDef",
        "Categories": List[Literal["FAULT"]],
        "State": InsightStateType,
        "StartTime": datetime,
        "EndTime": datetime,
        "Summary": str,
        "ClientRequestImpactStatistics": "RequestImpactStatisticsTypeDef",
        "RootCauseServiceRequestImpactStatistics": "RequestImpactStatisticsTypeDef",
        "TopAnomalousServices": List["AnomalousServiceTypeDef"],
    },
    total=False,
)

InsightsConfigurationTypeDef = TypedDict(
    "InsightsConfigurationTypeDef",
    {
        "InsightsEnabled": bool,
        "NotificationsEnabled": bool,
    },
    total=False,
)

InstanceIdDetailTypeDef = TypedDict(
    "InstanceIdDetailTypeDef",
    {
        "Id": str,
    },
    total=False,
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredPutEncryptionConfigRequestRequestTypeDef = TypedDict(
    "_RequiredPutEncryptionConfigRequestRequestTypeDef",
    {
        "Type": EncryptionTypeType,
    },
)
_OptionalPutEncryptionConfigRequestRequestTypeDef = TypedDict(
    "_OptionalPutEncryptionConfigRequestRequestTypeDef",
    {
        "KeyId": str,
    },
    total=False,
)

class PutEncryptionConfigRequestRequestTypeDef(
    _RequiredPutEncryptionConfigRequestRequestTypeDef,
    _OptionalPutEncryptionConfigRequestRequestTypeDef,
):
    pass

PutEncryptionConfigResultTypeDef = TypedDict(
    "PutEncryptionConfigResultTypeDef",
    {
        "EncryptionConfig": "EncryptionConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutTelemetryRecordsRequestRequestTypeDef = TypedDict(
    "_RequiredPutTelemetryRecordsRequestRequestTypeDef",
    {
        "TelemetryRecords": List["TelemetryRecordTypeDef"],
    },
)
_OptionalPutTelemetryRecordsRequestRequestTypeDef = TypedDict(
    "_OptionalPutTelemetryRecordsRequestRequestTypeDef",
    {
        "EC2InstanceId": str,
        "Hostname": str,
        "ResourceARN": str,
    },
    total=False,
)

class PutTelemetryRecordsRequestRequestTypeDef(
    _RequiredPutTelemetryRecordsRequestRequestTypeDef,
    _OptionalPutTelemetryRecordsRequestRequestTypeDef,
):
    pass

PutTraceSegmentsRequestRequestTypeDef = TypedDict(
    "PutTraceSegmentsRequestRequestTypeDef",
    {
        "TraceSegmentDocuments": List[str],
    },
)

PutTraceSegmentsResultTypeDef = TypedDict(
    "PutTraceSegmentsResultTypeDef",
    {
        "UnprocessedTraceSegments": List["UnprocessedTraceSegmentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequestImpactStatisticsTypeDef = TypedDict(
    "RequestImpactStatisticsTypeDef",
    {
        "FaultCount": int,
        "OkCount": int,
        "TotalCount": int,
    },
    total=False,
)

ResourceARNDetailTypeDef = TypedDict(
    "ResourceARNDetailTypeDef",
    {
        "ARN": str,
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

ResponseTimeRootCauseEntityTypeDef = TypedDict(
    "ResponseTimeRootCauseEntityTypeDef",
    {
        "Name": str,
        "Coverage": float,
        "Remote": bool,
    },
    total=False,
)

ResponseTimeRootCauseServiceTypeDef = TypedDict(
    "ResponseTimeRootCauseServiceTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List["ResponseTimeRootCauseEntityTypeDef"],
        "Inferred": bool,
    },
    total=False,
)

ResponseTimeRootCauseTypeDef = TypedDict(
    "ResponseTimeRootCauseTypeDef",
    {
        "Services": List["ResponseTimeRootCauseServiceTypeDef"],
        "ClientImpacting": bool,
    },
    total=False,
)

RootCauseExceptionTypeDef = TypedDict(
    "RootCauseExceptionTypeDef",
    {
        "Name": str,
        "Message": str,
    },
    total=False,
)

SamplingRuleRecordTypeDef = TypedDict(
    "SamplingRuleRecordTypeDef",
    {
        "SamplingRule": "SamplingRuleTypeDef",
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)

_RequiredSamplingRuleTypeDef = TypedDict(
    "_RequiredSamplingRuleTypeDef",
    {
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
    },
)
_OptionalSamplingRuleTypeDef = TypedDict(
    "_OptionalSamplingRuleTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)

class SamplingRuleTypeDef(_RequiredSamplingRuleTypeDef, _OptionalSamplingRuleTypeDef):
    pass

SamplingRuleUpdateTypeDef = TypedDict(
    "SamplingRuleUpdateTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "Host": str,
        "ServiceName": str,
        "ServiceType": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)

SamplingStatisticSummaryTypeDef = TypedDict(
    "SamplingStatisticSummaryTypeDef",
    {
        "RuleName": str,
        "Timestamp": datetime,
        "RequestCount": int,
        "BorrowCount": int,
        "SampledCount": int,
    },
    total=False,
)

_RequiredSamplingStatisticsDocumentTypeDef = TypedDict(
    "_RequiredSamplingStatisticsDocumentTypeDef",
    {
        "RuleName": str,
        "ClientID": str,
        "Timestamp": Union[datetime, str],
        "RequestCount": int,
        "SampledCount": int,
    },
)
_OptionalSamplingStatisticsDocumentTypeDef = TypedDict(
    "_OptionalSamplingStatisticsDocumentTypeDef",
    {
        "BorrowCount": int,
    },
    total=False,
)

class SamplingStatisticsDocumentTypeDef(
    _RequiredSamplingStatisticsDocumentTypeDef, _OptionalSamplingStatisticsDocumentTypeDef
):
    pass

SamplingStrategyTypeDef = TypedDict(
    "SamplingStrategyTypeDef",
    {
        "Name": SamplingStrategyNameType,
        "Value": float,
    },
    total=False,
)

SamplingTargetDocumentTypeDef = TypedDict(
    "SamplingTargetDocumentTypeDef",
    {
        "RuleName": str,
        "FixedRate": float,
        "ReservoirQuota": int,
        "ReservoirQuotaTTL": datetime,
        "Interval": int,
    },
    total=False,
)

SegmentTypeDef = TypedDict(
    "SegmentTypeDef",
    {
        "Id": str,
        "Document": str,
    },
    total=False,
)

ServiceIdTypeDef = TypedDict(
    "ServiceIdTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "AccountId": str,
        "Type": str,
    },
    total=False,
)

ServiceStatisticsTypeDef = TypedDict(
    "ServiceStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": "ErrorStatisticsTypeDef",
        "FaultStatistics": "FaultStatisticsTypeDef",
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "ReferenceId": int,
        "Name": str,
        "Names": List[str],
        "Root": bool,
        "AccountId": str,
        "Type": str,
        "State": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Edges": List["EdgeTypeDef"],
        "SummaryStatistics": "ServiceStatisticsTypeDef",
        "DurationHistogram": List["HistogramEntryTypeDef"],
        "ResponseTimeHistogram": List["HistogramEntryTypeDef"],
    },
    total=False,
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

_RequiredTelemetryRecordTypeDef = TypedDict(
    "_RequiredTelemetryRecordTypeDef",
    {
        "Timestamp": Union[datetime, str],
    },
)
_OptionalTelemetryRecordTypeDef = TypedDict(
    "_OptionalTelemetryRecordTypeDef",
    {
        "SegmentsReceivedCount": int,
        "SegmentsSentCount": int,
        "SegmentsSpilloverCount": int,
        "SegmentsRejectedCount": int,
        "BackendConnectionErrors": "BackendConnectionErrorsTypeDef",
    },
    total=False,
)

class TelemetryRecordTypeDef(_RequiredTelemetryRecordTypeDef, _OptionalTelemetryRecordTypeDef):
    pass

TimeSeriesServiceStatisticsTypeDef = TypedDict(
    "TimeSeriesServiceStatisticsTypeDef",
    {
        "Timestamp": datetime,
        "EdgeSummaryStatistics": "EdgeStatisticsTypeDef",
        "ServiceSummaryStatistics": "ServiceStatisticsTypeDef",
        "ServiceForecastStatistics": "ForecastStatisticsTypeDef",
        "ResponseTimeHistogram": List["HistogramEntryTypeDef"],
    },
    total=False,
)

TraceSummaryTypeDef = TypedDict(
    "TraceSummaryTypeDef",
    {
        "Id": str,
        "Duration": float,
        "ResponseTime": float,
        "HasFault": bool,
        "HasError": bool,
        "HasThrottle": bool,
        "IsPartial": bool,
        "Http": "HttpTypeDef",
        "Annotations": Dict[str, List["ValueWithServiceIdsTypeDef"]],
        "Users": List["TraceUserTypeDef"],
        "ServiceIds": List["ServiceIdTypeDef"],
        "ResourceARNs": List["ResourceARNDetailTypeDef"],
        "InstanceIds": List["InstanceIdDetailTypeDef"],
        "AvailabilityZones": List["AvailabilityZoneDetailTypeDef"],
        "EntryPoint": "ServiceIdTypeDef",
        "FaultRootCauses": List["FaultRootCauseTypeDef"],
        "ErrorRootCauses": List["ErrorRootCauseTypeDef"],
        "ResponseTimeRootCauses": List["ResponseTimeRootCauseTypeDef"],
        "Revision": int,
        "MatchedEventTime": datetime,
    },
    total=False,
)

TraceTypeDef = TypedDict(
    "TraceTypeDef",
    {
        "Id": str,
        "Duration": float,
        "LimitExceeded": bool,
        "Segments": List["SegmentTypeDef"],
    },
    total=False,
)

TraceUserTypeDef = TypedDict(
    "TraceUserTypeDef",
    {
        "UserName": str,
        "ServiceIds": List["ServiceIdTypeDef"],
    },
    total=False,
)

UnprocessedStatisticsTypeDef = TypedDict(
    "UnprocessedStatisticsTypeDef",
    {
        "RuleName": str,
        "ErrorCode": str,
        "Message": str,
    },
    total=False,
)

UnprocessedTraceSegmentTypeDef = TypedDict(
    "UnprocessedTraceSegmentTypeDef",
    {
        "Id": str,
        "ErrorCode": str,
        "Message": str,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

UpdateGroupRequestRequestTypeDef = TypedDict(
    "UpdateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "GroupARN": str,
        "FilterExpression": str,
        "InsightsConfiguration": "InsightsConfigurationTypeDef",
    },
    total=False,
)

UpdateGroupResultTypeDef = TypedDict(
    "UpdateGroupResultTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSamplingRuleRequestRequestTypeDef = TypedDict(
    "UpdateSamplingRuleRequestRequestTypeDef",
    {
        "SamplingRuleUpdate": "SamplingRuleUpdateTypeDef",
    },
)

UpdateSamplingRuleResultTypeDef = TypedDict(
    "UpdateSamplingRuleResultTypeDef",
    {
        "SamplingRuleRecord": "SamplingRuleRecordTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValueWithServiceIdsTypeDef = TypedDict(
    "ValueWithServiceIdsTypeDef",
    {
        "AnnotationValue": "AnnotationValueTypeDef",
        "ServiceIds": List["ServiceIdTypeDef"],
    },
    total=False,
)
