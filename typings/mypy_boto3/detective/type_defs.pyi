"""
Type annotations for detective service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/type_defs.html)

Usage::

    ```python
    from mypy_boto3_detective.type_defs import AcceptInvitationRequestRequestTypeDef

    data: AcceptInvitationRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import InvitationTypeType, MemberDisabledReasonType, MemberStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AcceptInvitationRequestRequestTypeDef",
    "AccountTypeDef",
    "AdministratorTypeDef",
    "CreateGraphRequestRequestTypeDef",
    "CreateGraphResponseTypeDef",
    "CreateMembersRequestRequestTypeDef",
    "CreateMembersResponseTypeDef",
    "DeleteGraphRequestRequestTypeDef",
    "DeleteMembersRequestRequestTypeDef",
    "DeleteMembersResponseTypeDef",
    "DescribeOrganizationConfigurationRequestRequestTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DisassociateMembershipRequestRequestTypeDef",
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    "GetMembersRequestRequestTypeDef",
    "GetMembersResponseTypeDef",
    "GraphTypeDef",
    "ListGraphsRequestRequestTypeDef",
    "ListGraphsResponseTypeDef",
    "ListInvitationsRequestRequestTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListMembersRequestRequestTypeDef",
    "ListMembersResponseTypeDef",
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MemberDetailTypeDef",
    "RejectInvitationRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "StartMonitoringMemberRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UnprocessedAccountTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
)

AcceptInvitationRequestRequestTypeDef = TypedDict(
    "AcceptInvitationRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)

AccountTypeDef = TypedDict(
    "AccountTypeDef",
    {
        "AccountId": str,
        "EmailAddress": str,
    },
)

AdministratorTypeDef = TypedDict(
    "AdministratorTypeDef",
    {
        "AccountId": str,
        "GraphArn": str,
        "DelegationTime": datetime,
    },
    total=False,
)

CreateGraphRequestRequestTypeDef = TypedDict(
    "CreateGraphRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

CreateGraphResponseTypeDef = TypedDict(
    "CreateGraphResponseTypeDef",
    {
        "GraphArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMembersRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMembersRequestRequestTypeDef",
    {
        "GraphArn": str,
        "Accounts": List["AccountTypeDef"],
    },
)
_OptionalCreateMembersRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMembersRequestRequestTypeDef",
    {
        "Message": str,
        "DisableEmailNotification": bool,
    },
    total=False,
)

class CreateMembersRequestRequestTypeDef(
    _RequiredCreateMembersRequestRequestTypeDef, _OptionalCreateMembersRequestRequestTypeDef
):
    pass

CreateMembersResponseTypeDef = TypedDict(
    "CreateMembersResponseTypeDef",
    {
        "Members": List["MemberDetailTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGraphRequestRequestTypeDef = TypedDict(
    "DeleteGraphRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)

DeleteMembersRequestRequestTypeDef = TypedDict(
    "DeleteMembersRequestRequestTypeDef",
    {
        "GraphArn": str,
        "AccountIds": List[str],
    },
)

DeleteMembersResponseTypeDef = TypedDict(
    "DeleteMembersResponseTypeDef",
    {
        "AccountIds": List[str],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConfigurationRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)

DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "AutoEnable": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateMembershipRequestRequestTypeDef = TypedDict(
    "DisassociateMembershipRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)

EnableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

GetMembersRequestRequestTypeDef = TypedDict(
    "GetMembersRequestRequestTypeDef",
    {
        "GraphArn": str,
        "AccountIds": List[str],
    },
)

GetMembersResponseTypeDef = TypedDict(
    "GetMembersResponseTypeDef",
    {
        "MemberDetails": List["MemberDetailTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GraphTypeDef = TypedDict(
    "GraphTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
    },
    total=False,
)

ListGraphsRequestRequestTypeDef = TypedDict(
    "ListGraphsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListGraphsResponseTypeDef = TypedDict(
    "ListGraphsResponseTypeDef",
    {
        "GraphList": List["GraphTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInvitationsRequestRequestTypeDef = TypedDict(
    "ListInvitationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {
        "Invitations": List["MemberDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMembersRequestRequestTypeDef = TypedDict(
    "_RequiredListMembersRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)
_OptionalListMembersRequestRequestTypeDef = TypedDict(
    "_OptionalListMembersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListMembersRequestRequestTypeDef(
    _RequiredListMembersRequestRequestTypeDef, _OptionalListMembersRequestRequestTypeDef
):
    pass

ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef",
    {
        "MemberDetails": List["MemberDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOrganizationAdminAccountsRequestRequestTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListOrganizationAdminAccountsResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseTypeDef",
    {
        "Administrators": List["AdministratorTypeDef"],
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

MemberDetailTypeDef = TypedDict(
    "MemberDetailTypeDef",
    {
        "AccountId": str,
        "EmailAddress": str,
        "GraphArn": str,
        "MasterId": str,
        "AdministratorId": str,
        "Status": MemberStatusType,
        "DisabledReason": MemberDisabledReasonType,
        "InvitedTime": datetime,
        "UpdatedTime": datetime,
        "VolumeUsageInBytes": int,
        "VolumeUsageUpdatedTime": datetime,
        "PercentOfGraphUtilization": float,
        "PercentOfGraphUtilizationUpdatedTime": datetime,
        "InvitationType": InvitationTypeType,
    },
    total=False,
)

RejectInvitationRequestRequestTypeDef = TypedDict(
    "RejectInvitationRequestRequestTypeDef",
    {
        "GraphArn": str,
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

StartMonitoringMemberRequestRequestTypeDef = TypedDict(
    "StartMonitoringMemberRequestRequestTypeDef",
    {
        "GraphArn": str,
        "AccountId": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UnprocessedAccountTypeDef = TypedDict(
    "UnprocessedAccountTypeDef",
    {
        "AccountId": str,
        "Reason": str,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)
_OptionalUpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "AutoEnable": bool,
    },
    total=False,
)

class UpdateOrganizationConfigurationRequestRequestTypeDef(
    _RequiredUpdateOrganizationConfigurationRequestRequestTypeDef,
    _OptionalUpdateOrganizationConfigurationRequestRequestTypeDef,
):
    pass
