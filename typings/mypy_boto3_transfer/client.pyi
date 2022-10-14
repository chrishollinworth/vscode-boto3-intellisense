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
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AgreementStatusTypeType,
    CertificateUsageTypeType,
    CustomStepStatusType,
    DomainType,
    EndpointTypeType,
    HomeDirectoryTypeType,
    IdentityProviderTypeType,
    ProfileTypeType,
    ProtocolType,
)
from .paginator import (
    ListAccessesPaginator,
    ListAgreementsPaginator,
    ListCertificatesPaginator,
    ListConnectorsPaginator,
    ListExecutionsPaginator,
    ListProfilesPaginator,
    ListSecurityPoliciesPaginator,
    ListServersPaginator,
    ListTagsForResourcePaginator,
    ListUsersPaginator,
    ListWorkflowsPaginator,
)
from .type_defs import (
    As2ConnectorConfigTypeDef,
    CreateAccessResponseTypeDef,
    CreateAgreementResponseTypeDef,
    CreateConnectorResponseTypeDef,
    CreateProfileResponseTypeDef,
    CreateServerResponseTypeDef,
    CreateUserResponseTypeDef,
    CreateWorkflowResponseTypeDef,
    DescribeAccessResponseTypeDef,
    DescribeAgreementResponseTypeDef,
    DescribeCertificateResponseTypeDef,
    DescribeConnectorResponseTypeDef,
    DescribeExecutionResponseTypeDef,
    DescribeHostKeyResponseTypeDef,
    DescribeProfileResponseTypeDef,
    DescribeSecurityPolicyResponseTypeDef,
    DescribeServerResponseTypeDef,
    DescribeUserResponseTypeDef,
    DescribeWorkflowResponseTypeDef,
    EndpointDetailsTypeDef,
    HomeDirectoryMapEntryTypeDef,
    IdentityProviderDetailsTypeDef,
    ImportCertificateResponseTypeDef,
    ImportHostKeyResponseTypeDef,
    ImportSshPublicKeyResponseTypeDef,
    ListAccessesResponseTypeDef,
    ListAgreementsResponseTypeDef,
    ListCertificatesResponseTypeDef,
    ListConnectorsResponseTypeDef,
    ListExecutionsResponseTypeDef,
    ListHostKeysResponseTypeDef,
    ListProfilesResponseTypeDef,
    ListSecurityPoliciesResponseTypeDef,
    ListServersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsersResponseTypeDef,
    ListWorkflowsResponseTypeDef,
    PosixProfileTypeDef,
    ProtocolDetailsTypeDef,
    StartFileTransferResponseTypeDef,
    TagTypeDef,
    TestIdentityProviderResponseTypeDef,
    UpdateAccessResponseTypeDef,
    UpdateAgreementResponseTypeDef,
    UpdateCertificateResponseTypeDef,
    UpdateConnectorResponseTypeDef,
    UpdateHostKeyResponseTypeDef,
    UpdateProfileResponseTypeDef,
    UpdateServerResponseTypeDef,
    UpdateUserResponseTypeDef,
    WorkflowDetailsTypeDef,
    WorkflowStepTypeDef,
)
from .waiter import ServerOfflineWaiter, ServerOnlineWaiter

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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#close)
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
        access to upload and download files over the enabled protocols using Transfer
        Family.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.create_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#create_access)
        """
    def create_agreement(
        self,
        *,
        ServerId: str,
        LocalProfileId: str,
        PartnerProfileId: str,
        BaseDirectory: str,
        AccessRole: str,
        Description: str = None,
        Status: AgreementStatusTypeType = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAgreementResponseTypeDef:
        """
        Creates an agreement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.create_agreement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#create_agreement)
        """
    def create_connector(
        self,
        *,
        Url: str,
        As2Config: "As2ConnectorConfigTypeDef",
        AccessRole: str,
        LoggingRole: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateConnectorResponseTypeDef:
        """
        Creates the connector, which captures the parameters for an outbound connection
        for the AS2 protocol.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.create_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#create_connector)
        """
    def create_profile(
        self,
        *,
        As2Id: str,
        ProfileType: ProfileTypeType,
        CertificateIds: List[str] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateProfileResponseTypeDef:
        """
        Creates the profile for the AS2 process.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.create_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#create_profile)
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
        PostAuthenticationLoginBanner: str = None,
        PreAuthenticationLoginBanner: str = None,
        Protocols: List[ProtocolType] = None,
        ProtocolDetails: "ProtocolDetailsTypeDef" = None,
        SecurityPolicyName: str = None,
        Tags: List["TagTypeDef"] = None,
        WorkflowDetails: "WorkflowDetailsTypeDef" = None
    ) -> CreateServerResponseTypeDef:
        """
        Instantiates an auto-scaling virtual server based on the selected file transfer
        protocol in Amazon Web Services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.create_server)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#create_user)
        """
    def create_workflow(
        self,
        *,
        Steps: List["WorkflowStepTypeDef"],
        Description: str = None,
        OnExceptionSteps: List["WorkflowStepTypeDef"] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateWorkflowResponseTypeDef:
        """
        Allows you to create a workflow with specified steps and step details the
        workflow invokes after file transfer completes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.create_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#create_workflow)
        """
    def delete_access(self, *, ServerId: str, ExternalId: str) -> None:
        """
        Allows you to delete the access specified in the `ServerID` and `ExternalID`
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.delete_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#delete_access)
        """
    def delete_agreement(self, *, AgreementId: str, ServerId: str) -> None:
        """
        Delete the agreement that's specified in the provided `AgreementId` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.delete_agreement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#delete_agreement)
        """
    def delete_certificate(self, *, CertificateId: str) -> None:
        """
        Deletes the certificate that's specified in the `CertificateId` parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.delete_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#delete_certificate)
        """
    def delete_connector(self, *, ConnectorId: str) -> None:
        """
        Deletes the agreement that's specified in the provided `ConnectorId` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.delete_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#delete_connector)
        """
    def delete_host_key(self, *, ServerId: str, HostKeyId: str) -> None:
        """
        Deletes the host key that's specified in the `HoskKeyId` parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.delete_host_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#delete_host_key)
        """
    def delete_profile(self, *, ProfileId: str) -> None:
        """
        Deletes the profile that's specified in the `ProfileId` parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.delete_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#delete_profile)
        """
    def delete_server(self, *, ServerId: str) -> None:
        """
        Deletes the file transfer protocol-enabled server that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.delete_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#delete_server)
        """
    def delete_ssh_public_key(self, *, ServerId: str, SshPublicKeyId: str, UserName: str) -> None:
        """
        Deletes a user's Secure Shell (SSH) public key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.delete_ssh_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#delete_ssh_public_key)
        """
    def delete_user(self, *, ServerId: str, UserName: str) -> None:
        """
        Deletes the user belonging to a file transfer protocol-enabled server you
        specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#delete_user)
        """
    def delete_workflow(self, *, WorkflowId: str) -> None:
        """
        Deletes the specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.delete_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#delete_workflow)
        """
    def describe_access(self, *, ServerId: str, ExternalId: str) -> DescribeAccessResponseTypeDef:
        """
        Describes the access that is assigned to the specific file transfer protocol-
        enabled server, as identified by its `ServerId` property and its `ExternalId` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.describe_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#describe_access)
        """
    def describe_agreement(
        self, *, AgreementId: str, ServerId: str
    ) -> DescribeAgreementResponseTypeDef:
        """
        Describes the agreement that's identified by the `AgreementId` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.describe_agreement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#describe_agreement)
        """
    def describe_certificate(self, *, CertificateId: str) -> DescribeCertificateResponseTypeDef:
        """
        Describes the certificate that's identified by the `CertificateId` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.describe_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#describe_certificate)
        """
    def describe_connector(self, *, ConnectorId: str) -> DescribeConnectorResponseTypeDef:
        """
        Describes the connector that's identified by the `ConnectorId.` See also: `AWS
        API Documentation <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-
        05/DescribeConnector>`_ **Request Syntax** response = client.describe_connector(
        ConnectorId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.describe_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#describe_connector)
        """
    def describe_execution(
        self, *, ExecutionId: str, WorkflowId: str
    ) -> DescribeExecutionResponseTypeDef:
        """
        You can use `DescribeExecution` to check the details of the execution of the
        specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.describe_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#describe_execution)
        """
    def describe_host_key(self, *, ServerId: str, HostKeyId: str) -> DescribeHostKeyResponseTypeDef:
        """
        Returns the details of the host key that's specified by the `HostKeyId` and
        `ServerId` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.describe_host_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#describe_host_key)
        """
    def describe_profile(self, *, ProfileId: str) -> DescribeProfileResponseTypeDef:
        """
        Returns the details of the profile that's specified by the `ProfileId` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.describe_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#describe_profile)
        """
    def describe_security_policy(
        self, *, SecurityPolicyName: str
    ) -> DescribeSecurityPolicyResponseTypeDef:
        """
        Describes the security policy that is attached to your file transfer protocol-
        enabled server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.describe_security_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#describe_security_policy)
        """
    def describe_server(self, *, ServerId: str) -> DescribeServerResponseTypeDef:
        """
        Describes a file transfer protocol-enabled server that you specify by passing
        the `ServerId` parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.describe_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#describe_server)
        """
    def describe_user(self, *, ServerId: str, UserName: str) -> DescribeUserResponseTypeDef:
        """
        Describes the user assigned to the specific file transfer protocol-enabled
        server, as identified by its `ServerId` property.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.describe_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#describe_user)
        """
    def describe_workflow(self, *, WorkflowId: str) -> DescribeWorkflowResponseTypeDef:
        """
        Describes the specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.describe_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#describe_workflow)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#generate_presigned_url)
        """
    def import_certificate(
        self,
        *,
        Usage: CertificateUsageTypeType,
        Certificate: str,
        CertificateChain: str = None,
        PrivateKey: str = None,
        ActiveDate: Union[datetime, str] = None,
        InactiveDate: Union[datetime, str] = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> ImportCertificateResponseTypeDef:
        """
        Imports the signing and encryption certificates that you need to create local
        (AS2) profiles and partner profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.import_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#import_certificate)
        """
    def import_host_key(
        self,
        *,
        ServerId: str,
        HostKeyBody: str,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> ImportHostKeyResponseTypeDef:
        """
        Adds a host key to the server specified by the `ServerId` parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.import_host_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#import_host_key)
        """
    def import_ssh_public_key(
        self, *, ServerId: str, SshPublicKeyBody: str, UserName: str
    ) -> ImportSshPublicKeyResponseTypeDef:
        """
        Adds a Secure Shell (SSH) public key to a user account identified by a
        `UserName` value assigned to the specific file transfer protocol-enabled server,
        identified by `ServerId` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.import_ssh_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#import_ssh_public_key)
        """
    def list_accesses(
        self, *, ServerId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAccessesResponseTypeDef:
        """
        Lists the details for all the accesses you have on your server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.list_accesses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list_accesses)
        """
    def list_agreements(
        self, *, ServerId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAgreementsResponseTypeDef:
        """
        Returns a list of the agreements for the server that's identified by the
        `ServerId` that you supply.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.list_agreements)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list_agreements)
        """
    def list_certificates(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListCertificatesResponseTypeDef:
        """
        Returns a list of the current certificates that have been imported into Transfer
        Family.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.list_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list_certificates)
        """
    def list_connectors(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListConnectorsResponseTypeDef:
        """
        Lists the connectors for the specified Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.list_connectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list_connectors)
        """
    def list_executions(
        self, *, WorkflowId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListExecutionsResponseTypeDef:
        """
        Lists all executions for the specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.list_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list_executions)
        """
    def list_host_keys(
        self, *, ServerId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListHostKeysResponseTypeDef:
        """
        Returns a list of host keys for the server specified by the `ServerId` paramter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.list_host_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list_host_keys)
        """
    def list_profiles(
        self, *, MaxResults: int = None, NextToken: str = None, ProfileType: ProfileTypeType = None
    ) -> ListProfilesResponseTypeDef:
        """
        Returns a list of the profiles for your system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.list_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list_profiles)
        """
    def list_security_policies(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListSecurityPoliciesResponseTypeDef:
        """
        Lists the security policies that are attached to your file transfer protocol-
        enabled servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.list_security_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list_security_policies)
        """
    def list_servers(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListServersResponseTypeDef:
        """
        Lists the file transfer protocol-enabled servers that are associated with your
        Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.list_servers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list_servers)
        """
    def list_tags_for_resource(
        self, *, Arn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all of the tags associated with the Amazon Resource Name (ARN) that you
        specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list_tags_for_resource)
        """
    def list_users(
        self, *, ServerId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListUsersResponseTypeDef:
        """
        Lists the users for a file transfer protocol-enabled server that you specify by
        passing the `ServerId` parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.list_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list_users)
        """
    def list_workflows(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListWorkflowsResponseTypeDef:
        """
        Lists all of your workflows.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.list_workflows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list_workflows)
        """
    def send_workflow_step_state(
        self, *, WorkflowId: str, ExecutionId: str, Token: str, Status: CustomStepStatusType
    ) -> Dict[str, Any]:
        """
        Sends a callback for asynchronous custom steps.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.send_workflow_step_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#send_workflow_step_state)
        """
    def start_file_transfer(
        self, *, ConnectorId: str, SendFilePaths: List[str]
    ) -> StartFileTransferResponseTypeDef:
        """
        Begins an outbound file transfer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.start_file_transfer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#start_file_transfer)
        """
    def start_server(self, *, ServerId: str) -> None:
        """
        Changes the state of a file transfer protocol-enabled server from `OFFLINE` to
        `ONLINE`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.start_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#start_server)
        """
    def stop_server(self, *, ServerId: str) -> None:
        """
        Changes the state of a file transfer protocol-enabled server from `ONLINE` to
        `OFFLINE`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.stop_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#stop_server)
        """
    def tag_resource(self, *, Arn: str, Tags: List["TagTypeDef"]) -> None:
        """
        Attaches a key-value pair to a resource, as identified by its Amazon Resource
        Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.tag_resource)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.test_identity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#test_identity_provider)
        """
    def untag_resource(self, *, Arn: str, TagKeys: List[str]) -> None:
        """
        Detaches a key-value pair from a resource, as identified by its Amazon Resource
        Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.untag_resource)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.update_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#update_access)
        """
    def update_agreement(
        self,
        *,
        AgreementId: str,
        ServerId: str,
        Description: str = None,
        Status: AgreementStatusTypeType = None,
        LocalProfileId: str = None,
        PartnerProfileId: str = None,
        BaseDirectory: str = None,
        AccessRole: str = None
    ) -> UpdateAgreementResponseTypeDef:
        """
        Updates some of the parameters for an existing agreement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.update_agreement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#update_agreement)
        """
    def update_certificate(
        self,
        *,
        CertificateId: str,
        ActiveDate: Union[datetime, str] = None,
        InactiveDate: Union[datetime, str] = None,
        Description: str = None
    ) -> UpdateCertificateResponseTypeDef:
        """
        Updates the active and inactive dates for a certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.update_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#update_certificate)
        """
    def update_connector(
        self,
        *,
        ConnectorId: str,
        Url: str = None,
        As2Config: "As2ConnectorConfigTypeDef" = None,
        AccessRole: str = None,
        LoggingRole: str = None
    ) -> UpdateConnectorResponseTypeDef:
        """
        Updates some of the parameters for an existing connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.update_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#update_connector)
        """
    def update_host_key(
        self, *, ServerId: str, HostKeyId: str, Description: str
    ) -> UpdateHostKeyResponseTypeDef:
        """
        Updates the description for the host key specified by the specified by the
        `ServerId` and `HostKeyId` parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.update_host_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#update_host_key)
        """
    def update_profile(
        self, *, ProfileId: str, CertificateIds: List[str] = None
    ) -> UpdateProfileResponseTypeDef:
        """
        Updates some of the parameters for an existing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.update_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#update_profile)
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
        PostAuthenticationLoginBanner: str = None,
        PreAuthenticationLoginBanner: str = None,
        Protocols: List[ProtocolType] = None,
        SecurityPolicyName: str = None,
        WorkflowDetails: "WorkflowDetailsTypeDef" = None
    ) -> UpdateServerResponseTypeDef:
        """
        Updates the file transfer protocol-enabled server's properties after that server
        has been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.update_server)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Client.update_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#update_user)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_accesses"]) -> ListAccessesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListAccesses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listaccessespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_agreements"]) -> ListAgreementsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListAgreements)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listagreementspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_certificates"]
    ) -> ListCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListCertificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listcertificatespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_connectors"]) -> ListConnectorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListConnectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listconnectorspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_executions"]) -> ListExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listexecutionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_profiles"]) -> ListProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listprofilespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_policies"]
    ) -> ListSecurityPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListSecurityPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listsecuritypoliciespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_servers"]) -> ListServersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListServers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listserverspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listtagsforresourcepaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListUsers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listuserspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_workflows"]) -> ListWorkflowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListWorkflows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listworkflowspaginator)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["server_offline"]) -> ServerOfflineWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Waiter.ServerOffline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/waiters.html#serverofflinewaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["server_online"]) -> ServerOnlineWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Waiter.ServerOnline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/waiters.html#serveronlinewaiter)
        """
