"""
Type annotations for workmail service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/literals.html)

Usage::

    ```python
    from mypy_boto3_workmail.literals import AccessControlRuleEffectType

    data: AccessControlRuleEffectType = "ALLOW"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccessControlRuleEffectType",
    "AccessEffectType",
    "AvailabilityProviderTypeType",
    "DnsRecordVerificationStatusType",
    "EntityStateType",
    "EntityTypeType",
    "FolderNameType",
    "ImpersonationRoleTypeType",
    "ListAliasesPaginatorName",
    "ListAvailabilityConfigurationsPaginatorName",
    "ListGroupMembersPaginatorName",
    "ListGroupsPaginatorName",
    "ListMailboxPermissionsPaginatorName",
    "ListOrganizationsPaginatorName",
    "ListResourceDelegatesPaginatorName",
    "ListResourcesPaginatorName",
    "ListUsersPaginatorName",
    "MailboxExportJobStateType",
    "MemberTypeType",
    "MobileDeviceAccessRuleEffectType",
    "PermissionTypeType",
    "ResourceTypeType",
    "RetentionActionType",
    "UserRoleType",
)

AccessControlRuleEffectType = Literal["ALLOW", "DENY"]
AccessEffectType = Literal["ALLOW", "DENY"]
AvailabilityProviderTypeType = Literal["EWS", "LAMBDA"]
DnsRecordVerificationStatusType = Literal["FAILED", "PENDING", "VERIFIED"]
EntityStateType = Literal["DELETED", "DISABLED", "ENABLED"]
EntityTypeType = Literal["GROUP", "RESOURCE", "USER"]
FolderNameType = Literal["DELETED_ITEMS", "DRAFTS", "INBOX", "JUNK_EMAIL", "SENT_ITEMS"]
ImpersonationRoleTypeType = Literal["FULL_ACCESS", "READ_ONLY"]
ListAliasesPaginatorName = Literal["list_aliases"]
ListAvailabilityConfigurationsPaginatorName = Literal["list_availability_configurations"]
ListGroupMembersPaginatorName = Literal["list_group_members"]
ListGroupsPaginatorName = Literal["list_groups"]
ListMailboxPermissionsPaginatorName = Literal["list_mailbox_permissions"]
ListOrganizationsPaginatorName = Literal["list_organizations"]
ListResourceDelegatesPaginatorName = Literal["list_resource_delegates"]
ListResourcesPaginatorName = Literal["list_resources"]
ListUsersPaginatorName = Literal["list_users"]
MailboxExportJobStateType = Literal["CANCELLED", "COMPLETED", "FAILED", "RUNNING"]
MemberTypeType = Literal["GROUP", "USER"]
MobileDeviceAccessRuleEffectType = Literal["ALLOW", "DENY"]
PermissionTypeType = Literal["FULL_ACCESS", "SEND_AS", "SEND_ON_BEHALF"]
ResourceTypeType = Literal["EQUIPMENT", "ROOM"]
RetentionActionType = Literal["DELETE", "NONE", "PERMANENTLY_DELETE"]
UserRoleType = Literal["REMOTE_USER", "RESOURCE", "SYSTEM_USER", "USER"]
