"""
Main interface for managedblockchain service client

Usage::

    ```python
    import boto3
    from mypy_boto3_managedblockchain import ManagedBlockchainClient

    client: ManagedBlockchainClient = boto3.client("managedblockchain")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_managedblockchain.type_defs import (
    CreateMemberOutputTypeDef,
    CreateNetworkOutputTypeDef,
    CreateNodeOutputTypeDef,
    CreateProposalOutputTypeDef,
    GetMemberOutputTypeDef,
    GetNetworkOutputTypeDef,
    GetNodeOutputTypeDef,
    GetProposalOutputTypeDef,
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


class ManagedBlockchainClient:
    """
    [ManagedBlockchain.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.can_paginate)
        """

    def create_member(
        self,
        ClientRequestToken: str,
        InvitationId: str,
        NetworkId: str,
        MemberConfiguration: MemberConfigurationTypeDef,
    ) -> CreateMemberOutputTypeDef:
        """
        [Client.create_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_member)
        """

    def create_network(
        self,
        ClientRequestToken: str,
        Name: str,
        Framework: Literal["HYPERLEDGER_FABRIC", "ETHEREUM"],
        FrameworkVersion: str,
        VotingPolicy: "VotingPolicyTypeDef",
        MemberConfiguration: MemberConfigurationTypeDef,
        Description: str = None,
        FrameworkConfiguration: NetworkFrameworkConfigurationTypeDef = None,
        Tags: Dict[str, str] = None,
    ) -> CreateNetworkOutputTypeDef:
        """
        [Client.create_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_network)
        """

    def create_node(
        self,
        ClientRequestToken: str,
        NetworkId: str,
        NodeConfiguration: NodeConfigurationTypeDef,
        MemberId: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateNodeOutputTypeDef:
        """
        [Client.create_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_node)
        """

    def create_proposal(
        self,
        ClientRequestToken: str,
        NetworkId: str,
        MemberId: str,
        Actions: "ProposalActionsTypeDef",
        Description: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateProposalOutputTypeDef:
        """
        [Client.create_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_proposal)
        """

    def delete_member(self, NetworkId: str, MemberId: str) -> Dict[str, Any]:
        """
        [Client.delete_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.delete_member)
        """

    def delete_node(self, NetworkId: str, NodeId: str, MemberId: str = None) -> Dict[str, Any]:
        """
        [Client.delete_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.delete_node)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.generate_presigned_url)
        """

    def get_member(self, NetworkId: str, MemberId: str) -> GetMemberOutputTypeDef:
        """
        [Client.get_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_member)
        """

    def get_network(self, NetworkId: str) -> GetNetworkOutputTypeDef:
        """
        [Client.get_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_network)
        """

    def get_node(self, NetworkId: str, NodeId: str, MemberId: str = None) -> GetNodeOutputTypeDef:
        """
        [Client.get_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_node)
        """

    def get_proposal(self, NetworkId: str, ProposalId: str) -> GetProposalOutputTypeDef:
        """
        [Client.get_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_proposal)
        """

    def list_invitations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListInvitationsOutputTypeDef:
        """
        [Client.list_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_invitations)
        """

    def list_members(
        self,
        NetworkId: str,
        Name: str = None,
        Status: Literal[
            "CREATING", "AVAILABLE", "CREATE_FAILED", "UPDATING", "DELETING", "DELETED"
        ] = None,
        IsOwned: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListMembersOutputTypeDef:
        """
        [Client.list_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_members)
        """

    def list_networks(
        self,
        Name: str = None,
        Framework: Literal["HYPERLEDGER_FABRIC", "ETHEREUM"] = None,
        Status: Literal["CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListNetworksOutputTypeDef:
        """
        [Client.list_networks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_networks)
        """

    def list_nodes(
        self,
        NetworkId: str,
        MemberId: str = None,
        Status: Literal[
            "CREATING",
            "AVAILABLE",
            "UNHEALTHY",
            "CREATE_FAILED",
            "UPDATING",
            "DELETING",
            "DELETED",
            "FAILED",
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListNodesOutputTypeDef:
        """
        [Client.list_nodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_nodes)
        """

    def list_proposal_votes(
        self, NetworkId: str, ProposalId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListProposalVotesOutputTypeDef:
        """
        [Client.list_proposal_votes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_proposal_votes)
        """

    def list_proposals(
        self, NetworkId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListProposalsOutputTypeDef:
        """
        [Client.list_proposals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_proposals)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_tags_for_resource)
        """

    def reject_invitation(self, InvitationId: str) -> Dict[str, Any]:
        """
        [Client.reject_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.reject_invitation)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.untag_resource)
        """

    def update_member(
        self,
        NetworkId: str,
        MemberId: str,
        LogPublishingConfiguration: "MemberLogPublishingConfigurationTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.update_member)
        """

    def update_node(
        self,
        NetworkId: str,
        NodeId: str,
        MemberId: str = None,
        LogPublishingConfiguration: "NodeLogPublishingConfigurationTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.update_node)
        """

    def vote_on_proposal(
        self, NetworkId: str, ProposalId: str, VoterMemberId: str, Vote: Literal["YES", "NO"]
    ) -> Dict[str, Any]:
        """
        [Client.vote_on_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/managedblockchain.html#ManagedBlockchain.Client.vote_on_proposal)
        """
