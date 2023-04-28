"""
Type annotations for elasticache service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_elasticache import ElastiCacheClient

    client: ElastiCacheClient = boto3.client("elasticache")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AuthTokenUpdateStrategyTypeType,
    AZModeType,
    IpDiscoveryType,
    NetworkTypeType,
    OutpostModeType,
    ServiceUpdateStatusType,
    SourceTypeType,
    TransitEncryptionModeType,
    UpdateActionStatusType,
)
from .paginator import (
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
from .type_defs import (
    AllowedNodeTypeModificationsMessageTypeDef,
    AuthenticationModeTypeDef,
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
    LogDeliveryConfigurationRequestTypeDef,
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
    UserGroupResponseMetadataTypeDef,
    UserResponseMetadataTypeDef,
)
from .waiter import (
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

class ElastiCacheClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ElastiCacheClient exceptions.
        """
    def add_tags_to_resource(
        self, *, ResourceName: str, Tags: List["TagTypeDef"]
    ) -> TagListMessageTypeDef:
        """
        A tag is a key-value pair where the key and value are case-sensitive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.add_tags_to_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#add_tags_to_resource)
        """
    def authorize_cache_security_group_ingress(
        self,
        *,
        CacheSecurityGroupName: str,
        EC2SecurityGroupName: str,
        EC2SecurityGroupOwnerId: str
    ) -> AuthorizeCacheSecurityGroupIngressResultTypeDef:
        """
        Allows network ingress to a cache security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.authorize_cache_security_group_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#authorize_cache_security_group_ingress)
        """
    def batch_apply_update_action(
        self,
        *,
        ServiceUpdateName: str,
        ReplicationGroupIds: List[str] = None,
        CacheClusterIds: List[str] = None
    ) -> UpdateActionResultsMessageTypeDef:
        """
        Apply the service update.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.batch_apply_update_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#batch_apply_update_action)
        """
    def batch_stop_update_action(
        self,
        *,
        ServiceUpdateName: str,
        ReplicationGroupIds: List[str] = None,
        CacheClusterIds: List[str] = None
    ) -> UpdateActionResultsMessageTypeDef:
        """
        Stop the service update.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.batch_stop_update_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#batch_stop_update_action)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#close)
        """
    def complete_migration(
        self, *, ReplicationGroupId: str, Force: bool = None
    ) -> CompleteMigrationResponseTypeDef:
        """
        Complete the migration of data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.complete_migration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#complete_migration)
        """
    def copy_snapshot(
        self,
        *,
        SourceSnapshotName: str,
        TargetSnapshotName: str,
        TargetBucket: str = None,
        KmsKeyId: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CopySnapshotResultTypeDef:
        """
        Makes a copy of an existing snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.copy_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#copy_snapshot)
        """
    def create_cache_cluster(
        self,
        *,
        CacheClusterId: str,
        ReplicationGroupId: str = None,
        AZMode: AZModeType = None,
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
        OutpostMode: OutpostModeType = None,
        PreferredOutpostArn: str = None,
        PreferredOutpostArns: List[str] = None,
        LogDeliveryConfigurations: List["LogDeliveryConfigurationRequestTypeDef"] = None,
        TransitEncryptionEnabled: bool = None,
        NetworkType: NetworkTypeType = None,
        IpDiscovery: IpDiscoveryType = None
    ) -> CreateCacheClusterResultTypeDef:
        """
        Creates a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.create_cache_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#create_cache_cluster)
        """
    def create_cache_parameter_group(
        self,
        *,
        CacheParameterGroupName: str,
        CacheParameterGroupFamily: str,
        Description: str,
        Tags: List["TagTypeDef"] = None
    ) -> CreateCacheParameterGroupResultTypeDef:
        """
        Creates a new Amazon ElastiCache cache parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.create_cache_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#create_cache_parameter_group)
        """
    def create_cache_security_group(
        self, *, CacheSecurityGroupName: str, Description: str, Tags: List["TagTypeDef"] = None
    ) -> CreateCacheSecurityGroupResultTypeDef:
        """
        Creates a new cache security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.create_cache_security_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#create_cache_security_group)
        """
    def create_cache_subnet_group(
        self,
        *,
        CacheSubnetGroupName: str,
        CacheSubnetGroupDescription: str,
        SubnetIds: List[str],
        Tags: List["TagTypeDef"] = None
    ) -> CreateCacheSubnetGroupResultTypeDef:
        """
        Creates a new cache subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.create_cache_subnet_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#create_cache_subnet_group)
        """
    def create_global_replication_group(
        self,
        *,
        GlobalReplicationGroupIdSuffix: str,
        PrimaryReplicationGroupId: str,
        GlobalReplicationGroupDescription: str = None
    ) -> CreateGlobalReplicationGroupResultTypeDef:
        """
        Global Datastore for Redis offers fully managed, fast, reliable and secure
        cross-region replication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.create_global_replication_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#create_global_replication_group)
        """
    def create_replication_group(
        self,
        *,
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
        LogDeliveryConfigurations: List["LogDeliveryConfigurationRequestTypeDef"] = None,
        DataTieringEnabled: bool = None,
        NetworkType: NetworkTypeType = None,
        IpDiscovery: IpDiscoveryType = None,
        TransitEncryptionMode: TransitEncryptionModeType = None
    ) -> CreateReplicationGroupResultTypeDef:
        """
        Creates a Redis (cluster mode disabled) or a Redis (cluster mode enabled)
        replication group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.create_replication_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#create_replication_group)
        """
    def create_snapshot(
        self,
        *,
        SnapshotName: str,
        ReplicationGroupId: str = None,
        CacheClusterId: str = None,
        KmsKeyId: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateSnapshotResultTypeDef:
        """
        Creates a copy of an entire cluster or replication group at a specific moment in
        time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.create_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#create_snapshot)
        """
    def create_user(
        self,
        *,
        UserId: str,
        UserName: str,
        Engine: str,
        AccessString: str,
        Passwords: List[str] = None,
        NoPasswordRequired: bool = None,
        Tags: List["TagTypeDef"] = None,
        AuthenticationMode: "AuthenticationModeTypeDef" = None
    ) -> UserResponseMetadataTypeDef:
        """
        For Redis engine version 6.0 onwards: Creates a Redis user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#create_user)
        """
    def create_user_group(
        self,
        *,
        UserGroupId: str,
        Engine: str,
        UserIds: List[str] = None,
        Tags: List["TagTypeDef"] = None
    ) -> UserGroupResponseMetadataTypeDef:
        """
        For Redis engine version 6.0 onwards: Creates a Redis user group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.create_user_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#create_user_group)
        """
    def decrease_node_groups_in_global_replication_group(
        self,
        *,
        GlobalReplicationGroupId: str,
        NodeGroupCount: int,
        ApplyImmediately: bool,
        GlobalNodeGroupsToRemove: List[str] = None,
        GlobalNodeGroupsToRetain: List[str] = None
    ) -> DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef:
        """
        Decreases the number of node groups in a Global datastore See also: `AWS API
        Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-
        02/DecreaseNodeGroupsInGlobalReplicationGroup>`_ **Request Syntax** response =
        client.decrease_node_groups_in_global_replication_group...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.decrease_node_groups_in_global_replication_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#decrease_node_groups_in_global_replication_group)
        """
    def decrease_replica_count(
        self,
        *,
        ReplicationGroupId: str,
        ApplyImmediately: bool,
        NewReplicaCount: int = None,
        ReplicaConfiguration: List["ConfigureShardTypeDef"] = None,
        ReplicasToRemove: List[str] = None
    ) -> DecreaseReplicaCountResultTypeDef:
        """
        Dynamically decreases the number of replicas in a Redis (cluster mode disabled)
        replication group or the number of replica nodes in one or more node groups
        (shards) of a Redis (cluster mode enabled) replication group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.decrease_replica_count)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#decrease_replica_count)
        """
    def delete_cache_cluster(
        self, *, CacheClusterId: str, FinalSnapshotIdentifier: str = None
    ) -> DeleteCacheClusterResultTypeDef:
        """
        Deletes a previously provisioned cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.delete_cache_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#delete_cache_cluster)
        """
    def delete_cache_parameter_group(self, *, CacheParameterGroupName: str) -> None:
        """
        Deletes the specified cache parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.delete_cache_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#delete_cache_parameter_group)
        """
    def delete_cache_security_group(self, *, CacheSecurityGroupName: str) -> None:
        """
        Deletes a cache security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.delete_cache_security_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#delete_cache_security_group)
        """
    def delete_cache_subnet_group(self, *, CacheSubnetGroupName: str) -> None:
        """
        Deletes a cache subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.delete_cache_subnet_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#delete_cache_subnet_group)
        """
    def delete_global_replication_group(
        self, *, GlobalReplicationGroupId: str, RetainPrimaryReplicationGroup: bool
    ) -> DeleteGlobalReplicationGroupResultTypeDef:
        """
        Deleting a Global datastore is a two-step process * First, you must
        DisassociateGlobalReplicationGroup to remove the secondary clusters in the
        Global datastore.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.delete_global_replication_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#delete_global_replication_group)
        """
    def delete_replication_group(
        self,
        *,
        ReplicationGroupId: str,
        RetainPrimaryCluster: bool = None,
        FinalSnapshotIdentifier: str = None
    ) -> DeleteReplicationGroupResultTypeDef:
        """
        Deletes an existing replication group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.delete_replication_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#delete_replication_group)
        """
    def delete_snapshot(self, *, SnapshotName: str) -> DeleteSnapshotResultTypeDef:
        """
        Deletes an existing snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.delete_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#delete_snapshot)
        """
    def delete_user(self, *, UserId: str) -> UserResponseMetadataTypeDef:
        """
        For Redis engine version 6.0 onwards: Deletes a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#delete_user)
        """
    def delete_user_group(self, *, UserGroupId: str) -> UserGroupResponseMetadataTypeDef:
        """
        For Redis engine version 6.0 onwards: Deletes a user group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.delete_user_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#delete_user_group)
        """
    def describe_cache_clusters(
        self,
        *,
        CacheClusterId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None
    ) -> CacheClusterMessageTypeDef:
        """
        Returns information about all provisioned clusters if no cluster identifier is
        specified, or about a specific cache cluster if a cluster identifier is
        supplied.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.describe_cache_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#describe_cache_clusters)
        """
    def describe_cache_engine_versions(
        self,
        *,
        Engine: str = None,
        EngineVersion: str = None,
        CacheParameterGroupFamily: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        DefaultOnly: bool = None
    ) -> CacheEngineVersionMessageTypeDef:
        """
        Returns a list of the available cache engines and their versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.describe_cache_engine_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#describe_cache_engine_versions)
        """
    def describe_cache_parameter_groups(
        self, *, CacheParameterGroupName: str = None, MaxRecords: int = None, Marker: str = None
    ) -> CacheParameterGroupsMessageTypeDef:
        """
        Returns a list of cache parameter group descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.describe_cache_parameter_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#describe_cache_parameter_groups)
        """
    def describe_cache_parameters(
        self,
        *,
        CacheParameterGroupName: str,
        Source: str = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> CacheParameterGroupDetailsTypeDef:
        """
        Returns the detailed parameter list for a particular cache parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.describe_cache_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#describe_cache_parameters)
        """
    def describe_cache_security_groups(
        self, *, CacheSecurityGroupName: str = None, MaxRecords: int = None, Marker: str = None
    ) -> CacheSecurityGroupMessageTypeDef:
        """
        Returns a list of cache security group descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.describe_cache_security_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#describe_cache_security_groups)
        """
    def describe_cache_subnet_groups(
        self, *, CacheSubnetGroupName: str = None, MaxRecords: int = None, Marker: str = None
    ) -> CacheSubnetGroupMessageTypeDef:
        """
        Returns a list of cache subnet group descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.describe_cache_subnet_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#describe_cache_subnet_groups)
        """
    def describe_engine_default_parameters(
        self, *, CacheParameterGroupFamily: str, MaxRecords: int = None, Marker: str = None
    ) -> DescribeEngineDefaultParametersResultTypeDef:
        """
        Returns the default engine and system parameter information for the specified
        cache engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.describe_engine_default_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#describe_engine_default_parameters)
        """
    def describe_events(
        self,
        *,
        SourceIdentifier: str = None,
        SourceType: SourceTypeType = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        Duration: int = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> EventsMessageTypeDef:
        """
        Returns events related to clusters, cache security groups, and cache parameter
        groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.describe_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#describe_events)
        """
    def describe_global_replication_groups(
        self,
        *,
        GlobalReplicationGroupId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowMemberInfo: bool = None
    ) -> DescribeGlobalReplicationGroupsResultTypeDef:
        """
        Returns information about a particular global replication group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.describe_global_replication_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#describe_global_replication_groups)
        """
    def describe_replication_groups(
        self, *, ReplicationGroupId: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ReplicationGroupMessageTypeDef:
        """
        Returns information about a particular replication group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.describe_replication_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#describe_replication_groups)
        """
    def describe_reserved_cache_nodes(
        self,
        *,
        ReservedCacheNodeId: str = None,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> ReservedCacheNodeMessageTypeDef:
        """
        Returns information about reserved cache nodes for this account, or about a
        specified reserved cache node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.describe_reserved_cache_nodes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#describe_reserved_cache_nodes)
        """
    def describe_reserved_cache_nodes_offerings(
        self,
        *,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> ReservedCacheNodesOfferingMessageTypeDef:
        """
        Lists available reserved cache node offerings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.describe_reserved_cache_nodes_offerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#describe_reserved_cache_nodes_offerings)
        """
    def describe_service_updates(
        self,
        *,
        ServiceUpdateName: str = None,
        ServiceUpdateStatus: List[ServiceUpdateStatusType] = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> ServiceUpdatesMessageTypeDef:
        """
        Returns details of the service updates See also: `AWS API Documentation <https:/
        /docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-
        02/DescribeServiceUpdates>`_ **Request Syntax** response =
        client.describe_service_updates( ServiceUpdateName='string',
        ServiceUpdateStatus=[...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.describe_service_updates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#describe_service_updates)
        """
    def describe_snapshots(
        self,
        *,
        ReplicationGroupId: str = None,
        CacheClusterId: str = None,
        SnapshotName: str = None,
        SnapshotSource: str = None,
        Marker: str = None,
        MaxRecords: int = None,
        ShowNodeGroupConfig: bool = None
    ) -> DescribeSnapshotsListMessageTypeDef:
        """
        Returns information about cluster or replication group snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.describe_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#describe_snapshots)
        """
    def describe_update_actions(
        self,
        *,
        ServiceUpdateName: str = None,
        ReplicationGroupIds: List[str] = None,
        CacheClusterIds: List[str] = None,
        Engine: str = None,
        ServiceUpdateStatus: List[ServiceUpdateStatusType] = None,
        ServiceUpdateTimeRange: "TimeRangeFilterTypeDef" = None,
        UpdateActionStatus: List[UpdateActionStatusType] = None,
        ShowNodeLevelUpdateStatus: bool = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> UpdateActionsMessageTypeDef:
        """
        Returns details of the update actions See also: `AWS API Documentation <https://
        docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeUpdateActions>`_
        **Request Syntax** response = client.describe_update_actions(
        ServiceUpdateName='string', ReplicationGroupIds=[ ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.describe_update_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#describe_update_actions)
        """
    def describe_user_groups(
        self, *, UserGroupId: str = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeUserGroupsResultTypeDef:
        """
        Returns a list of user groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.describe_user_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#describe_user_groups)
        """
    def describe_users(
        self,
        *,
        Engine: str = None,
        UserId: str = None,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> DescribeUsersResultTypeDef:
        """
        Returns a list of users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.describe_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#describe_users)
        """
    def disassociate_global_replication_group(
        self, *, GlobalReplicationGroupId: str, ReplicationGroupId: str, ReplicationGroupRegion: str
    ) -> DisassociateGlobalReplicationGroupResultTypeDef:
        """
        Remove a secondary cluster from the Global datastore using the Global datastore
        name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.disassociate_global_replication_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#disassociate_global_replication_group)
        """
    def failover_global_replication_group(
        self, *, GlobalReplicationGroupId: str, PrimaryRegion: str, PrimaryReplicationGroupId: str
    ) -> FailoverGlobalReplicationGroupResultTypeDef:
        """
        Used to failover the primary region to a secondary region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.failover_global_replication_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#failover_global_replication_group)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#generate_presigned_url)
        """
    def increase_node_groups_in_global_replication_group(
        self,
        *,
        GlobalReplicationGroupId: str,
        NodeGroupCount: int,
        ApplyImmediately: bool,
        RegionalConfigurations: List["RegionalConfigurationTypeDef"] = None
    ) -> IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef:
        """
        Increase the number of node groups in the Global datastore See also: `AWS API
        Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-
        02/IncreaseNodeGroupsInGlobalReplicationGroup>`_ **Request Syntax** response =
        client.increase_node_groups_in_global_replication_grou...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.increase_node_groups_in_global_replication_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#increase_node_groups_in_global_replication_group)
        """
    def increase_replica_count(
        self,
        *,
        ReplicationGroupId: str,
        ApplyImmediately: bool,
        NewReplicaCount: int = None,
        ReplicaConfiguration: List["ConfigureShardTypeDef"] = None
    ) -> IncreaseReplicaCountResultTypeDef:
        """
        Dynamically increases the number of replicas in a Redis (cluster mode disabled)
        replication group or the number of replica nodes in one or more node groups
        (shards) of a Redis (cluster mode enabled) replication group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.increase_replica_count)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#increase_replica_count)
        """
    def list_allowed_node_type_modifications(
        self, *, CacheClusterId: str = None, ReplicationGroupId: str = None
    ) -> AllowedNodeTypeModificationsMessageTypeDef:
        """
        Lists all available node types that you can scale your Redis cluster's or
        replication group's current node type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.list_allowed_node_type_modifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#list_allowed_node_type_modifications)
        """
    def list_tags_for_resource(self, *, ResourceName: str) -> TagListMessageTypeDef:
        """
        Lists all tags currently on a named resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#list_tags_for_resource)
        """
    def modify_cache_cluster(
        self,
        *,
        CacheClusterId: str,
        NumCacheNodes: int = None,
        CacheNodeIdsToRemove: List[str] = None,
        AZMode: AZModeType = None,
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
        AuthTokenUpdateStrategy: AuthTokenUpdateStrategyTypeType = None,
        LogDeliveryConfigurations: List["LogDeliveryConfigurationRequestTypeDef"] = None,
        IpDiscovery: IpDiscoveryType = None
    ) -> ModifyCacheClusterResultTypeDef:
        """
        Modifies the settings for a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.modify_cache_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#modify_cache_cluster)
        """
    def modify_cache_parameter_group(
        self,
        *,
        CacheParameterGroupName: str,
        ParameterNameValues: List["ParameterNameValueTypeDef"]
    ) -> CacheParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a cache parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.modify_cache_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#modify_cache_parameter_group)
        """
    def modify_cache_subnet_group(
        self,
        *,
        CacheSubnetGroupName: str,
        CacheSubnetGroupDescription: str = None,
        SubnetIds: List[str] = None
    ) -> ModifyCacheSubnetGroupResultTypeDef:
        """
        Modifies an existing cache subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.modify_cache_subnet_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#modify_cache_subnet_group)
        """
    def modify_global_replication_group(
        self,
        *,
        GlobalReplicationGroupId: str,
        ApplyImmediately: bool,
        CacheNodeType: str = None,
        EngineVersion: str = None,
        CacheParameterGroupName: str = None,
        GlobalReplicationGroupDescription: str = None,
        AutomaticFailoverEnabled: bool = None
    ) -> ModifyGlobalReplicationGroupResultTypeDef:
        """
        Modifies the settings for a Global datastore.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.modify_global_replication_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#modify_global_replication_group)
        """
    def modify_replication_group(
        self,
        *,
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
        AuthTokenUpdateStrategy: AuthTokenUpdateStrategyTypeType = None,
        UserGroupIdsToAdd: List[str] = None,
        UserGroupIdsToRemove: List[str] = None,
        RemoveUserGroups: bool = None,
        LogDeliveryConfigurations: List["LogDeliveryConfigurationRequestTypeDef"] = None,
        IpDiscovery: IpDiscoveryType = None,
        TransitEncryptionEnabled: bool = None,
        TransitEncryptionMode: TransitEncryptionModeType = None
    ) -> ModifyReplicationGroupResultTypeDef:
        """
        Modifies the settings for a replication group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.modify_replication_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#modify_replication_group)
        """
    def modify_replication_group_shard_configuration(
        self,
        *,
        ReplicationGroupId: str,
        NodeGroupCount: int,
        ApplyImmediately: bool,
        ReshardingConfiguration: List["ReshardingConfigurationTypeDef"] = None,
        NodeGroupsToRemove: List[str] = None,
        NodeGroupsToRetain: List[str] = None
    ) -> ModifyReplicationGroupShardConfigurationResultTypeDef:
        """
        Modifies a replication group's shards (node groups) by allowing you to add
        shards, remove shards, or rebalance the keyspaces among existing shards.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.modify_replication_group_shard_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#modify_replication_group_shard_configuration)
        """
    def modify_user(
        self,
        *,
        UserId: str,
        AccessString: str = None,
        AppendAccessString: str = None,
        Passwords: List[str] = None,
        NoPasswordRequired: bool = None,
        AuthenticationMode: "AuthenticationModeTypeDef" = None
    ) -> UserResponseMetadataTypeDef:
        """
        Changes user password(s) and/or access string.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.modify_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#modify_user)
        """
    def modify_user_group(
        self, *, UserGroupId: str, UserIdsToAdd: List[str] = None, UserIdsToRemove: List[str] = None
    ) -> UserGroupResponseMetadataTypeDef:
        """
        Changes the list of users that belong to the user group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.modify_user_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#modify_user_group)
        """
    def purchase_reserved_cache_nodes_offering(
        self,
        *,
        ReservedCacheNodesOfferingId: str,
        ReservedCacheNodeId: str = None,
        CacheNodeCount: int = None,
        Tags: List["TagTypeDef"] = None
    ) -> PurchaseReservedCacheNodesOfferingResultTypeDef:
        """
        Allows you to purchase a reserved cache node offering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.purchase_reserved_cache_nodes_offering)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#purchase_reserved_cache_nodes_offering)
        """
    def rebalance_slots_in_global_replication_group(
        self, *, GlobalReplicationGroupId: str, ApplyImmediately: bool
    ) -> RebalanceSlotsInGlobalReplicationGroupResultTypeDef:
        """
        Redistribute slots to ensure uniform distribution across existing shards in the
        cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.rebalance_slots_in_global_replication_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#rebalance_slots_in_global_replication_group)
        """
    def reboot_cache_cluster(
        self, *, CacheClusterId: str, CacheNodeIdsToReboot: List[str]
    ) -> RebootCacheClusterResultTypeDef:
        """
        Reboots some, or all, of the cache nodes within a provisioned cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.reboot_cache_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#reboot_cache_cluster)
        """
    def remove_tags_from_resource(
        self, *, ResourceName: str, TagKeys: List[str]
    ) -> TagListMessageTypeDef:
        """
        Removes the tags identified by the `TagKeys` list from the named resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.remove_tags_from_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#remove_tags_from_resource)
        """
    def reset_cache_parameter_group(
        self,
        *,
        CacheParameterGroupName: str,
        ResetAllParameters: bool = None,
        ParameterNameValues: List["ParameterNameValueTypeDef"] = None
    ) -> CacheParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a cache parameter group to the engine or system
        default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.reset_cache_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#reset_cache_parameter_group)
        """
    def revoke_cache_security_group_ingress(
        self,
        *,
        CacheSecurityGroupName: str,
        EC2SecurityGroupName: str,
        EC2SecurityGroupOwnerId: str
    ) -> RevokeCacheSecurityGroupIngressResultTypeDef:
        """
        Revokes ingress from a cache security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.revoke_cache_security_group_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#revoke_cache_security_group_ingress)
        """
    def start_migration(
        self,
        *,
        ReplicationGroupId: str,
        CustomerNodeEndpointList: List["CustomerNodeEndpointTypeDef"]
    ) -> StartMigrationResponseTypeDef:
        """
        Start the migration of data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.start_migration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#start_migration)
        """
    def test_failover(
        self, *, ReplicationGroupId: str, NodeGroupId: str
    ) -> TestFailoverResultTypeDef:
        """
        Represents the input of a `TestFailover` operation which test automatic failover
        on a specified node group (called shard in the console) in a replication group
        (called cluster in the console).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Client.test_failover)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client.html#test_failover)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cache_clusters"]
    ) -> DescribeCacheClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheClusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators.html#describecacheclusterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cache_engine_versions"]
    ) -> DescribeCacheEngineVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheEngineVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators.html#describecacheengineversionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cache_parameter_groups"]
    ) -> DescribeCacheParameterGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameterGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators.html#describecacheparametergroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cache_parameters"]
    ) -> DescribeCacheParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators.html#describecacheparameterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cache_security_groups"]
    ) -> DescribeCacheSecurityGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSecurityGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators.html#describecachesecuritygroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cache_subnet_groups"]
    ) -> DescribeCacheSubnetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSubnetGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators.html#describecachesubnetgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_engine_default_parameters"]
    ) -> DescribeEngineDefaultParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEngineDefaultParameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators.html#describeenginedefaultparameterspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators.html#describeeventspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_global_replication_groups"]
    ) -> DescribeGlobalReplicationGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Paginator.DescribeGlobalReplicationGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators.html#describeglobalreplicationgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_groups"]
    ) -> DescribeReplicationGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReplicationGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators.html#describereplicationgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_cache_nodes"]
    ) -> DescribeReservedCacheNodesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators.html#describereservedcachenodespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_cache_nodes_offerings"]
    ) -> DescribeReservedCacheNodesOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodesOfferings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators.html#describereservedcachenodesofferingspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_service_updates"]
    ) -> DescribeServiceUpdatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Paginator.DescribeServiceUpdates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators.html#describeserviceupdatespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshots"]
    ) -> DescribeSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Paginator.DescribeSnapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators.html#describesnapshotspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_update_actions"]
    ) -> DescribeUpdateActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUpdateActions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators.html#describeupdateactionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_user_groups"]
    ) -> DescribeUserGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUserGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators.html#describeusergroupspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_users"]) -> DescribeUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUsers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators.html#describeuserspaginator)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["cache_cluster_available"]
    ) -> CacheClusterAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Waiter.CacheClusterAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/waiters.html#cacheclusteravailablewaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["cache_cluster_deleted"]
    ) -> CacheClusterDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Waiter.CacheClusterDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/waiters.html#cacheclusterdeletedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_group_available"]
    ) -> ReplicationGroupAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Waiter.ReplicationGroupAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/waiters.html#replicationgroupavailablewaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_group_deleted"]
    ) -> ReplicationGroupDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elasticache.html#ElastiCache.Waiter.ReplicationGroupDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/waiters.html#replicationgroupdeletedwaiter)
        """
