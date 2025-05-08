"""
Type annotations for docdb-elastic service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_docdb_elastic.type_defs import ApplyPendingMaintenanceActionInputTypeDef

    data: ApplyPendingMaintenanceActionInputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

from .literals import AuthType, OptInTypeType, SnapshotTypeType, StatusType

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
    "ApplyPendingMaintenanceActionInputTypeDef",
    "ApplyPendingMaintenanceActionOutputTypeDef",
    "ClusterInListTypeDef",
    "ClusterSnapshotInListTypeDef",
    "ClusterSnapshotTypeDef",
    "ClusterTypeDef",
    "CopyClusterSnapshotInputTypeDef",
    "CopyClusterSnapshotOutputTypeDef",
    "CreateClusterInputTypeDef",
    "CreateClusterOutputTypeDef",
    "CreateClusterSnapshotInputTypeDef",
    "CreateClusterSnapshotOutputTypeDef",
    "DeleteClusterInputTypeDef",
    "DeleteClusterOutputTypeDef",
    "DeleteClusterSnapshotInputTypeDef",
    "DeleteClusterSnapshotOutputTypeDef",
    "GetClusterInputTypeDef",
    "GetClusterOutputTypeDef",
    "GetClusterSnapshotInputTypeDef",
    "GetClusterSnapshotOutputTypeDef",
    "GetPendingMaintenanceActionInputTypeDef",
    "GetPendingMaintenanceActionOutputTypeDef",
    "ListClusterSnapshotsInputPaginateTypeDef",
    "ListClusterSnapshotsInputTypeDef",
    "ListClusterSnapshotsOutputTypeDef",
    "ListClustersInputPaginateTypeDef",
    "ListClustersInputTypeDef",
    "ListClustersOutputTypeDef",
    "ListPendingMaintenanceActionsInputPaginateTypeDef",
    "ListPendingMaintenanceActionsInputTypeDef",
    "ListPendingMaintenanceActionsOutputTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PendingMaintenanceActionDetailsTypeDef",
    "ResourcePendingMaintenanceActionTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreClusterFromSnapshotInputTypeDef",
    "RestoreClusterFromSnapshotOutputTypeDef",
    "ShardTypeDef",
    "StartClusterInputTypeDef",
    "StartClusterOutputTypeDef",
    "StopClusterInputTypeDef",
    "StopClusterOutputTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateClusterInputTypeDef",
    "UpdateClusterOutputTypeDef",
)

class ApplyPendingMaintenanceActionInputTypeDef(TypedDict):
    applyAction: str
    optInType: OptInTypeType
    resourceArn: str
    applyOn: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ClusterInListTypeDef(TypedDict):
    clusterArn: str
    clusterName: str
    status: StatusType

class ClusterSnapshotInListTypeDef(TypedDict):
    clusterArn: str
    snapshotArn: str
    snapshotCreationTime: str
    snapshotName: str
    status: StatusType

class ClusterSnapshotTypeDef(TypedDict):
    adminUserName: str
    clusterArn: str
    clusterCreationTime: str
    kmsKeyId: str
    snapshotArn: str
    snapshotCreationTime: str
    snapshotName: str
    status: StatusType
    subnetIds: List[str]
    vpcSecurityGroupIds: List[str]
    snapshotType: NotRequired[SnapshotTypeType]

class ShardTypeDef(TypedDict):
    createTime: str
    shardId: str
    status: StatusType

class CopyClusterSnapshotInputTypeDef(TypedDict):
    snapshotArn: str
    targetSnapshotName: str
    copyTags: NotRequired[bool]
    kmsKeyId: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateClusterInputTypeDef(TypedDict):
    adminUserName: str
    adminUserPassword: str
    authType: AuthType
    clusterName: str
    shardCapacity: int
    shardCount: int
    backupRetentionPeriod: NotRequired[int]
    clientToken: NotRequired[str]
    kmsKeyId: NotRequired[str]
    preferredBackupWindow: NotRequired[str]
    preferredMaintenanceWindow: NotRequired[str]
    shardInstanceCount: NotRequired[int]
    subnetIds: NotRequired[Sequence[str]]
    tags: NotRequired[Mapping[str, str]]
    vpcSecurityGroupIds: NotRequired[Sequence[str]]

class CreateClusterSnapshotInputTypeDef(TypedDict):
    clusterArn: str
    snapshotName: str
    tags: NotRequired[Mapping[str, str]]

class DeleteClusterInputTypeDef(TypedDict):
    clusterArn: str

class DeleteClusterSnapshotInputTypeDef(TypedDict):
    snapshotArn: str

class GetClusterInputTypeDef(TypedDict):
    clusterArn: str

class GetClusterSnapshotInputTypeDef(TypedDict):
    snapshotArn: str

class GetPendingMaintenanceActionInputTypeDef(TypedDict):
    resourceArn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListClusterSnapshotsInputTypeDef(TypedDict):
    clusterArn: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    snapshotType: NotRequired[str]

class ListClustersInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListPendingMaintenanceActionsInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class PendingMaintenanceActionDetailsTypeDef(TypedDict):
    action: str
    autoAppliedAfterDate: NotRequired[str]
    currentApplyDate: NotRequired[str]
    description: NotRequired[str]
    forcedApplyDate: NotRequired[str]
    optInStatus: NotRequired[str]

class RestoreClusterFromSnapshotInputTypeDef(TypedDict):
    clusterName: str
    snapshotArn: str
    kmsKeyId: NotRequired[str]
    shardCapacity: NotRequired[int]
    shardInstanceCount: NotRequired[int]
    subnetIds: NotRequired[Sequence[str]]
    tags: NotRequired[Mapping[str, str]]
    vpcSecurityGroupIds: NotRequired[Sequence[str]]

class StartClusterInputTypeDef(TypedDict):
    clusterArn: str

class StopClusterInputTypeDef(TypedDict):
    clusterArn: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateClusterInputTypeDef(TypedDict):
    clusterArn: str
    adminUserPassword: NotRequired[str]
    authType: NotRequired[AuthType]
    backupRetentionPeriod: NotRequired[int]
    clientToken: NotRequired[str]
    preferredBackupWindow: NotRequired[str]
    preferredMaintenanceWindow: NotRequired[str]
    shardCapacity: NotRequired[int]
    shardCount: NotRequired[int]
    shardInstanceCount: NotRequired[int]
    subnetIds: NotRequired[Sequence[str]]
    vpcSecurityGroupIds: NotRequired[Sequence[str]]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListClustersOutputTypeDef(TypedDict):
    clusters: List[ClusterInListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListClusterSnapshotsOutputTypeDef(TypedDict):
    snapshots: List[ClusterSnapshotInListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CopyClusterSnapshotOutputTypeDef(TypedDict):
    snapshot: ClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterSnapshotOutputTypeDef(TypedDict):
    snapshot: ClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterSnapshotOutputTypeDef(TypedDict):
    snapshot: ClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetClusterSnapshotOutputTypeDef(TypedDict):
    snapshot: ClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterTypeDef(TypedDict):
    adminUserName: str
    authType: AuthType
    clusterArn: str
    clusterEndpoint: str
    clusterName: str
    createTime: str
    kmsKeyId: str
    preferredMaintenanceWindow: str
    shardCapacity: int
    shardCount: int
    status: StatusType
    subnetIds: List[str]
    vpcSecurityGroupIds: List[str]
    backupRetentionPeriod: NotRequired[int]
    preferredBackupWindow: NotRequired[str]
    shardInstanceCount: NotRequired[int]
    shards: NotRequired[List[ShardTypeDef]]

class ListClusterSnapshotsInputPaginateTypeDef(TypedDict):
    clusterArn: NotRequired[str]
    snapshotType: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListClustersInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPendingMaintenanceActionsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ResourcePendingMaintenanceActionTypeDef(TypedDict):
    pendingMaintenanceActionDetails: NotRequired[List[PendingMaintenanceActionDetailsTypeDef]]
    resourceArn: NotRequired[str]

class CreateClusterOutputTypeDef(TypedDict):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterOutputTypeDef(TypedDict):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetClusterOutputTypeDef(TypedDict):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreClusterFromSnapshotOutputTypeDef(TypedDict):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartClusterOutputTypeDef(TypedDict):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopClusterOutputTypeDef(TypedDict):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterOutputTypeDef(TypedDict):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ApplyPendingMaintenanceActionOutputTypeDef(TypedDict):
    resourcePendingMaintenanceAction: ResourcePendingMaintenanceActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPendingMaintenanceActionOutputTypeDef(TypedDict):
    resourcePendingMaintenanceAction: ResourcePendingMaintenanceActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPendingMaintenanceActionsOutputTypeDef(TypedDict):
    resourcePendingMaintenanceActions: List[ResourcePendingMaintenanceActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
