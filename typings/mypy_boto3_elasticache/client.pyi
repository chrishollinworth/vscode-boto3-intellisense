# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for elasticache service client

Usage::

    ```python
    import boto3
    from mypy_boto3_elasticache import ElastiCacheClient

    client: ElastiCacheClient = boto3.client("elasticache")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_elasticache.paginator import (
    DescribeCacheClustersPaginator,
    DescribeCacheEngineVersionsPaginator,
    DescribeCacheParameterGroupsPaginator,
    DescribeCacheParametersPaginator,
    DescribeCacheSecurityGroupsPaginator,
    DescribeCacheSubnetGroupsPaginator,
    DescribeEngineDefaultParametersPaginator,
    DescribeEventsPaginator,
    DescribeGlobalReplicationGroupsPaginator,
    DescribeReplicationGroupsPaginator,
    DescribeReservedCacheNodesOfferingsPaginator,
    DescribeReservedCacheNodesPaginator,
    DescribeServiceUpdatesPaginator,
    DescribeSnapshotsPaginator,
    DescribeUpdateActionsPaginator,
    DescribeUserGroupsPaginator,
    DescribeUsersPaginator,
)
from mypy_boto3_elasticache.type_defs import (
    AllowedNodeTypeModificationsMessageTypeDef,
    AuthorizeCacheSecurityGroupIngressResultTypeDef,
    CacheClusterMessageTypeDef,
    CacheEngineVersionMessageTypeDef,
    CacheParameterGroupDetailsTypeDef,
    CacheParameterGroupNameMessageTypeDef,
    CacheParameterGroupsMessageTypeDef,
    CacheSecurityGroupMessageTypeDef,
    CacheSubnetGroupMessageTypeDef,
    CompleteMigrationResponseTypeDef,
    ConfigureShardTypeDef,
    CopySnapshotResultTypeDef,
    CreateCacheClusterResultTypeDef,
    CreateCacheParameterGroupResultTypeDef,
    CreateCacheSecurityGroupResultTypeDef,
    CreateCacheSubnetGroupResultTypeDef,
    CreateGlobalReplicationGroupResultTypeDef,
    CreateReplicationGroupResultTypeDef,
    CreateSnapshotResultTypeDef,
    CustomerNodeEndpointTypeDef,
    DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef,
    DecreaseReplicaCountResultTypeDef,
    DeleteCacheClusterResultTypeDef,
    DeleteGlobalReplicationGroupResultTypeDef,
    DeleteReplicationGroupResultTypeDef,
    DeleteSnapshotResultTypeDef,
    DescribeEngineDefaultParametersResultTypeDef,
    DescribeGlobalReplicationGroupsResultTypeDef,
    DescribeSnapshotsListMessageTypeDef,
    DescribeUserGroupsResultTypeDef,
    DescribeUsersResultTypeDef,
    DisassociateGlobalReplicationGroupResultTypeDef,
    EventsMessageTypeDef,
    FailoverGlobalReplicationGroupResultTypeDef,
    FilterTypeDef,
    IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef,
    IncreaseReplicaCountResultTypeDef,
    ModifyCacheClusterResultTypeDef,
    ModifyCacheSubnetGroupResultTypeDef,
    ModifyGlobalReplicationGroupResultTypeDef,
    ModifyReplicationGroupResultTypeDef,
    ModifyReplicationGroupShardConfigurationResultTypeDef,
    NodeGroupConfigurationTypeDef,
    ParameterNameValueTypeDef,
    PurchaseReservedCacheNodesOfferingResultTypeDef,
    RebalanceSlotsInGlobalReplicationGroupResultTypeDef,
    RebootCacheClusterResultTypeDef,
    RegionalConfigurationTypeDef,
    ReplicationGroupMessageTypeDef,
    ReservedCacheNodeMessageTypeDef,
    ReservedCacheNodesOfferingMessageTypeDef,
    ReshardingConfigurationTypeDef,
    RevokeCacheSecurityGroupIngressResultTypeDef,
    ServiceUpdatesMessageTypeDef,
    StartMigrationResponseTypeDef,
    TagListMessageTypeDef,
    TagTypeDef,
    TestFailoverResultTypeDef,
    TimeRangeFilterTypeDef,
    UpdateActionResultsMessageTypeDef,
    UpdateActionsMessageTypeDef,
    UserGroupTypeDef,
    UserTypeDef,
)
from mypy_boto3_elasticache.waiter import (
    CacheClusterAvailableWaiter,
    CacheClusterDeletedWaiter,
    ReplicationGroupAvailableWaiter,
    ReplicationGroupDeletedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ElastiCacheClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    APICallRateForCustomerExceededFault: Type[BotocoreClientError]
    AuthorizationAlreadyExistsFault: Type[BotocoreClientError]
    AuthorizationNotFoundFault: Type[BotocoreClientError]
    CacheClusterAlreadyExistsFault: Type[BotocoreClientError]
    CacheClusterNotFoundFault: Type[BotocoreClientError]
    CacheParameterGroupAlreadyExistsFault: Type[BotocoreClientError]
    CacheParameterGroupNotFoundFault: Type[BotocoreClientError]
    CacheParameterGroupQuotaExceededFault: Type[BotocoreClientError]
    CacheSecurityGroupAlreadyExistsFault: Type[BotocoreClientError]
    CacheSecurityGroupNotFoundFault: Type[BotocoreClientError]
    CacheSecurityGroupQuotaExceededFault: Type[BotocoreClientError]
    CacheSubnetGroupAlreadyExistsFault: Type[BotocoreClientError]
    CacheSubnetGroupInUse: Type[BotocoreClientError]
    CacheSubnetGroupNotFoundFault: Type[BotocoreClientError]
    CacheSubnetGroupQuotaExceededFault: Type[BotocoreClientError]
    CacheSubnetQuotaExceededFault: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClusterQuotaForCustomerExceededFault: Type[BotocoreClientError]
    DefaultUserAssociatedToUserGroupFault: Type[BotocoreClientError]
    DefaultUserRequired: Type[BotocoreClientError]
    DuplicateUserNameFault: Type[BotocoreClientError]
    GlobalReplicationGroupAlreadyExistsFault: Type[BotocoreClientError]
    GlobalReplicationGroupNotFoundFault: Type[BotocoreClientError]
    InsufficientCacheClusterCapacityFault: Type[BotocoreClientError]
    InvalidARNFault: Type[BotocoreClientError]
    InvalidCacheClusterStateFault: Type[BotocoreClientError]
    InvalidCacheParameterGroupStateFault: Type[BotocoreClientError]
    InvalidCacheSecurityGroupStateFault: Type[BotocoreClientError]
    InvalidGlobalReplicationGroupStateFault: Type[BotocoreClientError]
    InvalidKMSKeyFault: Type[BotocoreClientError]
    InvalidParameterCombinationException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidReplicationGroupStateFault: Type[BotocoreClientError]
    InvalidSnapshotStateFault: Type[BotocoreClientError]
    InvalidSubnet: Type[BotocoreClientError]
    InvalidUserGroupStateFault: Type[BotocoreClientError]
    InvalidUserStateFault: Type[BotocoreClientError]
    InvalidVPCNetworkStateFault: Type[BotocoreClientError]
    NoOperationFault: Type[BotocoreClientError]
    NodeGroupNotFoundFault: Type[BotocoreClientError]
    NodeGroupsPerReplicationGroupQuotaExceededFault: Type[BotocoreClientError]
    NodeQuotaForClusterExceededFault: Type[BotocoreClientError]
    NodeQuotaForCustomerExceededFault: Type[BotocoreClientError]
    ReplicationGroupAlreadyExistsFault: Type[BotocoreClientError]
    ReplicationGroupAlreadyUnderMigrationFault: Type[BotocoreClientError]
    ReplicationGroupNotFoundFault: Type[BotocoreClientError]
    ReplicationGroupNotUnderMigrationFault: Type[BotocoreClientError]
    ReservedCacheNodeAlreadyExistsFault: Type[BotocoreClientError]
    ReservedCacheNodeNotFoundFault: Type[BotocoreClientError]
    ReservedCacheNodeQuotaExceededFault: Type[BotocoreClientError]
    ReservedCacheNodesOfferingNotFoundFault: Type[BotocoreClientError]
    ServiceLinkedRoleNotFoundFault: Type[BotocoreClientError]
    ServiceUpdateNotFoundFault: Type[BotocoreClientError]
    SnapshotAlreadyExistsFault: Type[BotocoreClientError]
    SnapshotFeatureNotSupportedFault: Type[BotocoreClientError]
    SnapshotNotFoundFault: Type[BotocoreClientError]
    SnapshotQuotaExceededFault: Type[BotocoreClientError]
    SubnetInUse: Type[BotocoreClientError]
    SubnetNotAllowedFault: Type[BotocoreClientError]
    TagNotFoundFault: Type[BotocoreClientError]
    TagQuotaPerResourceExceeded: Type[BotocoreClientError]
    TestFailoverNotAvailableFault: Type[BotocoreClientError]
    UserAlreadyExistsFault: Type[BotocoreClientError]
    UserGroupAlreadyExistsFault: Type[BotocoreClientError]
    UserGroupNotFoundFault: Type[BotocoreClientError]
    UserGroupQuotaExceededFault: Type[BotocoreClientError]
    UserNotFoundFault: Type[BotocoreClientError]
    UserQuotaExceededFault: Type[BotocoreClientError]


class ElastiCacheClient:
    """
    [ElastiCache.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_tags_to_resource(
        self, ResourceName: str, Tags: List["TagTypeDef"]
    ) -> TagListMessageTypeDef:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.add_tags_to_resource)
        """

    def authorize_cache_security_group_ingress(
        self, CacheSecurityGroupName: str, EC2SecurityGroupName: str, EC2SecurityGroupOwnerId: str
    ) -> AuthorizeCacheSecurityGroupIngressResultTypeDef:
        """
        [Client.authorize_cache_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.authorize_cache_security_group_ingress)
        """

    def batch_apply_update_action(
        self,
        ServiceUpdateName: str,
        ReplicationGroupIds: List[str] = None,
        CacheClusterIds: List[str] = None,
    ) -> UpdateActionResultsMessageTypeDef:
        """
        [Client.batch_apply_update_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.batch_apply_update_action)
        """

    def batch_stop_update_action(
        self,
        ServiceUpdateName: str,
        ReplicationGroupIds: List[str] = None,
        CacheClusterIds: List[str] = None,
    ) -> UpdateActionResultsMessageTypeDef:
        """
        [Client.batch_stop_update_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.batch_stop_update_action)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.can_paginate)
        """

    def complete_migration(
        self, ReplicationGroupId: str, Force: bool = None
    ) -> CompleteMigrationResponseTypeDef:
        """
        [Client.complete_migration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.complete_migration)
        """

    def copy_snapshot(
        self,
        SourceSnapshotName: str,
        TargetSnapshotName: str,
        TargetBucket: str = None,
        KmsKeyId: str = None,
    ) -> CopySnapshotResultTypeDef:
        """
        [Client.copy_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.copy_snapshot)
        """

    def create_cache_cluster(
        self,
        CacheClusterId: str,
        ReplicationGroupId: str = None,
        AZMode: Literal["single-az", "cross-az"] = None,
        PreferredAvailabilityZone: str = None,
        PreferredAvailabilityZones: List[str] = None,
        NumCacheNodes: int = None,
        CacheNodeType: str = None,
        Engine: str = None,
        EngineVersion: str = None,
        CacheParameterGroupName: str = None,
        CacheSubnetGroupName: str = None,
        CacheSecurityGroupNames: List[str] = None,
        SecurityGroupIds: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        SnapshotArns: List[str] = None,
        SnapshotName: str = None,
        PreferredMaintenanceWindow: str = None,
        Port: int = None,
        NotificationTopicArn: str = None,
        AutoMinorVersionUpgrade: bool = None,
        SnapshotRetentionLimit: int = None,
        SnapshotWindow: str = None,
        AuthToken: str = None,
        OutpostMode: Literal["single-outpost", "cross-outpost"] = None,
        PreferredOutpostArn: str = None,
        PreferredOutpostArns: List[str] = None,
    ) -> CreateCacheClusterResultTypeDef:
        """
        [Client.create_cache_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.create_cache_cluster)
        """

    def create_cache_parameter_group(
        self, CacheParameterGroupName: str, CacheParameterGroupFamily: str, Description: str
    ) -> CreateCacheParameterGroupResultTypeDef:
        """
        [Client.create_cache_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.create_cache_parameter_group)
        """

    def create_cache_security_group(
        self, CacheSecurityGroupName: str, Description: str
    ) -> CreateCacheSecurityGroupResultTypeDef:
        """
        [Client.create_cache_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.create_cache_security_group)
        """

    def create_cache_subnet_group(
        self, CacheSubnetGroupName: str, CacheSubnetGroupDescription: str, SubnetIds: List[str]
    ) -> CreateCacheSubnetGroupResultTypeDef:
        """
        [Client.create_cache_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.create_cache_subnet_group)
        """

    def create_global_replication_group(
        self,
        GlobalReplicationGroupIdSuffix: str,
        PrimaryReplicationGroupId: str,
        GlobalReplicationGroupDescription: str = None,
    ) -> CreateGlobalReplicationGroupResultTypeDef:
        """
        [Client.create_global_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.create_global_replication_group)
        """

    def create_replication_group(
        self,
        ReplicationGroupId: str,
        ReplicationGroupDescription: str,
        GlobalReplicationGroupId: str = None,
        PrimaryClusterId: str = None,
        AutomaticFailoverEnabled: bool = None,
        MultiAZEnabled: bool = None,
        NumCacheClusters: int = None,
        PreferredCacheClusterAZs: List[str] = None,
        NumNodeGroups: int = None,
        ReplicasPerNodeGroup: int = None,
        NodeGroupConfiguration: List["NodeGroupConfigurationTypeDef"] = None,
        CacheNodeType: str = None,
        Engine: str = None,
        EngineVersion: str = None,
        CacheParameterGroupName: str = None,
        CacheSubnetGroupName: str = None,
        CacheSecurityGroupNames: List[str] = None,
        SecurityGroupIds: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        SnapshotArns: List[str] = None,
        SnapshotName: str = None,
        PreferredMaintenanceWindow: str = None,
        Port: int = None,
        NotificationTopicArn: str = None,
        AutoMinorVersionUpgrade: bool = None,
        SnapshotRetentionLimit: int = None,
        SnapshotWindow: str = None,
        AuthToken: str = None,
        TransitEncryptionEnabled: bool = None,
        AtRestEncryptionEnabled: bool = None,
        KmsKeyId: str = None,
        UserGroupIds: List[str] = None,
    ) -> CreateReplicationGroupResultTypeDef:
        """
        [Client.create_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.create_replication_group)
        """

    def create_snapshot(
        self,
        SnapshotName: str,
        ReplicationGroupId: str = None,
        CacheClusterId: str = None,
        KmsKeyId: str = None,
    ) -> CreateSnapshotResultTypeDef:
        """
        [Client.create_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.create_snapshot)
        """

    def create_user(
        self,
        UserId: str,
        UserName: str,
        Engine: str,
        AccessString: str,
        Passwords: List[str] = None,
        NoPasswordRequired: bool = None,
    ) -> "UserTypeDef":
        """
        [Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.create_user)
        """

    def create_user_group(
        self, UserGroupId: str, Engine: str, UserIds: List[str] = None
    ) -> "UserGroupTypeDef":
        """
        [Client.create_user_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.create_user_group)
        """

    def decrease_node_groups_in_global_replication_group(
        self,
        GlobalReplicationGroupId: str,
        NodeGroupCount: int,
        ApplyImmediately: bool,
        GlobalNodeGroupsToRemove: List[str] = None,
        GlobalNodeGroupsToRetain: List[str] = None,
    ) -> DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef:
        """
        [Client.decrease_node_groups_in_global_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.decrease_node_groups_in_global_replication_group)
        """

    def decrease_replica_count(
        self,
        ReplicationGroupId: str,
        ApplyImmediately: bool,
        NewReplicaCount: int = None,
        ReplicaConfiguration: List[ConfigureShardTypeDef] = None,
        ReplicasToRemove: List[str] = None,
    ) -> DecreaseReplicaCountResultTypeDef:
        """
        [Client.decrease_replica_count documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.decrease_replica_count)
        """

    def delete_cache_cluster(
        self, CacheClusterId: str, FinalSnapshotIdentifier: str = None
    ) -> DeleteCacheClusterResultTypeDef:
        """
        [Client.delete_cache_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.delete_cache_cluster)
        """

    def delete_cache_parameter_group(self, CacheParameterGroupName: str) -> None:
        """
        [Client.delete_cache_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.delete_cache_parameter_group)
        """

    def delete_cache_security_group(self, CacheSecurityGroupName: str) -> None:
        """
        [Client.delete_cache_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.delete_cache_security_group)
        """

    def delete_cache_subnet_group(self, CacheSubnetGroupName: str) -> None:
        """
        [Client.delete_cache_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.delete_cache_subnet_group)
        """

    def delete_global_replication_group(
        self, GlobalReplicationGroupId: str, RetainPrimaryReplicationGroup: bool
    ) -> DeleteGlobalReplicationGroupResultTypeDef:
        """
        [Client.delete_global_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.delete_global_replication_group)
        """

    def delete_replication_group(
        self,
        ReplicationGroupId: str,
        RetainPrimaryCluster: bool = None,
        FinalSnapshotIdentifier: str = None,
    ) -> DeleteReplicationGroupResultTypeDef:
        """
        [Client.delete_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.delete_replication_group)
        """

    def delete_snapshot(self, SnapshotName: str) -> DeleteSnapshotResultTypeDef:
        """
        [Client.delete_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.delete_snapshot)
        """

    def delete_user(self, UserId: str) -> "UserTypeDef":
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.delete_user)
        """

    def delete_user_group(self, UserGroupId: str) -> "UserGroupTypeDef":
        """
        [Client.delete_user_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.delete_user_group)
        """

    def describe_cache_clusters(
        self,
        CacheClusterId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
    ) -> CacheClusterMessageTypeDef:
        """
        [Client.describe_cache_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.describe_cache_clusters)
        """

    def describe_cache_engine_versions(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        CacheParameterGroupFamily: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        DefaultOnly: bool = None,
    ) -> CacheEngineVersionMessageTypeDef:
        """
        [Client.describe_cache_engine_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.describe_cache_engine_versions)
        """

    def describe_cache_parameter_groups(
        self, CacheParameterGroupName: str = None, MaxRecords: int = None, Marker: str = None
    ) -> CacheParameterGroupsMessageTypeDef:
        """
        [Client.describe_cache_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.describe_cache_parameter_groups)
        """

    def describe_cache_parameters(
        self,
        CacheParameterGroupName: str,
        Source: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> CacheParameterGroupDetailsTypeDef:
        """
        [Client.describe_cache_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.describe_cache_parameters)
        """

    def describe_cache_security_groups(
        self, CacheSecurityGroupName: str = None, MaxRecords: int = None, Marker: str = None
    ) -> CacheSecurityGroupMessageTypeDef:
        """
        [Client.describe_cache_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.describe_cache_security_groups)
        """

    def describe_cache_subnet_groups(
        self, CacheSubnetGroupName: str = None, MaxRecords: int = None, Marker: str = None
    ) -> CacheSubnetGroupMessageTypeDef:
        """
        [Client.describe_cache_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.describe_cache_subnet_groups)
        """

    def describe_engine_default_parameters(
        self, CacheParameterGroupFamily: str, MaxRecords: int = None, Marker: str = None
    ) -> DescribeEngineDefaultParametersResultTypeDef:
        """
        [Client.describe_engine_default_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.describe_engine_default_parameters)
        """

    def describe_events(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal[
            "cache-cluster",
            "cache-parameter-group",
            "cache-security-group",
            "cache-subnet-group",
            "replication-group",
            "user",
            "user-group",
        ] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> EventsMessageTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.describe_events)
        """

    def describe_global_replication_groups(
        self,
        GlobalReplicationGroupId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowMemberInfo: bool = None,
    ) -> DescribeGlobalReplicationGroupsResultTypeDef:
        """
        [Client.describe_global_replication_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.describe_global_replication_groups)
        """

    def describe_replication_groups(
        self, ReplicationGroupId: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ReplicationGroupMessageTypeDef:
        """
        [Client.describe_replication_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.describe_replication_groups)
        """

    def describe_reserved_cache_nodes(
        self,
        ReservedCacheNodeId: str = None,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ReservedCacheNodeMessageTypeDef:
        """
        [Client.describe_reserved_cache_nodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.describe_reserved_cache_nodes)
        """

    def describe_reserved_cache_nodes_offerings(
        self,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ReservedCacheNodesOfferingMessageTypeDef:
        """
        [Client.describe_reserved_cache_nodes_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.describe_reserved_cache_nodes_offerings)
        """

    def describe_service_updates(
        self,
        ServiceUpdateName: str = None,
        ServiceUpdateStatus: List[Literal["available", "cancelled", "expired"]] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ServiceUpdatesMessageTypeDef:
        """
        [Client.describe_service_updates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.describe_service_updates)
        """

    def describe_snapshots(
        self,
        ReplicationGroupId: str = None,
        CacheClusterId: str = None,
        SnapshotName: str = None,
        SnapshotSource: str = None,
        Marker: str = None,
        MaxRecords: int = None,
        ShowNodeGroupConfig: bool = None,
    ) -> DescribeSnapshotsListMessageTypeDef:
        """
        [Client.describe_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.describe_snapshots)
        """

    def describe_update_actions(
        self,
        ServiceUpdateName: str = None,
        ReplicationGroupIds: List[str] = None,
        CacheClusterIds: List[str] = None,
        Engine: str = None,
        ServiceUpdateStatus: List[Literal["available", "cancelled", "expired"]] = None,
        ServiceUpdateTimeRange: TimeRangeFilterTypeDef = None,
        UpdateActionStatus: List[
            Literal[
                "not-applied",
                "waiting-to-start",
                "in-progress",
                "stopping",
                "stopped",
                "complete",
                "scheduling",
                "scheduled",
                "not-applicable",
            ]
        ] = None,
        ShowNodeLevelUpdateStatus: bool = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> UpdateActionsMessageTypeDef:
        """
        [Client.describe_update_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.describe_update_actions)
        """

    def describe_user_groups(
        self, UserGroupId: str = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeUserGroupsResultTypeDef:
        """
        [Client.describe_user_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.describe_user_groups)
        """

    def describe_users(
        self,
        Engine: str = None,
        UserId: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DescribeUsersResultTypeDef:
        """
        [Client.describe_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.describe_users)
        """

    def disassociate_global_replication_group(
        self, GlobalReplicationGroupId: str, ReplicationGroupId: str, ReplicationGroupRegion: str
    ) -> DisassociateGlobalReplicationGroupResultTypeDef:
        """
        [Client.disassociate_global_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.disassociate_global_replication_group)
        """

    def failover_global_replication_group(
        self, GlobalReplicationGroupId: str, PrimaryRegion: str, PrimaryReplicationGroupId: str
    ) -> FailoverGlobalReplicationGroupResultTypeDef:
        """
        [Client.failover_global_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.failover_global_replication_group)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.generate_presigned_url)
        """

    def increase_node_groups_in_global_replication_group(
        self,
        GlobalReplicationGroupId: str,
        NodeGroupCount: int,
        ApplyImmediately: bool,
        RegionalConfigurations: List[RegionalConfigurationTypeDef] = None,
    ) -> IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef:
        """
        [Client.increase_node_groups_in_global_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.increase_node_groups_in_global_replication_group)
        """

    def increase_replica_count(
        self,
        ReplicationGroupId: str,
        ApplyImmediately: bool,
        NewReplicaCount: int = None,
        ReplicaConfiguration: List[ConfigureShardTypeDef] = None,
    ) -> IncreaseReplicaCountResultTypeDef:
        """
        [Client.increase_replica_count documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.increase_replica_count)
        """

    def list_allowed_node_type_modifications(
        self, CacheClusterId: str = None, ReplicationGroupId: str = None
    ) -> AllowedNodeTypeModificationsMessageTypeDef:
        """
        [Client.list_allowed_node_type_modifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.list_allowed_node_type_modifications)
        """

    def list_tags_for_resource(self, ResourceName: str) -> TagListMessageTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.list_tags_for_resource)
        """

    def modify_cache_cluster(
        self,
        CacheClusterId: str,
        NumCacheNodes: int = None,
        CacheNodeIdsToRemove: List[str] = None,
        AZMode: Literal["single-az", "cross-az"] = None,
        NewAvailabilityZones: List[str] = None,
        CacheSecurityGroupNames: List[str] = None,
        SecurityGroupIds: List[str] = None,
        PreferredMaintenanceWindow: str = None,
        NotificationTopicArn: str = None,
        CacheParameterGroupName: str = None,
        NotificationTopicStatus: str = None,
        ApplyImmediately: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        SnapshotRetentionLimit: int = None,
        SnapshotWindow: str = None,
        CacheNodeType: str = None,
        AuthToken: str = None,
        AuthTokenUpdateStrategy: Literal["SET", "ROTATE", "DELETE"] = None,
    ) -> ModifyCacheClusterResultTypeDef:
        """
        [Client.modify_cache_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.modify_cache_cluster)
        """

    def modify_cache_parameter_group(
        self, CacheParameterGroupName: str, ParameterNameValues: List[ParameterNameValueTypeDef]
    ) -> CacheParameterGroupNameMessageTypeDef:
        """
        [Client.modify_cache_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.modify_cache_parameter_group)
        """

    def modify_cache_subnet_group(
        self,
        CacheSubnetGroupName: str,
        CacheSubnetGroupDescription: str = None,
        SubnetIds: List[str] = None,
    ) -> ModifyCacheSubnetGroupResultTypeDef:
        """
        [Client.modify_cache_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.modify_cache_subnet_group)
        """

    def modify_global_replication_group(
        self,
        GlobalReplicationGroupId: str,
        ApplyImmediately: bool,
        CacheNodeType: str = None,
        EngineVersion: str = None,
        GlobalReplicationGroupDescription: str = None,
        AutomaticFailoverEnabled: bool = None,
    ) -> ModifyGlobalReplicationGroupResultTypeDef:
        """
        [Client.modify_global_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.modify_global_replication_group)
        """

    def modify_replication_group(
        self,
        ReplicationGroupId: str,
        ReplicationGroupDescription: str = None,
        PrimaryClusterId: str = None,
        SnapshottingClusterId: str = None,
        AutomaticFailoverEnabled: bool = None,
        MultiAZEnabled: bool = None,
        NodeGroupId: str = None,
        CacheSecurityGroupNames: List[str] = None,
        SecurityGroupIds: List[str] = None,
        PreferredMaintenanceWindow: str = None,
        NotificationTopicArn: str = None,
        CacheParameterGroupName: str = None,
        NotificationTopicStatus: str = None,
        ApplyImmediately: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        SnapshotRetentionLimit: int = None,
        SnapshotWindow: str = None,
        CacheNodeType: str = None,
        AuthToken: str = None,
        AuthTokenUpdateStrategy: Literal["SET", "ROTATE", "DELETE"] = None,
        UserGroupIdsToAdd: List[str] = None,
        UserGroupIdsToRemove: List[str] = None,
        RemoveUserGroups: bool = None,
    ) -> ModifyReplicationGroupResultTypeDef:
        """
        [Client.modify_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.modify_replication_group)
        """

    def modify_replication_group_shard_configuration(
        self,
        ReplicationGroupId: str,
        NodeGroupCount: int,
        ApplyImmediately: bool,
        ReshardingConfiguration: List["ReshardingConfigurationTypeDef"] = None,
        NodeGroupsToRemove: List[str] = None,
        NodeGroupsToRetain: List[str] = None,
    ) -> ModifyReplicationGroupShardConfigurationResultTypeDef:
        """
        [Client.modify_replication_group_shard_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.modify_replication_group_shard_configuration)
        """

    def modify_user(
        self,
        UserId: str,
        AccessString: str = None,
        AppendAccessString: str = None,
        Passwords: List[str] = None,
        NoPasswordRequired: bool = None,
    ) -> "UserTypeDef":
        """
        [Client.modify_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.modify_user)
        """

    def modify_user_group(
        self, UserGroupId: str, UserIdsToAdd: List[str] = None, UserIdsToRemove: List[str] = None
    ) -> "UserGroupTypeDef":
        """
        [Client.modify_user_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.modify_user_group)
        """

    def purchase_reserved_cache_nodes_offering(
        self,
        ReservedCacheNodesOfferingId: str,
        ReservedCacheNodeId: str = None,
        CacheNodeCount: int = None,
    ) -> PurchaseReservedCacheNodesOfferingResultTypeDef:
        """
        [Client.purchase_reserved_cache_nodes_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.purchase_reserved_cache_nodes_offering)
        """

    def rebalance_slots_in_global_replication_group(
        self, GlobalReplicationGroupId: str, ApplyImmediately: bool
    ) -> RebalanceSlotsInGlobalReplicationGroupResultTypeDef:
        """
        [Client.rebalance_slots_in_global_replication_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.rebalance_slots_in_global_replication_group)
        """

    def reboot_cache_cluster(
        self, CacheClusterId: str, CacheNodeIdsToReboot: List[str]
    ) -> RebootCacheClusterResultTypeDef:
        """
        [Client.reboot_cache_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.reboot_cache_cluster)
        """

    def remove_tags_from_resource(
        self, ResourceName: str, TagKeys: List[str]
    ) -> TagListMessageTypeDef:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.remove_tags_from_resource)
        """

    def reset_cache_parameter_group(
        self,
        CacheParameterGroupName: str,
        ResetAllParameters: bool = None,
        ParameterNameValues: List[ParameterNameValueTypeDef] = None,
    ) -> CacheParameterGroupNameMessageTypeDef:
        """
        [Client.reset_cache_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.reset_cache_parameter_group)
        """

    def revoke_cache_security_group_ingress(
        self, CacheSecurityGroupName: str, EC2SecurityGroupName: str, EC2SecurityGroupOwnerId: str
    ) -> RevokeCacheSecurityGroupIngressResultTypeDef:
        """
        [Client.revoke_cache_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.revoke_cache_security_group_ingress)
        """

    def start_migration(
        self, ReplicationGroupId: str, CustomerNodeEndpointList: List[CustomerNodeEndpointTypeDef]
    ) -> StartMigrationResponseTypeDef:
        """
        [Client.start_migration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.start_migration)
        """

    def test_failover(self, ReplicationGroupId: str, NodeGroupId: str) -> TestFailoverResultTypeDef:
        """
        [Client.test_failover documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Client.test_failover)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cache_clusters"]
    ) -> DescribeCacheClustersPaginator:
        """
        [Paginator.DescribeCacheClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheClusters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cache_engine_versions"]
    ) -> DescribeCacheEngineVersionsPaginator:
        """
        [Paginator.DescribeCacheEngineVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheEngineVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cache_parameter_groups"]
    ) -> DescribeCacheParameterGroupsPaginator:
        """
        [Paginator.DescribeCacheParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameterGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cache_parameters"]
    ) -> DescribeCacheParametersPaginator:
        """
        [Paginator.DescribeCacheParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cache_security_groups"]
    ) -> DescribeCacheSecurityGroupsPaginator:
        """
        [Paginator.DescribeCacheSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSecurityGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cache_subnet_groups"]
    ) -> DescribeCacheSubnetGroupsPaginator:
        """
        [Paginator.DescribeCacheSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSubnetGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_engine_default_parameters"]
    ) -> DescribeEngineDefaultParametersPaginator:
        """
        [Paginator.DescribeEngineDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEngineDefaultParameters)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_global_replication_groups"]
    ) -> DescribeGlobalReplicationGroupsPaginator:
        """
        [Paginator.DescribeGlobalReplicationGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeGlobalReplicationGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_groups"]
    ) -> DescribeReplicationGroupsPaginator:
        """
        [Paginator.DescribeReplicationGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReplicationGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_cache_nodes"]
    ) -> DescribeReservedCacheNodesPaginator:
        """
        [Paginator.DescribeReservedCacheNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_cache_nodes_offerings"]
    ) -> DescribeReservedCacheNodesOfferingsPaginator:
        """
        [Paginator.DescribeReservedCacheNodesOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodesOfferings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_service_updates"]
    ) -> DescribeServiceUpdatesPaginator:
        """
        [Paginator.DescribeServiceUpdates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeServiceUpdates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshots"]
    ) -> DescribeSnapshotsPaginator:
        """
        [Paginator.DescribeSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeSnapshots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_update_actions"]
    ) -> DescribeUpdateActionsPaginator:
        """
        [Paginator.DescribeUpdateActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUpdateActions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_user_groups"]
    ) -> DescribeUserGroupsPaginator:
        """
        [Paginator.DescribeUserGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUserGroups)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_users"]) -> DescribeUsersPaginator:
        """
        [Paginator.DescribeUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUsers)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["cache_cluster_available"]
    ) -> CacheClusterAvailableWaiter:
        """
        [Waiter.CacheClusterAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Waiter.CacheClusterAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["cache_cluster_deleted"]
    ) -> CacheClusterDeletedWaiter:
        """
        [Waiter.CacheClusterDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Waiter.CacheClusterDeleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_group_available"]
    ) -> ReplicationGroupAvailableWaiter:
        """
        [Waiter.ReplicationGroupAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Waiter.ReplicationGroupAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_group_deleted"]
    ) -> ReplicationGroupDeletedWaiter:
        """
        [Waiter.ReplicationGroupDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Waiter.ReplicationGroupDeleted)
        """
