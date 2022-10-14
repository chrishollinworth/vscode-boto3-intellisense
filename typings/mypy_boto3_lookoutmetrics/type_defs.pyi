"""
Type annotations for lookoutmetrics service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lookoutmetrics.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AggregationFunctionType,
    AlertStatusType,
    AlertTypeType,
    AnomalyDetectionTaskStatusType,
    AnomalyDetectorFailureTypeType,
    AnomalyDetectorStatusType,
    ConfidenceType,
    CSVFileCompressionType,
    DataQualityMetricTypeType,
    FrequencyType,
    JsonFileCompressionType,
    RelationshipTypeType,
    SnsFormatType,
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
    "ActionTypeDef",
    "ActivateAnomalyDetectorRequestRequestTypeDef",
    "AlertFiltersTypeDef",
    "AlertSummaryTypeDef",
    "AlertTypeDef",
    "AnomalyDetectorConfigSummaryTypeDef",
    "AnomalyDetectorConfigTypeDef",
    "AnomalyDetectorDataQualityMetricTypeDef",
    "AnomalyDetectorSummaryTypeDef",
    "AnomalyGroupStatisticsTypeDef",
    "AnomalyGroupSummaryTypeDef",
    "AnomalyGroupTimeSeriesFeedbackTypeDef",
    "AnomalyGroupTimeSeriesTypeDef",
    "AnomalyGroupTypeDef",
    "AppFlowConfigTypeDef",
    "AthenaSourceConfigTypeDef",
    "AttributeValueTypeDef",
    "AutoDetectionMetricSourceTypeDef",
    "AutoDetectionS3SourceConfigTypeDef",
    "BackTestAnomalyDetectorRequestRequestTypeDef",
    "BackTestConfigurationTypeDef",
    "CloudWatchConfigTypeDef",
    "ContributionMatrixTypeDef",
    "CreateAlertRequestRequestTypeDef",
    "CreateAlertResponseTypeDef",
    "CreateAnomalyDetectorRequestRequestTypeDef",
    "CreateAnomalyDetectorResponseTypeDef",
    "CreateMetricSetRequestRequestTypeDef",
    "CreateMetricSetResponseTypeDef",
    "CsvFormatDescriptorTypeDef",
    "DataQualityMetricTypeDef",
    "DeactivateAnomalyDetectorRequestRequestTypeDef",
    "DeleteAlertRequestRequestTypeDef",
    "DeleteAnomalyDetectorRequestRequestTypeDef",
    "DescribeAlertRequestRequestTypeDef",
    "DescribeAlertResponseTypeDef",
    "DescribeAnomalyDetectionExecutionsRequestRequestTypeDef",
    "DescribeAnomalyDetectionExecutionsResponseTypeDef",
    "DescribeAnomalyDetectorRequestRequestTypeDef",
    "DescribeAnomalyDetectorResponseTypeDef",
    "DescribeMetricSetRequestRequestTypeDef",
    "DescribeMetricSetResponseTypeDef",
    "DetectMetricSetConfigRequestRequestTypeDef",
    "DetectMetricSetConfigResponseTypeDef",
    "DetectedCsvFormatDescriptorTypeDef",
    "DetectedFieldTypeDef",
    "DetectedFileFormatDescriptorTypeDef",
    "DetectedJsonFormatDescriptorTypeDef",
    "DetectedMetricSetConfigTypeDef",
    "DetectedMetricSourceTypeDef",
    "DetectedS3SourceConfigTypeDef",
    "DimensionContributionTypeDef",
    "DimensionFilterTypeDef",
    "DimensionNameValueTypeDef",
    "DimensionValueContributionTypeDef",
    "ExecutionStatusTypeDef",
    "FileFormatDescriptorTypeDef",
    "FilterTypeDef",
    "GetAnomalyGroupRequestRequestTypeDef",
    "GetAnomalyGroupResponseTypeDef",
    "GetDataQualityMetricsRequestRequestTypeDef",
    "GetDataQualityMetricsResponseTypeDef",
    "GetFeedbackRequestRequestTypeDef",
    "GetFeedbackResponseTypeDef",
    "GetSampleDataRequestRequestTypeDef",
    "GetSampleDataResponseTypeDef",
    "InterMetricImpactDetailsTypeDef",
    "ItemizedMetricStatsTypeDef",
    "JsonFormatDescriptorTypeDef",
    "LambdaConfigurationTypeDef",
    "ListAlertsRequestRequestTypeDef",
    "ListAlertsResponseTypeDef",
    "ListAnomalyDetectorsRequestRequestTypeDef",
    "ListAnomalyDetectorsResponseTypeDef",
    "ListAnomalyGroupRelatedMetricsRequestRequestTypeDef",
    "ListAnomalyGroupRelatedMetricsResponseTypeDef",
    "ListAnomalyGroupSummariesRequestRequestTypeDef",
    "ListAnomalyGroupSummariesResponseTypeDef",
    "ListAnomalyGroupTimeSeriesRequestRequestTypeDef",
    "ListAnomalyGroupTimeSeriesResponseTypeDef",
    "ListMetricSetsRequestRequestTypeDef",
    "ListMetricSetsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricLevelImpactTypeDef",
    "MetricSetDataQualityMetricTypeDef",
    "MetricSetDimensionFilterTypeDef",
    "MetricSetSummaryTypeDef",
    "MetricSourceTypeDef",
    "MetricTypeDef",
    "PutFeedbackRequestRequestTypeDef",
    "RDSSourceConfigTypeDef",
    "RedshiftSourceConfigTypeDef",
    "ResponseMetadataTypeDef",
    "S3SourceConfigTypeDef",
    "SNSConfigurationTypeDef",
    "SampleDataS3SourceConfigTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TimeSeriesFeedbackTypeDef",
    "TimeSeriesTypeDef",
    "TimestampColumnTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAlertRequestRequestTypeDef",
    "UpdateAlertResponseTypeDef",
    "UpdateAnomalyDetectorRequestRequestTypeDef",
    "UpdateAnomalyDetectorResponseTypeDef",
    "UpdateMetricSetRequestRequestTypeDef",
    "UpdateMetricSetResponseTypeDef",
    "VpcConfigurationTypeDef",
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "SNSConfiguration": "SNSConfigurationTypeDef",
        "LambdaConfiguration": "LambdaConfigurationTypeDef",
    },
    total=False,
)

ActivateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "ActivateAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)

AlertFiltersTypeDef = TypedDict(
    "AlertFiltersTypeDef",
    {
        "MetricList": List[str],
        "DimensionFilterList": List["DimensionFilterTypeDef"],
    },
    total=False,
)

AlertSummaryTypeDef = TypedDict(
    "AlertSummaryTypeDef",
    {
        "AlertArn": str,
        "AnomalyDetectorArn": str,
        "AlertName": str,
        "AlertSensitivityThreshold": int,
        "AlertType": AlertTypeType,
        "AlertStatus": AlertStatusType,
        "LastModificationTime": datetime,
        "CreationTime": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)

AlertTypeDef = TypedDict(
    "AlertTypeDef",
    {
        "Action": "ActionTypeDef",
        "AlertDescription": str,
        "AlertArn": str,
        "AnomalyDetectorArn": str,
        "AlertName": str,
        "AlertSensitivityThreshold": int,
        "AlertType": AlertTypeType,
        "AlertStatus": AlertStatusType,
        "LastModificationTime": datetime,
        "CreationTime": datetime,
        "AlertFilters": "AlertFiltersTypeDef",
    },
    total=False,
)

AnomalyDetectorConfigSummaryTypeDef = TypedDict(
    "AnomalyDetectorConfigSummaryTypeDef",
    {
        "AnomalyDetectorFrequency": FrequencyType,
    },
    total=False,
)

AnomalyDetectorConfigTypeDef = TypedDict(
    "AnomalyDetectorConfigTypeDef",
    {
        "AnomalyDetectorFrequency": FrequencyType,
    },
    total=False,
)

AnomalyDetectorDataQualityMetricTypeDef = TypedDict(
    "AnomalyDetectorDataQualityMetricTypeDef",
    {
        "StartTimestamp": datetime,
        "MetricSetDataQualityMetricList": List["MetricSetDataQualityMetricTypeDef"],
    },
    total=False,
)

AnomalyDetectorSummaryTypeDef = TypedDict(
    "AnomalyDetectorSummaryTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyDetectorName": str,
        "AnomalyDetectorDescription": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Status": AnomalyDetectorStatusType,
        "Tags": Dict[str, str],
    },
    total=False,
)

AnomalyGroupStatisticsTypeDef = TypedDict(
    "AnomalyGroupStatisticsTypeDef",
    {
        "EvaluationStartDate": str,
        "TotalCount": int,
        "ItemizedMetricStatsList": List["ItemizedMetricStatsTypeDef"],
    },
    total=False,
)

AnomalyGroupSummaryTypeDef = TypedDict(
    "AnomalyGroupSummaryTypeDef",
    {
        "StartTime": str,
        "EndTime": str,
        "AnomalyGroupId": str,
        "AnomalyGroupScore": float,
        "PrimaryMetricName": str,
    },
    total=False,
)

AnomalyGroupTimeSeriesFeedbackTypeDef = TypedDict(
    "AnomalyGroupTimeSeriesFeedbackTypeDef",
    {
        "AnomalyGroupId": str,
        "TimeSeriesId": str,
        "IsAnomaly": bool,
    },
)

_RequiredAnomalyGroupTimeSeriesTypeDef = TypedDict(
    "_RequiredAnomalyGroupTimeSeriesTypeDef",
    {
        "AnomalyGroupId": str,
    },
)
_OptionalAnomalyGroupTimeSeriesTypeDef = TypedDict(
    "_OptionalAnomalyGroupTimeSeriesTypeDef",
    {
        "TimeSeriesId": str,
    },
    total=False,
)

class AnomalyGroupTimeSeriesTypeDef(
    _RequiredAnomalyGroupTimeSeriesTypeDef, _OptionalAnomalyGroupTimeSeriesTypeDef
):
    pass

AnomalyGroupTypeDef = TypedDict(
    "AnomalyGroupTypeDef",
    {
        "StartTime": str,
        "EndTime": str,
        "AnomalyGroupId": str,
        "AnomalyGroupScore": float,
        "PrimaryMetricName": str,
        "MetricLevelImpactList": List["MetricLevelImpactTypeDef"],
    },
    total=False,
)

AppFlowConfigTypeDef = TypedDict(
    "AppFlowConfigTypeDef",
    {
        "RoleArn": str,
        "FlowName": str,
    },
    total=False,
)

AthenaSourceConfigTypeDef = TypedDict(
    "AthenaSourceConfigTypeDef",
    {
        "RoleArn": str,
        "DatabaseName": str,
        "DataCatalog": str,
        "TableName": str,
        "WorkGroupName": str,
        "S3ResultsPath": str,
        "BackTestConfiguration": "BackTestConfigurationTypeDef",
    },
    total=False,
)

AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "S": str,
        "N": str,
        "B": str,
        "SS": List[str],
        "NS": List[str],
        "BS": List[str],
    },
    total=False,
)

AutoDetectionMetricSourceTypeDef = TypedDict(
    "AutoDetectionMetricSourceTypeDef",
    {
        "S3SourceConfig": "AutoDetectionS3SourceConfigTypeDef",
    },
    total=False,
)

AutoDetectionS3SourceConfigTypeDef = TypedDict(
    "AutoDetectionS3SourceConfigTypeDef",
    {
        "TemplatedPathList": List[str],
        "HistoricalDataPathList": List[str],
    },
    total=False,
)

BackTestAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "BackTestAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)

BackTestConfigurationTypeDef = TypedDict(
    "BackTestConfigurationTypeDef",
    {
        "RunBackTestMode": bool,
    },
)

CloudWatchConfigTypeDef = TypedDict(
    "CloudWatchConfigTypeDef",
    {
        "RoleArn": str,
        "BackTestConfiguration": "BackTestConfigurationTypeDef",
    },
    total=False,
)

ContributionMatrixTypeDef = TypedDict(
    "ContributionMatrixTypeDef",
    {
        "DimensionContributionList": List["DimensionContributionTypeDef"],
    },
    total=False,
)

_RequiredCreateAlertRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAlertRequestRequestTypeDef",
    {
        "AlertName": str,
        "AnomalyDetectorArn": str,
        "Action": "ActionTypeDef",
    },
)
_OptionalCreateAlertRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAlertRequestRequestTypeDef",
    {
        "AlertSensitivityThreshold": int,
        "AlertDescription": str,
        "Tags": Dict[str, str],
        "AlertFilters": "AlertFiltersTypeDef",
    },
    total=False,
)

class CreateAlertRequestRequestTypeDef(
    _RequiredCreateAlertRequestRequestTypeDef, _OptionalCreateAlertRequestRequestTypeDef
):
    pass

CreateAlertResponseTypeDef = TypedDict(
    "CreateAlertResponseTypeDef",
    {
        "AlertArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorName": str,
        "AnomalyDetectorConfig": "AnomalyDetectorConfigTypeDef",
    },
)
_OptionalCreateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorDescription": str,
        "KmsKeyArn": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateAnomalyDetectorRequestRequestTypeDef(
    _RequiredCreateAnomalyDetectorRequestRequestTypeDef,
    _OptionalCreateAnomalyDetectorRequestRequestTypeDef,
):
    pass

CreateAnomalyDetectorResponseTypeDef = TypedDict(
    "CreateAnomalyDetectorResponseTypeDef",
    {
        "AnomalyDetectorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMetricSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMetricSetRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "MetricSetName": str,
        "MetricList": List["MetricTypeDef"],
        "MetricSource": "MetricSourceTypeDef",
    },
)
_OptionalCreateMetricSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMetricSetRequestRequestTypeDef",
    {
        "MetricSetDescription": str,
        "Offset": int,
        "TimestampColumn": "TimestampColumnTypeDef",
        "DimensionList": List[str],
        "MetricSetFrequency": FrequencyType,
        "Timezone": str,
        "Tags": Dict[str, str],
        "DimensionFilterList": List["MetricSetDimensionFilterTypeDef"],
    },
    total=False,
)

class CreateMetricSetRequestRequestTypeDef(
    _RequiredCreateMetricSetRequestRequestTypeDef, _OptionalCreateMetricSetRequestRequestTypeDef
):
    pass

CreateMetricSetResponseTypeDef = TypedDict(
    "CreateMetricSetResponseTypeDef",
    {
        "MetricSetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CsvFormatDescriptorTypeDef = TypedDict(
    "CsvFormatDescriptorTypeDef",
    {
        "FileCompression": CSVFileCompressionType,
        "Charset": str,
        "ContainsHeader": bool,
        "Delimiter": str,
        "HeaderList": List[str],
        "QuoteSymbol": str,
    },
    total=False,
)

DataQualityMetricTypeDef = TypedDict(
    "DataQualityMetricTypeDef",
    {
        "MetricType": DataQualityMetricTypeType,
        "MetricDescription": str,
        "RelatedColumnName": str,
        "MetricValue": float,
    },
    total=False,
)

DeactivateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "DeactivateAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)

DeleteAlertRequestRequestTypeDef = TypedDict(
    "DeleteAlertRequestRequestTypeDef",
    {
        "AlertArn": str,
    },
)

DeleteAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "DeleteAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)

DescribeAlertRequestRequestTypeDef = TypedDict(
    "DescribeAlertRequestRequestTypeDef",
    {
        "AlertArn": str,
    },
)

DescribeAlertResponseTypeDef = TypedDict(
    "DescribeAlertResponseTypeDef",
    {
        "Alert": "AlertTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAnomalyDetectionExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAnomalyDetectionExecutionsRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)
_OptionalDescribeAnomalyDetectionExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAnomalyDetectionExecutionsRequestRequestTypeDef",
    {
        "Timestamp": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeAnomalyDetectionExecutionsRequestRequestTypeDef(
    _RequiredDescribeAnomalyDetectionExecutionsRequestRequestTypeDef,
    _OptionalDescribeAnomalyDetectionExecutionsRequestRequestTypeDef,
):
    pass

DescribeAnomalyDetectionExecutionsResponseTypeDef = TypedDict(
    "DescribeAnomalyDetectionExecutionsResponseTypeDef",
    {
        "ExecutionList": List["ExecutionStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "DescribeAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)

DescribeAnomalyDetectorResponseTypeDef = TypedDict(
    "DescribeAnomalyDetectorResponseTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyDetectorName": str,
        "AnomalyDetectorDescription": str,
        "AnomalyDetectorConfig": "AnomalyDetectorConfigSummaryTypeDef",
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Status": AnomalyDetectorStatusType,
        "FailureReason": str,
        "KmsKeyArn": str,
        "FailureType": AnomalyDetectorFailureTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMetricSetRequestRequestTypeDef = TypedDict(
    "DescribeMetricSetRequestRequestTypeDef",
    {
        "MetricSetArn": str,
    },
)

DescribeMetricSetResponseTypeDef = TypedDict(
    "DescribeMetricSetResponseTypeDef",
    {
        "MetricSetArn": str,
        "AnomalyDetectorArn": str,
        "MetricSetName": str,
        "MetricSetDescription": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Offset": int,
        "MetricList": List["MetricTypeDef"],
        "TimestampColumn": "TimestampColumnTypeDef",
        "DimensionList": List[str],
        "MetricSetFrequency": FrequencyType,
        "Timezone": str,
        "MetricSource": "MetricSourceTypeDef",
        "DimensionFilterList": List["MetricSetDimensionFilterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectMetricSetConfigRequestRequestTypeDef = TypedDict(
    "DetectMetricSetConfigRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AutoDetectionMetricSource": "AutoDetectionMetricSourceTypeDef",
    },
)

DetectMetricSetConfigResponseTypeDef = TypedDict(
    "DetectMetricSetConfigResponseTypeDef",
    {
        "DetectedMetricSetConfig": "DetectedMetricSetConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectedCsvFormatDescriptorTypeDef = TypedDict(
    "DetectedCsvFormatDescriptorTypeDef",
    {
        "FileCompression": "DetectedFieldTypeDef",
        "Charset": "DetectedFieldTypeDef",
        "ContainsHeader": "DetectedFieldTypeDef",
        "Delimiter": "DetectedFieldTypeDef",
        "HeaderList": "DetectedFieldTypeDef",
        "QuoteSymbol": "DetectedFieldTypeDef",
    },
    total=False,
)

DetectedFieldTypeDef = TypedDict(
    "DetectedFieldTypeDef",
    {
        "Value": "AttributeValueTypeDef",
        "Confidence": ConfidenceType,
        "Message": str,
    },
    total=False,
)

DetectedFileFormatDescriptorTypeDef = TypedDict(
    "DetectedFileFormatDescriptorTypeDef",
    {
        "CsvFormatDescriptor": "DetectedCsvFormatDescriptorTypeDef",
        "JsonFormatDescriptor": "DetectedJsonFormatDescriptorTypeDef",
    },
    total=False,
)

DetectedJsonFormatDescriptorTypeDef = TypedDict(
    "DetectedJsonFormatDescriptorTypeDef",
    {
        "FileCompression": "DetectedFieldTypeDef",
        "Charset": "DetectedFieldTypeDef",
    },
    total=False,
)

DetectedMetricSetConfigTypeDef = TypedDict(
    "DetectedMetricSetConfigTypeDef",
    {
        "Offset": "DetectedFieldTypeDef",
        "MetricSetFrequency": "DetectedFieldTypeDef",
        "MetricSource": "DetectedMetricSourceTypeDef",
    },
    total=False,
)

DetectedMetricSourceTypeDef = TypedDict(
    "DetectedMetricSourceTypeDef",
    {
        "S3SourceConfig": "DetectedS3SourceConfigTypeDef",
    },
    total=False,
)

DetectedS3SourceConfigTypeDef = TypedDict(
    "DetectedS3SourceConfigTypeDef",
    {
        "FileFormatDescriptor": "DetectedFileFormatDescriptorTypeDef",
    },
    total=False,
)

DimensionContributionTypeDef = TypedDict(
    "DimensionContributionTypeDef",
    {
        "DimensionName": str,
        "DimensionValueContributionList": List["DimensionValueContributionTypeDef"],
    },
    total=False,
)

DimensionFilterTypeDef = TypedDict(
    "DimensionFilterTypeDef",
    {
        "DimensionName": str,
        "DimensionValueList": List[str],
    },
    total=False,
)

DimensionNameValueTypeDef = TypedDict(
    "DimensionNameValueTypeDef",
    {
        "DimensionName": str,
        "DimensionValue": str,
    },
)

DimensionValueContributionTypeDef = TypedDict(
    "DimensionValueContributionTypeDef",
    {
        "DimensionValue": str,
        "ContributionScore": float,
    },
    total=False,
)

ExecutionStatusTypeDef = TypedDict(
    "ExecutionStatusTypeDef",
    {
        "Timestamp": str,
        "Status": AnomalyDetectionTaskStatusType,
        "FailureReason": str,
    },
    total=False,
)

FileFormatDescriptorTypeDef = TypedDict(
    "FileFormatDescriptorTypeDef",
    {
        "CsvFormatDescriptor": "CsvFormatDescriptorTypeDef",
        "JsonFormatDescriptor": "JsonFormatDescriptorTypeDef",
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "DimensionValue": str,
        "FilterOperation": Literal["EQUALS"],
    },
    total=False,
)

GetAnomalyGroupRequestRequestTypeDef = TypedDict(
    "GetAnomalyGroupRequestRequestTypeDef",
    {
        "AnomalyGroupId": str,
        "AnomalyDetectorArn": str,
    },
)

GetAnomalyGroupResponseTypeDef = TypedDict(
    "GetAnomalyGroupResponseTypeDef",
    {
        "AnomalyGroup": "AnomalyGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDataQualityMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredGetDataQualityMetricsRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)
_OptionalGetDataQualityMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalGetDataQualityMetricsRequestRequestTypeDef",
    {
        "MetricSetArn": str,
    },
    total=False,
)

class GetDataQualityMetricsRequestRequestTypeDef(
    _RequiredGetDataQualityMetricsRequestRequestTypeDef,
    _OptionalGetDataQualityMetricsRequestRequestTypeDef,
):
    pass

GetDataQualityMetricsResponseTypeDef = TypedDict(
    "GetDataQualityMetricsResponseTypeDef",
    {
        "AnomalyDetectorDataQualityMetricList": List["AnomalyDetectorDataQualityMetricTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFeedbackRequestRequestTypeDef = TypedDict(
    "_RequiredGetFeedbackRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyGroupTimeSeriesFeedback": "AnomalyGroupTimeSeriesTypeDef",
    },
)
_OptionalGetFeedbackRequestRequestTypeDef = TypedDict(
    "_OptionalGetFeedbackRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetFeedbackRequestRequestTypeDef(
    _RequiredGetFeedbackRequestRequestTypeDef, _OptionalGetFeedbackRequestRequestTypeDef
):
    pass

GetFeedbackResponseTypeDef = TypedDict(
    "GetFeedbackResponseTypeDef",
    {
        "AnomalyGroupTimeSeriesFeedback": List["TimeSeriesFeedbackTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSampleDataRequestRequestTypeDef = TypedDict(
    "GetSampleDataRequestRequestTypeDef",
    {
        "S3SourceConfig": "SampleDataS3SourceConfigTypeDef",
    },
    total=False,
)

GetSampleDataResponseTypeDef = TypedDict(
    "GetSampleDataResponseTypeDef",
    {
        "HeaderValues": List[str],
        "SampleRows": List[List[str]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InterMetricImpactDetailsTypeDef = TypedDict(
    "InterMetricImpactDetailsTypeDef",
    {
        "MetricName": str,
        "AnomalyGroupId": str,
        "RelationshipType": RelationshipTypeType,
        "ContributionPercentage": float,
    },
    total=False,
)

ItemizedMetricStatsTypeDef = TypedDict(
    "ItemizedMetricStatsTypeDef",
    {
        "MetricName": str,
        "OccurrenceCount": int,
    },
    total=False,
)

JsonFormatDescriptorTypeDef = TypedDict(
    "JsonFormatDescriptorTypeDef",
    {
        "FileCompression": JsonFileCompressionType,
        "Charset": str,
    },
    total=False,
)

LambdaConfigurationTypeDef = TypedDict(
    "LambdaConfigurationTypeDef",
    {
        "RoleArn": str,
        "LambdaArn": str,
    },
)

ListAlertsRequestRequestTypeDef = TypedDict(
    "ListAlertsRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListAlertsResponseTypeDef = TypedDict(
    "ListAlertsResponseTypeDef",
    {
        "AlertSummaryList": List["AlertSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAnomalyDetectorsRequestRequestTypeDef = TypedDict(
    "ListAnomalyDetectorsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListAnomalyDetectorsResponseTypeDef = TypedDict(
    "ListAnomalyDetectorsResponseTypeDef",
    {
        "AnomalyDetectorSummaryList": List["AnomalyDetectorSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAnomalyGroupRelatedMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredListAnomalyGroupRelatedMetricsRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyGroupId": str,
    },
)
_OptionalListAnomalyGroupRelatedMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalListAnomalyGroupRelatedMetricsRequestRequestTypeDef",
    {
        "RelationshipTypeFilter": RelationshipTypeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAnomalyGroupRelatedMetricsRequestRequestTypeDef(
    _RequiredListAnomalyGroupRelatedMetricsRequestRequestTypeDef,
    _OptionalListAnomalyGroupRelatedMetricsRequestRequestTypeDef,
):
    pass

ListAnomalyGroupRelatedMetricsResponseTypeDef = TypedDict(
    "ListAnomalyGroupRelatedMetricsResponseTypeDef",
    {
        "InterMetricImpactList": List["InterMetricImpactDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAnomalyGroupSummariesRequestRequestTypeDef = TypedDict(
    "_RequiredListAnomalyGroupSummariesRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "SensitivityThreshold": int,
    },
)
_OptionalListAnomalyGroupSummariesRequestRequestTypeDef = TypedDict(
    "_OptionalListAnomalyGroupSummariesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAnomalyGroupSummariesRequestRequestTypeDef(
    _RequiredListAnomalyGroupSummariesRequestRequestTypeDef,
    _OptionalListAnomalyGroupSummariesRequestRequestTypeDef,
):
    pass

ListAnomalyGroupSummariesResponseTypeDef = TypedDict(
    "ListAnomalyGroupSummariesResponseTypeDef",
    {
        "AnomalyGroupSummaryList": List["AnomalyGroupSummaryTypeDef"],
        "AnomalyGroupStatistics": "AnomalyGroupStatisticsTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAnomalyGroupTimeSeriesRequestRequestTypeDef = TypedDict(
    "_RequiredListAnomalyGroupTimeSeriesRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyGroupId": str,
        "MetricName": str,
    },
)
_OptionalListAnomalyGroupTimeSeriesRequestRequestTypeDef = TypedDict(
    "_OptionalListAnomalyGroupTimeSeriesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAnomalyGroupTimeSeriesRequestRequestTypeDef(
    _RequiredListAnomalyGroupTimeSeriesRequestRequestTypeDef,
    _OptionalListAnomalyGroupTimeSeriesRequestRequestTypeDef,
):
    pass

ListAnomalyGroupTimeSeriesResponseTypeDef = TypedDict(
    "ListAnomalyGroupTimeSeriesResponseTypeDef",
    {
        "AnomalyGroupId": str,
        "MetricName": str,
        "TimestampList": List[str],
        "NextToken": str,
        "TimeSeriesList": List["TimeSeriesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMetricSetsRequestRequestTypeDef = TypedDict(
    "ListMetricSetsRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListMetricSetsResponseTypeDef = TypedDict(
    "ListMetricSetsResponseTypeDef",
    {
        "MetricSetSummaryList": List["MetricSetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricLevelImpactTypeDef = TypedDict(
    "MetricLevelImpactTypeDef",
    {
        "MetricName": str,
        "NumTimeSeries": int,
        "ContributionMatrix": "ContributionMatrixTypeDef",
    },
    total=False,
)

MetricSetDataQualityMetricTypeDef = TypedDict(
    "MetricSetDataQualityMetricTypeDef",
    {
        "MetricSetArn": str,
        "DataQualityMetricList": List["DataQualityMetricTypeDef"],
    },
    total=False,
)

MetricSetDimensionFilterTypeDef = TypedDict(
    "MetricSetDimensionFilterTypeDef",
    {
        "Name": str,
        "FilterList": List["FilterTypeDef"],
    },
    total=False,
)

MetricSetSummaryTypeDef = TypedDict(
    "MetricSetSummaryTypeDef",
    {
        "MetricSetArn": str,
        "AnomalyDetectorArn": str,
        "MetricSetDescription": str,
        "MetricSetName": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)

MetricSourceTypeDef = TypedDict(
    "MetricSourceTypeDef",
    {
        "S3SourceConfig": "S3SourceConfigTypeDef",
        "AppFlowConfig": "AppFlowConfigTypeDef",
        "CloudWatchConfig": "CloudWatchConfigTypeDef",
        "RDSSourceConfig": "RDSSourceConfigTypeDef",
        "RedshiftSourceConfig": "RedshiftSourceConfigTypeDef",
        "AthenaSourceConfig": "AthenaSourceConfigTypeDef",
    },
    total=False,
)

_RequiredMetricTypeDef = TypedDict(
    "_RequiredMetricTypeDef",
    {
        "MetricName": str,
        "AggregationFunction": AggregationFunctionType,
    },
)
_OptionalMetricTypeDef = TypedDict(
    "_OptionalMetricTypeDef",
    {
        "Namespace": str,
    },
    total=False,
)

class MetricTypeDef(_RequiredMetricTypeDef, _OptionalMetricTypeDef):
    pass

PutFeedbackRequestRequestTypeDef = TypedDict(
    "PutFeedbackRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyGroupTimeSeriesFeedback": "AnomalyGroupTimeSeriesFeedbackTypeDef",
    },
)

RDSSourceConfigTypeDef = TypedDict(
    "RDSSourceConfigTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DatabaseHost": str,
        "DatabasePort": int,
        "SecretManagerArn": str,
        "DatabaseName": str,
        "TableName": str,
        "RoleArn": str,
        "VpcConfiguration": "VpcConfigurationTypeDef",
    },
    total=False,
)

RedshiftSourceConfigTypeDef = TypedDict(
    "RedshiftSourceConfigTypeDef",
    {
        "ClusterIdentifier": str,
        "DatabaseHost": str,
        "DatabasePort": int,
        "SecretManagerArn": str,
        "DatabaseName": str,
        "TableName": str,
        "RoleArn": str,
        "VpcConfiguration": "VpcConfigurationTypeDef",
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

S3SourceConfigTypeDef = TypedDict(
    "S3SourceConfigTypeDef",
    {
        "RoleArn": str,
        "TemplatedPathList": List[str],
        "HistoricalDataPathList": List[str],
        "FileFormatDescriptor": "FileFormatDescriptorTypeDef",
    },
    total=False,
)

_RequiredSNSConfigurationTypeDef = TypedDict(
    "_RequiredSNSConfigurationTypeDef",
    {
        "RoleArn": str,
        "SnsTopicArn": str,
    },
)
_OptionalSNSConfigurationTypeDef = TypedDict(
    "_OptionalSNSConfigurationTypeDef",
    {
        "SnsFormat": SnsFormatType,
    },
    total=False,
)

class SNSConfigurationTypeDef(_RequiredSNSConfigurationTypeDef, _OptionalSNSConfigurationTypeDef):
    pass

_RequiredSampleDataS3SourceConfigTypeDef = TypedDict(
    "_RequiredSampleDataS3SourceConfigTypeDef",
    {
        "RoleArn": str,
        "FileFormatDescriptor": "FileFormatDescriptorTypeDef",
    },
)
_OptionalSampleDataS3SourceConfigTypeDef = TypedDict(
    "_OptionalSampleDataS3SourceConfigTypeDef",
    {
        "TemplatedPathList": List[str],
        "HistoricalDataPathList": List[str],
    },
    total=False,
)

class SampleDataS3SourceConfigTypeDef(
    _RequiredSampleDataS3SourceConfigTypeDef, _OptionalSampleDataS3SourceConfigTypeDef
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

TimeSeriesFeedbackTypeDef = TypedDict(
    "TimeSeriesFeedbackTypeDef",
    {
        "TimeSeriesId": str,
        "IsAnomaly": bool,
    },
    total=False,
)

TimeSeriesTypeDef = TypedDict(
    "TimeSeriesTypeDef",
    {
        "TimeSeriesId": str,
        "DimensionList": List["DimensionNameValueTypeDef"],
        "MetricValueList": List[float],
    },
)

TimestampColumnTypeDef = TypedDict(
    "TimestampColumnTypeDef",
    {
        "ColumnName": str,
        "ColumnFormat": str,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAlertRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAlertRequestRequestTypeDef",
    {
        "AlertArn": str,
    },
)
_OptionalUpdateAlertRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAlertRequestRequestTypeDef",
    {
        "AlertDescription": str,
        "AlertSensitivityThreshold": int,
        "Action": "ActionTypeDef",
        "AlertFilters": "AlertFiltersTypeDef",
    },
    total=False,
)

class UpdateAlertRequestRequestTypeDef(
    _RequiredUpdateAlertRequestRequestTypeDef, _OptionalUpdateAlertRequestRequestTypeDef
):
    pass

UpdateAlertResponseTypeDef = TypedDict(
    "UpdateAlertResponseTypeDef",
    {
        "AlertArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)
_OptionalUpdateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAnomalyDetectorRequestRequestTypeDef",
    {
        "KmsKeyArn": str,
        "AnomalyDetectorDescription": str,
        "AnomalyDetectorConfig": "AnomalyDetectorConfigTypeDef",
    },
    total=False,
)

class UpdateAnomalyDetectorRequestRequestTypeDef(
    _RequiredUpdateAnomalyDetectorRequestRequestTypeDef,
    _OptionalUpdateAnomalyDetectorRequestRequestTypeDef,
):
    pass

UpdateAnomalyDetectorResponseTypeDef = TypedDict(
    "UpdateAnomalyDetectorResponseTypeDef",
    {
        "AnomalyDetectorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMetricSetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMetricSetRequestRequestTypeDef",
    {
        "MetricSetArn": str,
    },
)
_OptionalUpdateMetricSetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMetricSetRequestRequestTypeDef",
    {
        "MetricSetDescription": str,
        "MetricList": List["MetricTypeDef"],
        "Offset": int,
        "TimestampColumn": "TimestampColumnTypeDef",
        "DimensionList": List[str],
        "MetricSetFrequency": FrequencyType,
        "MetricSource": "MetricSourceTypeDef",
        "DimensionFilterList": List["MetricSetDimensionFilterTypeDef"],
    },
    total=False,
)

class UpdateMetricSetRequestRequestTypeDef(
    _RequiredUpdateMetricSetRequestRequestTypeDef, _OptionalUpdateMetricSetRequestRequestTypeDef
):
    pass

UpdateMetricSetResponseTypeDef = TypedDict(
    "UpdateMetricSetResponseTypeDef",
    {
        "MetricSetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "SubnetIdList": List[str],
        "SecurityGroupIdList": List[str],
    },
)
