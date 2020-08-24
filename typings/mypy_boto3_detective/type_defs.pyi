"""
Main interface for detective service type definitions.

Usage::

    ```python
    from mypy_boto3_detective.type_defs import GraphTypeDef

    data: GraphTypeDef = {...}
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
    "GraphTypeDef",
    "MemberDetailTypeDef",
    "UnprocessedAccountTypeDef",
    "AccountTypeDef",
    "CreateGraphResponseTypeDef",
    "CreateMembersResponseTypeDef",
    "DeleteMembersResponseTypeDef",
    "GetMembersResponseTypeDef",
    "ListGraphsResponseTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListMembersResponseTypeDef",
)

GraphTypeDef = TypedDict("GraphTypeDef", {"Arn": str, "CreatedTime": datetime}, total=False)

MemberDetailTypeDef = TypedDict(
    "MemberDetailTypeDef",
    {
        "AccountId": str,
        "EmailAddress": str,
        "GraphArn": str,
        "MasterId": str,
        "Status": Literal[
            "INVITED",
            "VERIFICATION_IN_PROGRESS",
            "VERIFICATION_FAILED",
            "ENABLED",
            "ACCEPTED_BUT_DISABLED",
        ],
        "DisabledReason": Literal["VOLUME_TOO_HIGH", "VOLUME_UNKNOWN"],
        "InvitedTime": datetime,
        "UpdatedTime": datetime,
        "PercentOfGraphUtilization": float,
        "PercentOfGraphUtilizationUpdatedTime": datetime,
    },
    total=False,
)

UnprocessedAccountTypeDef = TypedDict(
    "UnprocessedAccountTypeDef", {"AccountId": str, "Reason": str}, total=False
)

AccountTypeDef = TypedDict("AccountTypeDef", {"AccountId": str, "EmailAddress": str})

CreateGraphResponseTypeDef = TypedDict("CreateGraphResponseTypeDef", {"GraphArn": str}, total=False)

CreateMembersResponseTypeDef = TypedDict(
    "CreateMembersResponseTypeDef",
    {
        "Members": List["MemberDetailTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
    },
    total=False,
)

DeleteMembersResponseTypeDef = TypedDict(
    "DeleteMembersResponseTypeDef",
    {"AccountIds": List[str], "UnprocessedAccounts": List["UnprocessedAccountTypeDef"]},
    total=False,
)

GetMembersResponseTypeDef = TypedDict(
    "GetMembersResponseTypeDef",
    {
        "MemberDetails": List["MemberDetailTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
    },
    total=False,
)

ListGraphsResponseTypeDef = TypedDict(
    "ListGraphsResponseTypeDef", {"GraphList": List["GraphTypeDef"], "NextToken": str}, total=False
)

ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {"Invitations": List["MemberDetailTypeDef"], "NextToken": str},
    total=False,
)

ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef",
    {"MemberDetails": List["MemberDetailTypeDef"], "NextToken": str},
    total=False,
)
