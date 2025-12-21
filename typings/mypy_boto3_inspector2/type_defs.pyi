"""
Type annotations for inspector2 service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_inspector2.type_defs import SeverityCountsTypeDef

    data: SeverityCountsTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    AccountSortByType,
    AggregationFindingTypeType,
    AggregationResourceTypeType,
    AggregationTypeType,
    AmiSortByType,
    ArchitectureType,
    AssociationResultStatusCodeType,
    AwsEcrContainerSortByType,
    CisFindingStatusType,
    CisReportFormatType,
    CisReportStatusType,
    CisResultStatusType,
    CisRuleStatusType,
    CisScanConfigurationsSortByType,
    CisScanResultDetailsSortByType,
    CisScanResultsAggregatedByChecksSortByType,
    CisScanResultsAggregatedByTargetResourceSortByType,
    CisScanStatusType,
    CisSecurityLevelType,
    CisSortOrderType,
    CisStringComparisonType,
    CisTargetStatusReasonType,
    CisTargetStatusType,
    CodeRepositoryProviderTypeType,
    CodeRepositorySortByType,
    CodeScanStatusType,
    CodeSnippetErrorCodeType,
    ConfigurationLevelType,
    ContinuousIntegrationScanEventType,
    CoverageResourceTypeType,
    CoverageStringComparisonType,
    DayType,
    DelegatedAdminStatusType,
    Ec2DeepInspectionStatusType,
    Ec2InstanceSortByType,
    Ec2PlatformType,
    Ec2ScanModeStatusType,
    Ec2ScanModeType,
    EcrPullDateRescanDurationType,
    EcrPullDateRescanModeType,
    EcrRescanDurationStatusType,
    EcrRescanDurationType,
    EcrScanFrequencyType,
    ErrorCodeType,
    ExploitAvailableType,
    ExternalReportStatusType,
    FilterActionType,
    FindingDetailsErrorCodeType,
    FindingStatusType,
    FindingTypeSortByType,
    FindingTypeType,
    FixAvailableType,
    FreeTrialInfoErrorCodeType,
    FreeTrialStatusType,
    FreeTrialTypeType,
    GroupKeyType,
    ImageLayerSortByType,
    IntegrationStatusType,
    IntegrationTypeType,
    LambdaFunctionSortByType,
    LambdaLayerSortByType,
    ListCisScansDetailLevelType,
    ListCisScansSortByType,
    NetworkProtocolType,
    OperationType,
    PackageManagerType,
    PackageSortByType,
    PackageTypeType,
    PeriodicScanFrequencyType,
    RelationshipStatusType,
    ReportFormatType,
    ReportingErrorCodeType,
    RepositorySortByType,
    ResourceScanTypeType,
    ResourceStringComparisonType,
    ResourceTypeType,
    RuleSetCategoryType,
    RuntimeType,
    SbomReportFormatType,
    ScanModeType,
    ScanStatusCodeType,
    ScanStatusReasonType,
    ScanTypeType,
    ServiceType,
    SeverityType,
    SortFieldType,
    SortOrderType,
    StatusType,
    StopCisSessionStatusType,
    StringComparisonType,
    TitleSortByType,
    UsageTypeType,
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
    "AccountAggregationResponseTypeDef",
    "AccountAggregationTypeDef",
    "AccountStateTypeDef",
    "AccountTypeDef",
    "AggregationRequestTypeDef",
    "AggregationResponseTypeDef",
    "AmiAggregationResponseTypeDef",
    "AmiAggregationTypeDef",
    "AssociateConfigurationRequestTypeDef",
    "AssociateMemberRequestTypeDef",
    "AssociateMemberResponseTypeDef",
    "AtigDataTypeDef",
    "AutoEnableTypeDef",
    "AwsEc2InstanceDetailsTypeDef",
    "AwsEcrContainerAggregationResponseTypeDef",
    "AwsEcrContainerAggregationTypeDef",
    "AwsEcrContainerImageDetailsTypeDef",
    "AwsEcsMetadataDetailsTypeDef",
    "AwsEksMetadataDetailsTypeDef",
    "AwsEksWorkloadInfoTypeDef",
    "AwsLambdaFunctionDetailsTypeDef",
    "BatchAssociateCodeSecurityScanConfigurationRequestTypeDef",
    "BatchAssociateCodeSecurityScanConfigurationResponseTypeDef",
    "BatchDisassociateCodeSecurityScanConfigurationRequestTypeDef",
    "BatchDisassociateCodeSecurityScanConfigurationResponseTypeDef",
    "BatchGetAccountStatusRequestTypeDef",
    "BatchGetAccountStatusResponseTypeDef",
    "BatchGetCodeSnippetRequestTypeDef",
    "BatchGetCodeSnippetResponseTypeDef",
    "BatchGetFindingDetailsRequestTypeDef",
    "BatchGetFindingDetailsResponseTypeDef",
    "BatchGetFreeTrialInfoRequestTypeDef",
    "BatchGetFreeTrialInfoResponseTypeDef",
    "BatchGetMemberEc2DeepInspectionStatusRequestTypeDef",
    "BatchGetMemberEc2DeepInspectionStatusResponseTypeDef",
    "BatchUpdateMemberEc2DeepInspectionStatusRequestTypeDef",
    "BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef",
    "BlobTypeDef",
    "CancelFindingsReportRequestTypeDef",
    "CancelFindingsReportResponseTypeDef",
    "CancelSbomExportRequestTypeDef",
    "CancelSbomExportResponseTypeDef",
    "CisCheckAggregationTypeDef",
    "CisDateFilterTypeDef",
    "CisFindingStatusFilterTypeDef",
    "CisNumberFilterTypeDef",
    "CisResultStatusFilterTypeDef",
    "CisScanConfigurationTypeDef",
    "CisScanResultDetailsFilterCriteriaTypeDef",
    "CisScanResultDetailsTypeDef",
    "CisScanResultsAggregatedByChecksFilterCriteriaTypeDef",
    "CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef",
    "CisScanStatusFilterTypeDef",
    "CisScanTypeDef",
    "CisSecurityLevelFilterTypeDef",
    "CisSessionMessageTypeDef",
    "CisStringFilterTypeDef",
    "CisTargetResourceAggregationTypeDef",
    "CisTargetStatusFilterTypeDef",
    "CisTargetStatusReasonFilterTypeDef",
    "CisTargetsTypeDef",
    "CisaDataTypeDef",
    "ClusterDetailsTypeDef",
    "ClusterForImageFilterCriteriaTypeDef",
    "ClusterInformationTypeDef",
    "ClusterMetadataTypeDef",
    "CodeFilePathTypeDef",
    "CodeLineTypeDef",
    "CodeRepositoryAggregationResponseTypeDef",
    "CodeRepositoryAggregationTypeDef",
    "CodeRepositoryDetailsTypeDef",
    "CodeRepositoryMetadataTypeDef",
    "CodeRepositoryOnDemandScanTypeDef",
    "CodeSecurityIntegrationSummaryTypeDef",
    "CodeSecurityResourceTypeDef",
    "CodeSecurityScanConfigurationAssociationSummaryTypeDef",
    "CodeSecurityScanConfigurationOutputTypeDef",
    "CodeSecurityScanConfigurationSummaryTypeDef",
    "CodeSecurityScanConfigurationTypeDef",
    "CodeSecurityScanConfigurationUnionTypeDef",
    "CodeSnippetErrorTypeDef",
    "CodeSnippetResultTypeDef",
    "CodeVulnerabilityDetailsTypeDef",
    "ComputePlatformTypeDef",
    "ContinuousIntegrationScanConfigurationOutputTypeDef",
    "ContinuousIntegrationScanConfigurationTypeDef",
    "CountsTypeDef",
    "CoverageDateFilterTypeDef",
    "CoverageFilterCriteriaTypeDef",
    "CoverageMapFilterTypeDef",
    "CoverageNumberFilterTypeDef",
    "CoverageStringFilterTypeDef",
    "CoveredResourceTypeDef",
    "CreateCisScanConfigurationRequestTypeDef",
    "CreateCisScanConfigurationResponseTypeDef",
    "CreateCisTargetsTypeDef",
    "CreateCodeSecurityIntegrationRequestTypeDef",
    "CreateCodeSecurityIntegrationResponseTypeDef",
    "CreateCodeSecurityScanConfigurationRequestTypeDef",
    "CreateCodeSecurityScanConfigurationResponseTypeDef",
    "CreateFilterRequestTypeDef",
    "CreateFilterResponseTypeDef",
    "CreateFindingsReportRequestTypeDef",
    "CreateFindingsReportResponseTypeDef",
    "CreateGitLabSelfManagedIntegrationDetailTypeDef",
    "CreateIntegrationDetailTypeDef",
    "CreateSbomExportRequestTypeDef",
    "CreateSbomExportResponseTypeDef",
    "Cvss2TypeDef",
    "Cvss3TypeDef",
    "Cvss4TypeDef",
    "CvssScoreAdjustmentTypeDef",
    "CvssScoreDetailsTypeDef",
    "CvssScoreTypeDef",
    "DailyScheduleTypeDef",
    "DateFilterOutputTypeDef",
    "DateFilterTypeDef",
    "DateFilterUnionTypeDef",
    "DelegatedAdminAccountTypeDef",
    "DelegatedAdminTypeDef",
    "DeleteCisScanConfigurationRequestTypeDef",
    "DeleteCisScanConfigurationResponseTypeDef",
    "DeleteCodeSecurityIntegrationRequestTypeDef",
    "DeleteCodeSecurityIntegrationResponseTypeDef",
    "DeleteCodeSecurityScanConfigurationRequestTypeDef",
    "DeleteCodeSecurityScanConfigurationResponseTypeDef",
    "DeleteFilterRequestTypeDef",
    "DeleteFilterResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DestinationTypeDef",
    "DisableDelegatedAdminAccountRequestTypeDef",
    "DisableDelegatedAdminAccountResponseTypeDef",
    "DisableRequestTypeDef",
    "DisableResponseTypeDef",
    "DisassociateConfigurationRequestTypeDef",
    "DisassociateMemberRequestTypeDef",
    "DisassociateMemberResponseTypeDef",
    "Ec2ConfigurationStateTypeDef",
    "Ec2ConfigurationTypeDef",
    "Ec2InstanceAggregationResponseTypeDef",
    "Ec2InstanceAggregationTypeDef",
    "Ec2MetadataTypeDef",
    "Ec2ScanModeStateTypeDef",
    "EcrConfigurationStateTypeDef",
    "EcrConfigurationTypeDef",
    "EcrContainerImageMetadataTypeDef",
    "EcrRepositoryMetadataTypeDef",
    "EcrRescanDurationStateTypeDef",
    "EnableDelegatedAdminAccountRequestTypeDef",
    "EnableDelegatedAdminAccountResponseTypeDef",
    "EnableRequestTypeDef",
    "EnableResponseTypeDef",
    "EpssDetailsTypeDef",
    "EpssTypeDef",
    "EvidenceTypeDef",
    "ExploitObservedTypeDef",
    "ExploitabilityDetailsTypeDef",
    "FailedAccountTypeDef",
    "FailedAssociationResultTypeDef",
    "FailedMemberAccountEc2DeepInspectionStatusStateTypeDef",
    "FilterCriteriaOutputTypeDef",
    "FilterCriteriaTypeDef",
    "FilterCriteriaUnionTypeDef",
    "FilterTypeDef",
    "FindingDetailTypeDef",
    "FindingDetailsErrorTypeDef",
    "FindingTypeAggregationResponseTypeDef",
    "FindingTypeAggregationTypeDef",
    "FindingTypeDef",
    "FreeTrialAccountInfoTypeDef",
    "FreeTrialInfoErrorTypeDef",
    "FreeTrialInfoTypeDef",
    "GetCisScanReportRequestTypeDef",
    "GetCisScanReportResponseTypeDef",
    "GetCisScanResultDetailsRequestPaginateTypeDef",
    "GetCisScanResultDetailsRequestTypeDef",
    "GetCisScanResultDetailsResponseTypeDef",
    "GetClustersForImageRequestPaginateTypeDef",
    "GetClustersForImageRequestTypeDef",
    "GetClustersForImageResponseTypeDef",
    "GetCodeSecurityIntegrationRequestTypeDef",
    "GetCodeSecurityIntegrationResponseTypeDef",
    "GetCodeSecurityScanConfigurationRequestTypeDef",
    "GetCodeSecurityScanConfigurationResponseTypeDef",
    "GetCodeSecurityScanRequestTypeDef",
    "GetCodeSecurityScanResponseTypeDef",
    "GetConfigurationResponseTypeDef",
    "GetDelegatedAdminAccountResponseTypeDef",
    "GetEc2DeepInspectionConfigurationResponseTypeDef",
    "GetEncryptionKeyRequestTypeDef",
    "GetEncryptionKeyResponseTypeDef",
    "GetFindingsReportStatusRequestTypeDef",
    "GetFindingsReportStatusResponseTypeDef",
    "GetMemberRequestTypeDef",
    "GetMemberResponseTypeDef",
    "GetSbomExportRequestTypeDef",
    "GetSbomExportResponseTypeDef",
    "ImageLayerAggregationResponseTypeDef",
    "ImageLayerAggregationTypeDef",
    "InspectorScoreDetailsTypeDef",
    "LambdaFunctionAggregationResponseTypeDef",
    "LambdaFunctionAggregationTypeDef",
    "LambdaFunctionMetadataTypeDef",
    "LambdaLayerAggregationResponseTypeDef",
    "LambdaLayerAggregationTypeDef",
    "LambdaVpcConfigTypeDef",
    "ListAccountPermissionsRequestPaginateTypeDef",
    "ListAccountPermissionsRequestTypeDef",
    "ListAccountPermissionsResponseTypeDef",
    "ListCisScanConfigurationsFilterCriteriaTypeDef",
    "ListCisScanConfigurationsRequestPaginateTypeDef",
    "ListCisScanConfigurationsRequestTypeDef",
    "ListCisScanConfigurationsResponseTypeDef",
    "ListCisScanResultsAggregatedByChecksRequestPaginateTypeDef",
    "ListCisScanResultsAggregatedByChecksRequestTypeDef",
    "ListCisScanResultsAggregatedByChecksResponseTypeDef",
    "ListCisScanResultsAggregatedByTargetResourceRequestPaginateTypeDef",
    "ListCisScanResultsAggregatedByTargetResourceRequestTypeDef",
    "ListCisScanResultsAggregatedByTargetResourceResponseTypeDef",
    "ListCisScansFilterCriteriaTypeDef",
    "ListCisScansRequestPaginateTypeDef",
    "ListCisScansRequestTypeDef",
    "ListCisScansResponseTypeDef",
    "ListCodeSecurityIntegrationsRequestTypeDef",
    "ListCodeSecurityIntegrationsResponseTypeDef",
    "ListCodeSecurityScanConfigurationAssociationsRequestTypeDef",
    "ListCodeSecurityScanConfigurationAssociationsResponseTypeDef",
    "ListCodeSecurityScanConfigurationsRequestTypeDef",
    "ListCodeSecurityScanConfigurationsResponseTypeDef",
    "ListCoverageRequestPaginateTypeDef",
    "ListCoverageRequestTypeDef",
    "ListCoverageResponseTypeDef",
    "ListCoverageStatisticsRequestPaginateTypeDef",
    "ListCoverageStatisticsRequestTypeDef",
    "ListCoverageStatisticsResponseTypeDef",
    "ListDelegatedAdminAccountsRequestPaginateTypeDef",
    "ListDelegatedAdminAccountsRequestTypeDef",
    "ListDelegatedAdminAccountsResponseTypeDef",
    "ListFiltersRequestPaginateTypeDef",
    "ListFiltersRequestTypeDef",
    "ListFiltersResponseTypeDef",
    "ListFindingAggregationsRequestPaginateTypeDef",
    "ListFindingAggregationsRequestTypeDef",
    "ListFindingAggregationsResponseTypeDef",
    "ListFindingsRequestPaginateTypeDef",
    "ListFindingsRequestTypeDef",
    "ListFindingsResponseTypeDef",
    "ListMembersRequestPaginateTypeDef",
    "ListMembersRequestTypeDef",
    "ListMembersResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsageTotalsRequestPaginateTypeDef",
    "ListUsageTotalsRequestTypeDef",
    "ListUsageTotalsResponseTypeDef",
    "MapFilterTypeDef",
    "MemberAccountEc2DeepInspectionStatusStateTypeDef",
    "MemberAccountEc2DeepInspectionStatusTypeDef",
    "MemberTypeDef",
    "MonthlyScheduleTypeDef",
    "NetworkPathTypeDef",
    "NetworkReachabilityDetailsTypeDef",
    "NumberFilterTypeDef",
    "PackageAggregationResponseTypeDef",
    "PackageAggregationTypeDef",
    "PackageFilterTypeDef",
    "PackageVulnerabilityDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "PeriodicScanConfigurationTypeDef",
    "PermissionTypeDef",
    "PortRangeFilterTypeDef",
    "PortRangeTypeDef",
    "ProjectCodeSecurityScanConfigurationTypeDef",
    "ProjectContinuousIntegrationScanConfigurationTypeDef",
    "ProjectPeriodicScanConfigurationTypeDef",
    "RecommendationTypeDef",
    "RemediationTypeDef",
    "RepositoryAggregationResponseTypeDef",
    "RepositoryAggregationTypeDef",
    "ResetEncryptionKeyRequestTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceFilterCriteriaOutputTypeDef",
    "ResourceFilterCriteriaTypeDef",
    "ResourceFilterCriteriaUnionTypeDef",
    "ResourceMapFilterTypeDef",
    "ResourceScanMetadataTypeDef",
    "ResourceStateTypeDef",
    "ResourceStatusTypeDef",
    "ResourceStringFilterTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "ScanStatusTypeDef",
    "ScheduleOutputTypeDef",
    "ScheduleTypeDef",
    "ScheduleUnionTypeDef",
    "ScopeSettingsTypeDef",
    "SearchVulnerabilitiesFilterCriteriaTypeDef",
    "SearchVulnerabilitiesRequestPaginateTypeDef",
    "SearchVulnerabilitiesRequestTypeDef",
    "SearchVulnerabilitiesResponseTypeDef",
    "SendCisSessionHealthRequestTypeDef",
    "SendCisSessionTelemetryRequestTypeDef",
    "SeverityCountsTypeDef",
    "SortCriteriaTypeDef",
    "StartCisSessionMessageTypeDef",
    "StartCisSessionRequestTypeDef",
    "StartCodeSecurityScanRequestTypeDef",
    "StartCodeSecurityScanResponseTypeDef",
    "StateTypeDef",
    "StatusCountsTypeDef",
    "StepTypeDef",
    "StopCisMessageProgressTypeDef",
    "StopCisSessionMessageTypeDef",
    "StopCisSessionRequestTypeDef",
    "StringFilterTypeDef",
    "SuccessfulAssociationResultTypeDef",
    "SuggestedFixTypeDef",
    "TagFilterTypeDef",
    "TagResourceRequestTypeDef",
    "TimeTypeDef",
    "TimestampTypeDef",
    "TitleAggregationResponseTypeDef",
    "TitleAggregationTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateCisScanConfigurationRequestTypeDef",
    "UpdateCisScanConfigurationResponseTypeDef",
    "UpdateCisTargetsTypeDef",
    "UpdateCodeSecurityIntegrationRequestTypeDef",
    "UpdateCodeSecurityIntegrationResponseTypeDef",
    "UpdateCodeSecurityScanConfigurationRequestTypeDef",
    "UpdateCodeSecurityScanConfigurationResponseTypeDef",
    "UpdateConfigurationRequestTypeDef",
    "UpdateEc2DeepInspectionConfigurationRequestTypeDef",
    "UpdateEc2DeepInspectionConfigurationResponseTypeDef",
    "UpdateEncryptionKeyRequestTypeDef",
    "UpdateFilterRequestTypeDef",
    "UpdateFilterResponseTypeDef",
    "UpdateGitHubIntegrationDetailTypeDef",
    "UpdateGitLabSelfManagedIntegrationDetailTypeDef",
    "UpdateIntegrationDetailsTypeDef",
    "UpdateOrgEc2DeepInspectionConfigurationRequestTypeDef",
    "UpdateOrganizationConfigurationRequestTypeDef",
    "UpdateOrganizationConfigurationResponseTypeDef",
    "UsageTotalTypeDef",
    "UsageTypeDef",
    "VulnerabilityTypeDef",
    "VulnerablePackageTypeDef",
    "WeeklyScheduleOutputTypeDef",
    "WeeklyScheduleTypeDef",
)

SeverityCountsTypeDef = TypedDict(
    "SeverityCountsTypeDef",
    {
        "all": NotRequired[int],
        "medium": NotRequired[int],
        "high": NotRequired[int],
        "critical": NotRequired[int],
    },
)

class AccountAggregationTypeDef(TypedDict):
    findingType: NotRequired[AggregationFindingTypeType]
    resourceType: NotRequired[AggregationResourceTypeType]
    sortOrder: NotRequired[SortOrderType]
    sortBy: NotRequired[AccountSortByType]

class StateTypeDef(TypedDict):
    status: StatusType
    errorCode: ErrorCodeType
    errorMessage: str

ResourceStatusTypeDef = TypedDict(
    "ResourceStatusTypeDef",
    {
        "ec2": StatusType,
        "ecr": StatusType,
        "lambda": NotRequired[StatusType],
        "lambdaCode": NotRequired[StatusType],
        "codeRepository": NotRequired[StatusType],
    },
)

class FindingTypeAggregationTypeDef(TypedDict):
    findingType: NotRequired[AggregationFindingTypeType]
    resourceType: NotRequired[AggregationResourceTypeType]
    sortOrder: NotRequired[SortOrderType]
    sortBy: NotRequired[FindingTypeSortByType]

class StringFilterTypeDef(TypedDict):
    comparison: StringComparisonType
    value: str

class CodeSecurityResourceTypeDef(TypedDict):
    projectId: NotRequired[str]

class AssociateMemberRequestTypeDef(TypedDict):
    accountId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AtigDataTypeDef(TypedDict):
    firstSeen: NotRequired[datetime]
    lastSeen: NotRequired[datetime]
    targets: NotRequired[List[str]]
    ttps: NotRequired[List[str]]

AutoEnableTypeDef = TypedDict(
    "AutoEnableTypeDef",
    {
        "ec2": bool,
        "ecr": bool,
        "lambda": NotRequired[bool],
        "lambdaCode": NotRequired[bool],
        "codeRepository": NotRequired[bool],
    },
)
AwsEc2InstanceDetailsTypeDef = TypedDict(
    "AwsEc2InstanceDetailsTypeDef",
    {
        "type": NotRequired[str],
        "imageId": NotRequired[str],
        "ipV4Addresses": NotRequired[List[str]],
        "ipV6Addresses": NotRequired[List[str]],
        "keyName": NotRequired[str],
        "iamInstanceProfileArn": NotRequired[str],
        "vpcId": NotRequired[str],
        "subnetId": NotRequired[str],
        "launchedAt": NotRequired[datetime],
        "platform": NotRequired[str],
    },
)

class NumberFilterTypeDef(TypedDict):
    upperInclusive: NotRequired[float]
    lowerInclusive: NotRequired[float]

class AwsEcrContainerImageDetailsTypeDef(TypedDict):
    repositoryName: str
    imageHash: str
    registry: str
    imageTags: NotRequired[List[str]]
    pushedAt: NotRequired[datetime]
    author: NotRequired[str]
    architecture: NotRequired[str]
    platform: NotRequired[str]
    lastInUseAt: NotRequired[datetime]
    inUseCount: NotRequired[int]

class AwsEcsMetadataDetailsTypeDef(TypedDict):
    detailsGroup: str
    taskDefinitionArn: str

AwsEksWorkloadInfoTypeDef = TypedDict(
    "AwsEksWorkloadInfoTypeDef",
    {
        "name": str,
        "type": str,
    },
)

class LambdaVpcConfigTypeDef(TypedDict):
    subnetIds: NotRequired[List[str]]
    securityGroupIds: NotRequired[List[str]]
    vpcId: NotRequired[str]

class BatchGetAccountStatusRequestTypeDef(TypedDict):
    accountIds: NotRequired[Sequence[str]]

class BatchGetCodeSnippetRequestTypeDef(TypedDict):
    findingArns: Sequence[str]

class CodeSnippetErrorTypeDef(TypedDict):
    findingArn: str
    errorCode: CodeSnippetErrorCodeType
    errorMessage: str

class BatchGetFindingDetailsRequestTypeDef(TypedDict):
    findingArns: Sequence[str]

class FindingDetailsErrorTypeDef(TypedDict):
    findingArn: str
    errorCode: FindingDetailsErrorCodeType
    errorMessage: str

class BatchGetFreeTrialInfoRequestTypeDef(TypedDict):
    accountIds: Sequence[str]

class FreeTrialInfoErrorTypeDef(TypedDict):
    accountId: str
    code: FreeTrialInfoErrorCodeType
    message: str

class BatchGetMemberEc2DeepInspectionStatusRequestTypeDef(TypedDict):
    accountIds: NotRequired[Sequence[str]]

class FailedMemberAccountEc2DeepInspectionStatusStateTypeDef(TypedDict):
    accountId: str
    ec2ScanStatus: NotRequired[StatusType]
    errorMessage: NotRequired[str]

class MemberAccountEc2DeepInspectionStatusStateTypeDef(TypedDict):
    accountId: str
    status: NotRequired[Ec2DeepInspectionStatusType]
    errorMessage: NotRequired[str]

class MemberAccountEc2DeepInspectionStatusTypeDef(TypedDict):
    accountId: str
    activateDeepInspection: bool

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CancelFindingsReportRequestTypeDef(TypedDict):
    reportId: str

class CancelSbomExportRequestTypeDef(TypedDict):
    reportId: str

class StatusCountsTypeDef(TypedDict):
    failed: NotRequired[int]
    skipped: NotRequired[int]
    passed: NotRequired[int]

TimestampTypeDef = Union[datetime, str]

class CisFindingStatusFilterTypeDef(TypedDict):
    comparison: Literal["EQUALS"]
    value: CisFindingStatusType

class CisNumberFilterTypeDef(TypedDict):
    upperInclusive: NotRequired[int]
    lowerInclusive: NotRequired[int]

class CisResultStatusFilterTypeDef(TypedDict):
    comparison: Literal["EQUALS"]
    value: CisResultStatusType

class CisTargetsTypeDef(TypedDict):
    accountIds: NotRequired[List[str]]
    targetResourceTags: NotRequired[Dict[str, List[str]]]

class CisSecurityLevelFilterTypeDef(TypedDict):
    comparison: Literal["EQUALS"]
    value: CisSecurityLevelType

class CisStringFilterTypeDef(TypedDict):
    comparison: CisStringComparisonType
    value: str

class CisScanResultDetailsTypeDef(TypedDict):
    scanArn: str
    accountId: NotRequired[str]
    targetResourceId: NotRequired[str]
    platform: NotRequired[str]
    status: NotRequired[CisFindingStatusType]
    statusReason: NotRequired[str]
    checkId: NotRequired[str]
    title: NotRequired[str]
    checkDescription: NotRequired[str]
    remediation: NotRequired[str]
    level: NotRequired[CisSecurityLevelType]
    findingArn: NotRequired[str]

class CisTargetStatusFilterTypeDef(TypedDict):
    comparison: Literal["EQUALS"]
    value: CisTargetStatusType

class CisTargetStatusReasonFilterTypeDef(TypedDict):
    comparison: Literal["EQUALS"]
    value: CisTargetStatusReasonType

class TagFilterTypeDef(TypedDict):
    comparison: Literal["EQUALS"]
    key: str
    value: str

class CisScanStatusFilterTypeDef(TypedDict):
    comparison: Literal["EQUALS"]
    value: CisScanStatusType

class CisaDataTypeDef(TypedDict):
    dateAdded: NotRequired[datetime]
    dateDue: NotRequired[datetime]
    action: NotRequired[str]

class ClusterForImageFilterCriteriaTypeDef(TypedDict):
    resourceId: str

class CodeFilePathTypeDef(TypedDict):
    fileName: str
    filePath: str
    startLine: int
    endLine: int

class CodeLineTypeDef(TypedDict):
    content: str
    lineNumber: int

class CodeRepositoryDetailsTypeDef(TypedDict):
    projectName: NotRequired[str]
    integrationArn: NotRequired[str]
    providerType: NotRequired[CodeRepositoryProviderTypeType]

class ScanStatusTypeDef(TypedDict):
    statusCode: ScanStatusCodeType
    reason: ScanStatusReasonType

CodeSecurityIntegrationSummaryTypeDef = TypedDict(
    "CodeSecurityIntegrationSummaryTypeDef",
    {
        "integrationArn": str,
        "name": str,
        "type": IntegrationTypeType,
        "status": IntegrationStatusType,
        "statusReason": str,
        "createdOn": datetime,
        "lastUpdateOn": datetime,
        "tags": NotRequired[Dict[str, str]],
    },
)

class ContinuousIntegrationScanConfigurationOutputTypeDef(TypedDict):
    supportedEvents: List[ContinuousIntegrationScanEventType]

class PeriodicScanConfigurationTypeDef(TypedDict):
    frequency: NotRequired[PeriodicScanFrequencyType]
    frequencyExpression: NotRequired[str]

class ScopeSettingsTypeDef(TypedDict):
    projectSelectionScope: NotRequired[Literal["ALL"]]

class ContinuousIntegrationScanConfigurationTypeDef(TypedDict):
    supportedEvents: Sequence[ContinuousIntegrationScanEventType]

class SuggestedFixTypeDef(TypedDict):
    description: NotRequired[str]
    code: NotRequired[str]

class ComputePlatformTypeDef(TypedDict):
    vendor: NotRequired[str]
    product: NotRequired[str]
    version: NotRequired[str]

class CountsTypeDef(TypedDict):
    count: NotRequired[int]
    groupKey: NotRequired[GroupKeyType]

class CoverageMapFilterTypeDef(TypedDict):
    comparison: Literal["EQUALS"]
    key: str
    value: NotRequired[str]

class CoverageNumberFilterTypeDef(TypedDict):
    upperInclusive: NotRequired[int]
    lowerInclusive: NotRequired[int]

class CoverageStringFilterTypeDef(TypedDict):
    comparison: CoverageStringComparisonType
    value: str

class CreateCisTargetsTypeDef(TypedDict):
    accountIds: Sequence[str]
    targetResourceTags: Mapping[str, Sequence[str]]

class DestinationTypeDef(TypedDict):
    bucketName: str
    kmsKeyArn: str
    keyPrefix: NotRequired[str]

class CreateGitLabSelfManagedIntegrationDetailTypeDef(TypedDict):
    instanceUrl: str
    accessToken: str

class Cvss2TypeDef(TypedDict):
    baseScore: NotRequired[float]
    scoringVector: NotRequired[str]

class Cvss3TypeDef(TypedDict):
    baseScore: NotRequired[float]
    scoringVector: NotRequired[str]

class Cvss4TypeDef(TypedDict):
    baseScore: NotRequired[float]
    scoringVector: NotRequired[str]

class CvssScoreAdjustmentTypeDef(TypedDict):
    metric: str
    reason: str

class CvssScoreTypeDef(TypedDict):
    baseScore: float
    scoringVector: str
    version: str
    source: str

class TimeTypeDef(TypedDict):
    timeOfDay: str
    timezone: str

class DateFilterOutputTypeDef(TypedDict):
    startInclusive: NotRequired[datetime]
    endInclusive: NotRequired[datetime]

class DelegatedAdminAccountTypeDef(TypedDict):
    accountId: NotRequired[str]
    status: NotRequired[DelegatedAdminStatusType]

class DelegatedAdminTypeDef(TypedDict):
    accountId: NotRequired[str]
    relationshipStatus: NotRequired[RelationshipStatusType]

class DeleteCisScanConfigurationRequestTypeDef(TypedDict):
    scanConfigurationArn: str

class DeleteCodeSecurityIntegrationRequestTypeDef(TypedDict):
    integrationArn: str

class DeleteCodeSecurityScanConfigurationRequestTypeDef(TypedDict):
    scanConfigurationArn: str

class DeleteFilterRequestTypeDef(TypedDict):
    arn: str

class DisableDelegatedAdminAccountRequestTypeDef(TypedDict):
    delegatedAdminAccountId: str

class DisableRequestTypeDef(TypedDict):
    accountIds: NotRequired[Sequence[str]]
    resourceTypes: NotRequired[Sequence[ResourceScanTypeType]]

class DisassociateMemberRequestTypeDef(TypedDict):
    accountId: str

class Ec2ScanModeStateTypeDef(TypedDict):
    scanMode: NotRequired[Ec2ScanModeType]
    scanModeStatus: NotRequired[Ec2ScanModeStatusType]

class Ec2ConfigurationTypeDef(TypedDict):
    scanMode: Ec2ScanModeType

class MapFilterTypeDef(TypedDict):
    comparison: Literal["EQUALS"]
    key: str
    value: NotRequired[str]

class Ec2MetadataTypeDef(TypedDict):
    tags: NotRequired[Dict[str, str]]
    amiId: NotRequired[str]
    platform: NotRequired[Ec2PlatformType]

class EcrRescanDurationStateTypeDef(TypedDict):
    rescanDuration: NotRequired[EcrRescanDurationType]
    status: NotRequired[EcrRescanDurationStatusType]
    updatedAt: NotRequired[datetime]
    pullDateRescanDuration: NotRequired[EcrPullDateRescanDurationType]
    pullDateRescanMode: NotRequired[EcrPullDateRescanModeType]

class EcrConfigurationTypeDef(TypedDict):
    rescanDuration: EcrRescanDurationType
    pullDateRescanDuration: NotRequired[EcrPullDateRescanDurationType]
    pullDateRescanMode: NotRequired[EcrPullDateRescanModeType]

class EcrContainerImageMetadataTypeDef(TypedDict):
    tags: NotRequired[List[str]]
    imagePulledAt: NotRequired[datetime]
    lastInUseAt: NotRequired[datetime]
    inUseCount: NotRequired[int]

class EcrRepositoryMetadataTypeDef(TypedDict):
    name: NotRequired[str]
    scanFrequency: NotRequired[EcrScanFrequencyType]

class EnableDelegatedAdminAccountRequestTypeDef(TypedDict):
    delegatedAdminAccountId: str
    clientToken: NotRequired[str]

class EnableRequestTypeDef(TypedDict):
    resourceTypes: Sequence[ResourceScanTypeType]
    accountIds: NotRequired[Sequence[str]]
    clientToken: NotRequired[str]

class EpssDetailsTypeDef(TypedDict):
    score: NotRequired[float]

class EpssTypeDef(TypedDict):
    score: NotRequired[float]

class EvidenceTypeDef(TypedDict):
    evidenceRule: NotRequired[str]
    evidenceDetail: NotRequired[str]
    severity: NotRequired[str]

class ExploitObservedTypeDef(TypedDict):
    lastSeen: NotRequired[datetime]
    firstSeen: NotRequired[datetime]

class ExploitabilityDetailsTypeDef(TypedDict):
    lastKnownExploitAt: NotRequired[datetime]

class PortRangeFilterTypeDef(TypedDict):
    beginInclusive: NotRequired[int]
    endInclusive: NotRequired[int]

FreeTrialInfoTypeDef = TypedDict(
    "FreeTrialInfoTypeDef",
    {
        "type": FreeTrialTypeType,
        "start": datetime,
        "end": datetime,
        "status": FreeTrialStatusType,
    },
)

class GetCisScanReportRequestTypeDef(TypedDict):
    scanArn: str
    targetAccounts: NotRequired[Sequence[str]]
    reportFormat: NotRequired[CisReportFormatType]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetCodeSecurityIntegrationRequestTypeDef(TypedDict):
    integrationArn: str
    tags: NotRequired[Mapping[str, str]]

class GetCodeSecurityScanConfigurationRequestTypeDef(TypedDict):
    scanConfigurationArn: str

class GetEncryptionKeyRequestTypeDef(TypedDict):
    scanType: ScanTypeType
    resourceType: ResourceTypeType

class GetFindingsReportStatusRequestTypeDef(TypedDict):
    reportId: NotRequired[str]

class GetMemberRequestTypeDef(TypedDict):
    accountId: str

class MemberTypeDef(TypedDict):
    accountId: NotRequired[str]
    relationshipStatus: NotRequired[RelationshipStatusType]
    delegatedAdminAccountId: NotRequired[str]
    updatedAt: NotRequired[datetime]

class GetSbomExportRequestTypeDef(TypedDict):
    reportId: str

class LambdaFunctionMetadataTypeDef(TypedDict):
    functionTags: NotRequired[Dict[str, str]]
    layers: NotRequired[List[str]]
    functionName: NotRequired[str]
    runtime: NotRequired[RuntimeType]

class ListAccountPermissionsRequestTypeDef(TypedDict):
    service: NotRequired[ServiceType]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class PermissionTypeDef(TypedDict):
    service: ServiceType
    operation: OperationType

class ListCodeSecurityIntegrationsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListCodeSecurityScanConfigurationAssociationsRequestTypeDef(TypedDict):
    scanConfigurationArn: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListCodeSecurityScanConfigurationsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListDelegatedAdminAccountsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListFiltersRequestTypeDef(TypedDict):
    arns: NotRequired[Sequence[str]]
    action: NotRequired[FilterActionType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class SortCriteriaTypeDef(TypedDict):
    field: SortFieldType
    sortOrder: SortOrderType

class ListMembersRequestTypeDef(TypedDict):
    onlyAssociated: NotRequired[bool]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListUsageTotalsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    accountIds: NotRequired[Sequence[str]]

class StepTypeDef(TypedDict):
    componentId: str
    componentType: str
    componentArn: NotRequired[str]

class PortRangeTypeDef(TypedDict):
    begin: int
    end: int

class VulnerablePackageTypeDef(TypedDict):
    name: str
    version: str
    sourceLayerHash: NotRequired[str]
    epoch: NotRequired[int]
    release: NotRequired[str]
    arch: NotRequired[str]
    packageManager: NotRequired[PackageManagerType]
    filePath: NotRequired[str]
    fixedInVersion: NotRequired[str]
    remediation: NotRequired[str]
    sourceLambdaLayerArn: NotRequired[str]

class ProjectContinuousIntegrationScanConfigurationTypeDef(TypedDict):
    supportedEvent: NotRequired[ContinuousIntegrationScanEventType]
    ruleSetCategories: NotRequired[List[RuleSetCategoryType]]

class ProjectPeriodicScanConfigurationTypeDef(TypedDict):
    frequencyExpression: NotRequired[str]
    ruleSetCategories: NotRequired[List[RuleSetCategoryType]]

class RecommendationTypeDef(TypedDict):
    text: NotRequired[str]
    Url: NotRequired[str]

class ResetEncryptionKeyRequestTypeDef(TypedDict):
    scanType: ScanTypeType
    resourceType: ResourceTypeType

class ResourceMapFilterTypeDef(TypedDict):
    comparison: Literal["EQUALS"]
    key: str
    value: NotRequired[str]

class ResourceStringFilterTypeDef(TypedDict):
    comparison: ResourceStringComparisonType
    value: str

class SearchVulnerabilitiesFilterCriteriaTypeDef(TypedDict):
    vulnerabilityIds: Sequence[str]

class SendCisSessionHealthRequestTypeDef(TypedDict):
    scanJobId: str
    sessionToken: str

class StartCisSessionMessageTypeDef(TypedDict):
    sessionToken: str

class StopCisMessageProgressTypeDef(TypedDict):
    totalChecks: NotRequired[int]
    successfulChecks: NotRequired[int]
    failedChecks: NotRequired[int]
    notEvaluatedChecks: NotRequired[int]
    unknownChecks: NotRequired[int]
    notApplicableChecks: NotRequired[int]
    informationalChecks: NotRequired[int]
    errorChecks: NotRequired[int]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateCisTargetsTypeDef(TypedDict):
    accountIds: NotRequired[Sequence[str]]
    targetResourceTags: NotRequired[Mapping[str, Sequence[str]]]

class UpdateEc2DeepInspectionConfigurationRequestTypeDef(TypedDict):
    activateDeepInspection: NotRequired[bool]
    packagePaths: NotRequired[Sequence[str]]

class UpdateEncryptionKeyRequestTypeDef(TypedDict):
    kmsKeyId: str
    scanType: ScanTypeType
    resourceType: ResourceTypeType

class UpdateGitHubIntegrationDetailTypeDef(TypedDict):
    code: str
    installationId: str

class UpdateGitLabSelfManagedIntegrationDetailTypeDef(TypedDict):
    authCode: str

class UpdateOrgEc2DeepInspectionConfigurationRequestTypeDef(TypedDict):
    orgPackagePaths: Sequence[str]

UsageTypeDef = TypedDict(
    "UsageTypeDef",
    {
        "type": NotRequired[UsageTypeType],
        "total": NotRequired[float],
        "estimatedMonthlyCost": NotRequired[float],
        "currency": NotRequired[Literal["USD"]],
    },
)

class AccountAggregationResponseTypeDef(TypedDict):
    accountId: NotRequired[str]
    severityCounts: NotRequired[SeverityCountsTypeDef]
    exploitAvailableCount: NotRequired[int]
    fixAvailableCount: NotRequired[int]

class AmiAggregationResponseTypeDef(TypedDict):
    ami: str
    accountId: NotRequired[str]
    severityCounts: NotRequired[SeverityCountsTypeDef]
    affectedInstances: NotRequired[int]

class AwsEcrContainerAggregationResponseTypeDef(TypedDict):
    resourceId: str
    imageSha: NotRequired[str]
    repository: NotRequired[str]
    architecture: NotRequired[str]
    imageTags: NotRequired[List[str]]
    accountId: NotRequired[str]
    severityCounts: NotRequired[SeverityCountsTypeDef]
    lastInUseAt: NotRequired[datetime]
    inUseCount: NotRequired[int]

class CodeRepositoryAggregationResponseTypeDef(TypedDict):
    projectNames: str
    providerType: NotRequired[str]
    severityCounts: NotRequired[SeverityCountsTypeDef]
    exploitAvailableActiveFindingsCount: NotRequired[int]
    fixAvailableActiveFindingsCount: NotRequired[int]
    accountId: NotRequired[str]
    resourceId: NotRequired[str]

class Ec2InstanceAggregationResponseTypeDef(TypedDict):
    instanceId: str
    ami: NotRequired[str]
    operatingSystem: NotRequired[str]
    instanceTags: NotRequired[Dict[str, str]]
    accountId: NotRequired[str]
    severityCounts: NotRequired[SeverityCountsTypeDef]
    networkFindings: NotRequired[int]

class FindingTypeAggregationResponseTypeDef(TypedDict):
    accountId: NotRequired[str]
    severityCounts: NotRequired[SeverityCountsTypeDef]
    exploitAvailableCount: NotRequired[int]
    fixAvailableCount: NotRequired[int]

class ImageLayerAggregationResponseTypeDef(TypedDict):
    repository: str
    resourceId: str
    layerHash: str
    accountId: str
    severityCounts: NotRequired[SeverityCountsTypeDef]

class LambdaFunctionAggregationResponseTypeDef(TypedDict):
    resourceId: str
    functionName: NotRequired[str]
    runtime: NotRequired[str]
    lambdaTags: NotRequired[Dict[str, str]]
    accountId: NotRequired[str]
    severityCounts: NotRequired[SeverityCountsTypeDef]
    lastModifiedAt: NotRequired[datetime]

class LambdaLayerAggregationResponseTypeDef(TypedDict):
    functionName: str
    resourceId: str
    layerArn: str
    accountId: str
    severityCounts: NotRequired[SeverityCountsTypeDef]

class PackageAggregationResponseTypeDef(TypedDict):
    packageName: str
    accountId: NotRequired[str]
    severityCounts: NotRequired[SeverityCountsTypeDef]

class RepositoryAggregationResponseTypeDef(TypedDict):
    repository: str
    accountId: NotRequired[str]
    severityCounts: NotRequired[SeverityCountsTypeDef]
    affectedImages: NotRequired[int]

class TitleAggregationResponseTypeDef(TypedDict):
    title: str
    vulnerabilityId: NotRequired[str]
    accountId: NotRequired[str]
    severityCounts: NotRequired[SeverityCountsTypeDef]

ResourceStateTypeDef = TypedDict(
    "ResourceStateTypeDef",
    {
        "ec2": StateTypeDef,
        "ecr": StateTypeDef,
        "lambda": NotRequired[StateTypeDef],
        "lambdaCode": NotRequired[StateTypeDef],
        "codeRepository": NotRequired[StateTypeDef],
    },
)

class AccountTypeDef(TypedDict):
    accountId: str
    status: StatusType
    resourceStatus: ResourceStatusTypeDef

class FailedAccountTypeDef(TypedDict):
    accountId: str
    errorCode: ErrorCodeType
    errorMessage: str
    status: NotRequired[StatusType]
    resourceStatus: NotRequired[ResourceStatusTypeDef]

class AmiAggregationTypeDef(TypedDict):
    amis: NotRequired[Sequence[StringFilterTypeDef]]
    sortOrder: NotRequired[SortOrderType]
    sortBy: NotRequired[AmiSortByType]

class CodeRepositoryAggregationTypeDef(TypedDict):
    projectNames: NotRequired[Sequence[StringFilterTypeDef]]
    providerTypes: NotRequired[Sequence[StringFilterTypeDef]]
    sortOrder: NotRequired[SortOrderType]
    sortBy: NotRequired[CodeRepositorySortByType]
    resourceIds: NotRequired[Sequence[StringFilterTypeDef]]

class ImageLayerAggregationTypeDef(TypedDict):
    repositories: NotRequired[Sequence[StringFilterTypeDef]]
    resourceIds: NotRequired[Sequence[StringFilterTypeDef]]
    layerHashes: NotRequired[Sequence[StringFilterTypeDef]]
    sortOrder: NotRequired[SortOrderType]
    sortBy: NotRequired[ImageLayerSortByType]

class LambdaLayerAggregationTypeDef(TypedDict):
    functionNames: NotRequired[Sequence[StringFilterTypeDef]]
    resourceIds: NotRequired[Sequence[StringFilterTypeDef]]
    layerArns: NotRequired[Sequence[StringFilterTypeDef]]
    sortOrder: NotRequired[SortOrderType]
    sortBy: NotRequired[LambdaLayerSortByType]

class PackageAggregationTypeDef(TypedDict):
    packageNames: NotRequired[Sequence[StringFilterTypeDef]]
    sortOrder: NotRequired[SortOrderType]
    sortBy: NotRequired[PackageSortByType]

class RepositoryAggregationTypeDef(TypedDict):
    repositories: NotRequired[Sequence[StringFilterTypeDef]]
    sortOrder: NotRequired[SortOrderType]
    sortBy: NotRequired[RepositorySortByType]

class TitleAggregationTypeDef(TypedDict):
    titles: NotRequired[Sequence[StringFilterTypeDef]]
    vulnerabilityIds: NotRequired[Sequence[StringFilterTypeDef]]
    resourceType: NotRequired[AggregationResourceTypeType]
    sortOrder: NotRequired[SortOrderType]
    sortBy: NotRequired[TitleSortByType]
    findingType: NotRequired[AggregationFindingTypeType]

class AssociateConfigurationRequestTypeDef(TypedDict):
    scanConfigurationArn: str
    resource: CodeSecurityResourceTypeDef

class CodeSecurityScanConfigurationAssociationSummaryTypeDef(TypedDict):
    resource: NotRequired[CodeSecurityResourceTypeDef]

class DisassociateConfigurationRequestTypeDef(TypedDict):
    scanConfigurationArn: str
    resource: CodeSecurityResourceTypeDef

class FailedAssociationResultTypeDef(TypedDict):
    scanConfigurationArn: NotRequired[str]
    resource: NotRequired[CodeSecurityResourceTypeDef]
    statusCode: NotRequired[AssociationResultStatusCodeType]
    statusMessage: NotRequired[str]

class GetCodeSecurityScanRequestTypeDef(TypedDict):
    resource: CodeSecurityResourceTypeDef
    scanId: str

class StartCodeSecurityScanRequestTypeDef(TypedDict):
    resource: CodeSecurityResourceTypeDef
    clientToken: NotRequired[str]

class SuccessfulAssociationResultTypeDef(TypedDict):
    scanConfigurationArn: NotRequired[str]
    resource: NotRequired[CodeSecurityResourceTypeDef]

class AssociateMemberResponseTypeDef(TypedDict):
    accountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelFindingsReportResponseTypeDef(TypedDict):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelSbomExportResponseTypeDef(TypedDict):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCisScanConfigurationResponseTypeDef(TypedDict):
    scanConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCodeSecurityIntegrationResponseTypeDef(TypedDict):
    integrationArn: str
    status: IntegrationStatusType
    authorizationUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCodeSecurityScanConfigurationResponseTypeDef(TypedDict):
    scanConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFilterResponseTypeDef(TypedDict):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFindingsReportResponseTypeDef(TypedDict):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSbomExportResponseTypeDef(TypedDict):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCisScanConfigurationResponseTypeDef(TypedDict):
    scanConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCodeSecurityIntegrationResponseTypeDef(TypedDict):
    integrationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCodeSecurityScanConfigurationResponseTypeDef(TypedDict):
    scanConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFilterResponseTypeDef(TypedDict):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableDelegatedAdminAccountResponseTypeDef(TypedDict):
    delegatedAdminAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateMemberResponseTypeDef(TypedDict):
    accountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnableDelegatedAdminAccountResponseTypeDef(TypedDict):
    delegatedAdminAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCisScanReportResponseTypeDef(TypedDict):
    url: str
    status: CisReportStatusType
    ResponseMetadata: ResponseMetadataTypeDef

GetCodeSecurityIntegrationResponseTypeDef = TypedDict(
    "GetCodeSecurityIntegrationResponseTypeDef",
    {
        "integrationArn": str,
        "name": str,
        "type": IntegrationTypeType,
        "status": IntegrationStatusType,
        "statusReason": str,
        "createdOn": datetime,
        "lastUpdateOn": datetime,
        "tags": Dict[str, str],
        "authorizationUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetCodeSecurityScanResponseTypeDef(TypedDict):
    scanId: str
    resource: CodeSecurityResourceTypeDef
    accountId: str
    status: CodeScanStatusType
    statusReason: str
    createdAt: datetime
    updatedAt: datetime
    lastCommitId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEc2DeepInspectionConfigurationResponseTypeDef(TypedDict):
    packagePaths: List[str]
    orgPackagePaths: List[str]
    status: Ec2DeepInspectionStatusType
    errorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEncryptionKeyResponseTypeDef(TypedDict):
    kmsKeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartCodeSecurityScanResponseTypeDef(TypedDict):
    scanId: str
    status: CodeScanStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCisScanConfigurationResponseTypeDef(TypedDict):
    scanConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCodeSecurityIntegrationResponseTypeDef(TypedDict):
    integrationArn: str
    status: IntegrationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCodeSecurityScanConfigurationResponseTypeDef(TypedDict):
    scanConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEc2DeepInspectionConfigurationResponseTypeDef(TypedDict):
    packagePaths: List[str]
    orgPackagePaths: List[str]
    status: Ec2DeepInspectionStatusType
    errorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFilterResponseTypeDef(TypedDict):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOrganizationConfigurationResponseTypeDef(TypedDict):
    autoEnable: AutoEnableTypeDef
    maxAccountLimitReached: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateOrganizationConfigurationRequestTypeDef(TypedDict):
    autoEnable: AutoEnableTypeDef

class UpdateOrganizationConfigurationResponseTypeDef(TypedDict):
    autoEnable: AutoEnableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PackageFilterTypeDef(TypedDict):
    name: NotRequired[StringFilterTypeDef]
    version: NotRequired[StringFilterTypeDef]
    epoch: NotRequired[NumberFilterTypeDef]
    release: NotRequired[StringFilterTypeDef]
    architecture: NotRequired[StringFilterTypeDef]
    sourceLayerHash: NotRequired[StringFilterTypeDef]
    sourceLambdaLayerArn: NotRequired[StringFilterTypeDef]
    filePath: NotRequired[StringFilterTypeDef]

class AwsEksMetadataDetailsTypeDef(TypedDict):
    namespace: NotRequired[str]
    workloadInfoList: NotRequired[List[AwsEksWorkloadInfoTypeDef]]

class AwsLambdaFunctionDetailsTypeDef(TypedDict):
    functionName: str
    runtime: RuntimeType
    codeSha256: str
    version: str
    executionRoleArn: str
    layers: NotRequired[List[str]]
    vpcConfig: NotRequired[LambdaVpcConfigTypeDef]
    packageType: NotRequired[PackageTypeType]
    architectures: NotRequired[List[ArchitectureType]]
    lastModifiedAt: NotRequired[datetime]

class BatchGetMemberEc2DeepInspectionStatusResponseTypeDef(TypedDict):
    accountIds: List[MemberAccountEc2DeepInspectionStatusStateTypeDef]
    failedAccountIds: List[FailedMemberAccountEc2DeepInspectionStatusStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef(TypedDict):
    accountIds: List[MemberAccountEc2DeepInspectionStatusStateTypeDef]
    failedAccountIds: List[FailedMemberAccountEc2DeepInspectionStatusStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateMemberEc2DeepInspectionStatusRequestTypeDef(TypedDict):
    accountIds: Sequence[MemberAccountEc2DeepInspectionStatusTypeDef]

class CisSessionMessageTypeDef(TypedDict):
    ruleId: str
    status: CisRuleStatusType
    cisRuleDetails: BlobTypeDef

class CisCheckAggregationTypeDef(TypedDict):
    scanArn: str
    checkId: NotRequired[str]
    title: NotRequired[str]
    checkDescription: NotRequired[str]
    level: NotRequired[CisSecurityLevelType]
    accountId: NotRequired[str]
    statusCounts: NotRequired[StatusCountsTypeDef]
    platform: NotRequired[str]

class CisTargetResourceAggregationTypeDef(TypedDict):
    scanArn: str
    targetResourceId: NotRequired[str]
    accountId: NotRequired[str]
    targetResourceTags: NotRequired[Dict[str, List[str]]]
    statusCounts: NotRequired[StatusCountsTypeDef]
    platform: NotRequired[str]
    targetStatus: NotRequired[CisTargetStatusType]
    targetStatusReason: NotRequired[CisTargetStatusReasonType]

class CisDateFilterTypeDef(TypedDict):
    earliestScanStartTime: NotRequired[TimestampTypeDef]
    latestScanStartTime: NotRequired[TimestampTypeDef]

class CoverageDateFilterTypeDef(TypedDict):
    startInclusive: NotRequired[TimestampTypeDef]
    endInclusive: NotRequired[TimestampTypeDef]

class DateFilterTypeDef(TypedDict):
    startInclusive: NotRequired[TimestampTypeDef]
    endInclusive: NotRequired[TimestampTypeDef]

class CisScanTypeDef(TypedDict):
    scanArn: str
    scanConfigurationArn: str
    status: NotRequired[CisScanStatusType]
    scanName: NotRequired[str]
    scanDate: NotRequired[datetime]
    failedChecks: NotRequired[int]
    totalChecks: NotRequired[int]
    targets: NotRequired[CisTargetsTypeDef]
    scheduledBy: NotRequired[str]
    securityLevel: NotRequired[CisSecurityLevelType]

class CisScanResultDetailsFilterCriteriaTypeDef(TypedDict):
    findingStatusFilters: NotRequired[Sequence[CisFindingStatusFilterTypeDef]]
    checkIdFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    titleFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    securityLevelFilters: NotRequired[Sequence[CisSecurityLevelFilterTypeDef]]
    findingArnFilters: NotRequired[Sequence[CisStringFilterTypeDef]]

class CisScanResultsAggregatedByChecksFilterCriteriaTypeDef(TypedDict):
    accountIdFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    checkIdFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    titleFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    platformFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    failedResourcesFilters: NotRequired[Sequence[CisNumberFilterTypeDef]]
    securityLevelFilters: NotRequired[Sequence[CisSecurityLevelFilterTypeDef]]

class GetCisScanResultDetailsResponseTypeDef(TypedDict):
    scanResultDetails: List[CisScanResultDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef(TypedDict):
    accountIdFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    statusFilters: NotRequired[Sequence[CisResultStatusFilterTypeDef]]
    checkIdFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    targetResourceIdFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    targetResourceTagFilters: NotRequired[Sequence[TagFilterTypeDef]]
    platformFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    targetStatusFilters: NotRequired[Sequence[CisTargetStatusFilterTypeDef]]
    targetStatusReasonFilters: NotRequired[Sequence[CisTargetStatusReasonFilterTypeDef]]
    failedChecksFilters: NotRequired[Sequence[CisNumberFilterTypeDef]]

class ListCisScanConfigurationsFilterCriteriaTypeDef(TypedDict):
    scanNameFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    targetResourceTagFilters: NotRequired[Sequence[TagFilterTypeDef]]
    scanConfigurationArnFilters: NotRequired[Sequence[CisStringFilterTypeDef]]

GetClustersForImageRequestTypeDef = TypedDict(
    "GetClustersForImageRequestTypeDef",
    {
        "filter": ClusterForImageFilterCriteriaTypeDef,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

class CodeVulnerabilityDetailsTypeDef(TypedDict):
    filePath: CodeFilePathTypeDef
    detectorId: str
    detectorName: str
    cwes: List[str]
    detectorTags: NotRequired[List[str]]
    referenceUrls: NotRequired[List[str]]
    ruleId: NotRequired[str]
    sourceLambdaLayerArn: NotRequired[str]

class CodeRepositoryOnDemandScanTypeDef(TypedDict):
    lastScannedCommitId: NotRequired[str]
    lastScanAt: NotRequired[datetime]
    scanStatus: NotRequired[ScanStatusTypeDef]

class ListCodeSecurityIntegrationsResponseTypeDef(TypedDict):
    integrations: List[CodeSecurityIntegrationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CodeSecurityScanConfigurationOutputTypeDef(TypedDict):
    ruleSetCategories: List[RuleSetCategoryType]
    periodicScanConfiguration: NotRequired[PeriodicScanConfigurationTypeDef]
    continuousIntegrationScanConfiguration: NotRequired[
        ContinuousIntegrationScanConfigurationOutputTypeDef
    ]

class CodeSecurityScanConfigurationSummaryTypeDef(TypedDict):
    scanConfigurationArn: str
    name: str
    ownerAccountId: str
    ruleSetCategories: List[RuleSetCategoryType]
    periodicScanFrequency: NotRequired[PeriodicScanFrequencyType]
    frequencyExpression: NotRequired[str]
    continuousIntegrationScanSupportedEvents: NotRequired[List[ContinuousIntegrationScanEventType]]
    scopeSettings: NotRequired[ScopeSettingsTypeDef]
    tags: NotRequired[Dict[str, str]]

class CodeSecurityScanConfigurationTypeDef(TypedDict):
    ruleSetCategories: Sequence[RuleSetCategoryType]
    periodicScanConfiguration: NotRequired[PeriodicScanConfigurationTypeDef]
    continuousIntegrationScanConfiguration: NotRequired[
        ContinuousIntegrationScanConfigurationTypeDef
    ]

class CodeSnippetResultTypeDef(TypedDict):
    findingArn: NotRequired[str]
    startLine: NotRequired[int]
    endLine: NotRequired[int]
    codeSnippet: NotRequired[List[CodeLineTypeDef]]
    suggestedFixes: NotRequired[List[SuggestedFixTypeDef]]

class ListCoverageStatisticsResponseTypeDef(TypedDict):
    countsByGroup: List[CountsTypeDef]
    totalCounts: int
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateIntegrationDetailTypeDef(TypedDict):
    gitlabSelfManaged: NotRequired[CreateGitLabSelfManagedIntegrationDetailTypeDef]

class CvssScoreDetailsTypeDef(TypedDict):
    scoreSource: str
    version: str
    score: float
    scoringVector: str
    cvssSource: NotRequired[str]
    adjustments: NotRequired[List[CvssScoreAdjustmentTypeDef]]

class DailyScheduleTypeDef(TypedDict):
    startTime: TimeTypeDef

class MonthlyScheduleTypeDef(TypedDict):
    startTime: TimeTypeDef
    day: DayType

class WeeklyScheduleOutputTypeDef(TypedDict):
    startTime: TimeTypeDef
    days: List[DayType]

class WeeklyScheduleTypeDef(TypedDict):
    startTime: TimeTypeDef
    days: Sequence[DayType]

class ListDelegatedAdminAccountsResponseTypeDef(TypedDict):
    delegatedAdminAccounts: List[DelegatedAdminAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetDelegatedAdminAccountResponseTypeDef(TypedDict):
    delegatedAdmin: DelegatedAdminTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class Ec2ConfigurationStateTypeDef(TypedDict):
    scanModeState: NotRequired[Ec2ScanModeStateTypeDef]

class Ec2InstanceAggregationTypeDef(TypedDict):
    amis: NotRequired[Sequence[StringFilterTypeDef]]
    operatingSystems: NotRequired[Sequence[StringFilterTypeDef]]
    instanceIds: NotRequired[Sequence[StringFilterTypeDef]]
    instanceTags: NotRequired[Sequence[MapFilterTypeDef]]
    sortOrder: NotRequired[SortOrderType]
    sortBy: NotRequired[Ec2InstanceSortByType]

class LambdaFunctionAggregationTypeDef(TypedDict):
    resourceIds: NotRequired[Sequence[StringFilterTypeDef]]
    functionNames: NotRequired[Sequence[StringFilterTypeDef]]
    runtimes: NotRequired[Sequence[StringFilterTypeDef]]
    functionTags: NotRequired[Sequence[MapFilterTypeDef]]
    sortOrder: NotRequired[SortOrderType]
    sortBy: NotRequired[LambdaFunctionSortByType]

class EcrConfigurationStateTypeDef(TypedDict):
    rescanDurationState: NotRequired[EcrRescanDurationStateTypeDef]

class UpdateConfigurationRequestTypeDef(TypedDict):
    ecrConfiguration: NotRequired[EcrConfigurationTypeDef]
    ec2Configuration: NotRequired[Ec2ConfigurationTypeDef]

class FindingDetailTypeDef(TypedDict):
    findingArn: NotRequired[str]
    cisaData: NotRequired[CisaDataTypeDef]
    riskScore: NotRequired[int]
    evidences: NotRequired[List[EvidenceTypeDef]]
    ttps: NotRequired[List[str]]
    tools: NotRequired[List[str]]
    exploitObserved: NotRequired[ExploitObservedTypeDef]
    referenceUrls: NotRequired[List[str]]
    cwes: NotRequired[List[str]]
    epssScore: NotRequired[float]

VulnerabilityTypeDef = TypedDict(
    "VulnerabilityTypeDef",
    {
        "id": str,
        "cwes": NotRequired[List[str]],
        "cisaData": NotRequired[CisaDataTypeDef],
        "source": NotRequired[Literal["NVD"]],
        "description": NotRequired[str],
        "atigData": NotRequired[AtigDataTypeDef],
        "vendorSeverity": NotRequired[str],
        "cvss4": NotRequired[Cvss4TypeDef],
        "cvss3": NotRequired[Cvss3TypeDef],
        "relatedVulnerabilities": NotRequired[List[str]],
        "cvss2": NotRequired[Cvss2TypeDef],
        "vendorCreatedAt": NotRequired[datetime],
        "vendorUpdatedAt": NotRequired[datetime],
        "sourceUrl": NotRequired[str],
        "referenceUrls": NotRequired[List[str]],
        "exploitObserved": NotRequired[ExploitObservedTypeDef],
        "detectionPlatforms": NotRequired[List[str]],
        "epss": NotRequired[EpssTypeDef],
    },
)

class FreeTrialAccountInfoTypeDef(TypedDict):
    accountId: str
    freeTrialInfo: List[FreeTrialInfoTypeDef]

GetClustersForImageRequestPaginateTypeDef = TypedDict(
    "GetClustersForImageRequestPaginateTypeDef",
    {
        "filter": ClusterForImageFilterCriteriaTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListAccountPermissionsRequestPaginateTypeDef(TypedDict):
    service: NotRequired[ServiceType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDelegatedAdminAccountsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFiltersRequestPaginateTypeDef(TypedDict):
    arns: NotRequired[Sequence[str]]
    action: NotRequired[FilterActionType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMembersRequestPaginateTypeDef(TypedDict):
    onlyAssociated: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUsageTotalsRequestPaginateTypeDef(TypedDict):
    accountIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetMemberResponseTypeDef(TypedDict):
    member: MemberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListMembersResponseTypeDef(TypedDict):
    members: List[MemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAccountPermissionsResponseTypeDef(TypedDict):
    permissions: List[PermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class NetworkPathTypeDef(TypedDict):
    steps: NotRequired[List[StepTypeDef]]

class PackageVulnerabilityDetailsTypeDef(TypedDict):
    vulnerabilityId: str
    source: str
    vulnerablePackages: NotRequired[List[VulnerablePackageTypeDef]]
    cvss: NotRequired[List[CvssScoreTypeDef]]
    relatedVulnerabilities: NotRequired[List[str]]
    sourceUrl: NotRequired[str]
    vendorSeverity: NotRequired[str]
    vendorCreatedAt: NotRequired[datetime]
    vendorUpdatedAt: NotRequired[datetime]
    referenceUrls: NotRequired[List[str]]

class ProjectCodeSecurityScanConfigurationTypeDef(TypedDict):
    periodicScanConfigurations: NotRequired[List[ProjectPeriodicScanConfigurationTypeDef]]
    continuousIntegrationScanConfigurations: NotRequired[
        List[ProjectContinuousIntegrationScanConfigurationTypeDef]
    ]

class RemediationTypeDef(TypedDict):
    recommendation: NotRequired[RecommendationTypeDef]

class ResourceFilterCriteriaOutputTypeDef(TypedDict):
    accountId: NotRequired[List[ResourceStringFilterTypeDef]]
    resourceId: NotRequired[List[ResourceStringFilterTypeDef]]
    resourceType: NotRequired[List[ResourceStringFilterTypeDef]]
    ecrRepositoryName: NotRequired[List[ResourceStringFilterTypeDef]]
    lambdaFunctionName: NotRequired[List[ResourceStringFilterTypeDef]]
    ecrImageTags: NotRequired[List[ResourceStringFilterTypeDef]]
    ec2InstanceTags: NotRequired[List[ResourceMapFilterTypeDef]]
    lambdaFunctionTags: NotRequired[List[ResourceMapFilterTypeDef]]

class ResourceFilterCriteriaTypeDef(TypedDict):
    accountId: NotRequired[Sequence[ResourceStringFilterTypeDef]]
    resourceId: NotRequired[Sequence[ResourceStringFilterTypeDef]]
    resourceType: NotRequired[Sequence[ResourceStringFilterTypeDef]]
    ecrRepositoryName: NotRequired[Sequence[ResourceStringFilterTypeDef]]
    lambdaFunctionName: NotRequired[Sequence[ResourceStringFilterTypeDef]]
    ecrImageTags: NotRequired[Sequence[ResourceStringFilterTypeDef]]
    ec2InstanceTags: NotRequired[Sequence[ResourceMapFilterTypeDef]]
    lambdaFunctionTags: NotRequired[Sequence[ResourceMapFilterTypeDef]]

class SearchVulnerabilitiesRequestPaginateTypeDef(TypedDict):
    filterCriteria: SearchVulnerabilitiesFilterCriteriaTypeDef
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchVulnerabilitiesRequestTypeDef(TypedDict):
    filterCriteria: SearchVulnerabilitiesFilterCriteriaTypeDef
    nextToken: NotRequired[str]

class StartCisSessionRequestTypeDef(TypedDict):
    scanJobId: str
    message: StartCisSessionMessageTypeDef

class StopCisSessionMessageTypeDef(TypedDict):
    status: StopCisSessionStatusType
    progress: StopCisMessageProgressTypeDef
    reason: NotRequired[str]
    computePlatform: NotRequired[ComputePlatformTypeDef]
    benchmarkVersion: NotRequired[str]
    benchmarkProfile: NotRequired[str]

class UpdateIntegrationDetailsTypeDef(TypedDict):
    gitlabSelfManaged: NotRequired[UpdateGitLabSelfManagedIntegrationDetailTypeDef]
    github: NotRequired[UpdateGitHubIntegrationDetailTypeDef]

class UsageTotalTypeDef(TypedDict):
    accountId: NotRequired[str]
    usage: NotRequired[List[UsageTypeDef]]

class AggregationResponseTypeDef(TypedDict):
    accountAggregation: NotRequired[AccountAggregationResponseTypeDef]
    amiAggregation: NotRequired[AmiAggregationResponseTypeDef]
    awsEcrContainerAggregation: NotRequired[AwsEcrContainerAggregationResponseTypeDef]
    ec2InstanceAggregation: NotRequired[Ec2InstanceAggregationResponseTypeDef]
    findingTypeAggregation: NotRequired[FindingTypeAggregationResponseTypeDef]
    imageLayerAggregation: NotRequired[ImageLayerAggregationResponseTypeDef]
    packageAggregation: NotRequired[PackageAggregationResponseTypeDef]
    repositoryAggregation: NotRequired[RepositoryAggregationResponseTypeDef]
    titleAggregation: NotRequired[TitleAggregationResponseTypeDef]
    lambdaLayerAggregation: NotRequired[LambdaLayerAggregationResponseTypeDef]
    lambdaFunctionAggregation: NotRequired[LambdaFunctionAggregationResponseTypeDef]
    codeRepositoryAggregation: NotRequired[CodeRepositoryAggregationResponseTypeDef]

class AccountStateTypeDef(TypedDict):
    accountId: str
    state: StateTypeDef
    resourceState: ResourceStateTypeDef

class DisableResponseTypeDef(TypedDict):
    accounts: List[AccountTypeDef]
    failedAccounts: List[FailedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EnableResponseTypeDef(TypedDict):
    accounts: List[AccountTypeDef]
    failedAccounts: List[FailedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchAssociateCodeSecurityScanConfigurationRequestTypeDef(TypedDict):
    associateConfigurationRequests: Sequence[AssociateConfigurationRequestTypeDef]

class ListCodeSecurityScanConfigurationAssociationsResponseTypeDef(TypedDict):
    associations: List[CodeSecurityScanConfigurationAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class BatchDisassociateCodeSecurityScanConfigurationRequestTypeDef(TypedDict):
    disassociateConfigurationRequests: Sequence[DisassociateConfigurationRequestTypeDef]

class BatchAssociateCodeSecurityScanConfigurationResponseTypeDef(TypedDict):
    failedAssociations: List[FailedAssociationResultTypeDef]
    successfulAssociations: List[SuccessfulAssociationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateCodeSecurityScanConfigurationResponseTypeDef(TypedDict):
    failedAssociations: List[FailedAssociationResultTypeDef]
    successfulAssociations: List[SuccessfulAssociationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FilterCriteriaOutputTypeDef(TypedDict):
    findingArn: NotRequired[List[StringFilterTypeDef]]
    awsAccountId: NotRequired[List[StringFilterTypeDef]]
    findingType: NotRequired[List[StringFilterTypeDef]]
    severity: NotRequired[List[StringFilterTypeDef]]
    firstObservedAt: NotRequired[List[DateFilterOutputTypeDef]]
    lastObservedAt: NotRequired[List[DateFilterOutputTypeDef]]
    updatedAt: NotRequired[List[DateFilterOutputTypeDef]]
    findingStatus: NotRequired[List[StringFilterTypeDef]]
    title: NotRequired[List[StringFilterTypeDef]]
    inspectorScore: NotRequired[List[NumberFilterTypeDef]]
    resourceType: NotRequired[List[StringFilterTypeDef]]
    resourceId: NotRequired[List[StringFilterTypeDef]]
    resourceTags: NotRequired[List[MapFilterTypeDef]]
    ec2InstanceImageId: NotRequired[List[StringFilterTypeDef]]
    ec2InstanceVpcId: NotRequired[List[StringFilterTypeDef]]
    ec2InstanceSubnetId: NotRequired[List[StringFilterTypeDef]]
    ecrImagePushedAt: NotRequired[List[DateFilterOutputTypeDef]]
    ecrImageArchitecture: NotRequired[List[StringFilterTypeDef]]
    ecrImageRegistry: NotRequired[List[StringFilterTypeDef]]
    ecrImageRepositoryName: NotRequired[List[StringFilterTypeDef]]
    ecrImageTags: NotRequired[List[StringFilterTypeDef]]
    ecrImageHash: NotRequired[List[StringFilterTypeDef]]
    ecrImageLastInUseAt: NotRequired[List[DateFilterOutputTypeDef]]
    ecrImageInUseCount: NotRequired[List[NumberFilterTypeDef]]
    portRange: NotRequired[List[PortRangeFilterTypeDef]]
    networkProtocol: NotRequired[List[StringFilterTypeDef]]
    componentId: NotRequired[List[StringFilterTypeDef]]
    componentType: NotRequired[List[StringFilterTypeDef]]
    vulnerabilityId: NotRequired[List[StringFilterTypeDef]]
    vulnerabilitySource: NotRequired[List[StringFilterTypeDef]]
    vendorSeverity: NotRequired[List[StringFilterTypeDef]]
    vulnerablePackages: NotRequired[List[PackageFilterTypeDef]]
    relatedVulnerabilities: NotRequired[List[StringFilterTypeDef]]
    fixAvailable: NotRequired[List[StringFilterTypeDef]]
    lambdaFunctionName: NotRequired[List[StringFilterTypeDef]]
    lambdaFunctionLayers: NotRequired[List[StringFilterTypeDef]]
    lambdaFunctionRuntime: NotRequired[List[StringFilterTypeDef]]
    lambdaFunctionLastModifiedAt: NotRequired[List[DateFilterOutputTypeDef]]
    lambdaFunctionExecutionRoleArn: NotRequired[List[StringFilterTypeDef]]
    exploitAvailable: NotRequired[List[StringFilterTypeDef]]
    codeVulnerabilityDetectorName: NotRequired[List[StringFilterTypeDef]]
    codeVulnerabilityDetectorTags: NotRequired[List[StringFilterTypeDef]]
    codeVulnerabilityFilePath: NotRequired[List[StringFilterTypeDef]]
    epssScore: NotRequired[List[NumberFilterTypeDef]]
    codeRepositoryProjectName: NotRequired[List[StringFilterTypeDef]]
    codeRepositoryProviderType: NotRequired[List[StringFilterTypeDef]]

class ClusterMetadataTypeDef(TypedDict):
    awsEcsMetadataDetails: NotRequired[AwsEcsMetadataDetailsTypeDef]
    awsEksMetadataDetails: NotRequired[AwsEksMetadataDetailsTypeDef]

class ResourceDetailsTypeDef(TypedDict):
    awsEc2Instance: NotRequired[AwsEc2InstanceDetailsTypeDef]
    awsEcrContainerImage: NotRequired[AwsEcrContainerImageDetailsTypeDef]
    awsLambdaFunction: NotRequired[AwsLambdaFunctionDetailsTypeDef]
    codeRepository: NotRequired[CodeRepositoryDetailsTypeDef]

class SendCisSessionTelemetryRequestTypeDef(TypedDict):
    scanJobId: str
    sessionToken: str
    messages: Sequence[CisSessionMessageTypeDef]

class ListCisScanResultsAggregatedByChecksResponseTypeDef(TypedDict):
    checkAggregations: List[CisCheckAggregationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListCisScanResultsAggregatedByTargetResourceResponseTypeDef(TypedDict):
    targetResourceAggregations: List[CisTargetResourceAggregationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListCisScansFilterCriteriaTypeDef(TypedDict):
    scanNameFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    targetResourceTagFilters: NotRequired[Sequence[TagFilterTypeDef]]
    targetResourceIdFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    scanStatusFilters: NotRequired[Sequence[CisScanStatusFilterTypeDef]]
    scanAtFilters: NotRequired[Sequence[CisDateFilterTypeDef]]
    scanConfigurationArnFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    scanArnFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    scheduledByFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    failedChecksFilters: NotRequired[Sequence[CisNumberFilterTypeDef]]
    targetAccountIdFilters: NotRequired[Sequence[CisStringFilterTypeDef]]

class CoverageFilterCriteriaTypeDef(TypedDict):
    scanStatusCode: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    scanStatusReason: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    accountId: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    resourceId: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    resourceType: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    scanType: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    ecrRepositoryName: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    ecrImageTags: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    ec2InstanceTags: NotRequired[Sequence[CoverageMapFilterTypeDef]]
    lambdaFunctionName: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    lambdaFunctionTags: NotRequired[Sequence[CoverageMapFilterTypeDef]]
    lambdaFunctionRuntime: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    lastScannedAt: NotRequired[Sequence[CoverageDateFilterTypeDef]]
    scanMode: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    imagePulledAt: NotRequired[Sequence[CoverageDateFilterTypeDef]]
    ecrImageLastInUseAt: NotRequired[Sequence[CoverageDateFilterTypeDef]]
    ecrImageInUseCount: NotRequired[Sequence[CoverageNumberFilterTypeDef]]
    codeRepositoryProjectName: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    codeRepositoryProviderType: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    codeRepositoryProviderTypeVisibility: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    lastScannedCommitId: NotRequired[Sequence[CoverageStringFilterTypeDef]]

DateFilterUnionTypeDef = Union[DateFilterTypeDef, DateFilterOutputTypeDef]

class FilterCriteriaTypeDef(TypedDict):
    findingArn: NotRequired[Sequence[StringFilterTypeDef]]
    awsAccountId: NotRequired[Sequence[StringFilterTypeDef]]
    findingType: NotRequired[Sequence[StringFilterTypeDef]]
    severity: NotRequired[Sequence[StringFilterTypeDef]]
    firstObservedAt: NotRequired[Sequence[DateFilterTypeDef]]
    lastObservedAt: NotRequired[Sequence[DateFilterTypeDef]]
    updatedAt: NotRequired[Sequence[DateFilterTypeDef]]
    findingStatus: NotRequired[Sequence[StringFilterTypeDef]]
    title: NotRequired[Sequence[StringFilterTypeDef]]
    inspectorScore: NotRequired[Sequence[NumberFilterTypeDef]]
    resourceType: NotRequired[Sequence[StringFilterTypeDef]]
    resourceId: NotRequired[Sequence[StringFilterTypeDef]]
    resourceTags: NotRequired[Sequence[MapFilterTypeDef]]
    ec2InstanceImageId: NotRequired[Sequence[StringFilterTypeDef]]
    ec2InstanceVpcId: NotRequired[Sequence[StringFilterTypeDef]]
    ec2InstanceSubnetId: NotRequired[Sequence[StringFilterTypeDef]]
    ecrImagePushedAt: NotRequired[Sequence[DateFilterTypeDef]]
    ecrImageArchitecture: NotRequired[Sequence[StringFilterTypeDef]]
    ecrImageRegistry: NotRequired[Sequence[StringFilterTypeDef]]
    ecrImageRepositoryName: NotRequired[Sequence[StringFilterTypeDef]]
    ecrImageTags: NotRequired[Sequence[StringFilterTypeDef]]
    ecrImageHash: NotRequired[Sequence[StringFilterTypeDef]]
    ecrImageLastInUseAt: NotRequired[Sequence[DateFilterTypeDef]]
    ecrImageInUseCount: NotRequired[Sequence[NumberFilterTypeDef]]
    portRange: NotRequired[Sequence[PortRangeFilterTypeDef]]
    networkProtocol: NotRequired[Sequence[StringFilterTypeDef]]
    componentId: NotRequired[Sequence[StringFilterTypeDef]]
    componentType: NotRequired[Sequence[StringFilterTypeDef]]
    vulnerabilityId: NotRequired[Sequence[StringFilterTypeDef]]
    vulnerabilitySource: NotRequired[Sequence[StringFilterTypeDef]]
    vendorSeverity: NotRequired[Sequence[StringFilterTypeDef]]
    vulnerablePackages: NotRequired[Sequence[PackageFilterTypeDef]]
    relatedVulnerabilities: NotRequired[Sequence[StringFilterTypeDef]]
    fixAvailable: NotRequired[Sequence[StringFilterTypeDef]]
    lambdaFunctionName: NotRequired[Sequence[StringFilterTypeDef]]
    lambdaFunctionLayers: NotRequired[Sequence[StringFilterTypeDef]]
    lambdaFunctionRuntime: NotRequired[Sequence[StringFilterTypeDef]]
    lambdaFunctionLastModifiedAt: NotRequired[Sequence[DateFilterTypeDef]]
    lambdaFunctionExecutionRoleArn: NotRequired[Sequence[StringFilterTypeDef]]
    exploitAvailable: NotRequired[Sequence[StringFilterTypeDef]]
    codeVulnerabilityDetectorName: NotRequired[Sequence[StringFilterTypeDef]]
    codeVulnerabilityDetectorTags: NotRequired[Sequence[StringFilterTypeDef]]
    codeVulnerabilityFilePath: NotRequired[Sequence[StringFilterTypeDef]]
    epssScore: NotRequired[Sequence[NumberFilterTypeDef]]
    codeRepositoryProjectName: NotRequired[Sequence[StringFilterTypeDef]]
    codeRepositoryProviderType: NotRequired[Sequence[StringFilterTypeDef]]

class ListCisScansResponseTypeDef(TypedDict):
    scans: List[CisScanTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetCisScanResultDetailsRequestPaginateTypeDef(TypedDict):
    scanArn: str
    targetResourceId: str
    accountId: str
    filterCriteria: NotRequired[CisScanResultDetailsFilterCriteriaTypeDef]
    sortBy: NotRequired[CisScanResultDetailsSortByType]
    sortOrder: NotRequired[CisSortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetCisScanResultDetailsRequestTypeDef(TypedDict):
    scanArn: str
    targetResourceId: str
    accountId: str
    filterCriteria: NotRequired[CisScanResultDetailsFilterCriteriaTypeDef]
    sortBy: NotRequired[CisScanResultDetailsSortByType]
    sortOrder: NotRequired[CisSortOrderType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListCisScanResultsAggregatedByChecksRequestPaginateTypeDef(TypedDict):
    scanArn: str
    filterCriteria: NotRequired[CisScanResultsAggregatedByChecksFilterCriteriaTypeDef]
    sortBy: NotRequired[CisScanResultsAggregatedByChecksSortByType]
    sortOrder: NotRequired[CisSortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCisScanResultsAggregatedByChecksRequestTypeDef(TypedDict):
    scanArn: str
    filterCriteria: NotRequired[CisScanResultsAggregatedByChecksFilterCriteriaTypeDef]
    sortBy: NotRequired[CisScanResultsAggregatedByChecksSortByType]
    sortOrder: NotRequired[CisSortOrderType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListCisScanResultsAggregatedByTargetResourceRequestPaginateTypeDef(TypedDict):
    scanArn: str
    filterCriteria: NotRequired[CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef]
    sortBy: NotRequired[CisScanResultsAggregatedByTargetResourceSortByType]
    sortOrder: NotRequired[CisSortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCisScanResultsAggregatedByTargetResourceRequestTypeDef(TypedDict):
    scanArn: str
    filterCriteria: NotRequired[CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef]
    sortBy: NotRequired[CisScanResultsAggregatedByTargetResourceSortByType]
    sortOrder: NotRequired[CisSortOrderType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListCisScanConfigurationsRequestPaginateTypeDef(TypedDict):
    filterCriteria: NotRequired[ListCisScanConfigurationsFilterCriteriaTypeDef]
    sortBy: NotRequired[CisScanConfigurationsSortByType]
    sortOrder: NotRequired[CisSortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCisScanConfigurationsRequestTypeDef(TypedDict):
    filterCriteria: NotRequired[ListCisScanConfigurationsFilterCriteriaTypeDef]
    sortBy: NotRequired[CisScanConfigurationsSortByType]
    sortOrder: NotRequired[CisSortOrderType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class GetCodeSecurityScanConfigurationResponseTypeDef(TypedDict):
    scanConfigurationArn: str
    name: str
    configuration: CodeSecurityScanConfigurationOutputTypeDef
    level: ConfigurationLevelType
    scopeSettings: ScopeSettingsTypeDef
    createdAt: datetime
    lastUpdatedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCodeSecurityScanConfigurationsResponseTypeDef(TypedDict):
    configurations: List[CodeSecurityScanConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

CodeSecurityScanConfigurationUnionTypeDef = Union[
    CodeSecurityScanConfigurationTypeDef, CodeSecurityScanConfigurationOutputTypeDef
]

class BatchGetCodeSnippetResponseTypeDef(TypedDict):
    codeSnippetResults: List[CodeSnippetResultTypeDef]
    errors: List[CodeSnippetErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

CreateCodeSecurityIntegrationRequestTypeDef = TypedDict(
    "CreateCodeSecurityIntegrationRequestTypeDef",
    {
        "name": str,
        "type": IntegrationTypeType,
        "details": NotRequired[CreateIntegrationDetailTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)

class InspectorScoreDetailsTypeDef(TypedDict):
    adjustedCvss: NotRequired[CvssScoreDetailsTypeDef]

class ScheduleOutputTypeDef(TypedDict):
    oneTime: NotRequired[Dict[str, Any]]
    daily: NotRequired[DailyScheduleTypeDef]
    weekly: NotRequired[WeeklyScheduleOutputTypeDef]
    monthly: NotRequired[MonthlyScheduleTypeDef]

class ScheduleTypeDef(TypedDict):
    oneTime: NotRequired[Mapping[str, Any]]
    daily: NotRequired[DailyScheduleTypeDef]
    weekly: NotRequired[WeeklyScheduleTypeDef]
    monthly: NotRequired[MonthlyScheduleTypeDef]

class GetConfigurationResponseTypeDef(TypedDict):
    ecrConfiguration: EcrConfigurationStateTypeDef
    ec2Configuration: Ec2ConfigurationStateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetFindingDetailsResponseTypeDef(TypedDict):
    findingDetails: List[FindingDetailTypeDef]
    errors: List[FindingDetailsErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchVulnerabilitiesResponseTypeDef(TypedDict):
    vulnerabilities: List[VulnerabilityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class BatchGetFreeTrialInfoResponseTypeDef(TypedDict):
    accounts: List[FreeTrialAccountInfoTypeDef]
    failedAccounts: List[FreeTrialInfoErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkReachabilityDetailsTypeDef(TypedDict):
    openPortRange: PortRangeTypeDef
    protocol: NetworkProtocolType
    networkPath: NetworkPathTypeDef

class CodeRepositoryMetadataTypeDef(TypedDict):
    projectName: str
    providerType: str
    providerTypeVisibility: str
    integrationArn: NotRequired[str]
    lastScannedCommitId: NotRequired[str]
    scanConfiguration: NotRequired[ProjectCodeSecurityScanConfigurationTypeDef]
    onDemandScan: NotRequired[CodeRepositoryOnDemandScanTypeDef]

GetSbomExportResponseTypeDef = TypedDict(
    "GetSbomExportResponseTypeDef",
    {
        "reportId": str,
        "format": SbomReportFormatType,
        "status": ExternalReportStatusType,
        "errorCode": ReportingErrorCodeType,
        "errorMessage": str,
        "s3Destination": DestinationTypeDef,
        "filterCriteria": ResourceFilterCriteriaOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResourceFilterCriteriaUnionTypeDef = Union[
    ResourceFilterCriteriaTypeDef, ResourceFilterCriteriaOutputTypeDef
]

class StopCisSessionRequestTypeDef(TypedDict):
    scanJobId: str
    sessionToken: str
    message: StopCisSessionMessageTypeDef

class UpdateCodeSecurityIntegrationRequestTypeDef(TypedDict):
    integrationArn: str
    details: UpdateIntegrationDetailsTypeDef

class ListUsageTotalsResponseTypeDef(TypedDict):
    totals: List[UsageTotalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListFindingAggregationsResponseTypeDef(TypedDict):
    aggregationType: AggregationTypeType
    responses: List[AggregationResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class BatchGetAccountStatusResponseTypeDef(TypedDict):
    accounts: List[AccountStateTypeDef]
    failedAccounts: List[FailedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FilterTypeDef(TypedDict):
    arn: str
    ownerId: str
    name: str
    criteria: FilterCriteriaOutputTypeDef
    action: FilterActionType
    createdAt: datetime
    updatedAt: datetime
    description: NotRequired[str]
    reason: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class GetFindingsReportStatusResponseTypeDef(TypedDict):
    reportId: str
    status: ExternalReportStatusType
    errorCode: ReportingErrorCodeType
    errorMessage: str
    destination: DestinationTypeDef
    filterCriteria: FilterCriteriaOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterDetailsTypeDef(TypedDict):
    lastInUse: datetime
    clusterMetadata: ClusterMetadataTypeDef
    runningUnitCount: NotRequired[int]
    stoppedUnitCount: NotRequired[int]

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "type": ResourceTypeType,
        "id": str,
        "partition": NotRequired[str],
        "region": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "details": NotRequired[ResourceDetailsTypeDef],
    },
)

class ListCisScansRequestPaginateTypeDef(TypedDict):
    filterCriteria: NotRequired[ListCisScansFilterCriteriaTypeDef]
    detailLevel: NotRequired[ListCisScansDetailLevelType]
    sortBy: NotRequired[ListCisScansSortByType]
    sortOrder: NotRequired[CisSortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCisScansRequestTypeDef(TypedDict):
    filterCriteria: NotRequired[ListCisScansFilterCriteriaTypeDef]
    detailLevel: NotRequired[ListCisScansDetailLevelType]
    sortBy: NotRequired[ListCisScansSortByType]
    sortOrder: NotRequired[CisSortOrderType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListCoverageRequestPaginateTypeDef(TypedDict):
    filterCriteria: NotRequired[CoverageFilterCriteriaTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCoverageRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    filterCriteria: NotRequired[CoverageFilterCriteriaTypeDef]

class ListCoverageStatisticsRequestPaginateTypeDef(TypedDict):
    filterCriteria: NotRequired[CoverageFilterCriteriaTypeDef]
    groupBy: NotRequired[GroupKeyType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCoverageStatisticsRequestTypeDef(TypedDict):
    filterCriteria: NotRequired[CoverageFilterCriteriaTypeDef]
    groupBy: NotRequired[GroupKeyType]
    nextToken: NotRequired[str]

class AwsEcrContainerAggregationTypeDef(TypedDict):
    resourceIds: NotRequired[Sequence[StringFilterTypeDef]]
    imageShas: NotRequired[Sequence[StringFilterTypeDef]]
    repositories: NotRequired[Sequence[StringFilterTypeDef]]
    architectures: NotRequired[Sequence[StringFilterTypeDef]]
    imageTags: NotRequired[Sequence[StringFilterTypeDef]]
    sortOrder: NotRequired[SortOrderType]
    sortBy: NotRequired[AwsEcrContainerSortByType]
    lastInUseAt: NotRequired[Sequence[DateFilterUnionTypeDef]]
    inUseCount: NotRequired[Sequence[NumberFilterTypeDef]]

FilterCriteriaUnionTypeDef = Union[FilterCriteriaTypeDef, FilterCriteriaOutputTypeDef]

class CreateCodeSecurityScanConfigurationRequestTypeDef(TypedDict):
    name: str
    level: ConfigurationLevelType
    configuration: CodeSecurityScanConfigurationUnionTypeDef
    scopeSettings: NotRequired[ScopeSettingsTypeDef]
    tags: NotRequired[Mapping[str, str]]

class UpdateCodeSecurityScanConfigurationRequestTypeDef(TypedDict):
    scanConfigurationArn: str
    configuration: CodeSecurityScanConfigurationUnionTypeDef

class CisScanConfigurationTypeDef(TypedDict):
    scanConfigurationArn: str
    ownerId: NotRequired[str]
    scanName: NotRequired[str]
    securityLevel: NotRequired[CisSecurityLevelType]
    schedule: NotRequired[ScheduleOutputTypeDef]
    targets: NotRequired[CisTargetsTypeDef]
    tags: NotRequired[Dict[str, str]]

ScheduleUnionTypeDef = Union[ScheduleTypeDef, ScheduleOutputTypeDef]

class ResourceScanMetadataTypeDef(TypedDict):
    ecrRepository: NotRequired[EcrRepositoryMetadataTypeDef]
    ecrImage: NotRequired[EcrContainerImageMetadataTypeDef]
    ec2: NotRequired[Ec2MetadataTypeDef]
    lambdaFunction: NotRequired[LambdaFunctionMetadataTypeDef]
    codeRepository: NotRequired[CodeRepositoryMetadataTypeDef]

class CreateSbomExportRequestTypeDef(TypedDict):
    reportFormat: SbomReportFormatType
    s3Destination: DestinationTypeDef
    resourceFilterCriteria: NotRequired[ResourceFilterCriteriaUnionTypeDef]

class ListFiltersResponseTypeDef(TypedDict):
    filters: List[FilterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ClusterInformationTypeDef(TypedDict):
    clusterArn: str
    clusterDetails: NotRequired[List[ClusterDetailsTypeDef]]

FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "findingArn": str,
        "awsAccountId": str,
        "type": FindingTypeType,
        "description": str,
        "remediation": RemediationTypeDef,
        "severity": SeverityType,
        "firstObservedAt": datetime,
        "lastObservedAt": datetime,
        "status": FindingStatusType,
        "resources": List[ResourceTypeDef],
        "title": NotRequired[str],
        "updatedAt": NotRequired[datetime],
        "inspectorScore": NotRequired[float],
        "inspectorScoreDetails": NotRequired[InspectorScoreDetailsTypeDef],
        "networkReachabilityDetails": NotRequired[NetworkReachabilityDetailsTypeDef],
        "packageVulnerabilityDetails": NotRequired[PackageVulnerabilityDetailsTypeDef],
        "fixAvailable": NotRequired[FixAvailableType],
        "exploitAvailable": NotRequired[ExploitAvailableType],
        "exploitabilityDetails": NotRequired[ExploitabilityDetailsTypeDef],
        "codeVulnerabilityDetails": NotRequired[CodeVulnerabilityDetailsTypeDef],
        "epss": NotRequired[EpssDetailsTypeDef],
    },
)

class AggregationRequestTypeDef(TypedDict):
    accountAggregation: NotRequired[AccountAggregationTypeDef]
    amiAggregation: NotRequired[AmiAggregationTypeDef]
    awsEcrContainerAggregation: NotRequired[AwsEcrContainerAggregationTypeDef]
    ec2InstanceAggregation: NotRequired[Ec2InstanceAggregationTypeDef]
    findingTypeAggregation: NotRequired[FindingTypeAggregationTypeDef]
    imageLayerAggregation: NotRequired[ImageLayerAggregationTypeDef]
    packageAggregation: NotRequired[PackageAggregationTypeDef]
    repositoryAggregation: NotRequired[RepositoryAggregationTypeDef]
    titleAggregation: NotRequired[TitleAggregationTypeDef]
    lambdaLayerAggregation: NotRequired[LambdaLayerAggregationTypeDef]
    lambdaFunctionAggregation: NotRequired[LambdaFunctionAggregationTypeDef]
    codeRepositoryAggregation: NotRequired[CodeRepositoryAggregationTypeDef]

class CreateFilterRequestTypeDef(TypedDict):
    action: FilterActionType
    filterCriteria: FilterCriteriaUnionTypeDef
    name: str
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    reason: NotRequired[str]

class CreateFindingsReportRequestTypeDef(TypedDict):
    reportFormat: ReportFormatType
    s3Destination: DestinationTypeDef
    filterCriteria: NotRequired[FilterCriteriaUnionTypeDef]

class ListFindingsRequestPaginateTypeDef(TypedDict):
    filterCriteria: NotRequired[FilterCriteriaUnionTypeDef]
    sortCriteria: NotRequired[SortCriteriaTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFindingsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    filterCriteria: NotRequired[FilterCriteriaUnionTypeDef]
    sortCriteria: NotRequired[SortCriteriaTypeDef]

class UpdateFilterRequestTypeDef(TypedDict):
    filterArn: str
    action: NotRequired[FilterActionType]
    description: NotRequired[str]
    filterCriteria: NotRequired[FilterCriteriaUnionTypeDef]
    name: NotRequired[str]
    reason: NotRequired[str]

class ListCisScanConfigurationsResponseTypeDef(TypedDict):
    scanConfigurations: List[CisScanConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateCisScanConfigurationRequestTypeDef(TypedDict):
    scanName: str
    securityLevel: CisSecurityLevelType
    schedule: ScheduleUnionTypeDef
    targets: CreateCisTargetsTypeDef
    tags: NotRequired[Mapping[str, str]]

class UpdateCisScanConfigurationRequestTypeDef(TypedDict):
    scanConfigurationArn: str
    scanName: NotRequired[str]
    securityLevel: NotRequired[CisSecurityLevelType]
    schedule: NotRequired[ScheduleUnionTypeDef]
    targets: NotRequired[UpdateCisTargetsTypeDef]

class CoveredResourceTypeDef(TypedDict):
    resourceType: CoverageResourceTypeType
    resourceId: str
    accountId: str
    scanType: ScanTypeType
    scanStatus: NotRequired[ScanStatusTypeDef]
    resourceMetadata: NotRequired[ResourceScanMetadataTypeDef]
    lastScannedAt: NotRequired[datetime]
    scanMode: NotRequired[ScanModeType]

class GetClustersForImageResponseTypeDef(TypedDict):
    cluster: List[ClusterInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListFindingsResponseTypeDef(TypedDict):
    findings: List[FindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListFindingAggregationsRequestPaginateTypeDef(TypedDict):
    aggregationType: AggregationTypeType
    accountIds: NotRequired[Sequence[StringFilterTypeDef]]
    aggregationRequest: NotRequired[AggregationRequestTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFindingAggregationsRequestTypeDef(TypedDict):
    aggregationType: AggregationTypeType
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    accountIds: NotRequired[Sequence[StringFilterTypeDef]]
    aggregationRequest: NotRequired[AggregationRequestTypeDef]

class ListCoverageResponseTypeDef(TypedDict):
    coveredResources: List[CoveredResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
