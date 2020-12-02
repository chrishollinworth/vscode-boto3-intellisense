"""
Main interface for kinesisanalyticsv2 service type definitions.

Usage::

    ```python
    from mypy_boto3_kinesisanalyticsv2.type_defs import ApplicationCodeConfigurationDescriptionTypeDef

    data: ApplicationCodeConfigurationDescriptionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationCodeConfigurationDescriptionTypeDef",
    "ApplicationCodeConfigurationTypeDef",
    "ApplicationCodeConfigurationUpdateTypeDef",
    "ApplicationConfigurationDescriptionTypeDef",
    "ApplicationDetailTypeDef",
    "ApplicationRestoreConfigurationTypeDef",
    "ApplicationSnapshotConfigurationDescriptionTypeDef",
    "ApplicationSnapshotConfigurationTypeDef",
    "ApplicationSnapshotConfigurationUpdateTypeDef",
    "ApplicationSummaryTypeDef",
    "CSVMappingParametersTypeDef",
    "CheckpointConfigurationDescriptionTypeDef",
    "CheckpointConfigurationTypeDef",
    "CheckpointConfigurationUpdateTypeDef",
    "CloudWatchLoggingOptionDescriptionTypeDef",
    "CodeContentDescriptionTypeDef",
    "CodeContentTypeDef",
    "CodeContentUpdateTypeDef",
    "DestinationSchemaTypeDef",
    "EnvironmentPropertiesTypeDef",
    "EnvironmentPropertyDescriptionsTypeDef",
    "EnvironmentPropertyUpdatesTypeDef",
    "FlinkApplicationConfigurationDescriptionTypeDef",
    "FlinkApplicationConfigurationTypeDef",
    "FlinkApplicationConfigurationUpdateTypeDef",
    "FlinkRunConfigurationTypeDef",
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
    "MappingParametersTypeDef",
    "MonitoringConfigurationDescriptionTypeDef",
    "MonitoringConfigurationTypeDef",
    "MonitoringConfigurationUpdateTypeDef",
    "OutputDescriptionTypeDef",
    "OutputTypeDef",
    "OutputUpdateTypeDef",
    "ParallelismConfigurationDescriptionTypeDef",
    "ParallelismConfigurationTypeDef",
    "ParallelismConfigurationUpdateTypeDef",
    "PropertyGroupTypeDef",
    "RecordColumnTypeDef",
    "RecordFormatTypeDef",
    "ReferenceDataSourceDescriptionTypeDef",
    "ReferenceDataSourceTypeDef",
    "ReferenceDataSourceUpdateTypeDef",
    "ResponseMetadata",
    "RunConfigurationDescriptionTypeDef",
    "S3ApplicationCodeLocationDescriptionTypeDef",
    "S3ContentLocationTypeDef",
    "S3ContentLocationUpdateTypeDef",
    "S3ReferenceDataSourceDescriptionTypeDef",
    "S3ReferenceDataSourceTypeDef",
    "S3ReferenceDataSourceUpdateTypeDef",
    "SnapshotDetailsTypeDef",
    "SourceSchemaTypeDef",
    "SqlApplicationConfigurationDescriptionTypeDef",
    "SqlApplicationConfigurationTypeDef",
    "SqlApplicationConfigurationUpdateTypeDef",
    "SqlRunConfigurationTypeDef",
    "TagTypeDef",
    "VpcConfigurationDescriptionTypeDef",
    "VpcConfigurationTypeDef",
    "VpcConfigurationUpdateTypeDef",
    "AddApplicationCloudWatchLoggingOptionResponseTypeDef",
    "AddApplicationInputProcessingConfigurationResponseTypeDef",
    "AddApplicationInputResponseTypeDef",
    "AddApplicationOutputResponseTypeDef",
    "AddApplicationReferenceDataSourceResponseTypeDef",
    "AddApplicationVpcConfigurationResponseTypeDef",
    "ApplicationConfigurationTypeDef",
    "ApplicationConfigurationUpdateTypeDef",
    "CloudWatchLoggingOptionTypeDef",
    "CloudWatchLoggingOptionUpdateTypeDef",
    "CreateApplicationPresignedUrlResponseTypeDef",
    "CreateApplicationResponseTypeDef",
    "DeleteApplicationCloudWatchLoggingOptionResponseTypeDef",
    "DeleteApplicationInputProcessingConfigurationResponseTypeDef",
    "DeleteApplicationOutputResponseTypeDef",
    "DeleteApplicationReferenceDataSourceResponseTypeDef",
    "DeleteApplicationVpcConfigurationResponseTypeDef",
    "DescribeApplicationResponseTypeDef",
    "DescribeApplicationSnapshotResponseTypeDef",
    "DiscoverInputSchemaResponseTypeDef",
    "ListApplicationSnapshotsResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RunConfigurationTypeDef",
    "RunConfigurationUpdateTypeDef",
    "S3ConfigurationTypeDef",
    "UpdateApplicationResponseTypeDef",
)

_RequiredApplicationCodeConfigurationDescriptionTypeDef = TypedDict(
    "_RequiredApplicationCodeConfigurationDescriptionTypeDef",
    {"CodeContentType": Literal["PLAINTEXT", "ZIPFILE"]},
)
_OptionalApplicationCodeConfigurationDescriptionTypeDef = TypedDict(
    "_OptionalApplicationCodeConfigurationDescriptionTypeDef",
    {"CodeContentDescription": "CodeContentDescriptionTypeDef"},
    total=False,
)


class ApplicationCodeConfigurationDescriptionTypeDef(
    _RequiredApplicationCodeConfigurationDescriptionTypeDef,
    _OptionalApplicationCodeConfigurationDescriptionTypeDef,
):
    pass


_RequiredApplicationCodeConfigurationTypeDef = TypedDict(
    "_RequiredApplicationCodeConfigurationTypeDef",
    {"CodeContentType": Literal["PLAINTEXT", "ZIPFILE"]},
)
_OptionalApplicationCodeConfigurationTypeDef = TypedDict(
    "_OptionalApplicationCodeConfigurationTypeDef",
    {"CodeContent": "CodeContentTypeDef"},
    total=False,
)


class ApplicationCodeConfigurationTypeDef(
    _RequiredApplicationCodeConfigurationTypeDef, _OptionalApplicationCodeConfigurationTypeDef
):
    pass


ApplicationCodeConfigurationUpdateTypeDef = TypedDict(
    "ApplicationCodeConfigurationUpdateTypeDef",
    {
        "CodeContentTypeUpdate": Literal["PLAINTEXT", "ZIPFILE"],
        "CodeContentUpdate": "CodeContentUpdateTypeDef",
    },
    total=False,
)

ApplicationConfigurationDescriptionTypeDef = TypedDict(
    "ApplicationConfigurationDescriptionTypeDef",
    {
        "SqlApplicationConfigurationDescription": "SqlApplicationConfigurationDescriptionTypeDef",
        "ApplicationCodeConfigurationDescription": "ApplicationCodeConfigurationDescriptionTypeDef",
        "RunConfigurationDescription": "RunConfigurationDescriptionTypeDef",
        "FlinkApplicationConfigurationDescription": "FlinkApplicationConfigurationDescriptionTypeDef",
        "EnvironmentPropertyDescriptions": "EnvironmentPropertyDescriptionsTypeDef",
        "ApplicationSnapshotConfigurationDescription": "ApplicationSnapshotConfigurationDescriptionTypeDef",
        "VpcConfigurationDescriptions": List["VpcConfigurationDescriptionTypeDef"],
    },
    total=False,
)

_RequiredApplicationDetailTypeDef = TypedDict(
    "_RequiredApplicationDetailTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationName": str,
        "RuntimeEnvironment": Literal["SQL-1_0", "FLINK-1_6", "FLINK-1_8", "FLINK-1_11"],
        "ApplicationStatus": Literal[
            "DELETING",
            "STARTING",
            "STOPPING",
            "READY",
            "RUNNING",
            "UPDATING",
            "AUTOSCALING",
            "FORCE_STOPPING",
        ],
        "ApplicationVersionId": int,
    },
)
_OptionalApplicationDetailTypeDef = TypedDict(
    "_OptionalApplicationDetailTypeDef",
    {
        "ApplicationDescription": str,
        "ServiceExecutionRole": str,
        "CreateTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "ApplicationConfigurationDescription": "ApplicationConfigurationDescriptionTypeDef",
        "CloudWatchLoggingOptionDescriptions": List["CloudWatchLoggingOptionDescriptionTypeDef"],
    },
    total=False,
)


class ApplicationDetailTypeDef(
    _RequiredApplicationDetailTypeDef, _OptionalApplicationDetailTypeDef
):
    pass


_RequiredApplicationRestoreConfigurationTypeDef = TypedDict(
    "_RequiredApplicationRestoreConfigurationTypeDef",
    {
        "ApplicationRestoreType": Literal[
            "SKIP_RESTORE_FROM_SNAPSHOT",
            "RESTORE_FROM_LATEST_SNAPSHOT",
            "RESTORE_FROM_CUSTOM_SNAPSHOT",
        ]
    },
)
_OptionalApplicationRestoreConfigurationTypeDef = TypedDict(
    "_OptionalApplicationRestoreConfigurationTypeDef", {"SnapshotName": str}, total=False
)


class ApplicationRestoreConfigurationTypeDef(
    _RequiredApplicationRestoreConfigurationTypeDef, _OptionalApplicationRestoreConfigurationTypeDef
):
    pass


ApplicationSnapshotConfigurationDescriptionTypeDef = TypedDict(
    "ApplicationSnapshotConfigurationDescriptionTypeDef", {"SnapshotsEnabled": bool}
)

ApplicationSnapshotConfigurationTypeDef = TypedDict(
    "ApplicationSnapshotConfigurationTypeDef", {"SnapshotsEnabled": bool}
)

ApplicationSnapshotConfigurationUpdateTypeDef = TypedDict(
    "ApplicationSnapshotConfigurationUpdateTypeDef", {"SnapshotsEnabledUpdate": bool}
)

ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "ApplicationName": str,
        "ApplicationARN": str,
        "ApplicationStatus": Literal[
            "DELETING",
            "STARTING",
            "STOPPING",
            "READY",
            "RUNNING",
            "UPDATING",
            "AUTOSCALING",
            "FORCE_STOPPING",
        ],
        "ApplicationVersionId": int,
        "RuntimeEnvironment": Literal["SQL-1_0", "FLINK-1_6", "FLINK-1_8", "FLINK-1_11"],
    },
)

CSVMappingParametersTypeDef = TypedDict(
    "CSVMappingParametersTypeDef", {"RecordRowDelimiter": str, "RecordColumnDelimiter": str}
)

CheckpointConfigurationDescriptionTypeDef = TypedDict(
    "CheckpointConfigurationDescriptionTypeDef",
    {
        "ConfigurationType": Literal["DEFAULT", "CUSTOM"],
        "CheckpointingEnabled": bool,
        "CheckpointInterval": int,
        "MinPauseBetweenCheckpoints": int,
    },
    total=False,
)

_RequiredCheckpointConfigurationTypeDef = TypedDict(
    "_RequiredCheckpointConfigurationTypeDef", {"ConfigurationType": Literal["DEFAULT", "CUSTOM"]}
)
_OptionalCheckpointConfigurationTypeDef = TypedDict(
    "_OptionalCheckpointConfigurationTypeDef",
    {"CheckpointingEnabled": bool, "CheckpointInterval": int, "MinPauseBetweenCheckpoints": int},
    total=False,
)


class CheckpointConfigurationTypeDef(
    _RequiredCheckpointConfigurationTypeDef, _OptionalCheckpointConfigurationTypeDef
):
    pass


CheckpointConfigurationUpdateTypeDef = TypedDict(
    "CheckpointConfigurationUpdateTypeDef",
    {
        "ConfigurationTypeUpdate": Literal["DEFAULT", "CUSTOM"],
        "CheckpointingEnabledUpdate": bool,
        "CheckpointIntervalUpdate": int,
        "MinPauseBetweenCheckpointsUpdate": int,
    },
    total=False,
)

_RequiredCloudWatchLoggingOptionDescriptionTypeDef = TypedDict(
    "_RequiredCloudWatchLoggingOptionDescriptionTypeDef", {"LogStreamARN": str}
)
_OptionalCloudWatchLoggingOptionDescriptionTypeDef = TypedDict(
    "_OptionalCloudWatchLoggingOptionDescriptionTypeDef",
    {"CloudWatchLoggingOptionId": str, "RoleARN": str},
    total=False,
)


class CloudWatchLoggingOptionDescriptionTypeDef(
    _RequiredCloudWatchLoggingOptionDescriptionTypeDef,
    _OptionalCloudWatchLoggingOptionDescriptionTypeDef,
):
    pass


CodeContentDescriptionTypeDef = TypedDict(
    "CodeContentDescriptionTypeDef",
    {
        "TextContent": str,
        "CodeMD5": str,
        "CodeSize": int,
        "S3ApplicationCodeLocationDescription": "S3ApplicationCodeLocationDescriptionTypeDef",
    },
    total=False,
)

CodeContentTypeDef = TypedDict(
    "CodeContentTypeDef",
    {
        "TextContent": str,
        "ZipFileContent": Union[bytes, IO[bytes]],
        "S3ContentLocation": "S3ContentLocationTypeDef",
    },
    total=False,
)

CodeContentUpdateTypeDef = TypedDict(
    "CodeContentUpdateTypeDef",
    {
        "TextContentUpdate": str,
        "ZipFileContentUpdate": Union[bytes, IO[bytes]],
        "S3ContentLocationUpdate": "S3ContentLocationUpdateTypeDef",
    },
    total=False,
)

DestinationSchemaTypeDef = TypedDict(
    "DestinationSchemaTypeDef", {"RecordFormatType": Literal["JSON", "CSV"]}
)

EnvironmentPropertiesTypeDef = TypedDict(
    "EnvironmentPropertiesTypeDef", {"PropertyGroups": List["PropertyGroupTypeDef"]}
)

EnvironmentPropertyDescriptionsTypeDef = TypedDict(
    "EnvironmentPropertyDescriptionsTypeDef",
    {"PropertyGroupDescriptions": List["PropertyGroupTypeDef"]},
    total=False,
)

EnvironmentPropertyUpdatesTypeDef = TypedDict(
    "EnvironmentPropertyUpdatesTypeDef", {"PropertyGroups": List["PropertyGroupTypeDef"]}
)

FlinkApplicationConfigurationDescriptionTypeDef = TypedDict(
    "FlinkApplicationConfigurationDescriptionTypeDef",
    {
        "CheckpointConfigurationDescription": "CheckpointConfigurationDescriptionTypeDef",
        "MonitoringConfigurationDescription": "MonitoringConfigurationDescriptionTypeDef",
        "ParallelismConfigurationDescription": "ParallelismConfigurationDescriptionTypeDef",
        "JobPlanDescription": str,
    },
    total=False,
)

FlinkApplicationConfigurationTypeDef = TypedDict(
    "FlinkApplicationConfigurationTypeDef",
    {
        "CheckpointConfiguration": "CheckpointConfigurationTypeDef",
        "MonitoringConfiguration": "MonitoringConfigurationTypeDef",
        "ParallelismConfiguration": "ParallelismConfigurationTypeDef",
    },
    total=False,
)

FlinkApplicationConfigurationUpdateTypeDef = TypedDict(
    "FlinkApplicationConfigurationUpdateTypeDef",
    {
        "CheckpointConfigurationUpdate": "CheckpointConfigurationUpdateTypeDef",
        "MonitoringConfigurationUpdate": "MonitoringConfigurationUpdateTypeDef",
        "ParallelismConfigurationUpdate": "ParallelismConfigurationUpdateTypeDef",
    },
    total=False,
)

FlinkRunConfigurationTypeDef = TypedDict(
    "FlinkRunConfigurationTypeDef", {"AllowNonRestoredState": bool}, total=False
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

_RequiredInputLambdaProcessorDescriptionTypeDef = TypedDict(
    "_RequiredInputLambdaProcessorDescriptionTypeDef", {"ResourceARN": str}
)
_OptionalInputLambdaProcessorDescriptionTypeDef = TypedDict(
    "_OptionalInputLambdaProcessorDescriptionTypeDef", {"RoleARN": str}, total=False
)


class InputLambdaProcessorDescriptionTypeDef(
    _RequiredInputLambdaProcessorDescriptionTypeDef, _OptionalInputLambdaProcessorDescriptionTypeDef
):
    pass


InputLambdaProcessorTypeDef = TypedDict("InputLambdaProcessorTypeDef", {"ResourceARN": str})

InputLambdaProcessorUpdateTypeDef = TypedDict(
    "InputLambdaProcessorUpdateTypeDef", {"ResourceARNUpdate": str}
)

InputParallelismTypeDef = TypedDict("InputParallelismTypeDef", {"Count": int}, total=False)

InputParallelismUpdateTypeDef = TypedDict("InputParallelismUpdateTypeDef", {"CountUpdate": int})

InputProcessingConfigurationDescriptionTypeDef = TypedDict(
    "InputProcessingConfigurationDescriptionTypeDef",
    {"InputLambdaProcessorDescription": "InputLambdaProcessorDescriptionTypeDef"},
    total=False,
)

InputProcessingConfigurationTypeDef = TypedDict(
    "InputProcessingConfigurationTypeDef", {"InputLambdaProcessor": "InputLambdaProcessorTypeDef"}
)

InputProcessingConfigurationUpdateTypeDef = TypedDict(
    "InputProcessingConfigurationUpdateTypeDef",
    {"InputLambdaProcessorUpdate": "InputLambdaProcessorUpdateTypeDef"},
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
    {"InputStartingPosition": Literal["NOW", "TRIM_HORIZON", "LAST_STOPPED_POINT"]},
    total=False,
)

_RequiredInputTypeDef = TypedDict(
    "_RequiredInputTypeDef", {"NamePrefix": str, "InputSchema": "SourceSchemaTypeDef"}
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


_RequiredInputUpdateTypeDef = TypedDict("_RequiredInputUpdateTypeDef", {"InputId": str})
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


JSONMappingParametersTypeDef = TypedDict("JSONMappingParametersTypeDef", {"RecordRowPath": str})

_RequiredKinesisFirehoseInputDescriptionTypeDef = TypedDict(
    "_RequiredKinesisFirehoseInputDescriptionTypeDef", {"ResourceARN": str}
)
_OptionalKinesisFirehoseInputDescriptionTypeDef = TypedDict(
    "_OptionalKinesisFirehoseInputDescriptionTypeDef", {"RoleARN": str}, total=False
)


class KinesisFirehoseInputDescriptionTypeDef(
    _RequiredKinesisFirehoseInputDescriptionTypeDef, _OptionalKinesisFirehoseInputDescriptionTypeDef
):
    pass


KinesisFirehoseInputTypeDef = TypedDict("KinesisFirehoseInputTypeDef", {"ResourceARN": str})

KinesisFirehoseInputUpdateTypeDef = TypedDict(
    "KinesisFirehoseInputUpdateTypeDef", {"ResourceARNUpdate": str}
)

_RequiredKinesisFirehoseOutputDescriptionTypeDef = TypedDict(
    "_RequiredKinesisFirehoseOutputDescriptionTypeDef", {"ResourceARN": str}
)
_OptionalKinesisFirehoseOutputDescriptionTypeDef = TypedDict(
    "_OptionalKinesisFirehoseOutputDescriptionTypeDef", {"RoleARN": str}, total=False
)


class KinesisFirehoseOutputDescriptionTypeDef(
    _RequiredKinesisFirehoseOutputDescriptionTypeDef,
    _OptionalKinesisFirehoseOutputDescriptionTypeDef,
):
    pass


_RequiredKinesisFirehoseOutputTypeDef = TypedDict(
    "_RequiredKinesisFirehoseOutputTypeDef", {"ResourceARN": str}
)
_OptionalKinesisFirehoseOutputTypeDef = TypedDict(
    "_OptionalKinesisFirehoseOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class KinesisFirehoseOutputTypeDef(
    _RequiredKinesisFirehoseOutputTypeDef, _OptionalKinesisFirehoseOutputTypeDef
):
    pass


KinesisFirehoseOutputUpdateTypeDef = TypedDict(
    "KinesisFirehoseOutputUpdateTypeDef", {"ResourceARNUpdate": str}
)

_RequiredKinesisStreamsInputDescriptionTypeDef = TypedDict(
    "_RequiredKinesisStreamsInputDescriptionTypeDef", {"ResourceARN": str}
)
_OptionalKinesisStreamsInputDescriptionTypeDef = TypedDict(
    "_OptionalKinesisStreamsInputDescriptionTypeDef", {"RoleARN": str}, total=False
)


class KinesisStreamsInputDescriptionTypeDef(
    _RequiredKinesisStreamsInputDescriptionTypeDef, _OptionalKinesisStreamsInputDescriptionTypeDef
):
    pass


KinesisStreamsInputTypeDef = TypedDict("KinesisStreamsInputTypeDef", {"ResourceARN": str})

KinesisStreamsInputUpdateTypeDef = TypedDict(
    "KinesisStreamsInputUpdateTypeDef", {"ResourceARNUpdate": str}
)

_RequiredKinesisStreamsOutputDescriptionTypeDef = TypedDict(
    "_RequiredKinesisStreamsOutputDescriptionTypeDef", {"ResourceARN": str}
)
_OptionalKinesisStreamsOutputDescriptionTypeDef = TypedDict(
    "_OptionalKinesisStreamsOutputDescriptionTypeDef", {"RoleARN": str}, total=False
)


class KinesisStreamsOutputDescriptionTypeDef(
    _RequiredKinesisStreamsOutputDescriptionTypeDef, _OptionalKinesisStreamsOutputDescriptionTypeDef
):
    pass


_RequiredKinesisStreamsOutputTypeDef = TypedDict(
    "_RequiredKinesisStreamsOutputTypeDef", {"ResourceARN": str}
)
_OptionalKinesisStreamsOutputTypeDef = TypedDict(
    "_OptionalKinesisStreamsOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class KinesisStreamsOutputTypeDef(
    _RequiredKinesisStreamsOutputTypeDef, _OptionalKinesisStreamsOutputTypeDef
):
    pass


KinesisStreamsOutputUpdateTypeDef = TypedDict(
    "KinesisStreamsOutputUpdateTypeDef", {"ResourceARNUpdate": str}
)

_RequiredLambdaOutputDescriptionTypeDef = TypedDict(
    "_RequiredLambdaOutputDescriptionTypeDef", {"ResourceARN": str}
)
_OptionalLambdaOutputDescriptionTypeDef = TypedDict(
    "_OptionalLambdaOutputDescriptionTypeDef", {"RoleARN": str}, total=False
)


class LambdaOutputDescriptionTypeDef(
    _RequiredLambdaOutputDescriptionTypeDef, _OptionalLambdaOutputDescriptionTypeDef
):
    pass


_RequiredLambdaOutputTypeDef = TypedDict("_RequiredLambdaOutputTypeDef", {"ResourceARN": str})
_OptionalLambdaOutputTypeDef = TypedDict(
    "_OptionalLambdaOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class LambdaOutputTypeDef(_RequiredLambdaOutputTypeDef, _OptionalLambdaOutputTypeDef):
    pass


LambdaOutputUpdateTypeDef = TypedDict("LambdaOutputUpdateTypeDef", {"ResourceARNUpdate": str})

MappingParametersTypeDef = TypedDict(
    "MappingParametersTypeDef",
    {
        "JSONMappingParameters": "JSONMappingParametersTypeDef",
        "CSVMappingParameters": "CSVMappingParametersTypeDef",
    },
    total=False,
)

MonitoringConfigurationDescriptionTypeDef = TypedDict(
    "MonitoringConfigurationDescriptionTypeDef",
    {
        "ConfigurationType": Literal["DEFAULT", "CUSTOM"],
        "MetricsLevel": Literal["APPLICATION", "TASK", "OPERATOR", "PARALLELISM"],
        "LogLevel": Literal["INFO", "WARN", "ERROR", "DEBUG"],
    },
    total=False,
)

_RequiredMonitoringConfigurationTypeDef = TypedDict(
    "_RequiredMonitoringConfigurationTypeDef", {"ConfigurationType": Literal["DEFAULT", "CUSTOM"]}
)
_OptionalMonitoringConfigurationTypeDef = TypedDict(
    "_OptionalMonitoringConfigurationTypeDef",
    {
        "MetricsLevel": Literal["APPLICATION", "TASK", "OPERATOR", "PARALLELISM"],
        "LogLevel": Literal["INFO", "WARN", "ERROR", "DEBUG"],
    },
    total=False,
)


class MonitoringConfigurationTypeDef(
    _RequiredMonitoringConfigurationTypeDef, _OptionalMonitoringConfigurationTypeDef
):
    pass


MonitoringConfigurationUpdateTypeDef = TypedDict(
    "MonitoringConfigurationUpdateTypeDef",
    {
        "ConfigurationTypeUpdate": Literal["DEFAULT", "CUSTOM"],
        "MetricsLevelUpdate": Literal["APPLICATION", "TASK", "OPERATOR", "PARALLELISM"],
        "LogLevelUpdate": Literal["INFO", "WARN", "ERROR", "DEBUG"],
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
    "_RequiredOutputTypeDef", {"Name": str, "DestinationSchema": "DestinationSchemaTypeDef"}
)
_OptionalOutputTypeDef = TypedDict(
    "_OptionalOutputTypeDef",
    {
        "KinesisStreamsOutput": "KinesisStreamsOutputTypeDef",
        "KinesisFirehoseOutput": "KinesisFirehoseOutputTypeDef",
        "LambdaOutput": "LambdaOutputTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class OutputTypeDef(_RequiredOutputTypeDef, _OptionalOutputTypeDef):
    pass


_RequiredOutputUpdateTypeDef = TypedDict("_RequiredOutputUpdateTypeDef", {"OutputId": str})
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


ParallelismConfigurationDescriptionTypeDef = TypedDict(
    "ParallelismConfigurationDescriptionTypeDef",
    {
        "ConfigurationType": Literal["DEFAULT", "CUSTOM"],
        "Parallelism": int,
        "ParallelismPerKPU": int,
        "CurrentParallelism": int,
        "AutoScalingEnabled": bool,
    },
    total=False,
)

_RequiredParallelismConfigurationTypeDef = TypedDict(
    "_RequiredParallelismConfigurationTypeDef", {"ConfigurationType": Literal["DEFAULT", "CUSTOM"]}
)
_OptionalParallelismConfigurationTypeDef = TypedDict(
    "_OptionalParallelismConfigurationTypeDef",
    {"Parallelism": int, "ParallelismPerKPU": int, "AutoScalingEnabled": bool},
    total=False,
)


class ParallelismConfigurationTypeDef(
    _RequiredParallelismConfigurationTypeDef, _OptionalParallelismConfigurationTypeDef
):
    pass


ParallelismConfigurationUpdateTypeDef = TypedDict(
    "ParallelismConfigurationUpdateTypeDef",
    {
        "ConfigurationTypeUpdate": Literal["DEFAULT", "CUSTOM"],
        "ParallelismUpdate": int,
        "ParallelismPerKPUUpdate": int,
        "AutoScalingEnabledUpdate": bool,
    },
    total=False,
)

PropertyGroupTypeDef = TypedDict(
    "PropertyGroupTypeDef", {"PropertyGroupId": str, "PropertyMap": Dict[str, str]}
)

_RequiredRecordColumnTypeDef = TypedDict(
    "_RequiredRecordColumnTypeDef", {"Name": str, "SqlType": str}
)
_OptionalRecordColumnTypeDef = TypedDict(
    "_OptionalRecordColumnTypeDef", {"Mapping": str}, total=False
)


class RecordColumnTypeDef(_RequiredRecordColumnTypeDef, _OptionalRecordColumnTypeDef):
    pass


_RequiredRecordFormatTypeDef = TypedDict(
    "_RequiredRecordFormatTypeDef", {"RecordFormatType": Literal["JSON", "CSV"]}
)
_OptionalRecordFormatTypeDef = TypedDict(
    "_OptionalRecordFormatTypeDef", {"MappingParameters": "MappingParametersTypeDef"}, total=False
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
    {"ReferenceSchema": "SourceSchemaTypeDef"},
    total=False,
)


class ReferenceDataSourceDescriptionTypeDef(
    _RequiredReferenceDataSourceDescriptionTypeDef, _OptionalReferenceDataSourceDescriptionTypeDef
):
    pass


_RequiredReferenceDataSourceTypeDef = TypedDict(
    "_RequiredReferenceDataSourceTypeDef",
    {"TableName": str, "ReferenceSchema": "SourceSchemaTypeDef"},
)
_OptionalReferenceDataSourceTypeDef = TypedDict(
    "_OptionalReferenceDataSourceTypeDef",
    {"S3ReferenceDataSource": "S3ReferenceDataSourceTypeDef"},
    total=False,
)


class ReferenceDataSourceTypeDef(
    _RequiredReferenceDataSourceTypeDef, _OptionalReferenceDataSourceTypeDef
):
    pass


_RequiredReferenceDataSourceUpdateTypeDef = TypedDict(
    "_RequiredReferenceDataSourceUpdateTypeDef", {"ReferenceId": str}
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


ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RunConfigurationDescriptionTypeDef = TypedDict(
    "RunConfigurationDescriptionTypeDef",
    {
        "ApplicationRestoreConfigurationDescription": "ApplicationRestoreConfigurationTypeDef",
        "FlinkRunConfigurationDescription": "FlinkRunConfigurationTypeDef",
    },
    total=False,
)

_RequiredS3ApplicationCodeLocationDescriptionTypeDef = TypedDict(
    "_RequiredS3ApplicationCodeLocationDescriptionTypeDef", {"BucketARN": str, "FileKey": str}
)
_OptionalS3ApplicationCodeLocationDescriptionTypeDef = TypedDict(
    "_OptionalS3ApplicationCodeLocationDescriptionTypeDef", {"ObjectVersion": str}, total=False
)


class S3ApplicationCodeLocationDescriptionTypeDef(
    _RequiredS3ApplicationCodeLocationDescriptionTypeDef,
    _OptionalS3ApplicationCodeLocationDescriptionTypeDef,
):
    pass


_RequiredS3ContentLocationTypeDef = TypedDict(
    "_RequiredS3ContentLocationTypeDef", {"BucketARN": str, "FileKey": str}
)
_OptionalS3ContentLocationTypeDef = TypedDict(
    "_OptionalS3ContentLocationTypeDef", {"ObjectVersion": str}, total=False
)


class S3ContentLocationTypeDef(
    _RequiredS3ContentLocationTypeDef, _OptionalS3ContentLocationTypeDef
):
    pass


S3ContentLocationUpdateTypeDef = TypedDict(
    "S3ContentLocationUpdateTypeDef",
    {"BucketARNUpdate": str, "FileKeyUpdate": str, "ObjectVersionUpdate": str},
    total=False,
)

_RequiredS3ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "_RequiredS3ReferenceDataSourceDescriptionTypeDef", {"BucketARN": str, "FileKey": str}
)
_OptionalS3ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "_OptionalS3ReferenceDataSourceDescriptionTypeDef", {"ReferenceRoleARN": str}, total=False
)


class S3ReferenceDataSourceDescriptionTypeDef(
    _RequiredS3ReferenceDataSourceDescriptionTypeDef,
    _OptionalS3ReferenceDataSourceDescriptionTypeDef,
):
    pass


S3ReferenceDataSourceTypeDef = TypedDict(
    "S3ReferenceDataSourceTypeDef", {"BucketARN": str, "FileKey": str}, total=False
)

S3ReferenceDataSourceUpdateTypeDef = TypedDict(
    "S3ReferenceDataSourceUpdateTypeDef",
    {"BucketARNUpdate": str, "FileKeyUpdate": str},
    total=False,
)

_RequiredSnapshotDetailsTypeDef = TypedDict(
    "_RequiredSnapshotDetailsTypeDef",
    {
        "SnapshotName": str,
        "SnapshotStatus": Literal["CREATING", "READY", "DELETING", "FAILED"],
        "ApplicationVersionId": int,
    },
)
_OptionalSnapshotDetailsTypeDef = TypedDict(
    "_OptionalSnapshotDetailsTypeDef", {"SnapshotCreationTimestamp": datetime}, total=False
)


class SnapshotDetailsTypeDef(_RequiredSnapshotDetailsTypeDef, _OptionalSnapshotDetailsTypeDef):
    pass


_RequiredSourceSchemaTypeDef = TypedDict(
    "_RequiredSourceSchemaTypeDef",
    {"RecordFormat": "RecordFormatTypeDef", "RecordColumns": List["RecordColumnTypeDef"]},
)
_OptionalSourceSchemaTypeDef = TypedDict(
    "_OptionalSourceSchemaTypeDef", {"RecordEncoding": str}, total=False
)


class SourceSchemaTypeDef(_RequiredSourceSchemaTypeDef, _OptionalSourceSchemaTypeDef):
    pass


SqlApplicationConfigurationDescriptionTypeDef = TypedDict(
    "SqlApplicationConfigurationDescriptionTypeDef",
    {
        "InputDescriptions": List["InputDescriptionTypeDef"],
        "OutputDescriptions": List["OutputDescriptionTypeDef"],
        "ReferenceDataSourceDescriptions": List["ReferenceDataSourceDescriptionTypeDef"],
    },
    total=False,
)

SqlApplicationConfigurationTypeDef = TypedDict(
    "SqlApplicationConfigurationTypeDef",
    {
        "Inputs": List["InputTypeDef"],
        "Outputs": List["OutputTypeDef"],
        "ReferenceDataSources": List["ReferenceDataSourceTypeDef"],
    },
    total=False,
)

SqlApplicationConfigurationUpdateTypeDef = TypedDict(
    "SqlApplicationConfigurationUpdateTypeDef",
    {
        "InputUpdates": List["InputUpdateTypeDef"],
        "OutputUpdates": List["OutputUpdateTypeDef"],
        "ReferenceDataSourceUpdates": List["ReferenceDataSourceUpdateTypeDef"],
    },
    total=False,
)

SqlRunConfigurationTypeDef = TypedDict(
    "SqlRunConfigurationTypeDef",
    {
        "InputId": str,
        "InputStartingPositionConfiguration": "InputStartingPositionConfigurationTypeDef",
    },
)

_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"Key": str})
_OptionalTagTypeDef = TypedDict("_OptionalTagTypeDef", {"Value": str}, total=False)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


VpcConfigurationDescriptionTypeDef = TypedDict(
    "VpcConfigurationDescriptionTypeDef",
    {
        "VpcConfigurationId": str,
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef", {"SubnetIds": List[str], "SecurityGroupIds": List[str]}
)

_RequiredVpcConfigurationUpdateTypeDef = TypedDict(
    "_RequiredVpcConfigurationUpdateTypeDef", {"VpcConfigurationId": str}
)
_OptionalVpcConfigurationUpdateTypeDef = TypedDict(
    "_OptionalVpcConfigurationUpdateTypeDef",
    {"SubnetIdUpdates": List[str], "SecurityGroupIdUpdates": List[str]},
    total=False,
)


class VpcConfigurationUpdateTypeDef(
    _RequiredVpcConfigurationUpdateTypeDef, _OptionalVpcConfigurationUpdateTypeDef
):
    pass


AddApplicationCloudWatchLoggingOptionResponseTypeDef = TypedDict(
    "AddApplicationCloudWatchLoggingOptionResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "CloudWatchLoggingOptionDescriptions": List["CloudWatchLoggingOptionDescriptionTypeDef"],
    },
    total=False,
)

AddApplicationInputProcessingConfigurationResponseTypeDef = TypedDict(
    "AddApplicationInputProcessingConfigurationResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "InputId": str,
        "InputProcessingConfigurationDescription": "InputProcessingConfigurationDescriptionTypeDef",
    },
    total=False,
)

AddApplicationInputResponseTypeDef = TypedDict(
    "AddApplicationInputResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "InputDescriptions": List["InputDescriptionTypeDef"],
    },
    total=False,
)

AddApplicationOutputResponseTypeDef = TypedDict(
    "AddApplicationOutputResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "OutputDescriptions": List["OutputDescriptionTypeDef"],
    },
    total=False,
)

AddApplicationReferenceDataSourceResponseTypeDef = TypedDict(
    "AddApplicationReferenceDataSourceResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "ReferenceDataSourceDescriptions": List["ReferenceDataSourceDescriptionTypeDef"],
    },
    total=False,
)

AddApplicationVpcConfigurationResponseTypeDef = TypedDict(
    "AddApplicationVpcConfigurationResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "VpcConfigurationDescription": "VpcConfigurationDescriptionTypeDef",
    },
    total=False,
)

_RequiredApplicationConfigurationTypeDef = TypedDict(
    "_RequiredApplicationConfigurationTypeDef",
    {"ApplicationCodeConfiguration": "ApplicationCodeConfigurationTypeDef"},
)
_OptionalApplicationConfigurationTypeDef = TypedDict(
    "_OptionalApplicationConfigurationTypeDef",
    {
        "SqlApplicationConfiguration": "SqlApplicationConfigurationTypeDef",
        "FlinkApplicationConfiguration": "FlinkApplicationConfigurationTypeDef",
        "EnvironmentProperties": "EnvironmentPropertiesTypeDef",
        "ApplicationSnapshotConfiguration": "ApplicationSnapshotConfigurationTypeDef",
        "VpcConfigurations": List["VpcConfigurationTypeDef"],
    },
    total=False,
)


class ApplicationConfigurationTypeDef(
    _RequiredApplicationConfigurationTypeDef, _OptionalApplicationConfigurationTypeDef
):
    pass


ApplicationConfigurationUpdateTypeDef = TypedDict(
    "ApplicationConfigurationUpdateTypeDef",
    {
        "SqlApplicationConfigurationUpdate": "SqlApplicationConfigurationUpdateTypeDef",
        "ApplicationCodeConfigurationUpdate": "ApplicationCodeConfigurationUpdateTypeDef",
        "FlinkApplicationConfigurationUpdate": "FlinkApplicationConfigurationUpdateTypeDef",
        "EnvironmentPropertyUpdates": "EnvironmentPropertyUpdatesTypeDef",
        "ApplicationSnapshotConfigurationUpdate": "ApplicationSnapshotConfigurationUpdateTypeDef",
        "VpcConfigurationUpdates": List["VpcConfigurationUpdateTypeDef"],
    },
    total=False,
)

CloudWatchLoggingOptionTypeDef = TypedDict("CloudWatchLoggingOptionTypeDef", {"LogStreamARN": str})

_RequiredCloudWatchLoggingOptionUpdateTypeDef = TypedDict(
    "_RequiredCloudWatchLoggingOptionUpdateTypeDef", {"CloudWatchLoggingOptionId": str}
)
_OptionalCloudWatchLoggingOptionUpdateTypeDef = TypedDict(
    "_OptionalCloudWatchLoggingOptionUpdateTypeDef", {"LogStreamARNUpdate": str}, total=False
)


class CloudWatchLoggingOptionUpdateTypeDef(
    _RequiredCloudWatchLoggingOptionUpdateTypeDef, _OptionalCloudWatchLoggingOptionUpdateTypeDef
):
    pass


CreateApplicationPresignedUrlResponseTypeDef = TypedDict(
    "CreateApplicationPresignedUrlResponseTypeDef", {"AuthorizedUrl": str}, total=False
)

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef", {"ApplicationDetail": "ApplicationDetailTypeDef"}
)

DeleteApplicationCloudWatchLoggingOptionResponseTypeDef = TypedDict(
    "DeleteApplicationCloudWatchLoggingOptionResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "CloudWatchLoggingOptionDescriptions": List["CloudWatchLoggingOptionDescriptionTypeDef"],
    },
    total=False,
)

DeleteApplicationInputProcessingConfigurationResponseTypeDef = TypedDict(
    "DeleteApplicationInputProcessingConfigurationResponseTypeDef",
    {"ApplicationARN": str, "ApplicationVersionId": int},
    total=False,
)

DeleteApplicationOutputResponseTypeDef = TypedDict(
    "DeleteApplicationOutputResponseTypeDef",
    {"ApplicationARN": str, "ApplicationVersionId": int},
    total=False,
)

DeleteApplicationReferenceDataSourceResponseTypeDef = TypedDict(
    "DeleteApplicationReferenceDataSourceResponseTypeDef",
    {"ApplicationARN": str, "ApplicationVersionId": int},
    total=False,
)

DeleteApplicationVpcConfigurationResponseTypeDef = TypedDict(
    "DeleteApplicationVpcConfigurationResponseTypeDef",
    {"ApplicationARN": str, "ApplicationVersionId": int},
    total=False,
)

DescribeApplicationResponseTypeDef = TypedDict(
    "DescribeApplicationResponseTypeDef", {"ApplicationDetail": "ApplicationDetailTypeDef"}
)

DescribeApplicationSnapshotResponseTypeDef = TypedDict(
    "DescribeApplicationSnapshotResponseTypeDef", {"SnapshotDetails": "SnapshotDetailsTypeDef"}
)

DiscoverInputSchemaResponseTypeDef = TypedDict(
    "DiscoverInputSchemaResponseTypeDef",
    {
        "InputSchema": "SourceSchemaTypeDef",
        "ParsedInputRecords": List[List[str]],
        "ProcessedInputRecords": List[str],
        "RawInputRecords": List[str],
    },
    total=False,
)

ListApplicationSnapshotsResponseTypeDef = TypedDict(
    "ListApplicationSnapshotsResponseTypeDef",
    {"SnapshotSummaries": List["SnapshotDetailsTypeDef"], "NextToken": str},
    total=False,
)

_RequiredListApplicationsResponseTypeDef = TypedDict(
    "_RequiredListApplicationsResponseTypeDef",
    {"ApplicationSummaries": List["ApplicationSummaryTypeDef"]},
)
_OptionalListApplicationsResponseTypeDef = TypedDict(
    "_OptionalListApplicationsResponseTypeDef", {"NextToken": str}, total=False
)


class ListApplicationsResponseTypeDef(
    _RequiredListApplicationsResponseTypeDef, _OptionalListApplicationsResponseTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RunConfigurationTypeDef = TypedDict(
    "RunConfigurationTypeDef",
    {
        "FlinkRunConfiguration": "FlinkRunConfigurationTypeDef",
        "SqlRunConfigurations": List["SqlRunConfigurationTypeDef"],
        "ApplicationRestoreConfiguration": "ApplicationRestoreConfigurationTypeDef",
    },
    total=False,
)

RunConfigurationUpdateTypeDef = TypedDict(
    "RunConfigurationUpdateTypeDef",
    {
        "FlinkRunConfiguration": "FlinkRunConfigurationTypeDef",
        "ApplicationRestoreConfiguration": "ApplicationRestoreConfigurationTypeDef",
    },
    total=False,
)

S3ConfigurationTypeDef = TypedDict("S3ConfigurationTypeDef", {"BucketARN": str, "FileKey": str})

UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef", {"ApplicationDetail": "ApplicationDetailTypeDef"}
)
