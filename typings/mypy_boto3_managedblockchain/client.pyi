"""
Type annotations for managedblockchain service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_managedblockchain import ManagedBlockchainClient

    client: ManagedBlockchainClient = boto3.client("managedblockchain")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AccessorNetworkTypeType,
    FrameworkType,
    MemberStatusType,
    NetworkStatusType,
    NodeStatusType,
    VoteValueType,
)
from .paginator import ListAccessorsPaginator
from .type_defs import (
    CreateAccessorOutputTypeDef,
    CreateMemberOutputTypeDef,
    CreateNetworkOutputTypeDef,
    CreateNodeOutputTypeDef,
    CreateProposalOutputTypeDef,
    GetAccessorOutputTypeDef,
    GetMemberOutputTypeDef,
    GetNetworkOutputTypeDef,
    GetNodeOutputTypeDef,
    GetProposalOutputTypeDef,
    ListAccessorsOutputTypeDef,
    ListInvitationsOutputTypeDef,
    ListMembersOutputTypeDef,
    ListNetworksOutputTypeDef,
    ListNodesOutputTypeDef,
    ListProposalsOutputTypeDef,
    ListProposalVotesOutputTypeDef,
    ListTagsForResourceResponseTypeDef,
    MemberConfigurationTypeDef,
    MemberLogPublishingConfigurationTypeDef,
    NetworkFrameworkConfigurationTypeDef,
    NodeConfigurationTypeDef,
    NodeLogPublishingConfigurationTypeDef,
    ProposalActionsTypeDef,
    VotingPolicyTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ManagedBlockchainClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    IllegalActionException: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceNotReadyException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]

class ManagedBlockchainClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ManagedBlockchainClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#close)
        """
    def create_accessor(
        self,
        *,
        ClientRequestToken: str,
        AccessorType: Literal["BILLING_TOKEN"],
        Tags: Dict[str, str] = None,
        NetworkType: AccessorNetworkTypeType = None
    ) -> CreateAccessorOutputTypeDef:
        """
        Creates a new accessor for use with Amazon Managed Blockchain service that
        supports token based access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_accessor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#create_accessor)
        """
    def create_member(
        self,
        *,
        ClientRequestToken: str,
        InvitationId: str,
        NetworkId: str,
        MemberConfiguration: "MemberConfigurationTypeDef"
    ) -> CreateMemberOutputTypeDef:
        """
        Creates a member within a Managed Blockchain network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#create_member)
        """
    def create_network(
        self,
        *,
        ClientRequestToken: str,
        Name: str,
        Framework: FrameworkType,
        FrameworkVersion: str,
        VotingPolicy: "VotingPolicyTypeDef",
        MemberConfiguration: "MemberConfigurationTypeDef",
        Description: str = None,
        FrameworkConfiguration: "NetworkFrameworkConfigurationTypeDef" = None,
        Tags: Dict[str, str] = None
    ) -> CreateNetworkOutputTypeDef:
        """
        Creates a new blockchain network using Amazon Managed Blockchain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#create_network)
        """
    def create_node(
        self,
        *,
        ClientRequestToken: str,
        NetworkId: str,
        NodeConfiguration: "NodeConfigurationTypeDef",
        MemberId: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateNodeOutputTypeDef:
        """
        Creates a node on the specified blockchain network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_node)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#create_node)
        """
    def create_proposal(
        self,
        *,
        ClientRequestToken: str,
        NetworkId: str,
        MemberId: str,
        Actions: "ProposalActionsTypeDef",
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateProposalOutputTypeDef:
        """
        Creates a proposal for a change to the network that other members of the network
        can vote on, for example, a proposal to add a new member to the network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_proposal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#create_proposal)
        """
    def delete_accessor(self, *, AccessorId: str) -> Dict[str, Any]:
        """
        Deletes an accessor that your Amazon Web Services account owns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.delete_accessor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#delete_accessor)
        """
    def delete_member(self, *, NetworkId: str, MemberId: str) -> Dict[str, Any]:
        """
        Deletes a member.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.delete_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#delete_member)
        """
    def delete_node(self, *, NetworkId: str, NodeId: str, MemberId: str = None) -> Dict[str, Any]:
        """
        Deletes a node that your Amazon Web Services account owns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.delete_node)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#delete_node)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#generate_presigned_url)
        """
    def get_accessor(self, *, AccessorId: str) -> GetAccessorOutputTypeDef:
        """
        Returns detailed information about an accessor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_accessor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#get_accessor)
        """
    def get_member(self, *, NetworkId: str, MemberId: str) -> GetMemberOutputTypeDef:
        """
        Returns detailed information about a member.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#get_member)
        """
    def get_network(self, *, NetworkId: str) -> GetNetworkOutputTypeDef:
        """
        Returns detailed information about a network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#get_network)
        """
    def get_node(
        self, *, NetworkId: str, NodeId: str, MemberId: str = None
    ) -> GetNodeOutputTypeDef:
        """
        Returns detailed information about a node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_node)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#get_node)
        """
    def get_proposal(self, *, NetworkId: str, ProposalId: str) -> GetProposalOutputTypeDef:
        """
        Returns detailed information about a proposal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_proposal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#get_proposal)
        """
    def list_accessors(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        NetworkType: AccessorNetworkTypeType = None
    ) -> ListAccessorsOutputTypeDef:
        """
        Returns a list of the accessors and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_accessors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#list_accessors)
        """
    def list_invitations(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListInvitationsOutputTypeDef:
        """
        Returns a list of all invitations for the current Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#list_invitations)
        """
    def list_members(
        self,
        *,
        NetworkId: str,
        Name: str = None,
        Status: MemberStatusType = None,
        IsOwned: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListMembersOutputTypeDef:
        """
        Returns a list of the members in a network and properties of their
        configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#list_members)
        """
    def list_networks(
        self,
        *,
        Name: str = None,
        Framework: FrameworkType = None,
        Status: NetworkStatusType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListNetworksOutputTypeDef:
        """
        Returns information about the networks in which the current Amazon Web Services
        account participates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_networks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#list_networks)
        """
    def list_nodes(
        self,
        *,
        NetworkId: str,
        MemberId: str = None,
        Status: NodeStatusType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListNodesOutputTypeDef:
        """
        Returns information about the nodes within a network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_nodes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#list_nodes)
        """
    def list_proposal_votes(
        self, *, NetworkId: str, ProposalId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListProposalVotesOutputTypeDef:
        """
        Returns the list of votes for a specified proposal, including the value of each
        vote and the unique identifier of the member that cast the vote.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_proposal_votes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#list_proposal_votes)
        """
    def list_proposals(
        self, *, NetworkId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListProposalsOutputTypeDef:
        """
        Returns a list of proposals for the network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_proposals)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#list_proposals)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#list_tags_for_resource)
        """
    def reject_invitation(self, *, InvitationId: str) -> Dict[str, Any]:
        """
        Rejects an invitation to join a network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.reject_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#reject_invitation)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds or overwrites the specified tags for the specified Amazon Managed
        Blockchain resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the specified tags from the Amazon Managed Blockchain resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#untag_resource)
        """
    def update_member(
        self,
        *,
        NetworkId: str,
        MemberId: str,
        LogPublishingConfiguration: "MemberLogPublishingConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates a member configuration with new parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.update_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#update_member)
        """
    def update_node(
        self,
        *,
        NetworkId: str,
        NodeId: str,
        MemberId: str = None,
        LogPublishingConfiguration: "NodeLogPublishingConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates a node configuration with new parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.update_node)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#update_node)
        """
    def vote_on_proposal(
        self, *, NetworkId: str, ProposalId: str, VoterMemberId: str, Vote: VoteValueType
    ) -> Dict[str, Any]:
        """
        Casts a vote for a specified `ProposalId` on behalf of a member.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Client.vote_on_proposal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/client.html#vote_on_proposal)
        """
    def get_paginator(self, operation_name: Literal["list_accessors"]) -> ListAccessorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain.html#ManagedBlockchain.Paginator.ListAccessors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/paginators.html#listaccessorspaginator)
        """
