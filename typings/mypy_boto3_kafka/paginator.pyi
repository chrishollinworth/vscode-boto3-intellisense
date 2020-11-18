# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for kafka service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_kafka import KafkaClient
    from mypy_boto3_kafka.paginator import (
        ListClusterOperationsPaginator,
        ListClustersPaginator,
        ListConfigurationRevisionsPaginator,
        ListConfigurationsPaginator,
        ListKafkaVersionsPaginator,
        ListNodesPaginator,
        ListScramSecretsPaginator,
    )

    client: KafkaClient = boto3.client("kafka")

    list_cluster_operations_paginator: ListClusterOperationsPaginator = client.get_paginator("list_cluster_operations")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_configuration_revisions_paginator: ListConfigurationRevisionsPaginator = client.get_paginator("list_configuration_revisions")
    list_configurations_paginator: ListConfigurationsPaginator = client.get_paginator("list_configurations")
    list_kafka_versions_paginator: ListKafkaVersionsPaginator = client.get_paginator("list_kafka_versions")
    list_nodes_paginator: ListNodesPaginator = client.get_paginator("list_nodes")
    list_scram_secrets_paginator: ListScramSecretsPaginator = client.get_paginator("list_scram_secrets")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_kafka.type_defs import (
    ListClusterOperationsResponseTypeDef,
    ListClustersResponseTypeDef,
    ListConfigurationRevisionsResponseTypeDef,
    ListConfigurationsResponseTypeDef,
    ListKafkaVersionsResponseTypeDef,
    ListNodesResponseTypeDef,
    ListScramSecretsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListClusterOperationsPaginator",
    "ListClustersPaginator",
    "ListConfigurationRevisionsPaginator",
    "ListConfigurationsPaginator",
    "ListKafkaVersionsPaginator",
    "ListNodesPaginator",
    "ListScramSecretsPaginator",
)


class ListClusterOperationsPaginator(Boto3Paginator):
    """
    [Paginator.ListClusterOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kafka.html#Kafka.Paginator.ListClusterOperations)
    """

    def paginate(
        self, ClusterArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListClusterOperationsResponseTypeDef]:
        """
        [ListClusterOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kafka.html#Kafka.Paginator.ListClusterOperations.paginate)
        """


class ListClustersPaginator(Boto3Paginator):
    """
    [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kafka.html#Kafka.Paginator.ListClusters)
    """

    def paginate(
        self, ClusterNameFilter: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListClustersResponseTypeDef]:
        """
        [ListClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kafka.html#Kafka.Paginator.ListClusters.paginate)
        """


class ListConfigurationRevisionsPaginator(Boto3Paginator):
    """
    [Paginator.ListConfigurationRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kafka.html#Kafka.Paginator.ListConfigurationRevisions)
    """

    def paginate(
        self, Arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConfigurationRevisionsResponseTypeDef]:
        """
        [ListConfigurationRevisions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kafka.html#Kafka.Paginator.ListConfigurationRevisions.paginate)
        """


class ListConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kafka.html#Kafka.Paginator.ListConfigurations)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConfigurationsResponseTypeDef]:
        """
        [ListConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kafka.html#Kafka.Paginator.ListConfigurations.paginate)
        """


class ListKafkaVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListKafkaVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kafka.html#Kafka.Paginator.ListKafkaVersions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListKafkaVersionsResponseTypeDef]:
        """
        [ListKafkaVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kafka.html#Kafka.Paginator.ListKafkaVersions.paginate)
        """


class ListNodesPaginator(Boto3Paginator):
    """
    [Paginator.ListNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kafka.html#Kafka.Paginator.ListNodes)
    """

    def paginate(
        self, ClusterArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNodesResponseTypeDef]:
        """
        [ListNodes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kafka.html#Kafka.Paginator.ListNodes.paginate)
        """


class ListScramSecretsPaginator(Boto3Paginator):
    """
    [Paginator.ListScramSecrets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kafka.html#Kafka.Paginator.ListScramSecrets)
    """

    def paginate(
        self, ClusterArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListScramSecretsResponseTypeDef]:
        """
        [ListScramSecrets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kafka.html#Kafka.Paginator.ListScramSecrets.paginate)
        """
