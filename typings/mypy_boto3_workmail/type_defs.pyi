"""
Main interface for workmail service type definitions.

Usage::

    ```python
    from mypy_boto3_workmail.type_defs import AccessControlRuleTypeDef

    data: AccessControlRuleTypeDef = {...}
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
    "AccessControlRuleTypeDef",
    "BookingOptionsTypeDef",
    "DelegateTypeDef",
    "FolderConfigurationTypeDef",
    "GroupTypeDef",
    "MailboxExportJobTypeDef",
    "MemberTypeDef",
    "OrganizationSummaryTypeDef",
    "PermissionTypeDef",
    "ResourceTypeDef",
    "TagTypeDef",
    "UserTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateOrganizationResponseTypeDef",
    "CreateResourceResponseTypeDef",
    "CreateUserResponseTypeDef",
    "DeleteOrganizationResponseTypeDef",
    "DescribeGroupResponseTypeDef",
    "DescribeMailboxExportJobResponseTypeDef",
    "DescribeOrganizationResponseTypeDef",
    "DescribeResourceResponseTypeDef",
    "DescribeUserResponseTypeDef",
    "DomainTypeDef",
    "GetAccessControlEffectResponseTypeDef",
    "GetDefaultRetentionPolicyResponseTypeDef",
    "GetMailboxDetailsResponseTypeDef",
    "ListAccessControlRulesResponseTypeDef",
    "ListAliasesResponseTypeDef",
    "ListGroupMembersResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "ListMailboxExportJobsResponseTypeDef",
    "ListMailboxPermissionsResponseTypeDef",
    "ListOrganizationsResponseTypeDef",
    "ListResourceDelegatesResponseTypeDef",
    "ListResourcesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsersResponseTypeDef",
    "PaginatorConfigTypeDef",
    "StartMailboxExportJobResponseTypeDef",
)

AccessControlRuleTypeDef = TypedDict(
    "AccessControlRuleTypeDef",
    {
        "Name": str,
        "Effect": Literal["ALLOW", "DENY"],
        "Description": str,
        "IpRanges": List[str],
        "NotIpRanges": List[str],
        "Actions": List[str],
        "NotActions": List[str],
        "UserIds": List[str],
        "NotUserIds": List[str],
        "DateCreated": datetime,
        "DateModified": datetime,
    },
    total=False,
)

BookingOptionsTypeDef = TypedDict(
    "BookingOptionsTypeDef",
    {
        "AutoAcceptRequests": bool,
        "AutoDeclineRecurringRequests": bool,
        "AutoDeclineConflictingRequests": bool,
    },
    total=False,
)

DelegateTypeDef = TypedDict("DelegateTypeDef", {"Id": str, "Type": Literal["GROUP", "USER"]})

_RequiredFolderConfigurationTypeDef = TypedDict(
    "_RequiredFolderConfigurationTypeDef",
    {
        "Name": Literal["INBOX", "DELETED_ITEMS", "SENT_ITEMS", "DRAFTS", "JUNK_EMAIL"],
        "Action": Literal["NONE", "DELETE", "PERMANENTLY_DELETE"],
    },
)
_OptionalFolderConfigurationTypeDef = TypedDict(
    "_OptionalFolderConfigurationTypeDef", {"Period": int}, total=False
)


class FolderConfigurationTypeDef(
    _RequiredFolderConfigurationTypeDef, _OptionalFolderConfigurationTypeDef
):
    pass


GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

MailboxExportJobTypeDef = TypedDict(
    "MailboxExportJobTypeDef",
    {
        "JobId": str,
        "EntityId": str,
        "Description": str,
        "S3BucketName": str,
        "S3Path": str,
        "EstimatedProgress": int,
        "State": Literal["RUNNING", "COMPLETED", "FAILED", "CANCELLED"],
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "Id": str,
        "Name": str,
        "Type": Literal["GROUP", "USER"],
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

OrganizationSummaryTypeDef = TypedDict(
    "OrganizationSummaryTypeDef",
    {
        "OrganizationId": str,
        "Alias": str,
        "DefaultMailDomain": str,
        "ErrorMessage": str,
        "State": str,
    },
    total=False,
)

PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "GranteeId": str,
        "GranteeType": Literal["GROUP", "USER"],
        "PermissionValues": List[Literal["FULL_ACCESS", "SEND_AS", "SEND_ON_BEHALF"]],
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "Type": Literal["ROOM", "EQUIPMENT"],
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "DisplayName": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "UserRole": Literal["USER", "RESOURCE", "SYSTEM_USER"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

CreateGroupResponseTypeDef = TypedDict("CreateGroupResponseTypeDef", {"GroupId": str}, total=False)

CreateOrganizationResponseTypeDef = TypedDict(
    "CreateOrganizationResponseTypeDef", {"OrganizationId": str}, total=False
)

CreateResourceResponseTypeDef = TypedDict(
    "CreateResourceResponseTypeDef", {"ResourceId": str}, total=False
)

CreateUserResponseTypeDef = TypedDict("CreateUserResponseTypeDef", {"UserId": str}, total=False)

DeleteOrganizationResponseTypeDef = TypedDict(
    "DeleteOrganizationResponseTypeDef", {"OrganizationId": str, "State": str}, total=False
)

DescribeGroupResponseTypeDef = TypedDict(
    "DescribeGroupResponseTypeDef",
    {
        "GroupId": str,
        "Name": str,
        "Email": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

DescribeMailboxExportJobResponseTypeDef = TypedDict(
    "DescribeMailboxExportJobResponseTypeDef",
    {
        "EntityId": str,
        "Description": str,
        "RoleArn": str,
        "KmsKeyArn": str,
        "S3BucketName": str,
        "S3Prefix": str,
        "S3Path": str,
        "EstimatedProgress": int,
        "State": Literal["RUNNING", "COMPLETED", "FAILED", "CANCELLED"],
        "ErrorInfo": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

DescribeOrganizationResponseTypeDef = TypedDict(
    "DescribeOrganizationResponseTypeDef",
    {
        "OrganizationId": str,
        "Alias": str,
        "State": str,
        "DirectoryId": str,
        "DirectoryType": str,
        "DefaultMailDomain": str,
        "CompletedDate": datetime,
        "ErrorMessage": str,
        "ARN": str,
    },
    total=False,
)

DescribeResourceResponseTypeDef = TypedDict(
    "DescribeResourceResponseTypeDef",
    {
        "ResourceId": str,
        "Email": str,
        "Name": str,
        "Type": Literal["ROOM", "EQUIPMENT"],
        "BookingOptions": "BookingOptionsTypeDef",
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "UserId": str,
        "Name": str,
        "Email": str,
        "DisplayName": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "UserRole": Literal["USER", "RESOURCE", "SYSTEM_USER"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

DomainTypeDef = TypedDict("DomainTypeDef", {"DomainName": str, "HostedZoneId": str}, total=False)

GetAccessControlEffectResponseTypeDef = TypedDict(
    "GetAccessControlEffectResponseTypeDef",
    {"Effect": Literal["ALLOW", "DENY"], "MatchedRules": List[str]},
    total=False,
)

GetDefaultRetentionPolicyResponseTypeDef = TypedDict(
    "GetDefaultRetentionPolicyResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "FolderConfigurations": List["FolderConfigurationTypeDef"],
    },
    total=False,
)

GetMailboxDetailsResponseTypeDef = TypedDict(
    "GetMailboxDetailsResponseTypeDef", {"MailboxQuota": int, "MailboxSize": float}, total=False
)

ListAccessControlRulesResponseTypeDef = TypedDict(
    "ListAccessControlRulesResponseTypeDef",
    {"Rules": List["AccessControlRuleTypeDef"]},
    total=False,
)

ListAliasesResponseTypeDef = TypedDict(
    "ListAliasesResponseTypeDef", {"Aliases": List[str], "NextToken": str}, total=False
)

ListGroupMembersResponseTypeDef = TypedDict(
    "ListGroupMembersResponseTypeDef",
    {"Members": List["MemberTypeDef"], "NextToken": str},
    total=False,
)

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef", {"Groups": List["GroupTypeDef"], "NextToken": str}, total=False
)

ListMailboxExportJobsResponseTypeDef = TypedDict(
    "ListMailboxExportJobsResponseTypeDef",
    {"Jobs": List["MailboxExportJobTypeDef"], "NextToken": str},
    total=False,
)

ListMailboxPermissionsResponseTypeDef = TypedDict(
    "ListMailboxPermissionsResponseTypeDef",
    {"Permissions": List["PermissionTypeDef"], "NextToken": str},
    total=False,
)

ListOrganizationsResponseTypeDef = TypedDict(
    "ListOrganizationsResponseTypeDef",
    {"OrganizationSummaries": List["OrganizationSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListResourceDelegatesResponseTypeDef = TypedDict(
    "ListResourceDelegatesResponseTypeDef",
    {"Delegates": List["DelegateTypeDef"], "NextToken": str},
    total=False,
)

ListResourcesResponseTypeDef = TypedDict(
    "ListResourcesResponseTypeDef",
    {"Resources": List["ResourceTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef", {"Users": List["UserTypeDef"], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

StartMailboxExportJobResponseTypeDef = TypedDict(
    "StartMailboxExportJobResponseTypeDef", {"JobId": str}, total=False
)
