"""
Type annotations for mq service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_mq import MQClient

    client: MQClient = boto3.client("mq")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AuthenticationStrategyType,
    BrokerStorageTypeType,
    DeploymentModeType,
    EngineTypeType,
)
from .paginator import ListBrokersPaginator
from .type_defs import (
    ConfigurationIdTypeDef,
    CreateBrokerResponseTypeDef,
    CreateConfigurationResponseTypeDef,
    DeleteBrokerResponseTypeDef,
    DescribeBrokerEngineTypesResponseTypeDef,
    DescribeBrokerInstanceOptionsResponseTypeDef,
    DescribeBrokerResponseTypeDef,
    DescribeConfigurationResponseTypeDef,
    DescribeConfigurationRevisionResponseTypeDef,
    DescribeUserResponseTypeDef,
    EncryptionOptionsTypeDef,
    LdapServerMetadataInputTypeDef,
    ListBrokersResponseTypeDef,
    ListConfigurationRevisionsResponseTypeDef,
    ListConfigurationsResponseTypeDef,
    ListTagsResponseTypeDef,
    ListUsersResponseTypeDef,
    LogsTypeDef,
    UpdateBrokerResponseTypeDef,
    UpdateConfigurationResponseTypeDef,
    UserTypeDef,
    WeeklyStartTimeTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("MQClient",)

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
    UnauthorizedException: Type[BotocoreClientError]

class MQClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MQClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#can_paginate)
        """
    def create_broker(
        self,
        *,
        AutoMinorVersionUpgrade: bool,
        BrokerName: str,
        DeploymentMode: DeploymentModeType,
        EngineType: EngineTypeType,
        EngineVersion: str,
        HostInstanceType: str,
        PubliclyAccessible: bool,
        Users: List["UserTypeDef"],
        AuthenticationStrategy: AuthenticationStrategyType = None,
        Configuration: "ConfigurationIdTypeDef" = None,
        CreatorRequestId: str = None,
        EncryptionOptions: "EncryptionOptionsTypeDef" = None,
        LdapServerMetadata: "LdapServerMetadataInputTypeDef" = None,
        Logs: "LogsTypeDef" = None,
        MaintenanceWindowStartTime: "WeeklyStartTimeTypeDef" = None,
        SecurityGroups: List[str] = None,
        StorageType: BrokerStorageTypeType = None,
        SubnetIds: List[str] = None,
        Tags: Dict[str, str] = None
    ) -> CreateBrokerResponseTypeDef:
        """
        Creates a broker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.create_broker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#create_broker)
        """
    def create_configuration(
        self,
        *,
        EngineType: EngineTypeType,
        EngineVersion: str,
        Name: str,
        AuthenticationStrategy: AuthenticationStrategyType = None,
        Tags: Dict[str, str] = None
    ) -> CreateConfigurationResponseTypeDef:
        """
        Creates a new configuration for the specified configuration name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.create_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#create_configuration)
        """
    def create_tags(self, *, ResourceArn: str, Tags: Dict[str, str] = None) -> None:
        """
        Add a tag to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#create_tags)
        """
    def create_user(
        self,
        *,
        BrokerId: str,
        Password: str,
        Username: str,
        ConsoleAccess: bool = None,
        Groups: List[str] = None
    ) -> Dict[str, Any]:
        """
        Creates an ActiveMQ user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#create_user)
        """
    def delete_broker(self, *, BrokerId: str) -> DeleteBrokerResponseTypeDef:
        """
        Deletes a broker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.delete_broker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#delete_broker)
        """
    def delete_tags(self, *, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        Removes a tag from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.delete_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#delete_tags)
        """
    def delete_user(self, *, BrokerId: str, Username: str) -> Dict[str, Any]:
        """
        Deletes an ActiveMQ user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#delete_user)
        """
    def describe_broker(self, *, BrokerId: str) -> DescribeBrokerResponseTypeDef:
        """
        Returns information about the specified broker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.describe_broker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#describe_broker)
        """
    def describe_broker_engine_types(
        self, *, EngineType: str = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeBrokerEngineTypesResponseTypeDef:
        """
        Describe available engine types and versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.describe_broker_engine_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#describe_broker_engine_types)
        """
    def describe_broker_instance_options(
        self,
        *,
        EngineType: str = None,
        HostInstanceType: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        StorageType: str = None
    ) -> DescribeBrokerInstanceOptionsResponseTypeDef:
        """
        Describe available broker instance options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.describe_broker_instance_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#describe_broker_instance_options)
        """
    def describe_configuration(
        self, *, ConfigurationId: str
    ) -> DescribeConfigurationResponseTypeDef:
        """
        Returns information about the specified configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.describe_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#describe_configuration)
        """
    def describe_configuration_revision(
        self, *, ConfigurationId: str, ConfigurationRevision: str
    ) -> DescribeConfigurationRevisionResponseTypeDef:
        """
        Returns the specified configuration revision for the specified configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.describe_configuration_revision)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#describe_configuration_revision)
        """
    def describe_user(self, *, BrokerId: str, Username: str) -> DescribeUserResponseTypeDef:
        """
        Returns information about an ActiveMQ user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.describe_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#describe_user)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#generate_presigned_url)
        """
    def list_brokers(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListBrokersResponseTypeDef:
        """
        Returns a list of all brokers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.list_brokers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#list_brokers)
        """
    def list_configuration_revisions(
        self, *, ConfigurationId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListConfigurationRevisionsResponseTypeDef:
        """
        Returns a list of all revisions for the specified configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.list_configuration_revisions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#list_configuration_revisions)
        """
    def list_configurations(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListConfigurationsResponseTypeDef:
        """
        Returns a list of all configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.list_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#list_configurations)
        """
    def list_tags(self, *, ResourceArn: str) -> ListTagsResponseTypeDef:
        """
        Lists tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.list_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#list_tags)
        """
    def list_users(
        self, *, BrokerId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListUsersResponseTypeDef:
        """
        Returns a list of all ActiveMQ users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.list_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#list_users)
        """
    def reboot_broker(self, *, BrokerId: str) -> Dict[str, Any]:
        """
        Reboots a broker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.reboot_broker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#reboot_broker)
        """
    def update_broker(
        self,
        *,
        BrokerId: str,
        AuthenticationStrategy: AuthenticationStrategyType = None,
        AutoMinorVersionUpgrade: bool = None,
        Configuration: "ConfigurationIdTypeDef" = None,
        EngineVersion: str = None,
        HostInstanceType: str = None,
        LdapServerMetadata: "LdapServerMetadataInputTypeDef" = None,
        Logs: "LogsTypeDef" = None,
        MaintenanceWindowStartTime: "WeeklyStartTimeTypeDef" = None,
        SecurityGroups: List[str] = None
    ) -> UpdateBrokerResponseTypeDef:
        """
        Adds a pending configuration change to a broker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.update_broker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#update_broker)
        """
    def update_configuration(
        self, *, ConfigurationId: str, Data: str, Description: str = None
    ) -> UpdateConfigurationResponseTypeDef:
        """
        Updates the specified configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.update_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#update_configuration)
        """
    def update_user(
        self,
        *,
        BrokerId: str,
        Username: str,
        ConsoleAccess: bool = None,
        Groups: List[str] = None,
        Password: str = None
    ) -> Dict[str, Any]:
        """
        Updates the information for an ActiveMQ user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Client.update_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/client.html#update_user)
        """
    def get_paginator(self, operation_name: Literal["list_brokers"]) -> ListBrokersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/mq.html#MQ.Paginator.ListBrokers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/paginators.html#listbrokerspaginator)
        """
