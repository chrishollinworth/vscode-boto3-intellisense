"""
Type annotations for guardduty service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/type_defs.html)

Usage::

    ```python
    from mypy_boto3_guardduty.type_defs import AcceptAdministratorInvitationRequestRequestTypeDef

    data: AcceptAdministratorInvitationRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AdminStatusType,
    CriterionKeyType,
    DataSourceStatusType,
    DataSourceType,
    DetectorStatusType,
    EbsSnapshotPreservationType,
    FeedbackType,
    FilterActionType,
    FindingPublishingFrequencyType,
    IpSetFormatType,
    IpSetStatusType,
    OrderByType,
    PublishingStatusType,
    ScanResultType,
    ScanStatusType,
    ThreatIntelSetFormatType,
    ThreatIntelSetStatusType,
    UsageStatisticTypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AcceptAdministratorInvitationRequestRequestTypeDef",
    "AcceptInvitationRequestRequestTypeDef",
    "AccessControlListTypeDef",
    "AccessKeyDetailsTypeDef",
    "AccountDetailTypeDef",
    "AccountFreeTrialInfoTypeDef",
    "AccountLevelPermissionsTypeDef",
    "ActionTypeDef",
    "AdminAccountTypeDef",
    "AdministratorTypeDef",
    "ArchiveFindingsRequestRequestTypeDef",
    "AwsApiCallActionTypeDef",
    "BlockPublicAccessTypeDef",
    "BucketLevelPermissionsTypeDef",
    "BucketPolicyTypeDef",
    "CityTypeDef",
    "CloudTrailConfigurationResultTypeDef",
    "ConditionTypeDef",
    "ContainerTypeDef",
    "CountryTypeDef",
    "CreateDetectorRequestRequestTypeDef",
    "CreateDetectorResponseTypeDef",
    "CreateFilterRequestRequestTypeDef",
    "CreateFilterResponseTypeDef",
    "CreateIPSetRequestRequestTypeDef",
    "CreateIPSetResponseTypeDef",
    "CreateMembersRequestRequestTypeDef",
    "CreateMembersResponseTypeDef",
    "CreatePublishingDestinationRequestRequestTypeDef",
    "CreatePublishingDestinationResponseTypeDef",
    "CreateSampleFindingsRequestRequestTypeDef",
    "CreateThreatIntelSetRequestRequestTypeDef",
    "CreateThreatIntelSetResponseTypeDef",
    "DNSLogsConfigurationResultTypeDef",
    "DataSourceConfigurationsResultTypeDef",
    "DataSourceConfigurationsTypeDef",
    "DataSourceFreeTrialTypeDef",
    "DataSourcesFreeTrialTypeDef",
    "DeclineInvitationsRequestRequestTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DefaultServerSideEncryptionTypeDef",
    "DeleteDetectorRequestRequestTypeDef",
    "DeleteFilterRequestRequestTypeDef",
    "DeleteIPSetRequestRequestTypeDef",
    "DeleteInvitationsRequestRequestTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "DeleteMembersRequestRequestTypeDef",
    "DeleteMembersResponseTypeDef",
    "DeletePublishingDestinationRequestRequestTypeDef",
    "DeleteThreatIntelSetRequestRequestTypeDef",
    "DescribeMalwareScansRequestRequestTypeDef",
    "DescribeMalwareScansResponseTypeDef",
    "DescribeOrganizationConfigurationRequestRequestTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DescribePublishingDestinationRequestRequestTypeDef",
    "DescribePublishingDestinationResponseTypeDef",
    "DestinationPropertiesTypeDef",
    "DestinationTypeDef",
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    "DisassociateFromAdministratorAccountRequestRequestTypeDef",
    "DisassociateFromMasterAccountRequestRequestTypeDef",
    "DisassociateMembersRequestRequestTypeDef",
    "DisassociateMembersResponseTypeDef",
    "DnsRequestActionTypeDef",
    "DomainDetailsTypeDef",
    "EbsVolumeDetailsTypeDef",
    "EbsVolumeScanDetailsTypeDef",
    "EbsVolumesResultTypeDef",
    "EcsClusterDetailsTypeDef",
    "EcsTaskDetailsTypeDef",
    "EksClusterDetailsTypeDef",
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    "EvidenceTypeDef",
    "FilterConditionTypeDef",
    "FilterCriteriaTypeDef",
    "FilterCriterionTypeDef",
    "FindingCriteriaTypeDef",
    "FindingStatisticsTypeDef",
    "FindingTypeDef",
    "FlowLogsConfigurationResultTypeDef",
    "GeoLocationTypeDef",
    "GetAdministratorAccountRequestRequestTypeDef",
    "GetAdministratorAccountResponseTypeDef",
    "GetDetectorRequestRequestTypeDef",
    "GetDetectorResponseTypeDef",
    "GetFilterRequestRequestTypeDef",
    "GetFilterResponseTypeDef",
    "GetFindingsRequestRequestTypeDef",
    "GetFindingsResponseTypeDef",
    "GetFindingsStatisticsRequestRequestTypeDef",
    "GetFindingsStatisticsResponseTypeDef",
    "GetIPSetRequestRequestTypeDef",
    "GetIPSetResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "GetMalwareScanSettingsRequestRequestTypeDef",
    "GetMalwareScanSettingsResponseTypeDef",
    "GetMasterAccountRequestRequestTypeDef",
    "GetMasterAccountResponseTypeDef",
    "GetMemberDetectorsRequestRequestTypeDef",
    "GetMemberDetectorsResponseTypeDef",
    "GetMembersRequestRequestTypeDef",
    "GetMembersResponseTypeDef",
    "GetRemainingFreeTrialDaysRequestRequestTypeDef",
    "GetRemainingFreeTrialDaysResponseTypeDef",
    "GetThreatIntelSetRequestRequestTypeDef",
    "GetThreatIntelSetResponseTypeDef",
    "GetUsageStatisticsRequestRequestTypeDef",
    "GetUsageStatisticsResponseTypeDef",
    "HighestSeverityThreatDetailsTypeDef",
    "HostPathTypeDef",
    "IamInstanceProfileTypeDef",
    "InstanceDetailsTypeDef",
    "InvitationTypeDef",
    "InviteMembersRequestRequestTypeDef",
    "InviteMembersResponseTypeDef",
    "KubernetesApiCallActionTypeDef",
    "KubernetesAuditLogsConfigurationResultTypeDef",
    "KubernetesAuditLogsConfigurationTypeDef",
    "KubernetesConfigurationResultTypeDef",
    "KubernetesConfigurationTypeDef",
    "KubernetesDataSourceFreeTrialTypeDef",
    "KubernetesDetailsTypeDef",
    "KubernetesUserDetailsTypeDef",
    "KubernetesWorkloadDetailsTypeDef",
    "ListDetectorsRequestRequestTypeDef",
    "ListDetectorsResponseTypeDef",
    "ListFiltersRequestRequestTypeDef",
    "ListFiltersResponseTypeDef",
    "ListFindingsRequestRequestTypeDef",
    "ListFindingsResponseTypeDef",
    "ListIPSetsRequestRequestTypeDef",
    "ListIPSetsResponseTypeDef",
    "ListInvitationsRequestRequestTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListMembersRequestRequestTypeDef",
    "ListMembersResponseTypeDef",
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListPublishingDestinationsRequestRequestTypeDef",
    "ListPublishingDestinationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListThreatIntelSetsRequestRequestTypeDef",
    "ListThreatIntelSetsResponseTypeDef",
    "LocalIpDetailsTypeDef",
    "LocalPortDetailsTypeDef",
    "MalwareProtectionConfigurationResultTypeDef",
    "MalwareProtectionConfigurationTypeDef",
    "MalwareProtectionDataSourceFreeTrialTypeDef",
    "MasterTypeDef",
    "MemberDataSourceConfigurationTypeDef",
    "MemberTypeDef",
    "NetworkConnectionActionTypeDef",
    "NetworkInterfaceTypeDef",
    "OrganizationDataSourceConfigurationsResultTypeDef",
    "OrganizationDataSourceConfigurationsTypeDef",
    "OrganizationEbsVolumesResultTypeDef",
    "OrganizationEbsVolumesTypeDef",
    "OrganizationKubernetesAuditLogsConfigurationResultTypeDef",
    "OrganizationKubernetesAuditLogsConfigurationTypeDef",
    "OrganizationKubernetesConfigurationResultTypeDef",
    "OrganizationKubernetesConfigurationTypeDef",
    "OrganizationMalwareProtectionConfigurationResultTypeDef",
    "OrganizationMalwareProtectionConfigurationTypeDef",
    "OrganizationS3LogsConfigurationResultTypeDef",
    "OrganizationS3LogsConfigurationTypeDef",
    "OrganizationScanEc2InstanceWithFindingsResultTypeDef",
    "OrganizationScanEc2InstanceWithFindingsTypeDef",
    "OrganizationTypeDef",
    "OwnerTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionConfigurationTypeDef",
    "PortProbeActionTypeDef",
    "PortProbeDetailTypeDef",
    "PrivateIpAddressDetailsTypeDef",
    "ProductCodeTypeDef",
    "PublicAccessTypeDef",
    "RemoteAccountDetailsTypeDef",
    "RemoteIpDetailsTypeDef",
    "RemotePortDetailsTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "S3BucketDetailTypeDef",
    "S3LogsConfigurationResultTypeDef",
    "S3LogsConfigurationTypeDef",
    "ScanConditionPairTypeDef",
    "ScanConditionTypeDef",
    "ScanDetectionsTypeDef",
    "ScanEc2InstanceWithFindingsResultTypeDef",
    "ScanEc2InstanceWithFindingsTypeDef",
    "ScanFilePathTypeDef",
    "ScanResourceCriteriaTypeDef",
    "ScanResultDetailsTypeDef",
    "ScanThreatNameTypeDef",
    "ScanTypeDef",
    "ScannedItemCountTypeDef",
    "SecurityContextTypeDef",
    "SecurityGroupTypeDef",
    "ServiceAdditionalInfoTypeDef",
    "ServiceTypeDef",
    "SortCriteriaTypeDef",
    "StartMonitoringMembersRequestRequestTypeDef",
    "StartMonitoringMembersResponseTypeDef",
    "StopMonitoringMembersRequestRequestTypeDef",
    "StopMonitoringMembersResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "ThreatDetectedByNameTypeDef",
    "ThreatIntelligenceDetailTypeDef",
    "ThreatsDetectedItemCountTypeDef",
    "TotalTypeDef",
    "TriggerDetailsTypeDef",
    "UnarchiveFindingsRequestRequestTypeDef",
    "UnprocessedAccountTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDetectorRequestRequestTypeDef",
    "UpdateFilterRequestRequestTypeDef",
    "UpdateFilterResponseTypeDef",
    "UpdateFindingsFeedbackRequestRequestTypeDef",
    "UpdateIPSetRequestRequestTypeDef",
    "UpdateMalwareScanSettingsRequestRequestTypeDef",
    "UpdateMemberDetectorsRequestRequestTypeDef",
    "UpdateMemberDetectorsResponseTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    "UpdatePublishingDestinationRequestRequestTypeDef",
    "UpdateThreatIntelSetRequestRequestTypeDef",
    "UsageAccountResultTypeDef",
    "UsageCriteriaTypeDef",
    "UsageDataSourceResultTypeDef",
    "UsageResourceResultTypeDef",
    "UsageStatisticsTypeDef",
    "VolumeDetailTypeDef",
    "VolumeMountTypeDef",
    "VolumeTypeDef",
)

AcceptAdministratorInvitationRequestRequestTypeDef = TypedDict(
    "AcceptAdministratorInvitationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AdministratorId": str,
        "InvitationId": str,
    },
)

AcceptInvitationRequestRequestTypeDef = TypedDict(
    "AcceptInvitationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "MasterId": str,
        "InvitationId": str,
    },
)

AccessControlListTypeDef = TypedDict(
    "AccessControlListTypeDef",
    {
        "AllowsPublicReadAccess": bool,
        "AllowsPublicWriteAccess": bool,
    },
    total=False,
)

AccessKeyDetailsTypeDef = TypedDict(
    "AccessKeyDetailsTypeDef",
    {
        "AccessKeyId": str,
        "PrincipalId": str,
        "UserName": str,
        "UserType": str,
    },
    total=False,
)

AccountDetailTypeDef = TypedDict(
    "AccountDetailTypeDef",
    {
        "AccountId": str,
        "Email": str,
    },
)

AccountFreeTrialInfoTypeDef = TypedDict(
    "AccountFreeTrialInfoTypeDef",
    {
        "AccountId": str,
        "DataSources": "DataSourcesFreeTrialTypeDef",
    },
    total=False,
)

AccountLevelPermissionsTypeDef = TypedDict(
    "AccountLevelPermissionsTypeDef",
    {
        "BlockPublicAccess": "BlockPublicAccessTypeDef",
    },
    total=False,
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ActionType": str,
        "AwsApiCallAction": "AwsApiCallActionTypeDef",
        "DnsRequestAction": "DnsRequestActionTypeDef",
        "NetworkConnectionAction": "NetworkConnectionActionTypeDef",
        "PortProbeAction": "PortProbeActionTypeDef",
        "KubernetesApiCallAction": "KubernetesApiCallActionTypeDef",
    },
    total=False,
)

AdminAccountTypeDef = TypedDict(
    "AdminAccountTypeDef",
    {
        "AdminAccountId": str,
        "AdminStatus": AdminStatusType,
    },
    total=False,
)

AdministratorTypeDef = TypedDict(
    "AdministratorTypeDef",
    {
        "AccountId": str,
        "InvitationId": str,
        "RelationshipStatus": str,
        "InvitedAt": str,
    },
    total=False,
)

ArchiveFindingsRequestRequestTypeDef = TypedDict(
    "ArchiveFindingsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FindingIds": List[str],
    },
)

AwsApiCallActionTypeDef = TypedDict(
    "AwsApiCallActionTypeDef",
    {
        "Api": str,
        "CallerType": str,
        "DomainDetails": "DomainDetailsTypeDef",
        "ErrorCode": str,
        "UserAgent": str,
        "RemoteIpDetails": "RemoteIpDetailsTypeDef",
        "ServiceName": str,
        "RemoteAccountDetails": "RemoteAccountDetailsTypeDef",
        "AffectedResources": Dict[str, str],
    },
    total=False,
)

BlockPublicAccessTypeDef = TypedDict(
    "BlockPublicAccessTypeDef",
    {
        "IgnorePublicAcls": bool,
        "RestrictPublicBuckets": bool,
        "BlockPublicAcls": bool,
        "BlockPublicPolicy": bool,
    },
    total=False,
)

BucketLevelPermissionsTypeDef = TypedDict(
    "BucketLevelPermissionsTypeDef",
    {
        "AccessControlList": "AccessControlListTypeDef",
        "BucketPolicy": "BucketPolicyTypeDef",
        "BlockPublicAccess": "BlockPublicAccessTypeDef",
    },
    total=False,
)

BucketPolicyTypeDef = TypedDict(
    "BucketPolicyTypeDef",
    {
        "AllowsPublicReadAccess": bool,
        "AllowsPublicWriteAccess": bool,
    },
    total=False,
)

CityTypeDef = TypedDict(
    "CityTypeDef",
    {
        "CityName": str,
    },
    total=False,
)

CloudTrailConfigurationResultTypeDef = TypedDict(
    "CloudTrailConfigurationResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "ContainerRuntime": str,
        "Id": str,
        "Name": str,
        "Image": str,
        "ImagePrefix": str,
        "VolumeMounts": List["VolumeMountTypeDef"],
        "SecurityContext": "SecurityContextTypeDef",
    },
    total=False,
)

CountryTypeDef = TypedDict(
    "CountryTypeDef",
    {
        "CountryCode": str,
        "CountryName": str,
    },
    total=False,
)

_RequiredCreateDetectorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDetectorRequestRequestTypeDef",
    {
        "Enable": bool,
    },
)
_OptionalCreateDetectorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDetectorRequestRequestTypeDef",
    {
        "ClientToken": str,
        "FindingPublishingFrequency": FindingPublishingFrequencyType,
        "DataSources": "DataSourceConfigurationsTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateDetectorRequestRequestTypeDef(
    _RequiredCreateDetectorRequestRequestTypeDef, _OptionalCreateDetectorRequestRequestTypeDef
):
    pass

CreateDetectorResponseTypeDef = TypedDict(
    "CreateDetectorResponseTypeDef",
    {
        "DetectorId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFilterRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFilterRequestRequestTypeDef",
    {
        "DetectorId": str,
        "Name": str,
        "FindingCriteria": "FindingCriteriaTypeDef",
    },
)
_OptionalCreateFilterRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFilterRequestRequestTypeDef",
    {
        "Description": str,
        "Action": FilterActionType,
        "Rank": int,
        "ClientToken": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateFilterRequestRequestTypeDef(
    _RequiredCreateFilterRequestRequestTypeDef, _OptionalCreateFilterRequestRequestTypeDef
):
    pass

CreateFilterResponseTypeDef = TypedDict(
    "CreateFilterResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIPSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIPSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "Name": str,
        "Format": IpSetFormatType,
        "Location": str,
        "Activate": bool,
    },
)
_OptionalCreateIPSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIPSetRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateIPSetRequestRequestTypeDef(
    _RequiredCreateIPSetRequestRequestTypeDef, _OptionalCreateIPSetRequestRequestTypeDef
):
    pass

CreateIPSetResponseTypeDef = TypedDict(
    "CreateIPSetResponseTypeDef",
    {
        "IpSetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMembersRequestRequestTypeDef = TypedDict(
    "CreateMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountDetails": List["AccountDetailTypeDef"],
    },
)

CreateMembersResponseTypeDef = TypedDict(
    "CreateMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePublishingDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePublishingDestinationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "DestinationType": Literal["S3"],
        "DestinationProperties": "DestinationPropertiesTypeDef",
    },
)
_OptionalCreatePublishingDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePublishingDestinationRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class CreatePublishingDestinationRequestRequestTypeDef(
    _RequiredCreatePublishingDestinationRequestRequestTypeDef,
    _OptionalCreatePublishingDestinationRequestRequestTypeDef,
):
    pass

CreatePublishingDestinationResponseTypeDef = TypedDict(
    "CreatePublishingDestinationResponseTypeDef",
    {
        "DestinationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSampleFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSampleFindingsRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalCreateSampleFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSampleFindingsRequestRequestTypeDef",
    {
        "FindingTypes": List[str],
    },
    total=False,
)

class CreateSampleFindingsRequestRequestTypeDef(
    _RequiredCreateSampleFindingsRequestRequestTypeDef,
    _OptionalCreateSampleFindingsRequestRequestTypeDef,
):
    pass

_RequiredCreateThreatIntelSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateThreatIntelSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "Name": str,
        "Format": ThreatIntelSetFormatType,
        "Location": str,
        "Activate": bool,
    },
)
_OptionalCreateThreatIntelSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateThreatIntelSetRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateThreatIntelSetRequestRequestTypeDef(
    _RequiredCreateThreatIntelSetRequestRequestTypeDef,
    _OptionalCreateThreatIntelSetRequestRequestTypeDef,
):
    pass

CreateThreatIntelSetResponseTypeDef = TypedDict(
    "CreateThreatIntelSetResponseTypeDef",
    {
        "ThreatIntelSetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DNSLogsConfigurationResultTypeDef = TypedDict(
    "DNSLogsConfigurationResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
)

_RequiredDataSourceConfigurationsResultTypeDef = TypedDict(
    "_RequiredDataSourceConfigurationsResultTypeDef",
    {
        "CloudTrail": "CloudTrailConfigurationResultTypeDef",
        "DNSLogs": "DNSLogsConfigurationResultTypeDef",
        "FlowLogs": "FlowLogsConfigurationResultTypeDef",
        "S3Logs": "S3LogsConfigurationResultTypeDef",
    },
)
_OptionalDataSourceConfigurationsResultTypeDef = TypedDict(
    "_OptionalDataSourceConfigurationsResultTypeDef",
    {
        "Kubernetes": "KubernetesConfigurationResultTypeDef",
        "MalwareProtection": "MalwareProtectionConfigurationResultTypeDef",
    },
    total=False,
)

class DataSourceConfigurationsResultTypeDef(
    _RequiredDataSourceConfigurationsResultTypeDef, _OptionalDataSourceConfigurationsResultTypeDef
):
    pass

DataSourceConfigurationsTypeDef = TypedDict(
    "DataSourceConfigurationsTypeDef",
    {
        "S3Logs": "S3LogsConfigurationTypeDef",
        "Kubernetes": "KubernetesConfigurationTypeDef",
        "MalwareProtection": "MalwareProtectionConfigurationTypeDef",
    },
    total=False,
)

DataSourceFreeTrialTypeDef = TypedDict(
    "DataSourceFreeTrialTypeDef",
    {
        "FreeTrialDaysRemaining": int,
    },
    total=False,
)

DataSourcesFreeTrialTypeDef = TypedDict(
    "DataSourcesFreeTrialTypeDef",
    {
        "CloudTrail": "DataSourceFreeTrialTypeDef",
        "DnsLogs": "DataSourceFreeTrialTypeDef",
        "FlowLogs": "DataSourceFreeTrialTypeDef",
        "S3Logs": "DataSourceFreeTrialTypeDef",
        "Kubernetes": "KubernetesDataSourceFreeTrialTypeDef",
        "MalwareProtection": "MalwareProtectionDataSourceFreeTrialTypeDef",
    },
    total=False,
)

DeclineInvitationsRequestRequestTypeDef = TypedDict(
    "DeclineInvitationsRequestRequestTypeDef",
    {
        "AccountIds": List[str],
    },
)

DeclineInvitationsResponseTypeDef = TypedDict(
    "DeclineInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefaultServerSideEncryptionTypeDef = TypedDict(
    "DefaultServerSideEncryptionTypeDef",
    {
        "EncryptionType": str,
        "KmsMasterKeyArn": str,
    },
    total=False,
)

DeleteDetectorRequestRequestTypeDef = TypedDict(
    "DeleteDetectorRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)

DeleteFilterRequestRequestTypeDef = TypedDict(
    "DeleteFilterRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FilterName": str,
    },
)

DeleteIPSetRequestRequestTypeDef = TypedDict(
    "DeleteIPSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "IpSetId": str,
    },
)

DeleteInvitationsRequestRequestTypeDef = TypedDict(
    "DeleteInvitationsRequestRequestTypeDef",
    {
        "AccountIds": List[str],
    },
)

DeleteInvitationsResponseTypeDef = TypedDict(
    "DeleteInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMembersRequestRequestTypeDef = TypedDict(
    "DeleteMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": List[str],
    },
)

DeleteMembersResponseTypeDef = TypedDict(
    "DeleteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePublishingDestinationRequestRequestTypeDef = TypedDict(
    "DeletePublishingDestinationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "DestinationId": str,
    },
)

DeleteThreatIntelSetRequestRequestTypeDef = TypedDict(
    "DeleteThreatIntelSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "ThreatIntelSetId": str,
    },
)

_RequiredDescribeMalwareScansRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeMalwareScansRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalDescribeMalwareScansRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeMalwareScansRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "FilterCriteria": "FilterCriteriaTypeDef",
        "SortCriteria": "SortCriteriaTypeDef",
    },
    total=False,
)

class DescribeMalwareScansRequestRequestTypeDef(
    _RequiredDescribeMalwareScansRequestRequestTypeDef,
    _OptionalDescribeMalwareScansRequestRequestTypeDef,
):
    pass

DescribeMalwareScansResponseTypeDef = TypedDict(
    "DescribeMalwareScansResponseTypeDef",
    {
        "Scans": List["ScanTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConfigurationRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)

DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "AutoEnable": bool,
        "MemberAccountLimitReached": bool,
        "DataSources": "OrganizationDataSourceConfigurationsResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePublishingDestinationRequestRequestTypeDef = TypedDict(
    "DescribePublishingDestinationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "DestinationId": str,
    },
)

DescribePublishingDestinationResponseTypeDef = TypedDict(
    "DescribePublishingDestinationResponseTypeDef",
    {
        "DestinationId": str,
        "DestinationType": Literal["S3"],
        "Status": PublishingStatusType,
        "PublishingFailureStartTimestamp": int,
        "DestinationProperties": "DestinationPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationPropertiesTypeDef = TypedDict(
    "DestinationPropertiesTypeDef",
    {
        "DestinationArn": str,
        "KmsKeyArn": str,
    },
    total=False,
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "DestinationId": str,
        "DestinationType": Literal["S3"],
        "Status": PublishingStatusType,
    },
)

DisableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AdminAccountId": str,
    },
)

DisassociateFromAdministratorAccountRequestRequestTypeDef = TypedDict(
    "DisassociateFromAdministratorAccountRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)

DisassociateFromMasterAccountRequestRequestTypeDef = TypedDict(
    "DisassociateFromMasterAccountRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)

DisassociateMembersRequestRequestTypeDef = TypedDict(
    "DisassociateMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": List[str],
    },
)

DisassociateMembersResponseTypeDef = TypedDict(
    "DisassociateMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DnsRequestActionTypeDef = TypedDict(
    "DnsRequestActionTypeDef",
    {
        "Domain": str,
        "Protocol": str,
        "Blocked": bool,
    },
    total=False,
)

DomainDetailsTypeDef = TypedDict(
    "DomainDetailsTypeDef",
    {
        "Domain": str,
    },
    total=False,
)

EbsVolumeDetailsTypeDef = TypedDict(
    "EbsVolumeDetailsTypeDef",
    {
        "ScannedVolumeDetails": List["VolumeDetailTypeDef"],
        "SkippedVolumeDetails": List["VolumeDetailTypeDef"],
    },
    total=False,
)

EbsVolumeScanDetailsTypeDef = TypedDict(
    "EbsVolumeScanDetailsTypeDef",
    {
        "ScanId": str,
        "ScanStartedAt": datetime,
        "ScanCompletedAt": datetime,
        "TriggerFindingId": str,
        "Sources": List[str],
        "ScanDetections": "ScanDetectionsTypeDef",
    },
    total=False,
)

EbsVolumesResultTypeDef = TypedDict(
    "EbsVolumesResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
    total=False,
)

EcsClusterDetailsTypeDef = TypedDict(
    "EcsClusterDetailsTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Status": str,
        "ActiveServicesCount": int,
        "RegisteredContainerInstancesCount": int,
        "RunningTasksCount": int,
        "Tags": List["TagTypeDef"],
        "TaskDetails": "EcsTaskDetailsTypeDef",
    },
    total=False,
)

EcsTaskDetailsTypeDef = TypedDict(
    "EcsTaskDetailsTypeDef",
    {
        "Arn": str,
        "DefinitionArn": str,
        "Version": str,
        "TaskCreatedAt": datetime,
        "StartedAt": datetime,
        "StartedBy": str,
        "Tags": List["TagTypeDef"],
        "Volumes": List["VolumeTypeDef"],
        "Containers": List["ContainerTypeDef"],
        "Group": str,
    },
    total=False,
)

EksClusterDetailsTypeDef = TypedDict(
    "EksClusterDetailsTypeDef",
    {
        "Name": str,
        "Arn": str,
        "VpcId": str,
        "Status": str,
        "Tags": List["TagTypeDef"],
        "CreatedAt": datetime,
    },
    total=False,
)

EnableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AdminAccountId": str,
    },
)

EvidenceTypeDef = TypedDict(
    "EvidenceTypeDef",
    {
        "ThreatIntelligenceDetails": List["ThreatIntelligenceDetailTypeDef"],
    },
    total=False,
)

FilterConditionTypeDef = TypedDict(
    "FilterConditionTypeDef",
    {
        "EqualsValue": str,
        "GreaterThan": int,
        "LessThan": int,
    },
    total=False,
)

FilterCriteriaTypeDef = TypedDict(
    "FilterCriteriaTypeDef",
    {
        "FilterCriterion": List["FilterCriterionTypeDef"],
    },
    total=False,
)

FilterCriterionTypeDef = TypedDict(
    "FilterCriterionTypeDef",
    {
        "CriterionKey": CriterionKeyType,
        "FilterCondition": "FilterConditionTypeDef",
    },
    total=False,
)

FindingCriteriaTypeDef = TypedDict(
    "FindingCriteriaTypeDef",
    {
        "Criterion": Dict[str, "ConditionTypeDef"],
    },
    total=False,
)

FindingStatisticsTypeDef = TypedDict(
    "FindingStatisticsTypeDef",
    {
        "CountBySeverity": Dict[str, int],
    },
    total=False,
)

_RequiredFindingTypeDef = TypedDict(
    "_RequiredFindingTypeDef",
    {
        "AccountId": str,
        "Arn": str,
        "CreatedAt": str,
        "Id": str,
        "Region": str,
        "Resource": "ResourceTypeDef",
        "SchemaVersion": str,
        "Severity": float,
        "Type": str,
        "UpdatedAt": str,
    },
)
_OptionalFindingTypeDef = TypedDict(
    "_OptionalFindingTypeDef",
    {
        "Confidence": float,
        "Description": str,
        "Partition": str,
        "Service": "ServiceTypeDef",
        "Title": str,
    },
    total=False,
)

class FindingTypeDef(_RequiredFindingTypeDef, _OptionalFindingTypeDef):
    pass

FlowLogsConfigurationResultTypeDef = TypedDict(
    "FlowLogsConfigurationResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
)

GeoLocationTypeDef = TypedDict(
    "GeoLocationTypeDef",
    {
        "Lat": float,
        "Lon": float,
    },
    total=False,
)

GetAdministratorAccountRequestRequestTypeDef = TypedDict(
    "GetAdministratorAccountRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)

GetAdministratorAccountResponseTypeDef = TypedDict(
    "GetAdministratorAccountResponseTypeDef",
    {
        "Administrator": "AdministratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDetectorRequestRequestTypeDef = TypedDict(
    "GetDetectorRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)

GetDetectorResponseTypeDef = TypedDict(
    "GetDetectorResponseTypeDef",
    {
        "CreatedAt": str,
        "FindingPublishingFrequency": FindingPublishingFrequencyType,
        "ServiceRole": str,
        "Status": DetectorStatusType,
        "UpdatedAt": str,
        "DataSources": "DataSourceConfigurationsResultTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFilterRequestRequestTypeDef = TypedDict(
    "GetFilterRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FilterName": str,
    },
)

GetFilterResponseTypeDef = TypedDict(
    "GetFilterResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": FilterActionType,
        "Rank": int,
        "FindingCriteria": "FindingCriteriaTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredGetFindingsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FindingIds": List[str],
    },
)
_OptionalGetFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalGetFindingsRequestRequestTypeDef",
    {
        "SortCriteria": "SortCriteriaTypeDef",
    },
    total=False,
)

class GetFindingsRequestRequestTypeDef(
    _RequiredGetFindingsRequestRequestTypeDef, _OptionalGetFindingsRequestRequestTypeDef
):
    pass

GetFindingsResponseTypeDef = TypedDict(
    "GetFindingsResponseTypeDef",
    {
        "Findings": List["FindingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFindingsStatisticsRequestRequestTypeDef = TypedDict(
    "_RequiredGetFindingsStatisticsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FindingStatisticTypes": List[Literal["COUNT_BY_SEVERITY"]],
    },
)
_OptionalGetFindingsStatisticsRequestRequestTypeDef = TypedDict(
    "_OptionalGetFindingsStatisticsRequestRequestTypeDef",
    {
        "FindingCriteria": "FindingCriteriaTypeDef",
    },
    total=False,
)

class GetFindingsStatisticsRequestRequestTypeDef(
    _RequiredGetFindingsStatisticsRequestRequestTypeDef,
    _OptionalGetFindingsStatisticsRequestRequestTypeDef,
):
    pass

GetFindingsStatisticsResponseTypeDef = TypedDict(
    "GetFindingsStatisticsResponseTypeDef",
    {
        "FindingStatistics": "FindingStatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIPSetRequestRequestTypeDef = TypedDict(
    "GetIPSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "IpSetId": str,
    },
)

GetIPSetResponseTypeDef = TypedDict(
    "GetIPSetResponseTypeDef",
    {
        "Name": str,
        "Format": IpSetFormatType,
        "Location": str,
        "Status": IpSetStatusType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInvitationsCountResponseTypeDef = TypedDict(
    "GetInvitationsCountResponseTypeDef",
    {
        "InvitationsCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMalwareScanSettingsRequestRequestTypeDef = TypedDict(
    "GetMalwareScanSettingsRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)

GetMalwareScanSettingsResponseTypeDef = TypedDict(
    "GetMalwareScanSettingsResponseTypeDef",
    {
        "ScanResourceCriteria": "ScanResourceCriteriaTypeDef",
        "EbsSnapshotPreservation": EbsSnapshotPreservationType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMasterAccountRequestRequestTypeDef = TypedDict(
    "GetMasterAccountRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)

GetMasterAccountResponseTypeDef = TypedDict(
    "GetMasterAccountResponseTypeDef",
    {
        "Master": "MasterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMemberDetectorsRequestRequestTypeDef = TypedDict(
    "GetMemberDetectorsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": List[str],
    },
)

GetMemberDetectorsResponseTypeDef = TypedDict(
    "GetMemberDetectorsResponseTypeDef",
    {
        "MemberDataSourceConfigurations": List["MemberDataSourceConfigurationTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMembersRequestRequestTypeDef = TypedDict(
    "GetMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": List[str],
    },
)

GetMembersResponseTypeDef = TypedDict(
    "GetMembersResponseTypeDef",
    {
        "Members": List["MemberTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRemainingFreeTrialDaysRequestRequestTypeDef = TypedDict(
    "_RequiredGetRemainingFreeTrialDaysRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalGetRemainingFreeTrialDaysRequestRequestTypeDef = TypedDict(
    "_OptionalGetRemainingFreeTrialDaysRequestRequestTypeDef",
    {
        "AccountIds": List[str],
    },
    total=False,
)

class GetRemainingFreeTrialDaysRequestRequestTypeDef(
    _RequiredGetRemainingFreeTrialDaysRequestRequestTypeDef,
    _OptionalGetRemainingFreeTrialDaysRequestRequestTypeDef,
):
    pass

GetRemainingFreeTrialDaysResponseTypeDef = TypedDict(
    "GetRemainingFreeTrialDaysResponseTypeDef",
    {
        "Accounts": List["AccountFreeTrialInfoTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetThreatIntelSetRequestRequestTypeDef = TypedDict(
    "GetThreatIntelSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "ThreatIntelSetId": str,
    },
)

GetThreatIntelSetResponseTypeDef = TypedDict(
    "GetThreatIntelSetResponseTypeDef",
    {
        "Name": str,
        "Format": ThreatIntelSetFormatType,
        "Location": str,
        "Status": ThreatIntelSetStatusType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetUsageStatisticsRequestRequestTypeDef = TypedDict(
    "_RequiredGetUsageStatisticsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "UsageStatisticType": UsageStatisticTypeType,
        "UsageCriteria": "UsageCriteriaTypeDef",
    },
)
_OptionalGetUsageStatisticsRequestRequestTypeDef = TypedDict(
    "_OptionalGetUsageStatisticsRequestRequestTypeDef",
    {
        "Unit": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetUsageStatisticsRequestRequestTypeDef(
    _RequiredGetUsageStatisticsRequestRequestTypeDef,
    _OptionalGetUsageStatisticsRequestRequestTypeDef,
):
    pass

GetUsageStatisticsResponseTypeDef = TypedDict(
    "GetUsageStatisticsResponseTypeDef",
    {
        "UsageStatistics": "UsageStatisticsTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HighestSeverityThreatDetailsTypeDef = TypedDict(
    "HighestSeverityThreatDetailsTypeDef",
    {
        "Severity": str,
        "ThreatName": str,
        "Count": int,
    },
    total=False,
)

HostPathTypeDef = TypedDict(
    "HostPathTypeDef",
    {
        "Path": str,
    },
    total=False,
)

IamInstanceProfileTypeDef = TypedDict(
    "IamInstanceProfileTypeDef",
    {
        "Arn": str,
        "Id": str,
    },
    total=False,
)

InstanceDetailsTypeDef = TypedDict(
    "InstanceDetailsTypeDef",
    {
        "AvailabilityZone": str,
        "IamInstanceProfile": "IamInstanceProfileTypeDef",
        "ImageDescription": str,
        "ImageId": str,
        "InstanceId": str,
        "InstanceState": str,
        "InstanceType": str,
        "OutpostArn": str,
        "LaunchTime": str,
        "NetworkInterfaces": List["NetworkInterfaceTypeDef"],
        "Platform": str,
        "ProductCodes": List["ProductCodeTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "AccountId": str,
        "InvitationId": str,
        "RelationshipStatus": str,
        "InvitedAt": str,
    },
    total=False,
)

_RequiredInviteMembersRequestRequestTypeDef = TypedDict(
    "_RequiredInviteMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": List[str],
    },
)
_OptionalInviteMembersRequestRequestTypeDef = TypedDict(
    "_OptionalInviteMembersRequestRequestTypeDef",
    {
        "DisableEmailNotification": bool,
        "Message": str,
    },
    total=False,
)

class InviteMembersRequestRequestTypeDef(
    _RequiredInviteMembersRequestRequestTypeDef, _OptionalInviteMembersRequestRequestTypeDef
):
    pass

InviteMembersResponseTypeDef = TypedDict(
    "InviteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KubernetesApiCallActionTypeDef = TypedDict(
    "KubernetesApiCallActionTypeDef",
    {
        "RequestUri": str,
        "Verb": str,
        "SourceIps": List[str],
        "UserAgent": str,
        "RemoteIpDetails": "RemoteIpDetailsTypeDef",
        "StatusCode": int,
        "Parameters": str,
    },
    total=False,
)

KubernetesAuditLogsConfigurationResultTypeDef = TypedDict(
    "KubernetesAuditLogsConfigurationResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
)

KubernetesAuditLogsConfigurationTypeDef = TypedDict(
    "KubernetesAuditLogsConfigurationTypeDef",
    {
        "Enable": bool,
    },
)

KubernetesConfigurationResultTypeDef = TypedDict(
    "KubernetesConfigurationResultTypeDef",
    {
        "AuditLogs": "KubernetesAuditLogsConfigurationResultTypeDef",
    },
)

KubernetesConfigurationTypeDef = TypedDict(
    "KubernetesConfigurationTypeDef",
    {
        "AuditLogs": "KubernetesAuditLogsConfigurationTypeDef",
    },
)

KubernetesDataSourceFreeTrialTypeDef = TypedDict(
    "KubernetesDataSourceFreeTrialTypeDef",
    {
        "AuditLogs": "DataSourceFreeTrialTypeDef",
    },
    total=False,
)

KubernetesDetailsTypeDef = TypedDict(
    "KubernetesDetailsTypeDef",
    {
        "KubernetesUserDetails": "KubernetesUserDetailsTypeDef",
        "KubernetesWorkloadDetails": "KubernetesWorkloadDetailsTypeDef",
    },
    total=False,
)

KubernetesUserDetailsTypeDef = TypedDict(
    "KubernetesUserDetailsTypeDef",
    {
        "Username": str,
        "Uid": str,
        "Groups": List[str],
    },
    total=False,
)

KubernetesWorkloadDetailsTypeDef = TypedDict(
    "KubernetesWorkloadDetailsTypeDef",
    {
        "Name": str,
        "Type": str,
        "Uid": str,
        "Namespace": str,
        "HostNetwork": bool,
        "Containers": List["ContainerTypeDef"],
        "Volumes": List["VolumeTypeDef"],
    },
    total=False,
)

ListDetectorsRequestRequestTypeDef = TypedDict(
    "ListDetectorsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListDetectorsResponseTypeDef = TypedDict(
    "ListDetectorsResponseTypeDef",
    {
        "DetectorIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFiltersRequestRequestTypeDef = TypedDict(
    "_RequiredListFiltersRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalListFiltersRequestRequestTypeDef = TypedDict(
    "_OptionalListFiltersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListFiltersRequestRequestTypeDef(
    _RequiredListFiltersRequestRequestTypeDef, _OptionalListFiltersRequestRequestTypeDef
):
    pass

ListFiltersResponseTypeDef = TypedDict(
    "ListFiltersResponseTypeDef",
    {
        "FilterNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredListFindingsRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalListFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalListFindingsRequestRequestTypeDef",
    {
        "FindingCriteria": "FindingCriteriaTypeDef",
        "SortCriteria": "SortCriteriaTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListFindingsRequestRequestTypeDef(
    _RequiredListFindingsRequestRequestTypeDef, _OptionalListFindingsRequestRequestTypeDef
):
    pass

ListFindingsResponseTypeDef = TypedDict(
    "ListFindingsResponseTypeDef",
    {
        "FindingIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIPSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListIPSetsRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalListIPSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListIPSetsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListIPSetsRequestRequestTypeDef(
    _RequiredListIPSetsRequestRequestTypeDef, _OptionalListIPSetsRequestRequestTypeDef
):
    pass

ListIPSetsResponseTypeDef = TypedDict(
    "ListIPSetsResponseTypeDef",
    {
        "IpSetIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInvitationsRequestRequestTypeDef = TypedDict(
    "ListInvitationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {
        "Invitations": List["InvitationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMembersRequestRequestTypeDef = TypedDict(
    "_RequiredListMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalListMembersRequestRequestTypeDef = TypedDict(
    "_OptionalListMembersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "OnlyAssociated": str,
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
        "Members": List["MemberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOrganizationAdminAccountsRequestRequestTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListOrganizationAdminAccountsResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseTypeDef",
    {
        "AdminAccounts": List["AdminAccountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPublishingDestinationsRequestRequestTypeDef = TypedDict(
    "_RequiredListPublishingDestinationsRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalListPublishingDestinationsRequestRequestTypeDef = TypedDict(
    "_OptionalListPublishingDestinationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListPublishingDestinationsRequestRequestTypeDef(
    _RequiredListPublishingDestinationsRequestRequestTypeDef,
    _OptionalListPublishingDestinationsRequestRequestTypeDef,
):
    pass

ListPublishingDestinationsResponseTypeDef = TypedDict(
    "ListPublishingDestinationsResponseTypeDef",
    {
        "Destinations": List["DestinationTypeDef"],
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

_RequiredListThreatIntelSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListThreatIntelSetsRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalListThreatIntelSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListThreatIntelSetsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListThreatIntelSetsRequestRequestTypeDef(
    _RequiredListThreatIntelSetsRequestRequestTypeDef,
    _OptionalListThreatIntelSetsRequestRequestTypeDef,
):
    pass

ListThreatIntelSetsResponseTypeDef = TypedDict(
    "ListThreatIntelSetsResponseTypeDef",
    {
        "ThreatIntelSetIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocalIpDetailsTypeDef = TypedDict(
    "LocalIpDetailsTypeDef",
    {
        "IpAddressV4": str,
    },
    total=False,
)

LocalPortDetailsTypeDef = TypedDict(
    "LocalPortDetailsTypeDef",
    {
        "Port": int,
        "PortName": str,
    },
    total=False,
)

MalwareProtectionConfigurationResultTypeDef = TypedDict(
    "MalwareProtectionConfigurationResultTypeDef",
    {
        "ScanEc2InstanceWithFindings": "ScanEc2InstanceWithFindingsResultTypeDef",
        "ServiceRole": str,
    },
    total=False,
)

MalwareProtectionConfigurationTypeDef = TypedDict(
    "MalwareProtectionConfigurationTypeDef",
    {
        "ScanEc2InstanceWithFindings": "ScanEc2InstanceWithFindingsTypeDef",
    },
    total=False,
)

MalwareProtectionDataSourceFreeTrialTypeDef = TypedDict(
    "MalwareProtectionDataSourceFreeTrialTypeDef",
    {
        "ScanEc2InstanceWithFindings": "DataSourceFreeTrialTypeDef",
    },
    total=False,
)

MasterTypeDef = TypedDict(
    "MasterTypeDef",
    {
        "AccountId": str,
        "InvitationId": str,
        "RelationshipStatus": str,
        "InvitedAt": str,
    },
    total=False,
)

MemberDataSourceConfigurationTypeDef = TypedDict(
    "MemberDataSourceConfigurationTypeDef",
    {
        "AccountId": str,
        "DataSources": "DataSourceConfigurationsResultTypeDef",
    },
)

_RequiredMemberTypeDef = TypedDict(
    "_RequiredMemberTypeDef",
    {
        "AccountId": str,
        "MasterId": str,
        "Email": str,
        "RelationshipStatus": str,
        "UpdatedAt": str,
    },
)
_OptionalMemberTypeDef = TypedDict(
    "_OptionalMemberTypeDef",
    {
        "DetectorId": str,
        "InvitedAt": str,
        "AdministratorId": str,
    },
    total=False,
)

class MemberTypeDef(_RequiredMemberTypeDef, _OptionalMemberTypeDef):
    pass

NetworkConnectionActionTypeDef = TypedDict(
    "NetworkConnectionActionTypeDef",
    {
        "Blocked": bool,
        "ConnectionDirection": str,
        "LocalPortDetails": "LocalPortDetailsTypeDef",
        "Protocol": str,
        "LocalIpDetails": "LocalIpDetailsTypeDef",
        "RemoteIpDetails": "RemoteIpDetailsTypeDef",
        "RemotePortDetails": "RemotePortDetailsTypeDef",
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "Ipv6Addresses": List[str],
        "NetworkInterfaceId": str,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["PrivateIpAddressDetailsTypeDef"],
        "PublicDnsName": str,
        "PublicIp": str,
        "SecurityGroups": List["SecurityGroupTypeDef"],
        "SubnetId": str,
        "VpcId": str,
    },
    total=False,
)

_RequiredOrganizationDataSourceConfigurationsResultTypeDef = TypedDict(
    "_RequiredOrganizationDataSourceConfigurationsResultTypeDef",
    {
        "S3Logs": "OrganizationS3LogsConfigurationResultTypeDef",
    },
)
_OptionalOrganizationDataSourceConfigurationsResultTypeDef = TypedDict(
    "_OptionalOrganizationDataSourceConfigurationsResultTypeDef",
    {
        "Kubernetes": "OrganizationKubernetesConfigurationResultTypeDef",
        "MalwareProtection": "OrganizationMalwareProtectionConfigurationResultTypeDef",
    },
    total=False,
)

class OrganizationDataSourceConfigurationsResultTypeDef(
    _RequiredOrganizationDataSourceConfigurationsResultTypeDef,
    _OptionalOrganizationDataSourceConfigurationsResultTypeDef,
):
    pass

OrganizationDataSourceConfigurationsTypeDef = TypedDict(
    "OrganizationDataSourceConfigurationsTypeDef",
    {
        "S3Logs": "OrganizationS3LogsConfigurationTypeDef",
        "Kubernetes": "OrganizationKubernetesConfigurationTypeDef",
        "MalwareProtection": "OrganizationMalwareProtectionConfigurationTypeDef",
    },
    total=False,
)

OrganizationEbsVolumesResultTypeDef = TypedDict(
    "OrganizationEbsVolumesResultTypeDef",
    {
        "AutoEnable": bool,
    },
    total=False,
)

OrganizationEbsVolumesTypeDef = TypedDict(
    "OrganizationEbsVolumesTypeDef",
    {
        "AutoEnable": bool,
    },
    total=False,
)

OrganizationKubernetesAuditLogsConfigurationResultTypeDef = TypedDict(
    "OrganizationKubernetesAuditLogsConfigurationResultTypeDef",
    {
        "AutoEnable": bool,
    },
)

OrganizationKubernetesAuditLogsConfigurationTypeDef = TypedDict(
    "OrganizationKubernetesAuditLogsConfigurationTypeDef",
    {
        "AutoEnable": bool,
    },
)

OrganizationKubernetesConfigurationResultTypeDef = TypedDict(
    "OrganizationKubernetesConfigurationResultTypeDef",
    {
        "AuditLogs": "OrganizationKubernetesAuditLogsConfigurationResultTypeDef",
    },
)

OrganizationKubernetesConfigurationTypeDef = TypedDict(
    "OrganizationKubernetesConfigurationTypeDef",
    {
        "AuditLogs": "OrganizationKubernetesAuditLogsConfigurationTypeDef",
    },
)

OrganizationMalwareProtectionConfigurationResultTypeDef = TypedDict(
    "OrganizationMalwareProtectionConfigurationResultTypeDef",
    {
        "ScanEc2InstanceWithFindings": "OrganizationScanEc2InstanceWithFindingsResultTypeDef",
    },
    total=False,
)

OrganizationMalwareProtectionConfigurationTypeDef = TypedDict(
    "OrganizationMalwareProtectionConfigurationTypeDef",
    {
        "ScanEc2InstanceWithFindings": "OrganizationScanEc2InstanceWithFindingsTypeDef",
    },
    total=False,
)

OrganizationS3LogsConfigurationResultTypeDef = TypedDict(
    "OrganizationS3LogsConfigurationResultTypeDef",
    {
        "AutoEnable": bool,
    },
)

OrganizationS3LogsConfigurationTypeDef = TypedDict(
    "OrganizationS3LogsConfigurationTypeDef",
    {
        "AutoEnable": bool,
    },
)

OrganizationScanEc2InstanceWithFindingsResultTypeDef = TypedDict(
    "OrganizationScanEc2InstanceWithFindingsResultTypeDef",
    {
        "EbsVolumes": "OrganizationEbsVolumesResultTypeDef",
    },
    total=False,
)

OrganizationScanEc2InstanceWithFindingsTypeDef = TypedDict(
    "OrganizationScanEc2InstanceWithFindingsTypeDef",
    {
        "EbsVolumes": "OrganizationEbsVolumesTypeDef",
    },
    total=False,
)

OrganizationTypeDef = TypedDict(
    "OrganizationTypeDef",
    {
        "Asn": str,
        "AsnOrg": str,
        "Isp": str,
        "Org": str,
    },
    total=False,
)

OwnerTypeDef = TypedDict(
    "OwnerTypeDef",
    {
        "Id": str,
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

PermissionConfigurationTypeDef = TypedDict(
    "PermissionConfigurationTypeDef",
    {
        "BucketLevelPermissions": "BucketLevelPermissionsTypeDef",
        "AccountLevelPermissions": "AccountLevelPermissionsTypeDef",
    },
    total=False,
)

PortProbeActionTypeDef = TypedDict(
    "PortProbeActionTypeDef",
    {
        "Blocked": bool,
        "PortProbeDetails": List["PortProbeDetailTypeDef"],
    },
    total=False,
)

PortProbeDetailTypeDef = TypedDict(
    "PortProbeDetailTypeDef",
    {
        "LocalPortDetails": "LocalPortDetailsTypeDef",
        "LocalIpDetails": "LocalIpDetailsTypeDef",
        "RemoteIpDetails": "RemoteIpDetailsTypeDef",
    },
    total=False,
)

PrivateIpAddressDetailsTypeDef = TypedDict(
    "PrivateIpAddressDetailsTypeDef",
    {
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
    },
    total=False,
)

ProductCodeTypeDef = TypedDict(
    "ProductCodeTypeDef",
    {
        "Code": str,
        "ProductType": str,
    },
    total=False,
)

PublicAccessTypeDef = TypedDict(
    "PublicAccessTypeDef",
    {
        "PermissionConfiguration": "PermissionConfigurationTypeDef",
        "EffectivePermission": str,
    },
    total=False,
)

RemoteAccountDetailsTypeDef = TypedDict(
    "RemoteAccountDetailsTypeDef",
    {
        "AccountId": str,
        "Affiliated": bool,
    },
    total=False,
)

RemoteIpDetailsTypeDef = TypedDict(
    "RemoteIpDetailsTypeDef",
    {
        "City": "CityTypeDef",
        "Country": "CountryTypeDef",
        "GeoLocation": "GeoLocationTypeDef",
        "IpAddressV4": str,
        "Organization": "OrganizationTypeDef",
    },
    total=False,
)

RemotePortDetailsTypeDef = TypedDict(
    "RemotePortDetailsTypeDef",
    {
        "Port": int,
        "PortName": str,
    },
    total=False,
)

ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "InstanceArn": str,
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "AccessKeyDetails": "AccessKeyDetailsTypeDef",
        "S3BucketDetails": List["S3BucketDetailTypeDef"],
        "InstanceDetails": "InstanceDetailsTypeDef",
        "EksClusterDetails": "EksClusterDetailsTypeDef",
        "KubernetesDetails": "KubernetesDetailsTypeDef",
        "ResourceType": str,
        "EbsVolumeDetails": "EbsVolumeDetailsTypeDef",
        "EcsClusterDetails": "EcsClusterDetailsTypeDef",
        "ContainerDetails": "ContainerTypeDef",
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

S3BucketDetailTypeDef = TypedDict(
    "S3BucketDetailTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": str,
        "CreatedAt": datetime,
        "Owner": "OwnerTypeDef",
        "Tags": List["TagTypeDef"],
        "DefaultServerSideEncryption": "DefaultServerSideEncryptionTypeDef",
        "PublicAccess": "PublicAccessTypeDef",
    },
    total=False,
)

S3LogsConfigurationResultTypeDef = TypedDict(
    "S3LogsConfigurationResultTypeDef",
    {
        "Status": DataSourceStatusType,
    },
)

S3LogsConfigurationTypeDef = TypedDict(
    "S3LogsConfigurationTypeDef",
    {
        "Enable": bool,
    },
)

_RequiredScanConditionPairTypeDef = TypedDict(
    "_RequiredScanConditionPairTypeDef",
    {
        "Key": str,
    },
)
_OptionalScanConditionPairTypeDef = TypedDict(
    "_OptionalScanConditionPairTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class ScanConditionPairTypeDef(
    _RequiredScanConditionPairTypeDef, _OptionalScanConditionPairTypeDef
):
    pass

ScanConditionTypeDef = TypedDict(
    "ScanConditionTypeDef",
    {
        "MapEquals": List["ScanConditionPairTypeDef"],
    },
)

ScanDetectionsTypeDef = TypedDict(
    "ScanDetectionsTypeDef",
    {
        "ScannedItemCount": "ScannedItemCountTypeDef",
        "ThreatsDetectedItemCount": "ThreatsDetectedItemCountTypeDef",
        "HighestSeverityThreatDetails": "HighestSeverityThreatDetailsTypeDef",
        "ThreatDetectedByName": "ThreatDetectedByNameTypeDef",
    },
    total=False,
)

ScanEc2InstanceWithFindingsResultTypeDef = TypedDict(
    "ScanEc2InstanceWithFindingsResultTypeDef",
    {
        "EbsVolumes": "EbsVolumesResultTypeDef",
    },
    total=False,
)

ScanEc2InstanceWithFindingsTypeDef = TypedDict(
    "ScanEc2InstanceWithFindingsTypeDef",
    {
        "EbsVolumes": bool,
    },
    total=False,
)

ScanFilePathTypeDef = TypedDict(
    "ScanFilePathTypeDef",
    {
        "FilePath": str,
        "VolumeArn": str,
        "Hash": str,
        "FileName": str,
    },
    total=False,
)

ScanResourceCriteriaTypeDef = TypedDict(
    "ScanResourceCriteriaTypeDef",
    {
        "Include": Dict[Literal["EC2_INSTANCE_TAG"], "ScanConditionTypeDef"],
        "Exclude": Dict[Literal["EC2_INSTANCE_TAG"], "ScanConditionTypeDef"],
    },
    total=False,
)

ScanResultDetailsTypeDef = TypedDict(
    "ScanResultDetailsTypeDef",
    {
        "ScanResult": ScanResultType,
    },
    total=False,
)

ScanThreatNameTypeDef = TypedDict(
    "ScanThreatNameTypeDef",
    {
        "Name": str,
        "Severity": str,
        "ItemCount": int,
        "FilePaths": List["ScanFilePathTypeDef"],
    },
    total=False,
)

ScanTypeDef = TypedDict(
    "ScanTypeDef",
    {
        "DetectorId": str,
        "AdminDetectorId": str,
        "ScanId": str,
        "ScanStatus": ScanStatusType,
        "FailureReason": str,
        "ScanStartTime": datetime,
        "ScanEndTime": datetime,
        "TriggerDetails": "TriggerDetailsTypeDef",
        "ResourceDetails": "ResourceDetailsTypeDef",
        "ScanResultDetails": "ScanResultDetailsTypeDef",
        "AccountId": str,
        "TotalBytes": int,
        "FileCount": int,
        "AttachedVolumes": List["VolumeDetailTypeDef"],
    },
    total=False,
)

ScannedItemCountTypeDef = TypedDict(
    "ScannedItemCountTypeDef",
    {
        "TotalGb": int,
        "Files": int,
        "Volumes": int,
    },
    total=False,
)

SecurityContextTypeDef = TypedDict(
    "SecurityContextTypeDef",
    {
        "Privileged": bool,
    },
    total=False,
)

SecurityGroupTypeDef = TypedDict(
    "SecurityGroupTypeDef",
    {
        "GroupId": str,
        "GroupName": str,
    },
    total=False,
)

ServiceAdditionalInfoTypeDef = TypedDict(
    "ServiceAdditionalInfoTypeDef",
    {
        "Value": str,
        "Type": str,
    },
    total=False,
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "Action": "ActionTypeDef",
        "Evidence": "EvidenceTypeDef",
        "Archived": bool,
        "Count": int,
        "DetectorId": str,
        "EventFirstSeen": str,
        "EventLastSeen": str,
        "ResourceRole": str,
        "ServiceName": str,
        "UserFeedback": str,
        "AdditionalInfo": "ServiceAdditionalInfoTypeDef",
        "FeatureName": str,
        "EbsVolumeScanDetails": "EbsVolumeScanDetailsTypeDef",
    },
    total=False,
)

SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef",
    {
        "AttributeName": str,
        "OrderBy": OrderByType,
    },
    total=False,
)

StartMonitoringMembersRequestRequestTypeDef = TypedDict(
    "StartMonitoringMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": List[str],
    },
)

StartMonitoringMembersResponseTypeDef = TypedDict(
    "StartMonitoringMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopMonitoringMembersRequestRequestTypeDef = TypedDict(
    "StopMonitoringMembersRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": List[str],
    },
)

StopMonitoringMembersResponseTypeDef = TypedDict(
    "StopMonitoringMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

ThreatDetectedByNameTypeDef = TypedDict(
    "ThreatDetectedByNameTypeDef",
    {
        "ItemCount": int,
        "UniqueThreatNameCount": int,
        "Shortened": bool,
        "ThreatNames": List["ScanThreatNameTypeDef"],
    },
    total=False,
)

ThreatIntelligenceDetailTypeDef = TypedDict(
    "ThreatIntelligenceDetailTypeDef",
    {
        "ThreatListName": str,
        "ThreatNames": List[str],
    },
    total=False,
)

ThreatsDetectedItemCountTypeDef = TypedDict(
    "ThreatsDetectedItemCountTypeDef",
    {
        "Files": int,
    },
    total=False,
)

TotalTypeDef = TypedDict(
    "TotalTypeDef",
    {
        "Amount": str,
        "Unit": str,
    },
    total=False,
)

TriggerDetailsTypeDef = TypedDict(
    "TriggerDetailsTypeDef",
    {
        "GuardDutyFindingId": str,
        "Description": str,
    },
    total=False,
)

UnarchiveFindingsRequestRequestTypeDef = TypedDict(
    "UnarchiveFindingsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FindingIds": List[str],
    },
)

UnprocessedAccountTypeDef = TypedDict(
    "UnprocessedAccountTypeDef",
    {
        "AccountId": str,
        "Result": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateDetectorRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDetectorRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalUpdateDetectorRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDetectorRequestRequestTypeDef",
    {
        "Enable": bool,
        "FindingPublishingFrequency": FindingPublishingFrequencyType,
        "DataSources": "DataSourceConfigurationsTypeDef",
    },
    total=False,
)

class UpdateDetectorRequestRequestTypeDef(
    _RequiredUpdateDetectorRequestRequestTypeDef, _OptionalUpdateDetectorRequestRequestTypeDef
):
    pass

_RequiredUpdateFilterRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFilterRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FilterName": str,
    },
)
_OptionalUpdateFilterRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFilterRequestRequestTypeDef",
    {
        "Description": str,
        "Action": FilterActionType,
        "Rank": int,
        "FindingCriteria": "FindingCriteriaTypeDef",
    },
    total=False,
)

class UpdateFilterRequestRequestTypeDef(
    _RequiredUpdateFilterRequestRequestTypeDef, _OptionalUpdateFilterRequestRequestTypeDef
):
    pass

UpdateFilterResponseTypeDef = TypedDict(
    "UpdateFilterResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFindingsFeedbackRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFindingsFeedbackRequestRequestTypeDef",
    {
        "DetectorId": str,
        "FindingIds": List[str],
        "Feedback": FeedbackType,
    },
)
_OptionalUpdateFindingsFeedbackRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFindingsFeedbackRequestRequestTypeDef",
    {
        "Comments": str,
    },
    total=False,
)

class UpdateFindingsFeedbackRequestRequestTypeDef(
    _RequiredUpdateFindingsFeedbackRequestRequestTypeDef,
    _OptionalUpdateFindingsFeedbackRequestRequestTypeDef,
):
    pass

_RequiredUpdateIPSetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIPSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "IpSetId": str,
    },
)
_OptionalUpdateIPSetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "Location": str,
        "Activate": bool,
    },
    total=False,
)

class UpdateIPSetRequestRequestTypeDef(
    _RequiredUpdateIPSetRequestRequestTypeDef, _OptionalUpdateIPSetRequestRequestTypeDef
):
    pass

_RequiredUpdateMalwareScanSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMalwareScanSettingsRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalUpdateMalwareScanSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMalwareScanSettingsRequestRequestTypeDef",
    {
        "ScanResourceCriteria": "ScanResourceCriteriaTypeDef",
        "EbsSnapshotPreservation": EbsSnapshotPreservationType,
    },
    total=False,
)

class UpdateMalwareScanSettingsRequestRequestTypeDef(
    _RequiredUpdateMalwareScanSettingsRequestRequestTypeDef,
    _OptionalUpdateMalwareScanSettingsRequestRequestTypeDef,
):
    pass

_RequiredUpdateMemberDetectorsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMemberDetectorsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AccountIds": List[str],
    },
)
_OptionalUpdateMemberDetectorsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMemberDetectorsRequestRequestTypeDef",
    {
        "DataSources": "DataSourceConfigurationsTypeDef",
    },
    total=False,
)

class UpdateMemberDetectorsRequestRequestTypeDef(
    _RequiredUpdateMemberDetectorsRequestRequestTypeDef,
    _OptionalUpdateMemberDetectorsRequestRequestTypeDef,
):
    pass

UpdateMemberDetectorsResponseTypeDef = TypedDict(
    "UpdateMemberDetectorsResponseTypeDef",
    {
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "AutoEnable": bool,
    },
)
_OptionalUpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "DataSources": "OrganizationDataSourceConfigurationsTypeDef",
    },
    total=False,
)

class UpdateOrganizationConfigurationRequestRequestTypeDef(
    _RequiredUpdateOrganizationConfigurationRequestRequestTypeDef,
    _OptionalUpdateOrganizationConfigurationRequestRequestTypeDef,
):
    pass

_RequiredUpdatePublishingDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePublishingDestinationRequestRequestTypeDef",
    {
        "DetectorId": str,
        "DestinationId": str,
    },
)
_OptionalUpdatePublishingDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePublishingDestinationRequestRequestTypeDef",
    {
        "DestinationProperties": "DestinationPropertiesTypeDef",
    },
    total=False,
)

class UpdatePublishingDestinationRequestRequestTypeDef(
    _RequiredUpdatePublishingDestinationRequestRequestTypeDef,
    _OptionalUpdatePublishingDestinationRequestRequestTypeDef,
):
    pass

_RequiredUpdateThreatIntelSetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateThreatIntelSetRequestRequestTypeDef",
    {
        "DetectorId": str,
        "ThreatIntelSetId": str,
    },
)
_OptionalUpdateThreatIntelSetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateThreatIntelSetRequestRequestTypeDef",
    {
        "Name": str,
        "Location": str,
        "Activate": bool,
    },
    total=False,
)

class UpdateThreatIntelSetRequestRequestTypeDef(
    _RequiredUpdateThreatIntelSetRequestRequestTypeDef,
    _OptionalUpdateThreatIntelSetRequestRequestTypeDef,
):
    pass

UsageAccountResultTypeDef = TypedDict(
    "UsageAccountResultTypeDef",
    {
        "AccountId": str,
        "Total": "TotalTypeDef",
    },
    total=False,
)

_RequiredUsageCriteriaTypeDef = TypedDict(
    "_RequiredUsageCriteriaTypeDef",
    {
        "DataSources": List[DataSourceType],
    },
)
_OptionalUsageCriteriaTypeDef = TypedDict(
    "_OptionalUsageCriteriaTypeDef",
    {
        "AccountIds": List[str],
        "Resources": List[str],
    },
    total=False,
)

class UsageCriteriaTypeDef(_RequiredUsageCriteriaTypeDef, _OptionalUsageCriteriaTypeDef):
    pass

UsageDataSourceResultTypeDef = TypedDict(
    "UsageDataSourceResultTypeDef",
    {
        "DataSource": DataSourceType,
        "Total": "TotalTypeDef",
    },
    total=False,
)

UsageResourceResultTypeDef = TypedDict(
    "UsageResourceResultTypeDef",
    {
        "Resource": str,
        "Total": "TotalTypeDef",
    },
    total=False,
)

UsageStatisticsTypeDef = TypedDict(
    "UsageStatisticsTypeDef",
    {
        "SumByAccount": List["UsageAccountResultTypeDef"],
        "SumByDataSource": List["UsageDataSourceResultTypeDef"],
        "SumByResource": List["UsageResourceResultTypeDef"],
        "TopResources": List["UsageResourceResultTypeDef"],
    },
    total=False,
)

VolumeDetailTypeDef = TypedDict(
    "VolumeDetailTypeDef",
    {
        "VolumeArn": str,
        "VolumeType": str,
        "DeviceName": str,
        "VolumeSizeInGB": int,
        "EncryptionType": str,
        "SnapshotArn": str,
        "KmsKeyArn": str,
    },
    total=False,
)

VolumeMountTypeDef = TypedDict(
    "VolumeMountTypeDef",
    {
        "Name": str,
        "MountPath": str,
    },
    total=False,
)

VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "Name": str,
        "HostPath": "HostPathTypeDef",
    },
    total=False,
)
