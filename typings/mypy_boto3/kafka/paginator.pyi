"""
Type annotations for kafka service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_kafka.client import KafkaClient
    from mypy_boto3_kafka.paginator import (
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
        ListVpcConnectionsPaginator,
    )

    session = Session()
    client: KafkaClient = session.client("kafka")

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
    list_vpc_connections_paginator: ListVpcConnectionsPaginator = client.get_paginator("list_vpc_connections")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListClientVpcConnectionsRequestPaginateTypeDef,
    ListClientVpcConnectionsResponseTypeDef,
    ListClusterOperationsRequestPaginateTypeDef,
    ListClusterOperationsResponseTypeDef,
    ListClusterOperationsV2RequestPaginateTypeDef,
    ListClusterOperationsV2ResponseTypeDef,
    ListClustersRequestPaginateTypeDef,
    ListClustersResponseTypeDef,
    ListClustersV2RequestPaginateTypeDef,
    ListClustersV2ResponseTypeDef,
    ListConfigurationRevisionsRequestPaginateTypeDef,
    ListConfigurationRevisionsResponseTypeDef,
    ListConfigurationsRequestPaginateTypeDef,
    ListConfigurationsResponseTypeDef,
    ListKafkaVersionsRequestPaginateTypeDef,
    ListKafkaVersionsResponseTypeDef,
    ListNodesRequestPaginateTypeDef,
    ListNodesResponseTypeDef,
    ListReplicatorsRequestPaginateTypeDef,
    ListReplicatorsResponseTypeDef,
    ListScramSecretsRequestPaginateTypeDef,
    ListScramSecretsResponseTypeDef,
    ListVpcConnectionsRequestPaginateTypeDef,
    ListVpcConnectionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
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
    "ListVpcConnectionsPaginator",
)

if TYPE_CHECKING:
    _ListClientVpcConnectionsPaginatorBase = Paginator[ListClientVpcConnectionsResponseTypeDef]
else:
    _ListClientVpcConnectionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListClientVpcConnectionsPaginator(_ListClientVpcConnectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListClientVpcConnections.html#Kafka.Paginator.ListClientVpcConnections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listclientvpcconnectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListClientVpcConnectionsRequestPaginateTypeDef]
    ) -> PageIterator[ListClientVpcConnectionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListClientVpcConnections.html#Kafka.Paginator.ListClientVpcConnections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listclientvpcconnectionspaginator)
        """

if TYPE_CHECKING:
    _ListClusterOperationsPaginatorBase = Paginator[ListClusterOperationsResponseTypeDef]
