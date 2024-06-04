"""
Type annotations for elasticache service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/literals.html)

Usage::

    ```python
    from mypy_boto3_elasticache.literals import AZModeType

    data: AZModeType = "cross-az"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AZModeType",
    "AuthTokenUpdateStatusType",
    "AuthTokenUpdateStrategyTypeType",
    "AuthenticationTypeType",
    "AutomaticFailoverStatusType",
    "CacheClusterAvailableWaiterName",
    "CacheClusterDeletedWaiterName",
    "ChangeTypeType",
    "ClusterModeType",
    "DataStorageUnitType",
    "DataTieringStatusType",
    "DescribeCacheClustersPaginatorName",
    "DescribeCacheEngineVersionsPaginatorName",
    "DescribeCacheParameterGroupsPaginatorName",
    "DescribeCacheParametersPaginatorName",
    "DescribeCacheSecurityGroupsPaginatorName",
    "DescribeCacheSubnetGroupsPaginatorName",
    "DescribeEngineDefaultParametersPaginatorName",
    "DescribeEventsPaginatorName",
    "DescribeGlobalReplicationGroupsPaginatorName",
    "DescribeReplicationGroupsPaginatorName",
    "DescribeReservedCacheNodesOfferingsPaginatorName",
    "DescribeReservedCacheNodesPaginatorName",
    "DescribeServerlessCacheSnapshotsPaginatorName",
    "DescribeServerlessCachesPaginatorName",
    "DescribeServiceUpdatesPaginatorName",
    "DescribeSnapshotsPaginatorName",
    "DescribeUpdateActionsPaginatorName",
    "DescribeUserGroupsPaginatorName",
    "DescribeUsersPaginatorName",
    "DestinationTypeType",
    "InputAuthenticationTypeType",
    "IpDiscoveryType",
    "LogDeliveryConfigurationStatusType",
    "LogFormatType",
    "LogTypeType",
    "MultiAZStatusType",
    "NetworkTypeType",
    "NodeUpdateInitiatedByType",
    "NodeUpdateStatusType",
    "OutpostModeType",
    "PendingAutomaticFailoverStatusType",
    "ReplicationGroupAvailableWaiterName",
    "ReplicationGroupDeletedWaiterName",
    "ServiceUpdateSeverityType",
    "ServiceUpdateStatusType",
    "ServiceUpdateTypeType",
    "SlaMetType",
    "SourceTypeType",
    "TransitEncryptionModeType",
    "UpdateActionStatusType",
)

AZModeType = Literal["cross-az", "single-az"]
AuthTokenUpdateStatusType = Literal["ROTATING", "SETTING"]
AuthTokenUpdateStrategyTypeType = Literal["DELETE", "ROTATE", "SET"]
AuthenticationTypeType = Literal["iam", "no-password", "password"]
AutomaticFailoverStatusType = Literal["disabled", "disabling", "enabled", "enabling"]
CacheClusterAvailableWaiterName = Literal["cache_cluster_available"]
CacheClusterDeletedWaiterName = Literal["cache_cluster_deleted"]
ChangeTypeType = Literal["immediate", "requires-reboot"]
ClusterModeType = Literal["compatible", "disabled", "enabled"]
DataStorageUnitType = Literal["GB"]
DataTieringStatusType = Literal["disabled", "enabled"]
DescribeCacheClustersPaginatorName = Literal["describe_cache_clusters"]
DescribeCacheEngineVersionsPaginatorName = Literal["describe_cache_engine_versions"]
DescribeCacheParameterGroupsPaginatorName = Literal["describe_cache_parameter_groups"]
DescribeCacheParametersPaginatorName = Literal["describe_cache_parameters"]
DescribeCacheSecurityGroupsPaginatorName = Literal["describe_cache_security_groups"]
DescribeCacheSubnetGroupsPaginatorName = Literal["describe_cache_subnet_groups"]
DescribeEngineDefaultParametersPaginatorName = Literal["describe_engine_default_parameters"]
DescribeEventsPaginatorName = Literal["describe_events"]
DescribeGlobalReplicationGroupsPaginatorName = Literal["describe_global_replication_groups"]
DescribeReplicationGroupsPaginatorName = Literal["describe_replication_groups"]
DescribeReservedCacheNodesOfferingsPaginatorName = Literal[
    "describe_reserved_cache_nodes_offerings"
]
DescribeReservedCacheNodesPaginatorName = Literal["describe_reserved_cache_nodes"]
DescribeServerlessCacheSnapshotsPaginatorName = Literal["describe_serverless_cache_snapshots"]
DescribeServerlessCachesPaginatorName = Literal["describe_serverless_caches"]
DescribeServiceUpdatesPaginatorName = Literal["describe_service_updates"]
DescribeSnapshotsPaginatorName = Literal["describe_snapshots"]
DescribeUpdateActionsPaginatorName = Literal["describe_update_actions"]
DescribeUserGroupsPaginatorName = Literal["describe_user_groups"]
DescribeUsersPaginatorName = Literal["describe_users"]
DestinationTypeType = Literal["cloudwatch-logs", "kinesis-firehose"]
InputAuthenticationTypeType = Literal["iam", "no-password-required", "password"]
IpDiscoveryType = Literal["ipv4", "ipv6"]
LogDeliveryConfigurationStatusType = Literal[
    "active", "disabling", "enabling", "error", "modifying"
]
LogFormatType = Literal["json", "text"]
LogTypeType = Literal["engine-log", "slow-log"]
MultiAZStatusType = Literal["disabled", "enabled"]
NetworkTypeType = Literal["dual_stack", "ipv4", "ipv6"]
NodeUpdateInitiatedByType = Literal["customer", "system"]
NodeUpdateStatusType = Literal[
    "complete", "in-progress", "not-applied", "stopped", "stopping", "waiting-to-start"
]
OutpostModeType = Literal["cross-outpost", "single-outpost"]
PendingAutomaticFailoverStatusType = Literal["disabled", "enabled"]
ReplicationGroupAvailableWaiterName = Literal["replication_group_available"]
ReplicationGroupDeletedWaiterName = Literal["replication_group_deleted"]
ServiceUpdateSeverityType = Literal["critical", "important", "low", "medium"]
ServiceUpdateStatusType = Literal["available", "cancelled", "expired"]
ServiceUpdateTypeType = Literal["security-update"]
SlaMetType = Literal["n/a", "no", "yes"]
SourceTypeType = Literal[
    "cache-cluster",
    "cache-parameter-group",
    "cache-security-group",
    "cache-subnet-group",
    "replication-group",
    "serverless-cache",
    "serverless-cache-snapshot",
    "user",
    "user-group",
]
TransitEncryptionModeType = Literal["preferred", "required"]
UpdateActionStatusType = Literal[
    "complete",
    "in-progress",
    "not-applicable",
    "not-applied",
    "scheduled",
    "scheduling",
    "stopped",
    "stopping",
    "waiting-to-start",
]
