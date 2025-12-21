"""
Type annotations for ds service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_ds.type_defs import AcceptSharedDirectoryRequestTypeDef

    data: AcceptSharedDirectoryRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    CaEnrollmentPolicyStatusType,
    CertificateStateType,
    CertificateTypeType,
    ClientAuthenticationStatusType,
    ClientAuthenticationTypeType,
    DataAccessStatusType,
    DirectoryConfigurationStatusType,
    DirectoryEditionType,
    DirectorySizeType,
    DirectoryStageType,
    DirectoryTypeType,
    DomainControllerStatusType,
    HybridUpdateTypeType,
    IpRouteStatusMsgType,
    LDAPSStatusType,
    NetworkTypeType,
    OSVersionType,
    RadiusAuthenticationProtocolType,
    RadiusStatusType,
    RegionTypeType,
    SchemaExtensionStatusType,
    SelectiveAuthType,
    ShareMethodType,
    ShareStatusType,
    SnapshotStatusType,
    SnapshotTypeType,
    TopicStatusType,
    TrustDirectionType,
    TrustStateType,
    TrustTypeType,
    UpdateStatusType,
    UpdateTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AcceptSharedDirectoryRequestTypeDef",
    "AcceptSharedDirectoryResultTypeDef",
    "AddIpRoutesRequestTypeDef",
    "AddRegionRequestTypeDef",
    "AddTagsToResourceRequestTypeDef",
    "AssessmentConfigurationTypeDef",
    "AssessmentReportTypeDef",
    "AssessmentSummaryTypeDef",
    "AssessmentTypeDef",
    "AssessmentValidationTypeDef",
    "AttributeTypeDef",
    "CancelSchemaExtensionRequestTypeDef",
    "CertificateInfoTypeDef",
    "CertificateTypeDef",
    "ClientAuthenticationSettingInfoTypeDef",
    "ClientCertAuthSettingsTypeDef",
    "ComputerTypeDef",
    "ConditionalForwarderTypeDef",
    "ConnectDirectoryRequestTypeDef",
    "ConnectDirectoryResultTypeDef",
    "CreateAliasRequestTypeDef",
    "CreateAliasResultTypeDef",
    "CreateComputerRequestTypeDef",
    "CreateComputerResultTypeDef",
    "CreateConditionalForwarderRequestTypeDef",
    "CreateDirectoryRequestTypeDef",
    "CreateDirectoryResultTypeDef",
    "CreateHybridADRequestTypeDef",
    "CreateHybridADResultTypeDef",
    "CreateLogSubscriptionRequestTypeDef",
    "CreateMicrosoftADRequestTypeDef",
    "CreateMicrosoftADResultTypeDef",
    "CreateSnapshotRequestTypeDef",
    "CreateSnapshotResultTypeDef",
    "CreateTrustRequestTypeDef",
    "CreateTrustResultTypeDef",
    "DeleteADAssessmentRequestTypeDef",
    "DeleteADAssessmentResultTypeDef",
    "DeleteConditionalForwarderRequestTypeDef",
    "DeleteDirectoryRequestTypeDef",
    "DeleteDirectoryResultTypeDef",
    "DeleteLogSubscriptionRequestTypeDef",
    "DeleteSnapshotRequestTypeDef",
    "DeleteSnapshotResultTypeDef",
    "DeleteTrustRequestTypeDef",
    "DeleteTrustResultTypeDef",
    "DeregisterCertificateRequestTypeDef",
    "DeregisterEventTopicRequestTypeDef",
    "DescribeADAssessmentRequestTypeDef",
    "DescribeADAssessmentResultTypeDef",
    "DescribeCAEnrollmentPolicyRequestTypeDef",
    "DescribeCAEnrollmentPolicyResultTypeDef",
    "DescribeCertificateRequestTypeDef",
    "DescribeCertificateResultTypeDef",
    "DescribeClientAuthenticationSettingsRequestPaginateTypeDef",
    "DescribeClientAuthenticationSettingsRequestTypeDef",
    "DescribeClientAuthenticationSettingsResultTypeDef",
    "DescribeConditionalForwardersRequestTypeDef",
    "DescribeConditionalForwardersResultTypeDef",
    "DescribeDirectoriesRequestPaginateTypeDef",
    "DescribeDirectoriesRequestTypeDef",
    "DescribeDirectoriesResultTypeDef",
    "DescribeDirectoryDataAccessRequestTypeDef",
    "DescribeDirectoryDataAccessResultTypeDef",
    "DescribeDomainControllersRequestPaginateTypeDef",
    "DescribeDomainControllersRequestTypeDef",
    "DescribeDomainControllersResultTypeDef",
    "DescribeEventTopicsRequestTypeDef",
    "DescribeEventTopicsResultTypeDef",
    "DescribeHybridADUpdateRequestTypeDef",
    "DescribeHybridADUpdateRequestWaitTypeDef",
    "DescribeHybridADUpdateResultTypeDef",
    "DescribeLDAPSSettingsRequestPaginateTypeDef",
    "DescribeLDAPSSettingsRequestTypeDef",
    "DescribeLDAPSSettingsResultTypeDef",
    "DescribeRegionsRequestPaginateTypeDef",
    "DescribeRegionsRequestTypeDef",
    "DescribeRegionsResultTypeDef",
    "DescribeSettingsRequestTypeDef",
    "DescribeSettingsResultTypeDef",
    "DescribeSharedDirectoriesRequestPaginateTypeDef",
    "DescribeSharedDirectoriesRequestTypeDef",
    "DescribeSharedDirectoriesResultTypeDef",
    "DescribeSnapshotsRequestPaginateTypeDef",
    "DescribeSnapshotsRequestTypeDef",
    "DescribeSnapshotsResultTypeDef",
    "DescribeTrustsRequestPaginateTypeDef",
    "DescribeTrustsRequestTypeDef",
    "DescribeTrustsResultTypeDef",
    "DescribeUpdateDirectoryRequestPaginateTypeDef",
    "DescribeUpdateDirectoryRequestTypeDef",
    "DescribeUpdateDirectoryResultTypeDef",
    "DirectoryConnectSettingsDescriptionTypeDef",
    "DirectoryConnectSettingsTypeDef",
    "DirectoryDescriptionTypeDef",
    "DirectoryLimitsTypeDef",
    "DirectorySizeUpdateSettingsTypeDef",
    "DirectoryVpcSettingsDescriptionTypeDef",
    "DirectoryVpcSettingsOutputTypeDef",
    "DirectoryVpcSettingsTypeDef",
    "DirectoryVpcSettingsUnionTypeDef",
    "DisableCAEnrollmentPolicyRequestTypeDef",
    "DisableClientAuthenticationRequestTypeDef",
    "DisableDirectoryDataAccessRequestTypeDef",
    "DisableLDAPSRequestTypeDef",
    "DisableRadiusRequestTypeDef",
    "DisableSsoRequestTypeDef",
    "DomainControllerTypeDef",
    "EnableCAEnrollmentPolicyRequestTypeDef",
    "EnableClientAuthenticationRequestTypeDef",
    "EnableDirectoryDataAccessRequestTypeDef",
    "EnableLDAPSRequestTypeDef",
    "EnableRadiusRequestTypeDef",
    "EnableSsoRequestTypeDef",
    "EventTopicTypeDef",
    "GetDirectoryLimitsResultTypeDef",
    "GetSnapshotLimitsRequestTypeDef",
    "GetSnapshotLimitsResultTypeDef",
    "HybridAdministratorAccountUpdateTypeDef",
    "HybridCustomerInstancesSettingsTypeDef",
    "HybridSettingsDescriptionTypeDef",
    "HybridUpdateActivitiesTypeDef",
    "HybridUpdateInfoEntryTypeDef",
    "HybridUpdateValueTypeDef",
    "IpRouteInfoTypeDef",
    "IpRouteTypeDef",
    "LDAPSSettingInfoTypeDef",
    "ListADAssessmentsRequestPaginateTypeDef",
    "ListADAssessmentsRequestTypeDef",
    "ListADAssessmentsResultTypeDef",
    "ListCertificatesRequestPaginateTypeDef",
    "ListCertificatesRequestTypeDef",
    "ListCertificatesResultTypeDef",
    "ListIpRoutesRequestPaginateTypeDef",
    "ListIpRoutesRequestTypeDef",
    "ListIpRoutesResultTypeDef",
    "ListLogSubscriptionsRequestPaginateTypeDef",
    "ListLogSubscriptionsRequestTypeDef",
    "ListLogSubscriptionsResultTypeDef",
    "ListSchemaExtensionsRequestPaginateTypeDef",
    "ListSchemaExtensionsRequestTypeDef",
    "ListSchemaExtensionsResultTypeDef",
    "ListTagsForResourceRequestPaginateTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "LogSubscriptionTypeDef",
    "NetworkUpdateSettingsTypeDef",
    "OSUpdateSettingsTypeDef",
    "OwnerDirectoryDescriptionTypeDef",
    "PaginatorConfigTypeDef",
    "RadiusSettingsOutputTypeDef",
    "RadiusSettingsTypeDef",
    "RadiusSettingsUnionTypeDef",
    "RegionDescriptionTypeDef",
    "RegionsInfoTypeDef",
    "RegisterCertificateRequestTypeDef",
    "RegisterCertificateResultTypeDef",
    "RegisterEventTopicRequestTypeDef",
    "RejectSharedDirectoryRequestTypeDef",
    "RejectSharedDirectoryResultTypeDef",
    "RemoveIpRoutesRequestTypeDef",
    "RemoveRegionRequestTypeDef",
    "RemoveTagsFromResourceRequestTypeDef",
    "ResetUserPasswordRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreFromSnapshotRequestTypeDef",
    "SchemaExtensionInfoTypeDef",
    "SettingEntryTypeDef",
    "SettingTypeDef",
    "ShareDirectoryRequestTypeDef",
    "ShareDirectoryResultTypeDef",
    "ShareTargetTypeDef",
    "SharedDirectoryTypeDef",
    "SnapshotLimitsTypeDef",
    "SnapshotTypeDef",
    "StartADAssessmentRequestTypeDef",
    "StartADAssessmentResultTypeDef",
    "StartSchemaExtensionRequestTypeDef",
    "StartSchemaExtensionResultTypeDef",
    "TagTypeDef",
    "TrustTypeDef",
    "UnshareDirectoryRequestTypeDef",
    "UnshareDirectoryResultTypeDef",
    "UnshareTargetTypeDef",
    "UpdateConditionalForwarderRequestTypeDef",
    "UpdateDirectorySetupRequestTypeDef",
    "UpdateHybridADRequestTypeDef",
    "UpdateHybridADResultTypeDef",
    "UpdateInfoEntryTypeDef",
    "UpdateNumberOfDomainControllersRequestTypeDef",
    "UpdateRadiusRequestTypeDef",
    "UpdateSettingsRequestTypeDef",
    "UpdateSettingsResultTypeDef",
    "UpdateTrustRequestTypeDef",
    "UpdateTrustResultTypeDef",
    "UpdateValueTypeDef",
    "VerifyTrustRequestTypeDef",
    "VerifyTrustResultTypeDef",
    "WaiterConfigTypeDef",
)

class AcceptSharedDirectoryRequestTypeDef(TypedDict):
    SharedDirectoryId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class SharedDirectoryTypeDef(TypedDict):
    OwnerAccountId: NotRequired[str]
    OwnerDirectoryId: NotRequired[str]
    ShareMethod: NotRequired[ShareMethodType]
    SharedAccountId: NotRequired[str]
    SharedDirectoryId: NotRequired[str]
    ShareStatus: NotRequired[ShareStatusType]
    ShareNotes: NotRequired[str]
    CreatedDateTime: NotRequired[datetime]
    LastUpdatedDateTime: NotRequired[datetime]

class IpRouteTypeDef(TypedDict):
    CidrIp: NotRequired[str]
    CidrIpv6: NotRequired[str]
    Description: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class AssessmentValidationTypeDef(TypedDict):
    Category: NotRequired[str]
    Name: NotRequired[str]
    Status: NotRequired[str]
    StatusCode: NotRequired[str]
    StatusReason: NotRequired[str]
    StartTime: NotRequired[datetime]
    LastUpdateDateTime: NotRequired[datetime]

class AssessmentSummaryTypeDef(TypedDict):
    AssessmentId: NotRequired[str]
    DirectoryId: NotRequired[str]
    DnsName: NotRequired[str]
    StartTime: NotRequired[datetime]
    LastUpdateDateTime: NotRequired[datetime]
    Status: NotRequired[str]
    CustomerDnsIps: NotRequired[List[str]]
    ReportType: NotRequired[str]

class AssessmentTypeDef(TypedDict):
    AssessmentId: NotRequired[str]
    DirectoryId: NotRequired[str]
    DnsName: NotRequired[str]
    StartTime: NotRequired[datetime]
    LastUpdateDateTime: NotRequired[datetime]
    Status: NotRequired[str]
    StatusCode: NotRequired[str]
    StatusReason: NotRequired[str]
    CustomerDnsIps: NotRequired[List[str]]
    VpcId: NotRequired[str]
    SubnetIds: NotRequired[List[str]]
    SecurityGroupIds: NotRequired[List[str]]
    SelfManagedInstanceIds: NotRequired[List[str]]
    ReportType: NotRequired[str]
    Version: NotRequired[str]

class AttributeTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]

class CancelSchemaExtensionRequestTypeDef(TypedDict):
    DirectoryId: str
    SchemaExtensionId: str

CertificateInfoTypeDef = TypedDict(
    "CertificateInfoTypeDef",
    {
        "CertificateId": NotRequired[str],
        "CommonName": NotRequired[str],
        "State": NotRequired[CertificateStateType],
        "ExpiryDateTime": NotRequired[datetime],
        "Type": NotRequired[CertificateTypeType],
    },
)

class ClientCertAuthSettingsTypeDef(TypedDict):
    OCSPUrl: NotRequired[str]

ClientAuthenticationSettingInfoTypeDef = TypedDict(
    "ClientAuthenticationSettingInfoTypeDef",
    {
        "Type": NotRequired[ClientAuthenticationTypeType],
        "Status": NotRequired[ClientAuthenticationStatusType],
        "LastUpdatedDateTime": NotRequired[datetime],
    },
)

class ConditionalForwarderTypeDef(TypedDict):
    RemoteDomainName: NotRequired[str]
    DnsIpAddrs: NotRequired[List[str]]
    DnsIpv6Addrs: NotRequired[List[str]]
    ReplicationScope: NotRequired[Literal["Domain"]]

class DirectoryConnectSettingsTypeDef(TypedDict):
    VpcId: str
    SubnetIds: Sequence[str]
    CustomerUserName: str
    CustomerDnsIps: NotRequired[Sequence[str]]
    CustomerDnsIpsV6: NotRequired[Sequence[str]]

class CreateAliasRequestTypeDef(TypedDict):
    DirectoryId: str
    Alias: str

class CreateConditionalForwarderRequestTypeDef(TypedDict):
    DirectoryId: str
    RemoteDomainName: str
    DnsIpAddrs: NotRequired[Sequence[str]]
    DnsIpv6Addrs: NotRequired[Sequence[str]]

class CreateLogSubscriptionRequestTypeDef(TypedDict):
    DirectoryId: str
    LogGroupName: str

class CreateSnapshotRequestTypeDef(TypedDict):
    DirectoryId: str
    Name: NotRequired[str]

class CreateTrustRequestTypeDef(TypedDict):
    DirectoryId: str
    RemoteDomainName: str
    TrustPassword: str
    TrustDirection: TrustDirectionType
    TrustType: NotRequired[TrustTypeType]
    ConditionalForwarderIpAddrs: NotRequired[Sequence[str]]
    ConditionalForwarderIpv6Addrs: NotRequired[Sequence[str]]
    SelectiveAuth: NotRequired[SelectiveAuthType]

class DeleteADAssessmentRequestTypeDef(TypedDict):
    AssessmentId: str

class DeleteConditionalForwarderRequestTypeDef(TypedDict):
    DirectoryId: str
    RemoteDomainName: str

class DeleteDirectoryRequestTypeDef(TypedDict):
    DirectoryId: str

class DeleteLogSubscriptionRequestTypeDef(TypedDict):
    DirectoryId: str

class DeleteSnapshotRequestTypeDef(TypedDict):
    SnapshotId: str

class DeleteTrustRequestTypeDef(TypedDict):
    TrustId: str
    DeleteAssociatedConditionalForwarder: NotRequired[bool]

class DeregisterCertificateRequestTypeDef(TypedDict):
    DirectoryId: str
    CertificateId: str

class DeregisterEventTopicRequestTypeDef(TypedDict):
    DirectoryId: str
    TopicName: str

class DescribeADAssessmentRequestTypeDef(TypedDict):
    AssessmentId: str

class DescribeCAEnrollmentPolicyRequestTypeDef(TypedDict):
    DirectoryId: str

class DescribeCertificateRequestTypeDef(TypedDict):
    DirectoryId: str
    CertificateId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

DescribeClientAuthenticationSettingsRequestTypeDef = TypedDict(
    "DescribeClientAuthenticationSettingsRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": NotRequired[ClientAuthenticationTypeType],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

class DescribeConditionalForwardersRequestTypeDef(TypedDict):
    DirectoryId: str
    RemoteDomainNames: NotRequired[Sequence[str]]

class DescribeDirectoriesRequestTypeDef(TypedDict):
    DirectoryIds: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]

class DescribeDirectoryDataAccessRequestTypeDef(TypedDict):
    DirectoryId: str

class DescribeDomainControllersRequestTypeDef(TypedDict):
    DirectoryId: str
    DomainControllerIds: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]

class DomainControllerTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    DomainControllerId: NotRequired[str]
    DnsIpAddr: NotRequired[str]
    DnsIpv6Addr: NotRequired[str]
    VpcId: NotRequired[str]
    SubnetId: NotRequired[str]
    AvailabilityZone: NotRequired[str]
    Status: NotRequired[DomainControllerStatusType]
    StatusReason: NotRequired[str]
    LaunchTime: NotRequired[datetime]
    StatusLastUpdatedDateTime: NotRequired[datetime]

class DescribeEventTopicsRequestTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    TopicNames: NotRequired[Sequence[str]]

class EventTopicTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    TopicName: NotRequired[str]
    TopicArn: NotRequired[str]
    CreatedDateTime: NotRequired[datetime]
    Status: NotRequired[TopicStatusType]

class DescribeHybridADUpdateRequestTypeDef(TypedDict):
    DirectoryId: str
    UpdateType: NotRequired[HybridUpdateTypeType]
    NextToken: NotRequired[str]

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

DescribeLDAPSSettingsRequestTypeDef = TypedDict(
    "DescribeLDAPSSettingsRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": NotRequired[Literal["Client"]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

class LDAPSSettingInfoTypeDef(TypedDict):
    LDAPSStatus: NotRequired[LDAPSStatusType]
    LDAPSStatusReason: NotRequired[str]
    LastUpdatedDateTime: NotRequired[datetime]

DescribeRegionsRequestTypeDef = TypedDict(
    "DescribeRegionsRequestTypeDef",
    {
        "DirectoryId": str,
        "RegionName": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

class DescribeSettingsRequestTypeDef(TypedDict):
    DirectoryId: str
    Status: NotRequired[DirectoryConfigurationStatusType]
    NextToken: NotRequired[str]

SettingEntryTypeDef = TypedDict(
    "SettingEntryTypeDef",
    {
        "Type": NotRequired[str],
        "Name": NotRequired[str],
        "AllowedValues": NotRequired[str],
        "AppliedValue": NotRequired[str],
        "RequestedValue": NotRequired[str],
        "RequestStatus": NotRequired[DirectoryConfigurationStatusType],
        "RequestDetailedStatus": NotRequired[Dict[str, DirectoryConfigurationStatusType]],
        "RequestStatusMessage": NotRequired[str],
        "LastUpdatedDateTime": NotRequired[datetime],
        "LastRequestedDateTime": NotRequired[datetime],
        "DataType": NotRequired[str],
    },
)

class DescribeSharedDirectoriesRequestTypeDef(TypedDict):
    OwnerDirectoryId: str
    SharedDirectoryIds: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]

class DescribeSnapshotsRequestTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    SnapshotIds: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "Type": NotRequired[SnapshotTypeType],
        "Name": NotRequired[str],
        "Status": NotRequired[SnapshotStatusType],
        "StartTime": NotRequired[datetime],
    },
)

class DescribeTrustsRequestTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    TrustIds: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]

class TrustTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    TrustId: NotRequired[str]
    RemoteDomainName: NotRequired[str]
    TrustType: NotRequired[TrustTypeType]
    TrustDirection: NotRequired[TrustDirectionType]
    TrustState: NotRequired[TrustStateType]
    CreatedDateTime: NotRequired[datetime]
    LastUpdatedDateTime: NotRequired[datetime]
    StateLastUpdatedDateTime: NotRequired[datetime]
    TrustStateReason: NotRequired[str]
    SelectiveAuth: NotRequired[SelectiveAuthType]

DescribeUpdateDirectoryRequestTypeDef = TypedDict(
    "DescribeUpdateDirectoryRequestTypeDef",
    {
        "DirectoryId": str,
        "UpdateType": UpdateTypeType,
        "RegionName": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

class DirectoryConnectSettingsDescriptionTypeDef(TypedDict):
    VpcId: NotRequired[str]
    SubnetIds: NotRequired[List[str]]
    CustomerUserName: NotRequired[str]
    SecurityGroupId: NotRequired[str]
    AvailabilityZones: NotRequired[List[str]]
    ConnectIps: NotRequired[List[str]]
    ConnectIpsV6: NotRequired[List[str]]

class DirectoryVpcSettingsDescriptionTypeDef(TypedDict):
    VpcId: NotRequired[str]
    SubnetIds: NotRequired[List[str]]
    SecurityGroupId: NotRequired[str]
    AvailabilityZones: NotRequired[List[str]]

class HybridSettingsDescriptionTypeDef(TypedDict):
    SelfManagedDnsIpAddrs: NotRequired[List[str]]
    SelfManagedInstanceIds: NotRequired[List[str]]

class RadiusSettingsOutputTypeDef(TypedDict):
    RadiusServers: NotRequired[List[str]]
    RadiusServersIpv6: NotRequired[List[str]]
    RadiusPort: NotRequired[int]
    RadiusTimeout: NotRequired[int]
    RadiusRetries: NotRequired[int]
    SharedSecret: NotRequired[str]
    AuthenticationProtocol: NotRequired[RadiusAuthenticationProtocolType]
    DisplayLabel: NotRequired[str]
    UseSameUsername: NotRequired[bool]

class RegionsInfoTypeDef(TypedDict):
    PrimaryRegion: NotRequired[str]
    AdditionalRegions: NotRequired[List[str]]

class DirectoryLimitsTypeDef(TypedDict):
    CloudOnlyDirectoriesLimit: NotRequired[int]
    CloudOnlyDirectoriesCurrentCount: NotRequired[int]
    CloudOnlyDirectoriesLimitReached: NotRequired[bool]
    CloudOnlyMicrosoftADLimit: NotRequired[int]
    CloudOnlyMicrosoftADCurrentCount: NotRequired[int]
    CloudOnlyMicrosoftADLimitReached: NotRequired[bool]
    ConnectedDirectoriesLimit: NotRequired[int]
    ConnectedDirectoriesCurrentCount: NotRequired[int]
    ConnectedDirectoriesLimitReached: NotRequired[bool]

class DirectorySizeUpdateSettingsTypeDef(TypedDict):
    DirectorySize: NotRequired[DirectorySizeType]

class DirectoryVpcSettingsOutputTypeDef(TypedDict):
    VpcId: str
    SubnetIds: List[str]

class DirectoryVpcSettingsTypeDef(TypedDict):
    VpcId: str
    SubnetIds: Sequence[str]

class DisableCAEnrollmentPolicyRequestTypeDef(TypedDict):
    DirectoryId: str

DisableClientAuthenticationRequestTypeDef = TypedDict(
    "DisableClientAuthenticationRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": ClientAuthenticationTypeType,
    },
)

class DisableDirectoryDataAccessRequestTypeDef(TypedDict):
    DirectoryId: str

DisableLDAPSRequestTypeDef = TypedDict(
    "DisableLDAPSRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": Literal["Client"],
    },
)

class DisableRadiusRequestTypeDef(TypedDict):
    DirectoryId: str

class DisableSsoRequestTypeDef(TypedDict):
    DirectoryId: str
    UserName: NotRequired[str]
    Password: NotRequired[str]

class EnableCAEnrollmentPolicyRequestTypeDef(TypedDict):
    DirectoryId: str
    PcaConnectorArn: str

EnableClientAuthenticationRequestTypeDef = TypedDict(
    "EnableClientAuthenticationRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": ClientAuthenticationTypeType,
    },
)

class EnableDirectoryDataAccessRequestTypeDef(TypedDict):
    DirectoryId: str

EnableLDAPSRequestTypeDef = TypedDict(
    "EnableLDAPSRequestTypeDef",
    {
        "DirectoryId": str,
        "Type": Literal["Client"],
    },
)

class EnableSsoRequestTypeDef(TypedDict):
    DirectoryId: str
    UserName: NotRequired[str]
    Password: NotRequired[str]

class GetSnapshotLimitsRequestTypeDef(TypedDict):
    DirectoryId: str

class SnapshotLimitsTypeDef(TypedDict):
    ManualSnapshotsLimit: NotRequired[int]
    ManualSnapshotsCurrentCount: NotRequired[int]
    ManualSnapshotsLimitReached: NotRequired[bool]

class HybridAdministratorAccountUpdateTypeDef(TypedDict):
    SecretArn: str

class HybridCustomerInstancesSettingsTypeDef(TypedDict):
    CustomerDnsIps: Sequence[str]
    InstanceIds: Sequence[str]

class HybridUpdateValueTypeDef(TypedDict):
    InstanceIds: NotRequired[List[str]]
    DnsIps: NotRequired[List[str]]

class IpRouteInfoTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    CidrIp: NotRequired[str]
    CidrIpv6: NotRequired[str]
    IpRouteStatusMsg: NotRequired[IpRouteStatusMsgType]
    AddedDateTime: NotRequired[datetime]
    IpRouteStatusReason: NotRequired[str]
    Description: NotRequired[str]

class ListADAssessmentsRequestTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]

class ListCertificatesRequestTypeDef(TypedDict):
    DirectoryId: str
    NextToken: NotRequired[str]
    Limit: NotRequired[int]

class ListIpRoutesRequestTypeDef(TypedDict):
    DirectoryId: str
    NextToken: NotRequired[str]
    Limit: NotRequired[int]

class ListLogSubscriptionsRequestTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]

class LogSubscriptionTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    LogGroupName: NotRequired[str]
    SubscriptionCreatedDateTime: NotRequired[datetime]

class ListSchemaExtensionsRequestTypeDef(TypedDict):
    DirectoryId: str
    NextToken: NotRequired[str]
    Limit: NotRequired[int]

class SchemaExtensionInfoTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    SchemaExtensionId: NotRequired[str]
    Description: NotRequired[str]
    SchemaExtensionStatus: NotRequired[SchemaExtensionStatusType]
    SchemaExtensionStatusReason: NotRequired[str]
    StartDateTime: NotRequired[datetime]
    EndDateTime: NotRequired[datetime]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceId: str
    NextToken: NotRequired[str]
    Limit: NotRequired[int]

class NetworkUpdateSettingsTypeDef(TypedDict):
    NetworkType: NotRequired[NetworkTypeType]
    CustomerDnsIpsV6: NotRequired[Sequence[str]]

class OSUpdateSettingsTypeDef(TypedDict):
    OSVersion: NotRequired[OSVersionType]

class RadiusSettingsTypeDef(TypedDict):
    RadiusServers: NotRequired[Sequence[str]]
    RadiusServersIpv6: NotRequired[Sequence[str]]
    RadiusPort: NotRequired[int]
    RadiusTimeout: NotRequired[int]
    RadiusRetries: NotRequired[int]
    SharedSecret: NotRequired[str]
    AuthenticationProtocol: NotRequired[RadiusAuthenticationProtocolType]
    DisplayLabel: NotRequired[str]
    UseSameUsername: NotRequired[bool]

class RegisterEventTopicRequestTypeDef(TypedDict):
    DirectoryId: str
    TopicName: str

class RejectSharedDirectoryRequestTypeDef(TypedDict):
    SharedDirectoryId: str

class RemoveIpRoutesRequestTypeDef(TypedDict):
    DirectoryId: str
    CidrIps: NotRequired[Sequence[str]]
    CidrIpv6s: NotRequired[Sequence[str]]

class RemoveRegionRequestTypeDef(TypedDict):
    DirectoryId: str

class RemoveTagsFromResourceRequestTypeDef(TypedDict):
    ResourceId: str
    TagKeys: Sequence[str]

class ResetUserPasswordRequestTypeDef(TypedDict):
    DirectoryId: str
    UserName: str
    NewPassword: str

class RestoreFromSnapshotRequestTypeDef(TypedDict):
    SnapshotId: str

class SettingTypeDef(TypedDict):
    Name: str
    Value: str

ShareTargetTypeDef = TypedDict(
    "ShareTargetTypeDef",
    {
        "Id": str,
        "Type": Literal["ACCOUNT"],
    },
)

class StartSchemaExtensionRequestTypeDef(TypedDict):
    DirectoryId: str
    CreateSnapshotBeforeSchemaExtension: bool
    LdifContent: str
    Description: str

UnshareTargetTypeDef = TypedDict(
    "UnshareTargetTypeDef",
    {
        "Id": str,
        "Type": Literal["ACCOUNT"],
    },
)

class UpdateConditionalForwarderRequestTypeDef(TypedDict):
    DirectoryId: str
    RemoteDomainName: str
    DnsIpAddrs: NotRequired[Sequence[str]]
    DnsIpv6Addrs: NotRequired[Sequence[str]]

class UpdateNumberOfDomainControllersRequestTypeDef(TypedDict):
    DirectoryId: str
    DesiredNumber: int

class UpdateTrustRequestTypeDef(TypedDict):
    TrustId: str
    SelectiveAuth: NotRequired[SelectiveAuthType]

class VerifyTrustRequestTypeDef(TypedDict):
    TrustId: str

class ConnectDirectoryResultTypeDef(TypedDict):
    DirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAliasResultTypeDef(TypedDict):
    DirectoryId: str
    Alias: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDirectoryResultTypeDef(TypedDict):
    DirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHybridADResultTypeDef(TypedDict):
    DirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMicrosoftADResultTypeDef(TypedDict):
    DirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSnapshotResultTypeDef(TypedDict):
    SnapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrustResultTypeDef(TypedDict):
    TrustId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteADAssessmentResultTypeDef(TypedDict):
    AssessmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDirectoryResultTypeDef(TypedDict):
    DirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSnapshotResultTypeDef(TypedDict):
    SnapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTrustResultTypeDef(TypedDict):
    TrustId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCAEnrollmentPolicyResultTypeDef(TypedDict):
    DirectoryId: str
    PcaConnectorArn: str
    CaEnrollmentPolicyStatus: CaEnrollmentPolicyStatusType
    LastUpdatedDateTime: datetime
    CaEnrollmentPolicyStatusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDirectoryDataAccessResultTypeDef(TypedDict):
    DataAccessStatus: DataAccessStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterCertificateResultTypeDef(TypedDict):
    CertificateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RejectSharedDirectoryResultTypeDef(TypedDict):
    SharedDirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ShareDirectoryResultTypeDef(TypedDict):
    SharedDirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartADAssessmentResultTypeDef(TypedDict):
    AssessmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSchemaExtensionResultTypeDef(TypedDict):
    SchemaExtensionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UnshareDirectoryResultTypeDef(TypedDict):
    SharedDirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateHybridADResultTypeDef(TypedDict):
    DirectoryId: str
    AssessmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSettingsResultTypeDef(TypedDict):
    DirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrustResultTypeDef(TypedDict):
    RequestId: str
    TrustId: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyTrustResultTypeDef(TypedDict):
    TrustId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptSharedDirectoryResultTypeDef(TypedDict):
    SharedDirectory: SharedDirectoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSharedDirectoriesResultTypeDef(TypedDict):
    SharedDirectories: List[SharedDirectoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AddIpRoutesRequestTypeDef(TypedDict):
    DirectoryId: str
    IpRoutes: Sequence[IpRouteTypeDef]
    UpdateSecurityGroupForDirectoryControllers: NotRequired[bool]

class AddTagsToResourceRequestTypeDef(TypedDict):
    ResourceId: str
    Tags: Sequence[TagTypeDef]

class CreateHybridADRequestTypeDef(TypedDict):
    SecretArn: str
    AssessmentId: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class ListTagsForResourceResultTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AssessmentReportTypeDef(TypedDict):
    DomainControllerIp: NotRequired[str]
    Validations: NotRequired[List[AssessmentValidationTypeDef]]

class ListADAssessmentsResultTypeDef(TypedDict):
    Assessments: List[AssessmentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ComputerTypeDef(TypedDict):
    ComputerId: NotRequired[str]
    ComputerName: NotRequired[str]
    ComputerAttributes: NotRequired[List[AttributeTypeDef]]

class CreateComputerRequestTypeDef(TypedDict):
    DirectoryId: str
    ComputerName: str
    Password: str
    OrganizationalUnitDistinguishedName: NotRequired[str]
    ComputerAttributes: NotRequired[Sequence[AttributeTypeDef]]

class ListCertificatesResultTypeDef(TypedDict):
    CertificatesInfo: List[CertificateInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateId": NotRequired[str],
        "State": NotRequired[CertificateStateType],
        "StateReason": NotRequired[str],
        "CommonName": NotRequired[str],
        "RegisteredDateTime": NotRequired[datetime],
        "ExpiryDateTime": NotRequired[datetime],
        "Type": NotRequired[CertificateTypeType],
        "ClientCertAuthSettings": NotRequired[ClientCertAuthSettingsTypeDef],
    },
)
RegisterCertificateRequestTypeDef = TypedDict(
    "RegisterCertificateRequestTypeDef",
    {
        "DirectoryId": str,
        "CertificateData": str,
        "Type": NotRequired[CertificateTypeType],
        "ClientCertAuthSettings": NotRequired[ClientCertAuthSettingsTypeDef],
    },
)

class DescribeClientAuthenticationSettingsResultTypeDef(TypedDict):
    ClientAuthenticationSettingsInfo: List[ClientAuthenticationSettingInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeConditionalForwardersResultTypeDef(TypedDict):
    ConditionalForwarders: List[ConditionalForwarderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectDirectoryRequestTypeDef(TypedDict):
    Name: str
    Password: str
    Size: DirectorySizeType
    ConnectSettings: DirectoryConnectSettingsTypeDef
    ShortName: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    NetworkType: NotRequired[NetworkTypeType]

DescribeClientAuthenticationSettingsRequestPaginateTypeDef = TypedDict(
    "DescribeClientAuthenticationSettingsRequestPaginateTypeDef",
    {
        "DirectoryId": str,
        "Type": NotRequired[ClientAuthenticationTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class DescribeDirectoriesRequestPaginateTypeDef(TypedDict):
    DirectoryIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDomainControllersRequestPaginateTypeDef(TypedDict):
    DirectoryId: str
    DomainControllerIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

DescribeLDAPSSettingsRequestPaginateTypeDef = TypedDict(
    "DescribeLDAPSSettingsRequestPaginateTypeDef",
    {
        "DirectoryId": str,
        "Type": NotRequired[Literal["Client"]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeRegionsRequestPaginateTypeDef = TypedDict(
    "DescribeRegionsRequestPaginateTypeDef",
    {
        "DirectoryId": str,
        "RegionName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class DescribeSharedDirectoriesRequestPaginateTypeDef(TypedDict):
    OwnerDirectoryId: str
    SharedDirectoryIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeSnapshotsRequestPaginateTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    SnapshotIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeTrustsRequestPaginateTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    TrustIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

DescribeUpdateDirectoryRequestPaginateTypeDef = TypedDict(
    "DescribeUpdateDirectoryRequestPaginateTypeDef",
    {
        "DirectoryId": str,
        "UpdateType": UpdateTypeType,
        "RegionName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListADAssessmentsRequestPaginateTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCertificatesRequestPaginateTypeDef(TypedDict):
    DirectoryId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIpRoutesRequestPaginateTypeDef(TypedDict):
    DirectoryId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLogSubscriptionsRequestPaginateTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSchemaExtensionsRequestPaginateTypeDef(TypedDict):
    DirectoryId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceRequestPaginateTypeDef(TypedDict):
    ResourceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDomainControllersResultTypeDef(TypedDict):
    DomainControllers: List[DomainControllerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeEventTopicsResultTypeDef(TypedDict):
    EventTopics: List[EventTopicTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeHybridADUpdateRequestWaitTypeDef(TypedDict):
    DirectoryId: str
    UpdateType: NotRequired[HybridUpdateTypeType]
    NextToken: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeLDAPSSettingsResultTypeDef(TypedDict):
    LDAPSSettingsInfo: List[LDAPSSettingInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeSettingsResultTypeDef(TypedDict):
    DirectoryId: str
    SettingEntries: List[SettingEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeSnapshotsResultTypeDef(TypedDict):
    Snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeTrustsResultTypeDef(TypedDict):
    Trusts: List[TrustTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class OwnerDirectoryDescriptionTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    AccountId: NotRequired[str]
    DnsIpAddrs: NotRequired[List[str]]
    DnsIpv6Addrs: NotRequired[List[str]]
    VpcSettings: NotRequired[DirectoryVpcSettingsDescriptionTypeDef]
    RadiusSettings: NotRequired[RadiusSettingsOutputTypeDef]
    RadiusStatus: NotRequired[RadiusStatusType]
    NetworkType: NotRequired[NetworkTypeType]

class GetDirectoryLimitsResultTypeDef(TypedDict):
    DirectoryLimits: DirectoryLimitsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

RegionDescriptionTypeDef = TypedDict(
    "RegionDescriptionTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "RegionName": NotRequired[str],
        "RegionType": NotRequired[RegionTypeType],
        "Status": NotRequired[DirectoryStageType],
        "VpcSettings": NotRequired[DirectoryVpcSettingsOutputTypeDef],
        "DesiredNumberOfDomainControllers": NotRequired[int],
        "LaunchTime": NotRequired[datetime],
        "StatusLastUpdatedDateTime": NotRequired[datetime],
        "LastUpdatedDateTime": NotRequired[datetime],
    },
)
DirectoryVpcSettingsUnionTypeDef = Union[
    DirectoryVpcSettingsTypeDef, DirectoryVpcSettingsOutputTypeDef
]

class GetSnapshotLimitsResultTypeDef(TypedDict):
    SnapshotLimits: SnapshotLimitsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateHybridADRequestTypeDef(TypedDict):
    DirectoryId: str
    HybridAdministratorAccountUpdate: NotRequired[HybridAdministratorAccountUpdateTypeDef]
    SelfManagedInstancesSettings: NotRequired[HybridCustomerInstancesSettingsTypeDef]

class HybridUpdateInfoEntryTypeDef(TypedDict):
    Status: NotRequired[UpdateStatusType]
    StatusReason: NotRequired[str]
    InitiatedBy: NotRequired[str]
    NewValue: NotRequired[HybridUpdateValueTypeDef]
    PreviousValue: NotRequired[HybridUpdateValueTypeDef]
    StartTime: NotRequired[datetime]
    LastUpdatedDateTime: NotRequired[datetime]
    AssessmentId: NotRequired[str]

class ListIpRoutesResultTypeDef(TypedDict):
    IpRoutesInfo: List[IpRouteInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListLogSubscriptionsResultTypeDef(TypedDict):
    LogSubscriptions: List[LogSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSchemaExtensionsResultTypeDef(TypedDict):
    SchemaExtensionsInfo: List[SchemaExtensionInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateDirectorySetupRequestTypeDef(TypedDict):
    DirectoryId: str
    UpdateType: UpdateTypeType
    OSUpdateSettings: NotRequired[OSUpdateSettingsTypeDef]
    DirectorySizeUpdateSettings: NotRequired[DirectorySizeUpdateSettingsTypeDef]
    NetworkUpdateSettings: NotRequired[NetworkUpdateSettingsTypeDef]
    CreateSnapshotBeforeUpdate: NotRequired[bool]

class UpdateValueTypeDef(TypedDict):
    OSUpdateSettings: NotRequired[OSUpdateSettingsTypeDef]

RadiusSettingsUnionTypeDef = Union[RadiusSettingsTypeDef, RadiusSettingsOutputTypeDef]

class UpdateSettingsRequestTypeDef(TypedDict):
    DirectoryId: str
    Settings: Sequence[SettingTypeDef]

class ShareDirectoryRequestTypeDef(TypedDict):
    DirectoryId: str
    ShareTarget: ShareTargetTypeDef
    ShareMethod: ShareMethodType
    ShareNotes: NotRequired[str]

class UnshareDirectoryRequestTypeDef(TypedDict):
    DirectoryId: str
    UnshareTarget: UnshareTargetTypeDef

class DescribeADAssessmentResultTypeDef(TypedDict):
    Assessment: AssessmentTypeDef
    AssessmentReports: List[AssessmentReportTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateComputerResultTypeDef(TypedDict):
    Computer: ComputerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCertificateResultTypeDef(TypedDict):
    Certificate: CertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

DirectoryDescriptionTypeDef = TypedDict(
    "DirectoryDescriptionTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "Name": NotRequired[str],
        "ShortName": NotRequired[str],
        "Size": NotRequired[DirectorySizeType],
        "Edition": NotRequired[DirectoryEditionType],
        "Alias": NotRequired[str],
        "AccessUrl": NotRequired[str],
        "Description": NotRequired[str],
        "DnsIpAddrs": NotRequired[List[str]],
        "DnsIpv6Addrs": NotRequired[List[str]],
        "Stage": NotRequired[DirectoryStageType],
        "ShareStatus": NotRequired[ShareStatusType],
        "ShareMethod": NotRequired[ShareMethodType],
        "ShareNotes": NotRequired[str],
        "LaunchTime": NotRequired[datetime],
        "StageLastUpdatedDateTime": NotRequired[datetime],
        "Type": NotRequired[DirectoryTypeType],
        "VpcSettings": NotRequired[DirectoryVpcSettingsDescriptionTypeDef],
        "ConnectSettings": NotRequired[DirectoryConnectSettingsDescriptionTypeDef],
        "RadiusSettings": NotRequired[RadiusSettingsOutputTypeDef],
        "RadiusStatus": NotRequired[RadiusStatusType],
        "StageReason": NotRequired[str],
        "SsoEnabled": NotRequired[bool],
        "DesiredNumberOfDomainControllers": NotRequired[int],
        "OwnerDirectoryDescription": NotRequired[OwnerDirectoryDescriptionTypeDef],
        "RegionsInfo": NotRequired[RegionsInfoTypeDef],
        "OsVersion": NotRequired[OSVersionType],
        "HybridSettings": NotRequired[HybridSettingsDescriptionTypeDef],
        "NetworkType": NotRequired[NetworkTypeType],
    },
)

class DescribeRegionsResultTypeDef(TypedDict):
    RegionsDescription: List[RegionDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

AddRegionRequestTypeDef = TypedDict(
    "AddRegionRequestTypeDef",
    {
        "DirectoryId": str,
        "RegionName": str,
        "VPCSettings": DirectoryVpcSettingsUnionTypeDef,
    },
)

class AssessmentConfigurationTypeDef(TypedDict):
    CustomerDnsIps: Sequence[str]
    DnsName: str
    VpcSettings: DirectoryVpcSettingsUnionTypeDef
    InstanceIds: Sequence[str]
    SecurityGroupIds: NotRequired[Sequence[str]]

class CreateDirectoryRequestTypeDef(TypedDict):
    Name: str
    Password: str
    Size: DirectorySizeType
    ShortName: NotRequired[str]
    Description: NotRequired[str]
    VpcSettings: NotRequired[DirectoryVpcSettingsUnionTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]
    NetworkType: NotRequired[NetworkTypeType]

class CreateMicrosoftADRequestTypeDef(TypedDict):
    Name: str
    Password: str
    VpcSettings: DirectoryVpcSettingsUnionTypeDef
    ShortName: NotRequired[str]
    Description: NotRequired[str]
    Edition: NotRequired[DirectoryEditionType]
    Tags: NotRequired[Sequence[TagTypeDef]]
    NetworkType: NotRequired[NetworkTypeType]

class HybridUpdateActivitiesTypeDef(TypedDict):
    SelfManagedInstances: NotRequired[List[HybridUpdateInfoEntryTypeDef]]
    HybridAdministratorAccount: NotRequired[List[HybridUpdateInfoEntryTypeDef]]

class UpdateInfoEntryTypeDef(TypedDict):
    Region: NotRequired[str]
    Status: NotRequired[UpdateStatusType]
    StatusReason: NotRequired[str]
    InitiatedBy: NotRequired[str]
    NewValue: NotRequired[UpdateValueTypeDef]
    PreviousValue: NotRequired[UpdateValueTypeDef]
    StartTime: NotRequired[datetime]
    LastUpdatedDateTime: NotRequired[datetime]

class EnableRadiusRequestTypeDef(TypedDict):
    DirectoryId: str
    RadiusSettings: RadiusSettingsUnionTypeDef

class UpdateRadiusRequestTypeDef(TypedDict):
    DirectoryId: str
    RadiusSettings: RadiusSettingsUnionTypeDef

class DescribeDirectoriesResultTypeDef(TypedDict):
    DirectoryDescriptions: List[DirectoryDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class StartADAssessmentRequestTypeDef(TypedDict):
    AssessmentConfiguration: NotRequired[AssessmentConfigurationTypeDef]
    DirectoryId: NotRequired[str]

class DescribeHybridADUpdateResultTypeDef(TypedDict):
    UpdateActivities: HybridUpdateActivitiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeUpdateDirectoryResultTypeDef(TypedDict):
    UpdateActivities: List[UpdateInfoEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
