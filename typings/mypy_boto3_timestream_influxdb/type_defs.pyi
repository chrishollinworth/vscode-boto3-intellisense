"""
Type annotations for timestream-influxdb service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_timestream_influxdb.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

from .literals import (
    ClusterStatusType,
    DbInstanceTypeType,
    DbStorageTypeType,
    DeploymentTypeType,
    DurationTypeType,
    FailoverModeType,
    InstanceModeType,
    LogLevelType,
    NetworkTypeType,
    StatusType,
    TracingTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "CreateDbClusterInputTypeDef",
    "CreateDbClusterOutputTypeDef",
    "CreateDbInstanceInputTypeDef",
    "CreateDbInstanceOutputTypeDef",
    "CreateDbParameterGroupInputTypeDef",
    "CreateDbParameterGroupOutputTypeDef",
    "DbClusterSummaryTypeDef",
    "DbInstanceForClusterSummaryTypeDef",
    "DbInstanceSummaryTypeDef",
    "DbParameterGroupSummaryTypeDef",
    "DeleteDbClusterInputTypeDef",
    "DeleteDbClusterOutputTypeDef",
    "DeleteDbInstanceInputTypeDef",
    "DeleteDbInstanceOutputTypeDef",
    "DurationTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetDbClusterInputTypeDef",
    "GetDbClusterOutputTypeDef",
    "GetDbInstanceInputTypeDef",
    "GetDbInstanceOutputTypeDef",
    "GetDbParameterGroupInputTypeDef",
    "GetDbParameterGroupOutputTypeDef",
    "InfluxDBv2ParametersTypeDef",
    "ListDbClustersInputPaginateTypeDef",
    "ListDbClustersInputTypeDef",
    "ListDbClustersOutputTypeDef",
    "ListDbInstancesForClusterInputPaginateTypeDef",
    "ListDbInstancesForClusterInputTypeDef",
    "ListDbInstancesForClusterOutputTypeDef",
    "ListDbInstancesInputPaginateTypeDef",
    "ListDbInstancesInputTypeDef",
    "ListDbInstancesOutputTypeDef",
    "ListDbParameterGroupsInputPaginateTypeDef",
    "ListDbParameterGroupsInputTypeDef",
    "ListDbParameterGroupsOutputTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogDeliveryConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ParametersTypeDef",
    "ResponseMetadataTypeDef",
    "S3ConfigurationTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDbClusterInputTypeDef",
    "UpdateDbClusterOutputTypeDef",
    "UpdateDbInstanceInputTypeDef",
    "UpdateDbInstanceOutputTypeDef",
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

DbClusterSummaryTypeDef = TypedDict(
    "DbClusterSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": NotRequired[ClusterStatusType],
        "endpoint": NotRequired[str],
        "readerEndpoint": NotRequired[str],
        "port": NotRequired[int],
        "deploymentType": NotRequired[Literal["MULTI_NODE_READ_REPLICAS"]],
        "dbInstanceType": NotRequired[DbInstanceTypeType],
        "networkType": NotRequired[NetworkTypeType],
        "dbStorageType": NotRequired[DbStorageTypeType],
        "allocatedStorage": NotRequired[int],
    },
)
DbInstanceForClusterSummaryTypeDef = TypedDict(
    "DbInstanceForClusterSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": NotRequired[StatusType],
        "endpoint": NotRequired[str],
        "port": NotRequired[int],
        "networkType": NotRequired[NetworkTypeType],
        "dbInstanceType": NotRequired[DbInstanceTypeType],
        "dbStorageType": NotRequired[DbStorageTypeType],
        "allocatedStorage": NotRequired[int],
        "deploymentType": NotRequired[DeploymentTypeType],
        "instanceMode": NotRequired[InstanceModeType],
    },
)
DbInstanceSummaryTypeDef = TypedDict(
    "DbInstanceSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": NotRequired[StatusType],
        "endpoint": NotRequired[str],
        "port": NotRequired[int],
        "networkType": NotRequired[NetworkTypeType],
        "dbInstanceType": NotRequired[DbInstanceTypeType],
        "dbStorageType": NotRequired[DbStorageTypeType],
        "allocatedStorage": NotRequired[int],
        "deploymentType": NotRequired[DeploymentTypeType],
    },
)
DbParameterGroupSummaryTypeDef = TypedDict(
    "DbParameterGroupSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "description": NotRequired[str],
    },
)

class DeleteDbClusterInputTypeDef(TypedDict):
    dbClusterId: str

class DeleteDbInstanceInputTypeDef(TypedDict):
    identifier: str

class DurationTypeDef(TypedDict):
    durationType: DurationTypeType
    value: int

class GetDbClusterInputTypeDef(TypedDict):
    dbClusterId: str

class GetDbInstanceInputTypeDef(TypedDict):
    identifier: str

class GetDbParameterGroupInputTypeDef(TypedDict):
    identifier: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListDbClustersInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListDbInstancesForClusterInputTypeDef(TypedDict):
    dbClusterId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListDbInstancesInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListDbParameterGroupsInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class S3ConfigurationTypeDef(TypedDict):
    bucketName: str
    enabled: bool

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class CreateDbClusterOutputTypeDef(TypedDict):
    dbClusterId: str
    dbClusterStatus: ClusterStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDbClusterOutputTypeDef(TypedDict):
    dbClusterStatus: ClusterStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDbClusterOutputTypeDef(TypedDict):
    dbClusterStatus: ClusterStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListDbClustersOutputTypeDef(TypedDict):
    items: List[DbClusterSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListDbInstancesForClusterOutputTypeDef(TypedDict):
    items: List[DbInstanceForClusterSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListDbInstancesOutputTypeDef(TypedDict):
    items: List[DbInstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListDbParameterGroupsOutputTypeDef(TypedDict):
    items: List[DbParameterGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class InfluxDBv2ParametersTypeDef(TypedDict):
    fluxLogEnabled: NotRequired[bool]
    logLevel: NotRequired[LogLevelType]
    noTasks: NotRequired[bool]
    queryConcurrency: NotRequired[int]
    queryQueueSize: NotRequired[int]
    tracingType: NotRequired[TracingTypeType]
    metricsDisabled: NotRequired[bool]
    httpIdleTimeout: NotRequired[DurationTypeDef]
    httpReadHeaderTimeout: NotRequired[DurationTypeDef]
    httpReadTimeout: NotRequired[DurationTypeDef]
    httpWriteTimeout: NotRequired[DurationTypeDef]
    influxqlMaxSelectBuckets: NotRequired[int]
    influxqlMaxSelectPoint: NotRequired[int]
    influxqlMaxSelectSeries: NotRequired[int]
    pprofDisabled: NotRequired[bool]
    queryInitialMemoryBytes: NotRequired[int]
    queryMaxMemoryBytes: NotRequired[int]
    queryMemoryBytes: NotRequired[int]
    sessionLength: NotRequired[int]
    sessionRenewDisabled: NotRequired[bool]
    storageCacheMaxMemorySize: NotRequired[int]
    storageCacheSnapshotMemorySize: NotRequired[int]
    storageCacheSnapshotWriteColdDuration: NotRequired[DurationTypeDef]
    storageCompactFullWriteColdDuration: NotRequired[DurationTypeDef]
    storageCompactThroughputBurst: NotRequired[int]
    storageMaxConcurrentCompactions: NotRequired[int]
    storageMaxIndexLogFileSize: NotRequired[int]
    storageNoValidateFieldSize: NotRequired[bool]
    storageRetentionCheckInterval: NotRequired[DurationTypeDef]
    storageSeriesFileMaxConcurrentSnapshotCompactions: NotRequired[int]
    storageSeriesIdSetCacheSize: NotRequired[int]
    storageWalMaxConcurrentWrites: NotRequired[int]
    storageWalMaxWriteDelay: NotRequired[DurationTypeDef]
    uiDisabled: NotRequired[bool]

class ListDbClustersInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDbInstancesForClusterInputPaginateTypeDef(TypedDict):
    dbClusterId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDbInstancesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDbParameterGroupsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class LogDeliveryConfigurationTypeDef(TypedDict):
    s3Configuration: S3ConfigurationTypeDef

class ParametersTypeDef(TypedDict):
    InfluxDBv2: NotRequired[InfluxDBv2ParametersTypeDef]

class CreateDbClusterInputTypeDef(TypedDict):
    name: str
    password: str
    dbInstanceType: DbInstanceTypeType
    allocatedStorage: int
    vpcSubnetIds: Sequence[str]
    vpcSecurityGroupIds: Sequence[str]
    deploymentType: Literal["MULTI_NODE_READ_REPLICAS"]
    username: NotRequired[str]
    organization: NotRequired[str]
    bucket: NotRequired[str]
    port: NotRequired[int]
    dbParameterGroupIdentifier: NotRequired[str]
    dbStorageType: NotRequired[DbStorageTypeType]
    networkType: NotRequired[NetworkTypeType]
    publiclyAccessible: NotRequired[bool]
    failoverMode: NotRequired[FailoverModeType]
    logDeliveryConfiguration: NotRequired[LogDeliveryConfigurationTypeDef]
    tags: NotRequired[Mapping[str, str]]

class CreateDbInstanceInputTypeDef(TypedDict):
    name: str
    password: str
    dbInstanceType: DbInstanceTypeType
    vpcSubnetIds: Sequence[str]
    vpcSecurityGroupIds: Sequence[str]
    allocatedStorage: int
    username: NotRequired[str]
    organization: NotRequired[str]
    bucket: NotRequired[str]
    publiclyAccessible: NotRequired[bool]
    dbStorageType: NotRequired[DbStorageTypeType]
    dbParameterGroupIdentifier: NotRequired[str]
    deploymentType: NotRequired[DeploymentTypeType]
    logDeliveryConfiguration: NotRequired[LogDeliveryConfigurationTypeDef]
    tags: NotRequired[Mapping[str, str]]
    port: NotRequired[int]
    networkType: NotRequired[NetworkTypeType]

CreateDbInstanceOutputTypeDef = TypedDict(
    "CreateDbInstanceOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": StatusType,
        "endpoint": str,
        "port": int,
        "networkType": NetworkTypeType,
        "dbInstanceType": DbInstanceTypeType,
        "dbStorageType": DbStorageTypeType,
        "allocatedStorage": int,
        "deploymentType": DeploymentTypeType,
        "vpcSubnetIds": List[str],
        "publiclyAccessible": bool,
        "vpcSecurityGroupIds": List[str],
        "dbParameterGroupIdentifier": str,
        "availabilityZone": str,
        "secondaryAvailabilityZone": str,
        "logDeliveryConfiguration": LogDeliveryConfigurationTypeDef,
        "influxAuthParametersSecretArn": str,
        "dbClusterId": str,
        "instanceMode": InstanceModeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDbInstanceOutputTypeDef = TypedDict(
    "DeleteDbInstanceOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": StatusType,
        "endpoint": str,
        "port": int,
        "networkType": NetworkTypeType,
        "dbInstanceType": DbInstanceTypeType,
        "dbStorageType": DbStorageTypeType,
        "allocatedStorage": int,
        "deploymentType": DeploymentTypeType,
        "vpcSubnetIds": List[str],
        "publiclyAccessible": bool,
        "vpcSecurityGroupIds": List[str],
        "dbParameterGroupIdentifier": str,
        "availabilityZone": str,
        "secondaryAvailabilityZone": str,
        "logDeliveryConfiguration": LogDeliveryConfigurationTypeDef,
        "influxAuthParametersSecretArn": str,
        "dbClusterId": str,
        "instanceMode": InstanceModeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDbClusterOutputTypeDef = TypedDict(
    "GetDbClusterOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": ClusterStatusType,
        "endpoint": str,
        "readerEndpoint": str,
        "port": int,
        "deploymentType": Literal["MULTI_NODE_READ_REPLICAS"],
        "dbInstanceType": DbInstanceTypeType,
        "networkType": NetworkTypeType,
        "dbStorageType": DbStorageTypeType,
        "allocatedStorage": int,
        "publiclyAccessible": bool,
        "dbParameterGroupIdentifier": str,
        "logDeliveryConfiguration": LogDeliveryConfigurationTypeDef,
        "influxAuthParametersSecretArn": str,
        "vpcSubnetIds": List[str],
        "vpcSecurityGroupIds": List[str],
        "failoverMode": FailoverModeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDbInstanceOutputTypeDef = TypedDict(
    "GetDbInstanceOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": StatusType,
        "endpoint": str,
        "port": int,
        "networkType": NetworkTypeType,
        "dbInstanceType": DbInstanceTypeType,
        "dbStorageType": DbStorageTypeType,
        "allocatedStorage": int,
        "deploymentType": DeploymentTypeType,
        "vpcSubnetIds": List[str],
        "publiclyAccessible": bool,
        "vpcSecurityGroupIds": List[str],
        "dbParameterGroupIdentifier": str,
        "availabilityZone": str,
        "secondaryAvailabilityZone": str,
        "logDeliveryConfiguration": LogDeliveryConfigurationTypeDef,
        "influxAuthParametersSecretArn": str,
        "dbClusterId": str,
        "instanceMode": InstanceModeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class UpdateDbClusterInputTypeDef(TypedDict):
    dbClusterId: str
    logDeliveryConfiguration: NotRequired[LogDeliveryConfigurationTypeDef]
    dbParameterGroupIdentifier: NotRequired[str]
    port: NotRequired[int]
    dbInstanceType: NotRequired[DbInstanceTypeType]
    failoverMode: NotRequired[FailoverModeType]

class UpdateDbInstanceInputTypeDef(TypedDict):
    identifier: str
    logDeliveryConfiguration: NotRequired[LogDeliveryConfigurationTypeDef]
    dbParameterGroupIdentifier: NotRequired[str]
    port: NotRequired[int]
    dbInstanceType: NotRequired[DbInstanceTypeType]
    deploymentType: NotRequired[DeploymentTypeType]
    dbStorageType: NotRequired[DbStorageTypeType]
    allocatedStorage: NotRequired[int]

UpdateDbInstanceOutputTypeDef = TypedDict(
    "UpdateDbInstanceOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": StatusType,
        "endpoint": str,
        "port": int,
        "networkType": NetworkTypeType,
        "dbInstanceType": DbInstanceTypeType,
        "dbStorageType": DbStorageTypeType,
        "allocatedStorage": int,
        "deploymentType": DeploymentTypeType,
        "vpcSubnetIds": List[str],
        "publiclyAccessible": bool,
        "vpcSecurityGroupIds": List[str],
        "dbParameterGroupIdentifier": str,
        "availabilityZone": str,
        "secondaryAvailabilityZone": str,
        "logDeliveryConfiguration": LogDeliveryConfigurationTypeDef,
        "influxAuthParametersSecretArn": str,
        "dbClusterId": str,
        "instanceMode": InstanceModeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateDbParameterGroupInputTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    parameters: NotRequired[ParametersTypeDef]
    tags: NotRequired[Mapping[str, str]]

CreateDbParameterGroupOutputTypeDef = TypedDict(
    "CreateDbParameterGroupOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "description": str,
        "parameters": ParametersTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDbParameterGroupOutputTypeDef = TypedDict(
    "GetDbParameterGroupOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "description": str,
        "parameters": ParametersTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
