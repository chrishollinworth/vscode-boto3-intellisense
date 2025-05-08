"""
Type annotations for guardduty service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_guardduty.type_defs import AcceptAdministratorInvitationRequestTypeDef

    data: AcceptAdministratorInvitationRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AdminStatusType,
    AutoEnableMembersType,
    CoverageFilterCriterionKeyType,
    CoverageSortKeyType,
    CoverageStatisticsTypeType,
    CoverageStatusType,
    CriterionKeyType,
    DataSourceStatusType,
    DataSourceType,
    DetectorFeatureResultType,
    DetectorFeatureType,
    DetectorStatusType,
    EbsSnapshotPreservationType,
    FeatureAdditionalConfigurationType,
    FeatureStatusType,
    FeedbackType,
    FilterActionType,
    FindingPublishingFrequencyType,
    FindingResourceTypeType,
    FreeTrialFeatureResultType,
    GroupByTypeType,
    IndicatorTypeType,
    IpSetFormatType,
    IpSetStatusType,
    MalwareProtectionPlanStatusType,
    MalwareProtectionPlanTaggingActionStatusType,
    ManagementTypeType,
    MfaStatusType,
    NetworkDirectionType,
    OrderByType,
    OrgFeatureAdditionalConfigurationType,
    OrgFeatureStatusType,
    OrgFeatureType,
    ProfileSubtypeType,
    PublicAccessStatusType,
    PublicAclIgnoreBehaviorType,
    PublicBucketRestrictBehaviorType,
    PublishingStatusType,
    ResourceTypeType,
    ScanResultType,
    ScanStatusType,
    ScanTypeType,
    SignalTypeType,
    ThreatIntelSetFormatType,
    ThreatIntelSetStatusType,
    UsageFeatureType,
    UsageStatisticTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AcceptAdministratorInvitationRequestTypeDef",
    "AcceptInvitationRequestTypeDef",
    "AccessControlListTypeDef",
    "AccessKeyDetailsTypeDef",
    "AccessKeyTypeDef",
    "AccountDetailTypeDef",
    "AccountFreeTrialInfoTypeDef",
    "AccountLevelPermissionsTypeDef",
    "AccountStatisticsTypeDef",
    "AccountTypeDef",
    "ActionTypeDef",
    "ActorTypeDef",
    "AddonDetailsTypeDef",
    "AdminAccountTypeDef",
    "AdministratorTypeDef",
    "AgentDetailsTypeDef",
    "AnomalyObjectTypeDef",
    "AnomalyTypeDef",
    "AnomalyUnusualTypeDef",
    "ArchiveFindingsRequestTypeDef",
    "AutonomousSystemTypeDef",
    "AwsApiCallActionTypeDef",
    "BlockPublicAccessTypeDef",
    "BucketLevelPermissionsTypeDef",
    "BucketPolicyTypeDef",
    "CityTypeDef",
    "CloudTrailConfigurationResultTypeDef",
    "ConditionOutputTypeDef",
    "ConditionTypeDef",
    "ContainerInstanceDetailsTypeDef",
    "ContainerTypeDef",
    "CountryTypeDef",
    "CoverageEc2InstanceDetailsTypeDef",
    "CoverageEcsClusterDetailsTypeDef",
    "CoverageEksClusterDetailsTypeDef",
    "CoverageFilterConditionTypeDef",
    "CoverageFilterCriteriaTypeDef",
    "CoverageFilterCriterionTypeDef",
    "CoverageResourceDetailsTypeDef",
    "CoverageResourceTypeDef",
    "CoverageSortCriteriaTypeDef",
    "CoverageStatisticsTypeDef",
    "CreateDetectorRequestTypeDef",
    "CreateDetectorResponseTypeDef",
    "CreateFilterRequestTypeDef",
    "CreateFilterResponseTypeDef",
    "CreateIPSetRequestTypeDef",
    "CreateIPSetResponseTypeDef",
    "CreateMalwareProtectionPlanRequestTypeDef",
    "CreateMalwareProtectionPlanResponseTypeDef",
    "CreateMembersRequestTypeDef",
    "CreateMembersResponseTypeDef",
    "CreateProtectedResourceOutputTypeDef",
    "CreateProtectedResourceTypeDef",
    "CreateProtectedResourceUnionTypeDef",
    "CreatePublishingDestinationRequestTypeDef",
    "CreatePublishingDestinationResponseTypeDef",
    "CreateS3BucketResourceOutputTypeDef",
    "CreateS3BucketResourceTypeDef",
    "CreateSampleFindingsRequestTypeDef",
    "CreateThreatIntelSetRequestTypeDef",
    "CreateThreatIntelSetResponseTypeDef",
    "DNSLogsConfigurationResultTypeDef",
    "DataSourceConfigurationsResultTypeDef",
    "DataSourceConfigurationsTypeDef",
    "DataSourceFreeTrialTypeDef",
    "DataSourcesFreeTrialTypeDef",
    "DateStatisticsTypeDef",
    "DeclineInvitationsRequestTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DefaultServerSideEncryptionTypeDef",
    "DeleteDetectorRequestTypeDef",
    "DeleteFilterRequestTypeDef",
    "DeleteIPSetRequestTypeDef",
    "DeleteInvitationsRequestTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "DeleteMalwareProtectionPlanRequestTypeDef",
    "DeleteMembersRequestTypeDef",
    "DeleteMembersResponseTypeDef",
    "DeletePublishingDestinationRequestTypeDef",
    "DeleteThreatIntelSetRequestTypeDef",
    "DescribeMalwareScansRequestPaginateTypeDef",
    "DescribeMalwareScansRequestTypeDef",
    "DescribeMalwareScansResponseTypeDef",
    "DescribeOrganizationConfigurationRequestTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DescribePublishingDestinationRequestTypeDef",
    "DescribePublishingDestinationResponseTypeDef",
    "DestinationPropertiesTypeDef",
    "DestinationTypeDef",
    "DetectionTypeDef",
    "DetectorAdditionalConfigurationResultTypeDef",
    "DetectorAdditionalConfigurationTypeDef",
    "DetectorFeatureConfigurationResultTypeDef",
    "DetectorFeatureConfigurationTypeDef",
    "DisableOrganizationAdminAccountRequestTypeDef",
    "DisassociateFromAdministratorAccountRequestTypeDef",
    "DisassociateFromMasterAccountRequestTypeDef",
    "DisassociateMembersRequestTypeDef",
    "DisassociateMembersResponseTypeDef",
    "DnsRequestActionTypeDef",
    "DomainDetailsTypeDef",
    "EbsVolumeDetailsTypeDef",
    "EbsVolumeScanDetailsTypeDef",
    "EbsVolumesResultTypeDef",
    "Ec2InstanceTypeDef",
    "Ec2NetworkInterfaceTypeDef",
    "EcsClusterDetailsTypeDef",
    "EcsTaskDetailsTypeDef",
    "EksClusterDetailsTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableOrganizationAdminAccountRequestTypeDef",
    "EvidenceTypeDef",
    "FargateDetailsTypeDef",
    "FilterConditionTypeDef",
    "FilterCriteriaTypeDef",
    "FilterCriterionTypeDef",
    "FindingCriteriaOutputTypeDef",
    "FindingCriteriaTypeDef",
    "FindingCriteriaUnionTypeDef",
    "FindingStatisticsTypeDef",
    "FindingTypeDef",
    "FindingTypeStatisticsTypeDef",
    "FlowLogsConfigurationResultTypeDef",
    "FreeTrialFeatureConfigurationResultTypeDef",
    "GeoLocationTypeDef",
    "GetAdministratorAccountRequestTypeDef",
    "GetAdministratorAccountResponseTypeDef",
    "GetCoverageStatisticsRequestTypeDef",
    "GetCoverageStatisticsResponseTypeDef",
    "GetDetectorRequestTypeDef",
    "GetDetectorResponseTypeDef",
    "GetFilterRequestTypeDef",
    "GetFilterResponseTypeDef",
    "GetFindingsRequestTypeDef",
    "GetFindingsResponseTypeDef",
    "GetFindingsStatisticsRequestTypeDef",
    "GetFindingsStatisticsResponseTypeDef",
    "GetIPSetRequestTypeDef",
    "GetIPSetResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "GetMalwareProtectionPlanRequestTypeDef",
    "GetMalwareProtectionPlanResponseTypeDef",
    "GetMalwareScanSettingsRequestTypeDef",
    "GetMalwareScanSettingsResponseTypeDef",
    "GetMasterAccountRequestTypeDef",
    "GetMasterAccountResponseTypeDef",
    "GetMemberDetectorsRequestTypeDef",
    "GetMemberDetectorsResponseTypeDef",
    "GetMembersRequestTypeDef",
    "GetMembersResponseTypeDef",
    "GetOrganizationStatisticsResponseTypeDef",
    "GetRemainingFreeTrialDaysRequestTypeDef",
    "GetRemainingFreeTrialDaysResponseTypeDef",
    "GetThreatIntelSetRequestTypeDef",
    "GetThreatIntelSetResponseTypeDef",
    "GetUsageStatisticsRequestTypeDef",
    "GetUsageStatisticsResponseTypeDef",
    "HighestSeverityThreatDetailsTypeDef",
    "HostPathTypeDef",
    "IamInstanceProfileTypeDef",
    "ImpersonatedUserTypeDef",
    "IndicatorTypeDef",
    "InstanceDetailsTypeDef",
    "InvitationTypeDef",
    "InviteMembersRequestTypeDef",
    "InviteMembersResponseTypeDef",
    "ItemPathTypeDef",
    "KubernetesApiCallActionTypeDef",
    "KubernetesAuditLogsConfigurationResultTypeDef",
    "KubernetesAuditLogsConfigurationTypeDef",
    "KubernetesConfigurationResultTypeDef",
    "KubernetesConfigurationTypeDef",
    "KubernetesDataSourceFreeTrialTypeDef",
    "KubernetesDetailsTypeDef",
    "KubernetesPermissionCheckedDetailsTypeDef",
    "KubernetesRoleBindingDetailsTypeDef",
    "KubernetesRoleDetailsTypeDef",
    "KubernetesUserDetailsTypeDef",
    "KubernetesWorkloadDetailsTypeDef",
    "LambdaDetailsTypeDef",
    "LineageObjectTypeDef",
    "ListCoverageRequestPaginateTypeDef",
    "ListCoverageRequestTypeDef",
    "ListCoverageResponseTypeDef",
    "ListDetectorsRequestPaginateTypeDef",
    "ListDetectorsRequestTypeDef",
    "ListDetectorsResponseTypeDef",
    "ListFiltersRequestPaginateTypeDef",
    "ListFiltersRequestTypeDef",
    "ListFiltersResponseTypeDef",
    "ListFindingsRequestPaginateTypeDef",
    "ListFindingsRequestTypeDef",
    "ListFindingsResponseTypeDef",
    "ListIPSetsRequestPaginateTypeDef",
    "ListIPSetsRequestTypeDef",
    "ListIPSetsResponseTypeDef",
    "ListInvitationsRequestPaginateTypeDef",
    "ListInvitationsRequestTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListMalwareProtectionPlansRequestTypeDef",
    "ListMalwareProtectionPlansResponseTypeDef",
    "ListMembersRequestPaginateTypeDef",
    "ListMembersRequestTypeDef",
    "ListMembersResponseTypeDef",
    "ListOrganizationAdminAccountsRequestPaginateTypeDef",
    "ListOrganizationAdminAccountsRequestTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListPublishingDestinationsRequestTypeDef",
    "ListPublishingDestinationsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListThreatIntelSetsRequestPaginateTypeDef",
    "ListThreatIntelSetsRequestTypeDef",
    "ListThreatIntelSetsResponseTypeDef",
    "LocalIpDetailsTypeDef",
    "LocalPortDetailsTypeDef",
    "LoginAttributeTypeDef",
    "MalwareProtectionConfigurationResultTypeDef",
    "MalwareProtectionConfigurationTypeDef",
    "MalwareProtectionDataSourceFreeTrialTypeDef",
    "MalwareProtectionPlanActionsTypeDef",
    "MalwareProtectionPlanStatusReasonTypeDef",
    "MalwareProtectionPlanSummaryTypeDef",
    "MalwareProtectionPlanTaggingActionTypeDef",
    "MalwareScanDetailsTypeDef",
    "MasterTypeDef",
    "MemberAdditionalConfigurationResultTypeDef",
    "MemberAdditionalConfigurationTypeDef",
    "MemberDataSourceConfigurationTypeDef",
    "MemberFeaturesConfigurationResultTypeDef",
    "MemberFeaturesConfigurationTypeDef",
    "MemberTypeDef",
    "NetworkConnectionActionTypeDef",
    "NetworkConnectionTypeDef",
    "NetworkEndpointTypeDef",
    "NetworkGeoLocationTypeDef",
    "NetworkInterfaceTypeDef",
    "ObservationsTypeDef",
    "OrganizationAdditionalConfigurationResultTypeDef",
    "OrganizationAdditionalConfigurationTypeDef",
    "OrganizationDataSourceConfigurationsResultTypeDef",
    "OrganizationDataSourceConfigurationsTypeDef",
    "OrganizationDetailsTypeDef",
    "OrganizationEbsVolumesResultTypeDef",
    "OrganizationEbsVolumesTypeDef",
    "OrganizationFeatureConfigurationResultTypeDef",
    "OrganizationFeatureConfigurationTypeDef",
    "OrganizationFeatureStatisticsAdditionalConfigurationTypeDef",
    "OrganizationFeatureStatisticsTypeDef",
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
    "OrganizationStatisticsTypeDef",
    "OrganizationTypeDef",
    "OwnerTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionConfigurationTypeDef",
    "PortProbeActionTypeDef",
    "PortProbeDetailTypeDef",
    "PrivateIpAddressDetailsTypeDef",
    "ProcessDetailsTypeDef",
    "ProductCodeTypeDef",
    "PublicAccessConfigurationTypeDef",
    "PublicAccessTypeDef",
    "RdsDbInstanceDetailsTypeDef",
    "RdsDbUserDetailsTypeDef",
    "RdsLimitlessDbDetailsTypeDef",
    "RdsLoginAttemptActionTypeDef",
    "RemoteAccountDetailsTypeDef",
    "RemoteIpDetailsTypeDef",
    "RemotePortDetailsTypeDef",
    "ResourceDataTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceStatisticsTypeDef",
    "ResourceTypeDef",
    "ResourceV2TypeDef",
    "ResponseMetadataTypeDef",
    "RuntimeContextTypeDef",
    "RuntimeDetailsTypeDef",
    "S3BucketDetailTypeDef",
    "S3BucketTypeDef",
    "S3LogsConfigurationResultTypeDef",
    "S3LogsConfigurationTypeDef",
    "S3ObjectDetailTypeDef",
    "S3ObjectTypeDef",
    "ScanConditionOutputTypeDef",
    "ScanConditionPairTypeDef",
    "ScanConditionTypeDef",
    "ScanDetectionsTypeDef",
    "ScanEc2InstanceWithFindingsResultTypeDef",
    "ScanEc2InstanceWithFindingsTypeDef",
    "ScanFilePathTypeDef",
    "ScanResourceCriteriaOutputTypeDef",
    "ScanResourceCriteriaTypeDef",
    "ScanResourceCriteriaUnionTypeDef",
    "ScanResultDetailsTypeDef",
    "ScanThreatNameTypeDef",
    "ScanTypeDef",
    "ScannedItemCountTypeDef",
    "SecurityContextTypeDef",
    "SecurityGroupTypeDef",
    "SequenceTypeDef",
    "ServiceAdditionalInfoTypeDef",
    "ServiceTypeDef",
    "SessionTypeDef",
    "SeverityStatisticsTypeDef",
    "SignalTypeDef",
    "SortCriteriaTypeDef",
    "StartMalwareScanRequestTypeDef",
    "StartMalwareScanResponseTypeDef",
    "StartMonitoringMembersRequestTypeDef",
    "StartMonitoringMembersResponseTypeDef",
    "StopMonitoringMembersRequestTypeDef",
    "StopMonitoringMembersResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "ThreatDetectedByNameTypeDef",
    "ThreatIntelligenceDetailTypeDef",
    "ThreatTypeDef",
    "ThreatsDetectedItemCountTypeDef",
    "TotalTypeDef",
    "TriggerDetailsTypeDef",
    "UnarchiveFindingsRequestTypeDef",
    "UnprocessedAccountTypeDef",
    "UnprocessedDataSourcesResultTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDetectorRequestTypeDef",
    "UpdateFilterRequestTypeDef",
    "UpdateFilterResponseTypeDef",
    "UpdateFindingsFeedbackRequestTypeDef",
    "UpdateIPSetRequestTypeDef",
    "UpdateMalwareProtectionPlanRequestTypeDef",
    "UpdateMalwareScanSettingsRequestTypeDef",
    "UpdateMemberDetectorsRequestTypeDef",
    "UpdateMemberDetectorsResponseTypeDef",
    "UpdateOrganizationConfigurationRequestTypeDef",
    "UpdateProtectedResourceTypeDef",
    "UpdatePublishingDestinationRequestTypeDef",
    "UpdateS3BucketResourceTypeDef",
    "UpdateThreatIntelSetRequestTypeDef",
    "UsageAccountResultTypeDef",
    "UsageCriteriaTypeDef",
    "UsageDataSourceResultTypeDef",
    "UsageFeatureResultTypeDef",
    "UsageResourceResultTypeDef",
    "UsageStatisticsTypeDef",
    "UsageTopAccountResultTypeDef",
    "UsageTopAccountsResultTypeDef",
    "UserTypeDef",
    "VolumeDetailTypeDef",
    "VolumeMountTypeDef",
    "VolumeTypeDef",
    "VpcConfigTypeDef",
)

class AcceptAdministratorInvitationRequestTypeDef(TypedDict):
    DetectorId: str
    AdministratorId: str
    InvitationId: str

class AcceptInvitationRequestTypeDef(TypedDict):
    DetectorId: str
    MasterId: str
    InvitationId: str

class AccessControlListTypeDef(TypedDict):
    AllowsPublicReadAccess: NotRequired[bool]
    AllowsPublicWriteAccess: NotRequired[bool]

class AccessKeyDetailsTypeDef(TypedDict):
    AccessKeyId: NotRequired[str]
    PrincipalId: NotRequired[str]
    UserName: NotRequired[str]
    UserType: NotRequired[str]

class AccessKeyTypeDef(TypedDict):
    PrincipalId: NotRequired[str]
    UserName: NotRequired[str]
    UserType: NotRequired[str]

class AccountDetailTypeDef(TypedDict):
    AccountId: str
    Email: str

class FreeTrialFeatureConfigurationResultTypeDef(TypedDict):
    Name: NotRequired[FreeTrialFeatureResultType]
    FreeTrialDaysRemaining: NotRequired[int]

class BlockPublicAccessTypeDef(TypedDict):
    IgnorePublicAcls: NotRequired[bool]
    RestrictPublicBuckets: NotRequired[bool]
    BlockPublicAcls: NotRequired[bool]
    BlockPublicPolicy: NotRequired[bool]

class AccountStatisticsTypeDef(TypedDict):
    AccountId: NotRequired[str]
    LastGeneratedAt: NotRequired[datetime]
    TotalFindings: NotRequired[int]

class AccountTypeDef(TypedDict):
    Uid: str
    Name: NotRequired[str]

DnsRequestActionTypeDef = TypedDict(
    "DnsRequestActionTypeDef",
    {
        "Domain": NotRequired[str],
        "Protocol": NotRequired[str],
        "Blocked": NotRequired[bool],
        "DomainWithSuffix": NotRequired[str],
    },
)

class KubernetesPermissionCheckedDetailsTypeDef(TypedDict):
    Verb: NotRequired[str]
    Resource: NotRequired[str]
    Namespace: NotRequired[str]
    Allowed: NotRequired[bool]

class KubernetesRoleBindingDetailsTypeDef(TypedDict):
    Kind: NotRequired[str]
    Name: NotRequired[str]
    Uid: NotRequired[str]
    RoleRefName: NotRequired[str]
    RoleRefKind: NotRequired[str]

class KubernetesRoleDetailsTypeDef(TypedDict):
    Kind: NotRequired[str]
    Name: NotRequired[str]
    Uid: NotRequired[str]

class SessionTypeDef(TypedDict):
    Uid: NotRequired[str]
    MfaStatus: NotRequired[MfaStatusType]
    CreatedTime: NotRequired[datetime]
    Issuer: NotRequired[str]

class AddonDetailsTypeDef(TypedDict):
    AddonVersion: NotRequired[str]
    AddonStatus: NotRequired[str]

class AdminAccountTypeDef(TypedDict):
    AdminAccountId: NotRequired[str]
    AdminStatus: NotRequired[AdminStatusType]

class AdministratorTypeDef(TypedDict):
    AccountId: NotRequired[str]
    InvitationId: NotRequired[str]
    RelationshipStatus: NotRequired[str]
    InvitedAt: NotRequired[str]

class AgentDetailsTypeDef(TypedDict):
    Version: NotRequired[str]

ObservationsTypeDef = TypedDict(
    "ObservationsTypeDef",
    {
        "Text": NotRequired[List[str]],
    },
)

class ArchiveFindingsRequestTypeDef(TypedDict):
    DetectorId: str
    FindingIds: Sequence[str]

class AutonomousSystemTypeDef(TypedDict):
    Name: str
    Number: int

class DomainDetailsTypeDef(TypedDict):
    Domain: NotRequired[str]

class RemoteAccountDetailsTypeDef(TypedDict):
    AccountId: NotRequired[str]
    Affiliated: NotRequired[bool]

class BucketPolicyTypeDef(TypedDict):
    AllowsPublicReadAccess: NotRequired[bool]
    AllowsPublicWriteAccess: NotRequired[bool]

class CityTypeDef(TypedDict):
    CityName: NotRequired[str]

class CloudTrailConfigurationResultTypeDef(TypedDict):
    Status: DataSourceStatusType

class ConditionOutputTypeDef(TypedDict):
    Eq: NotRequired[List[str]]
    Neq: NotRequired[List[str]]
    Gt: NotRequired[int]
    Gte: NotRequired[int]
    Lt: NotRequired[int]
    Lte: NotRequired[int]
    Equals: NotRequired[List[str]]
    NotEquals: NotRequired[List[str]]
    GreaterThan: NotRequired[int]
    GreaterThanOrEqual: NotRequired[int]
    LessThan: NotRequired[int]
    LessThanOrEqual: NotRequired[int]

class ConditionTypeDef(TypedDict):
    Eq: NotRequired[Sequence[str]]
    Neq: NotRequired[Sequence[str]]
    Gt: NotRequired[int]
    Gte: NotRequired[int]
    Lt: NotRequired[int]
    Lte: NotRequired[int]
    Equals: NotRequired[Sequence[str]]
    NotEquals: NotRequired[Sequence[str]]
    GreaterThan: NotRequired[int]
    GreaterThanOrEqual: NotRequired[int]
    LessThan: NotRequired[int]
    LessThanOrEqual: NotRequired[int]

class ContainerInstanceDetailsTypeDef(TypedDict):
    CoveredContainerInstances: NotRequired[int]
    CompatibleContainerInstances: NotRequired[int]

class SecurityContextTypeDef(TypedDict):
    Privileged: NotRequired[bool]
    AllowPrivilegeEscalation: NotRequired[bool]

class VolumeMountTypeDef(TypedDict):
    Name: NotRequired[str]
    MountPath: NotRequired[str]

class CountryTypeDef(TypedDict):
    CountryCode: NotRequired[str]
    CountryName: NotRequired[str]

class FargateDetailsTypeDef(TypedDict):
    Issues: NotRequired[List[str]]
    ManagementType: NotRequired[ManagementTypeType]

class CoverageFilterConditionTypeDef(TypedDict):
    Equals: NotRequired[Sequence[str]]
    NotEquals: NotRequired[Sequence[str]]

class CoverageSortCriteriaTypeDef(TypedDict):
    AttributeName: NotRequired[CoverageSortKeyType]
    OrderBy: NotRequired[OrderByType]

class CoverageStatisticsTypeDef(TypedDict):
    CountByResourceType: NotRequired[Dict[ResourceTypeType, int]]
    CountByCoverageStatus: NotRequired[Dict[CoverageStatusType, int]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateIPSetRequestTypeDef(TypedDict):
    DetectorId: str
    Name: str
    Format: IpSetFormatType
    Location: str
    Activate: bool
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class UnprocessedAccountTypeDef(TypedDict):
    AccountId: str
    Result: str

class CreateS3BucketResourceOutputTypeDef(TypedDict):
    BucketName: NotRequired[str]
    ObjectPrefixes: NotRequired[List[str]]

class CreateS3BucketResourceTypeDef(TypedDict):
    BucketName: NotRequired[str]
    ObjectPrefixes: NotRequired[Sequence[str]]

class DestinationPropertiesTypeDef(TypedDict):
    DestinationArn: NotRequired[str]
    KmsKeyArn: NotRequired[str]

class CreateSampleFindingsRequestTypeDef(TypedDict):
    DetectorId: str
    FindingTypes: NotRequired[Sequence[str]]

class CreateThreatIntelSetRequestTypeDef(TypedDict):
    DetectorId: str
    Name: str
    Format: ThreatIntelSetFormatType
    Location: str
    Activate: bool
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class DNSLogsConfigurationResultTypeDef(TypedDict):
    Status: DataSourceStatusType

class FlowLogsConfigurationResultTypeDef(TypedDict):
    Status: DataSourceStatusType

class S3LogsConfigurationResultTypeDef(TypedDict):
    Status: DataSourceStatusType

class S3LogsConfigurationTypeDef(TypedDict):
    Enable: bool

class DataSourceFreeTrialTypeDef(TypedDict):
    FreeTrialDaysRemaining: NotRequired[int]

class DateStatisticsTypeDef(TypedDict):
    Date: NotRequired[datetime]
    LastGeneratedAt: NotRequired[datetime]
    Severity: NotRequired[float]
    TotalFindings: NotRequired[int]

class DeclineInvitationsRequestTypeDef(TypedDict):
    AccountIds: Sequence[str]

class DefaultServerSideEncryptionTypeDef(TypedDict):
    EncryptionType: NotRequired[str]
    KmsMasterKeyArn: NotRequired[str]

class DeleteDetectorRequestTypeDef(TypedDict):
    DetectorId: str

class DeleteFilterRequestTypeDef(TypedDict):
    DetectorId: str
    FilterName: str

class DeleteIPSetRequestTypeDef(TypedDict):
    DetectorId: str
    IpSetId: str

class DeleteInvitationsRequestTypeDef(TypedDict):
    AccountIds: Sequence[str]

class DeleteMalwareProtectionPlanRequestTypeDef(TypedDict):
    MalwareProtectionPlanId: str

class DeleteMembersRequestTypeDef(TypedDict):
    DetectorId: str
    AccountIds: Sequence[str]

class DeletePublishingDestinationRequestTypeDef(TypedDict):
    DetectorId: str
    DestinationId: str

class DeleteThreatIntelSetRequestTypeDef(TypedDict):
    DetectorId: str
    ThreatIntelSetId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class SortCriteriaTypeDef(TypedDict):
    AttributeName: NotRequired[str]
    OrderBy: NotRequired[OrderByType]

class DescribeOrganizationConfigurationRequestTypeDef(TypedDict):
    DetectorId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribePublishingDestinationRequestTypeDef(TypedDict):
    DetectorId: str
    DestinationId: str

class DestinationTypeDef(TypedDict):
    DestinationId: str
    DestinationType: Literal["S3"]
    Status: PublishingStatusType

class DetectorAdditionalConfigurationResultTypeDef(TypedDict):
    Name: NotRequired[FeatureAdditionalConfigurationType]
    Status: NotRequired[FeatureStatusType]
    UpdatedAt: NotRequired[datetime]

class DetectorAdditionalConfigurationTypeDef(TypedDict):
    Name: NotRequired[FeatureAdditionalConfigurationType]
    Status: NotRequired[FeatureStatusType]

class DisableOrganizationAdminAccountRequestTypeDef(TypedDict):
    AdminAccountId: str

class DisassociateFromAdministratorAccountRequestTypeDef(TypedDict):
    DetectorId: str

class DisassociateFromMasterAccountRequestTypeDef(TypedDict):
    DetectorId: str

class DisassociateMembersRequestTypeDef(TypedDict):
    DetectorId: str
    AccountIds: Sequence[str]

class VolumeDetailTypeDef(TypedDict):
    VolumeArn: NotRequired[str]
    VolumeType: NotRequired[str]
    DeviceName: NotRequired[str]
    VolumeSizeInGB: NotRequired[int]
    EncryptionType: NotRequired[str]
    SnapshotArn: NotRequired[str]
    KmsKeyArn: NotRequired[str]

class EbsVolumesResultTypeDef(TypedDict):
    Status: NotRequired[DataSourceStatusType]
    Reason: NotRequired[str]

class IamInstanceProfileTypeDef(TypedDict):
    Arn: NotRequired[str]
    Id: NotRequired[str]

class ProductCodeTypeDef(TypedDict):
    Code: NotRequired[str]
    ProductType: NotRequired[str]

class PrivateIpAddressDetailsTypeDef(TypedDict):
    PrivateDnsName: NotRequired[str]
    PrivateIpAddress: NotRequired[str]

class SecurityGroupTypeDef(TypedDict):
    GroupId: NotRequired[str]
    GroupName: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class EnableOrganizationAdminAccountRequestTypeDef(TypedDict):
    AdminAccountId: str

class ThreatIntelligenceDetailTypeDef(TypedDict):
    ThreatListName: NotRequired[str]
    ThreatNames: NotRequired[List[str]]
    ThreatFileSha256: NotRequired[str]

class FilterConditionTypeDef(TypedDict):
    EqualsValue: NotRequired[str]
    GreaterThan: NotRequired[int]
    LessThan: NotRequired[int]

class FindingTypeStatisticsTypeDef(TypedDict):
    FindingType: NotRequired[str]
    LastGeneratedAt: NotRequired[datetime]
    TotalFindings: NotRequired[int]

class ResourceStatisticsTypeDef(TypedDict):
    AccountId: NotRequired[str]
    LastGeneratedAt: NotRequired[datetime]
    ResourceId: NotRequired[str]
    ResourceType: NotRequired[str]
    TotalFindings: NotRequired[int]

class SeverityStatisticsTypeDef(TypedDict):
    LastGeneratedAt: NotRequired[datetime]
    Severity: NotRequired[float]
    TotalFindings: NotRequired[int]

class GeoLocationTypeDef(TypedDict):
    Lat: NotRequired[float]
    Lon: NotRequired[float]

class GetAdministratorAccountRequestTypeDef(TypedDict):
    DetectorId: str

class GetDetectorRequestTypeDef(TypedDict):
    DetectorId: str

class GetFilterRequestTypeDef(TypedDict):
    DetectorId: str
    FilterName: str

class GetIPSetRequestTypeDef(TypedDict):
    DetectorId: str
    IpSetId: str

class GetMalwareProtectionPlanRequestTypeDef(TypedDict):
    MalwareProtectionPlanId: str

class MalwareProtectionPlanStatusReasonTypeDef(TypedDict):
    Code: NotRequired[str]
    Message: NotRequired[str]

class GetMalwareScanSettingsRequestTypeDef(TypedDict):
    DetectorId: str

class GetMasterAccountRequestTypeDef(TypedDict):
    DetectorId: str

class MasterTypeDef(TypedDict):
    AccountId: NotRequired[str]
    InvitationId: NotRequired[str]
    RelationshipStatus: NotRequired[str]
    InvitedAt: NotRequired[str]

class GetMemberDetectorsRequestTypeDef(TypedDict):
    DetectorId: str
    AccountIds: Sequence[str]

class GetMembersRequestTypeDef(TypedDict):
    DetectorId: str
    AccountIds: Sequence[str]

class MemberTypeDef(TypedDict):
    AccountId: str
    MasterId: str
    Email: str
    RelationshipStatus: str
    UpdatedAt: str
    DetectorId: NotRequired[str]
    InvitedAt: NotRequired[str]
    AdministratorId: NotRequired[str]

class GetRemainingFreeTrialDaysRequestTypeDef(TypedDict):
    DetectorId: str
    AccountIds: NotRequired[Sequence[str]]

class GetThreatIntelSetRequestTypeDef(TypedDict):
    DetectorId: str
    ThreatIntelSetId: str

class UsageCriteriaTypeDef(TypedDict):
    AccountIds: NotRequired[Sequence[str]]
    DataSources: NotRequired[Sequence[DataSourceType]]
    Resources: NotRequired[Sequence[str]]
    Features: NotRequired[Sequence[UsageFeatureType]]

class HighestSeverityThreatDetailsTypeDef(TypedDict):
    Severity: NotRequired[str]
    ThreatName: NotRequired[str]
    Count: NotRequired[int]

class HostPathTypeDef(TypedDict):
    Path: NotRequired[str]

class ImpersonatedUserTypeDef(TypedDict):
    Username: NotRequired[str]
    Groups: NotRequired[List[str]]

class IndicatorTypeDef(TypedDict):
    Key: IndicatorTypeType
    Values: NotRequired[List[str]]
    Title: NotRequired[str]

class InvitationTypeDef(TypedDict):
    AccountId: NotRequired[str]
    InvitationId: NotRequired[str]
    RelationshipStatus: NotRequired[str]
    InvitedAt: NotRequired[str]

class InviteMembersRequestTypeDef(TypedDict):
    DetectorId: str
    AccountIds: Sequence[str]
    DisableEmailNotification: NotRequired[bool]
    Message: NotRequired[str]

class ItemPathTypeDef(TypedDict):
    NestedItemPath: NotRequired[str]
    Hash: NotRequired[str]

class KubernetesAuditLogsConfigurationResultTypeDef(TypedDict):
    Status: DataSourceStatusType

class KubernetesAuditLogsConfigurationTypeDef(TypedDict):
    Enable: bool

class LineageObjectTypeDef(TypedDict):
    StartTime: NotRequired[datetime]
    NamespacePid: NotRequired[int]
    UserId: NotRequired[int]
    Name: NotRequired[str]
    Pid: NotRequired[int]
    Uuid: NotRequired[str]
    ExecutablePath: NotRequired[str]
    Euid: NotRequired[int]
    ParentUuid: NotRequired[str]

class ListDetectorsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListFiltersRequestTypeDef(TypedDict):
    DetectorId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListIPSetsRequestTypeDef(TypedDict):
    DetectorId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListInvitationsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListMalwareProtectionPlansRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]

class MalwareProtectionPlanSummaryTypeDef(TypedDict):
    MalwareProtectionPlanId: NotRequired[str]

class ListMembersRequestTypeDef(TypedDict):
    DetectorId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    OnlyAssociated: NotRequired[str]

class ListOrganizationAdminAccountsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListPublishingDestinationsRequestTypeDef(TypedDict):
    DetectorId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class ListThreatIntelSetsRequestTypeDef(TypedDict):
    DetectorId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class LocalIpDetailsTypeDef(TypedDict):
    IpAddressV4: NotRequired[str]
    IpAddressV6: NotRequired[str]

class LocalPortDetailsTypeDef(TypedDict):
    Port: NotRequired[int]
    PortName: NotRequired[str]

class LoginAttributeTypeDef(TypedDict):
    User: NotRequired[str]
    Application: NotRequired[str]
    FailedLoginAttempts: NotRequired[int]
    SuccessfulLoginAttempts: NotRequired[int]

class ScanEc2InstanceWithFindingsTypeDef(TypedDict):
    EbsVolumes: NotRequired[bool]

class MalwareProtectionPlanTaggingActionTypeDef(TypedDict):
    Status: NotRequired[MalwareProtectionPlanTaggingActionStatusType]

class MemberAdditionalConfigurationResultTypeDef(TypedDict):
    Name: NotRequired[OrgFeatureAdditionalConfigurationType]
    Status: NotRequired[FeatureStatusType]
    UpdatedAt: NotRequired[datetime]

class MemberAdditionalConfigurationTypeDef(TypedDict):
    Name: NotRequired[OrgFeatureAdditionalConfigurationType]
    Status: NotRequired[FeatureStatusType]

class RemotePortDetailsTypeDef(TypedDict):
    Port: NotRequired[int]
    PortName: NotRequired[str]

class NetworkConnectionTypeDef(TypedDict):
    Direction: NetworkDirectionType

class NetworkGeoLocationTypeDef(TypedDict):
    City: str
    Country: str
    Latitude: float
    Longitude: float

class OrganizationAdditionalConfigurationResultTypeDef(TypedDict):
    Name: NotRequired[OrgFeatureAdditionalConfigurationType]
    AutoEnable: NotRequired[OrgFeatureStatusType]

class OrganizationAdditionalConfigurationTypeDef(TypedDict):
    Name: NotRequired[OrgFeatureAdditionalConfigurationType]
    AutoEnable: NotRequired[OrgFeatureStatusType]

class OrganizationS3LogsConfigurationResultTypeDef(TypedDict):
    AutoEnable: bool

class OrganizationS3LogsConfigurationTypeDef(TypedDict):
    AutoEnable: bool

class OrganizationEbsVolumesResultTypeDef(TypedDict):
    AutoEnable: NotRequired[bool]

class OrganizationEbsVolumesTypeDef(TypedDict):
    AutoEnable: NotRequired[bool]

class OrganizationFeatureStatisticsAdditionalConfigurationTypeDef(TypedDict):
    Name: NotRequired[OrgFeatureAdditionalConfigurationType]
    EnabledAccountsCount: NotRequired[int]

class OrganizationKubernetesAuditLogsConfigurationResultTypeDef(TypedDict):
    AutoEnable: bool

class OrganizationKubernetesAuditLogsConfigurationTypeDef(TypedDict):
    AutoEnable: bool

class OrganizationTypeDef(TypedDict):
    Asn: NotRequired[str]
    AsnOrg: NotRequired[str]
    Isp: NotRequired[str]
    Org: NotRequired[str]

class OwnerTypeDef(TypedDict):
    Id: NotRequired[str]

class PublicAccessConfigurationTypeDef(TypedDict):
    PublicAclAccess: NotRequired[PublicAccessStatusType]
    PublicPolicyAccess: NotRequired[PublicAccessStatusType]
    PublicAclIgnoreBehavior: NotRequired[PublicAclIgnoreBehaviorType]
    PublicBucketRestrictBehavior: NotRequired[PublicBucketRestrictBehaviorType]

class RdsDbUserDetailsTypeDef(TypedDict):
    User: NotRequired[str]
    Application: NotRequired[str]
    Database: NotRequired[str]
    Ssl: NotRequired[str]
    AuthMethod: NotRequired[str]

class S3ObjectTypeDef(TypedDict):
    ETag: NotRequired[str]
    Key: NotRequired[str]
    VersionId: NotRequired[str]

class ResourceDetailsTypeDef(TypedDict):
    InstanceArn: NotRequired[str]

class S3ObjectDetailTypeDef(TypedDict):
    ObjectArn: NotRequired[str]
    Key: NotRequired[str]
    ETag: NotRequired[str]
    Hash: NotRequired[str]
    VersionId: NotRequired[str]

class ScanConditionPairTypeDef(TypedDict):
    Key: str
    Value: NotRequired[str]

class ScannedItemCountTypeDef(TypedDict):
    TotalGb: NotRequired[int]
    Files: NotRequired[int]
    Volumes: NotRequired[int]

class ThreatsDetectedItemCountTypeDef(TypedDict):
    Files: NotRequired[int]

class ScanFilePathTypeDef(TypedDict):
    FilePath: NotRequired[str]
    VolumeArn: NotRequired[str]
    Hash: NotRequired[str]
    FileName: NotRequired[str]

class ScanResultDetailsTypeDef(TypedDict):
    ScanResult: NotRequired[ScanResultType]

class TriggerDetailsTypeDef(TypedDict):
    GuardDutyFindingId: NotRequired[str]
    Description: NotRequired[str]

ServiceAdditionalInfoTypeDef = TypedDict(
    "ServiceAdditionalInfoTypeDef",
    {
        "Value": NotRequired[str],
        "Type": NotRequired[str],
    },
)

class StartMalwareScanRequestTypeDef(TypedDict):
    ResourceArn: str

class StartMonitoringMembersRequestTypeDef(TypedDict):
    DetectorId: str
    AccountIds: Sequence[str]

class StopMonitoringMembersRequestTypeDef(TypedDict):
    DetectorId: str
    AccountIds: Sequence[str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class TotalTypeDef(TypedDict):
    Amount: NotRequired[str]
    Unit: NotRequired[str]

class UnarchiveFindingsRequestTypeDef(TypedDict):
    DetectorId: str
    FindingIds: Sequence[str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateFindingsFeedbackRequestTypeDef(TypedDict):
    DetectorId: str
    FindingIds: Sequence[str]
    Feedback: FeedbackType
    Comments: NotRequired[str]

class UpdateIPSetRequestTypeDef(TypedDict):
    DetectorId: str
    IpSetId: str
    Name: NotRequired[str]
    Location: NotRequired[str]
    Activate: NotRequired[bool]

class UpdateS3BucketResourceTypeDef(TypedDict):
    ObjectPrefixes: NotRequired[Sequence[str]]

class UpdateThreatIntelSetRequestTypeDef(TypedDict):
    DetectorId: str
    ThreatIntelSetId: str
    Name: NotRequired[str]
    Location: NotRequired[str]
    Activate: NotRequired[bool]

class CreateMembersRequestTypeDef(TypedDict):
    DetectorId: str
    AccountDetails: Sequence[AccountDetailTypeDef]

class AccountLevelPermissionsTypeDef(TypedDict):
    BlockPublicAccess: NotRequired[BlockPublicAccessTypeDef]

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Name": str,
        "Uid": str,
        "Type": str,
        "CredentialUid": NotRequired[str],
        "Account": NotRequired[AccountTypeDef],
    },
)

class CoverageEksClusterDetailsTypeDef(TypedDict):
    ClusterName: NotRequired[str]
    CoveredNodes: NotRequired[int]
    CompatibleNodes: NotRequired[int]
    AddonDetails: NotRequired[AddonDetailsTypeDef]
    ManagementType: NotRequired[ManagementTypeType]

class CoverageEc2InstanceDetailsTypeDef(TypedDict):
    InstanceId: NotRequired[str]
    InstanceType: NotRequired[str]
    ClusterArn: NotRequired[str]
    AgentDetails: NotRequired[AgentDetailsTypeDef]
    ManagementType: NotRequired[ManagementTypeType]

class AnomalyObjectTypeDef(TypedDict):
    ProfileType: NotRequired[Literal["FREQUENCY"]]
    ProfileSubtype: NotRequired[ProfileSubtypeType]
    Observations: NotRequired[ObservationsTypeDef]

class BucketLevelPermissionsTypeDef(TypedDict):
    AccessControlList: NotRequired[AccessControlListTypeDef]
    BucketPolicy: NotRequired[BucketPolicyTypeDef]
    BlockPublicAccess: NotRequired[BlockPublicAccessTypeDef]

class FindingCriteriaOutputTypeDef(TypedDict):
    Criterion: NotRequired[Dict[str, ConditionOutputTypeDef]]

class FindingCriteriaTypeDef(TypedDict):
    Criterion: NotRequired[Mapping[str, ConditionTypeDef]]

class ContainerTypeDef(TypedDict):
    ContainerRuntime: NotRequired[str]
    Id: NotRequired[str]
    Name: NotRequired[str]
    Image: NotRequired[str]
    ImagePrefix: NotRequired[str]
    VolumeMounts: NotRequired[List[VolumeMountTypeDef]]
    SecurityContext: NotRequired[SecurityContextTypeDef]

class CoverageEcsClusterDetailsTypeDef(TypedDict):
    ClusterName: NotRequired[str]
    FargateDetails: NotRequired[FargateDetailsTypeDef]
    ContainerInstanceDetails: NotRequired[ContainerInstanceDetailsTypeDef]

class CoverageFilterCriterionTypeDef(TypedDict):
    CriterionKey: NotRequired[CoverageFilterCriterionKeyType]
    FilterCondition: NotRequired[CoverageFilterConditionTypeDef]

class CreateFilterResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIPSetResponseTypeDef(TypedDict):
    IpSetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMalwareProtectionPlanResponseTypeDef(TypedDict):
    MalwareProtectionPlanId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePublishingDestinationResponseTypeDef(TypedDict):
    DestinationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateThreatIntelSetResponseTypeDef(TypedDict):
    ThreatIntelSetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAdministratorAccountResponseTypeDef(TypedDict):
    Administrator: AdministratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCoverageStatisticsResponseTypeDef(TypedDict):
    CoverageStatistics: CoverageStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIPSetResponseTypeDef(TypedDict):
    Name: str
    Format: IpSetFormatType
    Location: str
    Status: IpSetStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetInvitationsCountResponseTypeDef(TypedDict):
    InvitationsCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetThreatIntelSetResponseTypeDef(TypedDict):
    Name: str
    Format: ThreatIntelSetFormatType
    Location: str
    Status: ThreatIntelSetStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDetectorsResponseTypeDef(TypedDict):
    DetectorIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListFiltersResponseTypeDef(TypedDict):
    FilterNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListFindingsResponseTypeDef(TypedDict):
    FindingIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListIPSetsResponseTypeDef(TypedDict):
    IpSetIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListOrganizationAdminAccountsResponseTypeDef(TypedDict):
    AdminAccounts: List[AdminAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListThreatIntelSetsResponseTypeDef(TypedDict):
    ThreatIntelSetIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class StartMalwareScanResponseTypeDef(TypedDict):
    ScanId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFilterResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMembersResponseTypeDef(TypedDict):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeclineInvitationsResponseTypeDef(TypedDict):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInvitationsResponseTypeDef(TypedDict):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMembersResponseTypeDef(TypedDict):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateMembersResponseTypeDef(TypedDict):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InviteMembersResponseTypeDef(TypedDict):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartMonitoringMembersResponseTypeDef(TypedDict):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StopMonitoringMembersResponseTypeDef(TypedDict):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMemberDetectorsResponseTypeDef(TypedDict):
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProtectedResourceOutputTypeDef(TypedDict):
    S3Bucket: NotRequired[CreateS3BucketResourceOutputTypeDef]

class CreateProtectedResourceTypeDef(TypedDict):
    S3Bucket: NotRequired[CreateS3BucketResourceTypeDef]

class CreatePublishingDestinationRequestTypeDef(TypedDict):
    DetectorId: str
    DestinationType: Literal["S3"]
    DestinationProperties: DestinationPropertiesTypeDef
    ClientToken: NotRequired[str]

class DescribePublishingDestinationResponseTypeDef(TypedDict):
    DestinationId: str
    DestinationType: Literal["S3"]
    Status: PublishingStatusType
    PublishingFailureStartTimestamp: int
    DestinationProperties: DestinationPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePublishingDestinationRequestTypeDef(TypedDict):
    DetectorId: str
    DestinationId: str
    DestinationProperties: NotRequired[DestinationPropertiesTypeDef]

class KubernetesDataSourceFreeTrialTypeDef(TypedDict):
    AuditLogs: NotRequired[DataSourceFreeTrialTypeDef]

class MalwareProtectionDataSourceFreeTrialTypeDef(TypedDict):
    ScanEc2InstanceWithFindings: NotRequired[DataSourceFreeTrialTypeDef]

class ListDetectorsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFiltersRequestPaginateTypeDef(TypedDict):
    DetectorId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIPSetsRequestPaginateTypeDef(TypedDict):
    DetectorId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListInvitationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMembersRequestPaginateTypeDef(TypedDict):
    DetectorId: str
    OnlyAssociated: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOrganizationAdminAccountsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListThreatIntelSetsRequestPaginateTypeDef(TypedDict):
    DetectorId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetFindingsRequestTypeDef(TypedDict):
    DetectorId: str
    FindingIds: Sequence[str]
    SortCriteria: NotRequired[SortCriteriaTypeDef]

class ListPublishingDestinationsResponseTypeDef(TypedDict):
    Destinations: List[DestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DetectorFeatureConfigurationResultTypeDef(TypedDict):
    Name: NotRequired[DetectorFeatureResultType]
    Status: NotRequired[FeatureStatusType]
    UpdatedAt: NotRequired[datetime]
    AdditionalConfiguration: NotRequired[List[DetectorAdditionalConfigurationResultTypeDef]]

class DetectorFeatureConfigurationTypeDef(TypedDict):
    Name: NotRequired[DetectorFeatureType]
    Status: NotRequired[FeatureStatusType]
    AdditionalConfiguration: NotRequired[Sequence[DetectorAdditionalConfigurationTypeDef]]

class EbsVolumeDetailsTypeDef(TypedDict):
    ScannedVolumeDetails: NotRequired[List[VolumeDetailTypeDef]]
    SkippedVolumeDetails: NotRequired[List[VolumeDetailTypeDef]]

class ScanEc2InstanceWithFindingsResultTypeDef(TypedDict):
    EbsVolumes: NotRequired[EbsVolumesResultTypeDef]

class Ec2InstanceTypeDef(TypedDict):
    AvailabilityZone: NotRequired[str]
    ImageDescription: NotRequired[str]
    InstanceState: NotRequired[str]
    IamInstanceProfile: NotRequired[IamInstanceProfileTypeDef]
    InstanceType: NotRequired[str]
    OutpostArn: NotRequired[str]
    Platform: NotRequired[str]
    ProductCodes: NotRequired[List[ProductCodeTypeDef]]
    Ec2NetworkInterfaceUids: NotRequired[List[str]]

class Ec2NetworkInterfaceTypeDef(TypedDict):
    Ipv6Addresses: NotRequired[List[str]]
    PrivateIpAddresses: NotRequired[List[PrivateIpAddressDetailsTypeDef]]
    PublicIp: NotRequired[str]
    SecurityGroups: NotRequired[List[SecurityGroupTypeDef]]
    SubNetId: NotRequired[str]
    VpcId: NotRequired[str]

class NetworkInterfaceTypeDef(TypedDict):
    Ipv6Addresses: NotRequired[List[str]]
    NetworkInterfaceId: NotRequired[str]
    PrivateDnsName: NotRequired[str]
    PrivateIpAddress: NotRequired[str]
    PrivateIpAddresses: NotRequired[List[PrivateIpAddressDetailsTypeDef]]
    PublicDnsName: NotRequired[str]
    PublicIp: NotRequired[str]
    SecurityGroups: NotRequired[List[SecurityGroupTypeDef]]
    SubnetId: NotRequired[str]
    VpcId: NotRequired[str]

class VpcConfigTypeDef(TypedDict):
    SubnetIds: NotRequired[List[str]]
    VpcId: NotRequired[str]
    SecurityGroups: NotRequired[List[SecurityGroupTypeDef]]

class EksClusterDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    Arn: NotRequired[str]
    VpcId: NotRequired[str]
    Status: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    CreatedAt: NotRequired[datetime]

class RdsDbInstanceDetailsTypeDef(TypedDict):
    DbInstanceIdentifier: NotRequired[str]
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    DbClusterIdentifier: NotRequired[str]
    DbInstanceArn: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]

class RdsLimitlessDbDetailsTypeDef(TypedDict):
    DbShardGroupIdentifier: NotRequired[str]
    DbShardGroupResourceId: NotRequired[str]
    DbShardGroupArn: NotRequired[str]
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    DbClusterIdentifier: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]

class EvidenceTypeDef(TypedDict):
    ThreatIntelligenceDetails: NotRequired[List[ThreatIntelligenceDetailTypeDef]]

class FilterCriterionTypeDef(TypedDict):
    CriterionKey: NotRequired[CriterionKeyType]
    FilterCondition: NotRequired[FilterConditionTypeDef]

class FindingStatisticsTypeDef(TypedDict):
    CountBySeverity: NotRequired[Dict[str, int]]
    GroupedByAccount: NotRequired[List[AccountStatisticsTypeDef]]
    GroupedByDate: NotRequired[List[DateStatisticsTypeDef]]
    GroupedByFindingType: NotRequired[List[FindingTypeStatisticsTypeDef]]
    GroupedByResource: NotRequired[List[ResourceStatisticsTypeDef]]
    GroupedBySeverity: NotRequired[List[SeverityStatisticsTypeDef]]

class GetMasterAccountResponseTypeDef(TypedDict):
    Master: MasterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMembersResponseTypeDef(TypedDict):
    Members: List[MemberTypeDef]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMembersResponseTypeDef(TypedDict):
    Members: List[MemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetUsageStatisticsRequestTypeDef(TypedDict):
    DetectorId: str
    UsageStatisticType: UsageStatisticTypeType
    UsageCriteria: UsageCriteriaTypeDef
    Unit: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class VolumeTypeDef(TypedDict):
    Name: NotRequired[str]
    HostPath: NotRequired[HostPathTypeDef]

class KubernetesUserDetailsTypeDef(TypedDict):
    Username: NotRequired[str]
    Uid: NotRequired[str]
    Groups: NotRequired[List[str]]
    SessionName: NotRequired[List[str]]
    ImpersonatedUser: NotRequired[ImpersonatedUserTypeDef]

SignalTypeDef = TypedDict(
    "SignalTypeDef",
    {
        "Uid": str,
        "Type": SignalTypeType,
        "Name": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "FirstSeenAt": datetime,
        "LastSeenAt": datetime,
        "Count": int,
        "Description": NotRequired[str],
        "Severity": NotRequired[float],
        "ResourceUids": NotRequired[List[str]],
        "ActorIds": NotRequired[List[str]],
        "EndpointIds": NotRequired[List[str]],
        "SignalIndicators": NotRequired[List[IndicatorTypeDef]],
    },
)

class ListInvitationsResponseTypeDef(TypedDict):
    Invitations: List[InvitationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ThreatTypeDef(TypedDict):
    Name: NotRequired[str]
    Source: NotRequired[str]
    ItemPaths: NotRequired[List[ItemPathTypeDef]]

class KubernetesConfigurationResultTypeDef(TypedDict):
    AuditLogs: KubernetesAuditLogsConfigurationResultTypeDef

class KubernetesConfigurationTypeDef(TypedDict):
    AuditLogs: KubernetesAuditLogsConfigurationTypeDef

class ProcessDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    ExecutablePath: NotRequired[str]
    ExecutableSha256: NotRequired[str]
    NamespacePid: NotRequired[int]
    Pwd: NotRequired[str]
    Pid: NotRequired[int]
    StartTime: NotRequired[datetime]
    Uuid: NotRequired[str]
    ParentUuid: NotRequired[str]
    User: NotRequired[str]
    UserId: NotRequired[int]
    Euid: NotRequired[int]
    Lineage: NotRequired[List[LineageObjectTypeDef]]

class ListMalwareProtectionPlansResponseTypeDef(TypedDict):
    MalwareProtectionPlans: List[MalwareProtectionPlanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class MalwareProtectionConfigurationTypeDef(TypedDict):
    ScanEc2InstanceWithFindings: NotRequired[ScanEc2InstanceWithFindingsTypeDef]

class MalwareProtectionPlanActionsTypeDef(TypedDict):
    Tagging: NotRequired[MalwareProtectionPlanTaggingActionTypeDef]

class MemberFeaturesConfigurationResultTypeDef(TypedDict):
    Name: NotRequired[OrgFeatureType]
    Status: NotRequired[FeatureStatusType]
    UpdatedAt: NotRequired[datetime]
    AdditionalConfiguration: NotRequired[List[MemberAdditionalConfigurationResultTypeDef]]

class MemberFeaturesConfigurationTypeDef(TypedDict):
    Name: NotRequired[OrgFeatureType]
    Status: NotRequired[FeatureStatusType]
    AdditionalConfiguration: NotRequired[Sequence[MemberAdditionalConfigurationTypeDef]]

class NetworkEndpointTypeDef(TypedDict):
    Id: str
    Ip: NotRequired[str]
    Domain: NotRequired[str]
    Port: NotRequired[int]
    Location: NotRequired[NetworkGeoLocationTypeDef]
    AutonomousSystem: NotRequired[AutonomousSystemTypeDef]
    Connection: NotRequired[NetworkConnectionTypeDef]

class OrganizationFeatureConfigurationResultTypeDef(TypedDict):
    Name: NotRequired[OrgFeatureType]
    AutoEnable: NotRequired[OrgFeatureStatusType]
    AdditionalConfiguration: NotRequired[List[OrganizationAdditionalConfigurationResultTypeDef]]

class OrganizationFeatureConfigurationTypeDef(TypedDict):
    Name: NotRequired[OrgFeatureType]
    AutoEnable: NotRequired[OrgFeatureStatusType]
    AdditionalConfiguration: NotRequired[Sequence[OrganizationAdditionalConfigurationTypeDef]]

class OrganizationScanEc2InstanceWithFindingsResultTypeDef(TypedDict):
    EbsVolumes: NotRequired[OrganizationEbsVolumesResultTypeDef]

class OrganizationScanEc2InstanceWithFindingsTypeDef(TypedDict):
    EbsVolumes: NotRequired[OrganizationEbsVolumesTypeDef]

class OrganizationFeatureStatisticsTypeDef(TypedDict):
    Name: NotRequired[OrgFeatureType]
    EnabledAccountsCount: NotRequired[int]
    AdditionalConfiguration: NotRequired[
        List[OrganizationFeatureStatisticsAdditionalConfigurationTypeDef]
    ]

class OrganizationKubernetesConfigurationResultTypeDef(TypedDict):
    AuditLogs: OrganizationKubernetesAuditLogsConfigurationResultTypeDef

class OrganizationKubernetesConfigurationTypeDef(TypedDict):
    AuditLogs: OrganizationKubernetesAuditLogsConfigurationTypeDef

class RemoteIpDetailsTypeDef(TypedDict):
    City: NotRequired[CityTypeDef]
    Country: NotRequired[CountryTypeDef]
    GeoLocation: NotRequired[GeoLocationTypeDef]
    IpAddressV4: NotRequired[str]
    IpAddressV6: NotRequired[str]
    Organization: NotRequired[OrganizationTypeDef]

class S3BucketTypeDef(TypedDict):
    OwnerId: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    EncryptionType: NotRequired[str]
    EncryptionKeyArn: NotRequired[str]
    EffectivePermission: NotRequired[str]
    PublicReadAccess: NotRequired[PublicAccessStatusType]
    PublicWriteAccess: NotRequired[PublicAccessStatusType]
    AccountPublicAccess: NotRequired[PublicAccessConfigurationTypeDef]
    BucketPublicAccess: NotRequired[PublicAccessConfigurationTypeDef]
    S3ObjectUids: NotRequired[List[str]]

class ScanConditionOutputTypeDef(TypedDict):
    MapEquals: List[ScanConditionPairTypeDef]

class ScanConditionTypeDef(TypedDict):
    MapEquals: Sequence[ScanConditionPairTypeDef]

class ScanThreatNameTypeDef(TypedDict):
    Name: NotRequired[str]
    Severity: NotRequired[str]
    ItemCount: NotRequired[int]
    FilePaths: NotRequired[List[ScanFilePathTypeDef]]

class ScanTypeDef(TypedDict):
    DetectorId: NotRequired[str]
    AdminDetectorId: NotRequired[str]
    ScanId: NotRequired[str]
    ScanStatus: NotRequired[ScanStatusType]
    FailureReason: NotRequired[str]
    ScanStartTime: NotRequired[datetime]
    ScanEndTime: NotRequired[datetime]
    TriggerDetails: NotRequired[TriggerDetailsTypeDef]
    ResourceDetails: NotRequired[ResourceDetailsTypeDef]
    ScanResultDetails: NotRequired[ScanResultDetailsTypeDef]
    AccountId: NotRequired[str]
    TotalBytes: NotRequired[int]
    FileCount: NotRequired[int]
    AttachedVolumes: NotRequired[List[VolumeDetailTypeDef]]
    ScanType: NotRequired[ScanTypeType]

class UsageAccountResultTypeDef(TypedDict):
    AccountId: NotRequired[str]
    Total: NotRequired[TotalTypeDef]

class UsageDataSourceResultTypeDef(TypedDict):
    DataSource: NotRequired[DataSourceType]
    Total: NotRequired[TotalTypeDef]

class UsageFeatureResultTypeDef(TypedDict):
    Feature: NotRequired[UsageFeatureType]
    Total: NotRequired[TotalTypeDef]

class UsageResourceResultTypeDef(TypedDict):
    Resource: NotRequired[str]
    Total: NotRequired[TotalTypeDef]

class UsageTopAccountResultTypeDef(TypedDict):
    AccountId: NotRequired[str]
    Total: NotRequired[TotalTypeDef]

class UpdateProtectedResourceTypeDef(TypedDict):
    S3Bucket: NotRequired[UpdateS3BucketResourceTypeDef]

class ActorTypeDef(TypedDict):
    Id: str
    User: NotRequired[UserTypeDef]
    Session: NotRequired[SessionTypeDef]

class AnomalyUnusualTypeDef(TypedDict):
    Behavior: NotRequired[Dict[str, Dict[str, AnomalyObjectTypeDef]]]

class PermissionConfigurationTypeDef(TypedDict):
    BucketLevelPermissions: NotRequired[BucketLevelPermissionsTypeDef]
    AccountLevelPermissions: NotRequired[AccountLevelPermissionsTypeDef]

class GetFilterResponseTypeDef(TypedDict):
    Name: str
    Description: str
    Action: FilterActionType
    Rank: int
    FindingCriteria: FindingCriteriaOutputTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

FindingCriteriaUnionTypeDef = Union[FindingCriteriaTypeDef, FindingCriteriaOutputTypeDef]

class CoverageResourceDetailsTypeDef(TypedDict):
    EksClusterDetails: NotRequired[CoverageEksClusterDetailsTypeDef]
    ResourceType: NotRequired[ResourceTypeType]
    EcsClusterDetails: NotRequired[CoverageEcsClusterDetailsTypeDef]
    Ec2InstanceDetails: NotRequired[CoverageEc2InstanceDetailsTypeDef]

class CoverageFilterCriteriaTypeDef(TypedDict):
    FilterCriterion: NotRequired[Sequence[CoverageFilterCriterionTypeDef]]

CreateProtectedResourceUnionTypeDef = Union[
    CreateProtectedResourceTypeDef, CreateProtectedResourceOutputTypeDef
]

class DataSourcesFreeTrialTypeDef(TypedDict):
    CloudTrail: NotRequired[DataSourceFreeTrialTypeDef]
    DnsLogs: NotRequired[DataSourceFreeTrialTypeDef]
    FlowLogs: NotRequired[DataSourceFreeTrialTypeDef]
    S3Logs: NotRequired[DataSourceFreeTrialTypeDef]
    Kubernetes: NotRequired[KubernetesDataSourceFreeTrialTypeDef]
    MalwareProtection: NotRequired[MalwareProtectionDataSourceFreeTrialTypeDef]

class MalwareProtectionConfigurationResultTypeDef(TypedDict):
    ScanEc2InstanceWithFindings: NotRequired[ScanEc2InstanceWithFindingsResultTypeDef]
    ServiceRole: NotRequired[str]

class InstanceDetailsTypeDef(TypedDict):
    AvailabilityZone: NotRequired[str]
    IamInstanceProfile: NotRequired[IamInstanceProfileTypeDef]
    ImageDescription: NotRequired[str]
    ImageId: NotRequired[str]
    InstanceId: NotRequired[str]
    InstanceState: NotRequired[str]
    InstanceType: NotRequired[str]
    OutpostArn: NotRequired[str]
    LaunchTime: NotRequired[str]
    NetworkInterfaces: NotRequired[List[NetworkInterfaceTypeDef]]
    Platform: NotRequired[str]
    ProductCodes: NotRequired[List[ProductCodeTypeDef]]
    Tags: NotRequired[List[TagTypeDef]]

class LambdaDetailsTypeDef(TypedDict):
    FunctionArn: NotRequired[str]
    FunctionName: NotRequired[str]
    Description: NotRequired[str]
    LastModifiedAt: NotRequired[datetime]
    RevisionId: NotRequired[str]
    FunctionVersion: NotRequired[str]
    Role: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigTypeDef]
    Tags: NotRequired[List[TagTypeDef]]

class FilterCriteriaTypeDef(TypedDict):
    FilterCriterion: NotRequired[Sequence[FilterCriterionTypeDef]]

class GetFindingsStatisticsResponseTypeDef(TypedDict):
    FindingStatistics: FindingStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class EcsTaskDetailsTypeDef(TypedDict):
    Arn: NotRequired[str]
    DefinitionArn: NotRequired[str]
    Version: NotRequired[str]
    TaskCreatedAt: NotRequired[datetime]
    StartedAt: NotRequired[datetime]
    StartedBy: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    Volumes: NotRequired[List[VolumeTypeDef]]
    Containers: NotRequired[List[ContainerTypeDef]]
    Group: NotRequired[str]
    LaunchType: NotRequired[str]

KubernetesWorkloadDetailsTypeDef = TypedDict(
    "KubernetesWorkloadDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "Uid": NotRequired[str],
        "Namespace": NotRequired[str],
        "HostNetwork": NotRequired[bool],
        "Containers": NotRequired[List[ContainerTypeDef]],
        "Volumes": NotRequired[List[VolumeTypeDef]],
        "ServiceAccountName": NotRequired[str],
        "HostIPC": NotRequired[bool],
        "HostPID": NotRequired[bool],
    },
)

class MalwareScanDetailsTypeDef(TypedDict):
    Threats: NotRequired[List[ThreatTypeDef]]

RuntimeContextTypeDef = TypedDict(
    "RuntimeContextTypeDef",
    {
        "ModifyingProcess": NotRequired[ProcessDetailsTypeDef],
        "ModifiedAt": NotRequired[datetime],
        "ScriptPath": NotRequired[str],
        "LibraryPath": NotRequired[str],
        "LdPreloadValue": NotRequired[str],
        "SocketPath": NotRequired[str],
        "RuncBinaryPath": NotRequired[str],
        "ReleaseAgentPath": NotRequired[str],
        "MountSource": NotRequired[str],
        "MountTarget": NotRequired[str],
        "FileSystemType": NotRequired[str],
        "Flags": NotRequired[List[str]],
        "ModuleName": NotRequired[str],
        "ModuleFilePath": NotRequired[str],
        "ModuleSha256": NotRequired[str],
        "ShellHistoryFilePath": NotRequired[str],
        "TargetProcess": NotRequired[ProcessDetailsTypeDef],
        "AddressFamily": NotRequired[str],
        "IanaProtocolNumber": NotRequired[int],
        "MemoryRegions": NotRequired[List[str]],
        "ToolName": NotRequired[str],
        "ToolCategory": NotRequired[str],
        "ServiceName": NotRequired[str],
        "CommandLineExample": NotRequired[str],
        "ThreatFilePath": NotRequired[str],
    },
)

class DataSourceConfigurationsTypeDef(TypedDict):
    S3Logs: NotRequired[S3LogsConfigurationTypeDef]
    Kubernetes: NotRequired[KubernetesConfigurationTypeDef]
    MalwareProtection: NotRequired[MalwareProtectionConfigurationTypeDef]

class GetMalwareProtectionPlanResponseTypeDef(TypedDict):
    Arn: str
    Role: str
    ProtectedResource: CreateProtectedResourceOutputTypeDef
    Actions: MalwareProtectionPlanActionsTypeDef
    CreatedAt: datetime
    Status: MalwareProtectionPlanStatusType
    StatusReasons: List[MalwareProtectionPlanStatusReasonTypeDef]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class OrganizationMalwareProtectionConfigurationResultTypeDef(TypedDict):
    ScanEc2InstanceWithFindings: NotRequired[OrganizationScanEc2InstanceWithFindingsResultTypeDef]

class OrganizationMalwareProtectionConfigurationTypeDef(TypedDict):
    ScanEc2InstanceWithFindings: NotRequired[OrganizationScanEc2InstanceWithFindingsTypeDef]

class OrganizationStatisticsTypeDef(TypedDict):
    TotalAccountsCount: NotRequired[int]
    MemberAccountsCount: NotRequired[int]
    ActiveAccountsCount: NotRequired[int]
    EnabledAccountsCount: NotRequired[int]
    CountByFeature: NotRequired[List[OrganizationFeatureStatisticsTypeDef]]

AwsApiCallActionTypeDef = TypedDict(
    "AwsApiCallActionTypeDef",
    {
        "Api": NotRequired[str],
        "CallerType": NotRequired[str],
        "DomainDetails": NotRequired[DomainDetailsTypeDef],
        "ErrorCode": NotRequired[str],
        "UserAgent": NotRequired[str],
        "RemoteIpDetails": NotRequired[RemoteIpDetailsTypeDef],
        "ServiceName": NotRequired[str],
        "RemoteAccountDetails": NotRequired[RemoteAccountDetailsTypeDef],
        "AffectedResources": NotRequired[Dict[str, str]],
    },
)

class KubernetesApiCallActionTypeDef(TypedDict):
    RequestUri: NotRequired[str]
    Verb: NotRequired[str]
    SourceIps: NotRequired[List[str]]
    UserAgent: NotRequired[str]
    RemoteIpDetails: NotRequired[RemoteIpDetailsTypeDef]
    StatusCode: NotRequired[int]
    Parameters: NotRequired[str]
    Resource: NotRequired[str]
    Subresource: NotRequired[str]
    Namespace: NotRequired[str]
    ResourceName: NotRequired[str]

NetworkConnectionActionTypeDef = TypedDict(
    "NetworkConnectionActionTypeDef",
    {
        "Blocked": NotRequired[bool],
        "ConnectionDirection": NotRequired[str],
        "LocalPortDetails": NotRequired[LocalPortDetailsTypeDef],
        "Protocol": NotRequired[str],
        "LocalIpDetails": NotRequired[LocalIpDetailsTypeDef],
        "LocalNetworkInterface": NotRequired[str],
        "RemoteIpDetails": NotRequired[RemoteIpDetailsTypeDef],
        "RemotePortDetails": NotRequired[RemotePortDetailsTypeDef],
    },
)

class PortProbeDetailTypeDef(TypedDict):
    LocalPortDetails: NotRequired[LocalPortDetailsTypeDef]
    LocalIpDetails: NotRequired[LocalIpDetailsTypeDef]
    RemoteIpDetails: NotRequired[RemoteIpDetailsTypeDef]

class RdsLoginAttemptActionTypeDef(TypedDict):
    RemoteIpDetails: NotRequired[RemoteIpDetailsTypeDef]
    LoginAttributes: NotRequired[List[LoginAttributeTypeDef]]

class ResourceDataTypeDef(TypedDict):
    S3Bucket: NotRequired[S3BucketTypeDef]
    Ec2Instance: NotRequired[Ec2InstanceTypeDef]
    AccessKey: NotRequired[AccessKeyTypeDef]
    Ec2NetworkInterface: NotRequired[Ec2NetworkInterfaceTypeDef]
    S3Object: NotRequired[S3ObjectTypeDef]

class ScanResourceCriteriaOutputTypeDef(TypedDict):
    Include: NotRequired[Dict[Literal["EC2_INSTANCE_TAG"], ScanConditionOutputTypeDef]]
    Exclude: NotRequired[Dict[Literal["EC2_INSTANCE_TAG"], ScanConditionOutputTypeDef]]

class ScanResourceCriteriaTypeDef(TypedDict):
    Include: NotRequired[Mapping[Literal["EC2_INSTANCE_TAG"], ScanConditionTypeDef]]
    Exclude: NotRequired[Mapping[Literal["EC2_INSTANCE_TAG"], ScanConditionTypeDef]]

class ThreatDetectedByNameTypeDef(TypedDict):
    ItemCount: NotRequired[int]
    UniqueThreatNameCount: NotRequired[int]
    Shortened: NotRequired[bool]
    ThreatNames: NotRequired[List[ScanThreatNameTypeDef]]

class DescribeMalwareScansResponseTypeDef(TypedDict):
    Scans: List[ScanTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UsageTopAccountsResultTypeDef(TypedDict):
    Feature: NotRequired[UsageFeatureType]
    Accounts: NotRequired[List[UsageTopAccountResultTypeDef]]

class UpdateMalwareProtectionPlanRequestTypeDef(TypedDict):
    MalwareProtectionPlanId: str
    Role: NotRequired[str]
    Actions: NotRequired[MalwareProtectionPlanActionsTypeDef]
    ProtectedResource: NotRequired[UpdateProtectedResourceTypeDef]

class AnomalyTypeDef(TypedDict):
    Profiles: NotRequired[Dict[str, Dict[str, List[AnomalyObjectTypeDef]]]]
    Unusual: NotRequired[AnomalyUnusualTypeDef]

class PublicAccessTypeDef(TypedDict):
    PermissionConfiguration: NotRequired[PermissionConfigurationTypeDef]
    EffectivePermission: NotRequired[str]

class CreateFilterRequestTypeDef(TypedDict):
    DetectorId: str
    Name: str
    FindingCriteria: FindingCriteriaUnionTypeDef
    Description: NotRequired[str]
    Action: NotRequired[FilterActionType]
    Rank: NotRequired[int]
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class GetFindingsStatisticsRequestTypeDef(TypedDict):
    DetectorId: str
    FindingStatisticTypes: NotRequired[Sequence[Literal["COUNT_BY_SEVERITY"]]]
    FindingCriteria: NotRequired[FindingCriteriaUnionTypeDef]
    GroupBy: NotRequired[GroupByTypeType]
    OrderBy: NotRequired[OrderByType]
    MaxResults: NotRequired[int]

class ListFindingsRequestPaginateTypeDef(TypedDict):
    DetectorId: str
    FindingCriteria: NotRequired[FindingCriteriaUnionTypeDef]
    SortCriteria: NotRequired[SortCriteriaTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFindingsRequestTypeDef(TypedDict):
    DetectorId: str
    FindingCriteria: NotRequired[FindingCriteriaUnionTypeDef]
    SortCriteria: NotRequired[SortCriteriaTypeDef]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class UpdateFilterRequestTypeDef(TypedDict):
    DetectorId: str
    FilterName: str
    Description: NotRequired[str]
    Action: NotRequired[FilterActionType]
    Rank: NotRequired[int]
    FindingCriteria: NotRequired[FindingCriteriaUnionTypeDef]

class CoverageResourceTypeDef(TypedDict):
    ResourceId: NotRequired[str]
    DetectorId: NotRequired[str]
    AccountId: NotRequired[str]
    ResourceDetails: NotRequired[CoverageResourceDetailsTypeDef]
    CoverageStatus: NotRequired[CoverageStatusType]
    Issue: NotRequired[str]
    UpdatedAt: NotRequired[datetime]

class GetCoverageStatisticsRequestTypeDef(TypedDict):
    DetectorId: str
    StatisticsType: Sequence[CoverageStatisticsTypeType]
    FilterCriteria: NotRequired[CoverageFilterCriteriaTypeDef]

class ListCoverageRequestPaginateTypeDef(TypedDict):
    DetectorId: str
    FilterCriteria: NotRequired[CoverageFilterCriteriaTypeDef]
    SortCriteria: NotRequired[CoverageSortCriteriaTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCoverageRequestTypeDef(TypedDict):
    DetectorId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    FilterCriteria: NotRequired[CoverageFilterCriteriaTypeDef]
    SortCriteria: NotRequired[CoverageSortCriteriaTypeDef]

class CreateMalwareProtectionPlanRequestTypeDef(TypedDict):
    Role: str
    ProtectedResource: CreateProtectedResourceUnionTypeDef
    ClientToken: NotRequired[str]
    Actions: NotRequired[MalwareProtectionPlanActionsTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class AccountFreeTrialInfoTypeDef(TypedDict):
    AccountId: NotRequired[str]
    DataSources: NotRequired[DataSourcesFreeTrialTypeDef]
    Features: NotRequired[List[FreeTrialFeatureConfigurationResultTypeDef]]

class DataSourceConfigurationsResultTypeDef(TypedDict):
    CloudTrail: CloudTrailConfigurationResultTypeDef
    DNSLogs: DNSLogsConfigurationResultTypeDef
    FlowLogs: FlowLogsConfigurationResultTypeDef
    S3Logs: S3LogsConfigurationResultTypeDef
    Kubernetes: NotRequired[KubernetesConfigurationResultTypeDef]
    MalwareProtection: NotRequired[MalwareProtectionConfigurationResultTypeDef]

class UnprocessedDataSourcesResultTypeDef(TypedDict):
    MalwareProtection: NotRequired[MalwareProtectionConfigurationResultTypeDef]

class DescribeMalwareScansRequestPaginateTypeDef(TypedDict):
    DetectorId: str
    FilterCriteria: NotRequired[FilterCriteriaTypeDef]
    SortCriteria: NotRequired[SortCriteriaTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeMalwareScansRequestTypeDef(TypedDict):
    DetectorId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    FilterCriteria: NotRequired[FilterCriteriaTypeDef]
    SortCriteria: NotRequired[SortCriteriaTypeDef]

class EcsClusterDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    Arn: NotRequired[str]
    Status: NotRequired[str]
    ActiveServicesCount: NotRequired[int]
    RegisteredContainerInstancesCount: NotRequired[int]
    RunningTasksCount: NotRequired[int]
    Tags: NotRequired[List[TagTypeDef]]
    TaskDetails: NotRequired[EcsTaskDetailsTypeDef]

class KubernetesDetailsTypeDef(TypedDict):
    KubernetesUserDetails: NotRequired[KubernetesUserDetailsTypeDef]
    KubernetesWorkloadDetails: NotRequired[KubernetesWorkloadDetailsTypeDef]

class RuntimeDetailsTypeDef(TypedDict):
    Process: NotRequired[ProcessDetailsTypeDef]
    Context: NotRequired[RuntimeContextTypeDef]

class CreateDetectorRequestTypeDef(TypedDict):
    Enable: bool
    ClientToken: NotRequired[str]
    FindingPublishingFrequency: NotRequired[FindingPublishingFrequencyType]
    DataSources: NotRequired[DataSourceConfigurationsTypeDef]
    Tags: NotRequired[Mapping[str, str]]
    Features: NotRequired[Sequence[DetectorFeatureConfigurationTypeDef]]

class UpdateDetectorRequestTypeDef(TypedDict):
    DetectorId: str
    Enable: NotRequired[bool]
    FindingPublishingFrequency: NotRequired[FindingPublishingFrequencyType]
    DataSources: NotRequired[DataSourceConfigurationsTypeDef]
    Features: NotRequired[Sequence[DetectorFeatureConfigurationTypeDef]]

class UpdateMemberDetectorsRequestTypeDef(TypedDict):
    DetectorId: str
    AccountIds: Sequence[str]
    DataSources: NotRequired[DataSourceConfigurationsTypeDef]
    Features: NotRequired[Sequence[MemberFeaturesConfigurationTypeDef]]

class OrganizationDataSourceConfigurationsResultTypeDef(TypedDict):
    S3Logs: OrganizationS3LogsConfigurationResultTypeDef
    Kubernetes: NotRequired[OrganizationKubernetesConfigurationResultTypeDef]
    MalwareProtection: NotRequired[OrganizationMalwareProtectionConfigurationResultTypeDef]

class OrganizationDataSourceConfigurationsTypeDef(TypedDict):
    S3Logs: NotRequired[OrganizationS3LogsConfigurationTypeDef]
    Kubernetes: NotRequired[OrganizationKubernetesConfigurationTypeDef]
    MalwareProtection: NotRequired[OrganizationMalwareProtectionConfigurationTypeDef]

class OrganizationDetailsTypeDef(TypedDict):
    UpdatedAt: NotRequired[datetime]
    OrganizationStatistics: NotRequired[OrganizationStatisticsTypeDef]

class PortProbeActionTypeDef(TypedDict):
    Blocked: NotRequired[bool]
    PortProbeDetails: NotRequired[List[PortProbeDetailTypeDef]]

class ResourceV2TypeDef(TypedDict):
    Uid: str
    ResourceType: FindingResourceTypeType
    Name: NotRequired[str]
    AccountId: NotRequired[str]
    Region: NotRequired[str]
    Service: NotRequired[str]
    CloudPartition: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    Data: NotRequired[ResourceDataTypeDef]

class GetMalwareScanSettingsResponseTypeDef(TypedDict):
    ScanResourceCriteria: ScanResourceCriteriaOutputTypeDef
    EbsSnapshotPreservation: EbsSnapshotPreservationType
    ResponseMetadata: ResponseMetadataTypeDef

ScanResourceCriteriaUnionTypeDef = Union[
    ScanResourceCriteriaTypeDef, ScanResourceCriteriaOutputTypeDef
]

class ScanDetectionsTypeDef(TypedDict):
    ScannedItemCount: NotRequired[ScannedItemCountTypeDef]
    ThreatsDetectedItemCount: NotRequired[ThreatsDetectedItemCountTypeDef]
    HighestSeverityThreatDetails: NotRequired[HighestSeverityThreatDetailsTypeDef]
    ThreatDetectedByName: NotRequired[ThreatDetectedByNameTypeDef]

class UsageStatisticsTypeDef(TypedDict):
    SumByAccount: NotRequired[List[UsageAccountResultTypeDef]]
    TopAccountsByFeature: NotRequired[List[UsageTopAccountsResultTypeDef]]
    SumByDataSource: NotRequired[List[UsageDataSourceResultTypeDef]]
    SumByResource: NotRequired[List[UsageResourceResultTypeDef]]
    TopResources: NotRequired[List[UsageResourceResultTypeDef]]
    SumByFeature: NotRequired[List[UsageFeatureResultTypeDef]]

S3BucketDetailTypeDef = TypedDict(
    "S3BucketDetailTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "Owner": NotRequired[OwnerTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
        "DefaultServerSideEncryption": NotRequired[DefaultServerSideEncryptionTypeDef],
        "PublicAccess": NotRequired[PublicAccessTypeDef],
        "S3ObjectDetails": NotRequired[List[S3ObjectDetailTypeDef]],
    },
)

class ListCoverageResponseTypeDef(TypedDict):
    Resources: List[CoverageResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetRemainingFreeTrialDaysResponseTypeDef(TypedDict):
    Accounts: List[AccountFreeTrialInfoTypeDef]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDetectorResponseTypeDef(TypedDict):
    CreatedAt: str
    FindingPublishingFrequency: FindingPublishingFrequencyType
    ServiceRole: str
    Status: DetectorStatusType
    UpdatedAt: str
    DataSources: DataSourceConfigurationsResultTypeDef
    Tags: Dict[str, str]
    Features: List[DetectorFeatureConfigurationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MemberDataSourceConfigurationTypeDef(TypedDict):
    AccountId: str
    DataSources: NotRequired[DataSourceConfigurationsResultTypeDef]
    Features: NotRequired[List[MemberFeaturesConfigurationResultTypeDef]]

class CreateDetectorResponseTypeDef(TypedDict):
    DetectorId: str
    UnprocessedDataSources: UnprocessedDataSourcesResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOrganizationConfigurationResponseTypeDef(TypedDict):
    AutoEnable: bool
    MemberAccountLimitReached: bool
    DataSources: OrganizationDataSourceConfigurationsResultTypeDef
    Features: List[OrganizationFeatureConfigurationResultTypeDef]
    AutoEnableOrganizationMembers: AutoEnableMembersType
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateOrganizationConfigurationRequestTypeDef(TypedDict):
    DetectorId: str
    AutoEnable: NotRequired[bool]
    DataSources: NotRequired[OrganizationDataSourceConfigurationsTypeDef]
    Features: NotRequired[Sequence[OrganizationFeatureConfigurationTypeDef]]
    AutoEnableOrganizationMembers: NotRequired[AutoEnableMembersType]

class GetOrganizationStatisticsResponseTypeDef(TypedDict):
    OrganizationDetails: OrganizationDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ActionTypeDef(TypedDict):
    ActionType: NotRequired[str]
    AwsApiCallAction: NotRequired[AwsApiCallActionTypeDef]
    DnsRequestAction: NotRequired[DnsRequestActionTypeDef]
    NetworkConnectionAction: NotRequired[NetworkConnectionActionTypeDef]
    PortProbeAction: NotRequired[PortProbeActionTypeDef]
    KubernetesApiCallAction: NotRequired[KubernetesApiCallActionTypeDef]
    RdsLoginAttemptAction: NotRequired[RdsLoginAttemptActionTypeDef]
    KubernetesPermissionCheckedDetails: NotRequired[KubernetesPermissionCheckedDetailsTypeDef]
    KubernetesRoleBindingDetails: NotRequired[KubernetesRoleBindingDetailsTypeDef]
    KubernetesRoleDetails: NotRequired[KubernetesRoleDetailsTypeDef]

class SequenceTypeDef(TypedDict):
    Uid: str
    Description: str
    Signals: List[SignalTypeDef]
    Actors: NotRequired[List[ActorTypeDef]]
    Resources: NotRequired[List[ResourceV2TypeDef]]
    Endpoints: NotRequired[List[NetworkEndpointTypeDef]]
    SequenceIndicators: NotRequired[List[IndicatorTypeDef]]

class UpdateMalwareScanSettingsRequestTypeDef(TypedDict):
    DetectorId: str
    ScanResourceCriteria: NotRequired[ScanResourceCriteriaUnionTypeDef]
    EbsSnapshotPreservation: NotRequired[EbsSnapshotPreservationType]

class EbsVolumeScanDetailsTypeDef(TypedDict):
    ScanId: NotRequired[str]
    ScanStartedAt: NotRequired[datetime]
    ScanCompletedAt: NotRequired[datetime]
    TriggerFindingId: NotRequired[str]
    Sources: NotRequired[List[str]]
    ScanDetections: NotRequired[ScanDetectionsTypeDef]
    ScanType: NotRequired[ScanTypeType]

class GetUsageStatisticsResponseTypeDef(TypedDict):
    UsageStatistics: UsageStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ResourceTypeDef(TypedDict):
    AccessKeyDetails: NotRequired[AccessKeyDetailsTypeDef]
    S3BucketDetails: NotRequired[List[S3BucketDetailTypeDef]]
    InstanceDetails: NotRequired[InstanceDetailsTypeDef]
    EksClusterDetails: NotRequired[EksClusterDetailsTypeDef]
    KubernetesDetails: NotRequired[KubernetesDetailsTypeDef]
    ResourceType: NotRequired[str]
    EbsVolumeDetails: NotRequired[EbsVolumeDetailsTypeDef]
    EcsClusterDetails: NotRequired[EcsClusterDetailsTypeDef]
    ContainerDetails: NotRequired[ContainerTypeDef]
    RdsDbInstanceDetails: NotRequired[RdsDbInstanceDetailsTypeDef]
    RdsLimitlessDbDetails: NotRequired[RdsLimitlessDbDetailsTypeDef]
    RdsDbUserDetails: NotRequired[RdsDbUserDetailsTypeDef]
    LambdaDetails: NotRequired[LambdaDetailsTypeDef]

class GetMemberDetectorsResponseTypeDef(TypedDict):
    MemberDataSourceConfigurations: List[MemberDataSourceConfigurationTypeDef]
    UnprocessedAccounts: List[UnprocessedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

DetectionTypeDef = TypedDict(
    "DetectionTypeDef",
    {
        "Anomaly": NotRequired[AnomalyTypeDef],
        "Sequence": NotRequired[SequenceTypeDef],
    },
)
ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "Action": NotRequired[ActionTypeDef],
        "Evidence": NotRequired[EvidenceTypeDef],
        "Archived": NotRequired[bool],
        "Count": NotRequired[int],
        "DetectorId": NotRequired[str],
        "EventFirstSeen": NotRequired[str],
        "EventLastSeen": NotRequired[str],
        "ResourceRole": NotRequired[str],
        "ServiceName": NotRequired[str],
        "UserFeedback": NotRequired[str],
        "AdditionalInfo": NotRequired[ServiceAdditionalInfoTypeDef],
        "FeatureName": NotRequired[str],
        "EbsVolumeScanDetails": NotRequired[EbsVolumeScanDetailsTypeDef],
        "RuntimeDetails": NotRequired[RuntimeDetailsTypeDef],
        "Detection": NotRequired[DetectionTypeDef],
        "MalwareScanDetails": NotRequired[MalwareScanDetailsTypeDef],
    },
)
FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "AccountId": str,
        "Arn": str,
        "CreatedAt": str,
        "Id": str,
        "Region": str,
        "Resource": ResourceTypeDef,
        "SchemaVersion": str,
        "Severity": float,
        "Type": str,
        "UpdatedAt": str,
        "Confidence": NotRequired[float],
        "Description": NotRequired[str],
        "Partition": NotRequired[str],
        "Service": NotRequired[ServiceTypeDef],
        "Title": NotRequired[str],
        "AssociatedAttackSequenceArn": NotRequired[str],
    },
)

class GetFindingsResponseTypeDef(TypedDict):
    Findings: List[FindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
