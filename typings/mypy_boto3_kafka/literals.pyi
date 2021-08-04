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
    "ConfigurationStateType",
    "EnhancedMonitoringType",
    "KafkaVersionStatusType",
    "ListClusterOperationsPaginatorName",
    "ListClustersPaginatorName",
    "ListConfigurationRevisionsPaginatorName",
    "ListConfigurationsPaginatorName",
    "ListKafkaVersionsPaginatorName",
    "ListNodesPaginatorName",
    "ListScramSecretsPaginatorName",
    "NodeTypeType",
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
ConfigurationStateType = Literal["ACTIVE", "DELETE_FAILED", "DELETING"]
EnhancedMonitoringType = Literal[
    "DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER", "PER_TOPIC_PER_PARTITION"
]
KafkaVersionStatusType = Literal["ACTIVE", "DEPRECATED"]
ListClusterOperationsPaginatorName = Literal["list_cluster_operations"]
ListClustersPaginatorName = Literal["list_clusters"]
ListConfigurationRevisionsPaginatorName = Literal["list_configuration_revisions"]
ListConfigurationsPaginatorName = Literal["list_configurations"]
ListKafkaVersionsPaginatorName = Literal["list_kafka_versions"]
ListNodesPaginatorName = Literal["list_nodes"]
ListScramSecretsPaginatorName = Literal["list_scram_secrets"]
NodeTypeType = Literal["BROKER"]
