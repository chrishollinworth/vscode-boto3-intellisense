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
    FreeTrialFeatureResultType,
    IpSetFormatType,
    IpSetStatusType,
    MalwareProtectionPlanStatusType,
    MalwareProtectionPlanTaggingActionStatusType,
    ManagementTypeType,
    OrderByType,
    OrgFeatureAdditionalConfigurationType,
    OrgFeatureStatusType,
    OrgFeatureType,
    ProfileSubtypeType,
    PublishingStatusType,
    ResourceTypeType,
    ScanResultType,
    ScanStatusType,
    ScanTypeType,
    ThreatIntelSetFormatType,
    ThreatIntelSetStatusType,
    UsageFeatureType,
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
    "AddonDetailsTypeDef",
    "AdminAccountTypeDef",
    "AdministratorTypeDef",
    "AgentDetailsTypeDef",
    "AnomalyObjectTypeDef",
    "AnomalyTypeDef",
    "AnomalyUnusualTypeDef",
    "ArchiveFindingsRequestRequestTypeDef",
    "AwsApiCallActionTypeDef",
    "BlockPublicAccessTypeDef",
    "BucketLevelPermissionsTypeDef",
    "BucketPolicyTypeDef",
    "CityTypeDef",
    "CloudTrailConfigurationResultTypeDef",
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
    "CreateDetectorRequestRequestTypeDef",
    "CreateDetectorResponseTypeDef",
    "CreateFilterRequestRequestTypeDef",
    "CreateFilterResponseTypeDef",
    "CreateIPSetRequestRequestTypeDef",
    "CreateIPSetResponseTypeDef",
    "CreateMalwareProtectionPlanRequestRequestTypeDef",
    "CreateMalwareProtectionPlanResponseTypeDef",
    "CreateMembersRequestRequestTypeDef",
    "CreateMembersResponseTypeDef",
    "CreateProtectedResourceTypeDef",
    "CreatePublishingDestinationRequestRequestTypeDef",
    "CreatePublishingDestinationResponseTypeDef",
    "CreateS3BucketResourceTypeDef",
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
    "DeleteMalwareProtectionPlanRequestRequestTypeDef",
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
    "DetectionTypeDef",
    "DetectorAdditionalConfigurationResultTypeDef",
    "DetectorAdditionalConfigurationTypeDef",
    "DetectorFeatureConfigurationResultTypeDef",
    "DetectorFeatureConfigurationTypeDef",
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
    "FargateDetailsTypeDef",
    "FilterConditionTypeDef",
    "FilterCriteriaTypeDef",
    "FilterCriterionTypeDef",
    "FindingCriteriaTypeDef",
    "FindingStatisticsTypeDef",
    "FindingTypeDef",
    "FlowLogsConfigurationResultTypeDef",
    "FreeTrialFeatureConfigurationResultTypeDef",
    "GeoLocationTypeDef",
    "GetAdministratorAccountRequestRequestTypeDef",
    "GetAdministratorAccountResponseTypeDef",
    "GetCoverageStatisticsRequestRequestTypeDef",
    "GetCoverageStatisticsResponseTypeDef",
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
    "GetMalwareProtectionPlanRequestRequestTypeDef",
    "GetMalwareProtectionPlanResponseTypeDef",
    "GetMalwareScanSettingsRequestRequestTypeDef",
    "GetMalwareScanSettingsResponseTypeDef",
    "GetMasterAccountRequestRequestTypeDef",
    "GetMasterAccountResponseTypeDef",
    "GetMemberDetectorsRequestRequestTypeDef",
    "GetMemberDetectorsResponseTypeDef",
    "GetMembersRequestRequestTypeDef",
    "GetMembersResponseTypeDef",
    "GetOrganizationStatisticsResponseTypeDef",
    "GetRemainingFreeTrialDaysRequestRequestTypeDef",
    "GetRemainingFreeTrialDaysResponseTypeDef",
    "GetThreatIntelSetRequestRequestTypeDef",
    "GetThreatIntelSetResponseTypeDef",
    "GetUsageStatisticsRequestRequestTypeDef",
    "GetUsageStatisticsResponseTypeDef",
    "HighestSeverityThreatDetailsTypeDef",
    "HostPathTypeDef",
    "IamInstanceProfileTypeDef",
    "ImpersonatedUserTypeDef",
    "InstanceDetailsTypeDef",
    "InvitationTypeDef",
    "InviteMembersRequestRequestTypeDef",
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
    "ListCoverageRequestRequestTypeDef",
    "ListCoverageResponseTypeDef",
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
    "ListMalwareProtectionPlansRequestRequestTypeDef",
    "ListMalwareProtectionPlansResponseTypeDef",
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
    "PublicAccessTypeDef",
    "RdsDbInstanceDetailsTypeDef",
    "RdsDbUserDetailsTypeDef",
    "RdsLoginAttemptActionTypeDef",
    "RemoteAccountDetailsTypeDef",
    "RemoteIpDetailsTypeDef",
    "RemotePortDetailsTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RuntimeContextTypeDef",
    "RuntimeDetailsTypeDef",
    "S3BucketDetailTypeDef",
    "S3LogsConfigurationResultTypeDef",
    "S3LogsConfigurationTypeDef",
    "S3ObjectDetailTypeDef",
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
    "StartMalwareScanRequestRequestTypeDef",
    "StartMalwareScanResponseTypeDef",
    "StartMonitoringMembersRequestRequestTypeDef",
    "StartMonitoringMembersResponseTypeDef",
    "StopMonitoringMembersRequestRequestTypeDef",
    "StopMonitoringMembersResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "ThreatDetectedByNameTypeDef",
    "ThreatIntelligenceDetailTypeDef",
    "ThreatTypeDef",
    "ThreatsDetectedItemCountTypeDef",
    "TotalTypeDef",
    "TriggerDetailsTypeDef",
    "UnarchiveFindingsRequestRequestTypeDef",
    "UnprocessedAccountTypeDef",
    "UnprocessedDataSourcesResultTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDetectorRequestRequestTypeDef",
    "UpdateFilterRequestRequestTypeDef",
    "UpdateFilterResponseTypeDef",
    "UpdateFindingsFeedbackRequestRequestTypeDef",
    "UpdateIPSetRequestRequestTypeDef",
    "UpdateMalwareProtectionPlanRequestRequestTypeDef",
    "UpdateMalwareScanSettingsRequestRequestTypeDef",
    "UpdateMemberDetectorsRequestRequestTypeDef",
    "UpdateMemberDetectorsResponseTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    "UpdateProtectedResourceTypeDef",
    "UpdatePublishingDestinationRequestRequestTypeDef",
    "UpdateS3BucketResourceTypeDef",
    "UpdateThreatIntelSetRequestRequestTypeDef",
    "UsageAccountResultTypeDef",
    "UsageCriteriaTypeDef",
    "UsageDataSourceResultTypeDef",
    "UsageFeatureResultTypeDef",
    "UsageResourceResultTypeDef",
    "UsageStatisticsTypeDef",
    "UsageTopAccountResultTypeDef",
    "UsageTopAccountsResultTypeDef",
    "VolumeDetailTypeDef",
    "VolumeMountTypeDef",
    "VolumeTypeDef",
    "VpcConfigTypeDef",
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
        "Features": List["FreeTrialFeatureConfigurationResultTypeDef"],
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
        "RdsLoginAttemptAction": "RdsLoginAttemptActionTypeDef",
        "KubernetesPermissionCheckedDetails": "KubernetesPermissionCheckedDetailsTypeDef",
        "KubernetesRoleBindingDetails": "KubernetesRoleBindingDetailsTypeDef",
        "KubernetesRoleDetails": "KubernetesRoleDetailsTypeDef",
    },
    total=False,
)

