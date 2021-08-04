"""
Type annotations for redshift service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/literals.html)

Usage::

    ```python
    from mypy_boto3_redshift.literals import ActionTypeType

    data: ActionTypeType = "recommend-node-config"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionTypeType",
    "AquaConfigurationStatusType",
    "AquaStatusType",
    "AuthorizationStatusType",
    "ClusterAvailableWaiterName",
    "ClusterDeletedWaiterName",
    "ClusterRestoredWaiterName",
    "DataShareStatusForConsumerType",
    "DataShareStatusForProducerType",
    "DataShareStatusType",
    "DescribeClusterDbRevisionsPaginatorName",
    "DescribeClusterParameterGroupsPaginatorName",
    "DescribeClusterParametersPaginatorName",
    "DescribeClusterSecurityGroupsPaginatorName",
    "DescribeClusterSnapshotsPaginatorName",
    "DescribeClusterSubnetGroupsPaginatorName",
    "DescribeClusterTracksPaginatorName",
    "DescribeClusterVersionsPaginatorName",
    "DescribeClustersPaginatorName",
    "DescribeDefaultClusterParametersPaginatorName",
    "DescribeEndpointAccessPaginatorName",
    "DescribeEndpointAuthorizationPaginatorName",
    "DescribeEventSubscriptionsPaginatorName",
    "DescribeEventsPaginatorName",
    "DescribeHsmClientCertificatesPaginatorName",
    "DescribeHsmConfigurationsPaginatorName",
    "DescribeNodeConfigurationOptionsPaginatorName",
    "DescribeOrderableClusterOptionsPaginatorName",
    "DescribeReservedNodeOfferingsPaginatorName",
    "DescribeReservedNodesPaginatorName",
    "DescribeScheduledActionsPaginatorName",
    "DescribeSnapshotCopyGrantsPaginatorName",
    "DescribeSnapshotSchedulesPaginatorName",
    "DescribeTableRestoreStatusPaginatorName",
    "DescribeTagsPaginatorName",
    "DescribeUsageLimitsPaginatorName",
    "GetReservedNodeExchangeOfferingsPaginatorName",
    "ModeType",
    "NodeConfigurationOptionsFilterNameType",
    "OperatorTypeType",
    "ParameterApplyTypeType",
    "PartnerIntegrationStatusType",
    "ReservedNodeOfferingTypeType",
    "ScheduleStateType",
    "ScheduledActionFilterNameType",
    "ScheduledActionStateType",
    "ScheduledActionTypeValuesType",
    "SnapshotAttributeToSortByType",
    "SnapshotAvailableWaiterName",
    "SortByOrderType",
    "SourceTypeType",
    "TableRestoreStatusTypeType",
    "UsageLimitBreachActionType",
    "UsageLimitFeatureTypeType",
    "UsageLimitLimitTypeType",
    "UsageLimitPeriodType",
)

ActionTypeType = Literal["recommend-node-config", "resize-cluster", "restore-cluster"]
AquaConfigurationStatusType = Literal["auto", "disabled", "enabled"]
AquaStatusType = Literal["applying", "disabled", "enabled"]
AuthorizationStatusType = Literal["Authorized", "Revoking"]
ClusterAvailableWaiterName = Literal["cluster_available"]
ClusterDeletedWaiterName = Literal["cluster_deleted"]
ClusterRestoredWaiterName = Literal["cluster_restored"]
DataShareStatusForConsumerType = Literal["ACTIVE", "AVAILABLE"]
DataShareStatusForProducerType = Literal[
    "ACTIVE", "AUTHORIZED", "DEAUTHORIZED", "PENDING_AUTHORIZATION", "REJECTED"
]
DataShareStatusType = Literal[
    "ACTIVE", "AUTHORIZED", "AVAILABLE", "DEAUTHORIZED", "PENDING_AUTHORIZATION", "REJECTED"
]
DescribeClusterDbRevisionsPaginatorName = Literal["describe_cluster_db_revisions"]
DescribeClusterParameterGroupsPaginatorName = Literal["describe_cluster_parameter_groups"]
DescribeClusterParametersPaginatorName = Literal["describe_cluster_parameters"]
DescribeClusterSecurityGroupsPaginatorName = Literal["describe_cluster_security_groups"]
DescribeClusterSnapshotsPaginatorName = Literal["describe_cluster_snapshots"]
DescribeClusterSubnetGroupsPaginatorName = Literal["describe_cluster_subnet_groups"]
DescribeClusterTracksPaginatorName = Literal["describe_cluster_tracks"]
DescribeClusterVersionsPaginatorName = Literal["describe_cluster_versions"]
DescribeClustersPaginatorName = Literal["describe_clusters"]
DescribeDefaultClusterParametersPaginatorName = Literal["describe_default_cluster_parameters"]
DescribeEndpointAccessPaginatorName = Literal["describe_endpoint_access"]
DescribeEndpointAuthorizationPaginatorName = Literal["describe_endpoint_authorization"]
DescribeEventSubscriptionsPaginatorName = Literal["describe_event_subscriptions"]
DescribeEventsPaginatorName = Literal["describe_events"]
DescribeHsmClientCertificatesPaginatorName = Literal["describe_hsm_client_certificates"]
DescribeHsmConfigurationsPaginatorName = Literal["describe_hsm_configurations"]
DescribeNodeConfigurationOptionsPaginatorName = Literal["describe_node_configuration_options"]
DescribeOrderableClusterOptionsPaginatorName = Literal["describe_orderable_cluster_options"]
DescribeReservedNodeOfferingsPaginatorName = Literal["describe_reserved_node_offerings"]
DescribeReservedNodesPaginatorName = Literal["describe_reserved_nodes"]
DescribeScheduledActionsPaginatorName = Literal["describe_scheduled_actions"]
DescribeSnapshotCopyGrantsPaginatorName = Literal["describe_snapshot_copy_grants"]
DescribeSnapshotSchedulesPaginatorName = Literal["describe_snapshot_schedules"]
DescribeTableRestoreStatusPaginatorName = Literal["describe_table_restore_status"]
DescribeTagsPaginatorName = Literal["describe_tags"]
DescribeUsageLimitsPaginatorName = Literal["describe_usage_limits"]
GetReservedNodeExchangeOfferingsPaginatorName = Literal["get_reserved_node_exchange_offerings"]
ModeType = Literal["high-performance", "standard"]
NodeConfigurationOptionsFilterNameType = Literal[
    "EstimatedDiskUtilizationPercent", "Mode", "NodeType", "NumberOfNodes"
]
OperatorTypeType = Literal["between", "eq", "ge", "gt", "in", "le", "lt"]
ParameterApplyTypeType = Literal["dynamic", "static"]
PartnerIntegrationStatusType = Literal["Active", "ConnectionFailure", "Inactive", "RuntimeFailure"]
ReservedNodeOfferingTypeType = Literal["Regular", "Upgradable"]
ScheduleStateType = Literal["ACTIVE", "FAILED", "MODIFYING"]
ScheduledActionFilterNameType = Literal["cluster-identifier", "iam-role"]
ScheduledActionStateType = Literal["ACTIVE", "DISABLED"]
ScheduledActionTypeValuesType = Literal["PauseCluster", "ResizeCluster", "ResumeCluster"]
SnapshotAttributeToSortByType = Literal["CREATE_TIME", "SOURCE_TYPE", "TOTAL_SIZE"]
SnapshotAvailableWaiterName = Literal["snapshot_available"]
SortByOrderType = Literal["ASC", "DESC"]
SourceTypeType = Literal[
    "cluster",
    "cluster-parameter-group",
    "cluster-security-group",
    "cluster-snapshot",
    "scheduled-action",
]
TableRestoreStatusTypeType = Literal["CANCELED", "FAILED", "IN_PROGRESS", "PENDING", "SUCCEEDED"]
UsageLimitBreachActionType = Literal["disable", "emit-metric", "log"]
UsageLimitFeatureTypeType = Literal["concurrency-scaling", "spectrum"]
UsageLimitLimitTypeType = Literal["data-scanned", "time"]
UsageLimitPeriodType = Literal["daily", "monthly", "weekly"]
