"""
Type annotations for rds service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/literals.html)

Usage::

    ```python
    from mypy_boto3_rds.literals import ActivityStreamModeType

    data: ActivityStreamModeType = "async"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActivityStreamModeType",
    "ActivityStreamPolicyStatusType",
    "ActivityStreamStatusType",
    "ApplyMethodType",
    "AuditPolicyStateType",
    "AuthSchemeType",
    "AutomationModeType",
    "ClientPasswordAuthTypeType",
    "CustomEngineVersionStatusType",
    "DBClusterAvailableWaiterName",
    "DBClusterDeletedWaiterName",
    "DBClusterSnapshotAvailableWaiterName",
    "DBClusterSnapshotDeletedWaiterName",
    "DBInstanceAvailableWaiterName",
    "DBInstanceDeletedWaiterName",
    "DBProxyEndpointStatusType",
    "DBProxyEndpointTargetRoleType",
    "DBProxyStatusType",
    "DBSnapshotAvailableWaiterName",
    "DBSnapshotCompletedWaiterName",
    "DBSnapshotDeletedWaiterName",
    "DescribeBlueGreenDeploymentsPaginatorName",
    "DescribeCertificatesPaginatorName",
    "DescribeDBClusterAutomatedBackupsPaginatorName",
    "DescribeDBClusterBacktracksPaginatorName",
    "DescribeDBClusterEndpointsPaginatorName",
    "DescribeDBClusterParameterGroupsPaginatorName",
    "DescribeDBClusterParametersPaginatorName",
    "DescribeDBClusterSnapshotsPaginatorName",
    "DescribeDBClustersPaginatorName",
    "DescribeDBEngineVersionsPaginatorName",
    "DescribeDBInstanceAutomatedBackupsPaginatorName",
    "DescribeDBInstancesPaginatorName",
    "DescribeDBLogFilesPaginatorName",
    "DescribeDBParameterGroupsPaginatorName",
    "DescribeDBParametersPaginatorName",
    "DescribeDBProxiesPaginatorName",
    "DescribeDBProxyEndpointsPaginatorName",
    "DescribeDBProxyTargetGroupsPaginatorName",
    "DescribeDBProxyTargetsPaginatorName",
    "DescribeDBRecommendationsPaginatorName",
    "DescribeDBSecurityGroupsPaginatorName",
    "DescribeDBSnapshotTenantDatabasesPaginatorName",
    "DescribeDBSnapshotsPaginatorName",
    "DescribeDBSubnetGroupsPaginatorName",
    "DescribeEngineDefaultClusterParametersPaginatorName",
    "DescribeEngineDefaultParametersPaginatorName",
    "DescribeEventSubscriptionsPaginatorName",
    "DescribeEventsPaginatorName",
    "DescribeExportTasksPaginatorName",
    "DescribeGlobalClustersPaginatorName",
    "DescribeIntegrationsPaginatorName",
    "DescribeOptionGroupOptionsPaginatorName",
    "DescribeOptionGroupsPaginatorName",
    "DescribeOrderableDBInstanceOptionsPaginatorName",
    "DescribePendingMaintenanceActionsPaginatorName",
    "DescribeReservedDBInstancesOfferingsPaginatorName",
    "DescribeReservedDBInstancesPaginatorName",
    "DescribeSourceRegionsPaginatorName",
    "DescribeTenantDatabasesPaginatorName",
    "DownloadDBLogFilePortionPaginatorName",
    "EngineFamilyType",
    "ExportSourceTypeType",
    "FailoverStatusType",
    "GlobalClusterMemberSynchronizationStatusType",
    "IAMAuthModeType",
    "IntegrationStatusType",
    "LimitlessDatabaseStatusType",
    "LocalWriteForwardingStatusType",
    "ReplicaModeType",
    "SourceTypeType",
    "TargetHealthReasonType",
    "TargetRoleType",
    "TargetStateType",
    "TargetTypeType",
    "TenantDatabaseAvailableWaiterName",
    "TenantDatabaseDeletedWaiterName",
    "WriteForwardingStatusType",
)

ActivityStreamModeType = Literal["async", "sync"]
ActivityStreamPolicyStatusType = Literal["locked", "locking-policy", "unlocked", "unlocking-policy"]
ActivityStreamStatusType = Literal["started", "starting", "stopped", "stopping"]
ApplyMethodType = Literal["immediate", "pending-reboot"]
AuditPolicyStateType = Literal["locked", "unlocked"]
AuthSchemeType = Literal["SECRETS"]
AutomationModeType = Literal["all-paused", "full"]
ClientPasswordAuthTypeType = Literal[
    "MYSQL_NATIVE_PASSWORD", "POSTGRES_MD5", "POSTGRES_SCRAM_SHA_256", "SQL_SERVER_AUTHENTICATION"
]
CustomEngineVersionStatusType = Literal["available", "inactive", "inactive-except-restore"]
DBClusterAvailableWaiterName = Literal["db_cluster_available"]
DBClusterDeletedWaiterName = Literal["db_cluster_deleted"]
DBClusterSnapshotAvailableWaiterName = Literal["db_cluster_snapshot_available"]
DBClusterSnapshotDeletedWaiterName = Literal["db_cluster_snapshot_deleted"]
DBInstanceAvailableWaiterName = Literal["db_instance_available"]
DBInstanceDeletedWaiterName = Literal["db_instance_deleted"]
DBProxyEndpointStatusType = Literal[
    "available",
    "creating",
    "deleting",
    "incompatible-network",
    "insufficient-resource-limits",
    "modifying",
]
DBProxyEndpointTargetRoleType = Literal["READ_ONLY", "READ_WRITE"]
DBProxyStatusType = Literal[
    "available",
    "creating",
    "deleting",
    "incompatible-network",
    "insufficient-resource-limits",
    "modifying",
    "reactivating",
    "suspended",
    "suspending",
]
DBSnapshotAvailableWaiterName = Literal["db_snapshot_available"]
DBSnapshotCompletedWaiterName = Literal["db_snapshot_completed"]
DBSnapshotDeletedWaiterName = Literal["db_snapshot_deleted"]
DescribeBlueGreenDeploymentsPaginatorName = Literal["describe_blue_green_deployments"]
DescribeCertificatesPaginatorName = Literal["describe_certificates"]
DescribeDBClusterAutomatedBackupsPaginatorName = Literal["describe_db_cluster_automated_backups"]
DescribeDBClusterBacktracksPaginatorName = Literal["describe_db_cluster_backtracks"]
DescribeDBClusterEndpointsPaginatorName = Literal["describe_db_cluster_endpoints"]
DescribeDBClusterParameterGroupsPaginatorName = Literal["describe_db_cluster_parameter_groups"]
DescribeDBClusterParametersPaginatorName = Literal["describe_db_cluster_parameters"]
DescribeDBClusterSnapshotsPaginatorName = Literal["describe_db_cluster_snapshots"]
DescribeDBClustersPaginatorName = Literal["describe_db_clusters"]
DescribeDBEngineVersionsPaginatorName = Literal["describe_db_engine_versions"]
DescribeDBInstanceAutomatedBackupsPaginatorName = Literal["describe_db_instance_automated_backups"]
DescribeDBInstancesPaginatorName = Literal["describe_db_instances"]
DescribeDBLogFilesPaginatorName = Literal["describe_db_log_files"]
DescribeDBParameterGroupsPaginatorName = Literal["describe_db_parameter_groups"]
DescribeDBParametersPaginatorName = Literal["describe_db_parameters"]
DescribeDBProxiesPaginatorName = Literal["describe_db_proxies"]
DescribeDBProxyEndpointsPaginatorName = Literal["describe_db_proxy_endpoints"]
DescribeDBProxyTargetGroupsPaginatorName = Literal["describe_db_proxy_target_groups"]
DescribeDBProxyTargetsPaginatorName = Literal["describe_db_proxy_targets"]
DescribeDBRecommendationsPaginatorName = Literal["describe_db_recommendations"]
DescribeDBSecurityGroupsPaginatorName = Literal["describe_db_security_groups"]
DescribeDBSnapshotTenantDatabasesPaginatorName = Literal["describe_db_snapshot_tenant_databases"]
DescribeDBSnapshotsPaginatorName = Literal["describe_db_snapshots"]
DescribeDBSubnetGroupsPaginatorName = Literal["describe_db_subnet_groups"]
DescribeEngineDefaultClusterParametersPaginatorName = Literal[
    "describe_engine_default_cluster_parameters"
]
DescribeEngineDefaultParametersPaginatorName = Literal["describe_engine_default_parameters"]
DescribeEventSubscriptionsPaginatorName = Literal["describe_event_subscriptions"]
DescribeEventsPaginatorName = Literal["describe_events"]
DescribeExportTasksPaginatorName = Literal["describe_export_tasks"]
DescribeGlobalClustersPaginatorName = Literal["describe_global_clusters"]
DescribeIntegrationsPaginatorName = Literal["describe_integrations"]
DescribeOptionGroupOptionsPaginatorName = Literal["describe_option_group_options"]
DescribeOptionGroupsPaginatorName = Literal["describe_option_groups"]
DescribeOrderableDBInstanceOptionsPaginatorName = Literal["describe_orderable_db_instance_options"]
DescribePendingMaintenanceActionsPaginatorName = Literal["describe_pending_maintenance_actions"]
DescribeReservedDBInstancesOfferingsPaginatorName = Literal[
    "describe_reserved_db_instances_offerings"
]
DescribeReservedDBInstancesPaginatorName = Literal["describe_reserved_db_instances"]
DescribeSourceRegionsPaginatorName = Literal["describe_source_regions"]
DescribeTenantDatabasesPaginatorName = Literal["describe_tenant_databases"]
DownloadDBLogFilePortionPaginatorName = Literal["download_db_log_file_portion"]
EngineFamilyType = Literal["MYSQL", "POSTGRESQL", "SQLSERVER"]
ExportSourceTypeType = Literal["CLUSTER", "SNAPSHOT"]
FailoverStatusType = Literal["cancelling", "failing-over", "pending"]
GlobalClusterMemberSynchronizationStatusType = Literal["connected", "pending-resync"]
IAMAuthModeType = Literal["DISABLED", "ENABLED", "REQUIRED"]
IntegrationStatusType = Literal[
    "active", "creating", "deleting", "failed", "modifying", "needs_attention", "syncing"
]
LimitlessDatabaseStatusType = Literal[
    "active",
    "disabled",
    "disabling",
    "enabled",
    "enabling",
    "error",
    "modifying-max-capacity",
    "not-in-use",
]
LocalWriteForwardingStatusType = Literal[
    "disabled", "disabling", "enabled", "enabling", "requested"
]
ReplicaModeType = Literal["mounted", "open-read-only"]
SourceTypeType = Literal[
    "blue-green-deployment",
    "custom-engine-version",
    "db-cluster",
    "db-cluster-snapshot",
    "db-instance",
    "db-parameter-group",
    "db-proxy",
    "db-security-group",
    "db-snapshot",
]
TargetHealthReasonType = Literal[
    "AUTH_FAILURE",
    "CONNECTION_FAILED",
    "INVALID_REPLICATION_STATE",
    "PENDING_PROXY_CAPACITY",
    "UNREACHABLE",
]
TargetRoleType = Literal["READ_ONLY", "READ_WRITE", "UNKNOWN"]
TargetStateType = Literal["AVAILABLE", "REGISTERING", "UNAVAILABLE"]
TargetTypeType = Literal["RDS_INSTANCE", "RDS_SERVERLESS_ENDPOINT", "TRACKED_CLUSTER"]
TenantDatabaseAvailableWaiterName = Literal["tenant_database_available"]
TenantDatabaseDeletedWaiterName = Literal["tenant_database_deleted"]
WriteForwardingStatusType = Literal["disabled", "disabling", "enabled", "enabling", "unknown"]
