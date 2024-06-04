"""
Type annotations for kafka service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafka/literals.html)

Usage::

    ```python
    from mypy_boto3_kafka.literals import BrokerAZDistributionType

    data: BrokerAZDistributionType = "DEFAULT"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BrokerAZDistributionType",
    "ClientBrokerType",
    "ClusterStateType",
    "ClusterTypeType",
    "ConfigurationStateType",
    "CustomerActionStatusType",
    "EnhancedMonitoringType",
    "KafkaVersionStatusType",
    "ListClientVpcConnectionsPaginatorName",
    "ListClusterOperationsPaginatorName",
    "ListClusterOperationsV2PaginatorName",
    "ListClustersPaginatorName",
    "ListClustersV2PaginatorName",
    "ListConfigurationRevisionsPaginatorName",
    "ListConfigurationsPaginatorName",
    "ListKafkaVersionsPaginatorName",
    "ListNodesPaginatorName",
    "ListReplicatorsPaginatorName",
    "ListScramSecretsPaginatorName",
    "ListVpcConnectionsPaginatorName",
    "NodeTypeType",
    "ReplicationStartingPositionTypeType",
    "ReplicatorStateType",
    "StorageModeType",
    "TargetCompressionTypeType",
    "UserIdentityTypeType",
    "VpcConnectionStateType",
)

BrokerAZDistributionType = Literal["DEFAULT"]
ClientBrokerType = Literal["PLAINTEXT", "TLS", "TLS_PLAINTEXT"]
ClusterStateType = Literal[
    "ACTIVE",
    "CREATING",
    "DELETING",
    "FAILED",
    "HEALING",
    "MAINTENANCE",
    "REBOOTING_BROKER",
    "UPDATING",
]
ClusterTypeType = Literal["PROVISIONED", "SERVERLESS"]
ConfigurationStateType = Literal["ACTIVE", "DELETE_FAILED", "DELETING"]
CustomerActionStatusType = Literal["ACTION_RECOMMENDED", "CRITICAL_ACTION_REQUIRED", "NONE"]
EnhancedMonitoringType = Literal[
    "DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER", "PER_TOPIC_PER_PARTITION"
]
KafkaVersionStatusType = Literal["ACTIVE", "DEPRECATED"]
ListClientVpcConnectionsPaginatorName = Literal["list_client_vpc_connections"]
ListClusterOperationsPaginatorName = Literal["list_cluster_operations"]
ListClusterOperationsV2PaginatorName = Literal["list_cluster_operations_v2"]
ListClustersPaginatorName = Literal["list_clusters"]
ListClustersV2PaginatorName = Literal["list_clusters_v2"]
ListConfigurationRevisionsPaginatorName = Literal["list_configuration_revisions"]
ListConfigurationsPaginatorName = Literal["list_configurations"]
ListKafkaVersionsPaginatorName = Literal["list_kafka_versions"]
ListNodesPaginatorName = Literal["list_nodes"]
ListReplicatorsPaginatorName = Literal["list_replicators"]
ListScramSecretsPaginatorName = Literal["list_scram_secrets"]
ListVpcConnectionsPaginatorName = Literal["list_vpc_connections"]
NodeTypeType = Literal["BROKER"]
ReplicationStartingPositionTypeType = Literal["EARLIEST", "LATEST"]
ReplicatorStateType = Literal["CREATING", "DELETING", "FAILED", "RUNNING", "UPDATING"]
StorageModeType = Literal["LOCAL", "TIERED"]
TargetCompressionTypeType = Literal["GZIP", "LZ4", "NONE", "SNAPPY", "ZSTD"]
UserIdentityTypeType = Literal["AWSACCOUNT", "AWSSERVICE"]
VpcConnectionStateType = Literal[
    "AVAILABLE",
    "CREATING",
    "DEACTIVATING",
    "DELETING",
    "FAILED",
    "INACTIVE",
    "REJECTED",
    "REJECTING",
]
