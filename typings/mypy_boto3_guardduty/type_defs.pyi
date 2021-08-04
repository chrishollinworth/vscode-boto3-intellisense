"""
Type annotations for guardduty service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/type_defs.html)

Usage::

    ```python
    from mypy_boto3_guardduty.type_defs import AcceptInvitationRequestRequestTypeDef

    data: AcceptInvitationRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AdminStatusType,
    DataSourceStatusType,
    DataSourceType,
    DetectorStatusType,
    FeedbackType,
    FilterActionType,
    FindingPublishingFrequencyType,
    IpSetFormatType,
    IpSetStatusType,
    OrderByType,
    PublishingStatusType,
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
    "AcceptInvitationRequestRequestTypeDef",
    "AccessControlListTypeDef",
    "AccessKeyDetailsTypeDef",
    "AccountDetailTypeDef",
    "AccountLevelPermissionsTypeDef",
    "ActionTypeDef",
    "AdminAccountTypeDef",
    "ArchiveFindingsRequestRequestTypeDef",
    "AwsApiCallActionTypeDef",
    "BlockPublicAccessTypeDef",
    "BucketLevelPermissionsTypeDef",
    "BucketPolicyTypeDef",
    "CityTypeDef",
    "CloudTrailConfigurationResultTypeDef",
    "ConditionTypeDef",
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
    "DescribeOrganizationConfigurationRequestRequestTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DescribePublishingDestinationRequestRequestTypeDef",
    "DescribePublishingDestinationResponseTypeDef",
    "DestinationPropertiesTypeDef",
    "DestinationTypeDef",
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    "DisassociateFromMasterAccountRequestRequestTypeDef",
    "DisassociateMembersRequestRequestTypeDef",
    "DisassociateMembersResponseTypeDef",
    "DnsRequestActionTypeDef",
    "DomainDetailsTypeDef",
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    "EvidenceTypeDef",
    "FindingCriteriaTypeDef",
    "FindingStatisticsTypeDef",
    "FindingTypeDef",
    "FlowLogsConfigurationResultTypeDef",
    "GeoLocationTypeDef",
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
    "GetMasterAccountRequestRequestTypeDef",
    "GetMasterAccountResponseTypeDef",
    "GetMemberDetectorsRequestRequestTypeDef",
    "GetMemberDetectorsResponseTypeDef",
    "GetMembersRequestRequestTypeDef",
    "GetMembersResponseTypeDef",
    "GetThreatIntelSetRequestRequestTypeDef",
    "GetThreatIntelSetResponseTypeDef",
    "GetUsageStatisticsRequestRequestTypeDef",
    "GetUsageStatisticsResponseTypeDef",
    "IamInstanceProfileTypeDef",
    "InstanceDetailsTypeDef",
    "InvitationTypeDef",
    "InviteMembersRequestRequestTypeDef",
    "InviteMembersResponseTypeDef",
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
    "MasterTypeDef",
    "MemberDataSourceConfigurationTypeDef",
    "MemberTypeDef",
    "NetworkConnectionActionTypeDef",
    "NetworkInterfaceTypeDef",
    "OrganizationDataSourceConfigurationsResultTypeDef",
    "OrganizationDataSourceConfigurationsTypeDef",
    "OrganizationS3LogsConfigurationResultTypeDef",
    "OrganizationS3LogsConfigurationTypeDef",
    "OrganizationTypeDef",
    "OwnerTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionConfigurationTypeDef",
    "PortProbeActionTypeDef",
    "PortProbeDetailTypeDef",
    "PrivateIpAddressDetailsTypeDef",
    "ProductCodeTypeDef",
    "PublicAccessTypeDef",
    "RemoteIpDetailsTypeDef",
    "RemotePortDetailsTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "S3BucketDetailTypeDef",
    "S3LogsConfigurationResultTypeDef",
    "S3LogsConfigurationTypeDef",
    "SecurityGroupTypeDef",
    "ServiceTypeDef",
    "SortCriteriaTypeDef",
    "StartMonitoringMembersRequestRequestTypeDef",
    "StartMonitoringMembersResponseTypeDef",
    "StopMonitoringMembersRequestRequestTypeDef",
    "StopMonitoringMembersResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "ThreatIntelligenceDetailTypeDef",
    "TotalTypeDef",
    "UnarchiveFindingsRequestRequestTypeDef",
    "UnprocessedAccountTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDetectorRequestRequestTypeDef",
    "UpdateFilterRequestRequestTypeDef",
    "UpdateFilterResponseTypeDef",
    "UpdateFindingsFeedbackRequestRequestTypeDef",
    "UpdateIPSetRequestRequestTypeDef",
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
        "RemoteIpDetails": "RemoteIpDetailsTypeDef",
        "ServiceName": str,
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

DataSourceConfigurationsResultTypeDef = TypedDict(
    "DataSourceConfigurationsResultTypeDef",
    {
        "CloudTrail": "CloudTrailConfigurationResultTypeDef",
        "DNSLogs": "DNSLogsConfigurationResultTypeDef",
        "FlowLogs": "FlowLogsConfigurationResultTypeDef",
        "S3Logs": "S3LogsConfigurationResultTypeDef",
    },
)

DataSourceConfigurationsTypeDef = TypedDict(
    "DataSourceConfigurationsTypeDef",
    {
        "S3Logs": "S3LogsConfigurationTypeDef",
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

OrganizationDataSourceConfigurationsResultTypeDef = TypedDict(
    "OrganizationDataSourceConfigurationsResultTypeDef",
    {
        "S3Logs": "OrganizationS3LogsConfigurationResultTypeDef",
    },
)

OrganizationDataSourceConfigurationsTypeDef = TypedDict(
    "OrganizationDataSourceConfigurationsTypeDef",
    {
        "S3Logs": "OrganizationS3LogsConfigurationTypeDef",
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

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "AccessKeyDetails": "AccessKeyDetailsTypeDef",
        "S3BucketDetails": List["S3BucketDetailTypeDef"],
        "InstanceDetails": "InstanceDetailsTypeDef",
        "ResourceType": str,
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

SecurityGroupTypeDef = TypedDict(
    "SecurityGroupTypeDef",
    {
        "GroupId": str,
        "GroupName": str,
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

ThreatIntelligenceDetailTypeDef = TypedDict(
    "ThreatIntelligenceDetailTypeDef",
    {
        "ThreatListName": str,
        "ThreatNames": List[str],
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
