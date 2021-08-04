"""
Type annotations for mwaa service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mwaa.type_defs import CreateCliTokenRequestRequestTypeDef

    data: CreateCliTokenRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    EnvironmentStatusType,
    LoggingLevelType,
    UnitType,
    UpdateStatusType,
    WebserverAccessModeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateCliTokenRequestRequestTypeDef",
    "CreateCliTokenResponseTypeDef",
    "CreateEnvironmentInputRequestTypeDef",
    "CreateEnvironmentOutputTypeDef",
    "CreateWebLoginTokenRequestRequestTypeDef",
    "CreateWebLoginTokenResponseTypeDef",
    "DeleteEnvironmentInputRequestTypeDef",
    "DimensionTypeDef",
    "EnvironmentTypeDef",
    "GetEnvironmentInputRequestTypeDef",
    "GetEnvironmentOutputTypeDef",
    "LastUpdateTypeDef",
    "ListEnvironmentsInputRequestTypeDef",
    "ListEnvironmentsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LoggingConfigurationInputTypeDef",
    "LoggingConfigurationTypeDef",
    "MetricDatumTypeDef",
    "ModuleLoggingConfigurationInputTypeDef",
    "ModuleLoggingConfigurationTypeDef",
    "NetworkConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PublishMetricsInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "StatisticSetTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateEnvironmentInputRequestTypeDef",
    "UpdateEnvironmentOutputTypeDef",
    "UpdateErrorTypeDef",
    "UpdateNetworkConfigurationInputTypeDef",
)

CreateCliTokenRequestRequestTypeDef = TypedDict(
    "CreateCliTokenRequestRequestTypeDef",
    {
        "Name": str,
    },
)

CreateCliTokenResponseTypeDef = TypedDict(
    "CreateCliTokenResponseTypeDef",
    {
        "CliToken": str,
        "WebServerHostname": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEnvironmentInputRequestTypeDef = TypedDict(
    "_RequiredCreateEnvironmentInputRequestTypeDef",
    {
        "DagS3Path": str,
        "ExecutionRoleArn": str,
        "Name": str,
        "NetworkConfiguration": "NetworkConfigurationTypeDef",
        "SourceBucketArn": str,
    },
)
_OptionalCreateEnvironmentInputRequestTypeDef = TypedDict(
    "_OptionalCreateEnvironmentInputRequestTypeDef",
    {
        "AirflowConfigurationOptions": Dict[str, str],
        "AirflowVersion": str,
        "EnvironmentClass": str,
        "KmsKey": str,
        "LoggingConfiguration": "LoggingConfigurationInputTypeDef",
        "MaxWorkers": int,
        "MinWorkers": int,
        "PluginsS3ObjectVersion": str,
        "PluginsS3Path": str,
        "RequirementsS3ObjectVersion": str,
        "RequirementsS3Path": str,
        "Schedulers": int,
        "Tags": Dict[str, str],
        "WebserverAccessMode": WebserverAccessModeType,
        "WeeklyMaintenanceWindowStart": str,
    },
    total=False,
)

class CreateEnvironmentInputRequestTypeDef(
    _RequiredCreateEnvironmentInputRequestTypeDef, _OptionalCreateEnvironmentInputRequestTypeDef
):
    pass

CreateEnvironmentOutputTypeDef = TypedDict(
    "CreateEnvironmentOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWebLoginTokenRequestRequestTypeDef = TypedDict(
    "CreateWebLoginTokenRequestRequestTypeDef",
    {
        "Name": str,
    },
)

CreateWebLoginTokenResponseTypeDef = TypedDict(
    "CreateWebLoginTokenResponseTypeDef",
    {
        "WebServerHostname": str,
        "WebToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentInputRequestTypeDef",
    {
        "Name": str,
    },
)

DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "AirflowConfigurationOptions": Dict[str, str],
        "AirflowVersion": str,
        "Arn": str,
        "CreatedAt": datetime,
        "DagS3Path": str,
        "EnvironmentClass": str,
        "ExecutionRoleArn": str,
        "KmsKey": str,
        "LastUpdate": "LastUpdateTypeDef",
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "MaxWorkers": int,
        "MinWorkers": int,
        "Name": str,
        "NetworkConfiguration": "NetworkConfigurationTypeDef",
        "PluginsS3ObjectVersion": str,
        "PluginsS3Path": str,
        "RequirementsS3ObjectVersion": str,
        "RequirementsS3Path": str,
        "Schedulers": int,
        "ServiceRoleArn": str,
        "SourceBucketArn": str,
        "Status": EnvironmentStatusType,
        "Tags": Dict[str, str],
        "WebserverAccessMode": WebserverAccessModeType,
        "WebserverUrl": str,
        "WeeklyMaintenanceWindowStart": str,
    },
    total=False,
)

GetEnvironmentInputRequestTypeDef = TypedDict(
    "GetEnvironmentInputRequestTypeDef",
    {
        "Name": str,
    },
)

GetEnvironmentOutputTypeDef = TypedDict(
    "GetEnvironmentOutputTypeDef",
    {
        "Environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LastUpdateTypeDef = TypedDict(
    "LastUpdateTypeDef",
    {
        "CreatedAt": datetime,
        "Error": "UpdateErrorTypeDef",
        "Status": UpdateStatusType,
    },
    total=False,
)

ListEnvironmentsInputRequestTypeDef = TypedDict(
    "ListEnvironmentsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListEnvironmentsOutputTypeDef = TypedDict(
    "ListEnvironmentsOutputTypeDef",
    {
        "Environments": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingConfigurationInputTypeDef = TypedDict(
    "LoggingConfigurationInputTypeDef",
    {
        "DagProcessingLogs": "ModuleLoggingConfigurationInputTypeDef",
        "SchedulerLogs": "ModuleLoggingConfigurationInputTypeDef",
        "TaskLogs": "ModuleLoggingConfigurationInputTypeDef",
        "WebserverLogs": "ModuleLoggingConfigurationInputTypeDef",
        "WorkerLogs": "ModuleLoggingConfigurationInputTypeDef",
    },
    total=False,
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "DagProcessingLogs": "ModuleLoggingConfigurationTypeDef",
        "SchedulerLogs": "ModuleLoggingConfigurationTypeDef",
        "TaskLogs": "ModuleLoggingConfigurationTypeDef",
        "WebserverLogs": "ModuleLoggingConfigurationTypeDef",
        "WorkerLogs": "ModuleLoggingConfigurationTypeDef",
    },
    total=False,
)

_RequiredMetricDatumTypeDef = TypedDict(
    "_RequiredMetricDatumTypeDef",
    {
        "MetricName": str,
        "Timestamp": Union[datetime, str],
    },
)
_OptionalMetricDatumTypeDef = TypedDict(
    "_OptionalMetricDatumTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
        "StatisticValues": "StatisticSetTypeDef",
        "Unit": UnitType,
        "Value": float,
    },
    total=False,
)

class MetricDatumTypeDef(_RequiredMetricDatumTypeDef, _OptionalMetricDatumTypeDef):
    pass

ModuleLoggingConfigurationInputTypeDef = TypedDict(
    "ModuleLoggingConfigurationInputTypeDef",
    {
        "Enabled": bool,
        "LogLevel": LoggingLevelType,
    },
)

ModuleLoggingConfigurationTypeDef = TypedDict(
    "ModuleLoggingConfigurationTypeDef",
    {
        "CloudWatchLogGroupArn": str,
        "Enabled": bool,
        "LogLevel": LoggingLevelType,
    },
    total=False,
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
    },
    total=False,
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

PublishMetricsInputRequestTypeDef = TypedDict(
    "PublishMetricsInputRequestTypeDef",
    {
        "EnvironmentName": str,
        "MetricData": List["MetricDatumTypeDef"],
    },
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

StatisticSetTypeDef = TypedDict(
    "StatisticSetTypeDef",
    {
        "Maximum": float,
        "Minimum": float,
        "SampleCount": int,
        "Sum": float,
    },
    total=False,
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateEnvironmentInputRequestTypeDef = TypedDict(
    "_RequiredUpdateEnvironmentInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateEnvironmentInputRequestTypeDef = TypedDict(
    "_OptionalUpdateEnvironmentInputRequestTypeDef",
    {
        "AirflowConfigurationOptions": Dict[str, str],
        "AirflowVersion": str,
        "DagS3Path": str,
        "EnvironmentClass": str,
        "ExecutionRoleArn": str,
        "LoggingConfiguration": "LoggingConfigurationInputTypeDef",
        "MaxWorkers": int,
        "MinWorkers": int,
        "NetworkConfiguration": "UpdateNetworkConfigurationInputTypeDef",
        "PluginsS3ObjectVersion": str,
        "PluginsS3Path": str,
        "RequirementsS3ObjectVersion": str,
        "RequirementsS3Path": str,
        "Schedulers": int,
        "SourceBucketArn": str,
        "WebserverAccessMode": WebserverAccessModeType,
        "WeeklyMaintenanceWindowStart": str,
    },
    total=False,
)

class UpdateEnvironmentInputRequestTypeDef(
    _RequiredUpdateEnvironmentInputRequestTypeDef, _OptionalUpdateEnvironmentInputRequestTypeDef
):
    pass

UpdateEnvironmentOutputTypeDef = TypedDict(
    "UpdateEnvironmentOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateErrorTypeDef = TypedDict(
    "UpdateErrorTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

UpdateNetworkConfigurationInputTypeDef = TypedDict(
    "UpdateNetworkConfigurationInputTypeDef",
    {
        "SecurityGroupIds": List[str],
    },
)
