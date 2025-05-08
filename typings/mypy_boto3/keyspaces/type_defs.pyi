"""
Type annotations for keyspaces service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_keyspaces.type_defs import TargetTrackingScalingPolicyConfigurationTypeDef

    data: TargetTrackingScalingPolicyConfigurationTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    EncryptionTypeType,
    KeyspaceStatusType,
    PointInTimeRecoveryStatusType,
    RsType,
    SortOrderType,
    TableStatusType,
    ThroughputModeType,
    TypeStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AutoScalingPolicyTypeDef",
    "AutoScalingSettingsTypeDef",
    "AutoScalingSpecificationTypeDef",
    "CapacitySpecificationSummaryTypeDef",
    "CapacitySpecificationTypeDef",
    "ClientSideTimestampsTypeDef",
    "ClusteringKeyTypeDef",
    "ColumnDefinitionTypeDef",
    "CommentTypeDef",
    "CreateKeyspaceRequestTypeDef",
    "CreateKeyspaceResponseTypeDef",
    "CreateTableRequestTypeDef",
    "CreateTableResponseTypeDef",
    "CreateTypeRequestTypeDef",
    "CreateTypeResponseTypeDef",
    "DeleteKeyspaceRequestTypeDef",
    "DeleteTableRequestTypeDef",
    "DeleteTypeRequestTypeDef",
    "DeleteTypeResponseTypeDef",
    "EncryptionSpecificationTypeDef",
    "FieldDefinitionTypeDef",
    "GetKeyspaceRequestTypeDef",
    "GetKeyspaceResponseTypeDef",
    "GetTableAutoScalingSettingsRequestTypeDef",
    "GetTableAutoScalingSettingsResponseTypeDef",
    "GetTableRequestTypeDef",
    "GetTableResponseTypeDef",
    "GetTypeRequestTypeDef",
    "GetTypeResponseTypeDef",
    "KeyspaceSummaryTypeDef",
    "ListKeyspacesRequestPaginateTypeDef",
    "ListKeyspacesRequestTypeDef",
    "ListKeyspacesResponseTypeDef",
    "ListTablesRequestPaginateTypeDef",
    "ListTablesRequestTypeDef",
    "ListTablesResponseTypeDef",
    "ListTagsForResourceRequestPaginateTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTypesRequestPaginateTypeDef",
    "ListTypesRequestTypeDef",
    "ListTypesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PartitionKeyTypeDef",
    "PointInTimeRecoverySummaryTypeDef",
    "PointInTimeRecoveryTypeDef",
    "ReplicaAutoScalingSpecificationTypeDef",
    "ReplicaSpecificationSummaryTypeDef",
    "ReplicaSpecificationTypeDef",
    "ReplicationGroupStatusTypeDef",
    "ReplicationSpecificationTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreTableRequestTypeDef",
    "RestoreTableResponseTypeDef",
    "SchemaDefinitionOutputTypeDef",
    "SchemaDefinitionTypeDef",
    "SchemaDefinitionUnionTypeDef",
    "StaticColumnTypeDef",
    "TableSummaryTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TargetTrackingScalingPolicyConfigurationTypeDef",
    "TimeToLiveTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateKeyspaceRequestTypeDef",
    "UpdateKeyspaceResponseTypeDef",
    "UpdateTableRequestTypeDef",
    "UpdateTableResponseTypeDef",
)

class TargetTrackingScalingPolicyConfigurationTypeDef(TypedDict):
    targetValue: float
    disableScaleIn: NotRequired[bool]
    scaleInCooldown: NotRequired[int]
    scaleOutCooldown: NotRequired[int]

class CapacitySpecificationSummaryTypeDef(TypedDict):
    throughputMode: ThroughputModeType
    readCapacityUnits: NotRequired[int]
    writeCapacityUnits: NotRequired[int]
    lastUpdateToPayPerRequestTimestamp: NotRequired[datetime]

class CapacitySpecificationTypeDef(TypedDict):
    throughputMode: ThroughputModeType
    readCapacityUnits: NotRequired[int]
    writeCapacityUnits: NotRequired[int]

class ClientSideTimestampsTypeDef(TypedDict):
    status: Literal["ENABLED"]

class ClusteringKeyTypeDef(TypedDict):
    name: str
    orderBy: SortOrderType

ColumnDefinitionTypeDef = TypedDict(
    "ColumnDefinitionTypeDef",
    {
        "name": str,
        "type": str,
    },
)

class CommentTypeDef(TypedDict):
    message: str

class ReplicationSpecificationTypeDef(TypedDict):
    replicationStrategy: RsType
    regionList: NotRequired[Sequence[str]]

class TagTypeDef(TypedDict):
    key: str
    value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

EncryptionSpecificationTypeDef = TypedDict(
    "EncryptionSpecificationTypeDef",
    {
        "type": EncryptionTypeType,
        "kmsKeyIdentifier": NotRequired[str],
    },
)

class PointInTimeRecoveryTypeDef(TypedDict):
    status: PointInTimeRecoveryStatusType

class TimeToLiveTypeDef(TypedDict):
    status: Literal["ENABLED"]

FieldDefinitionTypeDef = TypedDict(
    "FieldDefinitionTypeDef",
    {
        "name": str,
        "type": str,
    },
)

class DeleteKeyspaceRequestTypeDef(TypedDict):
    keyspaceName: str

class DeleteTableRequestTypeDef(TypedDict):
    keyspaceName: str
    tableName: str

class DeleteTypeRequestTypeDef(TypedDict):
    keyspaceName: str
    typeName: str

class GetKeyspaceRequestTypeDef(TypedDict):
    keyspaceName: str

class ReplicationGroupStatusTypeDef(TypedDict):
    region: str
    keyspaceStatus: KeyspaceStatusType
    tablesReplicationProgress: NotRequired[str]

class GetTableAutoScalingSettingsRequestTypeDef(TypedDict):
    keyspaceName: str
    tableName: str

class GetTableRequestTypeDef(TypedDict):
    keyspaceName: str
    tableName: str

class PointInTimeRecoverySummaryTypeDef(TypedDict):
    status: PointInTimeRecoveryStatusType
    earliestRestorableTimestamp: NotRequired[datetime]

class GetTypeRequestTypeDef(TypedDict):
    keyspaceName: str
    typeName: str

class KeyspaceSummaryTypeDef(TypedDict):
    keyspaceName: str
    resourceArn: str
    replicationStrategy: RsType
    replicationRegions: NotRequired[List[str]]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListKeyspacesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListTablesRequestTypeDef(TypedDict):
    keyspaceName: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class TableSummaryTypeDef(TypedDict):
    keyspaceName: str
    tableName: str
    resourceArn: str

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListTypesRequestTypeDef(TypedDict):
    keyspaceName: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class PartitionKeyTypeDef(TypedDict):
    name: str

TimestampTypeDef = Union[datetime, str]

class StaticColumnTypeDef(TypedDict):
    name: str

class AutoScalingPolicyTypeDef(TypedDict):
    targetTrackingScalingPolicyConfiguration: NotRequired[
        TargetTrackingScalingPolicyConfigurationTypeDef
    ]

class ReplicaSpecificationSummaryTypeDef(TypedDict):
    region: NotRequired[str]
    status: NotRequired[TableStatusType]
    capacitySpecification: NotRequired[CapacitySpecificationSummaryTypeDef]

class UpdateKeyspaceRequestTypeDef(TypedDict):
    keyspaceName: str
    replicationSpecification: ReplicationSpecificationTypeDef
    clientSideTimestamps: NotRequired[ClientSideTimestampsTypeDef]

class CreateKeyspaceRequestTypeDef(TypedDict):
    keyspaceName: str
    tags: NotRequired[Sequence[TagTypeDef]]
    replicationSpecification: NotRequired[ReplicationSpecificationTypeDef]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateKeyspaceResponseTypeDef(TypedDict):
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTableResponseTypeDef(TypedDict):
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTypeResponseTypeDef(TypedDict):
    keyspaceArn: str
    typeName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTypeResponseTypeDef(TypedDict):
    keyspaceArn: str
    typeName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ListTypesResponseTypeDef = TypedDict(
    "ListTypesResponseTypeDef",
    {
        "types": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "nextToken": NotRequired[str],
    },
)

class RestoreTableResponseTypeDef(TypedDict):
    restoredTableARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKeyspaceResponseTypeDef(TypedDict):
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTableResponseTypeDef(TypedDict):
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTypeRequestTypeDef(TypedDict):
    keyspaceName: str
    typeName: str
    fieldDefinitions: Sequence[FieldDefinitionTypeDef]

class GetTypeResponseTypeDef(TypedDict):
    keyspaceName: str
    typeName: str
    fieldDefinitions: List[FieldDefinitionTypeDef]
    lastModifiedTimestamp: datetime
    status: TypeStatusType
    directReferringTables: List[str]
    directParentTypes: List[str]
    maxNestingDepth: int
    keyspaceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetKeyspaceResponseTypeDef(TypedDict):
    keyspaceName: str
    resourceArn: str
    replicationStrategy: RsType
    replicationRegions: List[str]
    replicationGroupStatuses: List[ReplicationGroupStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeyspacesResponseTypeDef(TypedDict):
    keyspaces: List[KeyspaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListKeyspacesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTablesRequestPaginateTypeDef(TypedDict):
    keyspaceName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceRequestPaginateTypeDef(TypedDict):
    resourceArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTypesRequestPaginateTypeDef(TypedDict):
    keyspaceName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTablesResponseTypeDef(TypedDict):
    tables: List[TableSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SchemaDefinitionOutputTypeDef(TypedDict):
    allColumns: List[ColumnDefinitionTypeDef]
    partitionKeys: List[PartitionKeyTypeDef]
    clusteringKeys: NotRequired[List[ClusteringKeyTypeDef]]
    staticColumns: NotRequired[List[StaticColumnTypeDef]]

class SchemaDefinitionTypeDef(TypedDict):
    allColumns: Sequence[ColumnDefinitionTypeDef]
    partitionKeys: Sequence[PartitionKeyTypeDef]
    clusteringKeys: NotRequired[Sequence[ClusteringKeyTypeDef]]
    staticColumns: NotRequired[Sequence[StaticColumnTypeDef]]

class AutoScalingSettingsTypeDef(TypedDict):
    autoScalingDisabled: NotRequired[bool]
    minimumUnits: NotRequired[int]
    maximumUnits: NotRequired[int]
    scalingPolicy: NotRequired[AutoScalingPolicyTypeDef]

class GetTableResponseTypeDef(TypedDict):
    keyspaceName: str
    tableName: str
    resourceArn: str
    creationTimestamp: datetime
    status: TableStatusType
    schemaDefinition: SchemaDefinitionOutputTypeDef
    capacitySpecification: CapacitySpecificationSummaryTypeDef
    encryptionSpecification: EncryptionSpecificationTypeDef
    pointInTimeRecovery: PointInTimeRecoverySummaryTypeDef
    ttl: TimeToLiveTypeDef
    defaultTimeToLive: int
    comment: CommentTypeDef
    clientSideTimestamps: ClientSideTimestampsTypeDef
    replicaSpecifications: List[ReplicaSpecificationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

SchemaDefinitionUnionTypeDef = Union[SchemaDefinitionTypeDef, SchemaDefinitionOutputTypeDef]

class AutoScalingSpecificationTypeDef(TypedDict):
    writeCapacityAutoScaling: NotRequired[AutoScalingSettingsTypeDef]
    readCapacityAutoScaling: NotRequired[AutoScalingSettingsTypeDef]

class ReplicaSpecificationTypeDef(TypedDict):
    region: str
    readCapacityUnits: NotRequired[int]
    readCapacityAutoScaling: NotRequired[AutoScalingSettingsTypeDef]

class ReplicaAutoScalingSpecificationTypeDef(TypedDict):
    region: NotRequired[str]
    autoScalingSpecification: NotRequired[AutoScalingSpecificationTypeDef]

class CreateTableRequestTypeDef(TypedDict):
    keyspaceName: str
    tableName: str
    schemaDefinition: SchemaDefinitionUnionTypeDef
    comment: NotRequired[CommentTypeDef]
    capacitySpecification: NotRequired[CapacitySpecificationTypeDef]
    encryptionSpecification: NotRequired[EncryptionSpecificationTypeDef]
    pointInTimeRecovery: NotRequired[PointInTimeRecoveryTypeDef]
    ttl: NotRequired[TimeToLiveTypeDef]
    defaultTimeToLive: NotRequired[int]
    tags: NotRequired[Sequence[TagTypeDef]]
    clientSideTimestamps: NotRequired[ClientSideTimestampsTypeDef]
    autoScalingSpecification: NotRequired[AutoScalingSpecificationTypeDef]
    replicaSpecifications: NotRequired[Sequence[ReplicaSpecificationTypeDef]]

class RestoreTableRequestTypeDef(TypedDict):
    sourceKeyspaceName: str
    sourceTableName: str
    targetKeyspaceName: str
    targetTableName: str
    restoreTimestamp: NotRequired[TimestampTypeDef]
    capacitySpecificationOverride: NotRequired[CapacitySpecificationTypeDef]
    encryptionSpecificationOverride: NotRequired[EncryptionSpecificationTypeDef]
    pointInTimeRecoveryOverride: NotRequired[PointInTimeRecoveryTypeDef]
    tagsOverride: NotRequired[Sequence[TagTypeDef]]
    autoScalingSpecification: NotRequired[AutoScalingSpecificationTypeDef]
    replicaSpecifications: NotRequired[Sequence[ReplicaSpecificationTypeDef]]

class UpdateTableRequestTypeDef(TypedDict):
    keyspaceName: str
    tableName: str
    addColumns: NotRequired[Sequence[ColumnDefinitionTypeDef]]
    capacitySpecification: NotRequired[CapacitySpecificationTypeDef]
    encryptionSpecification: NotRequired[EncryptionSpecificationTypeDef]
    pointInTimeRecovery: NotRequired[PointInTimeRecoveryTypeDef]
    ttl: NotRequired[TimeToLiveTypeDef]
    defaultTimeToLive: NotRequired[int]
    clientSideTimestamps: NotRequired[ClientSideTimestampsTypeDef]
    autoScalingSpecification: NotRequired[AutoScalingSpecificationTypeDef]
    replicaSpecifications: NotRequired[Sequence[ReplicaSpecificationTypeDef]]

class GetTableAutoScalingSettingsResponseTypeDef(TypedDict):
    keyspaceName: str
    tableName: str
    resourceArn: str
    autoScalingSpecification: AutoScalingSpecificationTypeDef
    replicaSpecifications: List[ReplicaAutoScalingSpecificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
