"""
Type annotations for kafka service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_kafka.client import KafkaClient

    session = Session()
    client: KafkaClient = session.client("kafka")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
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
from .type_defs import (
    BatchAssociateScramSecretRequestTypeDef,
    BatchAssociateScramSecretResponseTypeDef,
    BatchDisassociateScramSecretRequestTypeDef,
    BatchDisassociateScramSecretResponseTypeDef,
    CreateClusterRequestTypeDef,
    CreateClusterResponseTypeDef,
    CreateClusterV2RequestTypeDef,
    CreateClusterV2ResponseTypeDef,
    CreateConfigurationRequestTypeDef,
    CreateConfigurationResponseTypeDef,
    CreateReplicatorRequestTypeDef,
    CreateReplicatorResponseTypeDef,
    CreateVpcConnectionRequestTypeDef,
    CreateVpcConnectionResponseTypeDef,
    DeleteClusterPolicyRequestTypeDef,
    DeleteClusterRequestTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteConfigurationRequestTypeDef,
    DeleteConfigurationResponseTypeDef,
    DeleteReplicatorRequestTypeDef,
    DeleteReplicatorResponseTypeDef,
    DeleteVpcConnectionRequestTypeDef,
    DeleteVpcConnectionResponseTypeDef,
    DescribeClusterOperationRequestTypeDef,
    DescribeClusterOperationResponseTypeDef,
    DescribeClusterOperationV2RequestTypeDef,
    DescribeClusterOperationV2ResponseTypeDef,
    DescribeClusterRequestTypeDef,
    DescribeClusterResponseTypeDef,
    DescribeClusterV2RequestTypeDef,
    DescribeClusterV2ResponseTypeDef,
    DescribeConfigurationRequestTypeDef,
    DescribeConfigurationResponseTypeDef,
    DescribeConfigurationRevisionRequestTypeDef,
    DescribeConfigurationRevisionResponseTypeDef,
    DescribeReplicatorRequestTypeDef,
    DescribeReplicatorResponseTypeDef,
    DescribeVpcConnectionRequestTypeDef,
    DescribeVpcConnectionResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetBootstrapBrokersRequestTypeDef,
    GetBootstrapBrokersResponseTypeDef,
    GetClusterPolicyRequestTypeDef,
    GetClusterPolicyResponseTypeDef,
    GetCompatibleKafkaVersionsRequestTypeDef,
    GetCompatibleKafkaVersionsResponseTypeDef,
    ListClientVpcConnectionsRequestTypeDef,
    ListClientVpcConnectionsResponseTypeDef,
    ListClusterOperationsRequestTypeDef,
    ListClusterOperationsResponseTypeDef,
    ListClusterOperationsV2RequestTypeDef,
    ListClusterOperationsV2ResponseTypeDef,
    ListClustersRequestTypeDef,
    ListClustersResponseTypeDef,
    ListClustersV2RequestTypeDef,
    ListClustersV2ResponseTypeDef,
    ListConfigurationRevisionsRequestTypeDef,
    ListConfigurationRevisionsResponseTypeDef,
    ListConfigurationsRequestTypeDef,
    ListConfigurationsResponseTypeDef,
    ListKafkaVersionsRequestTypeDef,
    ListKafkaVersionsResponseTypeDef,
    ListNodesRequestTypeDef,
    ListNodesResponseTypeDef,
    ListReplicatorsRequestTypeDef,
    ListReplicatorsResponseTypeDef,
    ListScramSecretsRequestTypeDef,
    ListScramSecretsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVpcConnectionsRequestTypeDef,
    ListVpcConnectionsResponseTypeDef,
    PutClusterPolicyRequestTypeDef,
    PutClusterPolicyResponseTypeDef,
    RebootBrokerRequestTypeDef,
    RebootBrokerResponseTypeDef,
    RejectClientVpcConnectionRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateBrokerCountRequestTypeDef,
    UpdateBrokerCountResponseTypeDef,
    UpdateBrokerStorageRequestTypeDef,
    UpdateBrokerStorageResponseTypeDef,
    UpdateBrokerTypeRequestTypeDef,
    UpdateBrokerTypeResponseTypeDef,
    UpdateClusterConfigurationRequestTypeDef,
    UpdateClusterConfigurationResponseTypeDef,
    UpdateClusterKafkaVersionRequestTypeDef,
    UpdateClusterKafkaVersionResponseTypeDef,
    UpdateConfigurationRequestTypeDef,
    UpdateConfigurationResponseTypeDef,
    UpdateConnectivityRequestTypeDef,
    UpdateConnectivityResponseTypeDef,
    UpdateMonitoringRequestTypeDef,
    UpdateMonitoringResponseTypeDef,
    UpdateReplicationInfoRequestTypeDef,
    UpdateReplicationInfoResponseTypeDef,
    UpdateSecurityRequestTypeDef,
    UpdateSecurityResponseTypeDef,
    UpdateStorageRequestTypeDef,
    UpdateStorageResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("KafkaClient",)

class Exceptions(BaseClientExceptions):
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]

class KafkaClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KafkaClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#generate_presigned_url)
        """

    def batch_associate_scram_secret(
        self, **kwargs: Unpack[BatchAssociateScramSecretRequestTypeDef]
    ) -> BatchAssociateScramSecretResponseTypeDef:
        """
        Associates one or more Scram Secrets with an Amazon MSK cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/batch_associate_scram_secret.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#batch_associate_scram_secret)
        """

    def create_cluster(
        self, **kwargs: Unpack[CreateClusterRequestTypeDef]
    ) -> CreateClusterResponseTypeDef:
        """
        Creates a new MSK cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/create_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#create_cluster)
        """

    def create_cluster_v2(
        self, **kwargs: Unpack[CreateClusterV2RequestTypeDef]
    ) -> CreateClusterV2ResponseTypeDef:
        """
        Creates a new MSK cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/create_cluster_v2.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#create_cluster_v2)
        """

    def create_configuration(
        self, **kwargs: Unpack[CreateConfigurationRequestTypeDef]
    ) -> CreateConfigurationResponseTypeDef:
        """
        Creates a new MSK configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/create_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#create_configuration)
        """

    def create_replicator(
        self, **kwargs: Unpack[CreateReplicatorRequestTypeDef]
    ) -> CreateReplicatorResponseTypeDef:
        """
        Creates the replicator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/create_replicator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#create_replicator)
        """

    def create_vpc_connection(
        self, **kwargs: Unpack[CreateVpcConnectionRequestTypeDef]
    ) -> CreateVpcConnectionResponseTypeDef:
        """
        Creates a new MSK VPC connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/create_vpc_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#create_vpc_connection)
        """

    def delete_cluster(
        self, **kwargs: Unpack[DeleteClusterRequestTypeDef]
    ) -> DeleteClusterResponseTypeDef:
        """
        Deletes the MSK cluster specified by the Amazon Resource Name (ARN) in the
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/delete_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#delete_cluster)
        """

    def delete_cluster_policy(
        self, **kwargs: Unpack[DeleteClusterPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the MSK cluster policy specified by the Amazon Resource Name (ARN) in
        the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/delete_cluster_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#delete_cluster_policy)
        """

    def delete_configuration(
        self, **kwargs: Unpack[DeleteConfigurationRequestTypeDef]
    ) -> DeleteConfigurationResponseTypeDef:
        """
        Deletes an MSK Configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/delete_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#delete_configuration)
        """

    def delete_replicator(
        self, **kwargs: Unpack[DeleteReplicatorRequestTypeDef]
    ) -> DeleteReplicatorResponseTypeDef:
        """
        Deletes a replicator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/delete_replicator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#delete_replicator)
        """

    def delete_vpc_connection(
        self, **kwargs: Unpack[DeleteVpcConnectionRequestTypeDef]
    ) -> DeleteVpcConnectionResponseTypeDef:
        """
        Deletes a MSK VPC connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/delete_vpc_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#delete_vpc_connection)
        """

    def describe_cluster(
        self, **kwargs: Unpack[DescribeClusterRequestTypeDef]
    ) -> DescribeClusterResponseTypeDef:
        """
        Returns a description of the MSK cluster whose Amazon Resource Name (ARN) is
        specified in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/describe_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#describe_cluster)
        """

    def describe_cluster_v2(
        self, **kwargs: Unpack[DescribeClusterV2RequestTypeDef]
    ) -> DescribeClusterV2ResponseTypeDef:
        """
        Returns a description of the MSK cluster whose Amazon Resource Name (ARN) is
        specified in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/describe_cluster_v2.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#describe_cluster_v2)
        """

    def describe_cluster_operation(
        self, **kwargs: Unpack[DescribeClusterOperationRequestTypeDef]
    ) -> DescribeClusterOperationResponseTypeDef:
        """
        Returns a description of the cluster operation specified by the ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/describe_cluster_operation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#describe_cluster_operation)
        """

    def describe_cluster_operation_v2(
        self, **kwargs: Unpack[DescribeClusterOperationV2RequestTypeDef]
    ) -> DescribeClusterOperationV2ResponseTypeDef:
        """
        Returns a description of the cluster operation specified by the ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/describe_cluster_operation_v2.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#describe_cluster_operation_v2)
        """

    def describe_configuration(
        self, **kwargs: Unpack[DescribeConfigurationRequestTypeDef]
    ) -> DescribeConfigurationResponseTypeDef:
        """
        Returns a description of this MSK configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/describe_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#describe_configuration)
        """

    def describe_configuration_revision(
        self, **kwargs: Unpack[DescribeConfigurationRevisionRequestTypeDef]
    ) -> DescribeConfigurationRevisionResponseTypeDef:
        """
        Returns a description of this revision of the configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/describe_configuration_revision.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#describe_configuration_revision)
        """

    def describe_replicator(
        self, **kwargs: Unpack[DescribeReplicatorRequestTypeDef]
    ) -> DescribeReplicatorResponseTypeDef:
        """
        Describes a replicator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/describe_replicator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#describe_replicator)
        """

    def describe_vpc_connection(
        self, **kwargs: Unpack[DescribeVpcConnectionRequestTypeDef]
    ) -> DescribeVpcConnectionResponseTypeDef:
        """
        Returns a description of this MSK VPC connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/describe_vpc_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#describe_vpc_connection)
        """

    def batch_disassociate_scram_secret(
        self, **kwargs: Unpack[BatchDisassociateScramSecretRequestTypeDef]
    ) -> BatchDisassociateScramSecretResponseTypeDef:
        """
        Disassociates one or more Scram Secrets from an Amazon MSK cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/batch_disassociate_scram_secret.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#batch_disassociate_scram_secret)
        """

    def get_bootstrap_brokers(
        self, **kwargs: Unpack[GetBootstrapBrokersRequestTypeDef]
    ) -> GetBootstrapBrokersResponseTypeDef:
        """
        A list of brokers that a client application can use to bootstrap.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/get_bootstrap_brokers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#get_bootstrap_brokers)
        """

    def get_compatible_kafka_versions(
        self, **kwargs: Unpack[GetCompatibleKafkaVersionsRequestTypeDef]
    ) -> GetCompatibleKafkaVersionsResponseTypeDef:
        """
        Gets the Apache Kafka versions to which you can update the MSK cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/get_compatible_kafka_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#get_compatible_kafka_versions)
        """

    def get_cluster_policy(
        self, **kwargs: Unpack[GetClusterPolicyRequestTypeDef]
    ) -> GetClusterPolicyResponseTypeDef:
        """
        Get the MSK cluster policy specified by the Amazon Resource Name (ARN) in the
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/get_cluster_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#get_cluster_policy)
        """

    def list_cluster_operations(
        self, **kwargs: Unpack[ListClusterOperationsRequestTypeDef]
    ) -> ListClusterOperationsResponseTypeDef:
        """
        Returns a list of all the operations that have been performed on the specified
        MSK cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/list_cluster_operations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#list_cluster_operations)
        """

    def list_cluster_operations_v2(
        self, **kwargs: Unpack[ListClusterOperationsV2RequestTypeDef]
    ) -> ListClusterOperationsV2ResponseTypeDef:
        """
        Returns a list of all the operations that have been performed on the specified
        MSK cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/list_cluster_operations_v2.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#list_cluster_operations_v2)
        """

    def list_clusters(
        self, **kwargs: Unpack[ListClustersRequestTypeDef]
    ) -> ListClustersResponseTypeDef:
        """
        Returns a list of all the MSK clusters in the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/list_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#list_clusters)
        """

    def list_clusters_v2(
        self, **kwargs: Unpack[ListClustersV2RequestTypeDef]
    ) -> ListClustersV2ResponseTypeDef:
        """
        Returns a list of all the MSK clusters in the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/list_clusters_v2.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#list_clusters_v2)
        """

    def list_configuration_revisions(
        self, **kwargs: Unpack[ListConfigurationRevisionsRequestTypeDef]
    ) -> ListConfigurationRevisionsResponseTypeDef:
        """
        Returns a list of all the MSK configurations in this Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/list_configuration_revisions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#list_configuration_revisions)
        """

    def list_configurations(
        self, **kwargs: Unpack[ListConfigurationsRequestTypeDef]
    ) -> ListConfigurationsResponseTypeDef:
        """
        Returns a list of all the MSK configurations in this Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/list_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#list_configurations)
        """

    def list_kafka_versions(
        self, **kwargs: Unpack[ListKafkaVersionsRequestTypeDef]
    ) -> ListKafkaVersionsResponseTypeDef:
        """
        Returns a list of Apache Kafka versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/list_kafka_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#list_kafka_versions)
        """

    def list_nodes(self, **kwargs: Unpack[ListNodesRequestTypeDef]) -> ListNodesResponseTypeDef:
        """
        Returns a list of the broker nodes in the cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/list_nodes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#list_nodes)
        """

    def list_replicators(
        self, **kwargs: Unpack[ListReplicatorsRequestTypeDef]
    ) -> ListReplicatorsResponseTypeDef:
        """
        Lists the replicators.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/list_replicators.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#list_replicators)
        """

    def list_scram_secrets(
        self, **kwargs: Unpack[ListScramSecretsRequestTypeDef]
    ) -> ListScramSecretsResponseTypeDef:
        """
        Returns a list of the Scram Secrets associated with an Amazon MSK cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/list_scram_secrets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#list_scram_secrets)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of the tags associated with the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#list_tags_for_resource)
        """

    def list_client_vpc_connections(
        self, **kwargs: Unpack[ListClientVpcConnectionsRequestTypeDef]
    ) -> ListClientVpcConnectionsResponseTypeDef:
        """
        Returns a list of all the VPC connections in this Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/list_client_vpc_connections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#list_client_vpc_connections)
        """

    def list_vpc_connections(
        self, **kwargs: Unpack[ListVpcConnectionsRequestTypeDef]
    ) -> ListVpcConnectionsResponseTypeDef:
        """
        Returns a list of all the VPC connections in this Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/list_vpc_connections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#list_vpc_connections)
        """

    def reject_client_vpc_connection(
        self, **kwargs: Unpack[RejectClientVpcConnectionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Returns empty response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/reject_client_vpc_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#reject_client_vpc_connection)
        """

    def put_cluster_policy(
        self, **kwargs: Unpack[PutClusterPolicyRequestTypeDef]
    ) -> PutClusterPolicyResponseTypeDef:
        """
        Creates or updates the MSK cluster policy specified by the cluster Amazon
        Resource Name (ARN) in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/put_cluster_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#put_cluster_policy)
        """

    def reboot_broker(
        self, **kwargs: Unpack[RebootBrokerRequestTypeDef]
    ) -> RebootBrokerResponseTypeDef:
        """
        Reboots brokers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/reboot_broker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#reboot_broker)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds tags to the specified MSK resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the tags associated with the keys that are provided in the query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#untag_resource)
        """

    def update_broker_count(
        self, **kwargs: Unpack[UpdateBrokerCountRequestTypeDef]
    ) -> UpdateBrokerCountResponseTypeDef:
        """
        Updates the number of broker nodes in the cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/update_broker_count.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#update_broker_count)
        """

    def update_broker_type(
        self, **kwargs: Unpack[UpdateBrokerTypeRequestTypeDef]
    ) -> UpdateBrokerTypeResponseTypeDef:
        """
        Updates EC2 instance type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/update_broker_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#update_broker_type)
        """

    def update_broker_storage(
        self, **kwargs: Unpack[UpdateBrokerStorageRequestTypeDef]
    ) -> UpdateBrokerStorageResponseTypeDef:
        """
        Updates the EBS storage associated with MSK brokers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/update_broker_storage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#update_broker_storage)
        """

    def update_configuration(
        self, **kwargs: Unpack[UpdateConfigurationRequestTypeDef]
    ) -> UpdateConfigurationResponseTypeDef:
        """
        Updates an MSK configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/update_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#update_configuration)
        """

    def update_connectivity(
        self, **kwargs: Unpack[UpdateConnectivityRequestTypeDef]
    ) -> UpdateConnectivityResponseTypeDef:
        """
        Updates the cluster's connectivity configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/update_connectivity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#update_connectivity)
        """

    def update_cluster_configuration(
        self, **kwargs: Unpack[UpdateClusterConfigurationRequestTypeDef]
    ) -> UpdateClusterConfigurationResponseTypeDef:
        """
        Updates the cluster with the configuration that is specified in the request
        body.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/update_cluster_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#update_cluster_configuration)
        """

    def update_cluster_kafka_version(
        self, **kwargs: Unpack[UpdateClusterKafkaVersionRequestTypeDef]
    ) -> UpdateClusterKafkaVersionResponseTypeDef:
        """
        Updates the Apache Kafka version for the cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/update_cluster_kafka_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#update_cluster_kafka_version)
        """

    def update_monitoring(
        self, **kwargs: Unpack[UpdateMonitoringRequestTypeDef]
    ) -> UpdateMonitoringResponseTypeDef:
        """
        Updates the monitoring settings for the cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/update_monitoring.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#update_monitoring)
        """

    def update_replication_info(
        self, **kwargs: Unpack[UpdateReplicationInfoRequestTypeDef]
    ) -> UpdateReplicationInfoResponseTypeDef:
        """
        Updates replication info of a replicator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/update_replication_info.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#update_replication_info)
        """

    def update_security(
        self, **kwargs: Unpack[UpdateSecurityRequestTypeDef]
    ) -> UpdateSecurityResponseTypeDef:
        """
        Updates the security settings for the cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/update_security.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#update_security)
        """

    def update_storage(
        self, **kwargs: Unpack[UpdateStorageRequestTypeDef]
    ) -> UpdateStorageResponseTypeDef:
        """
        Updates cluster broker volume size (or) sets cluster storage mode to TIERED.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/update_storage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#update_storage)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_client_vpc_connections"]
    ) -> ListClientVpcConnectionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_cluster_operations"]
    ) -> ListClusterOperationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_cluster_operations_v2"]
    ) -> ListClusterOperationsV2Paginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_clusters"]
    ) -> ListClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_clusters_v2"]
    ) -> ListClustersV2Paginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_configuration_revisions"]
    ) -> ListConfigurationRevisionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_configurations"]
    ) -> ListConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_kafka_versions"]
    ) -> ListKafkaVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_nodes"]
    ) -> ListNodesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_replicators"]
    ) -> ListReplicatorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_scram_secrets"]
    ) -> ListScramSecretsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_vpc_connections"]
    ) -> ListVpcConnectionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/client/#get_paginator)
        """
