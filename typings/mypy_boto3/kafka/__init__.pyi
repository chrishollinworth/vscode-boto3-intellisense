"""
Main interface for kafka service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_kafka import (
        Client,
        DescribeTopicPartitionsPaginator,
        KafkaClient,
        ListClientVpcConnectionsPaginator,
        ListClusterOperationsPaginator,
        ListClusterOperationsV2Paginator,
        ListClustersPaginator,
        ListClustersV2Paginator,
        ListConfigurationRevisionsPaginator,
        ListConfigurationsPaginator,
        ListKafkaVersionsPaginator,
        ListNodesPaginator,
        ListReplicatorsPaginator,
        ListScramSecretsPaginator,
        ListTopicsPaginator,
        ListVpcConnectionsPaginator,
    )

    session = Session()
    client: KafkaClient = session.client("kafka")

    describe_topic_partitions_paginator: DescribeTopicPartitionsPaginator = client.get_paginator("describe_topic_partitions")
    list_client_vpc_connections_paginator: ListClientVpcConnectionsPaginator = client.get_paginator("list_client_vpc_connections")
    list_cluster_operations_paginator: ListClusterOperationsPaginator = client.get_paginator("list_cluster_operations")
    list_cluster_operations_v2_paginator: ListClusterOperationsV2Paginator = client.get_paginator("list_cluster_operations_v2")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_clusters_v2_paginator: ListClustersV2Paginator = client.get_paginator("list_clusters_v2")
    list_configuration_revisions_paginator: ListConfigurationRevisionsPaginator = client.get_paginator("list_configuration_revisions")
    list_configurations_paginator: ListConfigurationsPaginator = client.get_paginator("list_configurations")
    list_kafka_versions_paginator: ListKafkaVersionsPaginator = client.get_paginator("list_kafka_versions")
    list_nodes_paginator: ListNodesPaginator = client.get_paginator("list_nodes")
    list_replicators_paginator: ListReplicatorsPaginator = client.get_paginator("list_replicators")
    list_scram_secrets_paginator: ListScramSecretsPaginator = client.get_paginator("list_scram_secrets")
    list_topics_paginator: ListTopicsPaginator = client.get_paginator("list_topics")
    list_vpc_connections_paginator: ListVpcConnectionsPaginator = client.get_paginator("list_vpc_connections")
    ```
"""

from .client import KafkaClient
from .paginator import (
    DescribeTopicPartitionsPaginator,
    ListClientVpcConnectionsPaginator,
    ListClusterOperationsPaginator,
    ListClusterOperationsV2Paginator,
    ListClustersPaginator,
    ListClustersV2Paginator,
    ListConfigurationRevisionsPaginator,
    ListConfigurationsPaginator,
    ListKafkaVersionsPaginator,
    ListNodesPaginator,
    ListReplicatorsPaginator,
    ListScramSecretsPaginator,
    ListTopicsPaginator,
    ListVpcConnectionsPaginator,
)

Client = KafkaClient

__all__ = (
    "Client",
    "DescribeTopicPartitionsPaginator",
    "KafkaClient",
    "ListClientVpcConnectionsPaginator",
    "ListClusterOperationsPaginator",
    "ListClusterOperationsV2Paginator",
    "ListClustersPaginator",
    "ListClustersV2Paginator",
    "ListConfigurationRevisionsPaginator",
    "ListConfigurationsPaginator",
    "ListKafkaVersionsPaginator",
    "ListNodesPaginator",
    "ListReplicatorsPaginator",
    "ListScramSecretsPaginator",
    "ListTopicsPaginator",
    "ListVpcConnectionsPaginator",
)
