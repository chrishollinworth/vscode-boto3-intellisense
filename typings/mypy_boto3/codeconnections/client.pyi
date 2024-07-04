"""
Type annotations for codeconnections service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_codeconnections import CodeConnectionsClient

    client: CodeConnectionsClient = boto3.client("codeconnections")
    ```
"""

import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import ProviderTypeType, PublishDeploymentStatusType, TriggerResourceUpdateOnType
from .type_defs import (
    CreateConnectionOutputTypeDef,
    CreateHostOutputTypeDef,
    CreateRepositoryLinkOutputTypeDef,
    CreateSyncConfigurationOutputTypeDef,
    GetConnectionOutputTypeDef,
    GetHostOutputTypeDef,
    GetRepositoryLinkOutputTypeDef,
    GetRepositorySyncStatusOutputTypeDef,
    GetResourceSyncStatusOutputTypeDef,
    GetSyncBlockerSummaryOutputTypeDef,
    GetSyncConfigurationOutputTypeDef,
    ListConnectionsOutputTypeDef,
    ListHostsOutputTypeDef,
    ListRepositoryLinksOutputTypeDef,
    ListRepositorySyncDefinitionsOutputTypeDef,
    ListSyncConfigurationsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    TagTypeDef,
    UpdateRepositoryLinkOutputTypeDef,
    UpdateSyncBlockerOutputTypeDef,
    UpdateSyncConfigurationOutputTypeDef,
    VpcConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CodeConnectionsClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConditionalCheckFailedException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    RetryLatestCommitFailedException: Type[BotocoreClientError]
    SyncBlockerDoesNotExistException: Type[BotocoreClientError]
    SyncConfigurationStillExistsException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]
    UnsupportedProviderTypeException: Type[BotocoreClientError]
    UpdateOutOfSyncException: Type[BotocoreClientError]

class CodeConnectionsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CodeConnectionsClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#close)
        """

    def create_connection(
        self,
        *,
        ConnectionName: str,
        ProviderType: ProviderTypeType = None,
        Tags: List["TagTypeDef"] = None,
        HostArn: str = None
    ) -> CreateConnectionOutputTypeDef:
        """
        Creates a connection that can then be given to other Amazon Web Services
        services like CodePipeline so that it can access third-party code repositories.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.create_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#create_connection)
        """

    def create_host(
        self,
        *,
        Name: str,
        ProviderType: ProviderTypeType,
        ProviderEndpoint: str,
        VpcConfiguration: "VpcConfigurationTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateHostOutputTypeDef:
        """
        Creates a resource that represents the infrastructure where a third-party
        provider is installed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.create_host)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#create_host)
        """

    def create_repository_link(
        self,
        *,
        ConnectionArn: str,
        OwnerId: str,
        RepositoryName: str,
        EncryptionKeyArn: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateRepositoryLinkOutputTypeDef:
        """
        Creates a link to a specified external Git repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.create_repository_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#create_repository_link)
        """

    def create_sync_configuration(
        self,
        *,
        Branch: str,
        ConfigFile: str,
        RepositoryLinkId: str,
        ResourceName: str,
        RoleArn: str,
        SyncType: Literal["CFN_STACK_SYNC"],
        PublishDeploymentStatus: PublishDeploymentStatusType = None,
        TriggerResourceUpdateOn: TriggerResourceUpdateOnType = None
    ) -> CreateSyncConfigurationOutputTypeDef:
        """
        Creates a sync configuration which allows Amazon Web Services to sync content
        from a Git repository to update a specified Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.create_sync_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#create_sync_configuration)
        """

    def delete_connection(self, *, ConnectionArn: str) -> Dict[str, Any]:
        """
        The connection to be deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.delete_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#delete_connection)
        """

    def delete_host(self, *, HostArn: str) -> Dict[str, Any]:
        """
        The host to be deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.delete_host)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#delete_host)
        """

    def delete_repository_link(self, *, RepositoryLinkId: str) -> Dict[str, Any]:
        """
        Deletes the association between your connection and a specified external Git
        repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.delete_repository_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#delete_repository_link)
        """

    def delete_sync_configuration(
        self, *, SyncType: Literal["CFN_STACK_SYNC"], ResourceName: str
    ) -> Dict[str, Any]:
        """
        Deletes the sync configuration for a specified repository and connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.delete_sync_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#delete_sync_configuration)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#generate_presigned_url)
        """

    def get_connection(self, *, ConnectionArn: str) -> GetConnectionOutputTypeDef:
        """
        Returns the connection ARN and details such as status, owner, and provider type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.get_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#get_connection)
        """

    def get_host(self, *, HostArn: str) -> GetHostOutputTypeDef:
        """
        Returns the host ARN and details such as status, provider type, endpoint, and,
        if applicable, the VPC configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.get_host)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#get_host)
        """

    def get_repository_link(self, *, RepositoryLinkId: str) -> GetRepositoryLinkOutputTypeDef:
        """
        Returns details about a repository link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.get_repository_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#get_repository_link)
        """

    def get_repository_sync_status(
        self, *, Branch: str, RepositoryLinkId: str, SyncType: Literal["CFN_STACK_SYNC"]
    ) -> GetRepositorySyncStatusOutputTypeDef:
        """
        Returns details about the sync status for a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.get_repository_sync_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#get_repository_sync_status)
        """

    def get_resource_sync_status(
        self, *, ResourceName: str, SyncType: Literal["CFN_STACK_SYNC"]
    ) -> GetResourceSyncStatusOutputTypeDef:
        """
        Returns the status of the sync with the Git repository for a specific Amazon Web
        Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.get_resource_sync_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#get_resource_sync_status)
        """

    def get_sync_blocker_summary(
        self, *, SyncType: Literal["CFN_STACK_SYNC"], ResourceName: str
    ) -> GetSyncBlockerSummaryOutputTypeDef:
        """
        Returns a list of the most recent sync blockers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.get_sync_blocker_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#get_sync_blocker_summary)
        """

    def get_sync_configuration(
        self, *, SyncType: Literal["CFN_STACK_SYNC"], ResourceName: str
    ) -> GetSyncConfigurationOutputTypeDef:
        """
        Returns details about a sync configuration, including the sync type and resource
        name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.get_sync_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#get_sync_configuration)
        """

    def list_connections(
        self,
        *,
        ProviderTypeFilter: ProviderTypeType = None,
        HostArnFilter: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListConnectionsOutputTypeDef:
        """
        Lists the connections associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.list_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#list_connections)
        """

    def list_hosts(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListHostsOutputTypeDef:
        """
        Lists the hosts associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.list_hosts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#list_hosts)
        """

    def list_repository_links(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListRepositoryLinksOutputTypeDef:
        """
        Lists the repository links created for connections in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.list_repository_links)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#list_repository_links)
        """

    def list_repository_sync_definitions(
        self, *, RepositoryLinkId: str, SyncType: Literal["CFN_STACK_SYNC"]
    ) -> ListRepositorySyncDefinitionsOutputTypeDef:
        """
        Lists the repository sync definitions for repository links in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.list_repository_sync_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#list_repository_sync_definitions)
        """

    def list_sync_configurations(
        self,
        *,
        RepositoryLinkId: str,
        SyncType: Literal["CFN_STACK_SYNC"],
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListSyncConfigurationsOutputTypeDef:
        """
        Returns a list of sync configurations for a specified repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.list_sync_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#list_sync_configurations)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Gets the set of key-value pairs (metadata) that are used to manage the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#list_tags_for_resource)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds to or modifies the tags of the given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#untag_resource)
        """

    def update_host(
        self,
        *,
        HostArn: str,
        ProviderEndpoint: str = None,
        VpcConfiguration: "VpcConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates a specified host with the provided configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.update_host)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#update_host)
        """

    def update_repository_link(
        self, *, RepositoryLinkId: str, ConnectionArn: str = None, EncryptionKeyArn: str = None
    ) -> UpdateRepositoryLinkOutputTypeDef:
        """
        Updates the association between your connection and a specified external Git
        repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.update_repository_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#update_repository_link)
        """

    def update_sync_blocker(
        self,
        *,
        Id: str,
        SyncType: Literal["CFN_STACK_SYNC"],
        ResourceName: str,
        ResolvedReason: str
    ) -> UpdateSyncBlockerOutputTypeDef:
        """
        Allows you to update the status of a sync blocker, resolving the blocker and
        allowing syncing to continue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.update_sync_blocker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#update_sync_blocker)
        """

    def update_sync_configuration(
        self,
        *,
        ResourceName: str,
        SyncType: Literal["CFN_STACK_SYNC"],
        Branch: str = None,
        ConfigFile: str = None,
        RepositoryLinkId: str = None,
        RoleArn: str = None,
        PublishDeploymentStatus: PublishDeploymentStatusType = None,
        TriggerResourceUpdateOn: TriggerResourceUpdateOnType = None
    ) -> UpdateSyncConfigurationOutputTypeDef:
        """
        Updates the sync configuration for your connection and a specified external Git
        repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/codeconnections.html#CodeConnections.Client.update_sync_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/client.html#update_sync_configuration)
        """
