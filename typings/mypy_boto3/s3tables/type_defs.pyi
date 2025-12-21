"""
Type annotations for s3tables service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3tables/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_s3tables.type_defs import CreateNamespaceRequestTypeDef

    data: CreateNamespaceRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    IcebergCompactionStrategyType,
    JobStatusType,
    MaintenanceStatusType,
    ReplicationStatusType,
    SSEAlgorithmType,
    StorageClassType,
    TableBucketTypeType,
    TableMaintenanceJobTypeType,
    TableMaintenanceTypeType,
    TableRecordExpirationJobStatusType,
    TableRecordExpirationStatusType,
    TableTypeType,
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
    "CreateNamespaceRequestTypeDef",
    "CreateNamespaceResponseTypeDef",
    "CreateTableBucketRequestTypeDef",
    "CreateTableBucketResponseTypeDef",
    "CreateTableRequestTypeDef",
    "CreateTableResponseTypeDef",
    "DeleteNamespaceRequestTypeDef",
    "DeleteTableBucketEncryptionRequestTypeDef",
    "DeleteTableBucketMetricsConfigurationRequestTypeDef",
    "DeleteTableBucketPolicyRequestTypeDef",
    "DeleteTableBucketReplicationRequestTypeDef",
    "DeleteTableBucketRequestTypeDef",
    "DeleteTablePolicyRequestTypeDef",
    "DeleteTableReplicationRequestTypeDef",
    "DeleteTableRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncryptionConfigurationTypeDef",
    "GetNamespaceRequestTypeDef",
    "GetNamespaceResponseTypeDef",
    "GetTableBucketEncryptionRequestTypeDef",
    "GetTableBucketEncryptionResponseTypeDef",
    "GetTableBucketMaintenanceConfigurationRequestTypeDef",
    "GetTableBucketMaintenanceConfigurationResponseTypeDef",
    "GetTableBucketMetricsConfigurationRequestTypeDef",
    "GetTableBucketMetricsConfigurationResponseTypeDef",
    "GetTableBucketPolicyRequestTypeDef",
    "GetTableBucketPolicyResponseTypeDef",
    "GetTableBucketReplicationRequestTypeDef",
    "GetTableBucketReplicationResponseTypeDef",
    "GetTableBucketRequestTypeDef",
    "GetTableBucketResponseTypeDef",
    "GetTableBucketStorageClassRequestTypeDef",
    "GetTableBucketStorageClassResponseTypeDef",
    "GetTableEncryptionRequestTypeDef",
    "GetTableEncryptionResponseTypeDef",
    "GetTableMaintenanceConfigurationRequestTypeDef",
    "GetTableMaintenanceConfigurationResponseTypeDef",
    "GetTableMaintenanceJobStatusRequestTypeDef",
    "GetTableMaintenanceJobStatusResponseTypeDef",
    "GetTableMetadataLocationRequestTypeDef",
    "GetTableMetadataLocationResponseTypeDef",
    "GetTablePolicyRequestTypeDef",
    "GetTablePolicyResponseTypeDef",
    "GetTableRecordExpirationConfigurationRequestTypeDef",
    "GetTableRecordExpirationConfigurationResponseTypeDef",
    "GetTableRecordExpirationJobStatusRequestTypeDef",
    "GetTableRecordExpirationJobStatusResponseTypeDef",
    "GetTableReplicationRequestTypeDef",
    "GetTableReplicationResponseTypeDef",
    "GetTableReplicationStatusRequestTypeDef",
    "GetTableReplicationStatusResponseTypeDef",
    "GetTableRequestTypeDef",
    "GetTableResponseTypeDef",
    "GetTableStorageClassRequestTypeDef",
    "GetTableStorageClassResponseTypeDef",
    "IcebergCompactionSettingsTypeDef",
    "IcebergMetadataTypeDef",
    "IcebergSchemaTypeDef",
    "IcebergSnapshotManagementSettingsTypeDef",
    "IcebergUnreferencedFileRemovalSettingsTypeDef",
    "LastSuccessfulReplicatedUpdateTypeDef",
    "ListNamespacesRequestPaginateTypeDef",
    "ListNamespacesRequestTypeDef",
    "ListNamespacesResponseTypeDef",
    "ListTableBucketsRequestPaginateTypeDef",
    "ListTableBucketsRequestTypeDef",
    "ListTableBucketsResponseTypeDef",
    "ListTablesRequestPaginateTypeDef",
    "ListTablesRequestTypeDef",
    "ListTablesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ManagedTableInformationTypeDef",
    "NamespaceSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "PutTableBucketEncryptionRequestTypeDef",
    "PutTableBucketMaintenanceConfigurationRequestTypeDef",
    "PutTableBucketMetricsConfigurationRequestTypeDef",
    "PutTableBucketPolicyRequestTypeDef",
    "PutTableBucketReplicationRequestTypeDef",
    "PutTableBucketReplicationResponseTypeDef",
    "PutTableBucketStorageClassRequestTypeDef",
    "PutTableMaintenanceConfigurationRequestTypeDef",
    "PutTablePolicyRequestTypeDef",
    "PutTableRecordExpirationConfigurationRequestTypeDef",
    "PutTableReplicationRequestTypeDef",
    "PutTableReplicationResponseTypeDef",
    "RenameTableRequestTypeDef",
    "ReplicationDestinationStatusModelTypeDef",
    "ReplicationDestinationTypeDef",
    "ReplicationInformationTypeDef",
    "ResponseMetadataTypeDef",
    "SchemaFieldTypeDef",
    "StorageClassConfigurationTypeDef",
    "TableBucketMaintenanceConfigurationValueTypeDef",
    "TableBucketMaintenanceSettingsTypeDef",
    "TableBucketReplicationConfigurationOutputTypeDef",
    "TableBucketReplicationConfigurationTypeDef",
    "TableBucketReplicationConfigurationUnionTypeDef",
    "TableBucketReplicationRuleOutputTypeDef",
    "TableBucketReplicationRuleTypeDef",
    "TableBucketSummaryTypeDef",
    "TableMaintenanceConfigurationValueTypeDef",
    "TableMaintenanceJobStatusValueTypeDef",
    "TableMaintenanceSettingsTypeDef",
    "TableMetadataTypeDef",
    "TableRecordExpirationConfigurationValueTypeDef",
    "TableRecordExpirationJobMetricsTypeDef",
    "TableRecordExpirationSettingsTypeDef",
    "TableReplicationConfigurationOutputTypeDef",
    "TableReplicationConfigurationTypeDef",
    "TableReplicationConfigurationUnionTypeDef",
    "TableReplicationRuleOutputTypeDef",
    "TableReplicationRuleTypeDef",
    "TableSummaryTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateTableMetadataLocationRequestTypeDef",
    "UpdateTableMetadataLocationResponseTypeDef",
)

class CreateNamespaceRequestTypeDef(TypedDict):
    tableBucketARN: str
    namespace: Sequence[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class EncryptionConfigurationTypeDef(TypedDict):
    sseAlgorithm: SSEAlgorithmType
    kmsKeyArn: NotRequired[str]

class StorageClassConfigurationTypeDef(TypedDict):
    storageClass: StorageClassType

class DeleteNamespaceRequestTypeDef(TypedDict):
    tableBucketARN: str
    namespace: str

class DeleteTableBucketEncryptionRequestTypeDef(TypedDict):
    tableBucketARN: str

class DeleteTableBucketMetricsConfigurationRequestTypeDef(TypedDict):
    tableBucketARN: str

class DeleteTableBucketPolicyRequestTypeDef(TypedDict):
    tableBucketARN: str

class DeleteTableBucketReplicationRequestTypeDef(TypedDict):
    tableBucketARN: str
    versionToken: NotRequired[str]

class DeleteTableBucketRequestTypeDef(TypedDict):
    tableBucketARN: str

class DeleteTablePolicyRequestTypeDef(TypedDict):
    tableBucketARN: str
    namespace: str
    name: str

class DeleteTableReplicationRequestTypeDef(TypedDict):
    tableArn: str
    versionToken: str

class DeleteTableRequestTypeDef(TypedDict):
    tableBucketARN: str
    namespace: str
    name: str
    versionToken: NotRequired[str]

class GetNamespaceRequestTypeDef(TypedDict):
    tableBucketARN: str
    namespace: str

class GetTableBucketEncryptionRequestTypeDef(TypedDict):
    tableBucketARN: str

class GetTableBucketMaintenanceConfigurationRequestTypeDef(TypedDict):
    tableBucketARN: str

class GetTableBucketMetricsConfigurationRequestTypeDef(TypedDict):
    tableBucketARN: str

class GetTableBucketPolicyRequestTypeDef(TypedDict):
    tableBucketARN: str

class GetTableBucketReplicationRequestTypeDef(TypedDict):
    tableBucketARN: str

class GetTableBucketRequestTypeDef(TypedDict):
    tableBucketARN: str

class GetTableBucketStorageClassRequestTypeDef(TypedDict):
    tableBucketARN: str

class GetTableEncryptionRequestTypeDef(TypedDict):
    tableBucketARN: str
    namespace: str
    name: str

class GetTableMaintenanceConfigurationRequestTypeDef(TypedDict):
    tableBucketARN: str
    namespace: str
    name: str

class GetTableMaintenanceJobStatusRequestTypeDef(TypedDict):
    tableBucketARN: str
    namespace: str
    name: str

class TableMaintenanceJobStatusValueTypeDef(TypedDict):
    status: JobStatusType
    lastRunTimestamp: NotRequired[datetime]
    failureMessage: NotRequired[str]

class GetTableMetadataLocationRequestTypeDef(TypedDict):
    tableBucketARN: str
    namespace: str
    name: str

class GetTablePolicyRequestTypeDef(TypedDict):
    tableBucketARN: str
    namespace: str
    name: str

class GetTableRecordExpirationConfigurationRequestTypeDef(TypedDict):
    tableArn: str

class GetTableRecordExpirationJobStatusRequestTypeDef(TypedDict):
    tableArn: str

class TableRecordExpirationJobMetricsTypeDef(TypedDict):
    deletedDataFiles: NotRequired[int]
    deletedRecords: NotRequired[int]
    removedFilesSize: NotRequired[int]

class GetTableReplicationRequestTypeDef(TypedDict):
    tableArn: str

class GetTableReplicationStatusRequestTypeDef(TypedDict):
    tableArn: str

class GetTableRequestTypeDef(TypedDict):
    tableBucketARN: NotRequired[str]
    namespace: NotRequired[str]
    name: NotRequired[str]
    tableArn: NotRequired[str]

class GetTableStorageClassRequestTypeDef(TypedDict):
    tableBucketARN: str
    namespace: str
    name: str

class IcebergCompactionSettingsTypeDef(TypedDict):
    targetFileSizeMB: NotRequired[int]
    strategy: NotRequired[IcebergCompactionStrategyType]

SchemaFieldTypeDef = TypedDict(
    "SchemaFieldTypeDef",
    {
        "name": str,
        "type": str,
        "required": NotRequired[bool],
    },
)

class IcebergSnapshotManagementSettingsTypeDef(TypedDict):
    minSnapshotsToKeep: NotRequired[int]
    maxSnapshotAgeHours: NotRequired[int]

class IcebergUnreferencedFileRemovalSettingsTypeDef(TypedDict):
    unreferencedDays: NotRequired[int]
    nonCurrentDays: NotRequired[int]

class LastSuccessfulReplicatedUpdateTypeDef(TypedDict):
    metadataLocation: str
    timestamp: datetime

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListNamespacesRequestTypeDef(TypedDict):
    tableBucketARN: str
    prefix: NotRequired[str]
    continuationToken: NotRequired[str]
    maxNamespaces: NotRequired[int]

class NamespaceSummaryTypeDef(TypedDict):
    namespace: List[str]
    createdAt: datetime
    createdBy: str
    ownerAccountId: str
    namespaceId: NotRequired[str]
    tableBucketId: NotRequired[str]

ListTableBucketsRequestTypeDef = TypedDict(
    "ListTableBucketsRequestTypeDef",
    {
        "prefix": NotRequired[str],
        "continuationToken": NotRequired[str],
        "maxBuckets": NotRequired[int],
        "type": NotRequired[TableBucketTypeType],
    },
)
TableBucketSummaryTypeDef = TypedDict(
    "TableBucketSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "ownerAccountId": str,
        "createdAt": datetime,
        "tableBucketId": NotRequired[str],
        "type": NotRequired[TableBucketTypeType],
    },
)

class ListTablesRequestTypeDef(TypedDict):
    tableBucketARN: str
    namespace: NotRequired[str]
    prefix: NotRequired[str]
    continuationToken: NotRequired[str]
    maxTables: NotRequired[int]

TableSummaryTypeDef = TypedDict(
    "TableSummaryTypeDef",
    {
        "namespace": List[str],
        "name": str,
        "type": TableTypeType,
        "tableARN": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "managedByService": NotRequired[str],
        "namespaceId": NotRequired[str],
        "tableBucketId": NotRequired[str],
    },
)

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ReplicationInformationTypeDef(TypedDict):
    sourceTableARN: str

class PutTableBucketMetricsConfigurationRequestTypeDef(TypedDict):
    tableBucketARN: str

class PutTableBucketPolicyRequestTypeDef(TypedDict):
    tableBucketARN: str
    resourcePolicy: str

class PutTablePolicyRequestTypeDef(TypedDict):
    tableBucketARN: str
    namespace: str
    name: str
    resourcePolicy: str

class RenameTableRequestTypeDef(TypedDict):
    tableBucketARN: str
    namespace: str
    name: str
    newNamespaceName: NotRequired[str]
    newName: NotRequired[str]
    versionToken: NotRequired[str]

class ReplicationDestinationTypeDef(TypedDict):
    destinationTableBucketARN: str

class TableRecordExpirationSettingsTypeDef(TypedDict):
    days: NotRequired[int]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateTableMetadataLocationRequestTypeDef(TypedDict):
    tableBucketARN: str
    namespace: str
    name: str
    versionToken: str
    metadataLocation: str

class CreateNamespaceResponseTypeDef(TypedDict):
    tableBucketARN: str
    namespace: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTableBucketResponseTypeDef(TypedDict):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTableResponseTypeDef(TypedDict):
    tableARN: str
    versionToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetNamespaceResponseTypeDef(TypedDict):
    namespace: List[str]
    createdAt: datetime
    createdBy: str
    ownerAccountId: str
    namespaceId: str
    tableBucketId: str
    ResponseMetadata: ResponseMetadataTypeDef

GetTableBucketMetricsConfigurationResponseTypeDef = TypedDict(
    "GetTableBucketMetricsConfigurationResponseTypeDef",
    {
        "tableBucketARN": str,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetTableBucketPolicyResponseTypeDef(TypedDict):
    resourcePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

GetTableBucketResponseTypeDef = TypedDict(
    "GetTableBucketResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "ownerAccountId": str,
        "createdAt": datetime,
        "tableBucketId": str,
        "type": TableBucketTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetTableMetadataLocationResponseTypeDef(TypedDict):
    versionToken: str
    metadataLocation: str
    warehouseLocation: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTablePolicyResponseTypeDef(TypedDict):
    resourcePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutTableBucketReplicationResponseTypeDef(TypedDict):
    versionToken: str
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutTableReplicationResponseTypeDef(TypedDict):
    versionToken: str
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTableMetadataLocationResponseTypeDef(TypedDict):
    name: str
    tableARN: str
    namespace: List[str]
    versionToken: str
    metadataLocation: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTableBucketEncryptionResponseTypeDef(TypedDict):
    encryptionConfiguration: EncryptionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTableEncryptionResponseTypeDef(TypedDict):
    encryptionConfiguration: EncryptionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutTableBucketEncryptionRequestTypeDef(TypedDict):
    tableBucketARN: str
    encryptionConfiguration: EncryptionConfigurationTypeDef

class CreateTableBucketRequestTypeDef(TypedDict):
    name: str
    encryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]
    storageClassConfiguration: NotRequired[StorageClassConfigurationTypeDef]
    tags: NotRequired[Mapping[str, str]]

class GetTableBucketStorageClassResponseTypeDef(TypedDict):
    storageClassConfiguration: StorageClassConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTableStorageClassResponseTypeDef(TypedDict):
    storageClassConfiguration: StorageClassConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutTableBucketStorageClassRequestTypeDef(TypedDict):
    tableBucketARN: str
    storageClassConfiguration: StorageClassConfigurationTypeDef

class GetTableMaintenanceJobStatusResponseTypeDef(TypedDict):
    tableARN: str
    status: Dict[TableMaintenanceJobTypeType, TableMaintenanceJobStatusValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTableRecordExpirationJobStatusResponseTypeDef(TypedDict):
    status: TableRecordExpirationJobStatusType
    lastRunTimestamp: datetime
    failureMessage: str
    metrics: TableRecordExpirationJobMetricsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IcebergSchemaTypeDef(TypedDict):
    fields: Sequence[SchemaFieldTypeDef]

class TableMaintenanceSettingsTypeDef(TypedDict):
    icebergCompaction: NotRequired[IcebergCompactionSettingsTypeDef]
    icebergSnapshotManagement: NotRequired[IcebergSnapshotManagementSettingsTypeDef]

class TableBucketMaintenanceSettingsTypeDef(TypedDict):
    icebergUnreferencedFileRemoval: NotRequired[IcebergUnreferencedFileRemovalSettingsTypeDef]

class ReplicationDestinationStatusModelTypeDef(TypedDict):
    replicationStatus: ReplicationStatusType
    destinationTableBucketArn: str
    destinationTableArn: NotRequired[str]
    lastSuccessfulReplicatedUpdate: NotRequired[LastSuccessfulReplicatedUpdateTypeDef]
    failureMessage: NotRequired[str]

class ListNamespacesRequestPaginateTypeDef(TypedDict):
    tableBucketARN: str
    prefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListTableBucketsRequestPaginateTypeDef = TypedDict(
    "ListTableBucketsRequestPaginateTypeDef",
    {
        "prefix": NotRequired[str],
        "type": NotRequired[TableBucketTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListTablesRequestPaginateTypeDef(TypedDict):
    tableBucketARN: str
    namespace: NotRequired[str]
    prefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListNamespacesResponseTypeDef(TypedDict):
    namespaces: List[NamespaceSummaryTypeDef]
    continuationToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTableBucketsResponseTypeDef(TypedDict):
    tableBuckets: List[TableBucketSummaryTypeDef]
    continuationToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTablesResponseTypeDef(TypedDict):
    tables: List[TableSummaryTypeDef]
    continuationToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ManagedTableInformationTypeDef(TypedDict):
    replicationInformation: NotRequired[ReplicationInformationTypeDef]

class TableBucketReplicationRuleOutputTypeDef(TypedDict):
    destinations: List[ReplicationDestinationTypeDef]

class TableBucketReplicationRuleTypeDef(TypedDict):
    destinations: Sequence[ReplicationDestinationTypeDef]

class TableReplicationRuleOutputTypeDef(TypedDict):
    destinations: List[ReplicationDestinationTypeDef]

class TableReplicationRuleTypeDef(TypedDict):
    destinations: Sequence[ReplicationDestinationTypeDef]

class TableRecordExpirationConfigurationValueTypeDef(TypedDict):
    status: NotRequired[TableRecordExpirationStatusType]
    settings: NotRequired[TableRecordExpirationSettingsTypeDef]

class IcebergMetadataTypeDef(TypedDict):
    schema: IcebergSchemaTypeDef
    properties: NotRequired[Mapping[str, str]]

class TableMaintenanceConfigurationValueTypeDef(TypedDict):
    status: NotRequired[MaintenanceStatusType]
    settings: NotRequired[TableMaintenanceSettingsTypeDef]

class TableBucketMaintenanceConfigurationValueTypeDef(TypedDict):
    status: NotRequired[MaintenanceStatusType]
    settings: NotRequired[TableBucketMaintenanceSettingsTypeDef]

class GetTableReplicationStatusResponseTypeDef(TypedDict):
    sourceTableArn: str
    destinations: List[ReplicationDestinationStatusModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

GetTableResponseTypeDef = TypedDict(
    "GetTableResponseTypeDef",
    {
        "name": str,
        "type": TableTypeType,
        "tableARN": str,
        "namespace": List[str],
        "namespaceId": str,
        "versionToken": str,
        "metadataLocation": str,
        "warehouseLocation": str,
        "createdAt": datetime,
        "createdBy": str,
        "managedByService": str,
        "modifiedAt": datetime,
        "modifiedBy": str,
        "ownerAccountId": str,
        "format": Literal["ICEBERG"],
        "tableBucketId": str,
        "managedTableInformation": ManagedTableInformationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class TableBucketReplicationConfigurationOutputTypeDef(TypedDict):
    role: str
    rules: List[TableBucketReplicationRuleOutputTypeDef]

class TableBucketReplicationConfigurationTypeDef(TypedDict):
    role: str
    rules: Sequence[TableBucketReplicationRuleTypeDef]

class TableReplicationConfigurationOutputTypeDef(TypedDict):
    role: str
    rules: List[TableReplicationRuleOutputTypeDef]

class TableReplicationConfigurationTypeDef(TypedDict):
    role: str
    rules: Sequence[TableReplicationRuleTypeDef]

class GetTableRecordExpirationConfigurationResponseTypeDef(TypedDict):
    configuration: TableRecordExpirationConfigurationValueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutTableRecordExpirationConfigurationRequestTypeDef(TypedDict):
    tableArn: str
    value: TableRecordExpirationConfigurationValueTypeDef

class TableMetadataTypeDef(TypedDict):
    iceberg: NotRequired[IcebergMetadataTypeDef]

class GetTableMaintenanceConfigurationResponseTypeDef(TypedDict):
    tableARN: str
    configuration: Dict[TableMaintenanceTypeType, TableMaintenanceConfigurationValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

PutTableMaintenanceConfigurationRequestTypeDef = TypedDict(
    "PutTableMaintenanceConfigurationRequestTypeDef",
    {
        "tableBucketARN": str,
        "namespace": str,
        "name": str,
        "type": TableMaintenanceTypeType,
        "value": TableMaintenanceConfigurationValueTypeDef,
    },
)

class GetTableBucketMaintenanceConfigurationResponseTypeDef(TypedDict):
    tableBucketARN: str
    configuration: Dict[
        Literal["icebergUnreferencedFileRemoval"], TableBucketMaintenanceConfigurationValueTypeDef
    ]
    ResponseMetadata: ResponseMetadataTypeDef

PutTableBucketMaintenanceConfigurationRequestTypeDef = TypedDict(
    "PutTableBucketMaintenanceConfigurationRequestTypeDef",
    {
        "tableBucketARN": str,
        "type": Literal["icebergUnreferencedFileRemoval"],
        "value": TableBucketMaintenanceConfigurationValueTypeDef,
    },
)

class GetTableBucketReplicationResponseTypeDef(TypedDict):
    versionToken: str
    configuration: TableBucketReplicationConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

TableBucketReplicationConfigurationUnionTypeDef = Union[
    TableBucketReplicationConfigurationTypeDef, TableBucketReplicationConfigurationOutputTypeDef
]

class GetTableReplicationResponseTypeDef(TypedDict):
    versionToken: str
    configuration: TableReplicationConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

TableReplicationConfigurationUnionTypeDef = Union[
    TableReplicationConfigurationTypeDef, TableReplicationConfigurationOutputTypeDef
]
CreateTableRequestTypeDef = TypedDict(
    "CreateTableRequestTypeDef",
    {
        "tableBucketARN": str,
        "namespace": str,
        "name": str,
        "format": Literal["ICEBERG"],
        "metadata": NotRequired[TableMetadataTypeDef],
        "encryptionConfiguration": NotRequired[EncryptionConfigurationTypeDef],
        "storageClassConfiguration": NotRequired[StorageClassConfigurationTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)

class PutTableBucketReplicationRequestTypeDef(TypedDict):
    tableBucketARN: str
    configuration: TableBucketReplicationConfigurationUnionTypeDef
    versionToken: NotRequired[str]

class PutTableReplicationRequestTypeDef(TypedDict):
    tableArn: str
    configuration: TableReplicationConfigurationUnionTypeDef
    versionToken: NotRequired[str]