AddonDetailsTypeDef = TypedDict(
    "AddonDetailsTypeDef",
    {
        "AddonVersion": str,
        "AddonStatus": str,
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

AgentDetailsTypeDef = TypedDict(
    "AgentDetailsTypeDef",
    {
        "Version": str,
    },
    total=False,
)

AnomalyObjectTypeDef = TypedDict(
    "AnomalyObjectTypeDef",
    {
        "ProfileType": Literal["FREQUENCY"],
        "ProfileSubtype": ProfileSubtypeType,
        "Observations": "ObservationsTypeDef",
    },
    total=False,
)

AnomalyTypeDef = TypedDict(
    "AnomalyTypeDef",
    {
        "Profiles": Dict[str, Dict[str, List["AnomalyObjectTypeDef"]]],
        "Unusual": "AnomalyUnusualTypeDef",
    },
    total=False,
)

AnomalyUnusualTypeDef = TypedDict(
    "AnomalyUnusualTypeDef",
    {
        "Behavior": Dict[str, Dict[str, "AnomalyObjectTypeDef"]],
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

ContainerInstanceDetailsTypeDef = TypedDict(
    "ContainerInstanceDetailsTypeDef",
    {
        "CoveredContainerInstances": int,
        "CompatibleContainerInstances": int,
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

CoverageEc2InstanceDetailsTypeDef = TypedDict(
    "CoverageEc2InstanceDetailsTypeDef",
    {
        "InstanceId": str,
        "InstanceType": str,
        "ClusterArn": str,
        "AgentDetails": "AgentDetailsTypeDef",
        "ManagementType": ManagementTypeType,
    },
    total=False,
)

CoverageEcsClusterDetailsTypeDef = TypedDict(
    "CoverageEcsClusterDetailsTypeDef",
    {
        "ClusterName": str,
        "FargateDetails": "FargateDetailsTypeDef",
        "ContainerInstanceDetails": "ContainerInstanceDetailsTypeDef",
    },
    total=False,
)

CoverageEksClusterDetailsTypeDef = TypedDict(
    "CoverageEksClusterDetailsTypeDef",
    {
        "ClusterName": str,
        "CoveredNodes": int,
        "CompatibleNodes": int,
        "AddonDetails": "AddonDetailsTypeDef",
        "ManagementType": ManagementTypeType,
    },
    total=False,
)

CoverageFilterConditionTypeDef = TypedDict(
    "CoverageFilterConditionTypeDef",
    {
        "Equals": List[str],
        "NotEquals": List[str],
    },
    total=False,
)

CoverageFilterCriteriaTypeDef = TypedDict(
    "CoverageFilterCriteriaTypeDef",
    {
        "FilterCriterion": List["CoverageFilterCriterionTypeDef"],
    },
    total=False,
)

CoverageFilterCriterionTypeDef = TypedDict(
    "CoverageFilterCriterionTypeDef",
    {
        "CriterionKey": CoverageFilterCriterionKeyType,
        "FilterCondition": "CoverageFilterConditionTypeDef",
    },
    total=False,
)

CoverageResourceDetailsTypeDef = TypedDict(
    "CoverageResourceDetailsTypeDef",
    {
        "EksClusterDetails": "CoverageEksClusterDetailsTypeDef",
        "ResourceType": ResourceTypeType,
        "EcsClusterDetails": "CoverageEcsClusterDetailsTypeDef",
        "Ec2InstanceDetails": "CoverageEc2InstanceDetailsTypeDef",
    },
    total=False,
)

CoverageResourceTypeDef = TypedDict(
    "CoverageResourceTypeDef",
    {
        "ResourceId": str,
        "DetectorId": str,
        "AccountId": str,
        "ResourceDetails": "CoverageResourceDetailsTypeDef",
        "CoverageStatus": CoverageStatusType,
        "Issue": str,
        "UpdatedAt": datetime,
    },
    total=False,
)

CoverageSortCriteriaTypeDef = TypedDict(
    "CoverageSortCriteriaTypeDef",
    {
        "AttributeName": CoverageSortKeyType,
        "OrderBy": OrderByType,
    },
    total=False,
)

CoverageStatisticsTypeDef = TypedDict(
    "CoverageStatisticsTypeDef",
    {
        "CountByResourceType": Dict[ResourceTypeType, int],
        "CountByCoverageStatus": Dict[CoverageStatusType, int],
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
        "Features": List["DetectorFeatureConfigurationTypeDef"],
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
        "UnprocessedDataSources": "UnprocessedDataSourcesResultTypeDef",
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

_RequiredCreateMalwareProtectionPlanRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMalwareProtectionPlanRequestRequestTypeDef",
    {
        "Role": str,
        "ProtectedResource": "CreateProtectedResourceTypeDef",
    },
)
_OptionalCreateMalwareProtectionPlanRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMalwareProtectionPlanRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Actions": "MalwareProtectionPlanActionsTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateMalwareProtectionPlanRequestRequestTypeDef(
    _RequiredCreateMalwareProtectionPlanRequestRequestTypeDef,
    _OptionalCreateMalwareProtectionPlanRequestRequestTypeDef,
):
    pass

CreateMalwareProtectionPlanResponseTypeDef = TypedDict(
    "CreateMalwareProtectionPlanResponseTypeDef",
    {
        "MalwareProtectionPlanId": str,
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

CreateProtectedResourceTypeDef = TypedDict(
    "CreateProtectedResourceTypeDef",
    {
        "S3Bucket": "CreateS3BucketResourceTypeDef",
    },
    total=False,
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

CreateS3BucketResourceTypeDef = TypedDict(
    "CreateS3BucketResourceTypeDef",
    {
        "BucketName": str,
        "ObjectPrefixes": List[str],
    },
    total=False,
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

DeleteMalwareProtectionPlanRequestRequestTypeDef = TypedDict(
    "DeleteMalwareProtectionPlanRequestRequestTypeDef",
    {
        "MalwareProtectionPlanId": str,
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

_RequiredDescribeOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeOrganizationConfigurationRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalDescribeOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeOrganizationConfigurationRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeOrganizationConfigurationRequestRequestTypeDef(
    _RequiredDescribeOrganizationConfigurationRequestRequestTypeDef,
    _OptionalDescribeOrganizationConfigurationRequestRequestTypeDef,
):
    pass

DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "AutoEnable": bool,
        "MemberAccountLimitReached": bool,
        "DataSources": "OrganizationDataSourceConfigurationsResultTypeDef",
        "Features": List["OrganizationFeatureConfigurationResultTypeDef"],
        "NextToken": str,
        "AutoEnableOrganizationMembers": AutoEnableMembersType,
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

DetectionTypeDef = TypedDict(
    "DetectionTypeDef",
    {
        "Anomaly": "AnomalyTypeDef",
    },
    total=False,
)

DetectorAdditionalConfigurationResultTypeDef = TypedDict(
    "DetectorAdditionalConfigurationResultTypeDef",
    {
        "Name": FeatureAdditionalConfigurationType,
        "Status": FeatureStatusType,
        "UpdatedAt": datetime,
    },
    total=False,
)

DetectorAdditionalConfigurationTypeDef = TypedDict(
    "DetectorAdditionalConfigurationTypeDef",
    {
        "Name": FeatureAdditionalConfigurationType,
        "Status": FeatureStatusType,
    },
    total=False,
)

DetectorFeatureConfigurationResultTypeDef = TypedDict(
    "DetectorFeatureConfigurationResultTypeDef",
    {
        "Name": DetectorFeatureResultType,
        "Status": FeatureStatusType,
        "UpdatedAt": datetime,
        "AdditionalConfiguration": List["DetectorAdditionalConfigurationResultTypeDef"],
    },
    total=False,
)

DetectorFeatureConfigurationTypeDef = TypedDict(
    "DetectorFeatureConfigurationTypeDef",
    {
        "Name": DetectorFeatureType,
        "Status": FeatureStatusType,
        "AdditionalConfiguration": List["DetectorAdditionalConfigurationTypeDef"],
    },
    total=False,
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
        "DomainWithSuffix": str,
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
        "ScanType": ScanTypeType,
    },
    total=False,
)

EbsVolumesResultTypeDef = TypedDict(
    "EbsVolumesResultTypeDef",
    {
        "Status": DataSourceStatusType,
        "Reason": str,
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

FargateDetailsTypeDef = TypedDict(
    "FargateDetailsTypeDef",
    {
        "Issues": List[str],
        "ManagementType": ManagementTypeType,
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

FreeTrialFeatureConfigurationResultTypeDef = TypedDict(
    "FreeTrialFeatureConfigurationResultTypeDef",
    {
        "Name": FreeTrialFeatureResultType,
        "FreeTrialDaysRemaining": int,
    },
    total=False,
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

_RequiredGetCoverageStatisticsRequestRequestTypeDef = TypedDict(
    "_RequiredGetCoverageStatisticsRequestRequestTypeDef",
    {
        "DetectorId": str,
        "StatisticsType": List[CoverageStatisticsTypeType],
    },
)
_OptionalGetCoverageStatisticsRequestRequestTypeDef = TypedDict(
    "_OptionalGetCoverageStatisticsRequestRequestTypeDef",
    {
        "FilterCriteria": "CoverageFilterCriteriaTypeDef",
    },
    total=False,
)

class GetCoverageStatisticsRequestRequestTypeDef(
    _RequiredGetCoverageStatisticsRequestRequestTypeDef,
    _OptionalGetCoverageStatisticsRequestRequestTypeDef,
):
    pass

GetCoverageStatisticsResponseTypeDef = TypedDict(
    "GetCoverageStatisticsResponseTypeDef",
    {
        "CoverageStatistics": "CoverageStatisticsTypeDef",
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
        "Features": List["DetectorFeatureConfigurationResultTypeDef"],
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

GetMalwareProtectionPlanRequestRequestTypeDef = TypedDict(
    "GetMalwareProtectionPlanRequestRequestTypeDef",
    {
        "MalwareProtectionPlanId": str,
    },
)

GetMalwareProtectionPlanResponseTypeDef = TypedDict(
    "GetMalwareProtectionPlanResponseTypeDef",
    {
        "Arn": str,
        "Role": str,
        "ProtectedResource": "CreateProtectedResourceTypeDef",
        "Actions": "MalwareProtectionPlanActionsTypeDef",
        "CreatedAt": datetime,
        "Status": MalwareProtectionPlanStatusType,
        "StatusReasons": List["MalwareProtectionPlanStatusReasonTypeDef"],
        "Tags": Dict[str, str],
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

GetOrganizationStatisticsResponseTypeDef = TypedDict(
    "GetOrganizationStatisticsResponseTypeDef",
    {
        "OrganizationDetails": "OrganizationDetailsTypeDef",
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

ImpersonatedUserTypeDef = TypedDict(
    "ImpersonatedUserTypeDef",
    {
        "Username": str,
        "Groups": List[str],
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

ItemPathTypeDef = TypedDict(
    "ItemPathTypeDef",
    {
        "NestedItemPath": str,
        "Hash": str,
    },
    total=False,
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
        "Resource": str,
        "Subresource": str,
        "Namespace": str,
        "ResourceName": str,
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

KubernetesPermissionCheckedDetailsTypeDef = TypedDict(
    "KubernetesPermissionCheckedDetailsTypeDef",
    {
        "Verb": str,
        "Resource": str,
        "Namespace": str,
        "Allowed": bool,
    },
    total=False,
)

KubernetesRoleBindingDetailsTypeDef = TypedDict(
    "KubernetesRoleBindingDetailsTypeDef",
    {
        "Kind": str,
        "Name": str,
        "Uid": str,
        "RoleRefName": str,
        "RoleRefKind": str,
    },
    total=False,
)

KubernetesRoleDetailsTypeDef = TypedDict(
    "KubernetesRoleDetailsTypeDef",
    {
        "Kind": str,
        "Name": str,
        "Uid": str,
    },
    total=False,
)

KubernetesUserDetailsTypeDef = TypedDict(
    "KubernetesUserDetailsTypeDef",
    {
        "Username": str,
        "Uid": str,
        "Groups": List[str],
        "SessionName": List[str],
        "ImpersonatedUser": "ImpersonatedUserTypeDef",
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
        "ServiceAccountName": str,
        "HostIPC": bool,
        "HostPID": bool,
    },
    total=False,
)

LambdaDetailsTypeDef = TypedDict(
    "LambdaDetailsTypeDef",
    {
        "FunctionArn": str,
        "FunctionName": str,
        "Description": str,
        "LastModifiedAt": datetime,
        "RevisionId": str,
        "FunctionVersion": str,
        "Role": str,
        "VpcConfig": "VpcConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LineageObjectTypeDef = TypedDict(
    "LineageObjectTypeDef",
    {
        "StartTime": datetime,
        "NamespacePid": int,
        "UserId": int,
        "Name": str,
        "Pid": int,
        "Uuid": str,
        "ExecutablePath": str,
        "Euid": int,
        "ParentUuid": str,
    },
    total=False,
)

_RequiredListCoverageRequestRequestTypeDef = TypedDict(
    "_RequiredListCoverageRequestRequestTypeDef",
    {
        "DetectorId": str,
    },
)
_OptionalListCoverageRequestRequestTypeDef = TypedDict(
    "_OptionalListCoverageRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "FilterCriteria": "CoverageFilterCriteriaTypeDef",
        "SortCriteria": "CoverageSortCriteriaTypeDef",
    },
    total=False,
)

class ListCoverageRequestRequestTypeDef(
    _RequiredListCoverageRequestRequestTypeDef, _OptionalListCoverageRequestRequestTypeDef
):
    pass

ListCoverageResponseTypeDef = TypedDict(
    "ListCoverageResponseTypeDef",
    {
        "Resources": List["CoverageResourceTypeDef"],
        "NextToken": str,
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

ListMalwareProtectionPlansRequestRequestTypeDef = TypedDict(
    "ListMalwareProtectionPlansRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListMalwareProtectionPlansResponseTypeDef = TypedDict(
    "ListMalwareProtectionPlansResponseTypeDef",
    {
        "MalwareProtectionPlans": List["MalwareProtectionPlanSummaryTypeDef"],
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
        "IpAddressV6": str,
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

LoginAttributeTypeDef = TypedDict(
    "LoginAttributeTypeDef",
    {
        "User": str,
        "Application": str,
        "FailedLoginAttempts": int,
        "SuccessfulLoginAttempts": int,
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

MalwareProtectionPlanActionsTypeDef = TypedDict(
    "MalwareProtectionPlanActionsTypeDef",
    {
        "Tagging": "MalwareProtectionPlanTaggingActionTypeDef",
    },
    total=False,
)

MalwareProtectionPlanStatusReasonTypeDef = TypedDict(
    "MalwareProtectionPlanStatusReasonTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

MalwareProtectionPlanSummaryTypeDef = TypedDict(
    "MalwareProtectionPlanSummaryTypeDef",
    {
        "MalwareProtectionPlanId": str,
    },
    total=False,
)

MalwareProtectionPlanTaggingActionTypeDef = TypedDict(
    "MalwareProtectionPlanTaggingActionTypeDef",
    {
        "Status": MalwareProtectionPlanTaggingActionStatusType,
    },
    total=False,
)

MalwareScanDetailsTypeDef = TypedDict(
    "MalwareScanDetailsTypeDef",
    {
        "Threats": List["ThreatTypeDef"],
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

MemberAdditionalConfigurationResultTypeDef = TypedDict(
    "MemberAdditionalConfigurationResultTypeDef",
    {
        "Name": OrgFeatureAdditionalConfigurationType,
        "Status": FeatureStatusType,
        "UpdatedAt": datetime,
    },
    total=False,
)

MemberAdditionalConfigurationTypeDef = TypedDict(
    "MemberAdditionalConfigurationTypeDef",
    {
        "Name": OrgFeatureAdditionalConfigurationType,
        "Status": FeatureStatusType,
    },
    total=False,
)

_RequiredMemberDataSourceConfigurationTypeDef = TypedDict(
    "_RequiredMemberDataSourceConfigurationTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalMemberDataSourceConfigurationTypeDef = TypedDict(
    "_OptionalMemberDataSourceConfigurationTypeDef",
    {
        "DataSources": "DataSourceConfigurationsResultTypeDef",
        "Features": List["MemberFeaturesConfigurationResultTypeDef"],
    },
    total=False,
)

class MemberDataSourceConfigurationTypeDef(
    _RequiredMemberDataSourceConfigurationTypeDef, _OptionalMemberDataSourceConfigurationTypeDef
):
    pass

MemberFeaturesConfigurationResultTypeDef = TypedDict(
    "MemberFeaturesConfigurationResultTypeDef",
    {
        "Name": OrgFeatureType,
        "Status": FeatureStatusType,
        "UpdatedAt": datetime,
        "AdditionalConfiguration": List["MemberAdditionalConfigurationResultTypeDef"],
    },
    total=False,
)

MemberFeaturesConfigurationTypeDef = TypedDict(
    "MemberFeaturesConfigurationTypeDef",
    {
        "Name": OrgFeatureType,
        "Status": FeatureStatusType,
        "AdditionalConfiguration": List["MemberAdditionalConfigurationTypeDef"],
    },
    total=False,
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

ObservationsTypeDef = TypedDict(
    "ObservationsTypeDef",
    {
        "Text": List[str],
    },
    total=False,
)

OrganizationAdditionalConfigurationResultTypeDef = TypedDict(
    "OrganizationAdditionalConfigurationResultTypeDef",
    {
        "Name": OrgFeatureAdditionalConfigurationType,
        "AutoEnable": OrgFeatureStatusType,
    },
    total=False,
)

OrganizationAdditionalConfigurationTypeDef = TypedDict(
    "OrganizationAdditionalConfigurationTypeDef",
    {
        "Name": OrgFeatureAdditionalConfigurationType,
        "AutoEnable": OrgFeatureStatusType,
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

OrganizationDetailsTypeDef = TypedDict(
    "OrganizationDetailsTypeDef",
    {
        "UpdatedAt": datetime,
        "OrganizationStatistics": "OrganizationStatisticsTypeDef",
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

OrganizationFeatureConfigurationResultTypeDef = TypedDict(
    "OrganizationFeatureConfigurationResultTypeDef",
    {
        "Name": OrgFeatureType,
        "AutoEnable": OrgFeatureStatusType,
        "AdditionalConfiguration": List["OrganizationAdditionalConfigurationResultTypeDef"],
    },
    total=False,
)

OrganizationFeatureConfigurationTypeDef = TypedDict(
    "OrganizationFeatureConfigurationTypeDef",
    {
        "Name": OrgFeatureType,
        "AutoEnable": OrgFeatureStatusType,
        "AdditionalConfiguration": List["OrganizationAdditionalConfigurationTypeDef"],
    },
    total=False,
)

OrganizationFeatureStatisticsAdditionalConfigurationTypeDef = TypedDict(
    "OrganizationFeatureStatisticsAdditionalConfigurationTypeDef",
    {
        "Name": OrgFeatureAdditionalConfigurationType,
        "EnabledAccountsCount": int,
    },
    total=False,
)

OrganizationFeatureStatisticsTypeDef = TypedDict(
    "OrganizationFeatureStatisticsTypeDef",
    {
        "Name": OrgFeatureType,
        "EnabledAccountsCount": int,
        "AdditionalConfiguration": List[
            "OrganizationFeatureStatisticsAdditionalConfigurationTypeDef"
        ],
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

OrganizationStatisticsTypeDef = TypedDict(
    "OrganizationStatisticsTypeDef",
    {
        "TotalAccountsCount": int,
        "MemberAccountsCount": int,
        "ActiveAccountsCount": int,
        "EnabledAccountsCount": int,
        "CountByFeature": List["OrganizationFeatureStatisticsTypeDef"],
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

ProcessDetailsTypeDef = TypedDict(
    "ProcessDetailsTypeDef",
    {
        "Name": str,
        "ExecutablePath": str,
        "ExecutableSha256": str,
        "NamespacePid": int,
        "Pwd": str,
        "Pid": int,
        "StartTime": datetime,
        "Uuid": str,
        "ParentUuid": str,
        "User": str,
        "UserId": int,
        "Euid": int,
        "Lineage": List["LineageObjectTypeDef"],
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

RdsDbInstanceDetailsTypeDef = TypedDict(
    "RdsDbInstanceDetailsTypeDef",
    {
        "DbInstanceIdentifier": str,
        "Engine": str,
        "EngineVersion": str,
        "DbClusterIdentifier": str,
        "DbInstanceArn": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

RdsDbUserDetailsTypeDef = TypedDict(
    "RdsDbUserDetailsTypeDef",
    {
        "User": str,
        "Application": str,
        "Database": str,
        "Ssl": str,
        "AuthMethod": str,
    },
    total=False,
)

RdsLoginAttemptActionTypeDef = TypedDict(
    "RdsLoginAttemptActionTypeDef",
    {
        "RemoteIpDetails": "RemoteIpDetailsTypeDef",
        "LoginAttributes": List["LoginAttributeTypeDef"],
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
        "IpAddressV6": str,
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
        "RdsDbInstanceDetails": "RdsDbInstanceDetailsTypeDef",
        "RdsDbUserDetails": "RdsDbUserDetailsTypeDef",
        "LambdaDetails": "LambdaDetailsTypeDef",
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

RuntimeContextTypeDef = TypedDict(
    "RuntimeContextTypeDef",
    {
        "ModifyingProcess": "ProcessDetailsTypeDef",
        "ModifiedAt": datetime,
        "ScriptPath": str,
        "LibraryPath": str,
        "LdPreloadValue": str,
        "SocketPath": str,
        "RuncBinaryPath": str,
        "ReleaseAgentPath": str,
        "MountSource": str,
        "MountTarget": str,
        "FileSystemType": str,
        "Flags": List[str],
        "ModuleName": str,
        "ModuleFilePath": str,
        "ModuleSha256": str,
        "ShellHistoryFilePath": str,
        "TargetProcess": "ProcessDetailsTypeDef",
        "AddressFamily": str,
        "IanaProtocolNumber": int,
        "MemoryRegions": List[str],
        "ToolName": str,
        "ToolCategory": str,
        "ServiceName": str,
        "CommandLineExample": str,
        "ThreatFilePath": str,
    },
    total=False,
)

RuntimeDetailsTypeDef = TypedDict(
    "RuntimeDetailsTypeDef",
    {
        "Process": "ProcessDetailsTypeDef",
        "Context": "RuntimeContextTypeDef",
    },
    total=False,
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
        "S3ObjectDetails": List["S3ObjectDetailTypeDef"],
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

S3ObjectDetailTypeDef = TypedDict(
    "S3ObjectDetailTypeDef",
    {
        "ObjectArn": str,
        "Key": str,
        "ETag": str,
        "Hash": str,
        "VersionId": str,
    },
    total=False,
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
        "ScanType": ScanTypeType,
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
        "AllowPrivilegeEscalation": bool,
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
        "RuntimeDetails": "RuntimeDetailsTypeDef",
        "Detection": "DetectionTypeDef",
        "MalwareScanDetails": "MalwareScanDetailsTypeDef",
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

StartMalwareScanRequestRequestTypeDef = TypedDict(
    "StartMalwareScanRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

StartMalwareScanResponseTypeDef = TypedDict(
    "StartMalwareScanResponseTypeDef",
    {
        "ScanId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "ThreatFileSha256": str,
    },
    total=False,
)

ThreatTypeDef = TypedDict(
    "ThreatTypeDef",
    {
        "Name": str,
        "Source": str,
        "ItemPaths": List["ItemPathTypeDef"],
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

UnprocessedDataSourcesResultTypeDef = TypedDict(
    "UnprocessedDataSourcesResultTypeDef",
    {
        "MalwareProtection": "MalwareProtectionConfigurationResultTypeDef",
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
        "Features": List["DetectorFeatureConfigurationTypeDef"],
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

_RequiredUpdateMalwareProtectionPlanRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMalwareProtectionPlanRequestRequestTypeDef",
    {
        "MalwareProtectionPlanId": str,
    },
)
_OptionalUpdateMalwareProtectionPlanRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMalwareProtectionPlanRequestRequestTypeDef",
    {
        "Role": str,
        "Actions": "MalwareProtectionPlanActionsTypeDef",
        "ProtectedResource": "UpdateProtectedResourceTypeDef",
    },
    total=False,
)

class UpdateMalwareProtectionPlanRequestRequestTypeDef(
    _RequiredUpdateMalwareProtectionPlanRequestRequestTypeDef,
    _OptionalUpdateMalwareProtectionPlanRequestRequestTypeDef,
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
        "Features": List["MemberFeaturesConfigurationTypeDef"],
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
    },
)
_OptionalUpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "AutoEnable": bool,
        "DataSources": "OrganizationDataSourceConfigurationsTypeDef",
        "Features": List["OrganizationFeatureConfigurationTypeDef"],
        "AutoEnableOrganizationMembers": AutoEnableMembersType,
    },
    total=False,
)

class UpdateOrganizationConfigurationRequestRequestTypeDef(
    _RequiredUpdateOrganizationConfigurationRequestRequestTypeDef,
    _OptionalUpdateOrganizationConfigurationRequestRequestTypeDef,
):
    pass

UpdateProtectedResourceTypeDef = TypedDict(
    "UpdateProtectedResourceTypeDef",
    {
        "S3Bucket": "UpdateS3BucketResourceTypeDef",
    },
    total=False,
)

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

UpdateS3BucketResourceTypeDef = TypedDict(
    "UpdateS3BucketResourceTypeDef",
    {
        "ObjectPrefixes": List[str],
    },
    total=False,
)

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

UsageCriteriaTypeDef = TypedDict(
    "UsageCriteriaTypeDef",
    {
        "AccountIds": List[str],
        "DataSources": List[DataSourceType],
        "Resources": List[str],
        "Features": List[UsageFeatureType],
    },
    total=False,
)

UsageDataSourceResultTypeDef = TypedDict(
    "UsageDataSourceResultTypeDef",
    {
        "DataSource": DataSourceType,
        "Total": "TotalTypeDef",
    },
    total=False,
)

UsageFeatureResultTypeDef = TypedDict(
    "UsageFeatureResultTypeDef",
    {
        "Feature": UsageFeatureType,
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
        "TopAccountsByFeature": List["UsageTopAccountsResultTypeDef"],
        "SumByDataSource": List["UsageDataSourceResultTypeDef"],
        "SumByResource": List["UsageResourceResultTypeDef"],
        "TopResources": List["UsageResourceResultTypeDef"],
        "SumByFeature": List["UsageFeatureResultTypeDef"],
    },
    total=False,
)

UsageTopAccountResultTypeDef = TypedDict(
    "UsageTopAccountResultTypeDef",
    {
        "AccountId": str,
        "Total": "TotalTypeDef",
    },
    total=False,
)

UsageTopAccountsResultTypeDef = TypedDict(
    "UsageTopAccountsResultTypeDef",
    {
        "Feature": UsageFeatureType,
        "Accounts": List["UsageTopAccountResultTypeDef"],
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

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "SubnetIds": List[str],
        "VpcId": str,
        "SecurityGroups": List["SecurityGroupTypeDef"],
    },
    total=False,
)
