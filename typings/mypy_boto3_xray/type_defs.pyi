"""
Main interface for xray service type definitions.

Usage::

    ```python
    from mypy_boto3_xray.type_defs import AliasTypeDef

    data: AliasTypeDef = {...}
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
    "AliasTypeDef",
    "AnnotationValueTypeDef",
    "AvailabilityZoneDetailTypeDef",
    "BackendConnectionErrorsTypeDef",
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
    "GroupSummaryTypeDef",
    "GroupTypeDef",
    "HistogramEntryTypeDef",
    "HttpTypeDef",
    "InstanceIdDetailTypeDef",
    "ResourceARNDetailTypeDef",
    "ResponseTimeRootCauseEntityTypeDef",
    "ResponseTimeRootCauseServiceTypeDef",
    "ResponseTimeRootCauseTypeDef",
    "RootCauseExceptionTypeDef",
    "SamplingRuleRecordTypeDef",
    "SamplingRuleTypeDef",
    "SamplingStatisticSummaryTypeDef",
    "SamplingTargetDocumentTypeDef",
    "SegmentTypeDef",
    "ServiceIdTypeDef",
    "ServiceStatisticsTypeDef",
    "ServiceTypeDef",
    "TimeSeriesServiceStatisticsTypeDef",
    "TraceSummaryTypeDef",
    "TraceTypeDef",
    "TraceUserTypeDef",
    "UnprocessedStatisticsTypeDef",
    "UnprocessedTraceSegmentTypeDef",
    "ValueWithServiceIdsTypeDef",
    "BatchGetTracesResultTypeDef",
    "CreateGroupResultTypeDef",
    "CreateSamplingRuleResultTypeDef",
    "DeleteSamplingRuleResultTypeDef",
    "GetEncryptionConfigResultTypeDef",
    "GetGroupResultTypeDef",
    "GetGroupsResultTypeDef",
    "GetSamplingRulesResultTypeDef",
    "GetSamplingStatisticSummariesResultTypeDef",
    "GetSamplingTargetsResultTypeDef",
    "GetServiceGraphResultTypeDef",
    "GetTimeSeriesServiceStatisticsResultTypeDef",
    "GetTraceGraphResultTypeDef",
    "GetTraceSummariesResultTypeDef",
    "PaginatorConfigTypeDef",
    "PutEncryptionConfigResultTypeDef",
    "PutTraceSegmentsResultTypeDef",
    "SamplingRuleUpdateTypeDef",
    "SamplingStatisticsDocumentTypeDef",
    "SamplingStrategyTypeDef",
    "TelemetryRecordTypeDef",
    "UpdateGroupResultTypeDef",
    "UpdateSamplingRuleResultTypeDef",
)

AliasTypeDef = TypedDict(
    "AliasTypeDef", {"Name": str, "Names": List[str], "Type": str}, total=False
)

AnnotationValueTypeDef = TypedDict(
    "AnnotationValueTypeDef",
    {"NumberValue": float, "BooleanValue": bool, "StringValue": str},
    total=False,
)

AvailabilityZoneDetailTypeDef = TypedDict(
    "AvailabilityZoneDetailTypeDef", {"Name": str}, total=False
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
    {"KeyId": str, "Status": Literal["UPDATING", "ACTIVE"], "Type": Literal["NONE", "KMS"]},
    total=False,
)

ErrorRootCauseEntityTypeDef = TypedDict(
    "ErrorRootCauseEntityTypeDef",
    {"Name": str, "Exceptions": List["RootCauseExceptionTypeDef"], "Remote": bool},
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
    {"Services": List["ErrorRootCauseServiceTypeDef"], "ClientImpacting": bool},
    total=False,
)

ErrorStatisticsTypeDef = TypedDict(
    "ErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

FaultRootCauseEntityTypeDef = TypedDict(
    "FaultRootCauseEntityTypeDef",
    {"Name": str, "Exceptions": List["RootCauseExceptionTypeDef"], "Remote": bool},
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
    {"Services": List["FaultRootCauseServiceTypeDef"], "ClientImpacting": bool},
    total=False,
)

FaultStatisticsTypeDef = TypedDict(
    "FaultStatisticsTypeDef", {"OtherCount": int, "TotalCount": int}, total=False
)

GroupSummaryTypeDef = TypedDict(
    "GroupSummaryTypeDef", {"GroupName": str, "GroupARN": str, "FilterExpression": str}, total=False
)

GroupTypeDef = TypedDict(
    "GroupTypeDef", {"GroupName": str, "GroupARN": str, "FilterExpression": str}, total=False
)

HistogramEntryTypeDef = TypedDict(
    "HistogramEntryTypeDef", {"Value": float, "Count": int}, total=False
)

HttpTypeDef = TypedDict(
    "HttpTypeDef",
    {"HttpURL": str, "HttpStatus": int, "HttpMethod": str, "UserAgent": str, "ClientIp": str},
    total=False,
)

InstanceIdDetailTypeDef = TypedDict("InstanceIdDetailTypeDef", {"Id": str}, total=False)

ResourceARNDetailTypeDef = TypedDict("ResourceARNDetailTypeDef", {"ARN": str}, total=False)

ResponseTimeRootCauseEntityTypeDef = TypedDict(
    "ResponseTimeRootCauseEntityTypeDef",
    {"Name": str, "Coverage": float, "Remote": bool},
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
    {"Services": List["ResponseTimeRootCauseServiceTypeDef"], "ClientImpacting": bool},
    total=False,
)

RootCauseExceptionTypeDef = TypedDict(
    "RootCauseExceptionTypeDef", {"Name": str, "Message": str}, total=False
)

SamplingRuleRecordTypeDef = TypedDict(
    "SamplingRuleRecordTypeDef",
    {"SamplingRule": "SamplingRuleTypeDef", "CreatedAt": datetime, "ModifiedAt": datetime},
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
    {"RuleName": str, "RuleARN": str, "Attributes": Dict[str, str]},
    total=False,
)


class SamplingRuleTypeDef(_RequiredSamplingRuleTypeDef, _OptionalSamplingRuleTypeDef):
    pass


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

SegmentTypeDef = TypedDict("SegmentTypeDef", {"Id": str, "Document": str}, total=False)

ServiceIdTypeDef = TypedDict(
    "ServiceIdTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
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

TimeSeriesServiceStatisticsTypeDef = TypedDict(
    "TimeSeriesServiceStatisticsTypeDef",
    {
        "Timestamp": datetime,
        "EdgeSummaryStatistics": "EdgeStatisticsTypeDef",
        "ServiceSummaryStatistics": "ServiceStatisticsTypeDef",
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
    "TraceTypeDef", {"Id": str, "Duration": float, "Segments": List["SegmentTypeDef"]}, total=False
)

TraceUserTypeDef = TypedDict(
    "TraceUserTypeDef", {"UserName": str, "ServiceIds": List["ServiceIdTypeDef"]}, total=False
)

UnprocessedStatisticsTypeDef = TypedDict(
    "UnprocessedStatisticsTypeDef", {"RuleName": str, "ErrorCode": str, "Message": str}, total=False
)

UnprocessedTraceSegmentTypeDef = TypedDict(
    "UnprocessedTraceSegmentTypeDef", {"Id": str, "ErrorCode": str, "Message": str}, total=False
)

ValueWithServiceIdsTypeDef = TypedDict(
    "ValueWithServiceIdsTypeDef",
    {"AnnotationValue": "AnnotationValueTypeDef", "ServiceIds": List["ServiceIdTypeDef"]},
    total=False,
)

BatchGetTracesResultTypeDef = TypedDict(
    "BatchGetTracesResultTypeDef",
    {"Traces": List["TraceTypeDef"], "UnprocessedTraceIds": List[str], "NextToken": str},
    total=False,
)

CreateGroupResultTypeDef = TypedDict(
    "CreateGroupResultTypeDef", {"Group": "GroupTypeDef"}, total=False
)

CreateSamplingRuleResultTypeDef = TypedDict(
    "CreateSamplingRuleResultTypeDef",
    {"SamplingRuleRecord": "SamplingRuleRecordTypeDef"},
    total=False,
)

DeleteSamplingRuleResultTypeDef = TypedDict(
    "DeleteSamplingRuleResultTypeDef",
    {"SamplingRuleRecord": "SamplingRuleRecordTypeDef"},
    total=False,
)

GetEncryptionConfigResultTypeDef = TypedDict(
    "GetEncryptionConfigResultTypeDef", {"EncryptionConfig": "EncryptionConfigTypeDef"}, total=False
)

GetGroupResultTypeDef = TypedDict("GetGroupResultTypeDef", {"Group": "GroupTypeDef"}, total=False)

GetGroupsResultTypeDef = TypedDict(
    "GetGroupsResultTypeDef", {"Groups": List["GroupSummaryTypeDef"], "NextToken": str}, total=False
)

GetSamplingRulesResultTypeDef = TypedDict(
    "GetSamplingRulesResultTypeDef",
    {"SamplingRuleRecords": List["SamplingRuleRecordTypeDef"], "NextToken": str},
    total=False,
)

GetSamplingStatisticSummariesResultTypeDef = TypedDict(
    "GetSamplingStatisticSummariesResultTypeDef",
    {"SamplingStatisticSummaries": List["SamplingStatisticSummaryTypeDef"], "NextToken": str},
    total=False,
)

GetSamplingTargetsResultTypeDef = TypedDict(
    "GetSamplingTargetsResultTypeDef",
    {
        "SamplingTargetDocuments": List["SamplingTargetDocumentTypeDef"],
        "LastRuleModification": datetime,
        "UnprocessedStatistics": List["UnprocessedStatisticsTypeDef"],
    },
    total=False,
)

GetServiceGraphResultTypeDef = TypedDict(
    "GetServiceGraphResultTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "Services": List["ServiceTypeDef"],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
    },
    total=False,
)

GetTimeSeriesServiceStatisticsResultTypeDef = TypedDict(
    "GetTimeSeriesServiceStatisticsResultTypeDef",
    {
        "TimeSeriesServiceStatistics": List["TimeSeriesServiceStatisticsTypeDef"],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
    },
    total=False,
)

GetTraceGraphResultTypeDef = TypedDict(
    "GetTraceGraphResultTypeDef",
    {"Services": List["ServiceTypeDef"], "NextToken": str},
    total=False,
)

GetTraceSummariesResultTypeDef = TypedDict(
    "GetTraceSummariesResultTypeDef",
    {
        "TraceSummaries": List["TraceSummaryTypeDef"],
        "ApproximateTime": datetime,
        "TracesProcessedCount": int,
        "NextToken": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutEncryptionConfigResultTypeDef = TypedDict(
    "PutEncryptionConfigResultTypeDef", {"EncryptionConfig": "EncryptionConfigTypeDef"}, total=False
)

PutTraceSegmentsResultTypeDef = TypedDict(
    "PutTraceSegmentsResultTypeDef",
    {"UnprocessedTraceSegments": List["UnprocessedTraceSegmentTypeDef"]},
    total=False,
)

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

_RequiredSamplingStatisticsDocumentTypeDef = TypedDict(
    "_RequiredSamplingStatisticsDocumentTypeDef",
    {
        "RuleName": str,
        "ClientID": str,
        "Timestamp": datetime,
        "RequestCount": int,
        "SampledCount": int,
    },
)
_OptionalSamplingStatisticsDocumentTypeDef = TypedDict(
    "_OptionalSamplingStatisticsDocumentTypeDef", {"BorrowCount": int}, total=False
)


class SamplingStatisticsDocumentTypeDef(
    _RequiredSamplingStatisticsDocumentTypeDef, _OptionalSamplingStatisticsDocumentTypeDef
):
    pass


SamplingStrategyTypeDef = TypedDict(
    "SamplingStrategyTypeDef",
    {"Name": Literal["PartialScan", "FixedRate"], "Value": float},
    total=False,
)

_RequiredTelemetryRecordTypeDef = TypedDict(
    "_RequiredTelemetryRecordTypeDef", {"Timestamp": datetime}
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


UpdateGroupResultTypeDef = TypedDict(
    "UpdateGroupResultTypeDef", {"Group": "GroupTypeDef"}, total=False
)

UpdateSamplingRuleResultTypeDef = TypedDict(
    "UpdateSamplingRuleResultTypeDef",
    {"SamplingRuleRecord": "SamplingRuleRecordTypeDef"},
    total=False,
)
