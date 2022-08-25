"""
Type annotations for workmail service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/type_defs.html)

Usage::

    ```python
    from mypy_boto3_workmail.type_defs import AccessControlRuleTypeDef

    data: AccessControlRuleTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AccessControlRuleEffectType,
    AvailabilityProviderTypeType,
    DnsRecordVerificationStatusType,
    EntityStateType,
    FolderNameType,
    MailboxExportJobStateType,
    MemberTypeType,
    MobileDeviceAccessRuleEffectType,
    PermissionTypeType,
    ResourceTypeType,
    RetentionActionType,
    UserRoleType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccessControlRuleTypeDef",
    "AssociateDelegateToResourceRequestRequestTypeDef",
    "AssociateMemberToGroupRequestRequestTypeDef",
    "AvailabilityConfigurationTypeDef",
    "BookingOptionsTypeDef",
    "CancelMailboxExportJobRequestRequestTypeDef",
    "CreateAliasRequestRequestTypeDef",
    "CreateAvailabilityConfigurationRequestRequestTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateMobileDeviceAccessRuleRequestRequestTypeDef",
    "CreateMobileDeviceAccessRuleResponseTypeDef",
    "CreateOrganizationRequestRequestTypeDef",
    "CreateOrganizationResponseTypeDef",
    "CreateResourceRequestRequestTypeDef",
    "CreateResourceResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserResponseTypeDef",
    "DelegateTypeDef",
    "DeleteAccessControlRuleRequestRequestTypeDef",
    "DeleteAliasRequestRequestTypeDef",
    "DeleteAvailabilityConfigurationRequestRequestTypeDef",
    "DeleteEmailMonitoringConfigurationRequestRequestTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteMailboxPermissionsRequestRequestTypeDef",
    "DeleteMobileDeviceAccessOverrideRequestRequestTypeDef",
    "DeleteMobileDeviceAccessRuleRequestRequestTypeDef",
    "DeleteOrganizationRequestRequestTypeDef",
    "DeleteOrganizationResponseTypeDef",
    "DeleteResourceRequestRequestTypeDef",
    "DeleteRetentionPolicyRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeregisterFromWorkMailRequestRequestTypeDef",
    "DeregisterMailDomainRequestRequestTypeDef",
    "DescribeEmailMonitoringConfigurationRequestRequestTypeDef",
    "DescribeEmailMonitoringConfigurationResponseTypeDef",
    "DescribeGroupRequestRequestTypeDef",
    "DescribeGroupResponseTypeDef",
    "DescribeInboundDmarcSettingsRequestRequestTypeDef",
    "DescribeInboundDmarcSettingsResponseTypeDef",
    "DescribeMailboxExportJobRequestRequestTypeDef",
    "DescribeMailboxExportJobResponseTypeDef",
    "DescribeOrganizationRequestRequestTypeDef",
    "DescribeOrganizationResponseTypeDef",
    "DescribeResourceRequestRequestTypeDef",
    "DescribeResourceResponseTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "DisassociateDelegateFromResourceRequestRequestTypeDef",
    "DisassociateMemberFromGroupRequestRequestTypeDef",
    "DnsRecordTypeDef",
    "DomainTypeDef",
    "EwsAvailabilityProviderTypeDef",
    "FolderConfigurationTypeDef",
    "GetAccessControlEffectRequestRequestTypeDef",
    "GetAccessControlEffectResponseTypeDef",
    "GetDefaultRetentionPolicyRequestRequestTypeDef",
    "GetDefaultRetentionPolicyResponseTypeDef",
    "GetMailDomainRequestRequestTypeDef",
    "GetMailDomainResponseTypeDef",
    "GetMailboxDetailsRequestRequestTypeDef",
    "GetMailboxDetailsResponseTypeDef",
    "GetMobileDeviceAccessEffectRequestRequestTypeDef",
    "GetMobileDeviceAccessEffectResponseTypeDef",
    "GetMobileDeviceAccessOverrideRequestRequestTypeDef",
    "GetMobileDeviceAccessOverrideResponseTypeDef",
    "GroupTypeDef",
    "LambdaAvailabilityProviderTypeDef",
    "ListAccessControlRulesRequestRequestTypeDef",
    "ListAccessControlRulesResponseTypeDef",
    "ListAliasesRequestRequestTypeDef",
    "ListAliasesResponseTypeDef",
    "ListAvailabilityConfigurationsRequestRequestTypeDef",
    "ListAvailabilityConfigurationsResponseTypeDef",
    "ListGroupMembersRequestRequestTypeDef",
    "ListGroupMembersResponseTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListGroupsResponseTypeDef",
    "ListMailDomainsRequestRequestTypeDef",
    "ListMailDomainsResponseTypeDef",
    "ListMailboxExportJobsRequestRequestTypeDef",
    "ListMailboxExportJobsResponseTypeDef",
    "ListMailboxPermissionsRequestRequestTypeDef",
    "ListMailboxPermissionsResponseTypeDef",
    "ListMobileDeviceAccessOverridesRequestRequestTypeDef",
    "ListMobileDeviceAccessOverridesResponseTypeDef",
    "ListMobileDeviceAccessRulesRequestRequestTypeDef",
    "ListMobileDeviceAccessRulesResponseTypeDef",
    "ListOrganizationsRequestRequestTypeDef",
    "ListOrganizationsResponseTypeDef",
    "ListResourceDelegatesRequestRequestTypeDef",
    "ListResourceDelegatesResponseTypeDef",
    "ListResourcesRequestRequestTypeDef",
    "ListResourcesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
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
    "PutAccessControlRuleRequestRequestTypeDef",
    "PutEmailMonitoringConfigurationRequestRequestTypeDef",
    "PutInboundDmarcSettingsRequestRequestTypeDef",
    "PutMailboxPermissionsRequestRequestTypeDef",
    "PutMobileDeviceAccessOverrideRequestRequestTypeDef",
    "PutRetentionPolicyRequestRequestTypeDef",
    "RedactedEwsAvailabilityProviderTypeDef",
    "RegisterMailDomainRequestRequestTypeDef",
    "RegisterToWorkMailRequestRequestTypeDef",
    "ResetPasswordRequestRequestTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "StartMailboxExportJobRequestRequestTypeDef",
    "StartMailboxExportJobResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TestAvailabilityConfigurationRequestRequestTypeDef",
    "TestAvailabilityConfigurationResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAvailabilityConfigurationRequestRequestTypeDef",
    "UpdateDefaultMailDomainRequestRequestTypeDef",
    "UpdateMailboxQuotaRequestRequestTypeDef",
    "UpdateMobileDeviceAccessRuleRequestRequestTypeDef",
    "UpdatePrimaryEmailAddressRequestRequestTypeDef",
    "UpdateResourceRequestRequestTypeDef",
    "UserTypeDef",
)

AccessControlRuleTypeDef = TypedDict(
    "AccessControlRuleTypeDef",
    {
        "Name": str,
        "Effect": AccessControlRuleEffectType,
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

AssociateDelegateToResourceRequestRequestTypeDef = TypedDict(
    "AssociateDelegateToResourceRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
        "EntityId": str,
    },
)

AssociateMemberToGroupRequestRequestTypeDef = TypedDict(
    "AssociateMemberToGroupRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "GroupId": str,
        "MemberId": str,
    },
)

AvailabilityConfigurationTypeDef = TypedDict(
    "AvailabilityConfigurationTypeDef",
    {
        "DomainName": str,
        "ProviderType": AvailabilityProviderTypeType,
        "EwsProvider": "RedactedEwsAvailabilityProviderTypeDef",
        "LambdaProvider": "LambdaAvailabilityProviderTypeDef",
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

CancelMailboxExportJobRequestRequestTypeDef = TypedDict(
    "CancelMailboxExportJobRequestRequestTypeDef",
    {
        "ClientToken": str,
        "JobId": str,
        "OrganizationId": str,
    },
)

CreateAliasRequestRequestTypeDef = TypedDict(
    "CreateAliasRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "Alias": str,
    },
)

_RequiredCreateAvailabilityConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAvailabilityConfigurationRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "DomainName": str,
    },
)
_OptionalCreateAvailabilityConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAvailabilityConfigurationRequestRequestTypeDef",
    {
        "ClientToken": str,
        "EwsProvider": "EwsAvailabilityProviderTypeDef",
        "LambdaProvider": "LambdaAvailabilityProviderTypeDef",
    },
    total=False,
)

class CreateAvailabilityConfigurationRequestRequestTypeDef(
    _RequiredCreateAvailabilityConfigurationRequestRequestTypeDef,
    _OptionalCreateAvailabilityConfigurationRequestRequestTypeDef,
):
    pass

CreateGroupRequestRequestTypeDef = TypedDict(
    "CreateGroupRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
    },
)

CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "GroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMobileDeviceAccessRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMobileDeviceAccessRuleRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
        "Effect": MobileDeviceAccessRuleEffectType,
    },
)
_OptionalCreateMobileDeviceAccessRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMobileDeviceAccessRuleRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "DeviceTypes": List[str],
        "NotDeviceTypes": List[str],
        "DeviceModels": List[str],
        "NotDeviceModels": List[str],
        "DeviceOperatingSystems": List[str],
        "NotDeviceOperatingSystems": List[str],
        "DeviceUserAgents": List[str],
        "NotDeviceUserAgents": List[str],
    },
    total=False,
)

class CreateMobileDeviceAccessRuleRequestRequestTypeDef(
    _RequiredCreateMobileDeviceAccessRuleRequestRequestTypeDef,
    _OptionalCreateMobileDeviceAccessRuleRequestRequestTypeDef,
):
    pass

CreateMobileDeviceAccessRuleResponseTypeDef = TypedDict(
    "CreateMobileDeviceAccessRuleResponseTypeDef",
    {
        "MobileDeviceAccessRuleId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateOrganizationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateOrganizationRequestRequestTypeDef",
    {
        "Alias": str,
    },
)
_OptionalCreateOrganizationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateOrganizationRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "ClientToken": str,
        "Domains": List["DomainTypeDef"],
        "KmsKeyArn": str,
        "EnableInteroperability": bool,
    },
    total=False,
)

class CreateOrganizationRequestRequestTypeDef(
    _RequiredCreateOrganizationRequestRequestTypeDef,
    _OptionalCreateOrganizationRequestRequestTypeDef,
):
    pass

CreateOrganizationResponseTypeDef = TypedDict(
    "CreateOrganizationResponseTypeDef",
    {
        "OrganizationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResourceRequestRequestTypeDef = TypedDict(
    "CreateResourceRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
        "Type": ResourceTypeType,
    },
)

CreateResourceResponseTypeDef = TypedDict(
    "CreateResourceResponseTypeDef",
    {
        "ResourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
        "DisplayName": str,
        "Password": str,
    },
)

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "UserId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DelegateTypeDef = TypedDict(
    "DelegateTypeDef",
    {
        "Id": str,
        "Type": MemberTypeType,
    },
)

DeleteAccessControlRuleRequestRequestTypeDef = TypedDict(
    "DeleteAccessControlRuleRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
    },
)

DeleteAliasRequestRequestTypeDef = TypedDict(
    "DeleteAliasRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "Alias": str,
    },
)

DeleteAvailabilityConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAvailabilityConfigurationRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "DomainName": str,
    },
)

DeleteEmailMonitoringConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteEmailMonitoringConfigurationRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)

DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "GroupId": str,
    },
)

DeleteMailboxPermissionsRequestRequestTypeDef = TypedDict(
    "DeleteMailboxPermissionsRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "GranteeId": str,
    },
)

DeleteMobileDeviceAccessOverrideRequestRequestTypeDef = TypedDict(
    "DeleteMobileDeviceAccessOverrideRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
        "DeviceId": str,
    },
)

DeleteMobileDeviceAccessRuleRequestRequestTypeDef = TypedDict(
    "DeleteMobileDeviceAccessRuleRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "MobileDeviceAccessRuleId": str,
    },
)

_RequiredDeleteOrganizationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteOrganizationRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "DeleteDirectory": bool,
    },
)
_OptionalDeleteOrganizationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteOrganizationRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class DeleteOrganizationRequestRequestTypeDef(
    _RequiredDeleteOrganizationRequestRequestTypeDef,
    _OptionalDeleteOrganizationRequestRequestTypeDef,
):
    pass

DeleteOrganizationResponseTypeDef = TypedDict(
    "DeleteOrganizationResponseTypeDef",
    {
        "OrganizationId": str,
        "State": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourceRequestRequestTypeDef = TypedDict(
    "DeleteResourceRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
    },
)

DeleteRetentionPolicyRequestRequestTypeDef = TypedDict(
    "DeleteRetentionPolicyRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Id": str,
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
    },
)

DeregisterFromWorkMailRequestRequestTypeDef = TypedDict(
    "DeregisterFromWorkMailRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
    },
)

DeregisterMailDomainRequestRequestTypeDef = TypedDict(
    "DeregisterMailDomainRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "DomainName": str,
    },
)

DescribeEmailMonitoringConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeEmailMonitoringConfigurationRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)

DescribeEmailMonitoringConfigurationResponseTypeDef = TypedDict(
    "DescribeEmailMonitoringConfigurationResponseTypeDef",
    {
        "RoleArn": str,
        "LogGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGroupRequestRequestTypeDef = TypedDict(
    "DescribeGroupRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "GroupId": str,
    },
)

DescribeGroupResponseTypeDef = TypedDict(
    "DescribeGroupResponseTypeDef",
    {
        "GroupId": str,
        "Name": str,
        "Email": str,
        "State": EntityStateType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInboundDmarcSettingsRequestRequestTypeDef = TypedDict(
    "DescribeInboundDmarcSettingsRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)

DescribeInboundDmarcSettingsResponseTypeDef = TypedDict(
    "DescribeInboundDmarcSettingsResponseTypeDef",
    {
        "Enforced": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMailboxExportJobRequestRequestTypeDef = TypedDict(
    "DescribeMailboxExportJobRequestRequestTypeDef",
    {
        "JobId": str,
        "OrganizationId": str,
    },
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
        "State": MailboxExportJobStateType,
        "ErrorInfo": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourceRequestRequestTypeDef = TypedDict(
    "DescribeResourceRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
    },
)

DescribeResourceResponseTypeDef = TypedDict(
    "DescribeResourceResponseTypeDef",
    {
        "ResourceId": str,
        "Email": str,
        "Name": str,
        "Type": ResourceTypeType,
        "BookingOptions": "BookingOptionsTypeDef",
        "State": EntityStateType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
    },
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "UserId": str,
        "Name": str,
        "Email": str,
        "DisplayName": str,
        "State": EntityStateType,
        "UserRole": UserRoleType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateDelegateFromResourceRequestRequestTypeDef = TypedDict(
    "DisassociateDelegateFromResourceRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
        "EntityId": str,
    },
)

DisassociateMemberFromGroupRequestRequestTypeDef = TypedDict(
    "DisassociateMemberFromGroupRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "GroupId": str,
        "MemberId": str,
    },
)

DnsRecordTypeDef = TypedDict(
    "DnsRecordTypeDef",
    {
        "Type": str,
        "Hostname": str,
        "Value": str,
    },
    total=False,
)

DomainTypeDef = TypedDict(
    "DomainTypeDef",
    {
        "DomainName": str,
        "HostedZoneId": str,
    },
    total=False,
)

EwsAvailabilityProviderTypeDef = TypedDict(
    "EwsAvailabilityProviderTypeDef",
    {
        "EwsEndpoint": str,
        "EwsUsername": str,
        "EwsPassword": str,
    },
)

_RequiredFolderConfigurationTypeDef = TypedDict(
    "_RequiredFolderConfigurationTypeDef",
    {
        "Name": FolderNameType,
        "Action": RetentionActionType,
    },
)
_OptionalFolderConfigurationTypeDef = TypedDict(
    "_OptionalFolderConfigurationTypeDef",
    {
        "Period": int,
    },
    total=False,
)

class FolderConfigurationTypeDef(
    _RequiredFolderConfigurationTypeDef, _OptionalFolderConfigurationTypeDef
):
    pass

GetAccessControlEffectRequestRequestTypeDef = TypedDict(
    "GetAccessControlEffectRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "IpAddress": str,
        "Action": str,
        "UserId": str,
    },
)

GetAccessControlEffectResponseTypeDef = TypedDict(
    "GetAccessControlEffectResponseTypeDef",
    {
        "Effect": AccessControlRuleEffectType,
        "MatchedRules": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDefaultRetentionPolicyRequestRequestTypeDef = TypedDict(
    "GetDefaultRetentionPolicyRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)

GetDefaultRetentionPolicyResponseTypeDef = TypedDict(
    "GetDefaultRetentionPolicyResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "FolderConfigurations": List["FolderConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMailDomainRequestRequestTypeDef = TypedDict(
    "GetMailDomainRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "DomainName": str,
    },
)

GetMailDomainResponseTypeDef = TypedDict(
    "GetMailDomainResponseTypeDef",
    {
        "Records": List["DnsRecordTypeDef"],
        "IsTestDomain": bool,
        "IsDefault": bool,
        "OwnershipVerificationStatus": DnsRecordVerificationStatusType,
        "DkimVerificationStatus": DnsRecordVerificationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMailboxDetailsRequestRequestTypeDef = TypedDict(
    "GetMailboxDetailsRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
    },
)

GetMailboxDetailsResponseTypeDef = TypedDict(
    "GetMailboxDetailsResponseTypeDef",
    {
        "MailboxQuota": int,
        "MailboxSize": float,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMobileDeviceAccessEffectRequestRequestTypeDef = TypedDict(
    "_RequiredGetMobileDeviceAccessEffectRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
_OptionalGetMobileDeviceAccessEffectRequestRequestTypeDef = TypedDict(
    "_OptionalGetMobileDeviceAccessEffectRequestRequestTypeDef",
    {
        "DeviceType": str,
        "DeviceModel": str,
        "DeviceOperatingSystem": str,
        "DeviceUserAgent": str,
    },
    total=False,
)

class GetMobileDeviceAccessEffectRequestRequestTypeDef(
    _RequiredGetMobileDeviceAccessEffectRequestRequestTypeDef,
    _OptionalGetMobileDeviceAccessEffectRequestRequestTypeDef,
):
    pass

GetMobileDeviceAccessEffectResponseTypeDef = TypedDict(
    "GetMobileDeviceAccessEffectResponseTypeDef",
    {
        "Effect": MobileDeviceAccessRuleEffectType,
        "MatchedRules": List["MobileDeviceAccessMatchedRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMobileDeviceAccessOverrideRequestRequestTypeDef = TypedDict(
    "GetMobileDeviceAccessOverrideRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
        "DeviceId": str,
    },
)

GetMobileDeviceAccessOverrideResponseTypeDef = TypedDict(
    "GetMobileDeviceAccessOverrideResponseTypeDef",
    {
        "UserId": str,
        "DeviceId": str,
        "Effect": MobileDeviceAccessRuleEffectType,
        "Description": str,
        "DateCreated": datetime,
        "DateModified": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "State": EntityStateType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

LambdaAvailabilityProviderTypeDef = TypedDict(
    "LambdaAvailabilityProviderTypeDef",
    {
        "LambdaArn": str,
    },
)

ListAccessControlRulesRequestRequestTypeDef = TypedDict(
    "ListAccessControlRulesRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)

ListAccessControlRulesResponseTypeDef = TypedDict(
    "ListAccessControlRulesResponseTypeDef",
    {
        "Rules": List["AccessControlRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredListAliasesRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
    },
)
_OptionalListAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalListAliasesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListAliasesRequestRequestTypeDef(
    _RequiredListAliasesRequestRequestTypeDef, _OptionalListAliasesRequestRequestTypeDef
):
    pass

ListAliasesResponseTypeDef = TypedDict(
    "ListAliasesResponseTypeDef",
    {
        "Aliases": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAvailabilityConfigurationsRequestRequestTypeDef = TypedDict(
    "_RequiredListAvailabilityConfigurationsRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
_OptionalListAvailabilityConfigurationsRequestRequestTypeDef = TypedDict(
    "_OptionalListAvailabilityConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAvailabilityConfigurationsRequestRequestTypeDef(
    _RequiredListAvailabilityConfigurationsRequestRequestTypeDef,
    _OptionalListAvailabilityConfigurationsRequestRequestTypeDef,
):
    pass

ListAvailabilityConfigurationsResponseTypeDef = TypedDict(
    "ListAvailabilityConfigurationsResponseTypeDef",
    {
        "AvailabilityConfigurations": List["AvailabilityConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupMembersRequestRequestTypeDef = TypedDict(
    "_RequiredListGroupMembersRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "GroupId": str,
    },
)
_OptionalListGroupMembersRequestRequestTypeDef = TypedDict(
    "_OptionalListGroupMembersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListGroupMembersRequestRequestTypeDef(
    _RequiredListGroupMembersRequestRequestTypeDef, _OptionalListGroupMembersRequestRequestTypeDef
):
    pass

ListGroupMembersResponseTypeDef = TypedDict(
    "ListGroupMembersResponseTypeDef",
    {
        "Members": List["MemberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListGroupsRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
_OptionalListGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListGroupsRequestRequestTypeDef(
    _RequiredListGroupsRequestRequestTypeDef, _OptionalListGroupsRequestRequestTypeDef
):
    pass

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "Groups": List["GroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMailDomainsRequestRequestTypeDef = TypedDict(
    "_RequiredListMailDomainsRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
_OptionalListMailDomainsRequestRequestTypeDef = TypedDict(
    "_OptionalListMailDomainsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListMailDomainsRequestRequestTypeDef(
    _RequiredListMailDomainsRequestRequestTypeDef, _OptionalListMailDomainsRequestRequestTypeDef
):
    pass

ListMailDomainsResponseTypeDef = TypedDict(
    "ListMailDomainsResponseTypeDef",
    {
        "MailDomains": List["MailDomainSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMailboxExportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListMailboxExportJobsRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
_OptionalListMailboxExportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListMailboxExportJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListMailboxExportJobsRequestRequestTypeDef(
    _RequiredListMailboxExportJobsRequestRequestTypeDef,
    _OptionalListMailboxExportJobsRequestRequestTypeDef,
):
    pass

ListMailboxExportJobsResponseTypeDef = TypedDict(
    "ListMailboxExportJobsResponseTypeDef",
    {
        "Jobs": List["MailboxExportJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMailboxPermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredListMailboxPermissionsRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
    },
)
_OptionalListMailboxPermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalListMailboxPermissionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListMailboxPermissionsRequestRequestTypeDef(
    _RequiredListMailboxPermissionsRequestRequestTypeDef,
    _OptionalListMailboxPermissionsRequestRequestTypeDef,
):
    pass

ListMailboxPermissionsResponseTypeDef = TypedDict(
    "ListMailboxPermissionsResponseTypeDef",
    {
        "Permissions": List["PermissionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMobileDeviceAccessOverridesRequestRequestTypeDef = TypedDict(
    "_RequiredListMobileDeviceAccessOverridesRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
_OptionalListMobileDeviceAccessOverridesRequestRequestTypeDef = TypedDict(
    "_OptionalListMobileDeviceAccessOverridesRequestRequestTypeDef",
    {
        "UserId": str,
        "DeviceId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListMobileDeviceAccessOverridesRequestRequestTypeDef(
    _RequiredListMobileDeviceAccessOverridesRequestRequestTypeDef,
    _OptionalListMobileDeviceAccessOverridesRequestRequestTypeDef,
):
    pass

ListMobileDeviceAccessOverridesResponseTypeDef = TypedDict(
    "ListMobileDeviceAccessOverridesResponseTypeDef",
    {
        "Overrides": List["MobileDeviceAccessOverrideTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMobileDeviceAccessRulesRequestRequestTypeDef = TypedDict(
    "ListMobileDeviceAccessRulesRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)

ListMobileDeviceAccessRulesResponseTypeDef = TypedDict(
    "ListMobileDeviceAccessRulesResponseTypeDef",
    {
        "Rules": List["MobileDeviceAccessRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOrganizationsRequestRequestTypeDef = TypedDict(
    "ListOrganizationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListOrganizationsResponseTypeDef = TypedDict(
    "ListOrganizationsResponseTypeDef",
    {
        "OrganizationSummaries": List["OrganizationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourceDelegatesRequestRequestTypeDef = TypedDict(
    "_RequiredListResourceDelegatesRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
    },
)
_OptionalListResourceDelegatesRequestRequestTypeDef = TypedDict(
    "_OptionalListResourceDelegatesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListResourceDelegatesRequestRequestTypeDef(
    _RequiredListResourceDelegatesRequestRequestTypeDef,
    _OptionalListResourceDelegatesRequestRequestTypeDef,
):
    pass

ListResourceDelegatesResponseTypeDef = TypedDict(
    "ListResourceDelegatesResponseTypeDef",
    {
        "Delegates": List["DelegateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListResourcesRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
_OptionalListResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListResourcesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListResourcesRequestRequestTypeDef(
    _RequiredListResourcesRequestRequestTypeDef, _OptionalListResourcesRequestRequestTypeDef
):
    pass

ListResourcesResponseTypeDef = TypedDict(
    "ListResourcesResponseTypeDef",
    {
        "Resources": List["ResourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
_OptionalListUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListUsersRequestRequestTypeDef(
    _RequiredListUsersRequestRequestTypeDef, _OptionalListUsersRequestRequestTypeDef
):
    pass

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "Users": List["UserTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MailDomainSummaryTypeDef = TypedDict(
    "MailDomainSummaryTypeDef",
    {
        "DomainName": str,
        "DefaultDomain": bool,
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
        "State": MailboxExportJobStateType,
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
        "Type": MemberTypeType,
        "State": EntityStateType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

MobileDeviceAccessMatchedRuleTypeDef = TypedDict(
    "MobileDeviceAccessMatchedRuleTypeDef",
    {
        "MobileDeviceAccessRuleId": str,
        "Name": str,
    },
    total=False,
)

MobileDeviceAccessOverrideTypeDef = TypedDict(
    "MobileDeviceAccessOverrideTypeDef",
    {
        "UserId": str,
        "DeviceId": str,
        "Effect": MobileDeviceAccessRuleEffectType,
        "Description": str,
        "DateCreated": datetime,
        "DateModified": datetime,
    },
    total=False,
)

MobileDeviceAccessRuleTypeDef = TypedDict(
    "MobileDeviceAccessRuleTypeDef",
    {
        "MobileDeviceAccessRuleId": str,
        "Name": str,
        "Description": str,
        "Effect": MobileDeviceAccessRuleEffectType,
        "DeviceTypes": List[str],
        "NotDeviceTypes": List[str],
        "DeviceModels": List[str],
        "NotDeviceModels": List[str],
        "DeviceOperatingSystems": List[str],
        "NotDeviceOperatingSystems": List[str],
        "DeviceUserAgents": List[str],
        "NotDeviceUserAgents": List[str],
        "DateCreated": datetime,
        "DateModified": datetime,
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "GranteeId": str,
        "GranteeType": MemberTypeType,
        "PermissionValues": List[PermissionTypeType],
    },
)

_RequiredPutAccessControlRuleRequestRequestTypeDef = TypedDict(
    "_RequiredPutAccessControlRuleRequestRequestTypeDef",
    {
        "Name": str,
        "Effect": AccessControlRuleEffectType,
        "Description": str,
        "OrganizationId": str,
    },
)
_OptionalPutAccessControlRuleRequestRequestTypeDef = TypedDict(
    "_OptionalPutAccessControlRuleRequestRequestTypeDef",
    {
        "IpRanges": List[str],
        "NotIpRanges": List[str],
        "Actions": List[str],
        "NotActions": List[str],
        "UserIds": List[str],
        "NotUserIds": List[str],
    },
    total=False,
)

class PutAccessControlRuleRequestRequestTypeDef(
    _RequiredPutAccessControlRuleRequestRequestTypeDef,
    _OptionalPutAccessControlRuleRequestRequestTypeDef,
):
    pass

PutEmailMonitoringConfigurationRequestRequestTypeDef = TypedDict(
    "PutEmailMonitoringConfigurationRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "RoleArn": str,
        "LogGroupArn": str,
    },
)

PutInboundDmarcSettingsRequestRequestTypeDef = TypedDict(
    "PutInboundDmarcSettingsRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Enforced": bool,
    },
)

PutMailboxPermissionsRequestRequestTypeDef = TypedDict(
    "PutMailboxPermissionsRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "GranteeId": str,
        "PermissionValues": List[PermissionTypeType],
    },
)

_RequiredPutMobileDeviceAccessOverrideRequestRequestTypeDef = TypedDict(
    "_RequiredPutMobileDeviceAccessOverrideRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
        "DeviceId": str,
        "Effect": MobileDeviceAccessRuleEffectType,
    },
)
_OptionalPutMobileDeviceAccessOverrideRequestRequestTypeDef = TypedDict(
    "_OptionalPutMobileDeviceAccessOverrideRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class PutMobileDeviceAccessOverrideRequestRequestTypeDef(
    _RequiredPutMobileDeviceAccessOverrideRequestRequestTypeDef,
    _OptionalPutMobileDeviceAccessOverrideRequestRequestTypeDef,
):
    pass

_RequiredPutRetentionPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutRetentionPolicyRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
        "FolderConfigurations": List["FolderConfigurationTypeDef"],
    },
)
_OptionalPutRetentionPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutRetentionPolicyRequestRequestTypeDef",
    {
        "Id": str,
        "Description": str,
    },
    total=False,
)

class PutRetentionPolicyRequestRequestTypeDef(
    _RequiredPutRetentionPolicyRequestRequestTypeDef,
    _OptionalPutRetentionPolicyRequestRequestTypeDef,
):
    pass

RedactedEwsAvailabilityProviderTypeDef = TypedDict(
    "RedactedEwsAvailabilityProviderTypeDef",
    {
        "EwsEndpoint": str,
        "EwsUsername": str,
    },
    total=False,
)

_RequiredRegisterMailDomainRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterMailDomainRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "DomainName": str,
    },
)
_OptionalRegisterMailDomainRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterMailDomainRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class RegisterMailDomainRequestRequestTypeDef(
    _RequiredRegisterMailDomainRequestRequestTypeDef,
    _OptionalRegisterMailDomainRequestRequestTypeDef,
):
    pass

RegisterToWorkMailRequestRequestTypeDef = TypedDict(
    "RegisterToWorkMailRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "Email": str,
    },
)

ResetPasswordRequestRequestTypeDef = TypedDict(
    "ResetPasswordRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
        "Password": str,
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "Type": ResourceTypeType,
        "State": EntityStateType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
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

_RequiredStartMailboxExportJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartMailboxExportJobRequestRequestTypeDef",
    {
        "ClientToken": str,
        "OrganizationId": str,
        "EntityId": str,
        "RoleArn": str,
        "KmsKeyArn": str,
        "S3BucketName": str,
        "S3Prefix": str,
    },
)
_OptionalStartMailboxExportJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartMailboxExportJobRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class StartMailboxExportJobRequestRequestTypeDef(
    _RequiredStartMailboxExportJobRequestRequestTypeDef,
    _OptionalStartMailboxExportJobRequestRequestTypeDef,
):
    pass

StartMailboxExportJobResponseTypeDef = TypedDict(
    "StartMailboxExportJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredTestAvailabilityConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredTestAvailabilityConfigurationRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
_OptionalTestAvailabilityConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalTestAvailabilityConfigurationRequestRequestTypeDef",
    {
        "DomainName": str,
        "EwsProvider": "EwsAvailabilityProviderTypeDef",
        "LambdaProvider": "LambdaAvailabilityProviderTypeDef",
    },
    total=False,
)

class TestAvailabilityConfigurationRequestRequestTypeDef(
    _RequiredTestAvailabilityConfigurationRequestRequestTypeDef,
    _OptionalTestAvailabilityConfigurationRequestRequestTypeDef,
):
    pass

TestAvailabilityConfigurationResponseTypeDef = TypedDict(
    "TestAvailabilityConfigurationResponseTypeDef",
    {
        "TestPassed": bool,
        "FailureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAvailabilityConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAvailabilityConfigurationRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "DomainName": str,
    },
)
_OptionalUpdateAvailabilityConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAvailabilityConfigurationRequestRequestTypeDef",
    {
        "EwsProvider": "EwsAvailabilityProviderTypeDef",
        "LambdaProvider": "LambdaAvailabilityProviderTypeDef",
    },
    total=False,
)

class UpdateAvailabilityConfigurationRequestRequestTypeDef(
    _RequiredUpdateAvailabilityConfigurationRequestRequestTypeDef,
    _OptionalUpdateAvailabilityConfigurationRequestRequestTypeDef,
):
    pass

UpdateDefaultMailDomainRequestRequestTypeDef = TypedDict(
    "UpdateDefaultMailDomainRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "DomainName": str,
    },
)

UpdateMailboxQuotaRequestRequestTypeDef = TypedDict(
    "UpdateMailboxQuotaRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
        "MailboxQuota": int,
    },
)

_RequiredUpdateMobileDeviceAccessRuleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMobileDeviceAccessRuleRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "MobileDeviceAccessRuleId": str,
        "Name": str,
        "Effect": MobileDeviceAccessRuleEffectType,
    },
)
_OptionalUpdateMobileDeviceAccessRuleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMobileDeviceAccessRuleRequestRequestTypeDef",
    {
        "Description": str,
        "DeviceTypes": List[str],
        "NotDeviceTypes": List[str],
        "DeviceModels": List[str],
        "NotDeviceModels": List[str],
        "DeviceOperatingSystems": List[str],
        "NotDeviceOperatingSystems": List[str],
        "DeviceUserAgents": List[str],
        "NotDeviceUserAgents": List[str],
    },
    total=False,
)

class UpdateMobileDeviceAccessRuleRequestRequestTypeDef(
    _RequiredUpdateMobileDeviceAccessRuleRequestRequestTypeDef,
    _OptionalUpdateMobileDeviceAccessRuleRequestRequestTypeDef,
):
    pass

UpdatePrimaryEmailAddressRequestRequestTypeDef = TypedDict(
    "UpdatePrimaryEmailAddressRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "Email": str,
    },
)

_RequiredUpdateResourceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateResourceRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
    },
)
_OptionalUpdateResourceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateResourceRequestRequestTypeDef",
    {
        "Name": str,
        "BookingOptions": "BookingOptionsTypeDef",
    },
    total=False,
)

class UpdateResourceRequestRequestTypeDef(
    _RequiredUpdateResourceRequestRequestTypeDef, _OptionalUpdateResourceRequestRequestTypeDef
):
    pass

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "DisplayName": str,
        "State": EntityStateType,
        "UserRole": UserRoleType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)
