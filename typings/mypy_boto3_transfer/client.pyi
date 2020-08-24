# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for transfer service client

Usage::

    ```python
    import boto3
    from mypy_boto3_transfer import TransferClient

    client: TransferClient = boto3.client("transfer")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_transfer.paginator import ListServersPaginator
from mypy_boto3_transfer.type_defs import (
    CreateServerResponseTypeDef,
    CreateUserResponseTypeDef,
    DescribeSecurityPolicyResponseTypeDef,
    DescribeServerResponseTypeDef,
    DescribeUserResponseTypeDef,
    EndpointDetailsTypeDef,
    HomeDirectoryMapEntryTypeDef,
    IdentityProviderDetailsTypeDef,
    ImportSshPublicKeyResponseTypeDef,
    ListSecurityPoliciesResponseTypeDef,
    ListServersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsersResponseTypeDef,
    TagTypeDef,
    TestIdentityProviderResponseTypeDef,
    UpdateServerResponseTypeDef,
    UpdateUserResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("TransferClient",)


class Exceptions:
    AccessDeniedException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    ConflictException: Type[Boto3ClientError]
    InternalServiceError: Type[Boto3ClientError]
    InvalidNextTokenException: Type[Boto3ClientError]
    InvalidRequestException: Type[Boto3ClientError]
    ResourceExistsException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ServiceUnavailableException: Type[Boto3ClientError]
    ThrottlingException: Type[Boto3ClientError]


class TransferClient:
    """
    [Transfer.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.can_paginate)
        """

    def create_server(
        self,
        Certificate: str = None,
        EndpointDetails: "EndpointDetailsTypeDef" = None,
        EndpointType: Literal["PUBLIC", "VPC", "VPC_ENDPOINT"] = None,
        HostKey: str = None,
        IdentityProviderDetails: "IdentityProviderDetailsTypeDef" = None,
        IdentityProviderType: Literal["SERVICE_MANAGED", "API_GATEWAY"] = None,
        LoggingRole: str = None,
        Protocols: List[Literal["SFTP", "FTP", "FTPS"]] = None,
        SecurityPolicyName: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateServerResponseTypeDef:
        """
        [Client.create_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.create_server)
        """

    def create_user(
        self,
        Role: str,
        ServerId: str,
        UserName: str,
        HomeDirectory: str = None,
        HomeDirectoryType: Literal["PATH", "LOGICAL"] = None,
        HomeDirectoryMappings: List["HomeDirectoryMapEntryTypeDef"] = None,
        Policy: str = None,
        SshPublicKeyBody: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateUserResponseTypeDef:
        """
        [Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.create_user)
        """

    def delete_server(self, ServerId: str) -> None:
        """
        [Client.delete_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.delete_server)
        """

    def delete_ssh_public_key(self, ServerId: str, SshPublicKeyId: str, UserName: str) -> None:
        """
        [Client.delete_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.delete_ssh_public_key)
        """

    def delete_user(self, ServerId: str, UserName: str) -> None:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.delete_user)
        """

    def describe_security_policy(
        self, SecurityPolicyName: str
    ) -> DescribeSecurityPolicyResponseTypeDef:
        """
        [Client.describe_security_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.describe_security_policy)
        """

    def describe_server(self, ServerId: str) -> DescribeServerResponseTypeDef:
        """
        [Client.describe_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.describe_server)
        """

    def describe_user(self, ServerId: str, UserName: str) -> DescribeUserResponseTypeDef:
        """
        [Client.describe_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.describe_user)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.generate_presigned_url)
        """

    def import_ssh_public_key(
        self, ServerId: str, SshPublicKeyBody: str, UserName: str
    ) -> ImportSshPublicKeyResponseTypeDef:
        """
        [Client.import_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.import_ssh_public_key)
        """

    def list_security_policies(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListSecurityPoliciesResponseTypeDef:
        """
        [Client.list_security_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.list_security_policies)
        """

    def list_servers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListServersResponseTypeDef:
        """
        [Client.list_servers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.list_servers)
        """

    def list_tags_for_resource(
        self, Arn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.list_tags_for_resource)
        """

    def list_users(
        self, ServerId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListUsersResponseTypeDef:
        """
        [Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.list_users)
        """

    def start_server(self, ServerId: str) -> None:
        """
        [Client.start_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.start_server)
        """

    def stop_server(self, ServerId: str) -> None:
        """
        [Client.stop_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.stop_server)
        """

    def tag_resource(self, Arn: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.tag_resource)
        """

    def test_identity_provider(
        self,
        ServerId: str,
        UserName: str,
        ServerProtocol: Literal["SFTP", "FTP", "FTPS"] = None,
        SourceIp: str = None,
        UserPassword: str = None,
    ) -> TestIdentityProviderResponseTypeDef:
        """
        [Client.test_identity_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.test_identity_provider)
        """

    def untag_resource(self, Arn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.untag_resource)
        """

    def update_server(
        self,
        ServerId: str,
        Certificate: str = None,
        EndpointDetails: "EndpointDetailsTypeDef" = None,
        EndpointType: Literal["PUBLIC", "VPC", "VPC_ENDPOINT"] = None,
        HostKey: str = None,
        IdentityProviderDetails: "IdentityProviderDetailsTypeDef" = None,
        LoggingRole: str = None,
        Protocols: List[Literal["SFTP", "FTP", "FTPS"]] = None,
        SecurityPolicyName: str = None,
    ) -> UpdateServerResponseTypeDef:
        """
        [Client.update_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.update_server)
        """

    def update_user(
        self,
        ServerId: str,
        UserName: str,
        HomeDirectory: str = None,
        HomeDirectoryType: Literal["PATH", "LOGICAL"] = None,
        HomeDirectoryMappings: List["HomeDirectoryMapEntryTypeDef"] = None,
        Policy: str = None,
        Role: str = None,
    ) -> UpdateUserResponseTypeDef:
        """
        [Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Client.update_user)
        """

    def get_paginator(self, operation_name: Literal["list_servers"]) -> ListServersPaginator:
        """
        [Paginator.ListServers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/transfer.html#Transfer.Paginator.ListServers)
        """
