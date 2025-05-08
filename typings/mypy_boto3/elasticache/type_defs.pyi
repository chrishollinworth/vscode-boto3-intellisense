"""
Type annotations for elasticache service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_elasticache.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AuthenticationTypeType,
    AuthTokenUpdateStatusType,
    AuthTokenUpdateStrategyTypeType,
    AutomaticFailoverStatusType,
    AZModeType,
    ChangeTypeType,
    ClusterModeType,
    DataTieringStatusType,
    DestinationTypeType,
    InputAuthenticationTypeType,
    IpDiscoveryType,
    LogDeliveryConfigurationStatusType,
    LogFormatType,
    LogTypeType,
    MultiAZStatusType,
    NetworkTypeType,
    NodeUpdateInitiatedByType,
    NodeUpdateStatusType,
    OutpostModeType,
    PendingAutomaticFailoverStatusType,
    ServiceUpdateSeverityType,
    ServiceUpdateStatusType,
    SlaMetType,
    SourceTypeType,
    TransitEncryptionModeType,
    UpdateActionStatusType,
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
    "AddTagsToResourceMessageTypeDef",
    "AllowedNodeTypeModificationsMessageTypeDef",
    "AuthenticationModeTypeDef",
    "AuthenticationTypeDef",
    "AuthorizeCacheSecurityGroupIngressMessageTypeDef",
    "AuthorizeCacheSecurityGroupIngressResultTypeDef",
    "AvailabilityZoneTypeDef",
    "BatchApplyUpdateActionMessageTypeDef",
    "BatchStopUpdateActionMessageTypeDef",
    "CacheClusterMessageTypeDef",
    "CacheClusterTypeDef",
    "CacheEngineVersionMessageTypeDef",
    "CacheEngineVersionTypeDef",
    "CacheNodeTypeDef",
    "CacheNodeTypeSpecificParameterTypeDef",
    "CacheNodeTypeSpecificValueTypeDef",
    "CacheNodeUpdateStatusTypeDef",
    "CacheParameterGroupDetailsTypeDef",
    "CacheParameterGroupNameMessageTypeDef",
    "CacheParameterGroupStatusTypeDef",
    "CacheParameterGroupTypeDef",
    "CacheParameterGroupsMessageTypeDef",
    "CacheSecurityGroupMembershipTypeDef",
    "CacheSecurityGroupMessageTypeDef",
    "CacheSecurityGroupTypeDef",
    "CacheSubnetGroupMessageTypeDef",
    "CacheSubnetGroupTypeDef",
    "CacheUsageLimitsTypeDef",
    "CloudWatchLogsDestinationDetailsTypeDef",
    "CompleteMigrationMessageTypeDef",
    "CompleteMigrationResponseTypeDef",
    "ConfigureShardTypeDef",
    "CopyServerlessCacheSnapshotRequestTypeDef",
    "CopyServerlessCacheSnapshotResponseTypeDef",
    "CopySnapshotMessageTypeDef",
    "CopySnapshotResultTypeDef",
    "CreateCacheClusterMessageTypeDef",
    "CreateCacheClusterResultTypeDef",
    "CreateCacheParameterGroupMessageTypeDef",
    "CreateCacheParameterGroupResultTypeDef",
    "CreateCacheSecurityGroupMessageTypeDef",
    "CreateCacheSecurityGroupResultTypeDef",
    "CreateCacheSubnetGroupMessageTypeDef",
    "CreateCacheSubnetGroupResultTypeDef",
    "CreateGlobalReplicationGroupMessageTypeDef",
    "CreateGlobalReplicationGroupResultTypeDef",
    "CreateReplicationGroupMessageTypeDef",
    "CreateReplicationGroupResultTypeDef",
    "CreateServerlessCacheRequestTypeDef",
    "CreateServerlessCacheResponseTypeDef",
    "CreateServerlessCacheSnapshotRequestTypeDef",
    "CreateServerlessCacheSnapshotResponseTypeDef",
    "CreateSnapshotMessageTypeDef",
    "CreateSnapshotResultTypeDef",
    "CreateUserGroupMessageTypeDef",
    "CreateUserMessageTypeDef",
    "CustomerNodeEndpointTypeDef",
    "DataStorageTypeDef",
    "DecreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef",
    "DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef",
    "DecreaseReplicaCountMessageTypeDef",
    "DecreaseReplicaCountResultTypeDef",
    "DeleteCacheClusterMessageTypeDef",
    "DeleteCacheClusterResultTypeDef",
    "DeleteCacheParameterGroupMessageTypeDef",
    "DeleteCacheSecurityGroupMessageTypeDef",
    "DeleteCacheSubnetGroupMessageTypeDef",
    "DeleteGlobalReplicationGroupMessageTypeDef",
    "DeleteGlobalReplicationGroupResultTypeDef",
    "DeleteReplicationGroupMessageTypeDef",
    "DeleteReplicationGroupResultTypeDef",
    "DeleteServerlessCacheRequestTypeDef",
    "DeleteServerlessCacheResponseTypeDef",
    "DeleteServerlessCacheSnapshotRequestTypeDef",
    "DeleteServerlessCacheSnapshotResponseTypeDef",
    "DeleteSnapshotMessageTypeDef",
    "DeleteSnapshotResultTypeDef",
    "DeleteUserGroupMessageTypeDef",
    "DeleteUserMessageTypeDef",
    "DescribeCacheClustersMessagePaginateTypeDef",
    "DescribeCacheClustersMessageTypeDef",
    "DescribeCacheClustersMessageWaitExtraTypeDef",
    "DescribeCacheClustersMessageWaitTypeDef",
    "DescribeCacheEngineVersionsMessagePaginateTypeDef",
    "DescribeCacheEngineVersionsMessageTypeDef",
    "DescribeCacheParameterGroupsMessagePaginateTypeDef",
    "DescribeCacheParameterGroupsMessageTypeDef",
    "DescribeCacheParametersMessagePaginateTypeDef",
    "DescribeCacheParametersMessageTypeDef",
    "DescribeCacheSecurityGroupsMessagePaginateTypeDef",
    "DescribeCacheSecurityGroupsMessageTypeDef",
    "DescribeCacheSubnetGroupsMessagePaginateTypeDef",
    "DescribeCacheSubnetGroupsMessageTypeDef",
    "DescribeEngineDefaultParametersMessagePaginateTypeDef",
    "DescribeEngineDefaultParametersMessageTypeDef",
    "DescribeEngineDefaultParametersResultTypeDef",
    "DescribeEventsMessagePaginateTypeDef",
    "DescribeEventsMessageTypeDef",
    "DescribeGlobalReplicationGroupsMessagePaginateTypeDef",
    "DescribeGlobalReplicationGroupsMessageTypeDef",
    "DescribeGlobalReplicationGroupsResultTypeDef",
    "DescribeReplicationGroupsMessagePaginateTypeDef",
    "DescribeReplicationGroupsMessageTypeDef",
    "DescribeReplicationGroupsMessageWaitExtraTypeDef",
    "DescribeReplicationGroupsMessageWaitTypeDef",
    "DescribeReservedCacheNodesMessagePaginateTypeDef",
    "DescribeReservedCacheNodesMessageTypeDef",
    "DescribeReservedCacheNodesOfferingsMessagePaginateTypeDef",
    "DescribeReservedCacheNodesOfferingsMessageTypeDef",
    "DescribeServerlessCacheSnapshotsRequestPaginateTypeDef",
    "DescribeServerlessCacheSnapshotsRequestTypeDef",
    "DescribeServerlessCacheSnapshotsResponseTypeDef",
    "DescribeServerlessCachesRequestPaginateTypeDef",
    "DescribeServerlessCachesRequestTypeDef",
    "DescribeServerlessCachesResponseTypeDef",
    "DescribeServiceUpdatesMessagePaginateTypeDef",
    "DescribeServiceUpdatesMessageTypeDef",
    "DescribeSnapshotsListMessageTypeDef",
    "DescribeSnapshotsMessagePaginateTypeDef",
    "DescribeSnapshotsMessageTypeDef",
    "DescribeUpdateActionsMessagePaginateTypeDef",
    "DescribeUpdateActionsMessageTypeDef",
    "DescribeUserGroupsMessagePaginateTypeDef",
    "DescribeUserGroupsMessageTypeDef",
    "DescribeUserGroupsResultTypeDef",
    "DescribeUsersMessagePaginateTypeDef",
    "DescribeUsersMessageTypeDef",
    "DescribeUsersResultTypeDef",
    "DestinationDetailsTypeDef",
    "DisassociateGlobalReplicationGroupMessageTypeDef",
    "DisassociateGlobalReplicationGroupResultTypeDef",
    "EC2SecurityGroupTypeDef",
    "ECPUPerSecondTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EndpointTypeDef",
    "EngineDefaultsTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "ExportServerlessCacheSnapshotRequestTypeDef",
    "ExportServerlessCacheSnapshotResponseTypeDef",
    "FailoverGlobalReplicationGroupMessageTypeDef",
    "FailoverGlobalReplicationGroupResultTypeDef",
    "FilterTypeDef",
    "GlobalNodeGroupTypeDef",
    "GlobalReplicationGroupInfoTypeDef",
    "GlobalReplicationGroupMemberTypeDef",
    "GlobalReplicationGroupTypeDef",
    "IncreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef",
    "IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef",
    "IncreaseReplicaCountMessageTypeDef",
    "IncreaseReplicaCountResultTypeDef",
    "KinesisFirehoseDestinationDetailsTypeDef",
    "ListAllowedNodeTypeModificationsMessageTypeDef",
    "ListTagsForResourceMessageTypeDef",
    "LogDeliveryConfigurationRequestTypeDef",
    "LogDeliveryConfigurationTypeDef",
    "ModifyCacheClusterMessageTypeDef",
    "ModifyCacheClusterResultTypeDef",
    "ModifyCacheParameterGroupMessageTypeDef",
    "ModifyCacheSubnetGroupMessageTypeDef",
    "ModifyCacheSubnetGroupResultTypeDef",
    "ModifyGlobalReplicationGroupMessageTypeDef",
    "ModifyGlobalReplicationGroupResultTypeDef",
    "ModifyReplicationGroupMessageTypeDef",
    "ModifyReplicationGroupResultTypeDef",
    "ModifyReplicationGroupShardConfigurationMessageTypeDef",
    "ModifyReplicationGroupShardConfigurationResultTypeDef",
    "ModifyServerlessCacheRequestTypeDef",
    "ModifyServerlessCacheResponseTypeDef",
    "ModifyUserGroupMessageTypeDef",
    "ModifyUserMessageTypeDef",
    "NodeGroupConfigurationOutputTypeDef",
    "NodeGroupConfigurationTypeDef",
    "NodeGroupConfigurationUnionTypeDef",
    "NodeGroupMemberTypeDef",
    "NodeGroupMemberUpdateStatusTypeDef",
    "NodeGroupTypeDef",
    "NodeGroupUpdateStatusTypeDef",
    "NodeSnapshotTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterNameValueTypeDef",
    "ParameterTypeDef",
    "PendingLogDeliveryConfigurationTypeDef",
    "PendingModifiedValuesTypeDef",
    "ProcessedUpdateActionTypeDef",
    "PurchaseReservedCacheNodesOfferingMessageTypeDef",
    "PurchaseReservedCacheNodesOfferingResultTypeDef",
    "RebalanceSlotsInGlobalReplicationGroupMessageTypeDef",
    "RebalanceSlotsInGlobalReplicationGroupResultTypeDef",
    "RebootCacheClusterMessageTypeDef",
    "RebootCacheClusterResultTypeDef",
    "RecurringChargeTypeDef",
    "RegionalConfigurationTypeDef",
    "RemoveTagsFromResourceMessageTypeDef",
    "ReplicationGroupMessageTypeDef",
    "ReplicationGroupPendingModifiedValuesTypeDef",
    "ReplicationGroupTypeDef",
    "ReservedCacheNodeMessageTypeDef",
    "ReservedCacheNodeTypeDef",
    "ReservedCacheNodesOfferingMessageTypeDef",
    "ReservedCacheNodesOfferingTypeDef",
    "ResetCacheParameterGroupMessageTypeDef",
    "ReshardingConfigurationTypeDef",
    "ReshardingStatusTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeCacheSecurityGroupIngressMessageTypeDef",
    "RevokeCacheSecurityGroupIngressResultTypeDef",
    "ScaleConfigTypeDef",
    "SecurityGroupMembershipTypeDef",
    "ServerlessCacheConfigurationTypeDef",
    "ServerlessCacheSnapshotTypeDef",
    "ServerlessCacheTypeDef",
    "ServiceUpdateTypeDef",
    "ServiceUpdatesMessageTypeDef",
    "SlotMigrationTypeDef",
    "SnapshotTypeDef",
    "StartMigrationMessageTypeDef",
    "StartMigrationResponseTypeDef",
    "SubnetOutpostTypeDef",
    "SubnetTypeDef",
    "TagListMessageTypeDef",
    "TagTypeDef",
    "TestFailoverMessageTypeDef",
    "TestFailoverResultTypeDef",
    "TestMigrationMessageTypeDef",
    "TestMigrationResponseTypeDef",
    "TimeRangeFilterTypeDef",
    "TimestampTypeDef",
    "UnprocessedUpdateActionTypeDef",
    "UpdateActionResultsMessageTypeDef",
    "UpdateActionTypeDef",
    "UpdateActionsMessageTypeDef",
    "UserGroupPendingChangesTypeDef",
    "UserGroupResponseTypeDef",
    "UserGroupTypeDef",
    "UserGroupsUpdateStatusTypeDef",
    "UserResponseTypeDef",
    "UserTypeDef",
    "WaiterConfigTypeDef",
)

class TagTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

AuthenticationModeTypeDef = TypedDict(
    "AuthenticationModeTypeDef",
    {
        "Type": NotRequired[InputAuthenticationTypeType],
        "Passwords": NotRequired[Sequence[str]],
    },
)
AuthenticationTypeDef = TypedDict(
    "AuthenticationTypeDef",
    {
        "Type": NotRequired[AuthenticationTypeType],
        "PasswordCount": NotRequired[int],
    },
)

class AuthorizeCacheSecurityGroupIngressMessageTypeDef(TypedDict):
    CacheSecurityGroupName: str
    EC2SecurityGroupName: str
    EC2SecurityGroupOwnerId: str

class AvailabilityZoneTypeDef(TypedDict):
    Name: NotRequired[str]

class BatchApplyUpdateActionMessageTypeDef(TypedDict):
    ServiceUpdateName: str
    ReplicationGroupIds: NotRequired[Sequence[str]]
    CacheClusterIds: NotRequired[Sequence[str]]

class BatchStopUpdateActionMessageTypeDef(TypedDict):
    ServiceUpdateName: str
    ReplicationGroupIds: NotRequired[Sequence[str]]
    CacheClusterIds: NotRequired[Sequence[str]]

class CacheParameterGroupStatusTypeDef(TypedDict):
    CacheParameterGroupName: NotRequired[str]
    ParameterApplyStatus: NotRequired[str]
    CacheNodeIdsToReboot: NotRequired[List[str]]

class CacheSecurityGroupMembershipTypeDef(TypedDict):
    CacheSecurityGroupName: NotRequired[str]
    Status: NotRequired[str]

class EndpointTypeDef(TypedDict):
    Address: NotRequired[str]
    Port: NotRequired[int]

class NotificationConfigurationTypeDef(TypedDict):
    TopicArn: NotRequired[str]
    TopicStatus: NotRequired[str]

class SecurityGroupMembershipTypeDef(TypedDict):
    SecurityGroupId: NotRequired[str]
    Status: NotRequired[str]

class CacheEngineVersionTypeDef(TypedDict):
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    CacheParameterGroupFamily: NotRequired[str]
    CacheEngineDescription: NotRequired[str]
    CacheEngineVersionDescription: NotRequired[str]

class CacheNodeTypeSpecificValueTypeDef(TypedDict):
    CacheNodeType: NotRequired[str]
    Value: NotRequired[str]

class CacheNodeUpdateStatusTypeDef(TypedDict):
    CacheNodeId: NotRequired[str]
    NodeUpdateStatus: NotRequired[NodeUpdateStatusType]
    NodeDeletionDate: NotRequired[datetime]
    NodeUpdateStartDate: NotRequired[datetime]
    NodeUpdateEndDate: NotRequired[datetime]
    NodeUpdateInitiatedBy: NotRequired[NodeUpdateInitiatedByType]
    NodeUpdateInitiatedDate: NotRequired[datetime]
    NodeUpdateStatusModifiedDate: NotRequired[datetime]

class ParameterTypeDef(TypedDict):
    ParameterName: NotRequired[str]
    ParameterValue: NotRequired[str]
    Description: NotRequired[str]
    Source: NotRequired[str]
    DataType: NotRequired[str]
    AllowedValues: NotRequired[str]
    IsModifiable: NotRequired[bool]
    MinimumEngineVersion: NotRequired[str]
    ChangeType: NotRequired[ChangeTypeType]

class CacheParameterGroupTypeDef(TypedDict):
    CacheParameterGroupName: NotRequired[str]
    CacheParameterGroupFamily: NotRequired[str]
    Description: NotRequired[str]
    IsGlobal: NotRequired[bool]
    ARN: NotRequired[str]

class EC2SecurityGroupTypeDef(TypedDict):
    Status: NotRequired[str]
    EC2SecurityGroupName: NotRequired[str]
    EC2SecurityGroupOwnerId: NotRequired[str]

class DataStorageTypeDef(TypedDict):
    Unit: Literal["GB"]
    Maximum: NotRequired[int]
    Minimum: NotRequired[int]

class ECPUPerSecondTypeDef(TypedDict):
    Maximum: NotRequired[int]
    Minimum: NotRequired[int]

class CloudWatchLogsDestinationDetailsTypeDef(TypedDict):
    LogGroup: NotRequired[str]

class CompleteMigrationMessageTypeDef(TypedDict):
    ReplicationGroupId: str
    Force: NotRequired[bool]

class ConfigureShardTypeDef(TypedDict):
    NodeGroupId: str
    NewReplicaCount: int
    PreferredAvailabilityZones: NotRequired[Sequence[str]]
    PreferredOutpostArns: NotRequired[Sequence[str]]

class CreateGlobalReplicationGroupMessageTypeDef(TypedDict):
    GlobalReplicationGroupIdSuffix: str
    PrimaryReplicationGroupId: str
    GlobalReplicationGroupDescription: NotRequired[str]

class CustomerNodeEndpointTypeDef(TypedDict):
    Address: NotRequired[str]
    Port: NotRequired[int]

class DecreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef(TypedDict):
    GlobalReplicationGroupId: str
    NodeGroupCount: int
    ApplyImmediately: bool
    GlobalNodeGroupsToRemove: NotRequired[Sequence[str]]
    GlobalNodeGroupsToRetain: NotRequired[Sequence[str]]

class DeleteCacheClusterMessageTypeDef(TypedDict):
    CacheClusterId: str
    FinalSnapshotIdentifier: NotRequired[str]

class DeleteCacheParameterGroupMessageTypeDef(TypedDict):
    CacheParameterGroupName: str

class DeleteCacheSecurityGroupMessageTypeDef(TypedDict):
    CacheSecurityGroupName: str

class DeleteCacheSubnetGroupMessageTypeDef(TypedDict):
    CacheSubnetGroupName: str

class DeleteGlobalReplicationGroupMessageTypeDef(TypedDict):
    GlobalReplicationGroupId: str
    RetainPrimaryReplicationGroup: bool

class DeleteReplicationGroupMessageTypeDef(TypedDict):
    ReplicationGroupId: str
    RetainPrimaryCluster: NotRequired[bool]
    FinalSnapshotIdentifier: NotRequired[str]

class DeleteServerlessCacheRequestTypeDef(TypedDict):
    ServerlessCacheName: str
    FinalSnapshotName: NotRequired[str]

class DeleteServerlessCacheSnapshotRequestTypeDef(TypedDict):
    ServerlessCacheSnapshotName: str

class DeleteSnapshotMessageTypeDef(TypedDict):
    SnapshotName: str

class DeleteUserGroupMessageTypeDef(TypedDict):
    UserGroupId: str

class DeleteUserMessageTypeDef(TypedDict):
    UserId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeCacheClustersMessageTypeDef(TypedDict):
    CacheClusterId: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    ShowCacheNodeInfo: NotRequired[bool]
    ShowCacheClustersNotInReplicationGroups: NotRequired[bool]

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class DescribeCacheEngineVersionsMessageTypeDef(TypedDict):
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    CacheParameterGroupFamily: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    DefaultOnly: NotRequired[bool]

class DescribeCacheParameterGroupsMessageTypeDef(TypedDict):
    CacheParameterGroupName: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeCacheParametersMessageTypeDef(TypedDict):
    CacheParameterGroupName: str
    Source: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeCacheSecurityGroupsMessageTypeDef(TypedDict):
    CacheSecurityGroupName: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeCacheSubnetGroupsMessageTypeDef(TypedDict):
    CacheSubnetGroupName: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeEngineDefaultParametersMessageTypeDef(TypedDict):
    CacheParameterGroupFamily: str
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class DescribeGlobalReplicationGroupsMessageTypeDef(TypedDict):
    GlobalReplicationGroupId: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    ShowMemberInfo: NotRequired[bool]

class DescribeReplicationGroupsMessageTypeDef(TypedDict):
    ReplicationGroupId: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeReservedCacheNodesMessageTypeDef(TypedDict):
    ReservedCacheNodeId: NotRequired[str]
    ReservedCacheNodesOfferingId: NotRequired[str]
    CacheNodeType: NotRequired[str]
    Duration: NotRequired[str]
    ProductDescription: NotRequired[str]
    OfferingType: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeReservedCacheNodesOfferingsMessageTypeDef(TypedDict):
    ReservedCacheNodesOfferingId: NotRequired[str]
    CacheNodeType: NotRequired[str]
    Duration: NotRequired[str]
    ProductDescription: NotRequired[str]
    OfferingType: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeServerlessCacheSnapshotsRequestTypeDef(TypedDict):
    ServerlessCacheName: NotRequired[str]
    ServerlessCacheSnapshotName: NotRequired[str]
    SnapshotType: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeServerlessCachesRequestTypeDef(TypedDict):
    ServerlessCacheName: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeServiceUpdatesMessageTypeDef(TypedDict):
    ServiceUpdateName: NotRequired[str]
    ServiceUpdateStatus: NotRequired[Sequence[ServiceUpdateStatusType]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeSnapshotsMessageTypeDef(TypedDict):
    ReplicationGroupId: NotRequired[str]
    CacheClusterId: NotRequired[str]
    SnapshotName: NotRequired[str]
    SnapshotSource: NotRequired[str]
    Marker: NotRequired[str]
    MaxRecords: NotRequired[int]
    ShowNodeGroupConfig: NotRequired[bool]

class DescribeUserGroupsMessageTypeDef(TypedDict):
    UserGroupId: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class FilterTypeDef(TypedDict):
    Name: str
    Values: Sequence[str]

class KinesisFirehoseDestinationDetailsTypeDef(TypedDict):
    DeliveryStream: NotRequired[str]

class DisassociateGlobalReplicationGroupMessageTypeDef(TypedDict):
    GlobalReplicationGroupId: str
    ReplicationGroupId: str
    ReplicationGroupRegion: str

class EventTypeDef(TypedDict):
    SourceIdentifier: NotRequired[str]
    SourceType: NotRequired[SourceTypeType]
    Message: NotRequired[str]
    Date: NotRequired[datetime]

class ExportServerlessCacheSnapshotRequestTypeDef(TypedDict):
    ServerlessCacheSnapshotName: str
    S3BucketName: str

class FailoverGlobalReplicationGroupMessageTypeDef(TypedDict):
    GlobalReplicationGroupId: str
    PrimaryRegion: str
    PrimaryReplicationGroupId: str

class GlobalNodeGroupTypeDef(TypedDict):
    GlobalNodeGroupId: NotRequired[str]
    Slots: NotRequired[str]

class GlobalReplicationGroupInfoTypeDef(TypedDict):
    GlobalReplicationGroupId: NotRequired[str]
    GlobalReplicationGroupMemberRole: NotRequired[str]

class GlobalReplicationGroupMemberTypeDef(TypedDict):
    ReplicationGroupId: NotRequired[str]
    ReplicationGroupRegion: NotRequired[str]
    Role: NotRequired[str]
    AutomaticFailover: NotRequired[AutomaticFailoverStatusType]
    Status: NotRequired[str]

class ListAllowedNodeTypeModificationsMessageTypeDef(TypedDict):
    CacheClusterId: NotRequired[str]
    ReplicationGroupId: NotRequired[str]

class ListTagsForResourceMessageTypeDef(TypedDict):
    ResourceName: str

class ScaleConfigTypeDef(TypedDict):
    ScalePercentage: NotRequired[int]
    ScaleIntervalMinutes: NotRequired[int]

class ParameterNameValueTypeDef(TypedDict):
    ParameterName: NotRequired[str]
    ParameterValue: NotRequired[str]

class ModifyCacheSubnetGroupMessageTypeDef(TypedDict):
    CacheSubnetGroupName: str
    CacheSubnetGroupDescription: NotRequired[str]
    SubnetIds: NotRequired[Sequence[str]]

class ModifyGlobalReplicationGroupMessageTypeDef(TypedDict):
    GlobalReplicationGroupId: str
    ApplyImmediately: bool
    CacheNodeType: NotRequired[str]
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    CacheParameterGroupName: NotRequired[str]
    GlobalReplicationGroupDescription: NotRequired[str]
    AutomaticFailoverEnabled: NotRequired[bool]

class ReshardingConfigurationTypeDef(TypedDict):
    NodeGroupId: NotRequired[str]
    PreferredAvailabilityZones: NotRequired[Sequence[str]]

class ModifyUserGroupMessageTypeDef(TypedDict):
    UserGroupId: str
    UserIdsToAdd: NotRequired[Sequence[str]]
    UserIdsToRemove: NotRequired[Sequence[str]]
    Engine: NotRequired[str]

class NodeGroupConfigurationOutputTypeDef(TypedDict):
    NodeGroupId: NotRequired[str]
    Slots: NotRequired[str]
    ReplicaCount: NotRequired[int]
    PrimaryAvailabilityZone: NotRequired[str]
    ReplicaAvailabilityZones: NotRequired[List[str]]
    PrimaryOutpostArn: NotRequired[str]
    ReplicaOutpostArns: NotRequired[List[str]]

class NodeGroupConfigurationTypeDef(TypedDict):
    NodeGroupId: NotRequired[str]
    Slots: NotRequired[str]
    ReplicaCount: NotRequired[int]
    PrimaryAvailabilityZone: NotRequired[str]
    ReplicaAvailabilityZones: NotRequired[Sequence[str]]
    PrimaryOutpostArn: NotRequired[str]
    ReplicaOutpostArns: NotRequired[Sequence[str]]

class NodeGroupMemberUpdateStatusTypeDef(TypedDict):
    CacheClusterId: NotRequired[str]
    CacheNodeId: NotRequired[str]
    NodeUpdateStatus: NotRequired[NodeUpdateStatusType]
    NodeDeletionDate: NotRequired[datetime]
    NodeUpdateStartDate: NotRequired[datetime]
    NodeUpdateEndDate: NotRequired[datetime]
    NodeUpdateInitiatedBy: NotRequired[NodeUpdateInitiatedByType]
    NodeUpdateInitiatedDate: NotRequired[datetime]
    NodeUpdateStatusModifiedDate: NotRequired[datetime]

class ProcessedUpdateActionTypeDef(TypedDict):
    ReplicationGroupId: NotRequired[str]
    CacheClusterId: NotRequired[str]
    ServiceUpdateName: NotRequired[str]
    UpdateActionStatus: NotRequired[UpdateActionStatusType]

class RebalanceSlotsInGlobalReplicationGroupMessageTypeDef(TypedDict):
    GlobalReplicationGroupId: str
    ApplyImmediately: bool

class RebootCacheClusterMessageTypeDef(TypedDict):
    CacheClusterId: str
    CacheNodeIdsToReboot: Sequence[str]

class RecurringChargeTypeDef(TypedDict):
    RecurringChargeAmount: NotRequired[float]
    RecurringChargeFrequency: NotRequired[str]

class RemoveTagsFromResourceMessageTypeDef(TypedDict):
    ResourceName: str
    TagKeys: Sequence[str]

class UserGroupsUpdateStatusTypeDef(TypedDict):
    UserGroupIdsToAdd: NotRequired[List[str]]
    UserGroupIdsToRemove: NotRequired[List[str]]

class SlotMigrationTypeDef(TypedDict):
    ProgressPercentage: NotRequired[float]

class RevokeCacheSecurityGroupIngressMessageTypeDef(TypedDict):
    CacheSecurityGroupName: str
    EC2SecurityGroupName: str
    EC2SecurityGroupOwnerId: str

class ServerlessCacheConfigurationTypeDef(TypedDict):
    ServerlessCacheName: NotRequired[str]
    Engine: NotRequired[str]
    MajorEngineVersion: NotRequired[str]

class ServiceUpdateTypeDef(TypedDict):
    ServiceUpdateName: NotRequired[str]
    ServiceUpdateReleaseDate: NotRequired[datetime]
    ServiceUpdateEndDate: NotRequired[datetime]
    ServiceUpdateSeverity: NotRequired[ServiceUpdateSeverityType]
    ServiceUpdateRecommendedApplyByDate: NotRequired[datetime]
    ServiceUpdateStatus: NotRequired[ServiceUpdateStatusType]
    ServiceUpdateDescription: NotRequired[str]
    ServiceUpdateType: NotRequired[Literal["security-update"]]
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    AutoUpdateAfterRecommendedApplyByDate: NotRequired[bool]
    EstimatedUpdateTime: NotRequired[str]

class SubnetOutpostTypeDef(TypedDict):
    SubnetOutpostArn: NotRequired[str]

class TestFailoverMessageTypeDef(TypedDict):
    ReplicationGroupId: str
    NodeGroupId: str

class UnprocessedUpdateActionTypeDef(TypedDict):
    ReplicationGroupId: NotRequired[str]
    CacheClusterId: NotRequired[str]
    ServiceUpdateName: NotRequired[str]
    ErrorType: NotRequired[str]
    ErrorMessage: NotRequired[str]

class UserGroupPendingChangesTypeDef(TypedDict):
    UserIdsToRemove: NotRequired[List[str]]
    UserIdsToAdd: NotRequired[List[str]]

class AddTagsToResourceMessageTypeDef(TypedDict):
    ResourceName: str
    Tags: Sequence[TagTypeDef]

class CopyServerlessCacheSnapshotRequestTypeDef(TypedDict):
    SourceServerlessCacheSnapshotName: str
    TargetServerlessCacheSnapshotName: str
    KmsKeyId: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CopySnapshotMessageTypeDef(TypedDict):
    SourceSnapshotName: str
    TargetSnapshotName: str
    TargetBucket: NotRequired[str]
    KmsKeyId: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateCacheParameterGroupMessageTypeDef(TypedDict):
    CacheParameterGroupName: str
    CacheParameterGroupFamily: str
    Description: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateCacheSecurityGroupMessageTypeDef(TypedDict):
    CacheSecurityGroupName: str
    Description: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateCacheSubnetGroupMessageTypeDef(TypedDict):
    CacheSubnetGroupName: str
    CacheSubnetGroupDescription: str
    SubnetIds: Sequence[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateServerlessCacheSnapshotRequestTypeDef(TypedDict):
    ServerlessCacheSnapshotName: str
    ServerlessCacheName: str
    KmsKeyId: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateSnapshotMessageTypeDef(TypedDict):
    SnapshotName: str
    ReplicationGroupId: NotRequired[str]
    CacheClusterId: NotRequired[str]
    KmsKeyId: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateUserGroupMessageTypeDef(TypedDict):
    UserGroupId: str
    Engine: str
    UserIds: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]

class PurchaseReservedCacheNodesOfferingMessageTypeDef(TypedDict):
    ReservedCacheNodesOfferingId: str
    ReservedCacheNodeId: NotRequired[str]
    CacheNodeCount: NotRequired[int]
    Tags: NotRequired[Sequence[TagTypeDef]]

class AllowedNodeTypeModificationsMessageTypeDef(TypedDict):
    ScaleUpModifications: List[str]
    ScaleDownModifications: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CacheParameterGroupNameMessageTypeDef(TypedDict):
    CacheParameterGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class TagListMessageTypeDef(TypedDict):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserMessageTypeDef(TypedDict):
    UserId: str
    UserName: str
    Engine: str
    AccessString: str
    Passwords: NotRequired[Sequence[str]]
    NoPasswordRequired: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]
    AuthenticationMode: NotRequired[AuthenticationModeTypeDef]

class ModifyUserMessageTypeDef(TypedDict):
    UserId: str
    AccessString: NotRequired[str]
    AppendAccessString: NotRequired[str]
    Passwords: NotRequired[Sequence[str]]
    NoPasswordRequired: NotRequired[bool]
    AuthenticationMode: NotRequired[AuthenticationModeTypeDef]
    Engine: NotRequired[str]

class UserResponseTypeDef(TypedDict):
    UserId: str
    UserName: str
    Status: str
    Engine: str
    MinimumEngineVersion: str
    AccessString: str
    UserGroupIds: List[str]
    Authentication: AuthenticationTypeDef
    ARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UserTypeDef(TypedDict):
    UserId: NotRequired[str]
    UserName: NotRequired[str]
    Status: NotRequired[str]
    Engine: NotRequired[str]
    MinimumEngineVersion: NotRequired[str]
    AccessString: NotRequired[str]
    UserGroupIds: NotRequired[List[str]]
    Authentication: NotRequired[AuthenticationTypeDef]
    ARN: NotRequired[str]

class CacheNodeTypeDef(TypedDict):
    CacheNodeId: NotRequired[str]
    CacheNodeStatus: NotRequired[str]
    CacheNodeCreateTime: NotRequired[datetime]
    Endpoint: NotRequired[EndpointTypeDef]
    ParameterGroupStatus: NotRequired[str]
    SourceCacheNodeId: NotRequired[str]
    CustomerAvailabilityZone: NotRequired[str]
    CustomerOutpostArn: NotRequired[str]

class NodeGroupMemberTypeDef(TypedDict):
    CacheClusterId: NotRequired[str]
    CacheNodeId: NotRequired[str]
    ReadEndpoint: NotRequired[EndpointTypeDef]
    PreferredAvailabilityZone: NotRequired[str]
    PreferredOutpostArn: NotRequired[str]
    CurrentRole: NotRequired[str]

class CacheEngineVersionMessageTypeDef(TypedDict):
    Marker: str
    CacheEngineVersions: List[CacheEngineVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CacheNodeTypeSpecificParameterTypeDef(TypedDict):
    ParameterName: NotRequired[str]
    Description: NotRequired[str]
    Source: NotRequired[str]
    DataType: NotRequired[str]
    AllowedValues: NotRequired[str]
    IsModifiable: NotRequired[bool]
    MinimumEngineVersion: NotRequired[str]
    CacheNodeTypeSpecificValues: NotRequired[List[CacheNodeTypeSpecificValueTypeDef]]
    ChangeType: NotRequired[ChangeTypeType]

class CacheParameterGroupsMessageTypeDef(TypedDict):
    Marker: str
    CacheParameterGroups: List[CacheParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCacheParameterGroupResultTypeDef(TypedDict):
    CacheParameterGroup: CacheParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CacheSecurityGroupTypeDef(TypedDict):
    OwnerId: NotRequired[str]
    CacheSecurityGroupName: NotRequired[str]
    Description: NotRequired[str]
    EC2SecurityGroups: NotRequired[List[EC2SecurityGroupTypeDef]]
    ARN: NotRequired[str]

class CacheUsageLimitsTypeDef(TypedDict):
    DataStorage: NotRequired[DataStorageTypeDef]
    ECPUPerSecond: NotRequired[ECPUPerSecondTypeDef]

class DecreaseReplicaCountMessageTypeDef(TypedDict):
    ReplicationGroupId: str
    ApplyImmediately: bool
    NewReplicaCount: NotRequired[int]
    ReplicaConfiguration: NotRequired[Sequence[ConfigureShardTypeDef]]
    ReplicasToRemove: NotRequired[Sequence[str]]

class IncreaseReplicaCountMessageTypeDef(TypedDict):
    ReplicationGroupId: str
    ApplyImmediately: bool
    NewReplicaCount: NotRequired[int]
    ReplicaConfiguration: NotRequired[Sequence[ConfigureShardTypeDef]]

class StartMigrationMessageTypeDef(TypedDict):
    ReplicationGroupId: str
    CustomerNodeEndpointList: Sequence[CustomerNodeEndpointTypeDef]

class TestMigrationMessageTypeDef(TypedDict):
    ReplicationGroupId: str
    CustomerNodeEndpointList: Sequence[CustomerNodeEndpointTypeDef]

class DescribeCacheClustersMessagePaginateTypeDef(TypedDict):
    CacheClusterId: NotRequired[str]
    ShowCacheNodeInfo: NotRequired[bool]
    ShowCacheClustersNotInReplicationGroups: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeCacheEngineVersionsMessagePaginateTypeDef(TypedDict):
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    CacheParameterGroupFamily: NotRequired[str]
    DefaultOnly: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeCacheParameterGroupsMessagePaginateTypeDef(TypedDict):
    CacheParameterGroupName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeCacheParametersMessagePaginateTypeDef(TypedDict):
    CacheParameterGroupName: str
    Source: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeCacheSecurityGroupsMessagePaginateTypeDef(TypedDict):
    CacheSecurityGroupName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeCacheSubnetGroupsMessagePaginateTypeDef(TypedDict):
    CacheSubnetGroupName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEngineDefaultParametersMessagePaginateTypeDef(TypedDict):
    CacheParameterGroupFamily: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeGlobalReplicationGroupsMessagePaginateTypeDef(TypedDict):
    GlobalReplicationGroupId: NotRequired[str]
    ShowMemberInfo: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeReplicationGroupsMessagePaginateTypeDef(TypedDict):
    ReplicationGroupId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeReservedCacheNodesMessagePaginateTypeDef(TypedDict):
    ReservedCacheNodeId: NotRequired[str]
    ReservedCacheNodesOfferingId: NotRequired[str]
    CacheNodeType: NotRequired[str]
    Duration: NotRequired[str]
    ProductDescription: NotRequired[str]
    OfferingType: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeReservedCacheNodesOfferingsMessagePaginateTypeDef(TypedDict):
    ReservedCacheNodesOfferingId: NotRequired[str]
    CacheNodeType: NotRequired[str]
    Duration: NotRequired[str]
    ProductDescription: NotRequired[str]
    OfferingType: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeServerlessCacheSnapshotsRequestPaginateTypeDef(TypedDict):
    ServerlessCacheName: NotRequired[str]
    ServerlessCacheSnapshotName: NotRequired[str]
    SnapshotType: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeServerlessCachesRequestPaginateTypeDef(TypedDict):
    ServerlessCacheName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeServiceUpdatesMessagePaginateTypeDef(TypedDict):
    ServiceUpdateName: NotRequired[str]
    ServiceUpdateStatus: NotRequired[Sequence[ServiceUpdateStatusType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeSnapshotsMessagePaginateTypeDef(TypedDict):
    ReplicationGroupId: NotRequired[str]
    CacheClusterId: NotRequired[str]
    SnapshotName: NotRequired[str]
    SnapshotSource: NotRequired[str]
    ShowNodeGroupConfig: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeUserGroupsMessagePaginateTypeDef(TypedDict):
    UserGroupId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeCacheClustersMessageWaitExtraTypeDef(TypedDict):
    CacheClusterId: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    ShowCacheNodeInfo: NotRequired[bool]
    ShowCacheClustersNotInReplicationGroups: NotRequired[bool]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeCacheClustersMessageWaitTypeDef(TypedDict):
    CacheClusterId: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    ShowCacheNodeInfo: NotRequired[bool]
    ShowCacheClustersNotInReplicationGroups: NotRequired[bool]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeReplicationGroupsMessageWaitExtraTypeDef(TypedDict):
    ReplicationGroupId: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeReplicationGroupsMessageWaitTypeDef(TypedDict):
    ReplicationGroupId: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeEventsMessagePaginateTypeDef(TypedDict):
    SourceIdentifier: NotRequired[str]
    SourceType: NotRequired[SourceTypeType]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    Duration: NotRequired[int]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEventsMessageTypeDef(TypedDict):
    SourceIdentifier: NotRequired[str]
    SourceType: NotRequired[SourceTypeType]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    Duration: NotRequired[int]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class TimeRangeFilterTypeDef(TypedDict):
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]

class DescribeUsersMessagePaginateTypeDef(TypedDict):
    Engine: NotRequired[str]
    UserId: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeUsersMessageTypeDef(TypedDict):
    Engine: NotRequired[str]
    UserId: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DestinationDetailsTypeDef(TypedDict):
    CloudWatchLogsDetails: NotRequired[CloudWatchLogsDestinationDetailsTypeDef]
    KinesisFirehoseDetails: NotRequired[KinesisFirehoseDestinationDetailsTypeDef]

class EventsMessageTypeDef(TypedDict):
    Marker: str
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GlobalReplicationGroupTypeDef(TypedDict):
    GlobalReplicationGroupId: NotRequired[str]
    GlobalReplicationGroupDescription: NotRequired[str]
    Status: NotRequired[str]
    CacheNodeType: NotRequired[str]
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    Members: NotRequired[List[GlobalReplicationGroupMemberTypeDef]]
    ClusterEnabled: NotRequired[bool]
    GlobalNodeGroups: NotRequired[List[GlobalNodeGroupTypeDef]]
    AuthTokenEnabled: NotRequired[bool]
    TransitEncryptionEnabled: NotRequired[bool]
    AtRestEncryptionEnabled: NotRequired[bool]
    ARN: NotRequired[str]

class ModifyCacheParameterGroupMessageTypeDef(TypedDict):
    CacheParameterGroupName: str
    ParameterNameValues: Sequence[ParameterNameValueTypeDef]

class ResetCacheParameterGroupMessageTypeDef(TypedDict):
    CacheParameterGroupName: str
    ResetAllParameters: NotRequired[bool]
    ParameterNameValues: NotRequired[Sequence[ParameterNameValueTypeDef]]

class ModifyReplicationGroupShardConfigurationMessageTypeDef(TypedDict):
    ReplicationGroupId: str
    NodeGroupCount: int
    ApplyImmediately: bool
    ReshardingConfiguration: NotRequired[Sequence[ReshardingConfigurationTypeDef]]
    NodeGroupsToRemove: NotRequired[Sequence[str]]
    NodeGroupsToRetain: NotRequired[Sequence[str]]

class RegionalConfigurationTypeDef(TypedDict):
    ReplicationGroupId: str
    ReplicationGroupRegion: str
    ReshardingConfiguration: Sequence[ReshardingConfigurationTypeDef]

class NodeSnapshotTypeDef(TypedDict):
    CacheClusterId: NotRequired[str]
    NodeGroupId: NotRequired[str]
    CacheNodeId: NotRequired[str]
    NodeGroupConfiguration: NotRequired[NodeGroupConfigurationOutputTypeDef]
    CacheSize: NotRequired[str]
    CacheNodeCreateTime: NotRequired[datetime]
    SnapshotCreateTime: NotRequired[datetime]

NodeGroupConfigurationUnionTypeDef = Union[
    NodeGroupConfigurationTypeDef, NodeGroupConfigurationOutputTypeDef
]

class NodeGroupUpdateStatusTypeDef(TypedDict):
    NodeGroupId: NotRequired[str]
    NodeGroupMemberUpdateStatus: NotRequired[List[NodeGroupMemberUpdateStatusTypeDef]]

class ReservedCacheNodeTypeDef(TypedDict):
    ReservedCacheNodeId: NotRequired[str]
    ReservedCacheNodesOfferingId: NotRequired[str]
    CacheNodeType: NotRequired[str]
    StartTime: NotRequired[datetime]
    Duration: NotRequired[int]
    FixedPrice: NotRequired[float]
    UsagePrice: NotRequired[float]
    CacheNodeCount: NotRequired[int]
    ProductDescription: NotRequired[str]
    OfferingType: NotRequired[str]
    State: NotRequired[str]
    RecurringCharges: NotRequired[List[RecurringChargeTypeDef]]
    ReservationARN: NotRequired[str]

class ReservedCacheNodesOfferingTypeDef(TypedDict):
    ReservedCacheNodesOfferingId: NotRequired[str]
    CacheNodeType: NotRequired[str]
    Duration: NotRequired[int]
    FixedPrice: NotRequired[float]
    UsagePrice: NotRequired[float]
    ProductDescription: NotRequired[str]
    OfferingType: NotRequired[str]
    RecurringCharges: NotRequired[List[RecurringChargeTypeDef]]

class ReshardingStatusTypeDef(TypedDict):
    SlotMigration: NotRequired[SlotMigrationTypeDef]

class ServerlessCacheSnapshotTypeDef(TypedDict):
    ServerlessCacheSnapshotName: NotRequired[str]
    ARN: NotRequired[str]
    KmsKeyId: NotRequired[str]
    SnapshotType: NotRequired[str]
    Status: NotRequired[str]
    CreateTime: NotRequired[datetime]
    ExpiryTime: NotRequired[datetime]
    BytesUsedForCache: NotRequired[str]
    ServerlessCacheConfiguration: NotRequired[ServerlessCacheConfigurationTypeDef]

class ServiceUpdatesMessageTypeDef(TypedDict):
    Marker: str
    ServiceUpdates: List[ServiceUpdateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SubnetTypeDef(TypedDict):
    SubnetIdentifier: NotRequired[str]
    SubnetAvailabilityZone: NotRequired[AvailabilityZoneTypeDef]
    SubnetOutpost: NotRequired[SubnetOutpostTypeDef]
    SupportedNetworkTypes: NotRequired[List[NetworkTypeType]]

class UpdateActionResultsMessageTypeDef(TypedDict):
    ProcessedUpdateActions: List[ProcessedUpdateActionTypeDef]
    UnprocessedUpdateActions: List[UnprocessedUpdateActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UserGroupResponseTypeDef(TypedDict):
    UserGroupId: str
    Status: str
    Engine: str
    UserIds: List[str]
    MinimumEngineVersion: str
    PendingChanges: UserGroupPendingChangesTypeDef
    ReplicationGroups: List[str]
    ServerlessCaches: List[str]
    ARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UserGroupTypeDef(TypedDict):
    UserGroupId: NotRequired[str]
    Status: NotRequired[str]
    Engine: NotRequired[str]
    UserIds: NotRequired[List[str]]
    MinimumEngineVersion: NotRequired[str]
    PendingChanges: NotRequired[UserGroupPendingChangesTypeDef]
    ReplicationGroups: NotRequired[List[str]]
    ServerlessCaches: NotRequired[List[str]]
    ARN: NotRequired[str]

class DescribeUsersResultTypeDef(TypedDict):
    Users: List[UserTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class NodeGroupTypeDef(TypedDict):
    NodeGroupId: NotRequired[str]
    Status: NotRequired[str]
    PrimaryEndpoint: NotRequired[EndpointTypeDef]
    ReaderEndpoint: NotRequired[EndpointTypeDef]
    Slots: NotRequired[str]
    NodeGroupMembers: NotRequired[List[NodeGroupMemberTypeDef]]

class CacheParameterGroupDetailsTypeDef(TypedDict):
    Marker: str
    Parameters: List[ParameterTypeDef]
    CacheNodeTypeSpecificParameters: List[CacheNodeTypeSpecificParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EngineDefaultsTypeDef(TypedDict):
    CacheParameterGroupFamily: NotRequired[str]
    Marker: NotRequired[str]
    Parameters: NotRequired[List[ParameterTypeDef]]
    CacheNodeTypeSpecificParameters: NotRequired[List[CacheNodeTypeSpecificParameterTypeDef]]

class AuthorizeCacheSecurityGroupIngressResultTypeDef(TypedDict):
    CacheSecurityGroup: CacheSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CacheSecurityGroupMessageTypeDef(TypedDict):
    Marker: str
    CacheSecurityGroups: List[CacheSecurityGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCacheSecurityGroupResultTypeDef(TypedDict):
    CacheSecurityGroup: CacheSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeCacheSecurityGroupIngressResultTypeDef(TypedDict):
    CacheSecurityGroup: CacheSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServerlessCacheRequestTypeDef(TypedDict):
    ServerlessCacheName: str
    Engine: str
    Description: NotRequired[str]
    MajorEngineVersion: NotRequired[str]
    CacheUsageLimits: NotRequired[CacheUsageLimitsTypeDef]
    KmsKeyId: NotRequired[str]
    SecurityGroupIds: NotRequired[Sequence[str]]
    SnapshotArnsToRestore: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    UserGroupId: NotRequired[str]
    SubnetIds: NotRequired[Sequence[str]]
    SnapshotRetentionLimit: NotRequired[int]
    DailySnapshotTime: NotRequired[str]

class ModifyServerlessCacheRequestTypeDef(TypedDict):
    ServerlessCacheName: str
    Description: NotRequired[str]
    CacheUsageLimits: NotRequired[CacheUsageLimitsTypeDef]
    RemoveUserGroup: NotRequired[bool]
    UserGroupId: NotRequired[str]
    SecurityGroupIds: NotRequired[Sequence[str]]
    SnapshotRetentionLimit: NotRequired[int]
    DailySnapshotTime: NotRequired[str]
    Engine: NotRequired[str]
    MajorEngineVersion: NotRequired[str]

class ServerlessCacheTypeDef(TypedDict):
    ServerlessCacheName: NotRequired[str]
    Description: NotRequired[str]
    CreateTime: NotRequired[datetime]
    Status: NotRequired[str]
    Engine: NotRequired[str]
    MajorEngineVersion: NotRequired[str]
    FullEngineVersion: NotRequired[str]
    CacheUsageLimits: NotRequired[CacheUsageLimitsTypeDef]
    KmsKeyId: NotRequired[str]
    SecurityGroupIds: NotRequired[List[str]]
    Endpoint: NotRequired[EndpointTypeDef]
    ReaderEndpoint: NotRequired[EndpointTypeDef]
    ARN: NotRequired[str]
    UserGroupId: NotRequired[str]
    SubnetIds: NotRequired[List[str]]
    SnapshotRetentionLimit: NotRequired[int]
    DailySnapshotTime: NotRequired[str]

class DescribeUpdateActionsMessagePaginateTypeDef(TypedDict):
    ServiceUpdateName: NotRequired[str]
    ReplicationGroupIds: NotRequired[Sequence[str]]
    CacheClusterIds: NotRequired[Sequence[str]]
    Engine: NotRequired[str]
    ServiceUpdateStatus: NotRequired[Sequence[ServiceUpdateStatusType]]
    ServiceUpdateTimeRange: NotRequired[TimeRangeFilterTypeDef]
    UpdateActionStatus: NotRequired[Sequence[UpdateActionStatusType]]
    ShowNodeLevelUpdateStatus: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeUpdateActionsMessageTypeDef(TypedDict):
    ServiceUpdateName: NotRequired[str]
    ReplicationGroupIds: NotRequired[Sequence[str]]
    CacheClusterIds: NotRequired[Sequence[str]]
    Engine: NotRequired[str]
    ServiceUpdateStatus: NotRequired[Sequence[ServiceUpdateStatusType]]
    ServiceUpdateTimeRange: NotRequired[TimeRangeFilterTypeDef]
    UpdateActionStatus: NotRequired[Sequence[UpdateActionStatusType]]
    ShowNodeLevelUpdateStatus: NotRequired[bool]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class LogDeliveryConfigurationRequestTypeDef(TypedDict):
    LogType: NotRequired[LogTypeType]
    DestinationType: NotRequired[DestinationTypeType]
    DestinationDetails: NotRequired[DestinationDetailsTypeDef]
    LogFormat: NotRequired[LogFormatType]
    Enabled: NotRequired[bool]

class LogDeliveryConfigurationTypeDef(TypedDict):
    LogType: NotRequired[LogTypeType]
    DestinationType: NotRequired[DestinationTypeType]
    DestinationDetails: NotRequired[DestinationDetailsTypeDef]
    LogFormat: NotRequired[LogFormatType]
    Status: NotRequired[LogDeliveryConfigurationStatusType]
    Message: NotRequired[str]

class PendingLogDeliveryConfigurationTypeDef(TypedDict):
    LogType: NotRequired[LogTypeType]
    DestinationType: NotRequired[DestinationTypeType]
    DestinationDetails: NotRequired[DestinationDetailsTypeDef]
    LogFormat: NotRequired[LogFormatType]

class CreateGlobalReplicationGroupResultTypeDef(TypedDict):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef(TypedDict):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGlobalReplicationGroupResultTypeDef(TypedDict):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGlobalReplicationGroupsResultTypeDef(TypedDict):
    Marker: str
    GlobalReplicationGroups: List[GlobalReplicationGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateGlobalReplicationGroupResultTypeDef(TypedDict):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FailoverGlobalReplicationGroupResultTypeDef(TypedDict):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef(TypedDict):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyGlobalReplicationGroupResultTypeDef(TypedDict):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RebalanceSlotsInGlobalReplicationGroupResultTypeDef(TypedDict):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IncreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef(TypedDict):
    GlobalReplicationGroupId: str
    NodeGroupCount: int
    ApplyImmediately: bool
    RegionalConfigurations: NotRequired[Sequence[RegionalConfigurationTypeDef]]

class SnapshotTypeDef(TypedDict):
    SnapshotName: NotRequired[str]
    ReplicationGroupId: NotRequired[str]
    ReplicationGroupDescription: NotRequired[str]
    CacheClusterId: NotRequired[str]
    SnapshotStatus: NotRequired[str]
    SnapshotSource: NotRequired[str]
    CacheNodeType: NotRequired[str]
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    NumCacheNodes: NotRequired[int]
    PreferredAvailabilityZone: NotRequired[str]
    PreferredOutpostArn: NotRequired[str]
    CacheClusterCreateTime: NotRequired[datetime]
    PreferredMaintenanceWindow: NotRequired[str]
    TopicArn: NotRequired[str]
    Port: NotRequired[int]
    CacheParameterGroupName: NotRequired[str]
    CacheSubnetGroupName: NotRequired[str]
    VpcId: NotRequired[str]
    AutoMinorVersionUpgrade: NotRequired[bool]
    SnapshotRetentionLimit: NotRequired[int]
    SnapshotWindow: NotRequired[str]
    NumNodeGroups: NotRequired[int]
    AutomaticFailover: NotRequired[AutomaticFailoverStatusType]
    NodeSnapshots: NotRequired[List[NodeSnapshotTypeDef]]
    KmsKeyId: NotRequired[str]
    ARN: NotRequired[str]
    DataTiering: NotRequired[DataTieringStatusType]

class UpdateActionTypeDef(TypedDict):
    ReplicationGroupId: NotRequired[str]
    CacheClusterId: NotRequired[str]
    ServiceUpdateName: NotRequired[str]
    ServiceUpdateReleaseDate: NotRequired[datetime]
    ServiceUpdateSeverity: NotRequired[ServiceUpdateSeverityType]
    ServiceUpdateStatus: NotRequired[ServiceUpdateStatusType]
    ServiceUpdateRecommendedApplyByDate: NotRequired[datetime]
    ServiceUpdateType: NotRequired[Literal["security-update"]]
    UpdateActionAvailableDate: NotRequired[datetime]
    UpdateActionStatus: NotRequired[UpdateActionStatusType]
    NodesUpdated: NotRequired[str]
    UpdateActionStatusModifiedDate: NotRequired[datetime]
    SlaMet: NotRequired[SlaMetType]
    NodeGroupUpdateStatus: NotRequired[List[NodeGroupUpdateStatusTypeDef]]
    CacheNodeUpdateStatus: NotRequired[List[CacheNodeUpdateStatusTypeDef]]
    EstimatedUpdateTime: NotRequired[str]
    Engine: NotRequired[str]

class PurchaseReservedCacheNodesOfferingResultTypeDef(TypedDict):
    ReservedCacheNode: ReservedCacheNodeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReservedCacheNodeMessageTypeDef(TypedDict):
    Marker: str
    ReservedCacheNodes: List[ReservedCacheNodeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReservedCacheNodesOfferingMessageTypeDef(TypedDict):
    Marker: str
    ReservedCacheNodesOfferings: List[ReservedCacheNodesOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CopyServerlessCacheSnapshotResponseTypeDef(TypedDict):
    ServerlessCacheSnapshot: ServerlessCacheSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServerlessCacheSnapshotResponseTypeDef(TypedDict):
    ServerlessCacheSnapshot: ServerlessCacheSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServerlessCacheSnapshotResponseTypeDef(TypedDict):
    ServerlessCacheSnapshot: ServerlessCacheSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServerlessCacheSnapshotsResponseTypeDef(TypedDict):
    ServerlessCacheSnapshots: List[ServerlessCacheSnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ExportServerlessCacheSnapshotResponseTypeDef(TypedDict):
    ServerlessCacheSnapshot: ServerlessCacheSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CacheSubnetGroupTypeDef(TypedDict):
    CacheSubnetGroupName: NotRequired[str]
    CacheSubnetGroupDescription: NotRequired[str]
    VpcId: NotRequired[str]
    Subnets: NotRequired[List[SubnetTypeDef]]
    ARN: NotRequired[str]
    SupportedNetworkTypes: NotRequired[List[NetworkTypeType]]

class DescribeUserGroupsResultTypeDef(TypedDict):
    UserGroups: List[UserGroupTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEngineDefaultParametersResultTypeDef(TypedDict):
    EngineDefaults: EngineDefaultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServerlessCacheResponseTypeDef(TypedDict):
    ServerlessCache: ServerlessCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServerlessCacheResponseTypeDef(TypedDict):
    ServerlessCache: ServerlessCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServerlessCachesResponseTypeDef(TypedDict):
    ServerlessCaches: List[ServerlessCacheTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ModifyServerlessCacheResponseTypeDef(TypedDict):
    ServerlessCache: ServerlessCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCacheClusterMessageTypeDef(TypedDict):
    CacheClusterId: str
    ReplicationGroupId: NotRequired[str]
    AZMode: NotRequired[AZModeType]
    PreferredAvailabilityZone: NotRequired[str]
    PreferredAvailabilityZones: NotRequired[Sequence[str]]
    NumCacheNodes: NotRequired[int]
    CacheNodeType: NotRequired[str]
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    CacheParameterGroupName: NotRequired[str]
    CacheSubnetGroupName: NotRequired[str]
    CacheSecurityGroupNames: NotRequired[Sequence[str]]
    SecurityGroupIds: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    SnapshotArns: NotRequired[Sequence[str]]
    SnapshotName: NotRequired[str]
    PreferredMaintenanceWindow: NotRequired[str]
    Port: NotRequired[int]
    NotificationTopicArn: NotRequired[str]
    AutoMinorVersionUpgrade: NotRequired[bool]
    SnapshotRetentionLimit: NotRequired[int]
    SnapshotWindow: NotRequired[str]
    AuthToken: NotRequired[str]
    OutpostMode: NotRequired[OutpostModeType]
    PreferredOutpostArn: NotRequired[str]
    PreferredOutpostArns: NotRequired[Sequence[str]]
    LogDeliveryConfigurations: NotRequired[Sequence[LogDeliveryConfigurationRequestTypeDef]]
    TransitEncryptionEnabled: NotRequired[bool]
    NetworkType: NotRequired[NetworkTypeType]
    IpDiscovery: NotRequired[IpDiscoveryType]

class CreateReplicationGroupMessageTypeDef(TypedDict):
    ReplicationGroupId: str
    ReplicationGroupDescription: str
    GlobalReplicationGroupId: NotRequired[str]
    PrimaryClusterId: NotRequired[str]
    AutomaticFailoverEnabled: NotRequired[bool]
    MultiAZEnabled: NotRequired[bool]
    NumCacheClusters: NotRequired[int]
    PreferredCacheClusterAZs: NotRequired[Sequence[str]]
    NumNodeGroups: NotRequired[int]
    ReplicasPerNodeGroup: NotRequired[int]
    NodeGroupConfiguration: NotRequired[Sequence[NodeGroupConfigurationUnionTypeDef]]
    CacheNodeType: NotRequired[str]
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    CacheParameterGroupName: NotRequired[str]
    CacheSubnetGroupName: NotRequired[str]
    CacheSecurityGroupNames: NotRequired[Sequence[str]]
    SecurityGroupIds: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    SnapshotArns: NotRequired[Sequence[str]]
    SnapshotName: NotRequired[str]
    PreferredMaintenanceWindow: NotRequired[str]
    Port: NotRequired[int]
    NotificationTopicArn: NotRequired[str]
    AutoMinorVersionUpgrade: NotRequired[bool]
    SnapshotRetentionLimit: NotRequired[int]
    SnapshotWindow: NotRequired[str]
    AuthToken: NotRequired[str]
    TransitEncryptionEnabled: NotRequired[bool]
    AtRestEncryptionEnabled: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    UserGroupIds: NotRequired[Sequence[str]]
    LogDeliveryConfigurations: NotRequired[Sequence[LogDeliveryConfigurationRequestTypeDef]]
    DataTieringEnabled: NotRequired[bool]
    NetworkType: NotRequired[NetworkTypeType]
    IpDiscovery: NotRequired[IpDiscoveryType]
    TransitEncryptionMode: NotRequired[TransitEncryptionModeType]
    ClusterMode: NotRequired[ClusterModeType]
    ServerlessCacheSnapshotName: NotRequired[str]

class ModifyCacheClusterMessageTypeDef(TypedDict):
    CacheClusterId: str
    NumCacheNodes: NotRequired[int]
    CacheNodeIdsToRemove: NotRequired[Sequence[str]]
    AZMode: NotRequired[AZModeType]
    NewAvailabilityZones: NotRequired[Sequence[str]]
    CacheSecurityGroupNames: NotRequired[Sequence[str]]
    SecurityGroupIds: NotRequired[Sequence[str]]
    PreferredMaintenanceWindow: NotRequired[str]
    NotificationTopicArn: NotRequired[str]
    CacheParameterGroupName: NotRequired[str]
    NotificationTopicStatus: NotRequired[str]
    ApplyImmediately: NotRequired[bool]
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    AutoMinorVersionUpgrade: NotRequired[bool]
    SnapshotRetentionLimit: NotRequired[int]
    SnapshotWindow: NotRequired[str]
    CacheNodeType: NotRequired[str]
    AuthToken: NotRequired[str]
    AuthTokenUpdateStrategy: NotRequired[AuthTokenUpdateStrategyTypeType]
    LogDeliveryConfigurations: NotRequired[Sequence[LogDeliveryConfigurationRequestTypeDef]]
    IpDiscovery: NotRequired[IpDiscoveryType]
    ScaleConfig: NotRequired[ScaleConfigTypeDef]

class ModifyReplicationGroupMessageTypeDef(TypedDict):
    ReplicationGroupId: str
    ReplicationGroupDescription: NotRequired[str]
    PrimaryClusterId: NotRequired[str]
    SnapshottingClusterId: NotRequired[str]
    AutomaticFailoverEnabled: NotRequired[bool]
    MultiAZEnabled: NotRequired[bool]
    NodeGroupId: NotRequired[str]
    CacheSecurityGroupNames: NotRequired[Sequence[str]]
    SecurityGroupIds: NotRequired[Sequence[str]]
    PreferredMaintenanceWindow: NotRequired[str]
    NotificationTopicArn: NotRequired[str]
    CacheParameterGroupName: NotRequired[str]
    NotificationTopicStatus: NotRequired[str]
    ApplyImmediately: NotRequired[bool]
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    AutoMinorVersionUpgrade: NotRequired[bool]
    SnapshotRetentionLimit: NotRequired[int]
    SnapshotWindow: NotRequired[str]
    CacheNodeType: NotRequired[str]
    AuthToken: NotRequired[str]
    AuthTokenUpdateStrategy: NotRequired[AuthTokenUpdateStrategyTypeType]
    UserGroupIdsToAdd: NotRequired[Sequence[str]]
    UserGroupIdsToRemove: NotRequired[Sequence[str]]
    RemoveUserGroups: NotRequired[bool]
    LogDeliveryConfigurations: NotRequired[Sequence[LogDeliveryConfigurationRequestTypeDef]]
    IpDiscovery: NotRequired[IpDiscoveryType]
    TransitEncryptionEnabled: NotRequired[bool]
    TransitEncryptionMode: NotRequired[TransitEncryptionModeType]
    ClusterMode: NotRequired[ClusterModeType]

class PendingModifiedValuesTypeDef(TypedDict):
    NumCacheNodes: NotRequired[int]
    CacheNodeIdsToRemove: NotRequired[List[str]]
    EngineVersion: NotRequired[str]
    CacheNodeType: NotRequired[str]
    AuthTokenStatus: NotRequired[AuthTokenUpdateStatusType]
    LogDeliveryConfigurations: NotRequired[List[PendingLogDeliveryConfigurationTypeDef]]
    TransitEncryptionEnabled: NotRequired[bool]
    TransitEncryptionMode: NotRequired[TransitEncryptionModeType]
    ScaleConfig: NotRequired[ScaleConfigTypeDef]

class ReplicationGroupPendingModifiedValuesTypeDef(TypedDict):
    PrimaryClusterId: NotRequired[str]
    AutomaticFailoverStatus: NotRequired[PendingAutomaticFailoverStatusType]
    Resharding: NotRequired[ReshardingStatusTypeDef]
    AuthTokenStatus: NotRequired[AuthTokenUpdateStatusType]
    UserGroups: NotRequired[UserGroupsUpdateStatusTypeDef]
    LogDeliveryConfigurations: NotRequired[List[PendingLogDeliveryConfigurationTypeDef]]
    TransitEncryptionEnabled: NotRequired[bool]
    TransitEncryptionMode: NotRequired[TransitEncryptionModeType]
    ClusterMode: NotRequired[ClusterModeType]

class CopySnapshotResultTypeDef(TypedDict):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSnapshotResultTypeDef(TypedDict):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSnapshotResultTypeDef(TypedDict):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSnapshotsListMessageTypeDef(TypedDict):
    Marker: str
    Snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateActionsMessageTypeDef(TypedDict):
    Marker: str
    UpdateActions: List[UpdateActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CacheSubnetGroupMessageTypeDef(TypedDict):
    Marker: str
    CacheSubnetGroups: List[CacheSubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCacheSubnetGroupResultTypeDef(TypedDict):
    CacheSubnetGroup: CacheSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyCacheSubnetGroupResultTypeDef(TypedDict):
    CacheSubnetGroup: CacheSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CacheClusterTypeDef(TypedDict):
    CacheClusterId: NotRequired[str]
    ConfigurationEndpoint: NotRequired[EndpointTypeDef]
    ClientDownloadLandingPage: NotRequired[str]
    CacheNodeType: NotRequired[str]
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    CacheClusterStatus: NotRequired[str]
    NumCacheNodes: NotRequired[int]
    PreferredAvailabilityZone: NotRequired[str]
    PreferredOutpostArn: NotRequired[str]
    CacheClusterCreateTime: NotRequired[datetime]
    PreferredMaintenanceWindow: NotRequired[str]
    PendingModifiedValues: NotRequired[PendingModifiedValuesTypeDef]
    NotificationConfiguration: NotRequired[NotificationConfigurationTypeDef]
    CacheSecurityGroups: NotRequired[List[CacheSecurityGroupMembershipTypeDef]]
    CacheParameterGroup: NotRequired[CacheParameterGroupStatusTypeDef]
    CacheSubnetGroupName: NotRequired[str]
    CacheNodes: NotRequired[List[CacheNodeTypeDef]]
    AutoMinorVersionUpgrade: NotRequired[bool]
    SecurityGroups: NotRequired[List[SecurityGroupMembershipTypeDef]]
    ReplicationGroupId: NotRequired[str]
    SnapshotRetentionLimit: NotRequired[int]
    SnapshotWindow: NotRequired[str]
    AuthTokenEnabled: NotRequired[bool]
    AuthTokenLastModifiedDate: NotRequired[datetime]
    TransitEncryptionEnabled: NotRequired[bool]
    AtRestEncryptionEnabled: NotRequired[bool]
    ARN: NotRequired[str]
    ReplicationGroupLogDeliveryEnabled: NotRequired[bool]
    LogDeliveryConfigurations: NotRequired[List[LogDeliveryConfigurationTypeDef]]
    NetworkType: NotRequired[NetworkTypeType]
    IpDiscovery: NotRequired[IpDiscoveryType]
    TransitEncryptionMode: NotRequired[TransitEncryptionModeType]

class ReplicationGroupTypeDef(TypedDict):
    ReplicationGroupId: NotRequired[str]
    Description: NotRequired[str]
    GlobalReplicationGroupInfo: NotRequired[GlobalReplicationGroupInfoTypeDef]
    Status: NotRequired[str]
    PendingModifiedValues: NotRequired[ReplicationGroupPendingModifiedValuesTypeDef]
    MemberClusters: NotRequired[List[str]]
    NodeGroups: NotRequired[List[NodeGroupTypeDef]]
    SnapshottingClusterId: NotRequired[str]
    AutomaticFailover: NotRequired[AutomaticFailoverStatusType]
    MultiAZ: NotRequired[MultiAZStatusType]
    ConfigurationEndpoint: NotRequired[EndpointTypeDef]
    SnapshotRetentionLimit: NotRequired[int]
    SnapshotWindow: NotRequired[str]
    ClusterEnabled: NotRequired[bool]
    CacheNodeType: NotRequired[str]
    AuthTokenEnabled: NotRequired[bool]
    AuthTokenLastModifiedDate: NotRequired[datetime]
    TransitEncryptionEnabled: NotRequired[bool]
    AtRestEncryptionEnabled: NotRequired[bool]
    MemberClustersOutpostArns: NotRequired[List[str]]
    KmsKeyId: NotRequired[str]
    ARN: NotRequired[str]
    UserGroupIds: NotRequired[List[str]]
    LogDeliveryConfigurations: NotRequired[List[LogDeliveryConfigurationTypeDef]]
    ReplicationGroupCreateTime: NotRequired[datetime]
    DataTiering: NotRequired[DataTieringStatusType]
    AutoMinorVersionUpgrade: NotRequired[bool]
    NetworkType: NotRequired[NetworkTypeType]
    IpDiscovery: NotRequired[IpDiscoveryType]
    TransitEncryptionMode: NotRequired[TransitEncryptionModeType]
    ClusterMode: NotRequired[ClusterModeType]
    Engine: NotRequired[str]

class CacheClusterMessageTypeDef(TypedDict):
    Marker: str
    CacheClusters: List[CacheClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCacheClusterResultTypeDef(TypedDict):
    CacheCluster: CacheClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCacheClusterResultTypeDef(TypedDict):
    CacheCluster: CacheClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyCacheClusterResultTypeDef(TypedDict):
    CacheCluster: CacheClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RebootCacheClusterResultTypeDef(TypedDict):
    CacheCluster: CacheClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CompleteMigrationResponseTypeDef(TypedDict):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReplicationGroupResultTypeDef(TypedDict):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DecreaseReplicaCountResultTypeDef(TypedDict):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteReplicationGroupResultTypeDef(TypedDict):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IncreaseReplicaCountResultTypeDef(TypedDict):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyReplicationGroupResultTypeDef(TypedDict):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyReplicationGroupShardConfigurationResultTypeDef(TypedDict):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicationGroupMessageTypeDef(TypedDict):
    Marker: str
    ReplicationGroups: List[ReplicationGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartMigrationResponseTypeDef(TypedDict):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TestFailoverResultTypeDef(TypedDict):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TestMigrationResponseTypeDef(TypedDict):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
