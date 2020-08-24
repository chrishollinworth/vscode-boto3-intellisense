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
from typing import List

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
    "NetworkFabricAttributesTypeDef",
    "NetworkFabricConfigurationTypeDef",
    "NetworkFrameworkAttributesTypeDef",
    "NetworkSummaryTypeDef",
    "NetworkTypeDef",
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
    },
    total=False,
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
    "NetworkFrameworkAttributesTypeDef", {"Fabric": "NetworkFabricAttributesTypeDef"}, total=False
)

NetworkSummaryTypeDef = TypedDict(
    "NetworkSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Framework": Literal["HYPERLEDGER_FABRIC"],
        "FrameworkVersion": str,
        "Status": Literal["CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED"],
        "CreationDate": datetime,
    },
    total=False,
)

NetworkTypeDef = TypedDict(
    "NetworkTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Framework": Literal["HYPERLEDGER_FABRIC"],
        "FrameworkVersion": str,
        "FrameworkAttributes": "NetworkFrameworkAttributesTypeDef",
        "VpcEndpointServiceName": str,
        "VotingPolicy": "VotingPolicyTypeDef",
        "Status": Literal["CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED"],
        "CreationDate": datetime,
    },
    total=False,
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
    "NodeFrameworkAttributesTypeDef", {"Fabric": "NodeFabricAttributesTypeDef"}, total=False
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
            "CREATING", "AVAILABLE", "CREATE_FAILED", "UPDATING", "DELETING", "DELETED", "FAILED"
        ],
        "CreationDate": datetime,
        "AvailabilityZone": str,
        "InstanceType": str,
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
        "Status": Literal[
            "CREATING", "AVAILABLE", "CREATE_FAILED", "UPDATING", "DELETING", "DELETED", "FAILED"
        ],
        "CreationDate": datetime,
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
    },
    total=False,
)

RemoveActionTypeDef = TypedDict("RemoveActionTypeDef", {"MemberId": str})

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

CreateMemberOutputTypeDef = TypedDict("CreateMemberOutputTypeDef", {"MemberId": str}, total=False)

CreateNetworkOutputTypeDef = TypedDict(
    "CreateNetworkOutputTypeDef", {"NetworkId": str, "MemberId": str}, total=False
)

CreateNodeOutputTypeDef = TypedDict("CreateNodeOutputTypeDef", {"NodeId": str}, total=False)

CreateProposalOutputTypeDef = TypedDict(
    "CreateProposalOutputTypeDef", {"ProposalId": str}, total=False
)

GetMemberOutputTypeDef = TypedDict(
    "GetMemberOutputTypeDef", {"Member": "MemberTypeDef"}, total=False
)

GetNetworkOutputTypeDef = TypedDict(
    "GetNetworkOutputTypeDef", {"Network": "NetworkTypeDef"}, total=False
)

GetNodeOutputTypeDef = TypedDict("GetNodeOutputTypeDef", {"Node": "NodeTypeDef"}, total=False)

GetProposalOutputTypeDef = TypedDict(
    "GetProposalOutputTypeDef", {"Proposal": "ProposalTypeDef"}, total=False
)

ListInvitationsOutputTypeDef = TypedDict(
    "ListInvitationsOutputTypeDef",
    {"Invitations": List["InvitationTypeDef"], "NextToken": str},
    total=False,
)

ListMembersOutputTypeDef = TypedDict(
    "ListMembersOutputTypeDef",
    {"Members": List["MemberSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListNetworksOutputTypeDef = TypedDict(
    "ListNetworksOutputTypeDef",
    {"Networks": List["NetworkSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListNodesOutputTypeDef = TypedDict(
    "ListNodesOutputTypeDef", {"Nodes": List["NodeSummaryTypeDef"], "NextToken": str}, total=False
)

ListProposalVotesOutputTypeDef = TypedDict(
    "ListProposalVotesOutputTypeDef",
    {"ProposalVotes": List["VoteSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListProposalsOutputTypeDef = TypedDict(
    "ListProposalsOutputTypeDef",
    {"Proposals": List["ProposalSummaryTypeDef"], "NextToken": str},
    total=False,
)

_RequiredMemberConfigurationTypeDef = TypedDict(
    "_RequiredMemberConfigurationTypeDef",
    {"Name": str, "FrameworkConfiguration": "MemberFrameworkConfigurationTypeDef"},
)
_OptionalMemberConfigurationTypeDef = TypedDict(
    "_OptionalMemberConfigurationTypeDef",
    {"Description": str, "LogPublishingConfiguration": "MemberLogPublishingConfigurationTypeDef"},
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
    "_RequiredNodeConfigurationTypeDef", {"InstanceType": str, "AvailabilityZone": str}
)
_OptionalNodeConfigurationTypeDef = TypedDict(
    "_OptionalNodeConfigurationTypeDef",
    {"LogPublishingConfiguration": "NodeLogPublishingConfigurationTypeDef"},
    total=False,
)


class NodeConfigurationTypeDef(
    _RequiredNodeConfigurationTypeDef, _OptionalNodeConfigurationTypeDef
):
    pass