else:
    _ListClusterOperationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListClusterOperationsPaginator(_ListClusterOperationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListClusterOperations.html#Kafka.Paginator.ListClusterOperations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listclusteroperationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListClusterOperationsRequestPaginateTypeDef]
    ) -> PageIterator[ListClusterOperationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListClusterOperations.html#Kafka.Paginator.ListClusterOperations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listclusteroperationspaginator)
        """

if TYPE_CHECKING:
    _ListClusterOperationsV2PaginatorBase = Paginator[ListClusterOperationsV2ResponseTypeDef]
else:
    _ListClusterOperationsV2PaginatorBase = Paginator  # type: ignore[assignment]

class ListClusterOperationsV2Paginator(_ListClusterOperationsV2PaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListClusterOperationsV2.html#Kafka.Paginator.ListClusterOperationsV2)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listclusteroperationsv2paginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListClusterOperationsV2RequestPaginateTypeDef]
    ) -> PageIterator[ListClusterOperationsV2ResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListClusterOperationsV2.html#Kafka.Paginator.ListClusterOperationsV2.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listclusteroperationsv2paginator)
        """

if TYPE_CHECKING:
    _ListClustersPaginatorBase = Paginator[ListClustersResponseTypeDef]
else:
    _ListClustersPaginatorBase = Paginator  # type: ignore[assignment]

class ListClustersPaginator(_ListClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListClusters.html#Kafka.Paginator.ListClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListClustersRequestPaginateTypeDef]
    ) -> PageIterator[ListClustersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListClusters.html#Kafka.Paginator.ListClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listclusterspaginator)
        """

if TYPE_CHECKING:
    _ListClustersV2PaginatorBase = Paginator[ListClustersV2ResponseTypeDef]
else:
    _ListClustersV2PaginatorBase = Paginator  # type: ignore[assignment]

class ListClustersV2Paginator(_ListClustersV2PaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListClustersV2.html#Kafka.Paginator.ListClustersV2)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listclustersv2paginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListClustersV2RequestPaginateTypeDef]
    ) -> PageIterator[ListClustersV2ResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListClustersV2.html#Kafka.Paginator.ListClustersV2.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listclustersv2paginator)
        """

if TYPE_CHECKING:
    _ListConfigurationRevisionsPaginatorBase = Paginator[ListConfigurationRevisionsResponseTypeDef]
else:
    _ListConfigurationRevisionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConfigurationRevisionsPaginator(_ListConfigurationRevisionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListConfigurationRevisions.html#Kafka.Paginator.ListConfigurationRevisions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listconfigurationrevisionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConfigurationRevisionsRequestPaginateTypeDef]
    ) -> PageIterator[ListConfigurationRevisionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListConfigurationRevisions.html#Kafka.Paginator.ListConfigurationRevisions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listconfigurationrevisionspaginator)
        """

if TYPE_CHECKING:
    _ListConfigurationsPaginatorBase = Paginator[ListConfigurationsResponseTypeDef]
else:
    _ListConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConfigurationsPaginator(_ListConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListConfigurations.html#Kafka.Paginator.ListConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListConfigurations.html#Kafka.Paginator.ListConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListKafkaVersionsPaginatorBase = Paginator[ListKafkaVersionsResponseTypeDef]
else:
    _ListKafkaVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListKafkaVersionsPaginator(_ListKafkaVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListKafkaVersions.html#Kafka.Paginator.ListKafkaVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listkafkaversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListKafkaVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListKafkaVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListKafkaVersions.html#Kafka.Paginator.ListKafkaVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listkafkaversionspaginator)
        """

if TYPE_CHECKING:
    _ListNodesPaginatorBase = Paginator[ListNodesResponseTypeDef]
else:
    _ListNodesPaginatorBase = Paginator  # type: ignore[assignment]

class ListNodesPaginator(_ListNodesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListNodes.html#Kafka.Paginator.ListNodes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listnodespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNodesRequestPaginateTypeDef]
    ) -> PageIterator[ListNodesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListNodes.html#Kafka.Paginator.ListNodes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listnodespaginator)
        """

if TYPE_CHECKING:
    _ListReplicatorsPaginatorBase = Paginator[ListReplicatorsResponseTypeDef]
else:
    _ListReplicatorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListReplicatorsPaginator(_ListReplicatorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListReplicators.html#Kafka.Paginator.ListReplicators)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listreplicatorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReplicatorsRequestPaginateTypeDef]
    ) -> PageIterator[ListReplicatorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListReplicators.html#Kafka.Paginator.ListReplicators.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listreplicatorspaginator)
        """

if TYPE_CHECKING:
    _ListScramSecretsPaginatorBase = Paginator[ListScramSecretsResponseTypeDef]
else:
    _ListScramSecretsPaginatorBase = Paginator  # type: ignore[assignment]

class ListScramSecretsPaginator(_ListScramSecretsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListScramSecrets.html#Kafka.Paginator.ListScramSecrets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listscramsecretspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListScramSecretsRequestPaginateTypeDef]
    ) -> PageIterator[ListScramSecretsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListScramSecrets.html#Kafka.Paginator.ListScramSecrets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listscramsecretspaginator)
        """

if TYPE_CHECKING:
    _ListVpcConnectionsPaginatorBase = Paginator[ListVpcConnectionsResponseTypeDef]
else:
    _ListVpcConnectionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListVpcConnectionsPaginator(_ListVpcConnectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListVpcConnections.html#Kafka.Paginator.ListVpcConnections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listvpcconnectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListVpcConnectionsRequestPaginateTypeDef]
    ) -> PageIterator[ListVpcConnectionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/paginator/ListVpcConnections.html#Kafka.Paginator.ListVpcConnections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/paginators/#listvpcconnectionspaginator)
        """
