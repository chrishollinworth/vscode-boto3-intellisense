"""
Main interface for managedblockchain service type definitions.

Usage::

    ```python
    from mypy_boto3_managedblockchain.type_defs import ApprovalThresholdPolicyTypeDef

    data: ApprovalThresholdPolicyTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApprovalThresholdPolicyTypeDef",
    "InvitationTypeDef",
    "InviteActionTypeDef",
    "LogConfigurationTypeDef",
    "LogConfigurationsTypeDef",
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
    "NetworkSummaryTypeDef",
    "NetworkTypeDef",
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
    "RemoveActionTypeDef",
    "ResponseMetadata",
    "VoteSummaryTypeDef",
    "VotingPolicyTypeDef",
    "CreateMemberOutputTypeDef",
    "CreateNetworkOutputTypeDef",
    "CreateNodeOutputTypeDef",
    "CreateProposalOutputTypeDef",
    "GetMemberOutputTypeDef",
    "GetNetworkOutputTypeDef",
    "GetNodeOutputTypeDef",
    "GetProposalOutputTypeDef",
    "ListInvitationsOutputTypeDef",
    "ListMembersOutputTypeDef",
    "ListNetworksOutputTypeDef",
    "ListNodesOutputTypeDef",
    "ListProposalVotesOutputTypeDef",
    "ListProposalsOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MemberConfigurationTypeDef",
    "NetworkFrameworkConfigurationTypeDef",
    "NodeConfigurationTypeDef",
)

ApprovalThresholdPolicyTypeDef = TypedDict(
    "ApprovalThresholdPolicyTypeDef",
    {
        "ThresholdPercentage": int,
        "ProposalDurationInHours": int,
        "ThresholdComparator": Literal["GREATER_THAN", "GREATER_THAN_OR_EQUAL_TO"],
    },
    total=False,
)

InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "InvitationId": str,
        "CreationDate": datetime,
        "ExpirationDate": datetime,
        "Status": Literal["PENDING", "ACCEPTED", "ACCEPTING", "REJECTED", "EXPIRED"],
        "NetworkSummary": "NetworkSummaryTypeDef",
        "Arn": str,
    },
    total=False,
)

InviteActionTypeDef = TypedDict("InviteActionTypeDef", {"Principal": str})

LogConfigurationTypeDef = TypedDict("LogConfigurationTypeDef", {"Enabled": bool}, total=False)

LogConfigurationsTypeDef = TypedDict(
    "LogConfigurationsTypeDef", {"Cloudwatch": "LogConfigurationTypeDef"}, total=False
)

MemberFabricAttributesTypeDef = TypedDict(
    "MemberFabricAttributesTypeDef", {"AdminUsername": str, "CaEndpoint": str}, total=False
)

MemberFabricConfigurationTypeDef = TypedDict(
    "MemberFabricConfigurationTypeDef", {"AdminUsername": str, "AdminPassword": str}
)

MemberFabricLogPublishingConfigurationTypeDef = TypedDict(
    "MemberFabricLogPublishingConfigurationTypeDef",
    {"CaLogs": "LogConfigurationsTypeDef"},
    total=False,
)

MemberFrameworkAttributesTypeDef = TypedDict(
    "MemberFrameworkAttributesTypeDef", {"Fabric": "MemberFabricAttributesTypeDef"}, total=False
)

MemberFrameworkConfigurationTypeDef = TypedDict(
    "MemberFrameworkConfigurationTypeDef",
    {"Fabric": "MemberFabricConfigurationTypeDef"},
    total=False,
)

MemberLogPublishingConfigurationTypeDef = TypedDict(
    "MemberLogPublishingConfigurationTypeDef",
    {"Fabric": "MemberFabricLogPublishingConfigurationTypeDef"},
    total=False,
)

MemberSummaryTypeDef = TypedDict(
    "MemberSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Status": Literal[
            "CREATING", "AVAILABLE", "CREATE_FAILED", "UPDATING", "DELETING", "DELETED"
        ],
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
        "Status": Literal[
            "CREATING", "AVAILABLE", "CREATE_FAILED", "UPDATING", "DELETING", "DELETED"
        ],
        "CreationDate": datetime,
        "Tags": Dict[str, str],
        "Arn": str,
    },
    total=False,
)

NetworkEthereumAttributesTypeDef = TypedDict(
    "NetworkEthereumAttributesTypeDef", {"ChainId": str}, total=False
)

NetworkFabricAttributesTypeDef = TypedDict(
    "NetworkFabricAttributesTypeDef",
    {"OrderingServiceEndpoint": str, "Edition": Literal["STARTER", "STANDARD"]},
    total=False,
)

NetworkFabricConfigurationTypeDef = TypedDict(
    "NetworkFabricConfigurationTypeDef", {"Edition": Literal["STARTER", "STANDARD"]}
)

NetworkFrameworkAttributesTypeDef = TypedDict(
    "NetworkFrameworkAttributesTypeDef",
    {"Fabric": "NetworkFabricAttributesTypeDef", "Ethereum": "NetworkEthereumAttributesTypeDef"},
    total=False,
)

NetworkSummaryTypeDef = TypedDict(
    "NetworkSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Framework": Literal["HYPERLEDGER_FABRIC", "ETHEREUM"],
        "FrameworkVersion": str,
        "Status": Literal["CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED"],
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
        "Framework": Literal["HYPERLEDGER_FABRIC", "ETHEREUM"],
        "FrameworkVersion": str,
        "FrameworkAttributes": "NetworkFrameworkAttributesTypeDef",
        "VpcEndpointServiceName": str,
        "VotingPolicy": "VotingPolicyTypeDef",
        "Status": Literal["CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED"],
        "CreationDate": datetime,
        "Tags": Dict[str, str],
        "Arn": str,
    },
    total=False,
)

NodeEthereumAttributesTypeDef = TypedDict(
    "NodeEthereumAttributesTypeDef", {"HttpEndpoint": str, "WebSocketEndpoint": str}, total=False
)

NodeFabricAttributesTypeDef = TypedDict(
    "NodeFabricAttributesTypeDef", {"PeerEndpoint": str, "PeerEventEndpoint": str}, total=False
)

NodeFabricLogPublishingConfigurationTypeDef = TypedDict(
    "NodeFabricLogPublishingConfigurationTypeDef",
    {"ChaincodeLogs": "LogConfigurationsTypeDef", "PeerLogs": "LogConfigurationsTypeDef"},
    total=False,
)

NodeFrameworkAttributesTypeDef = TypedDict(
    "NodeFrameworkAttributesTypeDef",
    {"Fabric": "NodeFabricAttributesTypeDef", "Ethereum": "NodeEthereumAttributesTypeDef"},
    total=False,
)

NodeLogPublishingConfigurationTypeDef = TypedDict(
    "NodeLogPublishingConfigurationTypeDef",
    {"Fabric": "NodeFabricLogPublishingConfigurationTypeDef"},
    total=False,
)

NodeSummaryTypeDef = TypedDict(
    "NodeSummaryTypeDef",
    {
        "Id": str,
        "Status": Literal[
            "CREATING",
            "AVAILABLE",
            "UNHEALTHY",
            "CREATE_FAILED",
            "UPDATING",
            "DELETING",
            "DELETED",
            "FAILED",
        ],
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
        "StateDB": Literal["LevelDB", "CouchDB"],
        "Status": Literal[
            "CREATING",
            "AVAILABLE",
            "UNHEALTHY",
            "CREATE_FAILED",
            "UPDATING",
            "DELETING",
            "DELETED",
            "FAILED",
        ],
        "CreationDate": datetime,
        "Tags": Dict[str, str],
        "Arn": str,
    },
    total=False,
)

ProposalActionsTypeDef = TypedDict(
    "ProposalActionsTypeDef",
    {"Invitations": List["InviteActionTypeDef"], "Removals": List["RemoveActionTypeDef"]},
    total=False,
)

ProposalSummaryTypeDef = TypedDict(
    "ProposalSummaryTypeDef",
    {
        "ProposalId": str,
        "Description": str,
        "ProposedByMemberId": str,
        "ProposedByMemberName": str,
        "Status": Literal["IN_PROGRESS", "APPROVED", "REJECTED", "EXPIRED", "ACTION_FAILED"],
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
        "Status": Literal["IN_PROGRESS", "APPROVED", "REJECTED", "EXPIRED", "ACTION_FAILED"],
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

RemoveActionTypeDef = TypedDict("RemoveActionTypeDef", {"MemberId": str})

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

VoteSummaryTypeDef = TypedDict(
    "VoteSummaryTypeDef",
    {"Vote": Literal["YES", "NO"], "MemberName": str, "MemberId": str},
    total=False,
)

VotingPolicyTypeDef = TypedDict(
    "VotingPolicyTypeDef",
    {"ApprovalThresholdPolicy": "ApprovalThresholdPolicyTypeDef"},
    total=False,
)

CreateMemberOutputTypeDef = TypedDict(
    "CreateMemberOutputTypeDef",
    {"MemberId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateNetworkOutputTypeDef = TypedDict(
    "CreateNetworkOutputTypeDef",
    {"NetworkId": str, "MemberId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateNodeOutputTypeDef = TypedDict(
    "CreateNodeOutputTypeDef", {"NodeId": str, "ResponseMetadata": "ResponseMetadata"}, total=False
)

CreateProposalOutputTypeDef = TypedDict(
    "CreateProposalOutputTypeDef",
    {"ProposalId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetMemberOutputTypeDef = TypedDict(
    "GetMemberOutputTypeDef",
    {"Member": "MemberTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetNetworkOutputTypeDef = TypedDict(
    "GetNetworkOutputTypeDef",
    {"Network": "NetworkTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetNodeOutputTypeDef = TypedDict(
    "GetNodeOutputTypeDef",
    {"Node": "NodeTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetProposalOutputTypeDef = TypedDict(
    "GetProposalOutputTypeDef",
    {"Proposal": "ProposalTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListInvitationsOutputTypeDef = TypedDict(
    "ListInvitationsOutputTypeDef",
    {
        "Invitations": List["InvitationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListMembersOutputTypeDef = TypedDict(
    "ListMembersOutputTypeDef",
    {
        "Members": List["MemberSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListNetworksOutputTypeDef = TypedDict(
    "ListNetworksOutputTypeDef",
    {
        "Networks": List["NetworkSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListNodesOutputTypeDef = TypedDict(
    "ListNodesOutputTypeDef",
    {"Nodes": List["NodeSummaryTypeDef"], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListProposalVotesOutputTypeDef = TypedDict(
    "ListProposalVotesOutputTypeDef",
    {
        "ProposalVotes": List["VoteSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListProposalsOutputTypeDef = TypedDict(
    "ListProposalsOutputTypeDef",
    {
        "Proposals": List["ProposalSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

_RequiredMemberConfigurationTypeDef = TypedDict(
    "_RequiredMemberConfigurationTypeDef",
    {"Name": str, "FrameworkConfiguration": "MemberFrameworkConfigurationTypeDef"},
)
_OptionalMemberConfigurationTypeDef = TypedDict(
    "_OptionalMemberConfigurationTypeDef",
    {
        "Description": str,
        "LogPublishingConfiguration": "MemberLogPublishingConfigurationTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)


class MemberConfigurationTypeDef(
    _RequiredMemberConfigurationTypeDef, _OptionalMemberConfigurationTypeDef
):
    pass


NetworkFrameworkConfigurationTypeDef = TypedDict(
    "NetworkFrameworkConfigurationTypeDef",
    {"Fabric": "NetworkFabricConfigurationTypeDef"},
    total=False,
)

_RequiredNodeConfigurationTypeDef = TypedDict(
    "_RequiredNodeConfigurationTypeDef", {"InstanceType": str}
)
_OptionalNodeConfigurationTypeDef = TypedDict(
    "_OptionalNodeConfigurationTypeDef",
    {
        "AvailabilityZone": str,
        "LogPublishingConfiguration": "NodeLogPublishingConfigurationTypeDef",
        "StateDB": Literal["LevelDB", "CouchDB"],
    },
    total=False,
)


class NodeConfigurationTypeDef(
    _RequiredNodeConfigurationTypeDef, _OptionalNodeConfigurationTypeDef
):
    pass
