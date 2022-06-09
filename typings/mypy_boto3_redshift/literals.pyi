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
    "DescribeDataSharesForConsumerPaginatorName",
    "DescribeDataSharesForProducerPaginatorName",
    "DescribeDataSharesPaginatorName",
    "DescribeDefaultClusterParametersPaginatorName",
    "DescribeEndpointAccessPaginatorName",
    "DescribeEndpointAuthorizationPaginatorName",
    "DescribeEventSubscriptionsPaginatorName",
    "DescribeEventsPaginatorName",
    "DescribeHsmClientCertificatesPaginatorName",
    "DescribeHsmConfigurationsPaginatorName",
    "DescribeNodeConfigurationOptionsPaginatorName",
    "DescribeOrderableClusterOptionsPaginatorName",
    "DescribeReservedNodeExchangeStatusPaginatorName",
    "DescribeReservedNodeOfferingsPaginatorName",
    "DescribeReservedNodesPaginatorName",
    "DescribeScheduledActionsPaginatorName",
    "DescribeSnapshotCopyGrantsPaginatorName",
    "DescribeSnapshotSchedulesPaginatorName",
    "DescribeTableRestoreStatusPaginatorName",
    "DescribeTagsPaginatorName",
    "DescribeUsageLimitsPaginatorName",
    "GetReservedNodeExchangeConfigurationOptionsPaginatorName",
    "GetReservedNodeExchangeOfferingsPaginatorName",
    "LogDestinationTypeType",
    "ModeType",
    "NodeConfigurationOptionsFilterNameType",
    "OperatorTypeType",
    "ParameterApplyTypeType",
    "PartnerIntegrationStatusType",
    "ReservedNodeExchangeActionTypeType",
    "ReservedNodeExchangeStatusTypeType",
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
DescribeDataSharesForConsumerPaginatorName = Literal["describe_data_shares_for_consumer"]
DescribeDataSharesForProducerPaginatorName = Literal["describe_data_shares_for_producer"]
DescribeDataSharesPaginatorName = Literal["describe_data_shares"]
DescribeDefaultClusterParametersPaginatorName = Literal["describe_default_cluster_parameters"]
DescribeEndpointAccessPaginatorName = Literal["describe_endpoint_access"]
DescribeEndpointAuthorizationPaginatorName = Literal["describe_endpoint_authorization"]
DescribeEventSubscriptionsPaginatorName = Literal["describe_event_subscriptions"]
DescribeEventsPaginatorName = Literal["describe_events"]
DescribeHsmClientCertificatesPaginatorName = Literal["describe_hsm_client_certificates"]
DescribeHsmConfigurationsPaginatorName = Literal["describe_hsm_configurations"]
DescribeNodeConfigurationOptionsPaginatorName = Literal["describe_node_configuration_options"]
DescribeOrderableClusterOptionsPaginatorName = Literal["describe_orderable_cluster_options"]
DescribeReservedNodeExchangeStatusPaginatorName = Literal["describe_reserved_node_exchange_status"]
DescribeReservedNodeOfferingsPaginatorName = Literal["describe_reserved_node_offerings"]
DescribeReservedNodesPaginatorName = Literal["describe_reserved_nodes"]
DescribeScheduledActionsPaginatorName = Literal["describe_scheduled_actions"]
DescribeSnapshotCopyGrantsPaginatorName = Literal["describe_snapshot_copy_grants"]
DescribeSnapshotSchedulesPaginatorName = Literal["describe_snapshot_schedules"]
DescribeTableRestoreStatusPaginatorName = Literal["describe_table_restore_status"]
DescribeTagsPaginatorName = Literal["describe_tags"]
DescribeUsageLimitsPaginatorName = Literal["describe_usage_limits"]
GetReservedNodeExchangeConfigurationOptionsPaginatorName = Literal[
    "get_reserved_node_exchange_configuration_options"
]
GetReservedNodeExchangeOfferingsPaginatorName = Literal["get_reserved_node_exchange_offerings"]
LogDestinationTypeType = Literal["cloudwatch", "s3"]
ModeType = Literal["high-performance", "standard"]
NodeConfigurationOptionsFilterNameType = Literal[
    "EstimatedDiskUtilizationPercent", "Mode", "NodeType", "NumberOfNodes"
]
OperatorTypeType = Literal["between", "eq", "ge", "gt", "in", "le", "lt"]
ParameterApplyTypeType = Literal["dynamic", "static"]
PartnerIntegrationStatusType = Literal["Active", "ConnectionFailure", "Inactive", "RuntimeFailure"]
ReservedNodeExchangeActionTypeType = Literal["resize-cluster", "restore-cluster"]
ReservedNodeExchangeStatusTypeType = Literal[
    "FAILED", "IN_PROGRESS", "PENDING", "REQUESTED", "RETRYING", "SUCCEEDED"
]
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
UsageLimitFeatureTypeType = Literal["concurrency-scaling", "cross-region-datasharing", "spectrum"]
UsageLimitLimitTypeType = Literal["data-scanned", "time"]
UsageLimitPeriodType = Literal["daily", "monthly", "weekly"]
