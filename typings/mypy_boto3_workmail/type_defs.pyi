"""
Type annotations for workmail service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_workmail.type_defs import AccessControlRuleTypeDef

    data: AccessControlRuleTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AccessControlRuleEffectType,
    AccessEffectType,
    AvailabilityProviderTypeType,
    DnsRecordVerificationStatusType,
    EntityStateType,
    EntityTypeType,
    FolderNameType,
    IdentityProviderAuthenticationModeType,
    ImpersonationRoleTypeType,
    MailboxExportJobStateType,
    MemberTypeType,
    MobileDeviceAccessRuleEffectType,
    PermissionTypeType,
    PersonalAccessTokenConfigurationStatusType,
    ResourceTypeType,
    RetentionActionType,
    UserRoleType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AccessControlRuleTypeDef",
    "AssociateDelegateToResourceRequestTypeDef",
    "AssociateMemberToGroupRequestTypeDef",
    "AssumeImpersonationRoleRequestTypeDef",
    "AssumeImpersonationRoleResponseTypeDef",
    "AvailabilityConfigurationTypeDef",
    "BookingOptionsTypeDef",
    "CancelMailboxExportJobRequestTypeDef",
    "CreateAliasRequestTypeDef",
    "CreateAvailabilityConfigurationRequestTypeDef",
    "CreateGroupRequestTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateIdentityCenterApplicationRequestTypeDef",
    "CreateIdentityCenterApplicationResponseTypeDef",
    "CreateImpersonationRoleRequestTypeDef",
    "CreateImpersonationRoleResponseTypeDef",
    "CreateMobileDeviceAccessRuleRequestTypeDef",
    "CreateMobileDeviceAccessRuleResponseTypeDef",
    "CreateOrganizationRequestTypeDef",
    "CreateOrganizationResponseTypeDef",
    "CreateResourceRequestTypeDef",
    "CreateResourceResponseTypeDef",
    "CreateUserRequestTypeDef",
    "CreateUserResponseTypeDef",
    "DelegateTypeDef",
    "DeleteAccessControlRuleRequestTypeDef",
    "DeleteAliasRequestTypeDef",
    "DeleteAvailabilityConfigurationRequestTypeDef",
    "DeleteEmailMonitoringConfigurationRequestTypeDef",
    "DeleteGroupRequestTypeDef",
    "DeleteIdentityCenterApplicationRequestTypeDef",
    "DeleteIdentityProviderConfigurationRequestTypeDef",
    "DeleteImpersonationRoleRequestTypeDef",
    "DeleteMailboxPermissionsRequestTypeDef",
    "DeleteMobileDeviceAccessOverrideRequestTypeDef",
    "DeleteMobileDeviceAccessRuleRequestTypeDef",
    "DeleteOrganizationRequestTypeDef",
    "DeleteOrganizationResponseTypeDef",
    "DeletePersonalAccessTokenRequestTypeDef",
    "DeleteResourceRequestTypeDef",
    "DeleteRetentionPolicyRequestTypeDef",
    "DeleteUserRequestTypeDef",
    "DeregisterFromWorkMailRequestTypeDef",
    "DeregisterMailDomainRequestTypeDef",
    "DescribeEmailMonitoringConfigurationRequestTypeDef",
    "DescribeEmailMonitoringConfigurationResponseTypeDef",
    "DescribeEntityRequestTypeDef",
    "DescribeEntityResponseTypeDef",
    "DescribeGroupRequestTypeDef",
    "DescribeGroupResponseTypeDef",
    "DescribeIdentityProviderConfigurationRequestTypeDef",
    "DescribeIdentityProviderConfigurationResponseTypeDef",
    "DescribeInboundDmarcSettingsRequestTypeDef",
    "DescribeInboundDmarcSettingsResponseTypeDef",
    "DescribeMailboxExportJobRequestTypeDef",
    "DescribeMailboxExportJobResponseTypeDef",
    "DescribeOrganizationRequestTypeDef",
    "DescribeOrganizationResponseTypeDef",
    "DescribeResourceRequestTypeDef",
    "DescribeResourceResponseTypeDef",
    "DescribeUserRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "DisassociateDelegateFromResourceRequestTypeDef",
    "DisassociateMemberFromGroupRequestTypeDef",
    "DnsRecordTypeDef",
    "DomainTypeDef",
    "EwsAvailabilityProviderTypeDef",
    "FolderConfigurationTypeDef",
    "GetAccessControlEffectRequestTypeDef",
    "GetAccessControlEffectResponseTypeDef",
    "GetDefaultRetentionPolicyRequestTypeDef",
    "GetDefaultRetentionPolicyResponseTypeDef",
    "GetImpersonationRoleEffectRequestTypeDef",
    "GetImpersonationRoleEffectResponseTypeDef",
    "GetImpersonationRoleRequestTypeDef",
    "GetImpersonationRoleResponseTypeDef",
    "GetMailDomainRequestTypeDef",
    "GetMailDomainResponseTypeDef",
    "GetMailboxDetailsRequestTypeDef",
    "GetMailboxDetailsResponseTypeDef",
    "GetMobileDeviceAccessEffectRequestTypeDef",
    "GetMobileDeviceAccessEffectResponseTypeDef",
    "GetMobileDeviceAccessOverrideRequestTypeDef",
    "GetMobileDeviceAccessOverrideResponseTypeDef",
    "GetPersonalAccessTokenMetadataRequestTypeDef",
    "GetPersonalAccessTokenMetadataResponseTypeDef",
    "GroupIdentifierTypeDef",
    "GroupTypeDef",
    "IdentityCenterConfigurationTypeDef",
    "ImpersonationMatchedRuleTypeDef",
    "ImpersonationRoleTypeDef",
    "ImpersonationRuleOutputTypeDef",
    "ImpersonationRuleTypeDef",
    "ImpersonationRuleUnionTypeDef",
    "LambdaAvailabilityProviderTypeDef",
    "ListAccessControlRulesRequestTypeDef",
    "ListAccessControlRulesResponseTypeDef",
    "ListAliasesRequestPaginateTypeDef",
    "ListAliasesRequestTypeDef",
    "ListAliasesResponseTypeDef",
    "ListAvailabilityConfigurationsRequestPaginateTypeDef",
    "ListAvailabilityConfigurationsRequestTypeDef",
    "ListAvailabilityConfigurationsResponseTypeDef",
    "ListGroupMembersRequestPaginateTypeDef",
    "ListGroupMembersRequestTypeDef",
    "ListGroupMembersResponseTypeDef",
    "ListGroupsFiltersTypeDef",
    "ListGroupsForEntityFiltersTypeDef",
    "ListGroupsForEntityRequestTypeDef",
    "ListGroupsForEntityResponseTypeDef",
    "ListGroupsRequestPaginateTypeDef",
    "ListGroupsRequestTypeDef",
    "ListGroupsResponseTypeDef",
    "ListImpersonationRolesRequestTypeDef",
    "ListImpersonationRolesResponseTypeDef",
    "ListMailDomainsRequestTypeDef",
    "ListMailDomainsResponseTypeDef",
    "ListMailboxExportJobsRequestTypeDef",
    "ListMailboxExportJobsResponseTypeDef",
    "ListMailboxPermissionsRequestPaginateTypeDef",
    "ListMailboxPermissionsRequestTypeDef",
    "ListMailboxPermissionsResponseTypeDef",
    "ListMobileDeviceAccessOverridesRequestTypeDef",
    "ListMobileDeviceAccessOverridesResponseTypeDef",
    "ListMobileDeviceAccessRulesRequestTypeDef",
    "ListMobileDeviceAccessRulesResponseTypeDef",
    "ListOrganizationsRequestPaginateTypeDef",
    "ListOrganizationsRequestTypeDef",
    "ListOrganizationsResponseTypeDef",
    "ListPersonalAccessTokensRequestPaginateTypeDef",
    "ListPersonalAccessTokensRequestTypeDef",
    "ListPersonalAccessTokensResponseTypeDef",
    "ListResourceDelegatesRequestPaginateTypeDef",
    "ListResourceDelegatesRequestTypeDef",
    "ListResourceDelegatesResponseTypeDef",
    "ListResourcesFiltersTypeDef",
    "ListResourcesRequestPaginateTypeDef",
    "ListResourcesRequestTypeDef",
    "ListResourcesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsersFiltersTypeDef",
    "ListUsersRequestPaginateTypeDef",
    "ListUsersRequestTypeDef",
    "ListUsersResponseTypeDef",
    "MailDomainSummaryTypeDef",
    "MailboxExportJobTypeDef",
    "MemberTypeDef",
    "MobileDeviceAccessMatchedRuleTypeDef",
    "MobileDeviceAccessOverrideTypeDef",
    "MobileDeviceAccessRuleTypeDef",
    "OrganizationSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "PersonalAccessTokenConfigurationTypeDef",
    "PersonalAccessTokenSummaryTypeDef",
    "PutAccessControlRuleRequestTypeDef",
    "PutEmailMonitoringConfigurationRequestTypeDef",
    "PutIdentityProviderConfigurationRequestTypeDef",
    "PutInboundDmarcSettingsRequestTypeDef",
    "PutMailboxPermissionsRequestTypeDef",
    "PutMobileDeviceAccessOverrideRequestTypeDef",
    "PutRetentionPolicyRequestTypeDef",
    "RedactedEwsAvailabilityProviderTypeDef",
    "RegisterMailDomainRequestTypeDef",
    "RegisterToWorkMailRequestTypeDef",
    "ResetPasswordRequestTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "StartMailboxExportJobRequestTypeDef",
    "StartMailboxExportJobResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TestAvailabilityConfigurationRequestTypeDef",
    "TestAvailabilityConfigurationResponseTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAvailabilityConfigurationRequestTypeDef",
    "UpdateDefaultMailDomainRequestTypeDef",
    "UpdateGroupRequestTypeDef",
    "UpdateImpersonationRoleRequestTypeDef",
    "UpdateMailboxQuotaRequestTypeDef",
    "UpdateMobileDeviceAccessRuleRequestTypeDef",
    "UpdatePrimaryEmailAddressRequestTypeDef",
    "UpdateResourceRequestTypeDef",
    "UpdateUserRequestTypeDef",
    "UserTypeDef",
)

class AccessControlRuleTypeDef(TypedDict):
    Name: NotRequired[str]
    Effect: NotRequired[AccessControlRuleEffectType]
    Description: NotRequired[str]
    IpRanges: NotRequired[List[str]]
    NotIpRanges: NotRequired[List[str]]
    Actions: NotRequired[List[str]]
    NotActions: NotRequired[List[str]]
    UserIds: NotRequired[List[str]]
    NotUserIds: NotRequired[List[str]]
    DateCreated: NotRequired[datetime]
    DateModified: NotRequired[datetime]
    ImpersonationRoleIds: NotRequired[List[str]]
    NotImpersonationRoleIds: NotRequired[List[str]]

class AssociateDelegateToResourceRequestTypeDef(TypedDict):
    OrganizationId: str
    ResourceId: str
    EntityId: str

class AssociateMemberToGroupRequestTypeDef(TypedDict):
    OrganizationId: str
    GroupId: str
    MemberId: str

class AssumeImpersonationRoleRequestTypeDef(TypedDict):
    OrganizationId: str
    ImpersonationRoleId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class LambdaAvailabilityProviderTypeDef(TypedDict):
    LambdaArn: str

class RedactedEwsAvailabilityProviderTypeDef(TypedDict):
    EwsEndpoint: NotRequired[str]
    EwsUsername: NotRequired[str]

class BookingOptionsTypeDef(TypedDict):
    AutoAcceptRequests: NotRequired[bool]
    AutoDeclineRecurringRequests: NotRequired[bool]
    AutoDeclineConflictingRequests: NotRequired[bool]

class CancelMailboxExportJobRequestTypeDef(TypedDict):
    ClientToken: str
    JobId: str
    OrganizationId: str

class CreateAliasRequestTypeDef(TypedDict):
    OrganizationId: str
    EntityId: str
    Alias: str

class EwsAvailabilityProviderTypeDef(TypedDict):
    EwsEndpoint: str
    EwsUsername: str
    EwsPassword: str

class CreateGroupRequestTypeDef(TypedDict):
    OrganizationId: str
    Name: str
    HiddenFromGlobalAddressList: NotRequired[bool]

class CreateIdentityCenterApplicationRequestTypeDef(TypedDict):
    Name: str
    InstanceArn: str
    ClientToken: NotRequired[str]

class CreateMobileDeviceAccessRuleRequestTypeDef(TypedDict):
    OrganizationId: str
    Name: str
    Effect: MobileDeviceAccessRuleEffectType
    ClientToken: NotRequired[str]
    Description: NotRequired[str]
    DeviceTypes: NotRequired[Sequence[str]]
    NotDeviceTypes: NotRequired[Sequence[str]]
    DeviceModels: NotRequired[Sequence[str]]
    NotDeviceModels: NotRequired[Sequence[str]]
    DeviceOperatingSystems: NotRequired[Sequence[str]]
    NotDeviceOperatingSystems: NotRequired[Sequence[str]]
    DeviceUserAgents: NotRequired[Sequence[str]]
    NotDeviceUserAgents: NotRequired[Sequence[str]]

class DomainTypeDef(TypedDict):
    DomainName: str
    HostedZoneId: NotRequired[str]

CreateResourceRequestTypeDef = TypedDict(
    "CreateResourceRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
        "Type": ResourceTypeType,
        "Description": NotRequired[str],
        "HiddenFromGlobalAddressList": NotRequired[bool],
    },
)

class CreateUserRequestTypeDef(TypedDict):
    OrganizationId: str
    Name: str
    DisplayName: str
    Password: NotRequired[str]
    Role: NotRequired[UserRoleType]
    FirstName: NotRequired[str]
    LastName: NotRequired[str]
    HiddenFromGlobalAddressList: NotRequired[bool]
    IdentityProviderUserId: NotRequired[str]

DelegateTypeDef = TypedDict(
    "DelegateTypeDef",
    {
        "Id": str,
        "Type": MemberTypeType,
    },
)

class DeleteAccessControlRuleRequestTypeDef(TypedDict):
    OrganizationId: str
    Name: str

class DeleteAliasRequestTypeDef(TypedDict):
    OrganizationId: str
    EntityId: str
    Alias: str

class DeleteAvailabilityConfigurationRequestTypeDef(TypedDict):
    OrganizationId: str
    DomainName: str

class DeleteEmailMonitoringConfigurationRequestTypeDef(TypedDict):
    OrganizationId: str

class DeleteGroupRequestTypeDef(TypedDict):
    OrganizationId: str
    GroupId: str

class DeleteIdentityCenterApplicationRequestTypeDef(TypedDict):
    ApplicationArn: str

class DeleteIdentityProviderConfigurationRequestTypeDef(TypedDict):
    OrganizationId: str

class DeleteImpersonationRoleRequestTypeDef(TypedDict):
    OrganizationId: str
    ImpersonationRoleId: str

class DeleteMailboxPermissionsRequestTypeDef(TypedDict):
    OrganizationId: str
    EntityId: str
    GranteeId: str

class DeleteMobileDeviceAccessOverrideRequestTypeDef(TypedDict):
    OrganizationId: str
    UserId: str
    DeviceId: str

class DeleteMobileDeviceAccessRuleRequestTypeDef(TypedDict):
    OrganizationId: str
    MobileDeviceAccessRuleId: str

class DeleteOrganizationRequestTypeDef(TypedDict):
    OrganizationId: str
    DeleteDirectory: bool
    ClientToken: NotRequired[str]
    ForceDelete: NotRequired[bool]
    DeleteIdentityCenterApplication: NotRequired[bool]

class DeletePersonalAccessTokenRequestTypeDef(TypedDict):
    OrganizationId: str
    PersonalAccessTokenId: str

class DeleteResourceRequestTypeDef(TypedDict):
    OrganizationId: str
    ResourceId: str

class DeleteRetentionPolicyRequestTypeDef(TypedDict):
    OrganizationId: str
    Id: str

class DeleteUserRequestTypeDef(TypedDict):
    OrganizationId: str
    UserId: str

class DeregisterFromWorkMailRequestTypeDef(TypedDict):
    OrganizationId: str
    EntityId: str

class DeregisterMailDomainRequestTypeDef(TypedDict):
    OrganizationId: str
    DomainName: str

class DescribeEmailMonitoringConfigurationRequestTypeDef(TypedDict):
    OrganizationId: str

class DescribeEntityRequestTypeDef(TypedDict):
    OrganizationId: str
    Email: str

class DescribeGroupRequestTypeDef(TypedDict):
    OrganizationId: str
    GroupId: str

class DescribeIdentityProviderConfigurationRequestTypeDef(TypedDict):
    OrganizationId: str

class IdentityCenterConfigurationTypeDef(TypedDict):
    InstanceArn: str
    ApplicationArn: str

class PersonalAccessTokenConfigurationTypeDef(TypedDict):
    Status: PersonalAccessTokenConfigurationStatusType
    LifetimeInDays: NotRequired[int]

class DescribeInboundDmarcSettingsRequestTypeDef(TypedDict):
    OrganizationId: str

class DescribeMailboxExportJobRequestTypeDef(TypedDict):
    JobId: str
    OrganizationId: str

class DescribeOrganizationRequestTypeDef(TypedDict):
    OrganizationId: str

class DescribeResourceRequestTypeDef(TypedDict):
    OrganizationId: str
    ResourceId: str

class DescribeUserRequestTypeDef(TypedDict):
    OrganizationId: str
    UserId: str

class DisassociateDelegateFromResourceRequestTypeDef(TypedDict):
    OrganizationId: str
    ResourceId: str
    EntityId: str

class DisassociateMemberFromGroupRequestTypeDef(TypedDict):
    OrganizationId: str
    GroupId: str
    MemberId: str

DnsRecordTypeDef = TypedDict(
    "DnsRecordTypeDef",
    {
        "Type": NotRequired[str],
        "Hostname": NotRequired[str],
        "Value": NotRequired[str],
    },
)

class FolderConfigurationTypeDef(TypedDict):
    Name: FolderNameType
    Action: RetentionActionType
    Period: NotRequired[int]

class GetAccessControlEffectRequestTypeDef(TypedDict):
    OrganizationId: str
    IpAddress: str
    Action: str
    UserId: NotRequired[str]
    ImpersonationRoleId: NotRequired[str]

class GetDefaultRetentionPolicyRequestTypeDef(TypedDict):
    OrganizationId: str

class GetImpersonationRoleEffectRequestTypeDef(TypedDict):
    OrganizationId: str
    ImpersonationRoleId: str
    TargetUser: str

class ImpersonationMatchedRuleTypeDef(TypedDict):
    ImpersonationRuleId: NotRequired[str]
    Name: NotRequired[str]

class GetImpersonationRoleRequestTypeDef(TypedDict):
    OrganizationId: str
    ImpersonationRoleId: str

class ImpersonationRuleOutputTypeDef(TypedDict):
    ImpersonationRuleId: str
    Effect: AccessEffectType
    Name: NotRequired[str]
    Description: NotRequired[str]
    TargetUsers: NotRequired[List[str]]
    NotTargetUsers: NotRequired[List[str]]

class GetMailDomainRequestTypeDef(TypedDict):
    OrganizationId: str
    DomainName: str

class GetMailboxDetailsRequestTypeDef(TypedDict):
    OrganizationId: str
    UserId: str

class GetMobileDeviceAccessEffectRequestTypeDef(TypedDict):
    OrganizationId: str
    DeviceType: NotRequired[str]
    DeviceModel: NotRequired[str]
    DeviceOperatingSystem: NotRequired[str]
    DeviceUserAgent: NotRequired[str]

class MobileDeviceAccessMatchedRuleTypeDef(TypedDict):
    MobileDeviceAccessRuleId: NotRequired[str]
    Name: NotRequired[str]

class GetMobileDeviceAccessOverrideRequestTypeDef(TypedDict):
    OrganizationId: str
    UserId: str
    DeviceId: str

class GetPersonalAccessTokenMetadataRequestTypeDef(TypedDict):
    OrganizationId: str
    PersonalAccessTokenId: str

class GroupIdentifierTypeDef(TypedDict):
    GroupId: NotRequired[str]
    GroupName: NotRequired[str]

class GroupTypeDef(TypedDict):
    Id: NotRequired[str]
    Email: NotRequired[str]
    Name: NotRequired[str]
    State: NotRequired[EntityStateType]
    EnabledDate: NotRequired[datetime]
    DisabledDate: NotRequired[datetime]

ImpersonationRoleTypeDef = TypedDict(
    "ImpersonationRoleTypeDef",
    {
        "ImpersonationRoleId": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[ImpersonationRoleTypeType],
        "DateCreated": NotRequired[datetime],
        "DateModified": NotRequired[datetime],
    },
)

class ImpersonationRuleTypeDef(TypedDict):
    ImpersonationRuleId: str
    Effect: AccessEffectType
    Name: NotRequired[str]
    Description: NotRequired[str]
    TargetUsers: NotRequired[Sequence[str]]
    NotTargetUsers: NotRequired[Sequence[str]]

class ListAccessControlRulesRequestTypeDef(TypedDict):
    OrganizationId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAliasesRequestTypeDef(TypedDict):
    OrganizationId: str
    EntityId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListAvailabilityConfigurationsRequestTypeDef(TypedDict):
    OrganizationId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListGroupMembersRequestTypeDef(TypedDict):
    OrganizationId: str
    GroupId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[MemberTypeType],
        "State": NotRequired[EntityStateType],
        "EnabledDate": NotRequired[datetime],
        "DisabledDate": NotRequired[datetime],
    },
)

class ListGroupsFiltersTypeDef(TypedDict):
    NamePrefix: NotRequired[str]
    PrimaryEmailPrefix: NotRequired[str]
    State: NotRequired[EntityStateType]

class ListGroupsForEntityFiltersTypeDef(TypedDict):
    GroupNamePrefix: NotRequired[str]

class ListImpersonationRolesRequestTypeDef(TypedDict):
    OrganizationId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListMailDomainsRequestTypeDef(TypedDict):
    OrganizationId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class MailDomainSummaryTypeDef(TypedDict):
    DomainName: NotRequired[str]
    DefaultDomain: NotRequired[bool]

class ListMailboxExportJobsRequestTypeDef(TypedDict):
    OrganizationId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class MailboxExportJobTypeDef(TypedDict):
    JobId: NotRequired[str]
    EntityId: NotRequired[str]
    Description: NotRequired[str]
    S3BucketName: NotRequired[str]
    S3Path: NotRequired[str]
    EstimatedProgress: NotRequired[int]
    State: NotRequired[MailboxExportJobStateType]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]

class ListMailboxPermissionsRequestTypeDef(TypedDict):
    OrganizationId: str
    EntityId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class PermissionTypeDef(TypedDict):
    GranteeId: str
    GranteeType: MemberTypeType
    PermissionValues: List[PermissionTypeType]

class ListMobileDeviceAccessOverridesRequestTypeDef(TypedDict):
    OrganizationId: str
    UserId: NotRequired[str]
    DeviceId: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class MobileDeviceAccessOverrideTypeDef(TypedDict):
    UserId: NotRequired[str]
    DeviceId: NotRequired[str]
    Effect: NotRequired[MobileDeviceAccessRuleEffectType]
    Description: NotRequired[str]
    DateCreated: NotRequired[datetime]
    DateModified: NotRequired[datetime]

class ListMobileDeviceAccessRulesRequestTypeDef(TypedDict):
    OrganizationId: str

class MobileDeviceAccessRuleTypeDef(TypedDict):
    MobileDeviceAccessRuleId: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    Effect: NotRequired[MobileDeviceAccessRuleEffectType]
    DeviceTypes: NotRequired[List[str]]
    NotDeviceTypes: NotRequired[List[str]]
    DeviceModels: NotRequired[List[str]]
    NotDeviceModels: NotRequired[List[str]]
    DeviceOperatingSystems: NotRequired[List[str]]
    NotDeviceOperatingSystems: NotRequired[List[str]]
    DeviceUserAgents: NotRequired[List[str]]
    NotDeviceUserAgents: NotRequired[List[str]]
    DateCreated: NotRequired[datetime]
    DateModified: NotRequired[datetime]

class ListOrganizationsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class OrganizationSummaryTypeDef(TypedDict):
    OrganizationId: NotRequired[str]
    Alias: NotRequired[str]
    DefaultMailDomain: NotRequired[str]
    ErrorMessage: NotRequired[str]
    State: NotRequired[str]

class ListPersonalAccessTokensRequestTypeDef(TypedDict):
    OrganizationId: str
    UserId: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class PersonalAccessTokenSummaryTypeDef(TypedDict):
    PersonalAccessTokenId: NotRequired[str]
    UserId: NotRequired[str]
    Name: NotRequired[str]
    DateCreated: NotRequired[datetime]
    DateLastUsed: NotRequired[datetime]
    ExpiresTime: NotRequired[datetime]
    Scopes: NotRequired[List[str]]

class ListResourceDelegatesRequestTypeDef(TypedDict):
    OrganizationId: str
    ResourceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListResourcesFiltersTypeDef(TypedDict):
    NamePrefix: NotRequired[str]
    PrimaryEmailPrefix: NotRequired[str]
    State: NotRequired[EntityStateType]

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Id": NotRequired[str],
        "Email": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[ResourceTypeType],
        "State": NotRequired[EntityStateType],
        "EnabledDate": NotRequired[datetime],
        "DisabledDate": NotRequired[datetime],
        "Description": NotRequired[str],
    },
)

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class ListUsersFiltersTypeDef(TypedDict):
    UsernamePrefix: NotRequired[str]
    DisplayNamePrefix: NotRequired[str]
    PrimaryEmailPrefix: NotRequired[str]
    State: NotRequired[EntityStateType]
    IdentityProviderUserIdPrefix: NotRequired[str]

class UserTypeDef(TypedDict):
    Id: NotRequired[str]
    Email: NotRequired[str]
    Name: NotRequired[str]
    DisplayName: NotRequired[str]
    State: NotRequired[EntityStateType]
    UserRole: NotRequired[UserRoleType]
    EnabledDate: NotRequired[datetime]
    DisabledDate: NotRequired[datetime]
    IdentityProviderUserId: NotRequired[str]
    IdentityProviderIdentityStoreId: NotRequired[str]

class PutAccessControlRuleRequestTypeDef(TypedDict):
    Name: str
    Effect: AccessControlRuleEffectType
    Description: str
    OrganizationId: str
    IpRanges: NotRequired[Sequence[str]]
    NotIpRanges: NotRequired[Sequence[str]]
    Actions: NotRequired[Sequence[str]]
    NotActions: NotRequired[Sequence[str]]
    UserIds: NotRequired[Sequence[str]]
    NotUserIds: NotRequired[Sequence[str]]
    ImpersonationRoleIds: NotRequired[Sequence[str]]
    NotImpersonationRoleIds: NotRequired[Sequence[str]]

class PutEmailMonitoringConfigurationRequestTypeDef(TypedDict):
    OrganizationId: str
    RoleArn: str
    LogGroupArn: str

class PutInboundDmarcSettingsRequestTypeDef(TypedDict):
    OrganizationId: str
    Enforced: bool

class PutMailboxPermissionsRequestTypeDef(TypedDict):
    OrganizationId: str
    EntityId: str
    GranteeId: str
    PermissionValues: Sequence[PermissionTypeType]

class PutMobileDeviceAccessOverrideRequestTypeDef(TypedDict):
    OrganizationId: str
    UserId: str
    DeviceId: str
    Effect: MobileDeviceAccessRuleEffectType
    Description: NotRequired[str]

class RegisterMailDomainRequestTypeDef(TypedDict):
    OrganizationId: str
    DomainName: str
    ClientToken: NotRequired[str]

class RegisterToWorkMailRequestTypeDef(TypedDict):
    OrganizationId: str
    EntityId: str
    Email: str

class ResetPasswordRequestTypeDef(TypedDict):
    OrganizationId: str
    UserId: str
    Password: str

class StartMailboxExportJobRequestTypeDef(TypedDict):
    ClientToken: str
    OrganizationId: str
    EntityId: str
    RoleArn: str
    KmsKeyArn: str
    S3BucketName: str
    S3Prefix: str
    Description: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateDefaultMailDomainRequestTypeDef(TypedDict):
    OrganizationId: str
    DomainName: str

class UpdateGroupRequestTypeDef(TypedDict):
    OrganizationId: str
    GroupId: str
    HiddenFromGlobalAddressList: NotRequired[bool]

class UpdateMailboxQuotaRequestTypeDef(TypedDict):
    OrganizationId: str
    UserId: str
    MailboxQuota: int

class UpdateMobileDeviceAccessRuleRequestTypeDef(TypedDict):
    OrganizationId: str
    MobileDeviceAccessRuleId: str
    Name: str
    Effect: MobileDeviceAccessRuleEffectType
    Description: NotRequired[str]
    DeviceTypes: NotRequired[Sequence[str]]
    NotDeviceTypes: NotRequired[Sequence[str]]
    DeviceModels: NotRequired[Sequence[str]]
    NotDeviceModels: NotRequired[Sequence[str]]
    DeviceOperatingSystems: NotRequired[Sequence[str]]
    NotDeviceOperatingSystems: NotRequired[Sequence[str]]
    DeviceUserAgents: NotRequired[Sequence[str]]
    NotDeviceUserAgents: NotRequired[Sequence[str]]

class UpdatePrimaryEmailAddressRequestTypeDef(TypedDict):
    OrganizationId: str
    EntityId: str
    Email: str

class UpdateUserRequestTypeDef(TypedDict):
    OrganizationId: str
    UserId: str
    Role: NotRequired[UserRoleType]
    DisplayName: NotRequired[str]
    FirstName: NotRequired[str]
    LastName: NotRequired[str]
    HiddenFromGlobalAddressList: NotRequired[bool]
    Initials: NotRequired[str]
    Telephone: NotRequired[str]
    Street: NotRequired[str]
    JobTitle: NotRequired[str]
    City: NotRequired[str]
    Company: NotRequired[str]
    ZipCode: NotRequired[str]
    Department: NotRequired[str]
    Country: NotRequired[str]
    Office: NotRequired[str]
    IdentityProviderUserId: NotRequired[str]

class AssumeImpersonationRoleResponseTypeDef(TypedDict):
    Token: str
    ExpiresIn: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupResponseTypeDef(TypedDict):
    GroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIdentityCenterApplicationResponseTypeDef(TypedDict):
    ApplicationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImpersonationRoleResponseTypeDef(TypedDict):
    ImpersonationRoleId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMobileDeviceAccessRuleResponseTypeDef(TypedDict):
    MobileDeviceAccessRuleId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOrganizationResponseTypeDef(TypedDict):
    OrganizationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceResponseTypeDef(TypedDict):
    ResourceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserResponseTypeDef(TypedDict):
    UserId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteOrganizationResponseTypeDef(TypedDict):
    OrganizationId: str
    State: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEmailMonitoringConfigurationResponseTypeDef(TypedDict):
    RoleArn: str
    LogGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

DescribeEntityResponseTypeDef = TypedDict(
    "DescribeEntityResponseTypeDef",
    {
        "EntityId": str,
        "Name": str,
        "Type": EntityTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class DescribeGroupResponseTypeDef(TypedDict):
    GroupId: str
    Name: str
    Email: str
    State: EntityStateType
    EnabledDate: datetime
    DisabledDate: datetime
    HiddenFromGlobalAddressList: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInboundDmarcSettingsResponseTypeDef(TypedDict):
    Enforced: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMailboxExportJobResponseTypeDef(TypedDict):
    EntityId: str
    Description: str
    RoleArn: str
    KmsKeyArn: str
    S3BucketName: str
    S3Prefix: str
    S3Path: str
    EstimatedProgress: int
    State: MailboxExportJobStateType
    ErrorInfo: str
    StartTime: datetime
    EndTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOrganizationResponseTypeDef(TypedDict):
    OrganizationId: str
    Alias: str
    State: str
    DirectoryId: str
    DirectoryType: str
    DefaultMailDomain: str
    CompletedDate: datetime
    ErrorMessage: str
    ARN: str
    MigrationAdmin: str
    InteroperabilityEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUserResponseTypeDef(TypedDict):
    UserId: str
    Name: str
    Email: str
    DisplayName: str
    State: EntityStateType
    UserRole: UserRoleType
    EnabledDate: datetime
    DisabledDate: datetime
    MailboxProvisionedDate: datetime
    MailboxDeprovisionedDate: datetime
    FirstName: str
    LastName: str
    HiddenFromGlobalAddressList: bool
    Initials: str
    Telephone: str
    Street: str
    JobTitle: str
    City: str
    Company: str
    ZipCode: str
    Department: str
    Country: str
    Office: str
    IdentityProviderUserId: str
    IdentityProviderIdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessControlEffectResponseTypeDef(TypedDict):
    Effect: AccessControlRuleEffectType
    MatchedRules: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMailboxDetailsResponseTypeDef(TypedDict):
    MailboxQuota: int
    MailboxSize: float
    ResponseMetadata: ResponseMetadataTypeDef

class GetMobileDeviceAccessOverrideResponseTypeDef(TypedDict):
    UserId: str
    DeviceId: str
    Effect: MobileDeviceAccessRuleEffectType
    Description: str
    DateCreated: datetime
    DateModified: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetPersonalAccessTokenMetadataResponseTypeDef(TypedDict):
    PersonalAccessTokenId: str
    UserId: str
    Name: str
    DateCreated: datetime
    DateLastUsed: datetime
    ExpiresTime: datetime
    Scopes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessControlRulesResponseTypeDef(TypedDict):
    Rules: List[AccessControlRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAliasesResponseTypeDef(TypedDict):
    Aliases: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class StartMailboxExportJobResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestAvailabilityConfigurationResponseTypeDef(TypedDict):
    TestPassed: bool
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class AvailabilityConfigurationTypeDef(TypedDict):
    DomainName: NotRequired[str]
    ProviderType: NotRequired[AvailabilityProviderTypeType]
    EwsProvider: NotRequired[RedactedEwsAvailabilityProviderTypeDef]
    LambdaProvider: NotRequired[LambdaAvailabilityProviderTypeDef]
    DateCreated: NotRequired[datetime]
    DateModified: NotRequired[datetime]

DescribeResourceResponseTypeDef = TypedDict(
    "DescribeResourceResponseTypeDef",
    {
        "ResourceId": str,
        "Email": str,
        "Name": str,
        "Type": ResourceTypeType,
        "BookingOptions": BookingOptionsTypeDef,
        "State": EntityStateType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
        "Description": str,
        "HiddenFromGlobalAddressList": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateResourceRequestTypeDef = TypedDict(
    "UpdateResourceRequestTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
        "Name": NotRequired[str],
        "BookingOptions": NotRequired[BookingOptionsTypeDef],
        "Description": NotRequired[str],
        "Type": NotRequired[ResourceTypeType],
        "HiddenFromGlobalAddressList": NotRequired[bool],
    },
)

class CreateAvailabilityConfigurationRequestTypeDef(TypedDict):
    OrganizationId: str
    DomainName: str
    ClientToken: NotRequired[str]
    EwsProvider: NotRequired[EwsAvailabilityProviderTypeDef]
    LambdaProvider: NotRequired[LambdaAvailabilityProviderTypeDef]

class TestAvailabilityConfigurationRequestTypeDef(TypedDict):
    OrganizationId: str
    DomainName: NotRequired[str]
    EwsProvider: NotRequired[EwsAvailabilityProviderTypeDef]
    LambdaProvider: NotRequired[LambdaAvailabilityProviderTypeDef]

class UpdateAvailabilityConfigurationRequestTypeDef(TypedDict):
    OrganizationId: str
    DomainName: str
    EwsProvider: NotRequired[EwsAvailabilityProviderTypeDef]
    LambdaProvider: NotRequired[LambdaAvailabilityProviderTypeDef]

class CreateOrganizationRequestTypeDef(TypedDict):
    Alias: str
    DirectoryId: NotRequired[str]
    ClientToken: NotRequired[str]
    Domains: NotRequired[Sequence[DomainTypeDef]]
    KmsKeyArn: NotRequired[str]
    EnableInteroperability: NotRequired[bool]

class ListResourceDelegatesResponseTypeDef(TypedDict):
    Delegates: List[DelegateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeIdentityProviderConfigurationResponseTypeDef(TypedDict):
    AuthenticationMode: IdentityProviderAuthenticationModeType
    IdentityCenterConfiguration: IdentityCenterConfigurationTypeDef
    PersonalAccessTokenConfiguration: PersonalAccessTokenConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutIdentityProviderConfigurationRequestTypeDef(TypedDict):
    OrganizationId: str
    AuthenticationMode: IdentityProviderAuthenticationModeType
    IdentityCenterConfiguration: IdentityCenterConfigurationTypeDef
    PersonalAccessTokenConfiguration: PersonalAccessTokenConfigurationTypeDef

class GetMailDomainResponseTypeDef(TypedDict):
    Records: List[DnsRecordTypeDef]
    IsTestDomain: bool
    IsDefault: bool
    OwnershipVerificationStatus: DnsRecordVerificationStatusType
    DkimVerificationStatus: DnsRecordVerificationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetDefaultRetentionPolicyResponseTypeDef(TypedDict):
    Id: str
    Name: str
    Description: str
    FolderConfigurations: List[FolderConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutRetentionPolicyRequestTypeDef(TypedDict):
    OrganizationId: str
    Name: str
    FolderConfigurations: Sequence[FolderConfigurationTypeDef]
    Id: NotRequired[str]
    Description: NotRequired[str]

GetImpersonationRoleEffectResponseTypeDef = TypedDict(
    "GetImpersonationRoleEffectResponseTypeDef",
    {
        "Type": ImpersonationRoleTypeType,
        "Effect": AccessEffectType,
        "MatchedRules": List[ImpersonationMatchedRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImpersonationRoleResponseTypeDef = TypedDict(
    "GetImpersonationRoleResponseTypeDef",
    {
        "ImpersonationRoleId": str,
        "Name": str,
        "Type": ImpersonationRoleTypeType,
        "Description": str,
        "Rules": List[ImpersonationRuleOutputTypeDef],
        "DateCreated": datetime,
        "DateModified": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetMobileDeviceAccessEffectResponseTypeDef(TypedDict):
    Effect: MobileDeviceAccessRuleEffectType
    MatchedRules: List[MobileDeviceAccessMatchedRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsForEntityResponseTypeDef(TypedDict):
    Groups: List[GroupIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListGroupsResponseTypeDef(TypedDict):
    Groups: List[GroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListImpersonationRolesResponseTypeDef(TypedDict):
    Roles: List[ImpersonationRoleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

ImpersonationRuleUnionTypeDef = Union[ImpersonationRuleTypeDef, ImpersonationRuleOutputTypeDef]

class ListAliasesRequestPaginateTypeDef(TypedDict):
    OrganizationId: str
    EntityId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAvailabilityConfigurationsRequestPaginateTypeDef(TypedDict):
    OrganizationId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGroupMembersRequestPaginateTypeDef(TypedDict):
    OrganizationId: str
    GroupId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMailboxPermissionsRequestPaginateTypeDef(TypedDict):
    OrganizationId: str
    EntityId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOrganizationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPersonalAccessTokensRequestPaginateTypeDef(TypedDict):
    OrganizationId: str
    UserId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceDelegatesRequestPaginateTypeDef(TypedDict):
    OrganizationId: str
    ResourceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGroupMembersResponseTypeDef(TypedDict):
    Members: List[MemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListGroupsRequestPaginateTypeDef(TypedDict):
    OrganizationId: str
    Filters: NotRequired[ListGroupsFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGroupsRequestTypeDef(TypedDict):
    OrganizationId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[ListGroupsFiltersTypeDef]

class ListGroupsForEntityRequestTypeDef(TypedDict):
    OrganizationId: str
    EntityId: str
    Filters: NotRequired[ListGroupsForEntityFiltersTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListMailDomainsResponseTypeDef(TypedDict):
    MailDomains: List[MailDomainSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListMailboxExportJobsResponseTypeDef(TypedDict):
    Jobs: List[MailboxExportJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListMailboxPermissionsResponseTypeDef(TypedDict):
    Permissions: List[PermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListMobileDeviceAccessOverridesResponseTypeDef(TypedDict):
    Overrides: List[MobileDeviceAccessOverrideTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListMobileDeviceAccessRulesResponseTypeDef(TypedDict):
    Rules: List[MobileDeviceAccessRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrganizationsResponseTypeDef(TypedDict):
    OrganizationSummaries: List[OrganizationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPersonalAccessTokensResponseTypeDef(TypedDict):
    PersonalAccessTokenSummaries: List[PersonalAccessTokenSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListResourcesRequestPaginateTypeDef(TypedDict):
    OrganizationId: str
    Filters: NotRequired[ListResourcesFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourcesRequestTypeDef(TypedDict):
    OrganizationId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[ListResourcesFiltersTypeDef]

class ListResourcesResponseTypeDef(TypedDict):
    Resources: List[ResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class ListUsersRequestPaginateTypeDef(TypedDict):
    OrganizationId: str
    Filters: NotRequired[ListUsersFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUsersRequestTypeDef(TypedDict):
    OrganizationId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[ListUsersFiltersTypeDef]

class ListUsersResponseTypeDef(TypedDict):
    Users: List[UserTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListAvailabilityConfigurationsResponseTypeDef(TypedDict):
    AvailabilityConfigurations: List[AvailabilityConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

CreateImpersonationRoleRequestTypeDef = TypedDict(
    "CreateImpersonationRoleRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
        "Type": ImpersonationRoleTypeType,
        "Rules": Sequence[ImpersonationRuleUnionTypeDef],
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
    },
)
UpdateImpersonationRoleRequestTypeDef = TypedDict(
    "UpdateImpersonationRoleRequestTypeDef",
    {
        "OrganizationId": str,
        "ImpersonationRoleId": str,
        "Name": str,
        "Type": ImpersonationRoleTypeType,
        "Rules": Sequence[ImpersonationRuleUnionTypeDef],
        "Description": NotRequired[str],
    },
)
