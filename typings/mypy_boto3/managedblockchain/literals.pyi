"""
Type annotations for managedblockchain service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/literals.html)

Usage::

    ```python
    from mypy_boto3_managedblockchain.literals import AccessorNetworkTypeType

    data: AccessorNetworkTypeType = "ETHEREUM_GOERLI"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccessorNetworkTypeType",
    "AccessorStatusType",
    "AccessorTypeType",
    "EditionType",
    "FrameworkType",
    "InvitationStatusType",
    "ListAccessorsPaginatorName",
    "MemberStatusType",
    "NetworkStatusType",
    "NodeStatusType",
    "ProposalStatusType",
    "StateDBTypeType",
    "ThresholdComparatorType",
    "VoteValueType",
)

AccessorNetworkTypeType = Literal[
    "ETHEREUM_GOERLI",
    "ETHEREUM_MAINNET",
    "ETHEREUM_MAINNET_AND_GOERLI",
    "POLYGON_MAINNET",
    "POLYGON_MUMBAI",
]
AccessorStatusType = Literal["AVAILABLE", "DELETED", "PENDING_DELETION"]
AccessorTypeType = Literal["BILLING_TOKEN"]
EditionType = Literal["STANDARD", "STARTER"]
FrameworkType = Literal["ETHEREUM", "HYPERLEDGER_FABRIC"]
InvitationStatusType = Literal["ACCEPTED", "ACCEPTING", "EXPIRED", "PENDING", "REJECTED"]
ListAccessorsPaginatorName = Literal["list_accessors"]
MemberStatusType = Literal[
    "AVAILABLE",
    "CREATE_FAILED",
    "CREATING",
    "DELETED",
    "DELETING",
    "INACCESSIBLE_ENCRYPTION_KEY",
    "UPDATING",
]
NetworkStatusType = Literal["AVAILABLE", "CREATE_FAILED", "CREATING", "DELETED", "DELETING"]
NodeStatusType = Literal[
    "AVAILABLE",
    "CREATE_FAILED",
    "CREATING",
    "DELETED",
    "DELETING",
    "FAILED",
    "INACCESSIBLE_ENCRYPTION_KEY",
    "UNHEALTHY",
    "UPDATING",
]
ProposalStatusType = Literal["ACTION_FAILED", "APPROVED", "EXPIRED", "IN_PROGRESS", "REJECTED"]
StateDBTypeType = Literal["CouchDB", "LevelDB"]
ThresholdComparatorType = Literal["GREATER_THAN", "GREATER_THAN_OR_EQUAL_TO"]
VoteValueType = Literal["NO", "YES"]
