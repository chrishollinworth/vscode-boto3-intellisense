"""
Type annotations for kinesisanalyticsv2 service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_kinesisanalyticsv2.type_defs import CloudWatchLoggingOptionTypeDef

    data: CloudWatchLoggingOptionTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    ApplicationModeType,
    ApplicationRestoreTypeType,
    ApplicationStatusType,
    ArtifactTypeType,
    CodeContentTypeType,
    ConfigurationTypeType,
    InputStartingPositionType,
    LogLevelType,
    MetricsLevelType,
    OperationStatusType,
    RecordFormatTypeType,
    RuntimeEnvironmentType,
    SnapshotStatusType,
    UrlTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AddApplicationCloudWatchLoggingOptionRequestTypeDef",
    "AddApplicationCloudWatchLoggingOptionResponseTypeDef",
    "AddApplicationInputProcessingConfigurationRequestTypeDef",
    "AddApplicationInputProcessingConfigurationResponseTypeDef",
    "AddApplicationInputRequestTypeDef",
    "AddApplicationInputResponseTypeDef",
    "AddApplicationOutputRequestTypeDef",
    "AddApplicationOutputResponseTypeDef",
    "AddApplicationReferenceDataSourceRequestTypeDef",
    "AddApplicationReferenceDataSourceResponseTypeDef",
    "AddApplicationVpcConfigurationRequestTypeDef",
    "AddApplicationVpcConfigurationResponseTypeDef",
    "ApplicationCodeConfigurationDescriptionTypeDef",
    "ApplicationCodeConfigurationTypeDef",
    "ApplicationCodeConfigurationUpdateTypeDef",
    "ApplicationConfigurationDescriptionTypeDef",
    "ApplicationConfigurationTypeDef",
    "ApplicationConfigurationUpdateTypeDef",
    "ApplicationDetailTypeDef",
    "ApplicationMaintenanceConfigurationDescriptionTypeDef",
    "ApplicationMaintenanceConfigurationUpdateTypeDef",
    "ApplicationOperationInfoDetailsTypeDef",
    "ApplicationOperationInfoTypeDef",
    "ApplicationRestoreConfigurationTypeDef",
    "ApplicationSnapshotConfigurationDescriptionTypeDef",
    "ApplicationSnapshotConfigurationTypeDef",
    "ApplicationSnapshotConfigurationUpdateTypeDef",
    "ApplicationSummaryTypeDef",
    "ApplicationSystemRollbackConfigurationDescriptionTypeDef",
    "ApplicationSystemRollbackConfigurationTypeDef",
    "ApplicationSystemRollbackConfigurationUpdateTypeDef",
    "ApplicationVersionChangeDetailsTypeDef",
    "ApplicationVersionSummaryTypeDef",
    "BlobTypeDef",
    "CSVMappingParametersTypeDef",
    "CatalogConfigurationDescriptionTypeDef",
    "CatalogConfigurationTypeDef",
    "CatalogConfigurationUpdateTypeDef",
    "CheckpointConfigurationDescriptionTypeDef",
    "CheckpointConfigurationTypeDef",
    "CheckpointConfigurationUpdateTypeDef",
    "CloudWatchLoggingOptionDescriptionTypeDef",
    "CloudWatchLoggingOptionTypeDef",
    "CloudWatchLoggingOptionUpdateTypeDef",
    "CodeContentDescriptionTypeDef",
    "CodeContentTypeDef",
    "CodeContentUpdateTypeDef",
    "CreateApplicationPresignedUrlRequestTypeDef",
    "CreateApplicationPresignedUrlResponseTypeDef",
    "CreateApplicationRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateApplicationSnapshotRequestTypeDef",
    "CustomArtifactConfigurationDescriptionTypeDef",
    "CustomArtifactConfigurationTypeDef",
    "DeleteApplicationCloudWatchLoggingOptionRequestTypeDef",
    "DeleteApplicationCloudWatchLoggingOptionResponseTypeDef",
    "DeleteApplicationInputProcessingConfigurationRequestTypeDef",
    "DeleteApplicationInputProcessingConfigurationResponseTypeDef",
    "DeleteApplicationOutputRequestTypeDef",
    "DeleteApplicationOutputResponseTypeDef",
    "DeleteApplicationReferenceDataSourceRequestTypeDef",
    "DeleteApplicationReferenceDataSourceResponseTypeDef",
    "DeleteApplicationRequestTypeDef",
    "DeleteApplicationSnapshotRequestTypeDef",
    "DeleteApplicationVpcConfigurationRequestTypeDef",
    "DeleteApplicationVpcConfigurationResponseTypeDef",
    "DeployAsApplicationConfigurationDescriptionTypeDef",
    "DeployAsApplicationConfigurationTypeDef",
    "DeployAsApplicationConfigurationUpdateTypeDef",
    "DescribeApplicationOperationRequestTypeDef",
    "DescribeApplicationOperationResponseTypeDef",
    "DescribeApplicationRequestTypeDef",
    "DescribeApplicationResponseTypeDef",
    "DescribeApplicationSnapshotRequestTypeDef",
    "DescribeApplicationSnapshotResponseTypeDef",
    "DescribeApplicationVersionRequestTypeDef",
    "DescribeApplicationVersionResponseTypeDef",
    "DestinationSchemaTypeDef",
    "DiscoverInputSchemaRequestTypeDef",
    "DiscoverInputSchemaResponseTypeDef",
    "EnvironmentPropertiesTypeDef",
    "EnvironmentPropertyDescriptionsTypeDef",
    "EnvironmentPropertyUpdatesTypeDef",
    "ErrorInfoTypeDef",
    "FlinkApplicationConfigurationDescriptionTypeDef",
    "FlinkApplicationConfigurationTypeDef",
    "FlinkApplicationConfigurationUpdateTypeDef",
    "FlinkRunConfigurationTypeDef",
    "GlueDataCatalogConfigurationDescriptionTypeDef",
    "GlueDataCatalogConfigurationTypeDef",
    "GlueDataCatalogConfigurationUpdateTypeDef",
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
    "ListApplicationOperationsRequestPaginateTypeDef",
    "ListApplicationOperationsRequestTypeDef",
    "ListApplicationOperationsResponseTypeDef",
    "ListApplicationSnapshotsRequestPaginateTypeDef",
    "ListApplicationSnapshotsRequestTypeDef",
    "ListApplicationSnapshotsResponseTypeDef",
    "ListApplicationVersionsRequestPaginateTypeDef",
    "ListApplicationVersionsRequestTypeDef",
    "ListApplicationVersionsResponseTypeDef",
    "ListApplicationsRequestPaginateTypeDef",
    "ListApplicationsRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MappingParametersTypeDef",
    "MavenReferenceTypeDef",
    "MonitoringConfigurationDescriptionTypeDef",
    "MonitoringConfigurationTypeDef",
    "MonitoringConfigurationUpdateTypeDef",
    "OperationFailureDetailsTypeDef",
    "OutputDescriptionTypeDef",
    "OutputTypeDef",
    "OutputUpdateTypeDef",
    "PaginatorConfigTypeDef",
    "ParallelismConfigurationDescriptionTypeDef",
    "ParallelismConfigurationTypeDef",
    "ParallelismConfigurationUpdateTypeDef",
    "PropertyGroupOutputTypeDef",
    "PropertyGroupTypeDef",
    "PropertyGroupUnionTypeDef",
    "RecordColumnTypeDef",
    "RecordFormatTypeDef",
    "ReferenceDataSourceDescriptionTypeDef",
    "ReferenceDataSourceTypeDef",
    "ReferenceDataSourceUpdateTypeDef",
    "ResponseMetadataTypeDef",
    "RollbackApplicationRequestTypeDef",
    "RollbackApplicationResponseTypeDef",
    "RunConfigurationDescriptionTypeDef",
    "RunConfigurationTypeDef",
    "RunConfigurationUpdateTypeDef",
    "S3ApplicationCodeLocationDescriptionTypeDef",
    "S3ConfigurationTypeDef",
    "S3ContentBaseLocationDescriptionTypeDef",
    "S3ContentBaseLocationTypeDef",
    "S3ContentBaseLocationUpdateTypeDef",
    "S3ContentLocationTypeDef",
    "S3ContentLocationUpdateTypeDef",
    "S3ReferenceDataSourceDescriptionTypeDef",
    "S3ReferenceDataSourceTypeDef",
    "S3ReferenceDataSourceUpdateTypeDef",
    "SnapshotDetailsTypeDef",
    "SourceSchemaOutputTypeDef",
    "SourceSchemaTypeDef",
    "SourceSchemaUnionTypeDef",
    "SqlApplicationConfigurationDescriptionTypeDef",
    "SqlApplicationConfigurationTypeDef",
    "SqlApplicationConfigurationUpdateTypeDef",
    "SqlRunConfigurationTypeDef",
    "StartApplicationRequestTypeDef",
    "StartApplicationResponseTypeDef",
    "StopApplicationRequestTypeDef",
    "StopApplicationResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateApplicationMaintenanceConfigurationRequestTypeDef",
    "UpdateApplicationMaintenanceConfigurationResponseTypeDef",
    "UpdateApplicationRequestTypeDef",
    "UpdateApplicationResponseTypeDef",
    "VpcConfigurationDescriptionTypeDef",
    "VpcConfigurationTypeDef",
    "VpcConfigurationUpdateTypeDef",
    "ZeppelinApplicationConfigurationDescriptionTypeDef",
    "ZeppelinApplicationConfigurationTypeDef",
    "ZeppelinApplicationConfigurationUpdateTypeDef",
    "ZeppelinMonitoringConfigurationDescriptionTypeDef",
    "ZeppelinMonitoringConfigurationTypeDef",
    "ZeppelinMonitoringConfigurationUpdateTypeDef",
)

class CloudWatchLoggingOptionTypeDef(TypedDict):
    LogStreamARN: str

class CloudWatchLoggingOptionDescriptionTypeDef(TypedDict):
    LogStreamARN: str
    CloudWatchLoggingOptionId: NotRequired[str]
    RoleARN: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class VpcConfigurationTypeDef(TypedDict):
    SubnetIds: Sequence[str]
    SecurityGroupIds: Sequence[str]

class VpcConfigurationDescriptionTypeDef(TypedDict):
    VpcConfigurationId: str
    VpcId: str
    SubnetIds: List[str]
    SecurityGroupIds: List[str]

class ApplicationSnapshotConfigurationDescriptionTypeDef(TypedDict):
    SnapshotsEnabled: bool

class ApplicationSystemRollbackConfigurationDescriptionTypeDef(TypedDict):
    RollbackEnabled: bool

class ApplicationSnapshotConfigurationTypeDef(TypedDict):
    SnapshotsEnabled: bool

class ApplicationSystemRollbackConfigurationTypeDef(TypedDict):
    RollbackEnabled: bool

class ApplicationSnapshotConfigurationUpdateTypeDef(TypedDict):
    SnapshotsEnabledUpdate: bool

class ApplicationSystemRollbackConfigurationUpdateTypeDef(TypedDict):
    RollbackEnabledUpdate: bool

class VpcConfigurationUpdateTypeDef(TypedDict):
    VpcConfigurationId: str
    SubnetIdUpdates: NotRequired[Sequence[str]]
    SecurityGroupIdUpdates: NotRequired[Sequence[str]]

class ApplicationMaintenanceConfigurationDescriptionTypeDef(TypedDict):
    ApplicationMaintenanceWindowStartTime: str
    ApplicationMaintenanceWindowEndTime: str

class ApplicationMaintenanceConfigurationUpdateTypeDef(TypedDict):
    ApplicationMaintenanceWindowStartTimeUpdate: str

class ApplicationVersionChangeDetailsTypeDef(TypedDict):
    ApplicationVersionUpdatedFrom: int
    ApplicationVersionUpdatedTo: int

class ApplicationOperationInfoTypeDef(TypedDict):
    Operation: NotRequired[str]
    OperationId: NotRequired[str]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    OperationStatus: NotRequired[OperationStatusType]

class ApplicationRestoreConfigurationTypeDef(TypedDict):
    ApplicationRestoreType: ApplicationRestoreTypeType
    SnapshotName: NotRequired[str]

class ApplicationSummaryTypeDef(TypedDict):
    ApplicationName: str
    ApplicationARN: str
    ApplicationStatus: ApplicationStatusType
    ApplicationVersionId: int
    RuntimeEnvironment: RuntimeEnvironmentType
    ApplicationMode: NotRequired[ApplicationModeType]

class ApplicationVersionSummaryTypeDef(TypedDict):
    ApplicationVersionId: int
    ApplicationStatus: ApplicationStatusType

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CSVMappingParametersTypeDef(TypedDict):
    RecordRowDelimiter: str
    RecordColumnDelimiter: str

class GlueDataCatalogConfigurationDescriptionTypeDef(TypedDict):
    DatabaseARN: str

class GlueDataCatalogConfigurationTypeDef(TypedDict):
    DatabaseARN: str

class GlueDataCatalogConfigurationUpdateTypeDef(TypedDict):
    DatabaseARNUpdate: str

class CheckpointConfigurationDescriptionTypeDef(TypedDict):
    ConfigurationType: NotRequired[ConfigurationTypeType]
    CheckpointingEnabled: NotRequired[bool]
    CheckpointInterval: NotRequired[int]
    MinPauseBetweenCheckpoints: NotRequired[int]

class CheckpointConfigurationTypeDef(TypedDict):
    ConfigurationType: ConfigurationTypeType
    CheckpointingEnabled: NotRequired[bool]
    CheckpointInterval: NotRequired[int]
    MinPauseBetweenCheckpoints: NotRequired[int]

class CheckpointConfigurationUpdateTypeDef(TypedDict):
    ConfigurationTypeUpdate: NotRequired[ConfigurationTypeType]
    CheckpointingEnabledUpdate: NotRequired[bool]
    CheckpointIntervalUpdate: NotRequired[int]
    MinPauseBetweenCheckpointsUpdate: NotRequired[int]

class CloudWatchLoggingOptionUpdateTypeDef(TypedDict):
    CloudWatchLoggingOptionId: str
    LogStreamARNUpdate: NotRequired[str]

class S3ApplicationCodeLocationDescriptionTypeDef(TypedDict):
    BucketARN: str
    FileKey: str
    ObjectVersion: NotRequired[str]

class S3ContentLocationTypeDef(TypedDict):
    BucketARN: str
    FileKey: str
    ObjectVersion: NotRequired[str]

class S3ContentLocationUpdateTypeDef(TypedDict):
    BucketARNUpdate: NotRequired[str]
    FileKeyUpdate: NotRequired[str]
    ObjectVersionUpdate: NotRequired[str]

class CreateApplicationPresignedUrlRequestTypeDef(TypedDict):
    ApplicationName: str
    UrlType: UrlTypeType
    SessionExpirationDurationInSeconds: NotRequired[int]

class TagTypeDef(TypedDict):
    Key: str
    Value: NotRequired[str]

class CreateApplicationSnapshotRequestTypeDef(TypedDict):
    ApplicationName: str
    SnapshotName: str

class MavenReferenceTypeDef(TypedDict):
    GroupId: str
    ArtifactId: str
    Version: str

class DeleteApplicationCloudWatchLoggingOptionRequestTypeDef(TypedDict):
    ApplicationName: str
    CloudWatchLoggingOptionId: str
    CurrentApplicationVersionId: NotRequired[int]
    ConditionalToken: NotRequired[str]

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

class DeleteApplicationVpcConfigurationRequestTypeDef(TypedDict):
    ApplicationName: str
    VpcConfigurationId: str
    CurrentApplicationVersionId: NotRequired[int]
    ConditionalToken: NotRequired[str]

class S3ContentBaseLocationDescriptionTypeDef(TypedDict):
    BucketARN: str
    BasePath: NotRequired[str]

class S3ContentBaseLocationTypeDef(TypedDict):
    BucketARN: str
    BasePath: NotRequired[str]

class S3ContentBaseLocationUpdateTypeDef(TypedDict):
    BucketARNUpdate: NotRequired[str]
    BasePathUpdate: NotRequired[str]

class DescribeApplicationOperationRequestTypeDef(TypedDict):
    ApplicationName: str
    OperationId: str

class DescribeApplicationRequestTypeDef(TypedDict):
    ApplicationName: str
    IncludeAdditionalDetails: NotRequired[bool]

class DescribeApplicationSnapshotRequestTypeDef(TypedDict):
    ApplicationName: str
    SnapshotName: str

class SnapshotDetailsTypeDef(TypedDict):
    SnapshotName: str
    SnapshotStatus: SnapshotStatusType
    ApplicationVersionId: int
    SnapshotCreationTimestamp: NotRequired[datetime]
    RuntimeEnvironment: NotRequired[RuntimeEnvironmentType]

class DescribeApplicationVersionRequestTypeDef(TypedDict):
    ApplicationName: str
    ApplicationVersionId: int

class DestinationSchemaTypeDef(TypedDict):
    RecordFormatType: RecordFormatTypeType

class InputStartingPositionConfigurationTypeDef(TypedDict):
    InputStartingPosition: NotRequired[InputStartingPositionType]

class S3ConfigurationTypeDef(TypedDict):
    BucketARN: str
    FileKey: str

class PropertyGroupOutputTypeDef(TypedDict):
    PropertyGroupId: str
    PropertyMap: Dict[str, str]

class ErrorInfoTypeDef(TypedDict):
    ErrorString: NotRequired[str]

class MonitoringConfigurationDescriptionTypeDef(TypedDict):
    ConfigurationType: NotRequired[ConfigurationTypeType]
    MetricsLevel: NotRequired[MetricsLevelType]
    LogLevel: NotRequired[LogLevelType]

class ParallelismConfigurationDescriptionTypeDef(TypedDict):
    ConfigurationType: NotRequired[ConfigurationTypeType]
    Parallelism: NotRequired[int]
    ParallelismPerKPU: NotRequired[int]
    CurrentParallelism: NotRequired[int]
    AutoScalingEnabled: NotRequired[bool]

class MonitoringConfigurationTypeDef(TypedDict):
    ConfigurationType: ConfigurationTypeType
    MetricsLevel: NotRequired[MetricsLevelType]
    LogLevel: NotRequired[LogLevelType]

class ParallelismConfigurationTypeDef(TypedDict):
    ConfigurationType: ConfigurationTypeType
    Parallelism: NotRequired[int]
    ParallelismPerKPU: NotRequired[int]
    AutoScalingEnabled: NotRequired[bool]

class MonitoringConfigurationUpdateTypeDef(TypedDict):
    ConfigurationTypeUpdate: NotRequired[ConfigurationTypeType]
    MetricsLevelUpdate: NotRequired[MetricsLevelType]
    LogLevelUpdate: NotRequired[LogLevelType]

class ParallelismConfigurationUpdateTypeDef(TypedDict):
    ConfigurationTypeUpdate: NotRequired[ConfigurationTypeType]
    ParallelismUpdate: NotRequired[int]
    ParallelismPerKPUUpdate: NotRequired[int]
    AutoScalingEnabledUpdate: NotRequired[bool]

class FlinkRunConfigurationTypeDef(TypedDict):
    AllowNonRestoredState: NotRequired[bool]

class InputParallelismTypeDef(TypedDict):
    Count: NotRequired[int]

class KinesisFirehoseInputDescriptionTypeDef(TypedDict):
    ResourceARN: str
    RoleARN: NotRequired[str]

class KinesisStreamsInputDescriptionTypeDef(TypedDict):
    ResourceARN: str
    RoleARN: NotRequired[str]

class InputLambdaProcessorDescriptionTypeDef(TypedDict):
    ResourceARN: str
    RoleARN: NotRequired[str]

class InputLambdaProcessorTypeDef(TypedDict):
    ResourceARN: str

class InputLambdaProcessorUpdateTypeDef(TypedDict):
    ResourceARNUpdate: str

class InputParallelismUpdateTypeDef(TypedDict):
    CountUpdate: int

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

class KinesisStreamsInputTypeDef(TypedDict):
    ResourceARN: str

class KinesisFirehoseInputUpdateTypeDef(TypedDict):
    ResourceARNUpdate: str

class KinesisStreamsInputUpdateTypeDef(TypedDict):
    ResourceARNUpdate: str

class JSONMappingParametersTypeDef(TypedDict):
    RecordRowPath: str

class KinesisFirehoseOutputDescriptionTypeDef(TypedDict):
    ResourceARN: str
    RoleARN: NotRequired[str]

class KinesisFirehoseOutputTypeDef(TypedDict):
    ResourceARN: str

class KinesisFirehoseOutputUpdateTypeDef(TypedDict):
    ResourceARNUpdate: str

class KinesisStreamsOutputDescriptionTypeDef(TypedDict):
    ResourceARN: str
    RoleARN: NotRequired[str]

class KinesisStreamsOutputTypeDef(TypedDict):
    ResourceARN: str

class KinesisStreamsOutputUpdateTypeDef(TypedDict):
    ResourceARNUpdate: str

class LambdaOutputDescriptionTypeDef(TypedDict):
    ResourceARN: str
    RoleARN: NotRequired[str]

class LambdaOutputTypeDef(TypedDict):
    ResourceARN: str

class LambdaOutputUpdateTypeDef(TypedDict):
    ResourceARNUpdate: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListApplicationOperationsRequestTypeDef(TypedDict):
    ApplicationName: str
    Limit: NotRequired[int]
    NextToken: NotRequired[str]
    Operation: NotRequired[str]
    OperationStatus: NotRequired[OperationStatusType]

class ListApplicationSnapshotsRequestTypeDef(TypedDict):
    ApplicationName: str
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class ListApplicationVersionsRequestTypeDef(TypedDict):
    ApplicationName: str
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class ListApplicationsRequestTypeDef(TypedDict):
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class PropertyGroupTypeDef(TypedDict):
    PropertyGroupId: str
    PropertyMap: Mapping[str, str]

class S3ReferenceDataSourceDescriptionTypeDef(TypedDict):
    BucketARN: str
    FileKey: str
    ReferenceRoleARN: NotRequired[str]

class S3ReferenceDataSourceTypeDef(TypedDict):
    BucketARN: NotRequired[str]
    FileKey: NotRequired[str]

class S3ReferenceDataSourceUpdateTypeDef(TypedDict):
    BucketARNUpdate: NotRequired[str]
    FileKeyUpdate: NotRequired[str]

class RollbackApplicationRequestTypeDef(TypedDict):
    ApplicationName: str
    CurrentApplicationVersionId: int

class StopApplicationRequestTypeDef(TypedDict):
    ApplicationName: str
    Force: NotRequired[bool]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class ZeppelinMonitoringConfigurationDescriptionTypeDef(TypedDict):
    LogLevel: NotRequired[LogLevelType]

class ZeppelinMonitoringConfigurationTypeDef(TypedDict):
    LogLevel: LogLevelType

class ZeppelinMonitoringConfigurationUpdateTypeDef(TypedDict):
    LogLevelUpdate: LogLevelType

class AddApplicationCloudWatchLoggingOptionRequestTypeDef(TypedDict):
    ApplicationName: str
    CloudWatchLoggingOption: CloudWatchLoggingOptionTypeDef
    CurrentApplicationVersionId: NotRequired[int]
    ConditionalToken: NotRequired[str]

class AddApplicationCloudWatchLoggingOptionResponseTypeDef(TypedDict):
    ApplicationARN: str
    ApplicationVersionId: int
    CloudWatchLoggingOptionDescriptions: List[CloudWatchLoggingOptionDescriptionTypeDef]
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationPresignedUrlResponseTypeDef(TypedDict):
    AuthorizedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationCloudWatchLoggingOptionResponseTypeDef(TypedDict):
    ApplicationARN: str
    ApplicationVersionId: int
    CloudWatchLoggingOptionDescriptions: List[CloudWatchLoggingOptionDescriptionTypeDef]
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationInputProcessingConfigurationResponseTypeDef(TypedDict):
    ApplicationARN: str
    ApplicationVersionId: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationOutputResponseTypeDef(TypedDict):
    ApplicationARN: str
    ApplicationVersionId: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationReferenceDataSourceResponseTypeDef(TypedDict):
    ApplicationARN: str
    ApplicationVersionId: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationVpcConfigurationResponseTypeDef(TypedDict):
    ApplicationARN: str
    ApplicationVersionId: int
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartApplicationResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopApplicationResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddApplicationVpcConfigurationRequestTypeDef(TypedDict):
    ApplicationName: str
    VpcConfiguration: VpcConfigurationTypeDef
    CurrentApplicationVersionId: NotRequired[int]
    ConditionalToken: NotRequired[str]

class AddApplicationVpcConfigurationResponseTypeDef(TypedDict):
    ApplicationARN: str
    ApplicationVersionId: int
    VpcConfigurationDescription: VpcConfigurationDescriptionTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationMaintenanceConfigurationResponseTypeDef(TypedDict):
    ApplicationARN: str
    ApplicationMaintenanceConfigurationDescription: (
        ApplicationMaintenanceConfigurationDescriptionTypeDef
    )
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationMaintenanceConfigurationRequestTypeDef(TypedDict):
    ApplicationName: str
    ApplicationMaintenanceConfigurationUpdate: ApplicationMaintenanceConfigurationUpdateTypeDef

class ListApplicationOperationsResponseTypeDef(TypedDict):
    ApplicationOperationInfoList: List[ApplicationOperationInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListApplicationsResponseTypeDef(TypedDict):
    ApplicationSummaries: List[ApplicationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListApplicationVersionsResponseTypeDef(TypedDict):
    ApplicationVersionSummaries: List[ApplicationVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CatalogConfigurationDescriptionTypeDef(TypedDict):
    GlueDataCatalogConfigurationDescription: GlueDataCatalogConfigurationDescriptionTypeDef

class CatalogConfigurationTypeDef(TypedDict):
    GlueDataCatalogConfiguration: GlueDataCatalogConfigurationTypeDef

class CatalogConfigurationUpdateTypeDef(TypedDict):
    GlueDataCatalogConfigurationUpdate: GlueDataCatalogConfigurationUpdateTypeDef

class CodeContentDescriptionTypeDef(TypedDict):
    TextContent: NotRequired[str]
    CodeMD5: NotRequired[str]
    CodeSize: NotRequired[int]
    S3ApplicationCodeLocationDescription: NotRequired[S3ApplicationCodeLocationDescriptionTypeDef]

class CodeContentTypeDef(TypedDict):
    TextContent: NotRequired[str]
    ZipFileContent: NotRequired[BlobTypeDef]
    S3ContentLocation: NotRequired[S3ContentLocationTypeDef]

class CodeContentUpdateTypeDef(TypedDict):
    TextContentUpdate: NotRequired[str]
    ZipFileContentUpdate: NotRequired[BlobTypeDef]
    S3ContentLocationUpdate: NotRequired[S3ContentLocationUpdateTypeDef]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CustomArtifactConfigurationDescriptionTypeDef(TypedDict):
    ArtifactType: NotRequired[ArtifactTypeType]
    S3ContentLocationDescription: NotRequired[S3ContentLocationTypeDef]
    MavenReferenceDescription: NotRequired[MavenReferenceTypeDef]

class CustomArtifactConfigurationTypeDef(TypedDict):
    ArtifactType: ArtifactTypeType
    S3ContentLocation: NotRequired[S3ContentLocationTypeDef]
    MavenReference: NotRequired[MavenReferenceTypeDef]

class DeleteApplicationRequestTypeDef(TypedDict):
    ApplicationName: str
    CreateTimestamp: TimestampTypeDef

class DeleteApplicationSnapshotRequestTypeDef(TypedDict):
    ApplicationName: str
    SnapshotName: str
    SnapshotCreationTimestamp: TimestampTypeDef

class DeployAsApplicationConfigurationDescriptionTypeDef(TypedDict):
    S3ContentLocationDescription: S3ContentBaseLocationDescriptionTypeDef

class DeployAsApplicationConfigurationTypeDef(TypedDict):
    S3ContentLocation: S3ContentBaseLocationTypeDef

class DeployAsApplicationConfigurationUpdateTypeDef(TypedDict):
    S3ContentLocationUpdate: NotRequired[S3ContentBaseLocationUpdateTypeDef]

class DescribeApplicationSnapshotResponseTypeDef(TypedDict):
    SnapshotDetails: SnapshotDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationSnapshotsResponseTypeDef(TypedDict):
    SnapshotSummaries: List[SnapshotDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SqlRunConfigurationTypeDef(TypedDict):
    InputId: str
    InputStartingPositionConfiguration: InputStartingPositionConfigurationTypeDef

class EnvironmentPropertyDescriptionsTypeDef(TypedDict):
    PropertyGroupDescriptions: NotRequired[List[PropertyGroupOutputTypeDef]]

class OperationFailureDetailsTypeDef(TypedDict):
    RollbackOperationId: NotRequired[str]
    ErrorInfo: NotRequired[ErrorInfoTypeDef]

class FlinkApplicationConfigurationDescriptionTypeDef(TypedDict):
    CheckpointConfigurationDescription: NotRequired[CheckpointConfigurationDescriptionTypeDef]
    MonitoringConfigurationDescription: NotRequired[MonitoringConfigurationDescriptionTypeDef]
    ParallelismConfigurationDescription: NotRequired[ParallelismConfigurationDescriptionTypeDef]
    JobPlanDescription: NotRequired[str]

class FlinkApplicationConfigurationTypeDef(TypedDict):
    CheckpointConfiguration: NotRequired[CheckpointConfigurationTypeDef]
    MonitoringConfiguration: NotRequired[MonitoringConfigurationTypeDef]
    ParallelismConfiguration: NotRequired[ParallelismConfigurationTypeDef]

class FlinkApplicationConfigurationUpdateTypeDef(TypedDict):
    CheckpointConfigurationUpdate: NotRequired[CheckpointConfigurationUpdateTypeDef]
    MonitoringConfigurationUpdate: NotRequired[MonitoringConfigurationUpdateTypeDef]
    ParallelismConfigurationUpdate: NotRequired[ParallelismConfigurationUpdateTypeDef]

class RunConfigurationDescriptionTypeDef(TypedDict):
    ApplicationRestoreConfigurationDescription: NotRequired[ApplicationRestoreConfigurationTypeDef]
    FlinkRunConfigurationDescription: NotRequired[FlinkRunConfigurationTypeDef]

class RunConfigurationUpdateTypeDef(TypedDict):
    FlinkRunConfiguration: NotRequired[FlinkRunConfigurationTypeDef]
    ApplicationRestoreConfiguration: NotRequired[ApplicationRestoreConfigurationTypeDef]

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

class ListApplicationOperationsRequestPaginateTypeDef(TypedDict):
    ApplicationName: str
    Operation: NotRequired[str]
    OperationStatus: NotRequired[OperationStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListApplicationSnapshotsRequestPaginateTypeDef(TypedDict):
    ApplicationName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListApplicationVersionsRequestPaginateTypeDef(TypedDict):
    ApplicationName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListApplicationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

PropertyGroupUnionTypeDef = Union[PropertyGroupTypeDef, PropertyGroupOutputTypeDef]

class ApplicationCodeConfigurationDescriptionTypeDef(TypedDict):
    CodeContentType: CodeContentTypeType
    CodeContentDescription: NotRequired[CodeContentDescriptionTypeDef]

class ApplicationCodeConfigurationTypeDef(TypedDict):
    CodeContentType: CodeContentTypeType
    CodeContent: NotRequired[CodeContentTypeDef]

class ApplicationCodeConfigurationUpdateTypeDef(TypedDict):
    CodeContentTypeUpdate: NotRequired[CodeContentTypeType]
    CodeContentUpdate: NotRequired[CodeContentUpdateTypeDef]

class ZeppelinApplicationConfigurationDescriptionTypeDef(TypedDict):
    MonitoringConfigurationDescription: ZeppelinMonitoringConfigurationDescriptionTypeDef
    CatalogConfigurationDescription: NotRequired[CatalogConfigurationDescriptionTypeDef]
    DeployAsApplicationConfigurationDescription: NotRequired[
        DeployAsApplicationConfigurationDescriptionTypeDef
    ]
    CustomArtifactsConfigurationDescription: NotRequired[
        List[CustomArtifactConfigurationDescriptionTypeDef]
    ]

class ZeppelinApplicationConfigurationTypeDef(TypedDict):
    MonitoringConfiguration: NotRequired[ZeppelinMonitoringConfigurationTypeDef]
    CatalogConfiguration: NotRequired[CatalogConfigurationTypeDef]
    DeployAsApplicationConfiguration: NotRequired[DeployAsApplicationConfigurationTypeDef]
    CustomArtifactsConfiguration: NotRequired[Sequence[CustomArtifactConfigurationTypeDef]]

class ZeppelinApplicationConfigurationUpdateTypeDef(TypedDict):
    MonitoringConfigurationUpdate: NotRequired[ZeppelinMonitoringConfigurationUpdateTypeDef]
    CatalogConfigurationUpdate: NotRequired[CatalogConfigurationUpdateTypeDef]
    DeployAsApplicationConfigurationUpdate: NotRequired[
        DeployAsApplicationConfigurationUpdateTypeDef
    ]
    CustomArtifactsConfigurationUpdate: NotRequired[Sequence[CustomArtifactConfigurationTypeDef]]

class RunConfigurationTypeDef(TypedDict):
    FlinkRunConfiguration: NotRequired[FlinkRunConfigurationTypeDef]
    SqlRunConfigurations: NotRequired[Sequence[SqlRunConfigurationTypeDef]]
    ApplicationRestoreConfiguration: NotRequired[ApplicationRestoreConfigurationTypeDef]

class ApplicationOperationInfoDetailsTypeDef(TypedDict):
    Operation: str
    StartTime: datetime
    EndTime: datetime
    OperationStatus: OperationStatusType
    ApplicationVersionChangeDetails: NotRequired[ApplicationVersionChangeDetailsTypeDef]
    OperationFailureDetails: NotRequired[OperationFailureDetailsTypeDef]

class AddApplicationInputProcessingConfigurationResponseTypeDef(TypedDict):
    ApplicationARN: str
    ApplicationVersionId: int
    InputId: str
    InputProcessingConfigurationDescription: InputProcessingConfigurationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddApplicationInputProcessingConfigurationRequestTypeDef(TypedDict):
    ApplicationName: str
    CurrentApplicationVersionId: int
    InputId: str
    InputProcessingConfiguration: InputProcessingConfigurationTypeDef

class DiscoverInputSchemaRequestTypeDef(TypedDict):
    ServiceExecutionRole: str
    ResourceARN: NotRequired[str]
    InputStartingPositionConfiguration: NotRequired[InputStartingPositionConfigurationTypeDef]
    S3Configuration: NotRequired[S3ConfigurationTypeDef]
    InputProcessingConfiguration: NotRequired[InputProcessingConfigurationTypeDef]

class RecordFormatTypeDef(TypedDict):
    RecordFormatType: RecordFormatTypeType
    MappingParameters: NotRequired[MappingParametersTypeDef]

class AddApplicationOutputResponseTypeDef(TypedDict):
    ApplicationARN: str
    ApplicationVersionId: int
    OutputDescriptions: List[OutputDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AddApplicationOutputRequestTypeDef(TypedDict):
    ApplicationName: str
    CurrentApplicationVersionId: int
    Output: OutputTypeDef

class EnvironmentPropertiesTypeDef(TypedDict):
    PropertyGroups: Sequence[PropertyGroupUnionTypeDef]

class EnvironmentPropertyUpdatesTypeDef(TypedDict):
    PropertyGroups: Sequence[PropertyGroupUnionTypeDef]

class StartApplicationRequestTypeDef(TypedDict):
    ApplicationName: str
    RunConfiguration: NotRequired[RunConfigurationTypeDef]

class DescribeApplicationOperationResponseTypeDef(TypedDict):
    ApplicationOperationInfoDetails: ApplicationOperationInfoDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

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

class AddApplicationInputResponseTypeDef(TypedDict):
    ApplicationARN: str
    ApplicationVersionId: int
    InputDescriptions: List[InputDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AddApplicationReferenceDataSourceResponseTypeDef(TypedDict):
    ApplicationARN: str
    ApplicationVersionId: int
    ReferenceDataSourceDescriptions: List[ReferenceDataSourceDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SqlApplicationConfigurationDescriptionTypeDef(TypedDict):
    InputDescriptions: NotRequired[List[InputDescriptionTypeDef]]
    OutputDescriptions: NotRequired[List[OutputDescriptionTypeDef]]
    ReferenceDataSourceDescriptions: NotRequired[List[ReferenceDataSourceDescriptionTypeDef]]

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

class ApplicationConfigurationDescriptionTypeDef(TypedDict):
    SqlApplicationConfigurationDescription: NotRequired[
        SqlApplicationConfigurationDescriptionTypeDef
    ]
    ApplicationCodeConfigurationDescription: NotRequired[
        ApplicationCodeConfigurationDescriptionTypeDef
    ]
    RunConfigurationDescription: NotRequired[RunConfigurationDescriptionTypeDef]
    FlinkApplicationConfigurationDescription: NotRequired[
        FlinkApplicationConfigurationDescriptionTypeDef
    ]
    EnvironmentPropertyDescriptions: NotRequired[EnvironmentPropertyDescriptionsTypeDef]
    ApplicationSnapshotConfigurationDescription: NotRequired[
        ApplicationSnapshotConfigurationDescriptionTypeDef
    ]
    ApplicationSystemRollbackConfigurationDescription: NotRequired[
        ApplicationSystemRollbackConfigurationDescriptionTypeDef
    ]
    VpcConfigurationDescriptions: NotRequired[List[VpcConfigurationDescriptionTypeDef]]
    ZeppelinApplicationConfigurationDescription: NotRequired[
        ZeppelinApplicationConfigurationDescriptionTypeDef
    ]

class AddApplicationInputRequestTypeDef(TypedDict):
    ApplicationName: str
    CurrentApplicationVersionId: int
    Input: InputTypeDef

class AddApplicationReferenceDataSourceRequestTypeDef(TypedDict):
    ApplicationName: str
    CurrentApplicationVersionId: int
    ReferenceDataSource: ReferenceDataSourceTypeDef

class SqlApplicationConfigurationTypeDef(TypedDict):
    Inputs: NotRequired[Sequence[InputTypeDef]]
    Outputs: NotRequired[Sequence[OutputTypeDef]]
    ReferenceDataSources: NotRequired[Sequence[ReferenceDataSourceTypeDef]]

class SqlApplicationConfigurationUpdateTypeDef(TypedDict):
    InputUpdates: NotRequired[Sequence[InputUpdateTypeDef]]
    OutputUpdates: NotRequired[Sequence[OutputUpdateTypeDef]]
    ReferenceDataSourceUpdates: NotRequired[Sequence[ReferenceDataSourceUpdateTypeDef]]

class ApplicationDetailTypeDef(TypedDict):
    ApplicationARN: str
    ApplicationName: str
    RuntimeEnvironment: RuntimeEnvironmentType
    ApplicationStatus: ApplicationStatusType
    ApplicationVersionId: int
    ApplicationDescription: NotRequired[str]
    ServiceExecutionRole: NotRequired[str]
    CreateTimestamp: NotRequired[datetime]
    LastUpdateTimestamp: NotRequired[datetime]
    ApplicationConfigurationDescription: NotRequired[ApplicationConfigurationDescriptionTypeDef]
    CloudWatchLoggingOptionDescriptions: NotRequired[
        List[CloudWatchLoggingOptionDescriptionTypeDef]
    ]
    ApplicationMaintenanceConfigurationDescription: NotRequired[
        ApplicationMaintenanceConfigurationDescriptionTypeDef
    ]
    ApplicationVersionUpdatedFrom: NotRequired[int]
    ApplicationVersionRolledBackFrom: NotRequired[int]
    ApplicationVersionCreateTimestamp: NotRequired[datetime]
    ConditionalToken: NotRequired[str]
    ApplicationVersionRolledBackTo: NotRequired[int]
    ApplicationMode: NotRequired[ApplicationModeType]

class ApplicationConfigurationTypeDef(TypedDict):
    SqlApplicationConfiguration: NotRequired[SqlApplicationConfigurationTypeDef]
    FlinkApplicationConfiguration: NotRequired[FlinkApplicationConfigurationTypeDef]
    EnvironmentProperties: NotRequired[EnvironmentPropertiesTypeDef]
    ApplicationCodeConfiguration: NotRequired[ApplicationCodeConfigurationTypeDef]
    ApplicationSnapshotConfiguration: NotRequired[ApplicationSnapshotConfigurationTypeDef]
    ApplicationSystemRollbackConfiguration: NotRequired[
        ApplicationSystemRollbackConfigurationTypeDef
    ]
    VpcConfigurations: NotRequired[Sequence[VpcConfigurationTypeDef]]
    ZeppelinApplicationConfiguration: NotRequired[ZeppelinApplicationConfigurationTypeDef]

class ApplicationConfigurationUpdateTypeDef(TypedDict):
    SqlApplicationConfigurationUpdate: NotRequired[SqlApplicationConfigurationUpdateTypeDef]
    ApplicationCodeConfigurationUpdate: NotRequired[ApplicationCodeConfigurationUpdateTypeDef]
    FlinkApplicationConfigurationUpdate: NotRequired[FlinkApplicationConfigurationUpdateTypeDef]
    EnvironmentPropertyUpdates: NotRequired[EnvironmentPropertyUpdatesTypeDef]
    ApplicationSnapshotConfigurationUpdate: NotRequired[
        ApplicationSnapshotConfigurationUpdateTypeDef
    ]
    ApplicationSystemRollbackConfigurationUpdate: NotRequired[
        ApplicationSystemRollbackConfigurationUpdateTypeDef
    ]
    VpcConfigurationUpdates: NotRequired[Sequence[VpcConfigurationUpdateTypeDef]]
    ZeppelinApplicationConfigurationUpdate: NotRequired[
        ZeppelinApplicationConfigurationUpdateTypeDef
    ]

class CreateApplicationResponseTypeDef(TypedDict):
    ApplicationDetail: ApplicationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationResponseTypeDef(TypedDict):
    ApplicationDetail: ApplicationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationVersionResponseTypeDef(TypedDict):
    ApplicationVersionDetail: ApplicationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RollbackApplicationResponseTypeDef(TypedDict):
    ApplicationDetail: ApplicationDetailTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationResponseTypeDef(TypedDict):
    ApplicationDetail: ApplicationDetailTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationRequestTypeDef(TypedDict):
    ApplicationName: str
    RuntimeEnvironment: RuntimeEnvironmentType
    ServiceExecutionRole: str
    ApplicationDescription: NotRequired[str]
    ApplicationConfiguration: NotRequired[ApplicationConfigurationTypeDef]
    CloudWatchLoggingOptions: NotRequired[Sequence[CloudWatchLoggingOptionTypeDef]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ApplicationMode: NotRequired[ApplicationModeType]

class UpdateApplicationRequestTypeDef(TypedDict):
    ApplicationName: str
    CurrentApplicationVersionId: NotRequired[int]
    ApplicationConfigurationUpdate: NotRequired[ApplicationConfigurationUpdateTypeDef]
    ServiceExecutionRoleUpdate: NotRequired[str]
    RunConfigurationUpdate: NotRequired[RunConfigurationUpdateTypeDef]
    CloudWatchLoggingOptionUpdates: NotRequired[Sequence[CloudWatchLoggingOptionUpdateTypeDef]]
    ConditionalToken: NotRequired[str]
    RuntimeEnvironmentUpdate: NotRequired[RuntimeEnvironmentType]
