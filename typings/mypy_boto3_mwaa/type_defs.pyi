"""
Type annotations for mwaa service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_mwaa.type_defs import CreateCliTokenRequestTypeDef

    data: CreateCliTokenRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    EndpointManagementType,
    EnvironmentStatusType,
    LoggingLevelType,
    RestApiMethodType,
    UnitType,
    UpdateStatusType,
    WebserverAccessModeType,
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
    "CreateCliTokenRequestTypeDef",
    "CreateCliTokenResponseTypeDef",
    "CreateEnvironmentInputTypeDef",
    "CreateEnvironmentOutputTypeDef",
    "CreateWebLoginTokenRequestTypeDef",
    "CreateWebLoginTokenResponseTypeDef",
    "DeleteEnvironmentInputTypeDef",
    "DimensionTypeDef",
    "EnvironmentTypeDef",
    "GetEnvironmentInputTypeDef",
    "GetEnvironmentOutputTypeDef",
    "InvokeRestApiRequestTypeDef",
    "InvokeRestApiResponseTypeDef",
    "LastUpdateTypeDef",
    "ListEnvironmentsInputPaginateTypeDef",
    "ListEnvironmentsInputTypeDef",
    "ListEnvironmentsOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LoggingConfigurationInputTypeDef",
    "LoggingConfigurationTypeDef",
    "MetricDatumTypeDef",
    "ModuleLoggingConfigurationInputTypeDef",
    "ModuleLoggingConfigurationTypeDef",
    "NetworkConfigurationOutputTypeDef",
    "NetworkConfigurationTypeDef",
    "NetworkConfigurationUnionTypeDef",
    "PaginatorConfigTypeDef",
    "PublishMetricsInputTypeDef",
    "ResponseMetadataTypeDef",
    "StatisticSetTypeDef",
    "TagResourceInputTypeDef",
    "TimestampTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateEnvironmentInputTypeDef",
    "UpdateEnvironmentOutputTypeDef",
    "UpdateErrorTypeDef",
    "UpdateNetworkConfigurationInputTypeDef",
)

class CreateCliTokenRequestTypeDef(TypedDict):
    Name: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateWebLoginTokenRequestTypeDef(TypedDict):
    Name: str

class DeleteEnvironmentInputTypeDef(TypedDict):
    Name: str

class DimensionTypeDef(TypedDict):
    Name: str
    Value: str

class NetworkConfigurationOutputTypeDef(TypedDict):
    SubnetIds: NotRequired[List[str]]
    SecurityGroupIds: NotRequired[List[str]]

class GetEnvironmentInputTypeDef(TypedDict):
    Name: str

class InvokeRestApiRequestTypeDef(TypedDict):
    Name: str
    Path: str
    Method: RestApiMethodType
    QueryParameters: NotRequired[Mapping[str, Any]]
    Body: NotRequired[Mapping[str, Any]]

class UpdateErrorTypeDef(TypedDict):
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListEnvironmentsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTagsForResourceInputTypeDef(TypedDict):
    ResourceArn: str

class ModuleLoggingConfigurationInputTypeDef(TypedDict):
    Enabled: bool
    LogLevel: LoggingLevelType

class ModuleLoggingConfigurationTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    LogLevel: NotRequired[LoggingLevelType]
    CloudWatchLogGroupArn: NotRequired[str]

class StatisticSetTypeDef(TypedDict):
    SampleCount: NotRequired[int]
    Sum: NotRequired[float]
    Minimum: NotRequired[float]
    Maximum: NotRequired[float]

TimestampTypeDef = Union[datetime, str]

class NetworkConfigurationTypeDef(TypedDict):
    SubnetIds: NotRequired[Sequence[str]]
    SecurityGroupIds: NotRequired[Sequence[str]]

class TagResourceInputTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceInputTypeDef(TypedDict):
    ResourceArn: str
    tagKeys: Sequence[str]

class UpdateNetworkConfigurationInputTypeDef(TypedDict):
    SecurityGroupIds: Sequence[str]

class CreateCliTokenResponseTypeDef(TypedDict):
    CliToken: str
    WebServerHostname: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWebLoginTokenResponseTypeDef(TypedDict):
    WebToken: str
    WebServerHostname: str
    IamIdentity: str
    AirflowIdentity: str
    ResponseMetadata: ResponseMetadataTypeDef

class InvokeRestApiResponseTypeDef(TypedDict):
    RestApiStatusCode: int
    RestApiResponse: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentsOutputTypeDef(TypedDict):
    Environments: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceOutputTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class LastUpdateTypeDef(TypedDict):
    Status: NotRequired[UpdateStatusType]
    CreatedAt: NotRequired[datetime]
    Error: NotRequired[UpdateErrorTypeDef]
    Source: NotRequired[str]

class ListEnvironmentsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class LoggingConfigurationInputTypeDef(TypedDict):
    DagProcessingLogs: NotRequired[ModuleLoggingConfigurationInputTypeDef]
    SchedulerLogs: NotRequired[ModuleLoggingConfigurationInputTypeDef]
    WebserverLogs: NotRequired[ModuleLoggingConfigurationInputTypeDef]
    WorkerLogs: NotRequired[ModuleLoggingConfigurationInputTypeDef]
    TaskLogs: NotRequired[ModuleLoggingConfigurationInputTypeDef]

class LoggingConfigurationTypeDef(TypedDict):
    DagProcessingLogs: NotRequired[ModuleLoggingConfigurationTypeDef]
    SchedulerLogs: NotRequired[ModuleLoggingConfigurationTypeDef]
    WebserverLogs: NotRequired[ModuleLoggingConfigurationTypeDef]
    WorkerLogs: NotRequired[ModuleLoggingConfigurationTypeDef]
    TaskLogs: NotRequired[ModuleLoggingConfigurationTypeDef]

class MetricDatumTypeDef(TypedDict):
    MetricName: str
    Timestamp: TimestampTypeDef
    Dimensions: NotRequired[Sequence[DimensionTypeDef]]
    Value: NotRequired[float]
    Unit: NotRequired[UnitType]
    StatisticValues: NotRequired[StatisticSetTypeDef]

NetworkConfigurationUnionTypeDef = Union[
    NetworkConfigurationTypeDef, NetworkConfigurationOutputTypeDef
]

class UpdateEnvironmentInputTypeDef(TypedDict):
    Name: str
    ExecutionRoleArn: NotRequired[str]
    AirflowVersion: NotRequired[str]
    SourceBucketArn: NotRequired[str]
    DagS3Path: NotRequired[str]
    PluginsS3Path: NotRequired[str]
    PluginsS3ObjectVersion: NotRequired[str]
    RequirementsS3Path: NotRequired[str]
    RequirementsS3ObjectVersion: NotRequired[str]
    StartupScriptS3Path: NotRequired[str]
    StartupScriptS3ObjectVersion: NotRequired[str]
    AirflowConfigurationOptions: NotRequired[Mapping[str, str]]
    EnvironmentClass: NotRequired[str]
    MaxWorkers: NotRequired[int]
    NetworkConfiguration: NotRequired[UpdateNetworkConfigurationInputTypeDef]
    LoggingConfiguration: NotRequired[LoggingConfigurationInputTypeDef]
    WeeklyMaintenanceWindowStart: NotRequired[str]
    WebserverAccessMode: NotRequired[WebserverAccessModeType]
    MinWorkers: NotRequired[int]
    Schedulers: NotRequired[int]
    MinWebservers: NotRequired[int]
    MaxWebservers: NotRequired[int]

class EnvironmentTypeDef(TypedDict):
    Name: NotRequired[str]
    Status: NotRequired[EnvironmentStatusType]
    Arn: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    WebserverUrl: NotRequired[str]
    ExecutionRoleArn: NotRequired[str]
    ServiceRoleArn: NotRequired[str]
    KmsKey: NotRequired[str]
    AirflowVersion: NotRequired[str]
    SourceBucketArn: NotRequired[str]
    DagS3Path: NotRequired[str]
    PluginsS3Path: NotRequired[str]
    PluginsS3ObjectVersion: NotRequired[str]
    RequirementsS3Path: NotRequired[str]
    RequirementsS3ObjectVersion: NotRequired[str]
    StartupScriptS3Path: NotRequired[str]
    StartupScriptS3ObjectVersion: NotRequired[str]
    AirflowConfigurationOptions: NotRequired[Dict[str, str]]
    EnvironmentClass: NotRequired[str]
    MaxWorkers: NotRequired[int]
    NetworkConfiguration: NotRequired[NetworkConfigurationOutputTypeDef]
    LoggingConfiguration: NotRequired[LoggingConfigurationTypeDef]
    LastUpdate: NotRequired[LastUpdateTypeDef]
    WeeklyMaintenanceWindowStart: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]
    WebserverAccessMode: NotRequired[WebserverAccessModeType]
    MinWorkers: NotRequired[int]
    Schedulers: NotRequired[int]
    WebserverVpcEndpointService: NotRequired[str]
    DatabaseVpcEndpointService: NotRequired[str]
    CeleryExecutorQueue: NotRequired[str]
    EndpointManagement: NotRequired[EndpointManagementType]
    MinWebservers: NotRequired[int]
    MaxWebservers: NotRequired[int]

class PublishMetricsInputTypeDef(TypedDict):
    EnvironmentName: str
    MetricData: Sequence[MetricDatumTypeDef]

class CreateEnvironmentInputTypeDef(TypedDict):
    Name: str
    ExecutionRoleArn: str
    SourceBucketArn: str
    DagS3Path: str
    NetworkConfiguration: NetworkConfigurationUnionTypeDef
    PluginsS3Path: NotRequired[str]
    PluginsS3ObjectVersion: NotRequired[str]
    RequirementsS3Path: NotRequired[str]
    RequirementsS3ObjectVersion: NotRequired[str]
    StartupScriptS3Path: NotRequired[str]
    StartupScriptS3ObjectVersion: NotRequired[str]
    AirflowConfigurationOptions: NotRequired[Mapping[str, str]]
    EnvironmentClass: NotRequired[str]
    MaxWorkers: NotRequired[int]
    KmsKey: NotRequired[str]
    AirflowVersion: NotRequired[str]
    LoggingConfiguration: NotRequired[LoggingConfigurationInputTypeDef]
    WeeklyMaintenanceWindowStart: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    WebserverAccessMode: NotRequired[WebserverAccessModeType]
    MinWorkers: NotRequired[int]
    Schedulers: NotRequired[int]
    EndpointManagement: NotRequired[EndpointManagementType]
    MinWebservers: NotRequired[int]
    MaxWebservers: NotRequired[int]

class GetEnvironmentOutputTypeDef(TypedDict):
    Environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
