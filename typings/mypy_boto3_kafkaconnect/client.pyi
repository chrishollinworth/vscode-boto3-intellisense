"""
Type annotations for kafkaconnect service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_kafkaconnect import KafkaConnectClient

    client: KafkaConnectClient = boto3.client("kafkaconnect")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import CustomPluginContentTypeType
from .paginator import (
    ListConnectorsPaginator,
    ListCustomPluginsPaginator,
    ListWorkerConfigurationsPaginator,
)
from .type_defs import (
    CapacityTypeDef,
    CapacityUpdateTypeDef,
    CreateConnectorResponseTypeDef,
    CreateCustomPluginResponseTypeDef,
    CreateWorkerConfigurationResponseTypeDef,
    CustomPluginLocationTypeDef,
    DeleteConnectorResponseTypeDef,
    DeleteCustomPluginResponseTypeDef,
    DescribeConnectorResponseTypeDef,
    DescribeCustomPluginResponseTypeDef,
    DescribeWorkerConfigurationResponseTypeDef,
    KafkaClusterClientAuthenticationTypeDef,
    KafkaClusterEncryptionInTransitTypeDef,
    KafkaClusterTypeDef,
    ListConnectorsResponseTypeDef,
    ListCustomPluginsResponseTypeDef,
    ListWorkerConfigurationsResponseTypeDef,
    LogDeliveryTypeDef,
    PluginTypeDef,
    UpdateConnectorResponseTypeDef,
    WorkerConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("KafkaConnectClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]

class KafkaConnectClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kafkaconnect.html#KafkaConnect.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KafkaConnectClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kafkaconnect.html#KafkaConnect.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client.html#can_paginate)
        """
    def create_connector(
        self,
        *,
        capacity: "CapacityTypeDef",
        connectorConfiguration: Dict[str, str],
        connectorName: str,
        kafkaCluster: "KafkaClusterTypeDef",
        kafkaClusterClientAuthentication: "KafkaClusterClientAuthenticationTypeDef",
        kafkaClusterEncryptionInTransit: "KafkaClusterEncryptionInTransitTypeDef",
        kafkaConnectVersion: str,
        plugins: List["PluginTypeDef"],
        serviceExecutionRoleArn: str,
        connectorDescription: str = None,
        logDelivery: "LogDeliveryTypeDef" = None,
        workerConfiguration: "WorkerConfigurationTypeDef" = None
    ) -> CreateConnectorResponseTypeDef:
        """
        Creates a connector using the specified properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kafkaconnect.html#KafkaConnect.Client.create_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client.html#create_connector)
        """
    def create_custom_plugin(
        self,
        *,
        contentType: CustomPluginContentTypeType,
        location: "CustomPluginLocationTypeDef",
        name: str,
        description: str = None
    ) -> CreateCustomPluginResponseTypeDef:
        """
        Creates a custom plugin using the specified properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kafkaconnect.html#KafkaConnect.Client.create_custom_plugin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client.html#create_custom_plugin)
        """
    def create_worker_configuration(
        self, *, name: str, propertiesFileContent: str, description: str = None
    ) -> CreateWorkerConfigurationResponseTypeDef:
        """
        Creates a worker configuration using the specified properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kafkaconnect.html#KafkaConnect.Client.create_worker_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client.html#create_worker_configuration)
        """
    def delete_connector(
        self, *, connectorArn: str, currentVersion: str = None
    ) -> DeleteConnectorResponseTypeDef:
        """
        Deletes the specified connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kafkaconnect.html#KafkaConnect.Client.delete_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client.html#delete_connector)
        """
    def delete_custom_plugin(self, *, customPluginArn: str) -> DeleteCustomPluginResponseTypeDef:
        """
        Deletes a custom plugin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kafkaconnect.html#KafkaConnect.Client.delete_custom_plugin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client.html#delete_custom_plugin)
        """
    def describe_connector(self, *, connectorArn: str) -> DescribeConnectorResponseTypeDef:
        """
        Returns summary information about the connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kafkaconnect.html#KafkaConnect.Client.describe_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client.html#describe_connector)
        """
    def describe_custom_plugin(
        self, *, customPluginArn: str
    ) -> DescribeCustomPluginResponseTypeDef:
        """
        A summary description of the custom plugin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kafkaconnect.html#KafkaConnect.Client.describe_custom_plugin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client.html#describe_custom_plugin)
        """
    def describe_worker_configuration(
        self, *, workerConfigurationArn: str
    ) -> DescribeWorkerConfigurationResponseTypeDef:
        """
        Returns information about a worker configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kafkaconnect.html#KafkaConnect.Client.describe_worker_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client.html#describe_worker_configuration)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kafkaconnect.html#KafkaConnect.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client.html#generate_presigned_url)
        """
    def list_connectors(
        self, *, connectorNamePrefix: str = None, maxResults: int = None, nextToken: str = None
    ) -> ListConnectorsResponseTypeDef:
        """
        Returns a list of all the connectors in this account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kafkaconnect.html#KafkaConnect.Client.list_connectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client.html#list_connectors)
        """
    def list_custom_plugins(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListCustomPluginsResponseTypeDef:
        """
        Returns a list of all of the custom plugins in this account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kafkaconnect.html#KafkaConnect.Client.list_custom_plugins)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client.html#list_custom_plugins)
        """
    def list_worker_configurations(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListWorkerConfigurationsResponseTypeDef:
        """
        Returns a list of all of the worker configurations in this account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kafkaconnect.html#KafkaConnect.Client.list_worker_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client.html#list_worker_configurations)
        """
    def update_connector(
        self, *, capacity: "CapacityUpdateTypeDef", connectorArn: str, currentVersion: str
    ) -> UpdateConnectorResponseTypeDef:
        """
        Updates the specified connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kafkaconnect.html#KafkaConnect.Client.update_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/client.html#update_connector)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_connectors"]) -> ListConnectorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kafkaconnect.html#KafkaConnect.Paginator.ListConnectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/paginators.html#listconnectorspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_plugins"]
    ) -> ListCustomPluginsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kafkaconnect.html#KafkaConnect.Paginator.ListCustomPlugins)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/paginators.html#listcustompluginspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_worker_configurations"]
    ) -> ListWorkerConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kafkaconnect.html#KafkaConnect.Paginator.ListWorkerConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/paginators.html#listworkerconfigurationspaginator)
        """
