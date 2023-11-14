"""
Type annotations for kinesisanalytics service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesisanalytics.type_defs import AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef

    data: AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import ApplicationStatusType, InputStartingPositionType, RecordFormatTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    "AddApplicationInputProcessingConfigurationRequestRequestTypeDef",
    "AddApplicationInputRequestRequestTypeDef",
    "AddApplicationOutputRequestRequestTypeDef",
    "AddApplicationReferenceDataSourceRequestRequestTypeDef",
    "ApplicationDetailTypeDef",
    "ApplicationSummaryTypeDef",
    "ApplicationUpdateTypeDef",
    "CSVMappingParametersTypeDef",
    "CloudWatchLoggingOptionDescriptionTypeDef",
    "CloudWatchLoggingOptionTypeDef",
    "CloudWatchLoggingOptionUpdateTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    "DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef",
    "DeleteApplicationOutputRequestRequestTypeDef",
    "DeleteApplicationReferenceDataSourceRequestRequestTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DescribeApplicationRequestRequestTypeDef",
    "DescribeApplicationResponseTypeDef",
    "DestinationSchemaTypeDef",
    "DiscoverInputSchemaRequestRequestTypeDef",
    "DiscoverInputSchemaResponseTypeDef",
    "InputConfigurationTypeDef",
    "InputDescriptionTypeDef",
    "InputLambdaProcessorDescriptionTypeDef",
    "InputLambdaProcessorTypeDef",
    "InputLambdaProcessorUpdateTypeDef",
    "InputParallelismTypeDef",
    "InputParallelismUpdateTypeDef",
    "InputProcessingConfigurationDescriptionTypeDef",
    "InputProcessingConfigurationTypeDef",
    "InputProcessingConfigurationUpdateTypeDef",
    "InputSchemaUpdateTypeDef",
    "InputStartingPositionConfigurationTypeDef",
    "InputTypeDef",
    "InputUpdateTypeDef",
    "JSONMappingParametersTypeDef",
    "KinesisFirehoseInputDescriptionTypeDef",
    "KinesisFirehoseInputTypeDef",
    "KinesisFirehoseInputUpdateTypeDef",
    "KinesisFirehoseOutputDescriptionTypeDef",
    "KinesisFirehoseOutputTypeDef",
    "KinesisFirehoseOutputUpdateTypeDef",
    "KinesisStreamsInputDescriptionTypeDef",
    "KinesisStreamsInputTypeDef",
    "KinesisStreamsInputUpdateTypeDef",
    "KinesisStreamsOutputDescriptionTypeDef",
    "KinesisStreamsOutputTypeDef",
    "KinesisStreamsOutputUpdateTypeDef",
    "LambdaOutputDescriptionTypeDef",
    "LambdaOutputTypeDef",
    "LambdaOutputUpdateTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MappingParametersTypeDef",
    "OutputDescriptionTypeDef",
    "OutputTypeDef",
    "OutputUpdateTypeDef",
    "RecordColumnTypeDef",
    "RecordFormatTypeDef",
    "ReferenceDataSourceDescriptionTypeDef",
    "ReferenceDataSourceTypeDef",
    "ReferenceDataSourceUpdateTypeDef",
    "ResponseMetadataTypeDef",
    "S3ConfigurationTypeDef",
    "S3ReferenceDataSourceDescriptionTypeDef",
    "S3ReferenceDataSourceTypeDef",
    "S3ReferenceDataSourceUpdateTypeDef",
    "SourceSchemaTypeDef",
    "StartApplicationRequestRequestTypeDef",
    "StopApplicationRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
)

AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef = TypedDict(
    "AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "CloudWatchLoggingOption": "CloudWatchLoggingOptionTypeDef",
    },
)

AddApplicationInputProcessingConfigurationRequestRequestTypeDef = TypedDict(
    "AddApplicationInputProcessingConfigurationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "InputId": str,
        "InputProcessingConfiguration": "InputProcessingConfigurationTypeDef",
    },
)

AddApplicationInputRequestRequestTypeDef = TypedDict(
    "AddApplicationInputRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "Input": "InputTypeDef",
    },
)

AddApplicationOutputRequestRequestTypeDef = TypedDict(
    "AddApplicationOutputRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "Output": "OutputTypeDef",
    },
)

AddApplicationReferenceDataSourceRequestRequestTypeDef = TypedDict(
    "AddApplicationReferenceDataSourceRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "ReferenceDataSource": "ReferenceDataSourceTypeDef",
    },
)

_RequiredApplicationDetailTypeDef = TypedDict(
    "_RequiredApplicationDetailTypeDef",
    {
        "ApplicationName": str,
        "ApplicationARN": str,
        "ApplicationStatus": ApplicationStatusType,
        "ApplicationVersionId": int,
    },
)
_OptionalApplicationDetailTypeDef = TypedDict(
    "_OptionalApplicationDetailTypeDef",
    {
        "ApplicationDescription": str,
        "CreateTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "InputDescriptions": List["InputDescriptionTypeDef"],
        "OutputDescriptions": List["OutputDescriptionTypeDef"],
        "ReferenceDataSourceDescriptions": List["ReferenceDataSourceDescriptionTypeDef"],
        "CloudWatchLoggingOptionDescriptions": List["CloudWatchLoggingOptionDescriptionTypeDef"],
        "ApplicationCode": str,
    },
    total=False,
)

class ApplicationDetailTypeDef(
    _RequiredApplicationDetailTypeDef, _OptionalApplicationDetailTypeDef
):
    pass

ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "ApplicationName": str,
        "ApplicationARN": str,
        "ApplicationStatus": ApplicationStatusType,
    },
)

ApplicationUpdateTypeDef = TypedDict(
    "ApplicationUpdateTypeDef",
    {
        "InputUpdates": List["InputUpdateTypeDef"],
        "ApplicationCodeUpdate": str,
        "OutputUpdates": List["OutputUpdateTypeDef"],
        "ReferenceDataSourceUpdates": List["ReferenceDataSourceUpdateTypeDef"],
        "CloudWatchLoggingOptionUpdates": List["CloudWatchLoggingOptionUpdateTypeDef"],
    },
    total=False,
)

CSVMappingParametersTypeDef = TypedDict(
    "CSVMappingParametersTypeDef",
    {
        "RecordRowDelimiter": str,
        "RecordColumnDelimiter": str,
    },
)

_RequiredCloudWatchLoggingOptionDescriptionTypeDef = TypedDict(
    "_RequiredCloudWatchLoggingOptionDescriptionTypeDef",
    {
        "LogStreamARN": str,
        "RoleARN": str,
    },
)
_OptionalCloudWatchLoggingOptionDescriptionTypeDef = TypedDict(
    "_OptionalCloudWatchLoggingOptionDescriptionTypeDef",
    {
        "CloudWatchLoggingOptionId": str,
    },
    total=False,
)

class CloudWatchLoggingOptionDescriptionTypeDef(
    _RequiredCloudWatchLoggingOptionDescriptionTypeDef,
    _OptionalCloudWatchLoggingOptionDescriptionTypeDef,
):
    pass

CloudWatchLoggingOptionTypeDef = TypedDict(
    "CloudWatchLoggingOptionTypeDef",
    {
        "LogStreamARN": str,
        "RoleARN": str,
    },
)

_RequiredCloudWatchLoggingOptionUpdateTypeDef = TypedDict(
    "_RequiredCloudWatchLoggingOptionUpdateTypeDef",
    {
        "CloudWatchLoggingOptionId": str,
    },
)
_OptionalCloudWatchLoggingOptionUpdateTypeDef = TypedDict(
    "_OptionalCloudWatchLoggingOptionUpdateTypeDef",
    {
        "LogStreamARNUpdate": str,
        "RoleARNUpdate": str,
    },
    total=False,
)

class CloudWatchLoggingOptionUpdateTypeDef(
    _RequiredCloudWatchLoggingOptionUpdateTypeDef, _OptionalCloudWatchLoggingOptionUpdateTypeDef
):
    pass

_RequiredCreateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
    },
)
_OptionalCreateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestRequestTypeDef",
    {
        "ApplicationDescription": str,
        "Inputs": List["InputTypeDef"],
        "Outputs": List["OutputTypeDef"],
        "CloudWatchLoggingOptions": List["CloudWatchLoggingOptionTypeDef"],
        "ApplicationCode": str,
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
        "ApplicationSummary": "ApplicationSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef = TypedDict(
    "DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "CloudWatchLoggingOptionId": str,
    },
)

DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "InputId": str,
    },
)

DeleteApplicationOutputRequestRequestTypeDef = TypedDict(
    "DeleteApplicationOutputRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "OutputId": str,
    },
)

DeleteApplicationReferenceDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteApplicationReferenceDataSourceRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "ReferenceId": str,
    },
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CreateTimestamp": Union[datetime, str],
    },
)

DescribeApplicationRequestRequestTypeDef = TypedDict(
    "DescribeApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
    },
)

DescribeApplicationResponseTypeDef = TypedDict(
    "DescribeApplicationResponseTypeDef",
    {
        "ApplicationDetail": "ApplicationDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationSchemaTypeDef = TypedDict(
    "DestinationSchemaTypeDef",
    {
        "RecordFormatType": RecordFormatTypeType,
    },
)

DiscoverInputSchemaRequestRequestTypeDef = TypedDict(
    "DiscoverInputSchemaRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
        "InputStartingPositionConfiguration": "InputStartingPositionConfigurationTypeDef",
        "S3Configuration": "S3ConfigurationTypeDef",
        "InputProcessingConfiguration": "InputProcessingConfigurationTypeDef",
    },
    total=False,
)

DiscoverInputSchemaResponseTypeDef = TypedDict(
    "DiscoverInputSchemaResponseTypeDef",
    {
        "InputSchema": "SourceSchemaTypeDef",
        "ParsedInputRecords": List[List[str]],
        "ProcessedInputRecords": List[str],
        "RawInputRecords": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputConfigurationTypeDef = TypedDict(
    "InputConfigurationTypeDef",
    {
        "Id": str,
        "InputStartingPositionConfiguration": "InputStartingPositionConfigurationTypeDef",
    },
)

InputDescriptionTypeDef = TypedDict(
    "InputDescriptionTypeDef",
    {
        "InputId": str,
        "NamePrefix": str,
        "InAppStreamNames": List[str],
        "InputProcessingConfigurationDescription": "InputProcessingConfigurationDescriptionTypeDef",
        "KinesisStreamsInputDescription": "KinesisStreamsInputDescriptionTypeDef",
        "KinesisFirehoseInputDescription": "KinesisFirehoseInputDescriptionTypeDef",
        "InputSchema": "SourceSchemaTypeDef",
        "InputParallelism": "InputParallelismTypeDef",
        "InputStartingPositionConfiguration": "InputStartingPositionConfigurationTypeDef",
    },
    total=False,
)

InputLambdaProcessorDescriptionTypeDef = TypedDict(
    "InputLambdaProcessorDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
    total=False,
)

InputLambdaProcessorTypeDef = TypedDict(
    "InputLambdaProcessorTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)

InputLambdaProcessorUpdateTypeDef = TypedDict(
    "InputLambdaProcessorUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
        "RoleARNUpdate": str,
    },
    total=False,
)

InputParallelismTypeDef = TypedDict(
    "InputParallelismTypeDef",
    {
        "Count": int,
    },
    total=False,
)

InputParallelismUpdateTypeDef = TypedDict(
    "InputParallelismUpdateTypeDef",
    {
        "CountUpdate": int,
    },
    total=False,
)

InputProcessingConfigurationDescriptionTypeDef = TypedDict(
    "InputProcessingConfigurationDescriptionTypeDef",
    {
        "InputLambdaProcessorDescription": "InputLambdaProcessorDescriptionTypeDef",
    },
    total=False,
)

InputProcessingConfigurationTypeDef = TypedDict(
    "InputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": "InputLambdaProcessorTypeDef",
    },
)

InputProcessingConfigurationUpdateTypeDef = TypedDict(
    "InputProcessingConfigurationUpdateTypeDef",
    {
        "InputLambdaProcessorUpdate": "InputLambdaProcessorUpdateTypeDef",
    },
)

InputSchemaUpdateTypeDef = TypedDict(
    "InputSchemaUpdateTypeDef",
    {
        "RecordFormatUpdate": "RecordFormatTypeDef",
        "RecordEncodingUpdate": str,
        "RecordColumnUpdates": List["RecordColumnTypeDef"],
    },
    total=False,
)

InputStartingPositionConfigurationTypeDef = TypedDict(
    "InputStartingPositionConfigurationTypeDef",
    {
        "InputStartingPosition": InputStartingPositionType,
    },
    total=False,
)

_RequiredInputTypeDef = TypedDict(
    "_RequiredInputTypeDef",
    {
        "NamePrefix": str,
        "InputSchema": "SourceSchemaTypeDef",
    },
)
_OptionalInputTypeDef = TypedDict(
    "_OptionalInputTypeDef",
    {
        "InputProcessingConfiguration": "InputProcessingConfigurationTypeDef",
        "KinesisStreamsInput": "KinesisStreamsInputTypeDef",
        "KinesisFirehoseInput": "KinesisFirehoseInputTypeDef",
        "InputParallelism": "InputParallelismTypeDef",
    },
    total=False,
)

class InputTypeDef(_RequiredInputTypeDef, _OptionalInputTypeDef):
    pass

_RequiredInputUpdateTypeDef = TypedDict(
    "_RequiredInputUpdateTypeDef",
    {
        "InputId": str,
    },
)
_OptionalInputUpdateTypeDef = TypedDict(
    "_OptionalInputUpdateTypeDef",
    {
        "NamePrefixUpdate": str,
        "InputProcessingConfigurationUpdate": "InputProcessingConfigurationUpdateTypeDef",
        "KinesisStreamsInputUpdate": "KinesisStreamsInputUpdateTypeDef",
        "KinesisFirehoseInputUpdate": "KinesisFirehoseInputUpdateTypeDef",
        "InputSchemaUpdate": "InputSchemaUpdateTypeDef",
        "InputParallelismUpdate": "InputParallelismUpdateTypeDef",
    },
    total=False,
)

class InputUpdateTypeDef(_RequiredInputUpdateTypeDef, _OptionalInputUpdateTypeDef):
    pass

JSONMappingParametersTypeDef = TypedDict(
    "JSONMappingParametersTypeDef",
    {
        "RecordRowPath": str,
    },
)

KinesisFirehoseInputDescriptionTypeDef = TypedDict(
    "KinesisFirehoseInputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
    total=False,
)

KinesisFirehoseInputTypeDef = TypedDict(
    "KinesisFirehoseInputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)

KinesisFirehoseInputUpdateTypeDef = TypedDict(
    "KinesisFirehoseInputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
        "RoleARNUpdate": str,
    },
    total=False,
)

KinesisFirehoseOutputDescriptionTypeDef = TypedDict(
    "KinesisFirehoseOutputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
    total=False,
)

KinesisFirehoseOutputTypeDef = TypedDict(
    "KinesisFirehoseOutputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)

KinesisFirehoseOutputUpdateTypeDef = TypedDict(
    "KinesisFirehoseOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
        "RoleARNUpdate": str,
    },
    total=False,
)

KinesisStreamsInputDescriptionTypeDef = TypedDict(
    "KinesisStreamsInputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
    total=False,
)

KinesisStreamsInputTypeDef = TypedDict(
    "KinesisStreamsInputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)

KinesisStreamsInputUpdateTypeDef = TypedDict(
    "KinesisStreamsInputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
        "RoleARNUpdate": str,
    },
    total=False,
)

KinesisStreamsOutputDescriptionTypeDef = TypedDict(
    "KinesisStreamsOutputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
    total=False,
)

KinesisStreamsOutputTypeDef = TypedDict(
    "KinesisStreamsOutputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)

KinesisStreamsOutputUpdateTypeDef = TypedDict(
    "KinesisStreamsOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
        "RoleARNUpdate": str,
    },
    total=False,
)

LambdaOutputDescriptionTypeDef = TypedDict(
    "LambdaOutputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
    total=False,
)

LambdaOutputTypeDef = TypedDict(
    "LambdaOutputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)

LambdaOutputUpdateTypeDef = TypedDict(
    "LambdaOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
        "RoleARNUpdate": str,
    },
    total=False,
)

ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "Limit": int,
        "ExclusiveStartApplicationName": str,
    },
    total=False,
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "ApplicationSummaries": List["ApplicationSummaryTypeDef"],
        "HasMoreApplications": bool,
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

MappingParametersTypeDef = TypedDict(
    "MappingParametersTypeDef",
    {
        "JSONMappingParameters": "JSONMappingParametersTypeDef",
        "CSVMappingParameters": "CSVMappingParametersTypeDef",
    },
    total=False,
)

OutputDescriptionTypeDef = TypedDict(
    "OutputDescriptionTypeDef",
    {
        "OutputId": str,
        "Name": str,
        "KinesisStreamsOutputDescription": "KinesisStreamsOutputDescriptionTypeDef",
        "KinesisFirehoseOutputDescription": "KinesisFirehoseOutputDescriptionTypeDef",
        "LambdaOutputDescription": "LambdaOutputDescriptionTypeDef",
        "DestinationSchema": "DestinationSchemaTypeDef",
    },
    total=False,
)

_RequiredOutputTypeDef = TypedDict(
    "_RequiredOutputTypeDef",
    {
        "Name": str,
        "DestinationSchema": "DestinationSchemaTypeDef",
    },
)
_OptionalOutputTypeDef = TypedDict(
    "_OptionalOutputTypeDef",
    {
        "KinesisStreamsOutput": "KinesisStreamsOutputTypeDef",
        "KinesisFirehoseOutput": "KinesisFirehoseOutputTypeDef",
        "LambdaOutput": "LambdaOutputTypeDef",
    },
    total=False,
)

class OutputTypeDef(_RequiredOutputTypeDef, _OptionalOutputTypeDef):
    pass

_RequiredOutputUpdateTypeDef = TypedDict(
    "_RequiredOutputUpdateTypeDef",
    {
        "OutputId": str,
    },
)
_OptionalOutputUpdateTypeDef = TypedDict(
    "_OptionalOutputUpdateTypeDef",
    {
        "NameUpdate": str,
        "KinesisStreamsOutputUpdate": "KinesisStreamsOutputUpdateTypeDef",
        "KinesisFirehoseOutputUpdate": "KinesisFirehoseOutputUpdateTypeDef",
        "LambdaOutputUpdate": "LambdaOutputUpdateTypeDef",
        "DestinationSchemaUpdate": "DestinationSchemaTypeDef",
    },
    total=False,
)

class OutputUpdateTypeDef(_RequiredOutputUpdateTypeDef, _OptionalOutputUpdateTypeDef):
    pass

_RequiredRecordColumnTypeDef = TypedDict(
    "_RequiredRecordColumnTypeDef",
    {
        "Name": str,
        "SqlType": str,
    },
)
_OptionalRecordColumnTypeDef = TypedDict(
    "_OptionalRecordColumnTypeDef",
    {
        "Mapping": str,
    },
    total=False,
)

class RecordColumnTypeDef(_RequiredRecordColumnTypeDef, _OptionalRecordColumnTypeDef):
    pass

_RequiredRecordFormatTypeDef = TypedDict(
    "_RequiredRecordFormatTypeDef",
    {
        "RecordFormatType": RecordFormatTypeType,
    },
)
_OptionalRecordFormatTypeDef = TypedDict(
    "_OptionalRecordFormatTypeDef",
    {
        "MappingParameters": "MappingParametersTypeDef",
    },
    total=False,
)

class RecordFormatTypeDef(_RequiredRecordFormatTypeDef, _OptionalRecordFormatTypeDef):
    pass

_RequiredReferenceDataSourceDescriptionTypeDef = TypedDict(
    "_RequiredReferenceDataSourceDescriptionTypeDef",
    {
        "ReferenceId": str,
        "TableName": str,
        "S3ReferenceDataSourceDescription": "S3ReferenceDataSourceDescriptionTypeDef",
    },
)
_OptionalReferenceDataSourceDescriptionTypeDef = TypedDict(
    "_OptionalReferenceDataSourceDescriptionTypeDef",
    {
        "ReferenceSchema": "SourceSchemaTypeDef",
    },
    total=False,
)

class ReferenceDataSourceDescriptionTypeDef(
    _RequiredReferenceDataSourceDescriptionTypeDef, _OptionalReferenceDataSourceDescriptionTypeDef
):
    pass

_RequiredReferenceDataSourceTypeDef = TypedDict(
    "_RequiredReferenceDataSourceTypeDef",
    {
        "TableName": str,
        "ReferenceSchema": "SourceSchemaTypeDef",
    },
)
_OptionalReferenceDataSourceTypeDef = TypedDict(
    "_OptionalReferenceDataSourceTypeDef",
    {
        "S3ReferenceDataSource": "S3ReferenceDataSourceTypeDef",
    },
    total=False,
)

class ReferenceDataSourceTypeDef(
    _RequiredReferenceDataSourceTypeDef, _OptionalReferenceDataSourceTypeDef
):
    pass

_RequiredReferenceDataSourceUpdateTypeDef = TypedDict(
    "_RequiredReferenceDataSourceUpdateTypeDef",
    {
        "ReferenceId": str,
    },
)
_OptionalReferenceDataSourceUpdateTypeDef = TypedDict(
    "_OptionalReferenceDataSourceUpdateTypeDef",
    {
        "TableNameUpdate": str,
        "S3ReferenceDataSourceUpdate": "S3ReferenceDataSourceUpdateTypeDef",
        "ReferenceSchemaUpdate": "SourceSchemaTypeDef",
    },
    total=False,
)

class ReferenceDataSourceUpdateTypeDef(
    _RequiredReferenceDataSourceUpdateTypeDef, _OptionalReferenceDataSourceUpdateTypeDef
):
    pass

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

S3ConfigurationTypeDef = TypedDict(
    "S3ConfigurationTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "FileKey": str,
    },
)

S3ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "S3ReferenceDataSourceDescriptionTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
        "ReferenceRoleARN": str,
    },
)

S3ReferenceDataSourceTypeDef = TypedDict(
    "S3ReferenceDataSourceTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
        "ReferenceRoleARN": str,
    },
)

S3ReferenceDataSourceUpdateTypeDef = TypedDict(
    "S3ReferenceDataSourceUpdateTypeDef",
    {
        "BucketARNUpdate": str,
        "FileKeyUpdate": str,
        "ReferenceRoleARNUpdate": str,
    },
    total=False,
)

_RequiredSourceSchemaTypeDef = TypedDict(
    "_RequiredSourceSchemaTypeDef",
    {
        "RecordFormat": "RecordFormatTypeDef",
        "RecordColumns": List["RecordColumnTypeDef"],
    },
)
_OptionalSourceSchemaTypeDef = TypedDict(
    "_OptionalSourceSchemaTypeDef",
    {
        "RecordEncoding": str,
    },
    total=False,
)

class SourceSchemaTypeDef(_RequiredSourceSchemaTypeDef, _OptionalSourceSchemaTypeDef):
    pass

StartApplicationRequestRequestTypeDef = TypedDict(
    "StartApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "InputConfigurations": List["InputConfigurationTypeDef"],
    },
)

StopApplicationRequestRequestTypeDef = TypedDict(
    "StopApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "ApplicationUpdate": "ApplicationUpdateTypeDef",
    },
)
