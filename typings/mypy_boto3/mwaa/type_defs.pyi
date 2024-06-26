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
    EndpointManagementType,
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
        "Name": str,
        "ExecutionRoleArn": str,
        "SourceBucketArn": str,
        "DagS3Path": str,
        "NetworkConfiguration": "NetworkConfigurationTypeDef",
    },
)
_OptionalCreateEnvironmentInputRequestTypeDef = TypedDict(
    "_OptionalCreateEnvironmentInputRequestTypeDef",
    {
        "PluginsS3Path": str,
        "PluginsS3ObjectVersion": str,
        "RequirementsS3Path": str,
        "RequirementsS3ObjectVersion": str,
        "StartupScriptS3Path": str,
        "StartupScriptS3ObjectVersion": str,
        "AirflowConfigurationOptions": Dict[str, str],
        "EnvironmentClass": str,
        "MaxWorkers": int,
        "KmsKey": str,
        "AirflowVersion": str,
        "LoggingConfiguration": "LoggingConfigurationInputTypeDef",
        "WeeklyMaintenanceWindowStart": str,
        "Tags": Dict[str, str],
        "WebserverAccessMode": WebserverAccessModeType,
        "MinWorkers": int,
        "Schedulers": int,
        "EndpointManagement": EndpointManagementType,
        "MinWebservers": int,
        "MaxWebservers": int,
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
        "WebToken": str,
        "WebServerHostname": str,
        "IamIdentity": str,
        "AirflowIdentity": str,
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
        "Name": str,
        "Status": EnvironmentStatusType,
        "Arn": str,
        "CreatedAt": datetime,
        "WebserverUrl": str,
        "ExecutionRoleArn": str,
        "ServiceRoleArn": str,
        "KmsKey": str,
        "AirflowVersion": str,
        "SourceBucketArn": str,
        "DagS3Path": str,
        "PluginsS3Path": str,
        "PluginsS3ObjectVersion": str,
        "RequirementsS3Path": str,
        "RequirementsS3ObjectVersion": str,
        "StartupScriptS3Path": str,
        "StartupScriptS3ObjectVersion": str,
        "AirflowConfigurationOptions": Dict[str, str],
        "EnvironmentClass": str,
        "MaxWorkers": int,
        "NetworkConfiguration": "NetworkConfigurationTypeDef",
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "LastUpdate": "LastUpdateTypeDef",
        "WeeklyMaintenanceWindowStart": str,
        "Tags": Dict[str, str],
        "WebserverAccessMode": WebserverAccessModeType,
        "MinWorkers": int,
        "Schedulers": int,
        "WebserverVpcEndpointService": str,
        "DatabaseVpcEndpointService": str,
        "CeleryExecutorQueue": str,
        "EndpointManagement": EndpointManagementType,
        "MinWebservers": int,
        "MaxWebservers": int,
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
        "Status": UpdateStatusType,
        "CreatedAt": datetime,
        "Error": "UpdateErrorTypeDef",
        "Source": str,
    },
    total=False,
)

ListEnvironmentsInputRequestTypeDef = TypedDict(
    "ListEnvironmentsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
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
        "WebserverLogs": "ModuleLoggingConfigurationInputTypeDef",
        "WorkerLogs": "ModuleLoggingConfigurationInputTypeDef",
        "TaskLogs": "ModuleLoggingConfigurationInputTypeDef",
    },
    total=False,
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "DagProcessingLogs": "ModuleLoggingConfigurationTypeDef",
        "SchedulerLogs": "ModuleLoggingConfigurationTypeDef",
        "WebserverLogs": "ModuleLoggingConfigurationTypeDef",
        "WorkerLogs": "ModuleLoggingConfigurationTypeDef",
        "TaskLogs": "ModuleLoggingConfigurationTypeDef",
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
        "Value": float,
        "Unit": UnitType,
        "StatisticValues": "StatisticSetTypeDef",
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
        "Enabled": bool,
        "LogLevel": LoggingLevelType,
        "CloudWatchLogGroupArn": str,
    },
    total=False,
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
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
        "SampleCount": int,
        "Sum": float,
        "Minimum": float,
        "Maximum": float,
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
        "ExecutionRoleArn": str,
        "AirflowVersion": str,
        "SourceBucketArn": str,
        "DagS3Path": str,
        "PluginsS3Path": str,
        "PluginsS3ObjectVersion": str,
        "RequirementsS3Path": str,
        "RequirementsS3ObjectVersion": str,
        "StartupScriptS3Path": str,
        "StartupScriptS3ObjectVersion": str,
        "AirflowConfigurationOptions": Dict[str, str],
        "EnvironmentClass": str,
        "MaxWorkers": int,
        "NetworkConfiguration": "UpdateNetworkConfigurationInputTypeDef",
        "LoggingConfiguration": "LoggingConfigurationInputTypeDef",
        "WeeklyMaintenanceWindowStart": str,
        "WebserverAccessMode": WebserverAccessModeType,
        "MinWorkers": int,
        "Schedulers": int,
        "MinWebservers": int,
        "MaxWebservers": int,
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
