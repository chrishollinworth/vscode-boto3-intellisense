"""
Type annotations for kinesisanalytics service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_kinesisanalytics.type_defs import CloudWatchLoggingOptionTypeDef

    data: CloudWatchLoggingOptionTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import ApplicationStatusType, InputStartingPositionType, RecordFormatTypeType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AddApplicationCloudWatchLoggingOptionRequestTypeDef",
    "AddApplicationInputProcessingConfigurationRequestTypeDef",
    "AddApplicationInputRequestTypeDef",
    "AddApplicationOutputRequestTypeDef",
    "AddApplicationReferenceDataSourceRequestTypeDef",
    "ApplicationDetailTypeDef",
    "ApplicationSummaryTypeDef",
    "ApplicationUpdateTypeDef",
    "CSVMappingParametersTypeDef",
    "CloudWatchLoggingOptionDescriptionTypeDef",
    "CloudWatchLoggingOptionTypeDef",
    "CloudWatchLoggingOptionUpdateTypeDef",
    "CreateApplicationRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "DeleteApplicationCloudWatchLoggingOptionRequestTypeDef",
    "DeleteApplicationInputProcessingConfigurationRequestTypeDef",
    "DeleteApplicationOutputRequestTypeDef",
    "DeleteApplicationReferenceDataSourceRequestTypeDef",
    "DeleteApplicationRequestTypeDef",
    "DescribeApplicationRequestTypeDef",
    "DescribeApplicationResponseTypeDef",
    "DestinationSchemaTypeDef",
    "DiscoverInputSchemaRequestTypeDef",
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
    "ListApplicationsRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
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
    "SourceSchemaOutputTypeDef",
    "SourceSchemaTypeDef",
    "SourceSchemaUnionTypeDef",
    "StartApplicationRequestTypeDef",
    "StopApplicationRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateApplicationRequestTypeDef",
)

class CloudWatchLoggingOptionTypeDef(TypedDict):
    LogStreamARN: str
    RoleARN: str

class CloudWatchLoggingOptionDescriptionTypeDef(TypedDict):
    LogStreamARN: str
    RoleARN: str
    CloudWatchLoggingOptionId: NotRequired[str]

class ApplicationSummaryTypeDef(TypedDict):
    ApplicationName: str
    ApplicationARN: str
    ApplicationStatus: ApplicationStatusType

class CloudWatchLoggingOptionUpdateTypeDef(TypedDict):
    CloudWatchLoggingOptionId: str
    LogStreamARNUpdate: NotRequired[str]
    RoleARNUpdate: NotRequired[str]

class CSVMappingParametersTypeDef(TypedDict):
    RecordRowDelimiter: str
    RecordColumnDelimiter: str

class TagTypeDef(TypedDict):
    Key: str
    Value: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteApplicationCloudWatchLoggingOptionRequestTypeDef(TypedDict):
    ApplicationName: str
    CurrentApplicationVersionId: int
    CloudWatchLoggingOptionId: str

class DeleteApplicationInputProcessingConfigurationRequestTypeDef(TypedDict):
    ApplicationName: str
    CurrentApplicationVersionId: int
    InputId: str

class DeleteApplicationOutputRequestTypeDef(TypedDict):
    ApplicationName: str
    CurrentApplicationVersionId: int
    OutputId: str

class DeleteApplicationReferenceDataSourceRequestTypeDef(TypedDict):
    ApplicationName: str
    CurrentApplicationVersionId: int
    ReferenceId: str

TimestampTypeDef = Union[datetime, str]

class DescribeApplicationRequestTypeDef(TypedDict):
    ApplicationName: str

class DestinationSchemaTypeDef(TypedDict):
    RecordFormatType: RecordFormatTypeType

class InputStartingPositionConfigurationTypeDef(TypedDict):
    InputStartingPosition: NotRequired[InputStartingPositionType]

class S3ConfigurationTypeDef(TypedDict):
    RoleARN: str
    BucketARN: str
    FileKey: str

class InputParallelismTypeDef(TypedDict):
    Count: NotRequired[int]

class KinesisFirehoseInputDescriptionTypeDef(TypedDict):
    ResourceARN: NotRequired[str]
    RoleARN: NotRequired[str]

class KinesisStreamsInputDescriptionTypeDef(TypedDict):
    ResourceARN: NotRequired[str]
    RoleARN: NotRequired[str]

class InputLambdaProcessorDescriptionTypeDef(TypedDict):
    ResourceARN: NotRequired[str]
    RoleARN: NotRequired[str]

class InputLambdaProcessorTypeDef(TypedDict):
    ResourceARN: str
    RoleARN: str

class InputLambdaProcessorUpdateTypeDef(TypedDict):
    ResourceARNUpdate: NotRequired[str]
    RoleARNUpdate: NotRequired[str]

class InputParallelismUpdateTypeDef(TypedDict):
    CountUpdate: NotRequired[int]

RecordColumnTypeDef = TypedDict(
    "RecordColumnTypeDef",
    {
        "Name": str,
        "SqlType": str,
        "Mapping": NotRequired[str],
    },
)

class KinesisFirehoseInputTypeDef(TypedDict):
    ResourceARN: str
    RoleARN: str

class KinesisStreamsInputTypeDef(TypedDict):
    ResourceARN: str
    RoleARN: str

class KinesisFirehoseInputUpdateTypeDef(TypedDict):
    ResourceARNUpdate: NotRequired[str]
    RoleARNUpdate: NotRequired[str]

class KinesisStreamsInputUpdateTypeDef(TypedDict):
    ResourceARNUpdate: NotRequired[str]
    RoleARNUpdate: NotRequired[str]

class JSONMappingParametersTypeDef(TypedDict):
    RecordRowPath: str

class KinesisFirehoseOutputDescriptionTypeDef(TypedDict):
    ResourceARN: NotRequired[str]
    RoleARN: NotRequired[str]

class KinesisFirehoseOutputTypeDef(TypedDict):
    ResourceARN: str
    RoleARN: str

class KinesisFirehoseOutputUpdateTypeDef(TypedDict):
    ResourceARNUpdate: NotRequired[str]
    RoleARNUpdate: NotRequired[str]

class KinesisStreamsOutputDescriptionTypeDef(TypedDict):
    ResourceARN: NotRequired[str]
    RoleARN: NotRequired[str]

class KinesisStreamsOutputTypeDef(TypedDict):
    ResourceARN: str
    RoleARN: str

class KinesisStreamsOutputUpdateTypeDef(TypedDict):
    ResourceARNUpdate: NotRequired[str]
    RoleARNUpdate: NotRequired[str]

class LambdaOutputDescriptionTypeDef(TypedDict):
    ResourceARN: NotRequired[str]
    RoleARN: NotRequired[str]

class LambdaOutputTypeDef(TypedDict):
    ResourceARN: str
    RoleARN: str

class LambdaOutputUpdateTypeDef(TypedDict):
    ResourceARNUpdate: NotRequired[str]
    RoleARNUpdate: NotRequired[str]

class ListApplicationsRequestTypeDef(TypedDict):
    Limit: NotRequired[int]
    ExclusiveStartApplicationName: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class S3ReferenceDataSourceDescriptionTypeDef(TypedDict):
    BucketARN: str
    FileKey: str
    ReferenceRoleARN: str

class S3ReferenceDataSourceTypeDef(TypedDict):
    BucketARN: str
    FileKey: str
    ReferenceRoleARN: str

class S3ReferenceDataSourceUpdateTypeDef(TypedDict):
    BucketARNUpdate: NotRequired[str]
    FileKeyUpdate: NotRequired[str]
    ReferenceRoleARNUpdate: NotRequired[str]

class StopApplicationRequestTypeDef(TypedDict):
    ApplicationName: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class AddApplicationCloudWatchLoggingOptionRequestTypeDef(TypedDict):
    ApplicationName: str
    CurrentApplicationVersionId: int
    CloudWatchLoggingOption: CloudWatchLoggingOptionTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateApplicationResponseTypeDef(TypedDict):
    ApplicationSummary: ApplicationSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsResponseTypeDef(TypedDict):
    ApplicationSummaries: List[ApplicationSummaryTypeDef]
    HasMoreApplications: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationRequestTypeDef(TypedDict):
    ApplicationName: str
    CreateTimestamp: TimestampTypeDef

class InputConfigurationTypeDef(TypedDict):
    Id: str
    InputStartingPositionConfiguration: InputStartingPositionConfigurationTypeDef

class InputProcessingConfigurationDescriptionTypeDef(TypedDict):
    InputLambdaProcessorDescription: NotRequired[InputLambdaProcessorDescriptionTypeDef]

class InputProcessingConfigurationTypeDef(TypedDict):
    InputLambdaProcessor: InputLambdaProcessorTypeDef

class InputProcessingConfigurationUpdateTypeDef(TypedDict):
    InputLambdaProcessorUpdate: InputLambdaProcessorUpdateTypeDef

class MappingParametersTypeDef(TypedDict):
    JSONMappingParameters: NotRequired[JSONMappingParametersTypeDef]
    CSVMappingParameters: NotRequired[CSVMappingParametersTypeDef]

class OutputDescriptionTypeDef(TypedDict):
    OutputId: NotRequired[str]
    Name: NotRequired[str]
    KinesisStreamsOutputDescription: NotRequired[KinesisStreamsOutputDescriptionTypeDef]
    KinesisFirehoseOutputDescription: NotRequired[KinesisFirehoseOutputDescriptionTypeDef]
    LambdaOutputDescription: NotRequired[LambdaOutputDescriptionTypeDef]
    DestinationSchema: NotRequired[DestinationSchemaTypeDef]

class OutputTypeDef(TypedDict):
    Name: str
    DestinationSchema: DestinationSchemaTypeDef
    KinesisStreamsOutput: NotRequired[KinesisStreamsOutputTypeDef]
    KinesisFirehoseOutput: NotRequired[KinesisFirehoseOutputTypeDef]
    LambdaOutput: NotRequired[LambdaOutputTypeDef]

class OutputUpdateTypeDef(TypedDict):
    OutputId: str
    NameUpdate: NotRequired[str]
    KinesisStreamsOutputUpdate: NotRequired[KinesisStreamsOutputUpdateTypeDef]
    KinesisFirehoseOutputUpdate: NotRequired[KinesisFirehoseOutputUpdateTypeDef]
    LambdaOutputUpdate: NotRequired[LambdaOutputUpdateTypeDef]
    DestinationSchemaUpdate: NotRequired[DestinationSchemaTypeDef]

class StartApplicationRequestTypeDef(TypedDict):
    ApplicationName: str
    InputConfigurations: Sequence[InputConfigurationTypeDef]

class AddApplicationInputProcessingConfigurationRequestTypeDef(TypedDict):
    ApplicationName: str
    CurrentApplicationVersionId: int
    InputId: str
    InputProcessingConfiguration: InputProcessingConfigurationTypeDef

class DiscoverInputSchemaRequestTypeDef(TypedDict):
    ResourceARN: NotRequired[str]
    RoleARN: NotRequired[str]
    InputStartingPositionConfiguration: NotRequired[InputStartingPositionConfigurationTypeDef]
    S3Configuration: NotRequired[S3ConfigurationTypeDef]
    InputProcessingConfiguration: NotRequired[InputProcessingConfigurationTypeDef]

class RecordFormatTypeDef(TypedDict):
    RecordFormatType: RecordFormatTypeType
    MappingParameters: NotRequired[MappingParametersTypeDef]

class AddApplicationOutputRequestTypeDef(TypedDict):
    ApplicationName: str
    CurrentApplicationVersionId: int
    Output: OutputTypeDef

class InputSchemaUpdateTypeDef(TypedDict):
    RecordFormatUpdate: NotRequired[RecordFormatTypeDef]
    RecordEncodingUpdate: NotRequired[str]
    RecordColumnUpdates: NotRequired[Sequence[RecordColumnTypeDef]]

class SourceSchemaOutputTypeDef(TypedDict):
    RecordFormat: RecordFormatTypeDef
    RecordColumns: List[RecordColumnTypeDef]
    RecordEncoding: NotRequired[str]

class SourceSchemaTypeDef(TypedDict):
    RecordFormat: RecordFormatTypeDef
    RecordColumns: Sequence[RecordColumnTypeDef]
    RecordEncoding: NotRequired[str]

class InputUpdateTypeDef(TypedDict):
    InputId: str
    NamePrefixUpdate: NotRequired[str]
    InputProcessingConfigurationUpdate: NotRequired[InputProcessingConfigurationUpdateTypeDef]
    KinesisStreamsInputUpdate: NotRequired[KinesisStreamsInputUpdateTypeDef]
    KinesisFirehoseInputUpdate: NotRequired[KinesisFirehoseInputUpdateTypeDef]
    InputSchemaUpdate: NotRequired[InputSchemaUpdateTypeDef]
    InputParallelismUpdate: NotRequired[InputParallelismUpdateTypeDef]

class DiscoverInputSchemaResponseTypeDef(TypedDict):
    InputSchema: SourceSchemaOutputTypeDef
    ParsedInputRecords: List[List[str]]
    ProcessedInputRecords: List[str]
    RawInputRecords: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class InputDescriptionTypeDef(TypedDict):
    InputId: NotRequired[str]
    NamePrefix: NotRequired[str]
    InAppStreamNames: NotRequired[List[str]]
    InputProcessingConfigurationDescription: NotRequired[
        InputProcessingConfigurationDescriptionTypeDef
    ]
    KinesisStreamsInputDescription: NotRequired[KinesisStreamsInputDescriptionTypeDef]
    KinesisFirehoseInputDescription: NotRequired[KinesisFirehoseInputDescriptionTypeDef]
    InputSchema: NotRequired[SourceSchemaOutputTypeDef]
    InputParallelism: NotRequired[InputParallelismTypeDef]
    InputStartingPositionConfiguration: NotRequired[InputStartingPositionConfigurationTypeDef]

class ReferenceDataSourceDescriptionTypeDef(TypedDict):
    ReferenceId: str
    TableName: str
    S3ReferenceDataSourceDescription: S3ReferenceDataSourceDescriptionTypeDef
    ReferenceSchema: NotRequired[SourceSchemaOutputTypeDef]

SourceSchemaUnionTypeDef = Union[SourceSchemaTypeDef, SourceSchemaOutputTypeDef]

class ApplicationDetailTypeDef(TypedDict):
    ApplicationName: str
    ApplicationARN: str
    ApplicationStatus: ApplicationStatusType
    ApplicationVersionId: int
    ApplicationDescription: NotRequired[str]
    CreateTimestamp: NotRequired[datetime]
    LastUpdateTimestamp: NotRequired[datetime]
    InputDescriptions: NotRequired[List[InputDescriptionTypeDef]]
    OutputDescriptions: NotRequired[List[OutputDescriptionTypeDef]]
    ReferenceDataSourceDescriptions: NotRequired[List[ReferenceDataSourceDescriptionTypeDef]]
    CloudWatchLoggingOptionDescriptions: NotRequired[
        List[CloudWatchLoggingOptionDescriptionTypeDef]
    ]
    ApplicationCode: NotRequired[str]

class InputTypeDef(TypedDict):
    NamePrefix: str
    InputSchema: SourceSchemaUnionTypeDef
    InputProcessingConfiguration: NotRequired[InputProcessingConfigurationTypeDef]
    KinesisStreamsInput: NotRequired[KinesisStreamsInputTypeDef]
    KinesisFirehoseInput: NotRequired[KinesisFirehoseInputTypeDef]
    InputParallelism: NotRequired[InputParallelismTypeDef]

class ReferenceDataSourceTypeDef(TypedDict):
    TableName: str
    ReferenceSchema: SourceSchemaUnionTypeDef
    S3ReferenceDataSource: NotRequired[S3ReferenceDataSourceTypeDef]

class ReferenceDataSourceUpdateTypeDef(TypedDict):
    ReferenceId: str
    TableNameUpdate: NotRequired[str]
    S3ReferenceDataSourceUpdate: NotRequired[S3ReferenceDataSourceUpdateTypeDef]
    ReferenceSchemaUpdate: NotRequired[SourceSchemaUnionTypeDef]

class DescribeApplicationResponseTypeDef(TypedDict):
    ApplicationDetail: ApplicationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddApplicationInputRequestTypeDef(TypedDict):
    ApplicationName: str
    CurrentApplicationVersionId: int
    Input: InputTypeDef

class CreateApplicationRequestTypeDef(TypedDict):
    ApplicationName: str
    ApplicationDescription: NotRequired[str]
    Inputs: NotRequired[Sequence[InputTypeDef]]
    Outputs: NotRequired[Sequence[OutputTypeDef]]
    CloudWatchLoggingOptions: NotRequired[Sequence[CloudWatchLoggingOptionTypeDef]]
    ApplicationCode: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class AddApplicationReferenceDataSourceRequestTypeDef(TypedDict):
    ApplicationName: str
    CurrentApplicationVersionId: int
    ReferenceDataSource: ReferenceDataSourceTypeDef

class ApplicationUpdateTypeDef(TypedDict):
    InputUpdates: NotRequired[Sequence[InputUpdateTypeDef]]
    ApplicationCodeUpdate: NotRequired[str]
    OutputUpdates: NotRequired[Sequence[OutputUpdateTypeDef]]
    ReferenceDataSourceUpdates: NotRequired[Sequence[ReferenceDataSourceUpdateTypeDef]]
    CloudWatchLoggingOptionUpdates: NotRequired[Sequence[CloudWatchLoggingOptionUpdateTypeDef]]

class UpdateApplicationRequestTypeDef(TypedDict):
    ApplicationName: str
    CurrentApplicationVersionId: int
    ApplicationUpdate: ApplicationUpdateTypeDef
