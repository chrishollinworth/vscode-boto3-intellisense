"""
Type annotations for managedblockchain service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/type_defs.html)

Usage::

    ```python
    from mypy_boto3_managedblockchain.type_defs import ApprovalThresholdPolicyTypeDef

    data: ApprovalThresholdPolicyTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    EditionType,
    FrameworkType,
    InvitationStatusType,
    MemberStatusType,
    NetworkStatusType,
    NodeStatusType,
    ProposalStatusType,
    StateDBTypeType,
    ThresholdComparatorType,
    VoteValueType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ApprovalThresholdPolicyTypeDef",
    "CreateMemberInputRequestTypeDef",
    "CreateMemberOutputTypeDef",
    "CreateNetworkInputRequestTypeDef",
    "CreateNetworkOutputTypeDef",
    "CreateNodeInputRequestTypeDef",
    "CreateNodeOutputTypeDef",
    "CreateProposalInputRequestTypeDef",
    "CreateProposalOutputTypeDef",
    "DeleteMemberInputRequestTypeDef",
    "DeleteNodeInputRequestTypeDef",
    "GetMemberInputRequestTypeDef",
    "GetMemberOutputTypeDef",
    "GetNetworkInputRequestTypeDef",
    "GetNetworkOutputTypeDef",
    "GetNodeInputRequestTypeDef",
    "GetNodeOutputTypeDef",
    "GetProposalInputRequestTypeDef",
    "GetProposalOutputTypeDef",
    "InvitationTypeDef",
    "InviteActionTypeDef",
    "ListInvitationsInputRequestTypeDef",
    "ListInvitationsOutputTypeDef",
    "ListMembersInputRequestTypeDef",
    "ListMembersOutputTypeDef",
    "ListNetworksInputRequestTypeDef",
    "ListNetworksOutputTypeDef",
    "ListNodesInputRequestTypeDef",
    "ListNodesOutputTypeDef",
    "ListProposalVotesInputRequestTypeDef",
    "ListProposalVotesOutputTypeDef",
    "ListProposalsInputRequestTypeDef",
    "ListProposalsOutputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogConfigurationTypeDef",
    "LogConfigurationsTypeDef",
    "MemberConfigurationTypeDef",
    "MemberFabricAttributesTypeDef",
    "MemberFabricConfigurationTypeDef",
    "MemberFabricLogPublishingConfigurationTypeDef",
    "MemberFrameworkAttributesTypeDef",
    "MemberFrameworkConfigurationTypeDef",
    "MemberLogPublishingConfigurationTypeDef",
    "MemberSummaryTypeDef",
    "MemberTypeDef",
    "NetworkEthereumAttributesTypeDef",
    "NetworkFabricAttributesTypeDef",
    "NetworkFabricConfigurationTypeDef",
    "NetworkFrameworkAttributesTypeDef",
    "NetworkFrameworkConfigurationTypeDef",
    "NetworkSummaryTypeDef",
    "NetworkTypeDef",
    "NodeConfigurationTypeDef",
    "NodeEthereumAttributesTypeDef",
    "NodeFabricAttributesTypeDef",
    "NodeFabricLogPublishingConfigurationTypeDef",
    "NodeFrameworkAttributesTypeDef",
    "NodeLogPublishingConfigurationTypeDef",
    "NodeSummaryTypeDef",
    "NodeTypeDef",
    "ProposalActionsTypeDef",
    "ProposalSummaryTypeDef",
    "ProposalTypeDef",
    "RejectInvitationInputRequestTypeDef",
    "RemoveActionTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateMemberInputRequestTypeDef",
    "UpdateNodeInputRequestTypeDef",
    "VoteOnProposalInputRequestTypeDef",
    "VoteSummaryTypeDef",
    "VotingPolicyTypeDef",
)

ApprovalThresholdPolicyTypeDef = TypedDict(
    "ApprovalThresholdPolicyTypeDef",
    {
        "ThresholdPercentage": int,
        "ProposalDurationInHours": int,
        "ThresholdComparator": ThresholdComparatorType,
    },
    total=False,
)

CreateMemberInputRequestTypeDef = TypedDict(
    "CreateMemberInputRequestTypeDef",
    {
        "ClientRequestToken": str,
        "InvitationId": str,
        "NetworkId": str,
        "MemberConfiguration": "MemberConfigurationTypeDef",
    },
)

CreateMemberOutputTypeDef = TypedDict(
    "CreateMemberOutputTypeDef",
    {
        "MemberId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNetworkInputRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkInputRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Name": str,
        "Framework": FrameworkType,
        "FrameworkVersion": str,
        "VotingPolicy": "VotingPolicyTypeDef",
        "MemberConfiguration": "MemberConfigurationTypeDef",
    },
)
_OptionalCreateNetworkInputRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkInputRequestTypeDef",
    {
        "Description": str,
        "FrameworkConfiguration": "NetworkFrameworkConfigurationTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateNetworkInputRequestTypeDef(
    _RequiredCreateNetworkInputRequestTypeDef, _OptionalCreateNetworkInputRequestTypeDef
):
    pass

CreateNetworkOutputTypeDef = TypedDict(
    "CreateNetworkOutputTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNodeInputRequestTypeDef = TypedDict(
    "_RequiredCreateNodeInputRequestTypeDef",
    {
        "ClientRequestToken": str,
        "NetworkId": str,
        "NodeConfiguration": "NodeConfigurationTypeDef",
    },
)
_OptionalCreateNodeInputRequestTypeDef = TypedDict(
    "_OptionalCreateNodeInputRequestTypeDef",
    {
        "MemberId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateNodeInputRequestTypeDef(
    _RequiredCreateNodeInputRequestTypeDef, _OptionalCreateNodeInputRequestTypeDef
):
    pass

CreateNodeOutputTypeDef = TypedDict(
    "CreateNodeOutputTypeDef",
    {
        "NodeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProposalInputRequestTypeDef = TypedDict(
    "_RequiredCreateProposalInputRequestTypeDef",
    {
        "ClientRequestToken": str,
        "NetworkId": str,
        "MemberId": str,
        "Actions": "ProposalActionsTypeDef",
    },
)
_OptionalCreateProposalInputRequestTypeDef = TypedDict(
    "_OptionalCreateProposalInputRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateProposalInputRequestTypeDef(
    _RequiredCreateProposalInputRequestTypeDef, _OptionalCreateProposalInputRequestTypeDef
):
    pass

CreateProposalOutputTypeDef = TypedDict(
    "CreateProposalOutputTypeDef",
    {
        "ProposalId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMemberInputRequestTypeDef = TypedDict(
    "DeleteMemberInputRequestTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
    },
)

_RequiredDeleteNodeInputRequestTypeDef = TypedDict(
    "_RequiredDeleteNodeInputRequestTypeDef",
    {
        "NetworkId": str,
        "NodeId": str,
    },
)
_OptionalDeleteNodeInputRequestTypeDef = TypedDict(
    "_OptionalDeleteNodeInputRequestTypeDef",
    {
        "MemberId": str,
    },
    total=False,
)

class DeleteNodeInputRequestTypeDef(
    _RequiredDeleteNodeInputRequestTypeDef, _OptionalDeleteNodeInputRequestTypeDef
):
    pass

GetMemberInputRequestTypeDef = TypedDict(
    "GetMemberInputRequestTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
    },
)

GetMemberOutputTypeDef = TypedDict(
    "GetMemberOutputTypeDef",
    {
        "Member": "MemberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkInputRequestTypeDef = TypedDict(
    "GetNetworkInputRequestTypeDef",
    {
        "NetworkId": str,
    },
)

GetNetworkOutputTypeDef = TypedDict(
    "GetNetworkOutputTypeDef",
    {
        "Network": "NetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetNodeInputRequestTypeDef = TypedDict(
    "_RequiredGetNodeInputRequestTypeDef",
    {
        "NetworkId": str,
        "NodeId": str,
    },
)
_OptionalGetNodeInputRequestTypeDef = TypedDict(
    "_OptionalGetNodeInputRequestTypeDef",
    {
        "MemberId": str,
    },
    total=False,
)

class GetNodeInputRequestTypeDef(
    _RequiredGetNodeInputRequestTypeDef, _OptionalGetNodeInputRequestTypeDef
):
    pass

GetNodeOutputTypeDef = TypedDict(
    "GetNodeOutputTypeDef",
    {
        "Node": "NodeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProposalInputRequestTypeDef = TypedDict(
    "GetProposalInputRequestTypeDef",
    {
        "NetworkId": str,
        "ProposalId": str,
    },
)

GetProposalOutputTypeDef = TypedDict(
    "GetProposalOutputTypeDef",
    {
        "Proposal": "ProposalTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "InvitationId": str,
        "CreationDate": datetime,
        "ExpirationDate": datetime,
        "Status": InvitationStatusType,
        "NetworkSummary": "NetworkSummaryTypeDef",
        "Arn": str,
    },
    total=False,
)

InviteActionTypeDef = TypedDict(
    "InviteActionTypeDef",
    {
        "Principal": str,
    },
)

ListInvitationsInputRequestTypeDef = TypedDict(
    "ListInvitationsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListInvitationsOutputTypeDef = TypedDict(
    "ListInvitationsOutputTypeDef",
    {
        "Invitations": List["InvitationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMembersInputRequestTypeDef = TypedDict(
    "_RequiredListMembersInputRequestTypeDef",
    {
        "NetworkId": str,
    },
)
_OptionalListMembersInputRequestTypeDef = TypedDict(
    "_OptionalListMembersInputRequestTypeDef",
    {
        "Name": str,
        "Status": MemberStatusType,
        "IsOwned": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListMembersInputRequestTypeDef(
    _RequiredListMembersInputRequestTypeDef, _OptionalListMembersInputRequestTypeDef
):
    pass

ListMembersOutputTypeDef = TypedDict(
    "ListMembersOutputTypeDef",
    {
        "Members": List["MemberSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNetworksInputRequestTypeDef = TypedDict(
    "ListNetworksInputRequestTypeDef",
    {
        "Name": str,
        "Framework": FrameworkType,
        "Status": NetworkStatusType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListNetworksOutputTypeDef = TypedDict(
    "ListNetworksOutputTypeDef",
    {
        "Networks": List["NetworkSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListNodesInputRequestTypeDef = TypedDict(
    "_RequiredListNodesInputRequestTypeDef",
    {
        "NetworkId": str,
    },
)
_OptionalListNodesInputRequestTypeDef = TypedDict(
    "_OptionalListNodesInputRequestTypeDef",
    {
        "MemberId": str,
        "Status": NodeStatusType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListNodesInputRequestTypeDef(
    _RequiredListNodesInputRequestTypeDef, _OptionalListNodesInputRequestTypeDef
):
    pass

ListNodesOutputTypeDef = TypedDict(
    "ListNodesOutputTypeDef",
    {
        "Nodes": List["NodeSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProposalVotesInputRequestTypeDef = TypedDict(
    "_RequiredListProposalVotesInputRequestTypeDef",
    {
        "NetworkId": str,
        "ProposalId": str,
    },
)
_OptionalListProposalVotesInputRequestTypeDef = TypedDict(
    "_OptionalListProposalVotesInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListProposalVotesInputRequestTypeDef(
    _RequiredListProposalVotesInputRequestTypeDef, _OptionalListProposalVotesInputRequestTypeDef
):
    pass

ListProposalVotesOutputTypeDef = TypedDict(
    "ListProposalVotesOutputTypeDef",
    {
        "ProposalVotes": List["VoteSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProposalsInputRequestTypeDef = TypedDict(
    "_RequiredListProposalsInputRequestTypeDef",
    {
        "NetworkId": str,
    },
)
_OptionalListProposalsInputRequestTypeDef = TypedDict(
    "_OptionalListProposalsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListProposalsInputRequestTypeDef(
    _RequiredListProposalsInputRequestTypeDef, _OptionalListProposalsInputRequestTypeDef
):
    pass

ListProposalsOutputTypeDef = TypedDict(
    "ListProposalsOutputTypeDef",
    {
        "Proposals": List["ProposalSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogConfigurationTypeDef = TypedDict(
    "LogConfigurationTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

LogConfigurationsTypeDef = TypedDict(
    "LogConfigurationsTypeDef",
    {
        "Cloudwatch": "LogConfigurationTypeDef",
    },
    total=False,
)

_RequiredMemberConfigurationTypeDef = TypedDict(
    "_RequiredMemberConfigurationTypeDef",
    {
        "Name": str,
        "FrameworkConfiguration": "MemberFrameworkConfigurationTypeDef",
    },
)
_OptionalMemberConfigurationTypeDef = TypedDict(
    "_OptionalMemberConfigurationTypeDef",
    {
        "Description": str,
        "LogPublishingConfiguration": "MemberLogPublishingConfigurationTypeDef",
        "Tags": Dict[str, str],
        "KmsKeyArn": str,
    },
    total=False,
)

class MemberConfigurationTypeDef(
    _RequiredMemberConfigurationTypeDef, _OptionalMemberConfigurationTypeDef
):
    pass

MemberFabricAttributesTypeDef = TypedDict(
    "MemberFabricAttributesTypeDef",
    {
        "AdminUsername": str,
        "CaEndpoint": str,
    },
    total=False,
)

MemberFabricConfigurationTypeDef = TypedDict(
    "MemberFabricConfigurationTypeDef",
    {
        "AdminUsername": str,
        "AdminPassword": str,
    },
)

MemberFabricLogPublishingConfigurationTypeDef = TypedDict(
    "MemberFabricLogPublishingConfigurationTypeDef",
    {
        "CaLogs": "LogConfigurationsTypeDef",
    },
    total=False,
)

MemberFrameworkAttributesTypeDef = TypedDict(
    "MemberFrameworkAttributesTypeDef",
    {
        "Fabric": "MemberFabricAttributesTypeDef",
    },
    total=False,
)

MemberFrameworkConfigurationTypeDef = TypedDict(
    "MemberFrameworkConfigurationTypeDef",
    {
        "Fabric": "MemberFabricConfigurationTypeDef",
    },
    total=False,
)

MemberLogPublishingConfigurationTypeDef = TypedDict(
    "MemberLogPublishingConfigurationTypeDef",
    {
        "Fabric": "MemberFabricLogPublishingConfigurationTypeDef",
    },
    total=False,
)

MemberSummaryTypeDef = TypedDict(
    "MemberSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Status": MemberStatusType,
        "CreationDate": datetime,
        "IsOwned": bool,
        "Arn": str,
    },
    total=False,
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "NetworkId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "FrameworkAttributes": "MemberFrameworkAttributesTypeDef",
        "LogPublishingConfiguration": "MemberLogPublishingConfigurationTypeDef",
        "Status": MemberStatusType,
        "CreationDate": datetime,
        "Tags": Dict[str, str],
        "Arn": str,
        "KmsKeyArn": str,
    },
    total=False,
)

NetworkEthereumAttributesTypeDef = TypedDict(
    "NetworkEthereumAttributesTypeDef",
    {
        "ChainId": str,
    },
    total=False,
)

NetworkFabricAttributesTypeDef = TypedDict(
    "NetworkFabricAttributesTypeDef",
    {
        "OrderingServiceEndpoint": str,
        "Edition": EditionType,
    },
    total=False,
)

NetworkFabricConfigurationTypeDef = TypedDict(
    "NetworkFabricConfigurationTypeDef",
    {
        "Edition": EditionType,
    },
)

NetworkFrameworkAttributesTypeDef = TypedDict(
    "NetworkFrameworkAttributesTypeDef",
    {
        "Fabric": "NetworkFabricAttributesTypeDef",
        "Ethereum": "NetworkEthereumAttributesTypeDef",
    },
    total=False,
)

NetworkFrameworkConfigurationTypeDef = TypedDict(
    "NetworkFrameworkConfigurationTypeDef",
    {
        "Fabric": "NetworkFabricConfigurationTypeDef",
    },
    total=False,
)

NetworkSummaryTypeDef = TypedDict(
    "NetworkSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Framework": FrameworkType,
        "FrameworkVersion": str,
        "Status": NetworkStatusType,
        "CreationDate": datetime,
        "Arn": str,
    },
    total=False,
)

NetworkTypeDef = TypedDict(
    "NetworkTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Framework": FrameworkType,
        "FrameworkVersion": str,
        "FrameworkAttributes": "NetworkFrameworkAttributesTypeDef",
        "VpcEndpointServiceName": str,
        "VotingPolicy": "VotingPolicyTypeDef",
        "Status": NetworkStatusType,
        "CreationDate": datetime,
        "Tags": Dict[str, str],
        "Arn": str,
    },
    total=False,
)

_RequiredNodeConfigurationTypeDef = TypedDict(
    "_RequiredNodeConfigurationTypeDef",
    {
        "InstanceType": str,
    },
)
_OptionalNodeConfigurationTypeDef = TypedDict(
    "_OptionalNodeConfigurationTypeDef",
    {
        "AvailabilityZone": str,
        "LogPublishingConfiguration": "NodeLogPublishingConfigurationTypeDef",
        "StateDB": StateDBTypeType,
    },
    total=False,
)

class NodeConfigurationTypeDef(
    _RequiredNodeConfigurationTypeDef, _OptionalNodeConfigurationTypeDef
):
    pass

NodeEthereumAttributesTypeDef = TypedDict(
    "NodeEthereumAttributesTypeDef",
    {
        "HttpEndpoint": str,
        "WebSocketEndpoint": str,
    },
    total=False,
)

NodeFabricAttributesTypeDef = TypedDict(
    "NodeFabricAttributesTypeDef",
    {
        "PeerEndpoint": str,
        "PeerEventEndpoint": str,
    },
    total=False,
)

NodeFabricLogPublishingConfigurationTypeDef = TypedDict(
    "NodeFabricLogPublishingConfigurationTypeDef",
    {
        "ChaincodeLogs": "LogConfigurationsTypeDef",
        "PeerLogs": "LogConfigurationsTypeDef",
    },
    total=False,
)

NodeFrameworkAttributesTypeDef = TypedDict(
    "NodeFrameworkAttributesTypeDef",
    {
        "Fabric": "NodeFabricAttributesTypeDef",
        "Ethereum": "NodeEthereumAttributesTypeDef",
    },
    total=False,
)

NodeLogPublishingConfigurationTypeDef = TypedDict(
    "NodeLogPublishingConfigurationTypeDef",
    {
        "Fabric": "NodeFabricLogPublishingConfigurationTypeDef",
    },
    total=False,
)

NodeSummaryTypeDef = TypedDict(
    "NodeSummaryTypeDef",
    {
        "Id": str,
        "Status": NodeStatusType,
        "CreationDate": datetime,
        "AvailabilityZone": str,
        "InstanceType": str,
        "Arn": str,
    },
    total=False,
)

NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
        "Id": str,
        "InstanceType": str,
        "AvailabilityZone": str,
        "FrameworkAttributes": "NodeFrameworkAttributesTypeDef",
        "LogPublishingConfiguration": "NodeLogPublishingConfigurationTypeDef",
        "StateDB": StateDBTypeType,
        "Status": NodeStatusType,
        "CreationDate": datetime,
        "Tags": Dict[str, str],
        "Arn": str,
        "KmsKeyArn": str,
    },
    total=False,
)

ProposalActionsTypeDef = TypedDict(
    "ProposalActionsTypeDef",
    {
        "Invitations": List["InviteActionTypeDef"],
        "Removals": List["RemoveActionTypeDef"],
    },
    total=False,
)

ProposalSummaryTypeDef = TypedDict(
    "ProposalSummaryTypeDef",
    {
        "ProposalId": str,
        "Description": str,
        "ProposedByMemberId": str,
        "ProposedByMemberName": str,
        "Status": ProposalStatusType,
        "CreationDate": datetime,
        "ExpirationDate": datetime,
        "Arn": str,
    },
    total=False,
)

ProposalTypeDef = TypedDict(
    "ProposalTypeDef",
    {
        "ProposalId": str,
        "NetworkId": str,
        "Description": str,
        "Actions": "ProposalActionsTypeDef",
        "ProposedByMemberId": str,
        "ProposedByMemberName": str,
        "Status": ProposalStatusType,
        "CreationDate": datetime,
        "ExpirationDate": datetime,
        "YesVoteCount": int,
        "NoVoteCount": int,
        "OutstandingVoteCount": int,
        "Tags": Dict[str, str],
        "Arn": str,
    },
    total=False,
)

RejectInvitationInputRequestTypeDef = TypedDict(
    "RejectInvitationInputRequestTypeDef",
    {
        "InvitationId": str,
    },
)

RemoveActionTypeDef = TypedDict(
    "RemoveActionTypeDef",
    {
        "MemberId": str,
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateMemberInputRequestTypeDef = TypedDict(
    "_RequiredUpdateMemberInputRequestTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
    },
)
_OptionalUpdateMemberInputRequestTypeDef = TypedDict(
    "_OptionalUpdateMemberInputRequestTypeDef",
    {
        "LogPublishingConfiguration": "MemberLogPublishingConfigurationTypeDef",
    },
    total=False,
)

class UpdateMemberInputRequestTypeDef(
    _RequiredUpdateMemberInputRequestTypeDef, _OptionalUpdateMemberInputRequestTypeDef
):
    pass

_RequiredUpdateNodeInputRequestTypeDef = TypedDict(
    "_RequiredUpdateNodeInputRequestTypeDef",
    {
        "NetworkId": str,
        "NodeId": str,
    },
)
_OptionalUpdateNodeInputRequestTypeDef = TypedDict(
    "_OptionalUpdateNodeInputRequestTypeDef",
    {
        "MemberId": str,
        "LogPublishingConfiguration": "NodeLogPublishingConfigurationTypeDef",
    },
    total=False,
)

class UpdateNodeInputRequestTypeDef(
    _RequiredUpdateNodeInputRequestTypeDef, _OptionalUpdateNodeInputRequestTypeDef
):
    pass

VoteOnProposalInputRequestTypeDef = TypedDict(
    "VoteOnProposalInputRequestTypeDef",
    {
        "NetworkId": str,
        "ProposalId": str,
        "VoterMemberId": str,
        "Vote": VoteValueType,
    },
)

VoteSummaryTypeDef = TypedDict(
    "VoteSummaryTypeDef",
    {
        "Vote": VoteValueType,
        "MemberName": str,
        "MemberId": str,
    },
    total=False,
)

VotingPolicyTypeDef = TypedDict(
    "VotingPolicyTypeDef",
    {
        "ApprovalThresholdPolicy": "ApprovalThresholdPolicyTypeDef",
    },
    total=False,
)
