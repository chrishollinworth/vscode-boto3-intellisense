"""
Type annotations for transfer service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_transfer import TransferClient

    client: TransferClient = boto3.client("transfer")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import (
    DomainType,
    EndpointTypeType,
    HomeDirectoryTypeType,
    IdentityProviderTypeType,
    ProtocolType,
)
from .paginator import ListServersPaginator
from .type_defs import (
    CreateAccessResponseTypeDef,
    CreateServerResponseTypeDef,
    CreateUserResponseTypeDef,
    DescribeAccessResponseTypeDef,
    DescribeSecurityPolicyResponseTypeDef,
    DescribeServerResponseTypeDef,
    DescribeUserResponseTypeDef,
    EndpointDetailsTypeDef,
    HomeDirectoryMapEntryTypeDef,
    IdentityProviderDetailsTypeDef,
    ImportSshPublicKeyResponseTypeDef,
    ListAccessesResponseTypeDef,
    ListSecurityPoliciesResponseTypeDef,
    ListServersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsersResponseTypeDef,
    PosixProfileTypeDef,
    ProtocolDetailsTypeDef,
    TagTypeDef,
    TestIdentityProviderResponseTypeDef,
    UpdateAccessResponseTypeDef,
    UpdateServerResponseTypeDef,
    UpdateUserResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("TransferClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServiceError: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class TransferClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        TransferClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#can_paginate)
        """
    def create_access(
        self,
        *,
        Role: str,
        ServerId: str,
        ExternalId: str,
        HomeDirectory: str = None,
        HomeDirectoryType: HomeDirectoryTypeType = None,
        HomeDirectoryMappings: List["HomeDirectoryMapEntryTypeDef"] = None,
        Policy: str = None,
        PosixProfile: "PosixProfileTypeDef" = None
    ) -> CreateAccessResponseTypeDef:
        """
        Used by administrators to choose which groups in the directory should have
        access to upload and download files over the enabled protocols using Amazon Web
        Services Transfer Family.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.create_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#create_access)
        """
    def create_server(
        self,
        *,
        Certificate: str = None,
        Domain: DomainType = None,
        EndpointDetails: "EndpointDetailsTypeDef" = None,
        EndpointType: EndpointTypeType = None,
        HostKey: str = None,
        IdentityProviderDetails: "IdentityProviderDetailsTypeDef" = None,
        IdentityProviderType: IdentityProviderTypeType = None,
        LoggingRole: str = None,
        Protocols: List[ProtocolType] = None,
        SecurityPolicyName: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateServerResponseTypeDef:
        """
        Instantiates an auto-scaling virtual server based on the selected file transfer
        protocol in Amazon Web Services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.create_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#create_server)
        """
    def create_user(
        self,
        *,
        Role: str,
        ServerId: str,
        UserName: str,
        HomeDirectory: str = None,
        HomeDirectoryType: HomeDirectoryTypeType = None,
        HomeDirectoryMappings: List["HomeDirectoryMapEntryTypeDef"] = None,
        Policy: str = None,
        PosixProfile: "PosixProfileTypeDef" = None,
        SshPublicKeyBody: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateUserResponseTypeDef:
        """
        Creates a user and associates them with an existing file transfer protocol-
        enabled server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#create_user)
        """
    def delete_access(self, *, ServerId: str, ExternalId: str) -> None:
        """
        Allows you to delete the access specified in the `ServerID` and `ExternalID`
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.delete_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#delete_access)
        """
    def delete_server(self, *, ServerId: str) -> None:
        """
        Deletes the file transfer protocol-enabled server that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.delete_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#delete_server)
        """
    def delete_ssh_public_key(self, *, ServerId: str, SshPublicKeyId: str, UserName: str) -> None:
        """
        Deletes a user's Secure Shell (SSH) public key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.delete_ssh_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#delete_ssh_public_key)
        """
    def delete_user(self, *, ServerId: str, UserName: str) -> None:
        """
        Deletes the user belonging to a file transfer protocol-enabled server you
        specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#delete_user)
        """
    def describe_access(self, *, ServerId: str, ExternalId: str) -> DescribeAccessResponseTypeDef:
        """
        Describes the access that is assigned to the specific file transfer protocol-
        enabled server, as identified by its `ServerId` property and its `ExternalID` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.describe_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#describe_access)
        """
    def describe_security_policy(
        self, *, SecurityPolicyName: str
    ) -> DescribeSecurityPolicyResponseTypeDef:
        """
        Describes the security policy that is attached to your file transfer protocol-
        enabled server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.describe_security_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#describe_security_policy)
        """
    def describe_server(self, *, ServerId: str) -> DescribeServerResponseTypeDef:
        """
        Describes a file transfer protocol-enabled server that you specify by passing
        the `ServerId` parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.describe_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#describe_server)
        """
    def describe_user(self, *, ServerId: str, UserName: str) -> DescribeUserResponseTypeDef:
        """
        Describes the user assigned to the specific file transfer protocol-enabled
        server, as identified by its `ServerId` property.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.describe_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#describe_user)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#generate_presigned_url)
        """
    def import_ssh_public_key(
        self, *, ServerId: str, SshPublicKeyBody: str, UserName: str
    ) -> ImportSshPublicKeyResponseTypeDef:
        """
        Adds a Secure Shell (SSH) public key to a user account identified by a
        `UserName` value assigned to the specific file transfer protocol-enabled server,
        identified by `ServerId` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.import_ssh_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#import_ssh_public_key)
        """
    def list_accesses(
        self, *, ServerId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAccessesResponseTypeDef:
        """
        Lists the details for all the accesses you have on your server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.list_accesses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list_accesses)
        """
    def list_security_policies(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListSecurityPoliciesResponseTypeDef:
        """
        Lists the security policies that are attached to your file transfer protocol-
        enabled servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.list_security_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list_security_policies)
        """
    def list_servers(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListServersResponseTypeDef:
        """
        Lists the file transfer protocol-enabled servers that are associated with your
        Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.list_servers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list_servers)
        """
    def list_tags_for_resource(
        self, *, Arn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all of the tags associated with the Amazon Resource Name (ARN) that you
        specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list_tags_for_resource)
        """
    def list_users(
        self, *, ServerId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListUsersResponseTypeDef:
        """
        Lists the users for a file transfer protocol-enabled server that you specify by
        passing the `ServerId` parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.list_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list_users)
        """
    def start_server(self, *, ServerId: str) -> None:
        """
        Changes the state of a file transfer protocol-enabled server from `OFFLINE` to
        `ONLINE`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.start_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#start_server)
        """
    def stop_server(self, *, ServerId: str) -> None:
        """
        Changes the state of a file transfer protocol-enabled server from `ONLINE` to
        `OFFLINE`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.stop_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#stop_server)
        """
    def tag_resource(self, *, Arn: str, Tags: List["TagTypeDef"]) -> None:
        """
        Attaches a key-value pair to a resource, as identified by its Amazon Resource
        Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#tag_resource)
        """
    def test_identity_provider(
        self,
        *,
        ServerId: str,
        UserName: str,
        ServerProtocol: ProtocolType = None,
        SourceIp: str = None,
        UserPassword: str = None
    ) -> TestIdentityProviderResponseTypeDef:
        """
        If the `IdentityProviderType` of a file transfer protocol-enabled server is
        `AWS_DIRECTORY_SERVICE` or `API_Gateway` , tests whether your identity provider
        is set up successfully.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.test_identity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#test_identity_provider)
        """
    def untag_resource(self, *, Arn: str, TagKeys: List[str]) -> None:
        """
        Detaches a key-value pair from a resource, as identified by its Amazon Resource
        Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#untag_resource)
        """
    def update_access(
        self,
        *,
        ServerId: str,
        ExternalId: str,
        HomeDirectory: str = None,
        HomeDirectoryType: HomeDirectoryTypeType = None,
        HomeDirectoryMappings: List["HomeDirectoryMapEntryTypeDef"] = None,
        Policy: str = None,
        PosixProfile: "PosixProfileTypeDef" = None,
        Role: str = None
    ) -> UpdateAccessResponseTypeDef:
        """
        Allows you to update parameters for the access specified in the `ServerID` and
        `ExternalID` parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.update_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#update_access)
        """
    def update_server(
        self,
        *,
        ServerId: str,
        Certificate: str = None,
        ProtocolDetails: "ProtocolDetailsTypeDef" = None,
        EndpointDetails: "EndpointDetailsTypeDef" = None,
        EndpointType: EndpointTypeType = None,
        HostKey: str = None,
        IdentityProviderDetails: "IdentityProviderDetailsTypeDef" = None,
        LoggingRole: str = None,
        Protocols: List[ProtocolType] = None,
        SecurityPolicyName: str = None
    ) -> UpdateServerResponseTypeDef:
        """
        Updates the file transfer protocol-enabled server's properties after that server
        has been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.update_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#update_server)
        """
    def update_user(
        self,
        *,
        ServerId: str,
        UserName: str,
        HomeDirectory: str = None,
        HomeDirectoryType: HomeDirectoryTypeType = None,
        HomeDirectoryMappings: List["HomeDirectoryMapEntryTypeDef"] = None,
        Policy: str = None,
        PosixProfile: "PosixProfileTypeDef" = None,
        Role: str = None
    ) -> UpdateUserResponseTypeDef:
        """
        Assigns new properties to a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Client.update_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#update_user)
        """
    def get_paginator(self, operation_name: Literal["list_servers"]) -> ListServersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transfer.html#Transfer.Paginator.ListServers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listserverspaginator)
        """
