"""
Type annotations for timestream-query service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_timestream_query.type_defs import SnsConfigurationTypeDef

    data: SnsConfigurationTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    ComputeModeType,
    LastUpdateStatusType,
    MeasureValueTypeType,
    QueryInsightsModeType,
    QueryPricingModelType,
    S3EncryptionOptionType,
    ScalarMeasureValueTypeType,
    ScalarTypeType,
    ScheduledQueryInsightsModeType,
    ScheduledQueryRunStatusType,
    ScheduledQueryStateType,
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
    "AccountSettingsNotificationConfigurationTypeDef",
    "CancelQueryRequestTypeDef",
    "CancelQueryResponseTypeDef",
    "ColumnInfoPaginatorTypeDef",
    "ColumnInfoTypeDef",
    "CreateScheduledQueryRequestTypeDef",
    "CreateScheduledQueryResponseTypeDef",
    "DatumPaginatorTypeDef",
    "DatumTypeDef",
    "DeleteScheduledQueryRequestTypeDef",
    "DescribeAccountSettingsResponseTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeScheduledQueryRequestTypeDef",
    "DescribeScheduledQueryResponseTypeDef",
    "DimensionMappingTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EndpointTypeDef",
    "ErrorReportConfigurationTypeDef",
    "ErrorReportLocationTypeDef",
    "ExecuteScheduledQueryRequestTypeDef",
    "ExecutionStatsTypeDef",
    "LastUpdateTypeDef",
    "ListScheduledQueriesRequestPaginateTypeDef",
    "ListScheduledQueriesRequestTypeDef",
    "ListScheduledQueriesResponseTypeDef",
    "ListTagsForResourceRequestPaginateTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MixedMeasureMappingOutputTypeDef",
    "MixedMeasureMappingTypeDef",
    "MultiMeasureAttributeMappingTypeDef",
    "MultiMeasureMappingsOutputTypeDef",
    "MultiMeasureMappingsTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterMappingTypeDef",
    "PrepareQueryRequestTypeDef",
    "PrepareQueryResponseTypeDef",
    "ProvisionedCapacityRequestTypeDef",
    "ProvisionedCapacityResponseTypeDef",
    "QueryComputeRequestTypeDef",
    "QueryComputeResponseTypeDef",
    "QueryInsightsResponseTypeDef",
    "QueryInsightsTypeDef",
    "QueryRequestPaginateTypeDef",
    "QueryRequestTypeDef",
    "QueryResponsePaginatorTypeDef",
    "QueryResponseTypeDef",
    "QuerySpatialCoverageMaxTypeDef",
    "QuerySpatialCoverageTypeDef",
    "QueryStatusTypeDef",
    "QueryTemporalRangeMaxTypeDef",
    "QueryTemporalRangeTypeDef",
    "ResponseMetadataTypeDef",
    "RowPaginatorTypeDef",
    "RowTypeDef",
    "S3ConfigurationTypeDef",
    "S3ReportLocationTypeDef",
    "ScheduleConfigurationTypeDef",
    "ScheduledQueryDescriptionTypeDef",
    "ScheduledQueryInsightsResponseTypeDef",
    "ScheduledQueryInsightsTypeDef",
    "ScheduledQueryRunSummaryTypeDef",
    "ScheduledQueryTypeDef",
    "SelectColumnTypeDef",
    "SnsConfigurationTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TargetConfigurationOutputTypeDef",
    "TargetConfigurationTypeDef",
    "TargetConfigurationUnionTypeDef",
    "TargetDestinationTypeDef",
    "TimeSeriesDataPointPaginatorTypeDef",
    "TimeSeriesDataPointTypeDef",
    "TimestampTypeDef",
    "TimestreamConfigurationOutputTypeDef",
    "TimestreamConfigurationTypeDef",
    "TimestreamDestinationTypeDef",
    "TypePaginatorTypeDef",
    "TypeTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAccountSettingsRequestTypeDef",
    "UpdateAccountSettingsResponseTypeDef",
    "UpdateScheduledQueryRequestTypeDef",
)

class SnsConfigurationTypeDef(TypedDict):
    TopicArn: str

class CancelQueryRequestTypeDef(TypedDict):
    QueryId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class TypePaginatorTypeDef(TypedDict):
    ScalarType: NotRequired[ScalarTypeType]
    ArrayColumnInfo: NotRequired[Dict[str, Any]]
    TimeSeriesMeasureValueColumnInfo: NotRequired[Dict[str, Any]]
    RowColumnInfo: NotRequired[List[Dict[str, Any]]]

ColumnInfoTypeDef = TypedDict(
    "ColumnInfoTypeDef",
    {
        "Type": Dict[str, Any],
        "Name": NotRequired[str],
    },
)

class ScheduleConfigurationTypeDef(TypedDict):
    ScheduleExpression: str

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class TimeSeriesDataPointPaginatorTypeDef(TypedDict):
    Time: str
    Value: Dict[str, Any]

class TimeSeriesDataPointTypeDef(TypedDict):
    Time: str
    Value: Dict[str, Any]

class DeleteScheduledQueryRequestTypeDef(TypedDict):
    ScheduledQueryArn: str

class EndpointTypeDef(TypedDict):
    Address: str
    CachePeriodInMinutes: int

class DescribeScheduledQueryRequestTypeDef(TypedDict):
    ScheduledQueryArn: str

class DimensionMappingTypeDef(TypedDict):
    Name: str
    DimensionValueType: Literal["VARCHAR"]

class S3ConfigurationTypeDef(TypedDict):
    BucketName: str
    ObjectKeyPrefix: NotRequired[str]
    EncryptionOption: NotRequired[S3EncryptionOptionType]

class S3ReportLocationTypeDef(TypedDict):
    BucketName: NotRequired[str]
    ObjectKey: NotRequired[str]

class ScheduledQueryInsightsTypeDef(TypedDict):
    Mode: ScheduledQueryInsightsModeType

TimestampTypeDef = Union[datetime, str]

class ExecutionStatsTypeDef(TypedDict):
    ExecutionTimeInMillis: NotRequired[int]
    DataWrites: NotRequired[int]
    BytesMetered: NotRequired[int]
    CumulativeBytesScanned: NotRequired[int]
    RecordsIngested: NotRequired[int]
    QueryResultRows: NotRequired[int]

class LastUpdateTypeDef(TypedDict):
    TargetQueryTCU: NotRequired[int]
    Status: NotRequired[LastUpdateStatusType]
    StatusMessage: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListScheduledQueriesRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class MultiMeasureAttributeMappingTypeDef(TypedDict):
    SourceColumn: str
    MeasureValueType: ScalarMeasureValueTypeType
    TargetMultiMeasureAttributeName: NotRequired[str]

class PrepareQueryRequestTypeDef(TypedDict):
    QueryString: str
    ValidateOnly: NotRequired[bool]

class QueryInsightsTypeDef(TypedDict):
    Mode: QueryInsightsModeType

class QueryStatusTypeDef(TypedDict):
    ProgressPercentage: NotRequired[float]
    CumulativeBytesScanned: NotRequired[int]
    CumulativeBytesMetered: NotRequired[int]

class QuerySpatialCoverageMaxTypeDef(TypedDict):
    Value: NotRequired[float]
    TableArn: NotRequired[str]
    PartitionKey: NotRequired[List[str]]

class QueryTemporalRangeMaxTypeDef(TypedDict):
    Value: NotRequired[int]
    TableArn: NotRequired[str]

class TimestreamDestinationTypeDef(TypedDict):
    DatabaseName: NotRequired[str]
    TableName: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateScheduledQueryRequestTypeDef(TypedDict):
    ScheduledQueryArn: str
    State: ScheduledQueryStateType

class AccountSettingsNotificationConfigurationTypeDef(TypedDict):
    RoleArn: str
    SnsConfiguration: NotRequired[SnsConfigurationTypeDef]

class NotificationConfigurationTypeDef(TypedDict):
    SnsConfiguration: SnsConfigurationTypeDef

class CancelQueryResponseTypeDef(TypedDict):
    CancellationMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateScheduledQueryResponseTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

ColumnInfoPaginatorTypeDef = TypedDict(
    "ColumnInfoPaginatorTypeDef",
    {
        "Type": TypePaginatorTypeDef,
        "Name": NotRequired[str],
    },
)

class TypeTypeDef(TypedDict):
    ScalarType: NotRequired[ScalarTypeType]
    ArrayColumnInfo: NotRequired[Dict[str, Any]]
    TimeSeriesMeasureValueColumnInfo: NotRequired[Dict[str, Any]]
    RowColumnInfo: NotRequired[List[ColumnInfoTypeDef]]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class DatumPaginatorTypeDef(TypedDict):
    ScalarValue: NotRequired[str]
    TimeSeriesValue: NotRequired[List[TimeSeriesDataPointPaginatorTypeDef]]
    ArrayValue: NotRequired[List[Dict[str, Any]]]
    RowValue: NotRequired[Dict[str, Any]]
    NullValue: NotRequired[bool]

class DatumTypeDef(TypedDict):
    ScalarValue: NotRequired[str]
    TimeSeriesValue: NotRequired[List[TimeSeriesDataPointTypeDef]]
    ArrayValue: NotRequired[List[Dict[str, Any]]]
    RowValue: NotRequired[Dict[str, Any]]
    NullValue: NotRequired[bool]

class DescribeEndpointsResponseTypeDef(TypedDict):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ErrorReportConfigurationTypeDef(TypedDict):
    S3Configuration: S3ConfigurationTypeDef

class ErrorReportLocationTypeDef(TypedDict):
    S3ReportLocation: NotRequired[S3ReportLocationTypeDef]

class ExecuteScheduledQueryRequestTypeDef(TypedDict):
    ScheduledQueryArn: str
    InvocationTime: TimestampTypeDef
    ClientToken: NotRequired[str]
    QueryInsights: NotRequired[ScheduledQueryInsightsTypeDef]

class ListScheduledQueriesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceRequestPaginateTypeDef(TypedDict):
    ResourceARN: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class MixedMeasureMappingOutputTypeDef(TypedDict):
    MeasureValueType: MeasureValueTypeType
    MeasureName: NotRequired[str]
    SourceColumn: NotRequired[str]
    TargetMeasureName: NotRequired[str]
    MultiMeasureAttributeMappings: NotRequired[List[MultiMeasureAttributeMappingTypeDef]]

class MixedMeasureMappingTypeDef(TypedDict):
    MeasureValueType: MeasureValueTypeType
    MeasureName: NotRequired[str]
    SourceColumn: NotRequired[str]
    TargetMeasureName: NotRequired[str]
    MultiMeasureAttributeMappings: NotRequired[Sequence[MultiMeasureAttributeMappingTypeDef]]

class MultiMeasureMappingsOutputTypeDef(TypedDict):
    MultiMeasureAttributeMappings: List[MultiMeasureAttributeMappingTypeDef]
    TargetMultiMeasureName: NotRequired[str]

class MultiMeasureMappingsTypeDef(TypedDict):
    MultiMeasureAttributeMappings: Sequence[MultiMeasureAttributeMappingTypeDef]
    TargetMultiMeasureName: NotRequired[str]

class QueryRequestPaginateTypeDef(TypedDict):
    QueryString: str
    ClientToken: NotRequired[str]
    QueryInsights: NotRequired[QueryInsightsTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class QueryRequestTypeDef(TypedDict):
    QueryString: str
    ClientToken: NotRequired[str]
    NextToken: NotRequired[str]
    MaxRows: NotRequired[int]
    QueryInsights: NotRequired[QueryInsightsTypeDef]

class QuerySpatialCoverageTypeDef(TypedDict):
    Max: NotRequired[QuerySpatialCoverageMaxTypeDef]

class QueryTemporalRangeTypeDef(TypedDict):
    Max: NotRequired[QueryTemporalRangeMaxTypeDef]

class TargetDestinationTypeDef(TypedDict):
    TimestreamDestination: NotRequired[TimestreamDestinationTypeDef]

class ProvisionedCapacityRequestTypeDef(TypedDict):
    TargetQueryTCU: int
    NotificationConfiguration: NotRequired[AccountSettingsNotificationConfigurationTypeDef]

class ProvisionedCapacityResponseTypeDef(TypedDict):
    ActiveQueryTCU: NotRequired[int]
    NotificationConfiguration: NotRequired[AccountSettingsNotificationConfigurationTypeDef]
    LastUpdate: NotRequired[LastUpdateTypeDef]

ParameterMappingTypeDef = TypedDict(
    "ParameterMappingTypeDef",
    {
        "Name": str,
        "Type": TypeTypeDef,
    },
)
SelectColumnTypeDef = TypedDict(
    "SelectColumnTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[TypeTypeDef],
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
        "Aliased": NotRequired[bool],
    },
)

class RowPaginatorTypeDef(TypedDict):
    Data: List[DatumPaginatorTypeDef]

class RowTypeDef(TypedDict):
    Data: List[DatumTypeDef]

class TimestreamConfigurationOutputTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    TimeColumn: str
    DimensionMappings: List[DimensionMappingTypeDef]
    MultiMeasureMappings: NotRequired[MultiMeasureMappingsOutputTypeDef]
    MixedMeasureMappings: NotRequired[List[MixedMeasureMappingOutputTypeDef]]
    MeasureNameColumn: NotRequired[str]

class TimestreamConfigurationTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    TimeColumn: str
    DimensionMappings: Sequence[DimensionMappingTypeDef]
    MultiMeasureMappings: NotRequired[MultiMeasureMappingsTypeDef]
    MixedMeasureMappings: NotRequired[Sequence[MixedMeasureMappingTypeDef]]
    MeasureNameColumn: NotRequired[str]

class QueryInsightsResponseTypeDef(TypedDict):
    QuerySpatialCoverage: NotRequired[QuerySpatialCoverageTypeDef]
    QueryTemporalRange: NotRequired[QueryTemporalRangeTypeDef]
    QueryTableCount: NotRequired[int]
    OutputRows: NotRequired[int]
    OutputBytes: NotRequired[int]
    UnloadPartitionCount: NotRequired[int]
    UnloadWrittenRows: NotRequired[int]
    UnloadWrittenBytes: NotRequired[int]

class ScheduledQueryInsightsResponseTypeDef(TypedDict):
    QuerySpatialCoverage: NotRequired[QuerySpatialCoverageTypeDef]
    QueryTemporalRange: NotRequired[QueryTemporalRangeTypeDef]
    QueryTableCount: NotRequired[int]
    OutputRows: NotRequired[int]
    OutputBytes: NotRequired[int]

class ScheduledQueryTypeDef(TypedDict):
    Arn: str
    Name: str
    State: ScheduledQueryStateType
    CreationTime: NotRequired[datetime]
    PreviousInvocationTime: NotRequired[datetime]
    NextInvocationTime: NotRequired[datetime]
    ErrorReportConfiguration: NotRequired[ErrorReportConfigurationTypeDef]
    TargetDestination: NotRequired[TargetDestinationTypeDef]
    LastRunStatus: NotRequired[ScheduledQueryRunStatusType]

class QueryComputeRequestTypeDef(TypedDict):
    ComputeMode: NotRequired[ComputeModeType]
    ProvisionedCapacity: NotRequired[ProvisionedCapacityRequestTypeDef]

class QueryComputeResponseTypeDef(TypedDict):
    ComputeMode: NotRequired[ComputeModeType]
    ProvisionedCapacity: NotRequired[ProvisionedCapacityResponseTypeDef]

class PrepareQueryResponseTypeDef(TypedDict):
    QueryString: str
    Columns: List[SelectColumnTypeDef]
    Parameters: List[ParameterMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TargetConfigurationOutputTypeDef(TypedDict):
    TimestreamConfiguration: TimestreamConfigurationOutputTypeDef

class TargetConfigurationTypeDef(TypedDict):
    TimestreamConfiguration: TimestreamConfigurationTypeDef

class QueryResponsePaginatorTypeDef(TypedDict):
    QueryId: str
    Rows: List[RowPaginatorTypeDef]
    ColumnInfo: List[ColumnInfoPaginatorTypeDef]
    QueryStatus: QueryStatusTypeDef
    QueryInsightsResponse: QueryInsightsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class QueryResponseTypeDef(TypedDict):
    QueryId: str
    Rows: List[RowTypeDef]
    ColumnInfo: List[ColumnInfoTypeDef]
    QueryStatus: QueryStatusTypeDef
    QueryInsightsResponse: QueryInsightsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ScheduledQueryRunSummaryTypeDef(TypedDict):
    InvocationTime: NotRequired[datetime]
    TriggerTime: NotRequired[datetime]
    RunStatus: NotRequired[ScheduledQueryRunStatusType]
    ExecutionStats: NotRequired[ExecutionStatsTypeDef]
    QueryInsightsResponse: NotRequired[ScheduledQueryInsightsResponseTypeDef]
    ErrorReportLocation: NotRequired[ErrorReportLocationTypeDef]
    FailureReason: NotRequired[str]

class ListScheduledQueriesResponseTypeDef(TypedDict):
    ScheduledQueries: List[ScheduledQueryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateAccountSettingsRequestTypeDef(TypedDict):
    MaxQueryTCU: NotRequired[int]
    QueryPricingModel: NotRequired[QueryPricingModelType]
    QueryCompute: NotRequired[QueryComputeRequestTypeDef]

class DescribeAccountSettingsResponseTypeDef(TypedDict):
    MaxQueryTCU: int
    QueryPricingModel: QueryPricingModelType
    QueryCompute: QueryComputeResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountSettingsResponseTypeDef(TypedDict):
    MaxQueryTCU: int
    QueryPricingModel: QueryPricingModelType
    QueryCompute: QueryComputeResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

TargetConfigurationUnionTypeDef = Union[
    TargetConfigurationTypeDef, TargetConfigurationOutputTypeDef
]

class ScheduledQueryDescriptionTypeDef(TypedDict):
    Arn: str
    Name: str
    QueryString: str
    State: ScheduledQueryStateType
    ScheduleConfiguration: ScheduleConfigurationTypeDef
    NotificationConfiguration: NotificationConfigurationTypeDef
    CreationTime: NotRequired[datetime]
    PreviousInvocationTime: NotRequired[datetime]
    NextInvocationTime: NotRequired[datetime]
    TargetConfiguration: NotRequired[TargetConfigurationOutputTypeDef]
    ScheduledQueryExecutionRoleArn: NotRequired[str]
    KmsKeyId: NotRequired[str]
    ErrorReportConfiguration: NotRequired[ErrorReportConfigurationTypeDef]
    LastRunSummary: NotRequired[ScheduledQueryRunSummaryTypeDef]
    RecentlyFailedRuns: NotRequired[List[ScheduledQueryRunSummaryTypeDef]]

class CreateScheduledQueryRequestTypeDef(TypedDict):
    Name: str
    QueryString: str
    ScheduleConfiguration: ScheduleConfigurationTypeDef
    NotificationConfiguration: NotificationConfigurationTypeDef
    ScheduledQueryExecutionRoleArn: str
    ErrorReportConfiguration: ErrorReportConfigurationTypeDef
    TargetConfiguration: NotRequired[TargetConfigurationUnionTypeDef]
    ClientToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    KmsKeyId: NotRequired[str]

class DescribeScheduledQueryResponseTypeDef(TypedDict):
    ScheduledQuery: ScheduledQueryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
