# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for kafka service client

Usage::

    ```python
    import boto3
    from mypy_boto3_kafka import KafkaClient

    client: KafkaClient = boto3.client("kafka")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_kafka.paginator import (
    ListClusterOperationsPaginator,
    ListClustersPaginator,
    ListConfigurationRevisionsPaginator,
    ListConfigurationsPaginator,
    ListKafkaVersionsPaginator,
    ListNodesPaginator,
)
from mypy_boto3_kafka.type_defs import (
    BrokerEBSVolumeInfoTypeDef,
    BrokerNodeGroupInfoTypeDef,
    ClientAuthenticationTypeDef,
    ConfigurationInfoTypeDef,
    CreateClusterResponseTypeDef,
    CreateConfigurationResponseTypeDef,
    DeleteClusterResponseTypeDef,
    DescribeClusterOperationResponseTypeDef,
    DescribeClusterResponseTypeDef,
    DescribeConfigurationResponseTypeDef,
    DescribeConfigurationRevisionResponseTypeDef,
    EncryptionInfoTypeDef,
    GetBootstrapBrokersResponseTypeDef,
    GetCompatibleKafkaVersionsResponseTypeDef,
    ListClusterOperationsResponseTypeDef,
    ListClustersResponseTypeDef,
    ListConfigurationRevisionsResponseTypeDef,
    ListConfigurationsResponseTypeDef,
    ListKafkaVersionsResponseTypeDef,
    ListNodesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggingInfoTypeDef,
    OpenMonitoringInfoTypeDef,
    RebootBrokerResponseTypeDef,
    UpdateBrokerCountResponseTypeDef,
    UpdateBrokerStorageResponseTypeDef,
    UpdateClusterConfigurationResponseTypeDef,
    UpdateClusterKafkaVersionResponseTypeDef,
    UpdateMonitoringResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("KafkaClient",)


class Exceptions:
    BadRequestException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    ConflictException: Type[Boto3ClientError]
    ForbiddenException: Type[Boto3ClientError]
    InternalServerErrorException: Type[Boto3ClientError]
    NotFoundException: Type[Boto3ClientError]
    ServiceUnavailableException: Type[Boto3ClientError]
    TooManyRequestsException: Type[Boto3ClientError]
    UnauthorizedException: Type[Boto3ClientError]


class KafkaClient:
    """
    [Kafka.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.can_paginate)
        """

    def create_cluster(
        self,
        BrokerNodeGroupInfo: "BrokerNodeGroupInfoTypeDef",
        ClusterName: str,
        KafkaVersion: str,
        NumberOfBrokerNodes: int,
        ClientAuthentication: "ClientAuthenticationTypeDef" = None,
        ConfigurationInfo: "ConfigurationInfoTypeDef" = None,
        EncryptionInfo: "EncryptionInfoTypeDef" = None,
        EnhancedMonitoring: Literal["DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER"] = None,
        OpenMonitoring: OpenMonitoringInfoTypeDef = None,
        LoggingInfo: "LoggingInfoTypeDef" = None,
        Tags: Dict[str, str] = None,
    ) -> CreateClusterResponseTypeDef:
        """
        [Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.create_cluster)
        """

    def create_configuration(
        self,
        Name: str,
        ServerProperties: Union[bytes, IO[bytes]],
        Description: str = None,
        KafkaVersions: List[str] = None,
    ) -> CreateConfigurationResponseTypeDef:
        """
        [Client.create_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.create_configuration)
        """

    def delete_cluster(
        self, ClusterArn: str, CurrentVersion: str = None
    ) -> DeleteClusterResponseTypeDef:
        """
        [Client.delete_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.delete_cluster)
        """

    def describe_cluster(self, ClusterArn: str) -> DescribeClusterResponseTypeDef:
        """
        [Client.describe_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.describe_cluster)
        """

    def describe_cluster_operation(
        self, ClusterOperationArn: str
    ) -> DescribeClusterOperationResponseTypeDef:
        """
        [Client.describe_cluster_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.describe_cluster_operation)
        """

    def describe_configuration(self, Arn: str) -> DescribeConfigurationResponseTypeDef:
        """
        [Client.describe_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.describe_configuration)
        """

    def describe_configuration_revision(
        self, Arn: str, Revision: int
    ) -> DescribeConfigurationRevisionResponseTypeDef:
        """
        [Client.describe_configuration_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.describe_configuration_revision)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.generate_presigned_url)
        """

    def get_bootstrap_brokers(self, ClusterArn: str) -> GetBootstrapBrokersResponseTypeDef:
        """
        [Client.get_bootstrap_brokers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.get_bootstrap_brokers)
        """

    def get_compatible_kafka_versions(
        self, ClusterArn: str = None
    ) -> GetCompatibleKafkaVersionsResponseTypeDef:
        """
        [Client.get_compatible_kafka_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.get_compatible_kafka_versions)
        """

    def list_cluster_operations(
        self, ClusterArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListClusterOperationsResponseTypeDef:
        """
        [Client.list_cluster_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.list_cluster_operations)
        """

    def list_clusters(
        self, ClusterNameFilter: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListClustersResponseTypeDef:
        """
        [Client.list_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.list_clusters)
        """

    def list_configuration_revisions(
        self, Arn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListConfigurationRevisionsResponseTypeDef:
        """
        [Client.list_configuration_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.list_configuration_revisions)
        """

    def list_configurations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListConfigurationsResponseTypeDef:
        """
        [Client.list_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.list_configurations)
        """

    def list_kafka_versions(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListKafkaVersionsResponseTypeDef:
        """
        [Client.list_kafka_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.list_kafka_versions)
        """

    def list_nodes(
        self, ClusterArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListNodesResponseTypeDef:
        """
        [Client.list_nodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.list_nodes)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.list_tags_for_resource)
        """

    def reboot_broker(self, BrokerIds: List[str], ClusterArn: str) -> RebootBrokerResponseTypeDef:
        """
        [Client.reboot_broker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.reboot_broker)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.untag_resource)
        """

    def update_broker_count(
        self, ClusterArn: str, CurrentVersion: str, TargetNumberOfBrokerNodes: int
    ) -> UpdateBrokerCountResponseTypeDef:
        """
        [Client.update_broker_count documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.update_broker_count)
        """

    def update_broker_storage(
        self,
        ClusterArn: str,
        CurrentVersion: str,
        TargetBrokerEBSVolumeInfo: List["BrokerEBSVolumeInfoTypeDef"],
    ) -> UpdateBrokerStorageResponseTypeDef:
        """
        [Client.update_broker_storage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.update_broker_storage)
        """

    def update_cluster_configuration(
        self, ClusterArn: str, ConfigurationInfo: "ConfigurationInfoTypeDef", CurrentVersion: str
    ) -> UpdateClusterConfigurationResponseTypeDef:
        """
        [Client.update_cluster_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.update_cluster_configuration)
        """

    def update_cluster_kafka_version(
        self,
        ClusterArn: str,
        CurrentVersion: str,
        TargetKafkaVersion: str,
        ConfigurationInfo: "ConfigurationInfoTypeDef" = None,
    ) -> UpdateClusterKafkaVersionResponseTypeDef:
        """
        [Client.update_cluster_kafka_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.update_cluster_kafka_version)
        """

    def update_monitoring(
        self,
        ClusterArn: str,
        CurrentVersion: str,
        EnhancedMonitoring: Literal["DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER"] = None,
        OpenMonitoring: OpenMonitoringInfoTypeDef = None,
        LoggingInfo: "LoggingInfoTypeDef" = None,
    ) -> UpdateMonitoringResponseTypeDef:
        """
        [Client.update_monitoring documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Client.update_monitoring)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_cluster_operations"]
    ) -> ListClusterOperationsPaginator:
        """
        [Paginator.ListClusterOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Paginator.ListClusterOperations)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_clusters"]) -> ListClustersPaginator:
        """
        [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Paginator.ListClusters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configuration_revisions"]
    ) -> ListConfigurationRevisionsPaginator:
        """
        [Paginator.ListConfigurationRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Paginator.ListConfigurationRevisions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configurations"]
    ) -> ListConfigurationsPaginator:
        """
        [Paginator.ListConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Paginator.ListConfigurations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_kafka_versions"]
    ) -> ListKafkaVersionsPaginator:
        """
        [Paginator.ListKafkaVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Paginator.ListKafkaVersions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_nodes"]) -> ListNodesPaginator:
        """
        [Paginator.ListNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kafka.html#Kafka.Paginator.ListNodes)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
