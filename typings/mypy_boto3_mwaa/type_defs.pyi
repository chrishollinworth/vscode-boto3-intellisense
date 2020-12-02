"""
Main interface for mwaa service type definitions.

Usage::

    ```python
    from mypy_boto3_mwaa.type_defs import DimensionTypeDef

    data: DimensionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DimensionTypeDef",
    "EnvironmentTypeDef",
    "LastUpdateTypeDef",
    "LoggingConfigurationTypeDef",
    "ModuleLoggingConfigurationInputTypeDef",
    "ModuleLoggingConfigurationTypeDef",
    "NetworkConfigurationTypeDef",
    "ResponseMetadata",
    "StatisticSetTypeDef",
    "UpdateErrorTypeDef",
    "CreateCliTokenResponseTypeDef",
    "CreateEnvironmentOutputTypeDef",
    "CreateWebLoginTokenResponseTypeDef",
    "GetEnvironmentOutputTypeDef",
    "ListEnvironmentsOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LoggingConfigurationInputTypeDef",
    "MetricDatumTypeDef",
    "PaginatorConfigTypeDef",
    "UpdateEnvironmentOutputTypeDef",
    "UpdateNetworkConfigurationInputTypeDef",
)

DimensionTypeDef = TypedDict("DimensionTypeDef", {"Name": str, "Value": str})

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
        "Name": str,
        "NetworkConfiguration": "NetworkConfigurationTypeDef",
        "PluginsS3ObjectVersion": str,
        "PluginsS3Path": str,
        "RequirementsS3ObjectVersion": str,
        "RequirementsS3Path": str,
        "ServiceRoleArn": str,
        "SourceBucketArn": str,
        "Status": Literal[
            "CREATING", "CREATE_FAILED", "AVAILABLE", "UPDATING", "DELETING", "DELETED"
        ],
        "Tags": Dict[str, str],
        "WebserverAccessMode": Literal["PRIVATE_ONLY", "PUBLIC_ONLY"],
        "WebserverUrl": str,
        "WeeklyMaintenanceWindowStart": str,
    },
    total=False,
)

LastUpdateTypeDef = TypedDict(
    "LastUpdateTypeDef",
    {
        "CreatedAt": datetime,
        "Error": "UpdateErrorTypeDef",
        "Status": Literal["SUCCESS", "PENDING", "FAILED"],
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

ModuleLoggingConfigurationInputTypeDef = TypedDict(
    "ModuleLoggingConfigurationInputTypeDef",
    {"Enabled": bool, "LogLevel": Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]},
)

ModuleLoggingConfigurationTypeDef = TypedDict(
    "ModuleLoggingConfigurationTypeDef",
    {
        "CloudWatchLogGroupArn": str,
        "Enabled": bool,
        "LogLevel": Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"],
    },
    total=False,
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {"SecurityGroupIds": List[str], "SubnetIds": List[str]},
    total=False,
)

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

StatisticSetTypeDef = TypedDict(
    "StatisticSetTypeDef",
    {"Maximum": float, "Minimum": float, "SampleCount": int, "Sum": float},
    total=False,
)

UpdateErrorTypeDef = TypedDict(
    "UpdateErrorTypeDef", {"ErrorCode": str, "ErrorMessage": str}, total=False
)

CreateCliTokenResponseTypeDef = TypedDict(
    "CreateCliTokenResponseTypeDef", {"CliToken": str, "WebServerHostname": str}, total=False
)

CreateEnvironmentOutputTypeDef = TypedDict(
    "CreateEnvironmentOutputTypeDef",
    {"Arn": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateWebLoginTokenResponseTypeDef = TypedDict(
    "CreateWebLoginTokenResponseTypeDef", {"WebServerHostname": str, "WebToken": str}, total=False
)

GetEnvironmentOutputTypeDef = TypedDict(
    "GetEnvironmentOutputTypeDef",
    {"Environment": "EnvironmentTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredListEnvironmentsOutputTypeDef = TypedDict(
    "_RequiredListEnvironmentsOutputTypeDef", {"Environments": List[str]}
)
_OptionalListEnvironmentsOutputTypeDef = TypedDict(
    "_OptionalListEnvironmentsOutputTypeDef",
    {"NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListEnvironmentsOutputTypeDef(
    _RequiredListEnvironmentsOutputTypeDef, _OptionalListEnvironmentsOutputTypeDef
):
    pass


ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {"Tags": Dict[str, str], "ResponseMetadata": "ResponseMetadata"},
    total=False,
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

_RequiredMetricDatumTypeDef = TypedDict(
    "_RequiredMetricDatumTypeDef", {"MetricName": str, "Timestamp": datetime}
)
_OptionalMetricDatumTypeDef = TypedDict(
    "_OptionalMetricDatumTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
        "StatisticValues": "StatisticSetTypeDef",
        "Unit": Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ],
        "Value": float,
    },
    total=False,
)


class MetricDatumTypeDef(_RequiredMetricDatumTypeDef, _OptionalMetricDatumTypeDef):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UpdateEnvironmentOutputTypeDef = TypedDict(
    "UpdateEnvironmentOutputTypeDef",
    {"Arn": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateNetworkConfigurationInputTypeDef = TypedDict(
    "UpdateNetworkConfigurationInputTypeDef", {"SecurityGroupIds": List[str]}
)
