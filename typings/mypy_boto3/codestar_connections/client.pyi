"""
Type annotations for codestar-connections service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_codestar_connections import CodeStarconnectionsClient

    client: CodeStarconnectionsClient = boto3.client("codestar-connections")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import ProviderTypeType
from .type_defs import (
    CreateConnectionOutputTypeDef,
    CreateHostOutputTypeDef,
    GetConnectionOutputTypeDef,
    GetHostOutputTypeDef,
    ListConnectionsOutputTypeDef,
    ListHostsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    TagTypeDef,
    VpcConfigurationTypeDef,
)

__all__ = ("CodeStarconnectionsClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]

class CodeStarconnectionsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codestar-connections.html#CodeStarconnections.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        CodeStarconnectionsClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codestar-connections.html#CodeStarconnections.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#can_paginate)
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
        Creates a connection that can then be given to other AWS services like
        CodePipeline so that it can access third-party code repositories.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codestar-connections.html#CodeStarconnections.Client.create_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#create_connection)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codestar-connections.html#CodeStarconnections.Client.create_host)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#create_host)
        """
    def delete_connection(self, *, ConnectionArn: str) -> Dict[str, Any]:
        """
        The connection to be deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codestar-connections.html#CodeStarconnections.Client.delete_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#delete_connection)
        """
    def delete_host(self, *, HostArn: str) -> Dict[str, Any]:
        """
        The host to be deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codestar-connections.html#CodeStarconnections.Client.delete_host)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#delete_host)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codestar-connections.html#CodeStarconnections.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#generate_presigned_url)
        """
    def get_connection(self, *, ConnectionArn: str) -> GetConnectionOutputTypeDef:
        """
        Returns the connection ARN and details such as status, owner, and provider type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codestar-connections.html#CodeStarconnections.Client.get_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#get_connection)
        """
    def get_host(self, *, HostArn: str) -> GetHostOutputTypeDef:
        """
        Returns the host ARN and details such as status, provider type, endpoint, and,
        if applicable, the VPC configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codestar-connections.html#CodeStarconnections.Client.get_host)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#get_host)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codestar-connections.html#CodeStarconnections.Client.list_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#list_connections)
        """
    def list_hosts(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListHostsOutputTypeDef:
        """
        Lists the hosts associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codestar-connections.html#CodeStarconnections.Client.list_hosts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#list_hosts)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Gets the set of key-value pairs (metadata) that are used to manage the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codestar-connections.html#CodeStarconnections.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#list_tags_for_resource)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds to or modifies the tags of the given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codestar-connections.html#CodeStarconnections.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from an AWS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codestar-connections.html#CodeStarconnections.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#untag_resource)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codestar-connections.html#CodeStarconnections.Client.update_host)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#update_host)
        """
