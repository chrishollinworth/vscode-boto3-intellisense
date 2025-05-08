"""
Type annotations for elasticache service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_elasticache.client import ElastiCacheClient

    session = Session()
    client: ElastiCacheClient = session.client("elasticache")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
    DescribeServerlessCacheSnapshotsPaginator,
    DescribeServerlessCachesPaginator,
    DescribeServiceUpdatesPaginator,
    DescribeSnapshotsPaginator,
    DescribeUpdateActionsPaginator,
    DescribeUserGroupsPaginator,
    DescribeUsersPaginator,
)
from .type_defs import (
    AddTagsToResourceMessageTypeDef,
    AllowedNodeTypeModificationsMessageTypeDef,
    AuthorizeCacheSecurityGroupIngressMessageTypeDef,
    AuthorizeCacheSecurityGroupIngressResultTypeDef,
    BatchApplyUpdateActionMessageTypeDef,
    BatchStopUpdateActionMessageTypeDef,
    CacheClusterMessageTypeDef,
    CacheEngineVersionMessageTypeDef,
    CacheParameterGroupDetailsTypeDef,
    CacheParameterGroupNameMessageTypeDef,
    CacheParameterGroupsMessageTypeDef,
    CacheSecurityGroupMessageTypeDef,
    CacheSubnetGroupMessageTypeDef,
    CompleteMigrationMessageTypeDef,
    CompleteMigrationResponseTypeDef,
    CopyServerlessCacheSnapshotRequestTypeDef,
    CopyServerlessCacheSnapshotResponseTypeDef,
    CopySnapshotMessageTypeDef,
    CopySnapshotResultTypeDef,
    CreateCacheClusterMessageTypeDef,
    CreateCacheClusterResultTypeDef,
    CreateCacheParameterGroupMessageTypeDef,
    CreateCacheParameterGroupResultTypeDef,
    CreateCacheSecurityGroupMessageTypeDef,
    CreateCacheSecurityGroupResultTypeDef,
    CreateCacheSubnetGroupMessageTypeDef,
    CreateCacheSubnetGroupResultTypeDef,
    CreateGlobalReplicationGroupMessageTypeDef,
    CreateGlobalReplicationGroupResultTypeDef,
    CreateReplicationGroupMessageTypeDef,
    CreateReplicationGroupResultTypeDef,
    CreateServerlessCacheRequestTypeDef,
    CreateServerlessCacheResponseTypeDef,
    CreateServerlessCacheSnapshotRequestTypeDef,
    CreateServerlessCacheSnapshotResponseTypeDef,
    CreateSnapshotMessageTypeDef,
    CreateSnapshotResultTypeDef,
    CreateUserGroupMessageTypeDef,
    CreateUserMessageTypeDef,
    DecreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef,
    DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef,
    DecreaseReplicaCountMessageTypeDef,
    DecreaseReplicaCountResultTypeDef,
    DeleteCacheClusterMessageTypeDef,
    DeleteCacheClusterResultTypeDef,
    DeleteCacheParameterGroupMessageTypeDef,
    DeleteCacheSecurityGroupMessageTypeDef,
    DeleteCacheSubnetGroupMessageTypeDef,
    DeleteGlobalReplicationGroupMessageTypeDef,
    DeleteGlobalReplicationGroupResultTypeDef,
    DeleteReplicationGroupMessageTypeDef,
    DeleteReplicationGroupResultTypeDef,
    DeleteServerlessCacheRequestTypeDef,
    DeleteServerlessCacheResponseTypeDef,
    DeleteServerlessCacheSnapshotRequestTypeDef,
    DeleteServerlessCacheSnapshotResponseTypeDef,
    DeleteSnapshotMessageTypeDef,
    DeleteSnapshotResultTypeDef,
    DeleteUserGroupMessageTypeDef,
    DeleteUserMessageTypeDef,
    DescribeCacheClustersMessageTypeDef,
    DescribeCacheEngineVersionsMessageTypeDef,
    DescribeCacheParameterGroupsMessageTypeDef,
    DescribeCacheParametersMessageTypeDef,
    DescribeCacheSecurityGroupsMessageTypeDef,
    DescribeCacheSubnetGroupsMessageTypeDef,
    DescribeEngineDefaultParametersMessageTypeDef,
    DescribeEngineDefaultParametersResultTypeDef,
    DescribeEventsMessageTypeDef,
    DescribeGlobalReplicationGroupsMessageTypeDef,
    DescribeGlobalReplicationGroupsResultTypeDef,
    DescribeReplicationGroupsMessageTypeDef,
    DescribeReservedCacheNodesMessageTypeDef,
    DescribeReservedCacheNodesOfferingsMessageTypeDef,
    DescribeServerlessCacheSnapshotsRequestTypeDef,
    DescribeServerlessCacheSnapshotsResponseTypeDef,
    DescribeServerlessCachesRequestTypeDef,
    DescribeServerlessCachesResponseTypeDef,
    DescribeServiceUpdatesMessageTypeDef,
    DescribeSnapshotsListMessageTypeDef,
    DescribeSnapshotsMessageTypeDef,
    DescribeUpdateActionsMessageTypeDef,
    DescribeUserGroupsMessageTypeDef,
    DescribeUserGroupsResultTypeDef,
    DescribeUsersMessageTypeDef,
    DescribeUsersResultTypeDef,
    DisassociateGlobalReplicationGroupMessageTypeDef,
    DisassociateGlobalReplicationGroupResultTypeDef,
    EmptyResponseMetadataTypeDef,
    EventsMessageTypeDef,
    ExportServerlessCacheSnapshotRequestTypeDef,
    ExportServerlessCacheSnapshotResponseTypeDef,
    FailoverGlobalReplicationGroupMessageTypeDef,
    FailoverGlobalReplicationGroupResultTypeDef,
    IncreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef,
    IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef,
    IncreaseReplicaCountMessageTypeDef,
    IncreaseReplicaCountResultTypeDef,
    ListAllowedNodeTypeModificationsMessageTypeDef,
    ListTagsForResourceMessageTypeDef,
    ModifyCacheClusterMessageTypeDef,
    ModifyCacheClusterResultTypeDef,
    ModifyCacheParameterGroupMessageTypeDef,
    ModifyCacheSubnetGroupMessageTypeDef,
    ModifyCacheSubnetGroupResultTypeDef,
    ModifyGlobalReplicationGroupMessageTypeDef,
    ModifyGlobalReplicationGroupResultTypeDef,
    ModifyReplicationGroupMessageTypeDef,
    ModifyReplicationGroupResultTypeDef,
    ModifyReplicationGroupShardConfigurationMessageTypeDef,
    ModifyReplicationGroupShardConfigurationResultTypeDef,
    ModifyServerlessCacheRequestTypeDef,
    ModifyServerlessCacheResponseTypeDef,
    ModifyUserGroupMessageTypeDef,
    ModifyUserMessageTypeDef,
    PurchaseReservedCacheNodesOfferingMessageTypeDef,
    PurchaseReservedCacheNodesOfferingResultTypeDef,
    RebalanceSlotsInGlobalReplicationGroupMessageTypeDef,
    RebalanceSlotsInGlobalReplicationGroupResultTypeDef,
    RebootCacheClusterMessageTypeDef,
    RebootCacheClusterResultTypeDef,
    RemoveTagsFromResourceMessageTypeDef,
    ReplicationGroupMessageTypeDef,
    ReservedCacheNodeMessageTypeDef,
    ReservedCacheNodesOfferingMessageTypeDef,
    ResetCacheParameterGroupMessageTypeDef,
    RevokeCacheSecurityGroupIngressMessageTypeDef,
    RevokeCacheSecurityGroupIngressResultTypeDef,
    ServiceUpdatesMessageTypeDef,
    StartMigrationMessageTypeDef,
    StartMigrationResponseTypeDef,
    TagListMessageTypeDef,
    TestFailoverMessageTypeDef,
    TestFailoverResultTypeDef,
    TestMigrationMessageTypeDef,
    TestMigrationResponseTypeDef,
    UpdateActionResultsMessageTypeDef,
    UpdateActionsMessageTypeDef,
    UserGroupResponseTypeDef,
    UserResponseTypeDef,
)
from .waiter import (
    CacheClusterAvailableWaiter,
    CacheClusterDeletedWaiter,
    ReplicationGroupAvailableWaiter,
    ReplicationGroupDeletedWaiter,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("ElastiCacheClient",)

class Exceptions(BaseClientExceptions):
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
    InvalidCredentialsException: Type[BotocoreClientError]
    InvalidGlobalReplicationGroupStateFault: Type[BotocoreClientError]
    InvalidKMSKeyFault: Type[BotocoreClientError]
    InvalidParameterCombinationException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidReplicationGroupStateFault: Type[BotocoreClientError]
    InvalidServerlessCacheSnapshotStateFault: Type[BotocoreClientError]
    InvalidServerlessCacheStateFault: Type[BotocoreClientError]
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
    ServerlessCacheAlreadyExistsFault: Type[BotocoreClientError]
    ServerlessCacheNotFoundFault: Type[BotocoreClientError]
    ServerlessCacheQuotaForCustomerExceededFault: Type[BotocoreClientError]
    ServerlessCacheSnapshotAlreadyExistsFault: Type[BotocoreClientError]
    ServerlessCacheSnapshotNotFoundFault: Type[BotocoreClientError]
    ServerlessCacheSnapshotQuotaExceededFault: Type[BotocoreClientError]
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ElastiCacheClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#generate_presigned_url)
        """

    def add_tags_to_resource(
        self, **kwargs: Unpack[AddTagsToResourceMessageTypeDef]
    ) -> TagListMessageTypeDef:
        """
        A tag is a key-value pair where the key and value are case-sensitive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/add_tags_to_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#add_tags_to_resource)
        """

    def authorize_cache_security_group_ingress(
        self, **kwargs: Unpack[AuthorizeCacheSecurityGroupIngressMessageTypeDef]
    ) -> AuthorizeCacheSecurityGroupIngressResultTypeDef:
        """
        Allows network ingress to a cache security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/authorize_cache_security_group_ingress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#authorize_cache_security_group_ingress)
        """

    def batch_apply_update_action(
        self, **kwargs: Unpack[BatchApplyUpdateActionMessageTypeDef]
    ) -> UpdateActionResultsMessageTypeDef:
        """
        Apply the service update.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/batch_apply_update_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#batch_apply_update_action)
        """

    def batch_stop_update_action(
        self, **kwargs: Unpack[BatchStopUpdateActionMessageTypeDef]
    ) -> UpdateActionResultsMessageTypeDef:
        """
        Stop the service update.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/batch_stop_update_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#batch_stop_update_action)
        """

    def complete_migration(
        self, **kwargs: Unpack[CompleteMigrationMessageTypeDef]
    ) -> CompleteMigrationResponseTypeDef:
        """
        Complete the migration of data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/complete_migration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#complete_migration)
        """

    def copy_serverless_cache_snapshot(
        self, **kwargs: Unpack[CopyServerlessCacheSnapshotRequestTypeDef]
    ) -> CopyServerlessCacheSnapshotResponseTypeDef:
        """
        Creates a copy of an existing serverless cache's snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/copy_serverless_cache_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#copy_serverless_cache_snapshot)
        """

    def copy_snapshot(
        self, **kwargs: Unpack[CopySnapshotMessageTypeDef]
    ) -> CopySnapshotResultTypeDef:
        """
        Makes a copy of an existing snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/copy_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#copy_snapshot)
        """

    def create_cache_cluster(
        self, **kwargs: Unpack[CreateCacheClusterMessageTypeDef]
    ) -> CreateCacheClusterResultTypeDef:
        """
        Creates a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/create_cache_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#create_cache_cluster)
        """

    def create_cache_parameter_group(
        self, **kwargs: Unpack[CreateCacheParameterGroupMessageTypeDef]
    ) -> CreateCacheParameterGroupResultTypeDef:
        """
        Creates a new Amazon ElastiCache cache parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/create_cache_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#create_cache_parameter_group)
        """

    def create_cache_security_group(
        self, **kwargs: Unpack[CreateCacheSecurityGroupMessageTypeDef]
    ) -> CreateCacheSecurityGroupResultTypeDef:
        """
        Creates a new cache security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/create_cache_security_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#create_cache_security_group)
        """

    def create_cache_subnet_group(
        self, **kwargs: Unpack[CreateCacheSubnetGroupMessageTypeDef]
    ) -> CreateCacheSubnetGroupResultTypeDef:
        """
        Creates a new cache subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/create_cache_subnet_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#create_cache_subnet_group)
        """

    def create_global_replication_group(
        self, **kwargs: Unpack[CreateGlobalReplicationGroupMessageTypeDef]
    ) -> CreateGlobalReplicationGroupResultTypeDef:
        """
        Global Datastore offers fully managed, fast, reliable and secure cross-region
        replication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/create_global_replication_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#create_global_replication_group)
        """

    def create_replication_group(
        self, **kwargs: Unpack[CreateReplicationGroupMessageTypeDef]
    ) -> CreateReplicationGroupResultTypeDef:
        """
        Creates a Valkey or Redis OSS (cluster mode disabled) or a Valkey or Redis OSS
        (cluster mode enabled) replication group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/create_replication_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#create_replication_group)
        """

    def create_serverless_cache(
        self, **kwargs: Unpack[CreateServerlessCacheRequestTypeDef]
    ) -> CreateServerlessCacheResponseTypeDef:
        """
        Creates a serverless cache.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/create_serverless_cache.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#create_serverless_cache)
        """

    def create_serverless_cache_snapshot(
        self, **kwargs: Unpack[CreateServerlessCacheSnapshotRequestTypeDef]
    ) -> CreateServerlessCacheSnapshotResponseTypeDef:
        """
        This API creates a copy of an entire ServerlessCache at a specific moment in
        time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/create_serverless_cache_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#create_serverless_cache_snapshot)
        """

    def create_snapshot(
        self, **kwargs: Unpack[CreateSnapshotMessageTypeDef]
    ) -> CreateSnapshotResultTypeDef:
        """
        Creates a copy of an entire cluster or replication group at a specific moment
        in time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/create_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#create_snapshot)
        """

    def create_user(self, **kwargs: Unpack[CreateUserMessageTypeDef]) -> UserResponseTypeDef:
        """
        For Valkey engine version 7.2 onwards and Redis OSS 6.0 to 7.1: Creates a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/create_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#create_user)
        """

    def create_user_group(
        self, **kwargs: Unpack[CreateUserGroupMessageTypeDef]
    ) -> UserGroupResponseTypeDef:
        """
        For Valkey engine version 7.2 onwards and Redis OSS 6.0 to 7.1: Creates a user
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/create_user_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#create_user_group)
        """

    def decrease_node_groups_in_global_replication_group(
        self, **kwargs: Unpack[DecreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef]
    ) -> DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef:
        """
        Decreases the number of node groups in a Global datastore.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/decrease_node_groups_in_global_replication_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#decrease_node_groups_in_global_replication_group)
        """

    def decrease_replica_count(
        self, **kwargs: Unpack[DecreaseReplicaCountMessageTypeDef]
    ) -> DecreaseReplicaCountResultTypeDef:
        """
        Dynamically decreases the number of replicas in a Valkey or Redis OSS (cluster
        mode disabled) replication group or the number of replica nodes in one or more
        node groups (shards) of a Valkey or Redis OSS (cluster mode enabled)
        replication group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/decrease_replica_count.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#decrease_replica_count)
        """

    def delete_cache_cluster(
        self, **kwargs: Unpack[DeleteCacheClusterMessageTypeDef]
    ) -> DeleteCacheClusterResultTypeDef:
        """
        Deletes a previously provisioned cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/delete_cache_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#delete_cache_cluster)
        """

    def delete_cache_parameter_group(
        self, **kwargs: Unpack[DeleteCacheParameterGroupMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified cache parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/delete_cache_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#delete_cache_parameter_group)
        """

    def delete_cache_security_group(
        self, **kwargs: Unpack[DeleteCacheSecurityGroupMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a cache security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/delete_cache_security_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#delete_cache_security_group)
        """

    def delete_cache_subnet_group(
        self, **kwargs: Unpack[DeleteCacheSubnetGroupMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a cache subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/delete_cache_subnet_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#delete_cache_subnet_group)
        """

    def delete_global_replication_group(
        self, **kwargs: Unpack[DeleteGlobalReplicationGroupMessageTypeDef]
    ) -> DeleteGlobalReplicationGroupResultTypeDef:
        """
        Deleting a Global datastore is a two-step process:.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/delete_global_replication_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#delete_global_replication_group)
        """

    def delete_replication_group(
        self, **kwargs: Unpack[DeleteReplicationGroupMessageTypeDef]
    ) -> DeleteReplicationGroupResultTypeDef:
        """
        Deletes an existing replication group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/delete_replication_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#delete_replication_group)
        """

    def delete_serverless_cache(
        self, **kwargs: Unpack[DeleteServerlessCacheRequestTypeDef]
    ) -> DeleteServerlessCacheResponseTypeDef:
        """
        Deletes a specified existing serverless cache.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/delete_serverless_cache.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#delete_serverless_cache)
        """

    def delete_serverless_cache_snapshot(
        self, **kwargs: Unpack[DeleteServerlessCacheSnapshotRequestTypeDef]
    ) -> DeleteServerlessCacheSnapshotResponseTypeDef:
        """
        Deletes an existing serverless cache snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/delete_serverless_cache_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#delete_serverless_cache_snapshot)
        """

    def delete_snapshot(
        self, **kwargs: Unpack[DeleteSnapshotMessageTypeDef]
    ) -> DeleteSnapshotResultTypeDef:
        """
        Deletes an existing snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/delete_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#delete_snapshot)
        """

    def delete_user(self, **kwargs: Unpack[DeleteUserMessageTypeDef]) -> UserResponseTypeDef:
        """
        For Valkey engine version 7.2 onwards and Redis OSS 6.0 onwards: Deletes a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/delete_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#delete_user)
        """

    def delete_user_group(
        self, **kwargs: Unpack[DeleteUserGroupMessageTypeDef]
    ) -> UserGroupResponseTypeDef:
        """
        For Valkey engine version 7.2 onwards and Redis OSS 6.0 onwards: Deletes a user
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/delete_user_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#delete_user_group)
        """

    def describe_cache_clusters(
        self, **kwargs: Unpack[DescribeCacheClustersMessageTypeDef]
    ) -> CacheClusterMessageTypeDef:
        """
        Returns information about all provisioned clusters if no cluster identifier is
        specified, or about a specific cache cluster if a cluster identifier is
        supplied.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/describe_cache_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#describe_cache_clusters)
        """

    def describe_cache_engine_versions(
        self, **kwargs: Unpack[DescribeCacheEngineVersionsMessageTypeDef]
    ) -> CacheEngineVersionMessageTypeDef:
        """
        Returns a list of the available cache engines and their versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/describe_cache_engine_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#describe_cache_engine_versions)
        """

    def describe_cache_parameter_groups(
        self, **kwargs: Unpack[DescribeCacheParameterGroupsMessageTypeDef]
    ) -> CacheParameterGroupsMessageTypeDef:
        """
        Returns a list of cache parameter group descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/describe_cache_parameter_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#describe_cache_parameter_groups)
        """

    def describe_cache_parameters(
        self, **kwargs: Unpack[DescribeCacheParametersMessageTypeDef]
    ) -> CacheParameterGroupDetailsTypeDef:
        """
        Returns the detailed parameter list for a particular cache parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/describe_cache_parameters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#describe_cache_parameters)
        """

    def describe_cache_security_groups(
        self, **kwargs: Unpack[DescribeCacheSecurityGroupsMessageTypeDef]
    ) -> CacheSecurityGroupMessageTypeDef:
        """
        Returns a list of cache security group descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/describe_cache_security_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#describe_cache_security_groups)
        """

    def describe_cache_subnet_groups(
        self, **kwargs: Unpack[DescribeCacheSubnetGroupsMessageTypeDef]
    ) -> CacheSubnetGroupMessageTypeDef:
        """
        Returns a list of cache subnet group descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/describe_cache_subnet_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#describe_cache_subnet_groups)
        """

    def describe_engine_default_parameters(
        self, **kwargs: Unpack[DescribeEngineDefaultParametersMessageTypeDef]
    ) -> DescribeEngineDefaultParametersResultTypeDef:
        """
        Returns the default engine and system parameter information for the specified
        cache engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/describe_engine_default_parameters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#describe_engine_default_parameters)
        """

    def describe_events(
        self, **kwargs: Unpack[DescribeEventsMessageTypeDef]
    ) -> EventsMessageTypeDef:
        """
        Returns events related to clusters, cache security groups, and cache parameter
        groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/describe_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#describe_events)
        """

    def describe_global_replication_groups(
        self, **kwargs: Unpack[DescribeGlobalReplicationGroupsMessageTypeDef]
    ) -> DescribeGlobalReplicationGroupsResultTypeDef:
        """
        Returns information about a particular global replication group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/describe_global_replication_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#describe_global_replication_groups)
        """

    def describe_replication_groups(
        self, **kwargs: Unpack[DescribeReplicationGroupsMessageTypeDef]
    ) -> ReplicationGroupMessageTypeDef:
        """
        Returns information about a particular replication group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/describe_replication_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#describe_replication_groups)
        """

    def describe_reserved_cache_nodes(
        self, **kwargs: Unpack[DescribeReservedCacheNodesMessageTypeDef]
    ) -> ReservedCacheNodeMessageTypeDef:
        """
        Returns information about reserved cache nodes for this account, or about a
        specified reserved cache node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/describe_reserved_cache_nodes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#describe_reserved_cache_nodes)
        """

    def describe_reserved_cache_nodes_offerings(
        self, **kwargs: Unpack[DescribeReservedCacheNodesOfferingsMessageTypeDef]
    ) -> ReservedCacheNodesOfferingMessageTypeDef:
        """
        Lists available reserved cache node offerings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/describe_reserved_cache_nodes_offerings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#describe_reserved_cache_nodes_offerings)
        """

    def describe_serverless_cache_snapshots(
        self, **kwargs: Unpack[DescribeServerlessCacheSnapshotsRequestTypeDef]
    ) -> DescribeServerlessCacheSnapshotsResponseTypeDef:
        """
        Returns information about serverless cache snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/describe_serverless_cache_snapshots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#describe_serverless_cache_snapshots)
        """

    def describe_serverless_caches(
        self, **kwargs: Unpack[DescribeServerlessCachesRequestTypeDef]
    ) -> DescribeServerlessCachesResponseTypeDef:
        """
        Returns information about a specific serverless cache.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/describe_serverless_caches.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#describe_serverless_caches)
        """

    def describe_service_updates(
        self, **kwargs: Unpack[DescribeServiceUpdatesMessageTypeDef]
    ) -> ServiceUpdatesMessageTypeDef:
        """
        Returns details of the service updates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/describe_service_updates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#describe_service_updates)
        """

    def describe_snapshots(
        self, **kwargs: Unpack[DescribeSnapshotsMessageTypeDef]
    ) -> DescribeSnapshotsListMessageTypeDef:
        """
        Returns information about cluster or replication group snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/describe_snapshots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#describe_snapshots)
        """

    def describe_update_actions(
        self, **kwargs: Unpack[DescribeUpdateActionsMessageTypeDef]
    ) -> UpdateActionsMessageTypeDef:
        """
        Returns details of the update actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/describe_update_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#describe_update_actions)
        """

    def describe_user_groups(
        self, **kwargs: Unpack[DescribeUserGroupsMessageTypeDef]
    ) -> DescribeUserGroupsResultTypeDef:
        """
        Returns a list of user groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/describe_user_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#describe_user_groups)
        """

    def describe_users(
        self, **kwargs: Unpack[DescribeUsersMessageTypeDef]
    ) -> DescribeUsersResultTypeDef:
        """
        Returns a list of users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/describe_users.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#describe_users)
        """

    def disassociate_global_replication_group(
        self, **kwargs: Unpack[DisassociateGlobalReplicationGroupMessageTypeDef]
    ) -> DisassociateGlobalReplicationGroupResultTypeDef:
        """
        Remove a secondary cluster from the Global datastore using the Global datastore
        name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/disassociate_global_replication_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#disassociate_global_replication_group)
        """

    def export_serverless_cache_snapshot(
        self, **kwargs: Unpack[ExportServerlessCacheSnapshotRequestTypeDef]
    ) -> ExportServerlessCacheSnapshotResponseTypeDef:
        """
        Provides the functionality to export the serverless cache snapshot data to
        Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/export_serverless_cache_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#export_serverless_cache_snapshot)
        """

    def failover_global_replication_group(
        self, **kwargs: Unpack[FailoverGlobalReplicationGroupMessageTypeDef]
    ) -> FailoverGlobalReplicationGroupResultTypeDef:
        """
        Used to failover the primary region to a secondary region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/failover_global_replication_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#failover_global_replication_group)
        """

    def increase_node_groups_in_global_replication_group(
        self, **kwargs: Unpack[IncreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef]
    ) -> IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef:
        """
        Increase the number of node groups in the Global datastore.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/increase_node_groups_in_global_replication_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#increase_node_groups_in_global_replication_group)
        """

    def increase_replica_count(
        self, **kwargs: Unpack[IncreaseReplicaCountMessageTypeDef]
    ) -> IncreaseReplicaCountResultTypeDef:
        """
        Dynamically increases the number of replicas in a Valkey or Redis OSS (cluster
        mode disabled) replication group or the number of replica nodes in one or more
        node groups (shards) of a Valkey or Redis OSS (cluster mode enabled)
        replication group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/increase_replica_count.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#increase_replica_count)
        """

    def list_allowed_node_type_modifications(
        self, **kwargs: Unpack[ListAllowedNodeTypeModificationsMessageTypeDef]
    ) -> AllowedNodeTypeModificationsMessageTypeDef:
        """
        Lists all available node types that you can scale with your cluster's
        replication group's current node type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/list_allowed_node_type_modifications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#list_allowed_node_type_modifications)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceMessageTypeDef]
    ) -> TagListMessageTypeDef:
        """
        Lists all tags currently on a named resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#list_tags_for_resource)
        """

    def modify_cache_cluster(
        self, **kwargs: Unpack[ModifyCacheClusterMessageTypeDef]
    ) -> ModifyCacheClusterResultTypeDef:
        """
        Modifies the settings for a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/modify_cache_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#modify_cache_cluster)
        """

    def modify_cache_parameter_group(
        self, **kwargs: Unpack[ModifyCacheParameterGroupMessageTypeDef]
    ) -> CacheParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a cache parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/modify_cache_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#modify_cache_parameter_group)
        """

    def modify_cache_subnet_group(
        self, **kwargs: Unpack[ModifyCacheSubnetGroupMessageTypeDef]
    ) -> ModifyCacheSubnetGroupResultTypeDef:
        """
        Modifies an existing cache subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/modify_cache_subnet_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#modify_cache_subnet_group)
        """

    def modify_global_replication_group(
        self, **kwargs: Unpack[ModifyGlobalReplicationGroupMessageTypeDef]
    ) -> ModifyGlobalReplicationGroupResultTypeDef:
        """
        Modifies the settings for a Global datastore.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/modify_global_replication_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#modify_global_replication_group)
        """

    def modify_replication_group(
        self, **kwargs: Unpack[ModifyReplicationGroupMessageTypeDef]
    ) -> ModifyReplicationGroupResultTypeDef:
        """
        Modifies the settings for a replication group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/modify_replication_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#modify_replication_group)
        """

    def modify_replication_group_shard_configuration(
        self, **kwargs: Unpack[ModifyReplicationGroupShardConfigurationMessageTypeDef]
    ) -> ModifyReplicationGroupShardConfigurationResultTypeDef:
        """
        Modifies a replication group's shards (node groups) by allowing you to add
        shards, remove shards, or rebalance the keyspaces among existing shards.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/modify_replication_group_shard_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#modify_replication_group_shard_configuration)
        """

    def modify_serverless_cache(
        self, **kwargs: Unpack[ModifyServerlessCacheRequestTypeDef]
    ) -> ModifyServerlessCacheResponseTypeDef:
        """
        This API modifies the attributes of a serverless cache.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/modify_serverless_cache.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#modify_serverless_cache)
        """

    def modify_user(self, **kwargs: Unpack[ModifyUserMessageTypeDef]) -> UserResponseTypeDef:
        """
        Changes user password(s) and/or access string.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/modify_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#modify_user)
        """

    def modify_user_group(
        self, **kwargs: Unpack[ModifyUserGroupMessageTypeDef]
    ) -> UserGroupResponseTypeDef:
        """
        Changes the list of users that belong to the user group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/modify_user_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#modify_user_group)
        """

    def purchase_reserved_cache_nodes_offering(
        self, **kwargs: Unpack[PurchaseReservedCacheNodesOfferingMessageTypeDef]
    ) -> PurchaseReservedCacheNodesOfferingResultTypeDef:
        """
        Allows you to purchase a reserved cache node offering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/purchase_reserved_cache_nodes_offering.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#purchase_reserved_cache_nodes_offering)
        """

    def rebalance_slots_in_global_replication_group(
        self, **kwargs: Unpack[RebalanceSlotsInGlobalReplicationGroupMessageTypeDef]
    ) -> RebalanceSlotsInGlobalReplicationGroupResultTypeDef:
        """
        Redistribute slots to ensure uniform distribution across existing shards in the
        cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/rebalance_slots_in_global_replication_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#rebalance_slots_in_global_replication_group)
        """

    def reboot_cache_cluster(
        self, **kwargs: Unpack[RebootCacheClusterMessageTypeDef]
    ) -> RebootCacheClusterResultTypeDef:
        """
        Reboots some, or all, of the cache nodes within a provisioned cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/reboot_cache_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#reboot_cache_cluster)
        """

    def remove_tags_from_resource(
        self, **kwargs: Unpack[RemoveTagsFromResourceMessageTypeDef]
    ) -> TagListMessageTypeDef:
        """
        Removes the tags identified by the <code>TagKeys</code> list from the named
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/remove_tags_from_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#remove_tags_from_resource)
        """

    def reset_cache_parameter_group(
        self, **kwargs: Unpack[ResetCacheParameterGroupMessageTypeDef]
    ) -> CacheParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a cache parameter group to the engine or system
        default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/reset_cache_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#reset_cache_parameter_group)
        """

    def revoke_cache_security_group_ingress(
        self, **kwargs: Unpack[RevokeCacheSecurityGroupIngressMessageTypeDef]
    ) -> RevokeCacheSecurityGroupIngressResultTypeDef:
        """
        Revokes ingress from a cache security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/revoke_cache_security_group_ingress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#revoke_cache_security_group_ingress)
        """

    def start_migration(
        self, **kwargs: Unpack[StartMigrationMessageTypeDef]
    ) -> StartMigrationResponseTypeDef:
        """
        Start the migration of data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/start_migration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#start_migration)
        """

    def test_failover(
        self, **kwargs: Unpack[TestFailoverMessageTypeDef]
    ) -> TestFailoverResultTypeDef:
        """
        Represents the input of a <code>TestFailover</code> operation which tests
        automatic failover on a specified node group (called shard in the console) in a
        replication group (called cluster in the console).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/test_failover.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#test_failover)
        """

    def test_migration(
        self, **kwargs: Unpack[TestMigrationMessageTypeDef]
    ) -> TestMigrationResponseTypeDef:
        """
        Async API to test connection between source and target replication group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/test_migration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#test_migration)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_cache_clusters"]
    ) -> DescribeCacheClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_cache_engine_versions"]
    ) -> DescribeCacheEngineVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_cache_parameter_groups"]
    ) -> DescribeCacheParameterGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_cache_parameters"]
    ) -> DescribeCacheParametersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_cache_security_groups"]
    ) -> DescribeCacheSecurityGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_cache_subnet_groups"]
    ) -> DescribeCacheSubnetGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_engine_default_parameters"]
    ) -> DescribeEngineDefaultParametersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_events"]
    ) -> DescribeEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_global_replication_groups"]
    ) -> DescribeGlobalReplicationGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_replication_groups"]
    ) -> DescribeReplicationGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_reserved_cache_nodes_offerings"]
    ) -> DescribeReservedCacheNodesOfferingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_reserved_cache_nodes"]
    ) -> DescribeReservedCacheNodesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_serverless_cache_snapshots"]
    ) -> DescribeServerlessCacheSnapshotsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_serverless_caches"]
    ) -> DescribeServerlessCachesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_service_updates"]
    ) -> DescribeServiceUpdatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_snapshots"]
    ) -> DescribeSnapshotsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_update_actions"]
    ) -> DescribeUpdateActionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_user_groups"]
    ) -> DescribeUserGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_users"]
    ) -> DescribeUsersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["cache_cluster_available"]
    ) -> CacheClusterAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["cache_cluster_deleted"]
    ) -> CacheClusterDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["replication_group_available"]
    ) -> ReplicationGroupAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["replication_group_deleted"]
    ) -> ReplicationGroupDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/client/#get_waiter)
        """
