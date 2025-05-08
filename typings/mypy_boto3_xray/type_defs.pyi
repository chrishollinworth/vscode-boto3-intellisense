"""
Type annotations for xray service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_xray.type_defs import AliasTypeDef

    data: AliasTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    EncryptionStatusType,
    EncryptionTypeType,
    InsightStateType,
    RetrievalStatusType,
    SamplingStrategyNameType,
    TimeRangeTypeType,
    TraceFormatTypeType,
    TraceSegmentDestinationStatusType,
    TraceSegmentDestinationType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AliasTypeDef",
    "AnnotationValueTypeDef",
    "AnomalousServiceTypeDef",
    "AvailabilityZoneDetailTypeDef",
    "BackendConnectionErrorsTypeDef",
    "BatchGetTracesRequestPaginateTypeDef",
    "BatchGetTracesRequestTypeDef",
    "BatchGetTracesResultTypeDef",
    "CancelTraceRetrievalRequestTypeDef",
    "CreateGroupRequestTypeDef",
    "CreateGroupResultTypeDef",
    "CreateSamplingRuleRequestTypeDef",
    "CreateSamplingRuleResultTypeDef",
    "DeleteGroupRequestTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DeleteSamplingRuleRequestTypeDef",
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
    "GetGroupRequestTypeDef",
    "GetGroupResultTypeDef",
    "GetGroupsRequestPaginateTypeDef",
    "GetGroupsRequestTypeDef",
    "GetGroupsResultTypeDef",
    "GetIndexingRulesRequestTypeDef",
    "GetIndexingRulesResultTypeDef",
    "GetInsightEventsRequestTypeDef",
    "GetInsightEventsResultTypeDef",
    "GetInsightImpactGraphRequestTypeDef",
    "GetInsightImpactGraphResultTypeDef",
    "GetInsightRequestTypeDef",
    "GetInsightResultTypeDef",
    "GetInsightSummariesRequestTypeDef",
    "GetInsightSummariesResultTypeDef",
    "GetRetrievedTracesGraphRequestTypeDef",
    "GetRetrievedTracesGraphResultTypeDef",
    "GetSamplingRulesRequestPaginateTypeDef",
    "GetSamplingRulesRequestTypeDef",
    "GetSamplingRulesResultTypeDef",
    "GetSamplingStatisticSummariesRequestPaginateTypeDef",
    "GetSamplingStatisticSummariesRequestTypeDef",
    "GetSamplingStatisticSummariesResultTypeDef",
    "GetSamplingTargetsRequestTypeDef",
    "GetSamplingTargetsResultTypeDef",
    "GetServiceGraphRequestPaginateTypeDef",
    "GetServiceGraphRequestTypeDef",
    "GetServiceGraphResultTypeDef",
    "GetTimeSeriesServiceStatisticsRequestPaginateTypeDef",
    "GetTimeSeriesServiceStatisticsRequestTypeDef",
    "GetTimeSeriesServiceStatisticsResultTypeDef",
    "GetTraceGraphRequestPaginateTypeDef",
    "GetTraceGraphRequestTypeDef",
    "GetTraceGraphResultTypeDef",
    "GetTraceSegmentDestinationResultTypeDef",
    "GetTraceSummariesRequestPaginateTypeDef",
    "GetTraceSummariesRequestTypeDef",
    "GetTraceSummariesResultTypeDef",
    "GraphLinkTypeDef",
    "GroupSummaryTypeDef",
    "GroupTypeDef",
    "HistogramEntryTypeDef",
    "HttpTypeDef",
    "IndexingRuleTypeDef",
    "IndexingRuleValueTypeDef",
    "IndexingRuleValueUpdateTypeDef",
    "InsightEventTypeDef",
    "InsightImpactGraphEdgeTypeDef",
    "InsightImpactGraphServiceTypeDef",
    "InsightSummaryTypeDef",
    "InsightTypeDef",
    "InsightsConfigurationTypeDef",
    "InstanceIdDetailTypeDef",
    "ListResourcePoliciesRequestPaginateTypeDef",
    "ListResourcePoliciesRequestTypeDef",
    "ListResourcePoliciesResultTypeDef",
    "ListRetrievedTracesRequestTypeDef",
    "ListRetrievedTracesResultTypeDef",
    "ListTagsForResourceRequestPaginateTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ProbabilisticRuleValueTypeDef",
    "ProbabilisticRuleValueUpdateTypeDef",
    "PutEncryptionConfigRequestTypeDef",
    "PutEncryptionConfigResultTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "PutResourcePolicyResultTypeDef",
    "PutTelemetryRecordsRequestTypeDef",
    "PutTraceSegmentsRequestTypeDef",
    "PutTraceSegmentsResultTypeDef",
    "RequestImpactStatisticsTypeDef",
    "ResourceARNDetailTypeDef",
    "ResourcePolicyTypeDef",
    "ResponseMetadataTypeDef",
    "ResponseTimeRootCauseEntityTypeDef",
    "ResponseTimeRootCauseServiceTypeDef",
    "ResponseTimeRootCauseTypeDef",
    "RetrievedServiceTypeDef",
    "RetrievedTraceTypeDef",
    "RootCauseExceptionTypeDef",
    "SamplingRuleOutputTypeDef",
    "SamplingRuleRecordTypeDef",
    "SamplingRuleTypeDef",
    "SamplingRuleUnionTypeDef",
    "SamplingRuleUpdateTypeDef",
    "SamplingStatisticSummaryTypeDef",
    "SamplingStatisticsDocumentTypeDef",
    "SamplingStrategyTypeDef",
    "SamplingTargetDocumentTypeDef",
    "SegmentTypeDef",
    "ServiceIdTypeDef",
    "ServiceStatisticsTypeDef",
    "ServiceTypeDef",
    "SpanTypeDef",
    "StartTraceRetrievalRequestTypeDef",
    "StartTraceRetrievalResultTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TelemetryRecordTypeDef",
    "TimeSeriesServiceStatisticsTypeDef",
    "TimestampTypeDef",
    "TraceSummaryTypeDef",
    "TraceTypeDef",
    "TraceUserTypeDef",
    "UnprocessedStatisticsTypeDef",
    "UnprocessedTraceSegmentTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateGroupRequestTypeDef",
    "UpdateGroupResultTypeDef",
    "UpdateIndexingRuleRequestTypeDef",
    "UpdateIndexingRuleResultTypeDef",
    "UpdateSamplingRuleRequestTypeDef",
    "UpdateSamplingRuleResultTypeDef",
    "UpdateTraceSegmentDestinationRequestTypeDef",
    "UpdateTraceSegmentDestinationResultTypeDef",
    "ValueWithServiceIdsTypeDef",
)

AliasTypeDef = TypedDict(
    "AliasTypeDef",
    {
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "Type": NotRequired[str],
    },
)

class AnnotationValueTypeDef(TypedDict):
    NumberValue: NotRequired[float]
    BooleanValue: NotRequired[bool]
    StringValue: NotRequired[str]

ServiceIdTypeDef = TypedDict(
    "ServiceIdTypeDef",
    {
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "AccountId": NotRequired[str],
        "Type": NotRequired[str],
    },
)

class AvailabilityZoneDetailTypeDef(TypedDict):
    Name: NotRequired[str]

class BackendConnectionErrorsTypeDef(TypedDict):
    TimeoutCount: NotRequired[int]
    ConnectionRefusedCount: NotRequired[int]
    HTTPCode4XXCount: NotRequired[int]
    HTTPCode5XXCount: NotRequired[int]
    UnknownHostCount: NotRequired[int]
    OtherCount: NotRequired[int]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class BatchGetTracesRequestTypeDef(TypedDict):
    TraceIds: Sequence[str]
    NextToken: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CancelTraceRetrievalRequestTypeDef(TypedDict):
    RetrievalToken: str

class InsightsConfigurationTypeDef(TypedDict):
    InsightsEnabled: NotRequired[bool]
    NotificationsEnabled: NotRequired[bool]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class DeleteGroupRequestTypeDef(TypedDict):
    GroupName: NotRequired[str]
    GroupARN: NotRequired[str]

class DeleteResourcePolicyRequestTypeDef(TypedDict):
    PolicyName: str
    PolicyRevisionId: NotRequired[str]

class DeleteSamplingRuleRequestTypeDef(TypedDict):
    RuleName: NotRequired[str]
    RuleARN: NotRequired[str]

class ErrorStatisticsTypeDef(TypedDict):
    ThrottleCount: NotRequired[int]
    OtherCount: NotRequired[int]
    TotalCount: NotRequired[int]

class FaultStatisticsTypeDef(TypedDict):
    OtherCount: NotRequired[int]
    TotalCount: NotRequired[int]

class HistogramEntryTypeDef(TypedDict):
    Value: NotRequired[float]
    Count: NotRequired[int]

EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "KeyId": NotRequired[str],
        "Status": NotRequired[EncryptionStatusType],
        "Type": NotRequired[EncryptionTypeType],
    },
)

class RootCauseExceptionTypeDef(TypedDict):
    Name: NotRequired[str]
    Message: NotRequired[str]

class ForecastStatisticsTypeDef(TypedDict):
    FaultCountHigh: NotRequired[int]
    FaultCountLow: NotRequired[int]

class GetGroupRequestTypeDef(TypedDict):
    GroupName: NotRequired[str]
    GroupARN: NotRequired[str]

class GetGroupsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]

class GetIndexingRulesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]

class GetInsightEventsRequestTypeDef(TypedDict):
    InsightId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class GetInsightRequestTypeDef(TypedDict):
    InsightId: str

class GetRetrievedTracesGraphRequestTypeDef(TypedDict):
    RetrievalToken: str
    NextToken: NotRequired[str]

class GetSamplingRulesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]

class GetSamplingStatisticSummariesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]

class SamplingStatisticSummaryTypeDef(TypedDict):
    RuleName: NotRequired[str]
    Timestamp: NotRequired[datetime]
    RequestCount: NotRequired[int]
    BorrowCount: NotRequired[int]
    SampledCount: NotRequired[int]

class SamplingTargetDocumentTypeDef(TypedDict):
    RuleName: NotRequired[str]
    FixedRate: NotRequired[float]
    ReservoirQuota: NotRequired[int]
    ReservoirQuotaTTL: NotRequired[datetime]
    Interval: NotRequired[int]

class UnprocessedStatisticsTypeDef(TypedDict):
    RuleName: NotRequired[str]
    ErrorCode: NotRequired[str]
    Message: NotRequired[str]

class GetTraceGraphRequestTypeDef(TypedDict):
    TraceIds: Sequence[str]
    NextToken: NotRequired[str]

class SamplingStrategyTypeDef(TypedDict):
    Name: NotRequired[SamplingStrategyNameType]
    Value: NotRequired[float]

class GraphLinkTypeDef(TypedDict):
    ReferenceType: NotRequired[str]
    SourceTraceId: NotRequired[str]
    DestinationTraceIds: NotRequired[List[str]]

class HttpTypeDef(TypedDict):
    HttpURL: NotRequired[str]
    HttpStatus: NotRequired[int]
    HttpMethod: NotRequired[str]
    UserAgent: NotRequired[str]
    ClientIp: NotRequired[str]

class ProbabilisticRuleValueTypeDef(TypedDict):
    DesiredSamplingPercentage: float
    ActualSamplingPercentage: NotRequired[float]

class ProbabilisticRuleValueUpdateTypeDef(TypedDict):
    DesiredSamplingPercentage: float

class RequestImpactStatisticsTypeDef(TypedDict):
    FaultCount: NotRequired[int]
    OkCount: NotRequired[int]
    TotalCount: NotRequired[int]

class InsightImpactGraphEdgeTypeDef(TypedDict):
    ReferenceId: NotRequired[int]

class InstanceIdDetailTypeDef(TypedDict):
    Id: NotRequired[str]

class ListResourcePoliciesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]

class ResourcePolicyTypeDef(TypedDict):
    PolicyName: NotRequired[str]
    PolicyDocument: NotRequired[str]
    PolicyRevisionId: NotRequired[str]
    LastUpdatedTime: NotRequired[datetime]

class ListRetrievedTracesRequestTypeDef(TypedDict):
    RetrievalToken: str
    TraceFormat: NotRequired[TraceFormatTypeType]
    NextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    NextToken: NotRequired[str]

PutEncryptionConfigRequestTypeDef = TypedDict(
    "PutEncryptionConfigRequestTypeDef",
    {
        "Type": EncryptionTypeType,
        "KeyId": NotRequired[str],
    },
)

class PutResourcePolicyRequestTypeDef(TypedDict):
    PolicyName: str
    PolicyDocument: str
    PolicyRevisionId: NotRequired[str]
    BypassPolicyLockoutCheck: NotRequired[bool]

class PutTraceSegmentsRequestTypeDef(TypedDict):
    TraceSegmentDocuments: Sequence[str]

class UnprocessedTraceSegmentTypeDef(TypedDict):
    Id: NotRequired[str]
    ErrorCode: NotRequired[str]
    Message: NotRequired[str]

class ResourceARNDetailTypeDef(TypedDict):
    ARN: NotRequired[str]

class ResponseTimeRootCauseEntityTypeDef(TypedDict):
    Name: NotRequired[str]
    Coverage: NotRequired[float]
    Remote: NotRequired[bool]

class SpanTypeDef(TypedDict):
    Id: NotRequired[str]
    Document: NotRequired[str]

SamplingRuleOutputTypeDef = TypedDict(
    "SamplingRuleOutputTypeDef",
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
        "RuleName": NotRequired[str],
        "RuleARN": NotRequired[str],
        "Attributes": NotRequired[Dict[str, str]],
    },
)
SamplingRuleTypeDef = TypedDict(
    "SamplingRuleTypeDef",
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
        "RuleName": NotRequired[str],
        "RuleARN": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
    },
)
SamplingRuleUpdateTypeDef = TypedDict(
    "SamplingRuleUpdateTypeDef",
    {
        "RuleName": NotRequired[str],
        "RuleARN": NotRequired[str],
        "ResourceARN": NotRequired[str],
        "Priority": NotRequired[int],
        "FixedRate": NotRequired[float],
        "ReservoirSize": NotRequired[int],
        "Host": NotRequired[str],
        "ServiceName": NotRequired[str],
        "ServiceType": NotRequired[str],
        "HTTPMethod": NotRequired[str],
        "URLPath": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
    },
)

class SegmentTypeDef(TypedDict):
    Id: NotRequired[str]
    Document: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateTraceSegmentDestinationRequestTypeDef(TypedDict):
    Destination: NotRequired[TraceSegmentDestinationType]

class AnomalousServiceTypeDef(TypedDict):
    ServiceId: NotRequired[ServiceIdTypeDef]

class TraceUserTypeDef(TypedDict):
    UserName: NotRequired[str]
    ServiceIds: NotRequired[List[ServiceIdTypeDef]]

class ValueWithServiceIdsTypeDef(TypedDict):
    AnnotationValue: NotRequired[AnnotationValueTypeDef]
    ServiceIds: NotRequired[List[ServiceIdTypeDef]]

class BatchGetTracesRequestPaginateTypeDef(TypedDict):
    TraceIds: Sequence[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetGroupsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetSamplingRulesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetSamplingStatisticSummariesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetTraceGraphRequestPaginateTypeDef(TypedDict):
    TraceIds: Sequence[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourcePoliciesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceRequestPaginateTypeDef(TypedDict):
    ResourceARN: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetTraceSegmentDestinationResultTypeDef(TypedDict):
    Destination: TraceSegmentDestinationType
    Status: TraceSegmentDestinationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartTraceRetrievalResultTypeDef(TypedDict):
    RetrievalToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTraceSegmentDestinationResultTypeDef(TypedDict):
    Destination: TraceSegmentDestinationType
    Status: TraceSegmentDestinationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GroupSummaryTypeDef(TypedDict):
    GroupName: NotRequired[str]
    GroupARN: NotRequired[str]
    FilterExpression: NotRequired[str]
    InsightsConfiguration: NotRequired[InsightsConfigurationTypeDef]

class GroupTypeDef(TypedDict):
    GroupName: NotRequired[str]
    GroupARN: NotRequired[str]
    FilterExpression: NotRequired[str]
    InsightsConfiguration: NotRequired[InsightsConfigurationTypeDef]

class UpdateGroupRequestTypeDef(TypedDict):
    GroupName: NotRequired[str]
    GroupARN: NotRequired[str]
    FilterExpression: NotRequired[str]
    InsightsConfiguration: NotRequired[InsightsConfigurationTypeDef]

class CreateGroupRequestTypeDef(TypedDict):
    GroupName: str
    FilterExpression: NotRequired[str]
    InsightsConfiguration: NotRequired[InsightsConfigurationTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class EdgeStatisticsTypeDef(TypedDict):
    OkCount: NotRequired[int]
    ErrorStatistics: NotRequired[ErrorStatisticsTypeDef]
    FaultStatistics: NotRequired[FaultStatisticsTypeDef]
    TotalCount: NotRequired[int]
    TotalResponseTime: NotRequired[float]

class ServiceStatisticsTypeDef(TypedDict):
    OkCount: NotRequired[int]
    ErrorStatistics: NotRequired[ErrorStatisticsTypeDef]
    FaultStatistics: NotRequired[FaultStatisticsTypeDef]
    TotalCount: NotRequired[int]
    TotalResponseTime: NotRequired[float]

class GetEncryptionConfigResultTypeDef(TypedDict):
    EncryptionConfig: EncryptionConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutEncryptionConfigResultTypeDef(TypedDict):
    EncryptionConfig: EncryptionConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ErrorRootCauseEntityTypeDef(TypedDict):
    Name: NotRequired[str]
    Exceptions: NotRequired[List[RootCauseExceptionTypeDef]]
    Remote: NotRequired[bool]

class FaultRootCauseEntityTypeDef(TypedDict):
    Name: NotRequired[str]
    Exceptions: NotRequired[List[RootCauseExceptionTypeDef]]
    Remote: NotRequired[bool]

class GetInsightImpactGraphRequestTypeDef(TypedDict):
    InsightId: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    NextToken: NotRequired[str]

class GetInsightSummariesRequestTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    States: NotRequired[Sequence[InsightStateType]]
    GroupARN: NotRequired[str]
    GroupName: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetServiceGraphRequestPaginateTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    GroupName: NotRequired[str]
    GroupARN: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetServiceGraphRequestTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    GroupName: NotRequired[str]
    GroupARN: NotRequired[str]
    NextToken: NotRequired[str]

class GetTimeSeriesServiceStatisticsRequestPaginateTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    GroupName: NotRequired[str]
    GroupARN: NotRequired[str]
    EntitySelectorExpression: NotRequired[str]
    Period: NotRequired[int]
    ForecastStatistics: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetTimeSeriesServiceStatisticsRequestTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    GroupName: NotRequired[str]
    GroupARN: NotRequired[str]
    EntitySelectorExpression: NotRequired[str]
    Period: NotRequired[int]
    ForecastStatistics: NotRequired[bool]
    NextToken: NotRequired[str]

class SamplingStatisticsDocumentTypeDef(TypedDict):
    RuleName: str
    ClientID: str
    Timestamp: TimestampTypeDef
    RequestCount: int
    SampledCount: int
    BorrowCount: NotRequired[int]

class StartTraceRetrievalRequestTypeDef(TypedDict):
    TraceIds: Sequence[str]
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef

class TelemetryRecordTypeDef(TypedDict):
    Timestamp: TimestampTypeDef
    SegmentsReceivedCount: NotRequired[int]
    SegmentsSentCount: NotRequired[int]
    SegmentsSpilloverCount: NotRequired[int]
    SegmentsRejectedCount: NotRequired[int]
    BackendConnectionErrors: NotRequired[BackendConnectionErrorsTypeDef]

class GetSamplingStatisticSummariesResultTypeDef(TypedDict):
    SamplingStatisticSummaries: List[SamplingStatisticSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetSamplingTargetsResultTypeDef(TypedDict):
    SamplingTargetDocuments: List[SamplingTargetDocumentTypeDef]
    LastRuleModification: datetime
    UnprocessedStatistics: List[UnprocessedStatisticsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTraceSummariesRequestPaginateTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    TimeRangeType: NotRequired[TimeRangeTypeType]
    Sampling: NotRequired[bool]
    SamplingStrategy: NotRequired[SamplingStrategyTypeDef]
    FilterExpression: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetTraceSummariesRequestTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    TimeRangeType: NotRequired[TimeRangeTypeType]
    Sampling: NotRequired[bool]
    SamplingStrategy: NotRequired[SamplingStrategyTypeDef]
    FilterExpression: NotRequired[str]
    NextToken: NotRequired[str]

class IndexingRuleValueTypeDef(TypedDict):
    Probabilistic: NotRequired[ProbabilisticRuleValueTypeDef]

class IndexingRuleValueUpdateTypeDef(TypedDict):
    Probabilistic: NotRequired[ProbabilisticRuleValueUpdateTypeDef]

InsightImpactGraphServiceTypeDef = TypedDict(
    "InsightImpactGraphServiceTypeDef",
    {
        "ReferenceId": NotRequired[int],
        "Type": NotRequired[str],
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "AccountId": NotRequired[str],
        "Edges": NotRequired[List[InsightImpactGraphEdgeTypeDef]],
    },
)

class ListResourcePoliciesResultTypeDef(TypedDict):
    ResourcePolicies: List[ResourcePolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutResourcePolicyResultTypeDef(TypedDict):
    ResourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutTraceSegmentsResultTypeDef(TypedDict):
    UnprocessedTraceSegments: List[UnprocessedTraceSegmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

ResponseTimeRootCauseServiceTypeDef = TypedDict(
    "ResponseTimeRootCauseServiceTypeDef",
    {
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "Type": NotRequired[str],
        "AccountId": NotRequired[str],
        "EntityPath": NotRequired[List[ResponseTimeRootCauseEntityTypeDef]],
        "Inferred": NotRequired[bool],
    },
)

class RetrievedTraceTypeDef(TypedDict):
    Id: NotRequired[str]
    Duration: NotRequired[float]
    Spans: NotRequired[List[SpanTypeDef]]

class SamplingRuleRecordTypeDef(TypedDict):
    SamplingRule: NotRequired[SamplingRuleOutputTypeDef]
    CreatedAt: NotRequired[datetime]
    ModifiedAt: NotRequired[datetime]

SamplingRuleUnionTypeDef = Union[SamplingRuleTypeDef, SamplingRuleOutputTypeDef]

class UpdateSamplingRuleRequestTypeDef(TypedDict):
    SamplingRuleUpdate: SamplingRuleUpdateTypeDef

class TraceTypeDef(TypedDict):
    Id: NotRequired[str]
    Duration: NotRequired[float]
    LimitExceeded: NotRequired[bool]
    Segments: NotRequired[List[SegmentTypeDef]]

class InsightEventTypeDef(TypedDict):
    Summary: NotRequired[str]
    EventTime: NotRequired[datetime]
    ClientRequestImpactStatistics: NotRequired[RequestImpactStatisticsTypeDef]
    RootCauseServiceRequestImpactStatistics: NotRequired[RequestImpactStatisticsTypeDef]
    TopAnomalousServices: NotRequired[List[AnomalousServiceTypeDef]]

class InsightSummaryTypeDef(TypedDict):
    InsightId: NotRequired[str]
    GroupARN: NotRequired[str]
    GroupName: NotRequired[str]
    RootCauseServiceId: NotRequired[ServiceIdTypeDef]
    Categories: NotRequired[List[Literal["FAULT"]]]
    State: NotRequired[InsightStateType]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    Summary: NotRequired[str]
    ClientRequestImpactStatistics: NotRequired[RequestImpactStatisticsTypeDef]
    RootCauseServiceRequestImpactStatistics: NotRequired[RequestImpactStatisticsTypeDef]
    TopAnomalousServices: NotRequired[List[AnomalousServiceTypeDef]]
    LastUpdateTime: NotRequired[datetime]

class InsightTypeDef(TypedDict):
    InsightId: NotRequired[str]
    GroupARN: NotRequired[str]
    GroupName: NotRequired[str]
    RootCauseServiceId: NotRequired[ServiceIdTypeDef]
    Categories: NotRequired[List[Literal["FAULT"]]]
    State: NotRequired[InsightStateType]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    Summary: NotRequired[str]
    ClientRequestImpactStatistics: NotRequired[RequestImpactStatisticsTypeDef]
    RootCauseServiceRequestImpactStatistics: NotRequired[RequestImpactStatisticsTypeDef]
    TopAnomalousServices: NotRequired[List[AnomalousServiceTypeDef]]

class GetGroupsResultTypeDef(TypedDict):
    Groups: List[GroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateGroupResultTypeDef(TypedDict):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupResultTypeDef(TypedDict):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGroupResultTypeDef(TypedDict):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EdgeTypeDef(TypedDict):
    ReferenceId: NotRequired[int]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    SummaryStatistics: NotRequired[EdgeStatisticsTypeDef]
    ResponseTimeHistogram: NotRequired[List[HistogramEntryTypeDef]]
    Aliases: NotRequired[List[AliasTypeDef]]
    EdgeType: NotRequired[str]
    ReceivedEventAgeHistogram: NotRequired[List[HistogramEntryTypeDef]]

class TimeSeriesServiceStatisticsTypeDef(TypedDict):
    Timestamp: NotRequired[datetime]
    EdgeSummaryStatistics: NotRequired[EdgeStatisticsTypeDef]
    ServiceSummaryStatistics: NotRequired[ServiceStatisticsTypeDef]
    ServiceForecastStatistics: NotRequired[ForecastStatisticsTypeDef]
    ResponseTimeHistogram: NotRequired[List[HistogramEntryTypeDef]]

ErrorRootCauseServiceTypeDef = TypedDict(
    "ErrorRootCauseServiceTypeDef",
    {
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "Type": NotRequired[str],
        "AccountId": NotRequired[str],
        "EntityPath": NotRequired[List[ErrorRootCauseEntityTypeDef]],
        "Inferred": NotRequired[bool],
    },
)
FaultRootCauseServiceTypeDef = TypedDict(
    "FaultRootCauseServiceTypeDef",
    {
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "Type": NotRequired[str],
        "AccountId": NotRequired[str],
        "EntityPath": NotRequired[List[FaultRootCauseEntityTypeDef]],
        "Inferred": NotRequired[bool],
    },
)

class GetSamplingTargetsRequestTypeDef(TypedDict):
    SamplingStatisticsDocuments: Sequence[SamplingStatisticsDocumentTypeDef]

class PutTelemetryRecordsRequestTypeDef(TypedDict):
    TelemetryRecords: Sequence[TelemetryRecordTypeDef]
    EC2InstanceId: NotRequired[str]
    Hostname: NotRequired[str]
    ResourceARN: NotRequired[str]

class IndexingRuleTypeDef(TypedDict):
    Name: NotRequired[str]
    ModifiedAt: NotRequired[datetime]
    Rule: NotRequired[IndexingRuleValueTypeDef]

class UpdateIndexingRuleRequestTypeDef(TypedDict):
    Name: str
    Rule: IndexingRuleValueUpdateTypeDef

class GetInsightImpactGraphResultTypeDef(TypedDict):
    InsightId: str
    StartTime: datetime
    EndTime: datetime
    ServiceGraphStartTime: datetime
    ServiceGraphEndTime: datetime
    Services: List[InsightImpactGraphServiceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ResponseTimeRootCauseTypeDef(TypedDict):
    Services: NotRequired[List[ResponseTimeRootCauseServiceTypeDef]]
    ClientImpacting: NotRequired[bool]

class ListRetrievedTracesResultTypeDef(TypedDict):
    RetrievalStatus: RetrievalStatusType
    TraceFormat: TraceFormatTypeType
    Traces: List[RetrievedTraceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateSamplingRuleResultTypeDef(TypedDict):
    SamplingRuleRecord: SamplingRuleRecordTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSamplingRuleResultTypeDef(TypedDict):
    SamplingRuleRecord: SamplingRuleRecordTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSamplingRulesResultTypeDef(TypedDict):
    SamplingRuleRecords: List[SamplingRuleRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateSamplingRuleResultTypeDef(TypedDict):
    SamplingRuleRecord: SamplingRuleRecordTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSamplingRuleRequestTypeDef(TypedDict):
    SamplingRule: SamplingRuleUnionTypeDef
    Tags: NotRequired[Sequence[TagTypeDef]]

class BatchGetTracesResultTypeDef(TypedDict):
    Traces: List[TraceTypeDef]
    UnprocessedTraceIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetInsightEventsResultTypeDef(TypedDict):
    InsightEvents: List[InsightEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetInsightSummariesResultTypeDef(TypedDict):
    InsightSummaries: List[InsightSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetInsightResultTypeDef(TypedDict):
    Insight: InsightTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "ReferenceId": NotRequired[int],
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "Root": NotRequired[bool],
        "AccountId": NotRequired[str],
        "Type": NotRequired[str],
        "State": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Edges": NotRequired[List[EdgeTypeDef]],
        "SummaryStatistics": NotRequired[ServiceStatisticsTypeDef],
        "DurationHistogram": NotRequired[List[HistogramEntryTypeDef]],
        "ResponseTimeHistogram": NotRequired[List[HistogramEntryTypeDef]],
    },
)

class GetTimeSeriesServiceStatisticsResultTypeDef(TypedDict):
    TimeSeriesServiceStatistics: List[TimeSeriesServiceStatisticsTypeDef]
    ContainsOldGroupVersions: bool
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ErrorRootCauseTypeDef(TypedDict):
    Services: NotRequired[List[ErrorRootCauseServiceTypeDef]]
    ClientImpacting: NotRequired[bool]

class FaultRootCauseTypeDef(TypedDict):
    Services: NotRequired[List[FaultRootCauseServiceTypeDef]]
    ClientImpacting: NotRequired[bool]

class GetIndexingRulesResultTypeDef(TypedDict):
    IndexingRules: List[IndexingRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateIndexingRuleResultTypeDef(TypedDict):
    IndexingRule: IndexingRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceGraphResultTypeDef(TypedDict):
    StartTime: datetime
    EndTime: datetime
    Services: List[ServiceTypeDef]
    ContainsOldGroupVersions: bool
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetTraceGraphResultTypeDef(TypedDict):
    Services: List[ServiceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RetrievedServiceTypeDef(TypedDict):
    Service: NotRequired[ServiceTypeDef]
    Links: NotRequired[List[GraphLinkTypeDef]]

class TraceSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    StartTime: NotRequired[datetime]
    Duration: NotRequired[float]
    ResponseTime: NotRequired[float]
    HasFault: NotRequired[bool]
    HasError: NotRequired[bool]
    HasThrottle: NotRequired[bool]
    IsPartial: NotRequired[bool]
    Http: NotRequired[HttpTypeDef]
    Annotations: NotRequired[Dict[str, List[ValueWithServiceIdsTypeDef]]]
    Users: NotRequired[List[TraceUserTypeDef]]
    ServiceIds: NotRequired[List[ServiceIdTypeDef]]
    ResourceARNs: NotRequired[List[ResourceARNDetailTypeDef]]
    InstanceIds: NotRequired[List[InstanceIdDetailTypeDef]]
    AvailabilityZones: NotRequired[List[AvailabilityZoneDetailTypeDef]]
    EntryPoint: NotRequired[ServiceIdTypeDef]
    FaultRootCauses: NotRequired[List[FaultRootCauseTypeDef]]
    ErrorRootCauses: NotRequired[List[ErrorRootCauseTypeDef]]
    ResponseTimeRootCauses: NotRequired[List[ResponseTimeRootCauseTypeDef]]
    Revision: NotRequired[int]
    MatchedEventTime: NotRequired[datetime]

class GetRetrievedTracesGraphResultTypeDef(TypedDict):
    RetrievalStatus: RetrievalStatusType
    Services: List[RetrievedServiceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetTraceSummariesResultTypeDef(TypedDict):
    TraceSummaries: List[TraceSummaryTypeDef]
    ApproximateTime: datetime
    TracesProcessedCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
