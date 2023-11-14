"""
Type annotations for simspaceweaver service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_simspaceweaver/type_defs.html)

Usage::

    ```python
    from mypy_boto3_simspaceweaver.type_defs import CloudWatchLogsLogGroupTypeDef

    data: CloudWatchLogsLogGroupTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ClockStatusType,
    ClockTargetStatusType,
    LifecycleManagementStrategyType,
    SimulationAppStatusType,
    SimulationAppTargetStatusType,
    SimulationStatusType,
    SimulationTargetStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CloudWatchLogsLogGroupTypeDef",
    "CreateSnapshotInputRequestTypeDef",
    "DeleteAppInputRequestTypeDef",
    "DeleteSimulationInputRequestTypeDef",
    "DescribeAppInputRequestTypeDef",
    "DescribeAppOutputTypeDef",
    "DescribeSimulationInputRequestTypeDef",
    "DescribeSimulationOutputTypeDef",
    "DomainTypeDef",
    "LaunchOverridesTypeDef",
    "ListAppsInputRequestTypeDef",
    "ListAppsOutputTypeDef",
    "ListSimulationsInputRequestTypeDef",
    "ListSimulationsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LiveSimulationStateTypeDef",
    "LogDestinationTypeDef",
    "LoggingConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationTypeDef",
    "S3LocationTypeDef",
    "SimulationAppEndpointInfoTypeDef",
    "SimulationAppMetadataTypeDef",
    "SimulationAppPortMappingTypeDef",
    "SimulationClockTypeDef",
    "SimulationMetadataTypeDef",
    "StartAppInputRequestTypeDef",
    "StartAppOutputTypeDef",
    "StartClockInputRequestTypeDef",
    "StartSimulationInputRequestTypeDef",
    "StartSimulationOutputTypeDef",
    "StopAppInputRequestTypeDef",
    "StopClockInputRequestTypeDef",
    "StopSimulationInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
)

CloudWatchLogsLogGroupTypeDef = TypedDict(
    "CloudWatchLogsLogGroupTypeDef",
    {
        "LogGroupArn": str,
    },
    total=False,
)

CreateSnapshotInputRequestTypeDef = TypedDict(
    "CreateSnapshotInputRequestTypeDef",
    {
        "Destination": "S3DestinationTypeDef",
        "Simulation": str,
    },
)

DeleteAppInputRequestTypeDef = TypedDict(
    "DeleteAppInputRequestTypeDef",
    {
        "App": str,
        "Domain": str,
        "Simulation": str,
    },
)

DeleteSimulationInputRequestTypeDef = TypedDict(
    "DeleteSimulationInputRequestTypeDef",
    {
        "Simulation": str,
    },
)

DescribeAppInputRequestTypeDef = TypedDict(
    "DescribeAppInputRequestTypeDef",
    {
        "App": str,
        "Domain": str,
        "Simulation": str,
    },
)

DescribeAppOutputTypeDef = TypedDict(
    "DescribeAppOutputTypeDef",
    {
        "Description": str,
        "Domain": str,
        "EndpointInfo": "SimulationAppEndpointInfoTypeDef",
        "LaunchOverrides": "LaunchOverridesTypeDef",
        "Name": str,
        "Simulation": str,
        "Status": SimulationAppStatusType,
        "TargetStatus": SimulationAppTargetStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSimulationInputRequestTypeDef = TypedDict(
    "DescribeSimulationInputRequestTypeDef",
    {
        "Simulation": str,
    },
)

DescribeSimulationOutputTypeDef = TypedDict(
    "DescribeSimulationOutputTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "ExecutionId": str,
        "LiveSimulationState": "LiveSimulationStateTypeDef",
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "MaximumDuration": str,
        "Name": str,
        "RoleArn": str,
        "SchemaError": str,
        "SchemaS3Location": "S3LocationTypeDef",
        "SnapshotS3Location": "S3LocationTypeDef",
        "StartError": str,
        "Status": SimulationStatusType,
        "TargetStatus": SimulationTargetStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainTypeDef = TypedDict(
    "DomainTypeDef",
    {
        "Lifecycle": LifecycleManagementStrategyType,
        "Name": str,
    },
    total=False,
)

LaunchOverridesTypeDef = TypedDict(
    "LaunchOverridesTypeDef",
    {
        "LaunchCommands": List[str],
    },
    total=False,
)

_RequiredListAppsInputRequestTypeDef = TypedDict(
    "_RequiredListAppsInputRequestTypeDef",
    {
        "Simulation": str,
    },
)
_OptionalListAppsInputRequestTypeDef = TypedDict(
    "_OptionalListAppsInputRequestTypeDef",
    {
        "Domain": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAppsInputRequestTypeDef(
    _RequiredListAppsInputRequestTypeDef, _OptionalListAppsInputRequestTypeDef
):
    pass

ListAppsOutputTypeDef = TypedDict(
    "ListAppsOutputTypeDef",
    {
        "Apps": List["SimulationAppMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSimulationsInputRequestTypeDef = TypedDict(
    "ListSimulationsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSimulationsOutputTypeDef = TypedDict(
    "ListSimulationsOutputTypeDef",
    {
        "NextToken": str,
        "Simulations": List["SimulationMetadataTypeDef"],
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

LiveSimulationStateTypeDef = TypedDict(
    "LiveSimulationStateTypeDef",
    {
        "Clocks": List["SimulationClockTypeDef"],
        "Domains": List["DomainTypeDef"],
    },
    total=False,
)

LogDestinationTypeDef = TypedDict(
    "LogDestinationTypeDef",
    {
        "CloudWatchLogsLogGroup": "CloudWatchLogsLogGroupTypeDef",
    },
    total=False,
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "Destinations": List["LogDestinationTypeDef"],
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

_RequiredS3DestinationTypeDef = TypedDict(
    "_RequiredS3DestinationTypeDef",
    {
        "BucketName": str,
    },
)
_OptionalS3DestinationTypeDef = TypedDict(
    "_OptionalS3DestinationTypeDef",
    {
        "ObjectKeyPrefix": str,
    },
    total=False,
)

class S3DestinationTypeDef(_RequiredS3DestinationTypeDef, _OptionalS3DestinationTypeDef):
    pass

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "BucketName": str,
        "ObjectKey": str,
    },
)

SimulationAppEndpointInfoTypeDef = TypedDict(
    "SimulationAppEndpointInfoTypeDef",
    {
        "Address": str,
        "IngressPortMappings": List["SimulationAppPortMappingTypeDef"],
    },
    total=False,
)

SimulationAppMetadataTypeDef = TypedDict(
    "SimulationAppMetadataTypeDef",
    {
        "Domain": str,
        "Name": str,
        "Simulation": str,
        "Status": SimulationAppStatusType,
        "TargetStatus": SimulationAppTargetStatusType,
    },
    total=False,
)

SimulationAppPortMappingTypeDef = TypedDict(
    "SimulationAppPortMappingTypeDef",
    {
        "Actual": int,
        "Declared": int,
    },
    total=False,
)

SimulationClockTypeDef = TypedDict(
    "SimulationClockTypeDef",
    {
        "Status": ClockStatusType,
        "TargetStatus": ClockTargetStatusType,
    },
    total=False,
)

SimulationMetadataTypeDef = TypedDict(
    "SimulationMetadataTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Name": str,
        "Status": SimulationStatusType,
        "TargetStatus": SimulationTargetStatusType,
    },
    total=False,
)

_RequiredStartAppInputRequestTypeDef = TypedDict(
    "_RequiredStartAppInputRequestTypeDef",
    {
        "Domain": str,
        "Name": str,
        "Simulation": str,
    },
)
_OptionalStartAppInputRequestTypeDef = TypedDict(
    "_OptionalStartAppInputRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "LaunchOverrides": "LaunchOverridesTypeDef",
    },
    total=False,
)

class StartAppInputRequestTypeDef(
    _RequiredStartAppInputRequestTypeDef, _OptionalStartAppInputRequestTypeDef
):
    pass

StartAppOutputTypeDef = TypedDict(
    "StartAppOutputTypeDef",
    {
        "Domain": str,
        "Name": str,
        "Simulation": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartClockInputRequestTypeDef = TypedDict(
    "StartClockInputRequestTypeDef",
    {
        "Simulation": str,
    },
)

_RequiredStartSimulationInputRequestTypeDef = TypedDict(
    "_RequiredStartSimulationInputRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
    },
)
_OptionalStartSimulationInputRequestTypeDef = TypedDict(
    "_OptionalStartSimulationInputRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "MaximumDuration": str,
        "SchemaS3Location": "S3LocationTypeDef",
        "SnapshotS3Location": "S3LocationTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

class StartSimulationInputRequestTypeDef(
    _RequiredStartSimulationInputRequestTypeDef, _OptionalStartSimulationInputRequestTypeDef
):
    pass

StartSimulationOutputTypeDef = TypedDict(
    "StartSimulationOutputTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "ExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopAppInputRequestTypeDef = TypedDict(
    "StopAppInputRequestTypeDef",
    {
        "App": str,
        "Domain": str,
        "Simulation": str,
    },
)

StopClockInputRequestTypeDef = TypedDict(
    "StopClockInputRequestTypeDef",
    {
        "Simulation": str,
    },
)

StopSimulationInputRequestTypeDef = TypedDict(
    "StopSimulationInputRequestTypeDef",
    {
        "Simulation": str,
    },
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
        "TagKeys": List[str],
    },
)
