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
    CodeSnippetErrorCodeType,
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
    LambdaFunctionSortByType,
    LambdaLayerSortByType,
    ListCisScansDetailLevelType,
    ListCisScansSortByType,
    NetworkProtocolType,
    OperationType,
    PackageManagerType,
    PackageSortByType,
    PackageTypeType,
    RelationshipStatusType,
    ReportFormatType,
    ReportingErrorCodeType,
    RepositorySortByType,
    ResourceScanTypeType,
    ResourceStringComparisonType,
    ResourceTypeType,
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
    "AssociateMemberRequestTypeDef",
    "AssociateMemberResponseTypeDef",
    "AtigDataTypeDef",
    "AutoEnableTypeDef",
    "AwsEc2InstanceDetailsTypeDef",
    "AwsEcrContainerAggregationResponseTypeDef",
    "AwsEcrContainerAggregationTypeDef",
    "AwsEcrContainerImageDetailsTypeDef",
    "AwsLambdaFunctionDetailsTypeDef",
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
    "CodeFilePathTypeDef",
    "CodeLineTypeDef",
    "CodeSnippetErrorTypeDef",
    "CodeSnippetResultTypeDef",
    "CodeVulnerabilityDetailsTypeDef",
    "ComputePlatformTypeDef",
    "CountsTypeDef",
    "CoverageDateFilterTypeDef",
    "CoverageFilterCriteriaTypeDef",
    "CoverageMapFilterTypeDef",
    "CoverageStringFilterTypeDef",
    "CoveredResourceTypeDef",
    "CreateCisScanConfigurationRequestTypeDef",
    "CreateCisScanConfigurationResponseTypeDef",
    "CreateCisTargetsTypeDef",
    "CreateFilterRequestTypeDef",
    "CreateFilterResponseTypeDef",
    "CreateFindingsReportRequestTypeDef",
    "CreateFindingsReportResponseTypeDef",
    "CreateSbomExportRequestTypeDef",
    "CreateSbomExportResponseTypeDef",
    "Cvss2TypeDef",
    "Cvss3TypeDef",
    "CvssScoreAdjustmentTypeDef",
    "CvssScoreDetailsTypeDef",
    "CvssScoreTypeDef",
    "DailyScheduleTypeDef",
    "DateFilterOutputTypeDef",
    "DateFilterTypeDef",
    "DelegatedAdminAccountTypeDef",
    "DelegatedAdminTypeDef",
    "DeleteCisScanConfigurationRequestTypeDef",
    "DeleteCisScanConfigurationResponseTypeDef",
    "DeleteFilterRequestTypeDef",
    "DeleteFilterResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DestinationTypeDef",
    "DisableDelegatedAdminAccountRequestTypeDef",
    "DisableDelegatedAdminAccountResponseTypeDef",
    "DisableRequestTypeDef",
    "DisableResponseTypeDef",
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
    "PermissionTypeDef",
    "PortRangeFilterTypeDef",
    "PortRangeTypeDef",
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
    "StateTypeDef",
    "StatusCountsTypeDef",
    "StepTypeDef",
    "StopCisMessageProgressTypeDef",
    "StopCisSessionMessageTypeDef",
    "StopCisSessionRequestTypeDef",
    "StringFilterTypeDef",
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
    "UpdateConfigurationRequestTypeDef",
    "UpdateEc2DeepInspectionConfigurationRequestTypeDef",
    "UpdateEc2DeepInspectionConfigurationResponseTypeDef",
    "UpdateEncryptionKeyRequestTypeDef",
    "UpdateFilterRequestTypeDef",
    "UpdateFilterResponseTypeDef",
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
        "critical": NotRequired[int],
        "high": NotRequired[int],
        "medium": NotRequired[int],
    },
)

class AccountAggregationTypeDef(TypedDict):
    findingType: NotRequired[AggregationFindingTypeType]
    resourceType: NotRequired[AggregationResourceTypeType]
    sortBy: NotRequired[AccountSortByType]
    sortOrder: NotRequired[SortOrderType]

class StateTypeDef(TypedDict):
    errorCode: ErrorCodeType
    errorMessage: str
    status: StatusType

ResourceStatusTypeDef = TypedDict(
    "ResourceStatusTypeDef",
    {
        "ec2": StatusType,
        "ecr": StatusType,
        "lambda": NotRequired[StatusType],
        "lambdaCode": NotRequired[StatusType],
    },
)

class FindingTypeAggregationTypeDef(TypedDict):
    findingType: NotRequired[AggregationFindingTypeType]
    resourceType: NotRequired[AggregationResourceTypeType]
    sortBy: NotRequired[FindingTypeSortByType]
    sortOrder: NotRequired[SortOrderType]

class StringFilterTypeDef(TypedDict):
    comparison: StringComparisonType
    value: str

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
    },
)
AwsEc2InstanceDetailsTypeDef = TypedDict(
    "AwsEc2InstanceDetailsTypeDef",
    {
        "iamInstanceProfileArn": NotRequired[str],
        "imageId": NotRequired[str],
        "ipV4Addresses": NotRequired[List[str]],
        "ipV6Addresses": NotRequired[List[str]],
        "keyName": NotRequired[str],
        "launchedAt": NotRequired[datetime],
        "platform": NotRequired[str],
        "subnetId": NotRequired[str],
        "type": NotRequired[str],
        "vpcId": NotRequired[str],
    },
)

class AwsEcrContainerImageDetailsTypeDef(TypedDict):
    imageHash: str
    registry: str
    repositoryName: str
    architecture: NotRequired[str]
    author: NotRequired[str]
    imageTags: NotRequired[List[str]]
    platform: NotRequired[str]
    pushedAt: NotRequired[datetime]

class LambdaVpcConfigTypeDef(TypedDict):
    securityGroupIds: NotRequired[List[str]]
    subnetIds: NotRequired[List[str]]
    vpcId: NotRequired[str]

class BatchGetAccountStatusRequestTypeDef(TypedDict):
    accountIds: NotRequired[Sequence[str]]

class BatchGetCodeSnippetRequestTypeDef(TypedDict):
    findingArns: Sequence[str]

class CodeSnippetErrorTypeDef(TypedDict):
    errorCode: CodeSnippetErrorCodeType
    errorMessage: str
    findingArn: str

class BatchGetFindingDetailsRequestTypeDef(TypedDict):
    findingArns: Sequence[str]

class FindingDetailsErrorTypeDef(TypedDict):
    errorCode: FindingDetailsErrorCodeType
    errorMessage: str
    findingArn: str

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
    errorMessage: NotRequired[str]
    status: NotRequired[Ec2DeepInspectionStatusType]

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
    passed: NotRequired[int]
    skipped: NotRequired[int]

TimestampTypeDef = Union[datetime, str]

class CisFindingStatusFilterTypeDef(TypedDict):
    comparison: Literal["EQUALS"]
    value: CisFindingStatusType

class CisNumberFilterTypeDef(TypedDict):
    lowerInclusive: NotRequired[int]
    upperInclusive: NotRequired[int]

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
    checkDescription: NotRequired[str]
    checkId: NotRequired[str]
    findingArn: NotRequired[str]
    level: NotRequired[CisSecurityLevelType]
    platform: NotRequired[str]
    remediation: NotRequired[str]
    status: NotRequired[CisFindingStatusType]
    statusReason: NotRequired[str]
    targetResourceId: NotRequired[str]
    title: NotRequired[str]

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
    action: NotRequired[str]
    dateAdded: NotRequired[datetime]
    dateDue: NotRequired[datetime]

class CodeFilePathTypeDef(TypedDict):
    endLine: int
    fileName: str
    filePath: str
    startLine: int

class CodeLineTypeDef(TypedDict):
    content: str
    lineNumber: int

class SuggestedFixTypeDef(TypedDict):
    code: NotRequired[str]
    description: NotRequired[str]

class ComputePlatformTypeDef(TypedDict):
    product: NotRequired[str]
    vendor: NotRequired[str]
    version: NotRequired[str]

class CountsTypeDef(TypedDict):
    count: NotRequired[int]
    groupKey: NotRequired[GroupKeyType]

class CoverageMapFilterTypeDef(TypedDict):
    comparison: Literal["EQUALS"]
    key: str
    value: NotRequired[str]

class CoverageStringFilterTypeDef(TypedDict):
    comparison: CoverageStringComparisonType
    value: str

class ScanStatusTypeDef(TypedDict):
    reason: ScanStatusReasonType
    statusCode: ScanStatusCodeType

class CreateCisTargetsTypeDef(TypedDict):
    accountIds: Sequence[str]
    targetResourceTags: Mapping[str, Sequence[str]]

class DestinationTypeDef(TypedDict):
    bucketName: str
    kmsKeyArn: str
    keyPrefix: NotRequired[str]

class Cvss2TypeDef(TypedDict):
    baseScore: NotRequired[float]
    scoringVector: NotRequired[str]

class Cvss3TypeDef(TypedDict):
    baseScore: NotRequired[float]
    scoringVector: NotRequired[str]

class CvssScoreAdjustmentTypeDef(TypedDict):
    metric: str
    reason: str

class CvssScoreTypeDef(TypedDict):
    baseScore: float
    scoringVector: str
    source: str
    version: str

class TimeTypeDef(TypedDict):
    timeOfDay: str
    timezone: str

class DateFilterOutputTypeDef(TypedDict):
    endInclusive: NotRequired[datetime]
    startInclusive: NotRequired[datetime]

class DelegatedAdminAccountTypeDef(TypedDict):
    accountId: NotRequired[str]
    status: NotRequired[DelegatedAdminStatusType]

class DelegatedAdminTypeDef(TypedDict):
    accountId: NotRequired[str]
    relationshipStatus: NotRequired[RelationshipStatusType]

class DeleteCisScanConfigurationRequestTypeDef(TypedDict):
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
    amiId: NotRequired[str]
    platform: NotRequired[Ec2PlatformType]
    tags: NotRequired[Dict[str, str]]

class EcrRescanDurationStateTypeDef(TypedDict):
    pullDateRescanDuration: NotRequired[EcrPullDateRescanDurationType]
    rescanDuration: NotRequired[EcrRescanDurationType]
    status: NotRequired[EcrRescanDurationStatusType]
    updatedAt: NotRequired[datetime]

class EcrConfigurationTypeDef(TypedDict):
    rescanDuration: EcrRescanDurationType
    pullDateRescanDuration: NotRequired[EcrPullDateRescanDurationType]

class EcrContainerImageMetadataTypeDef(TypedDict):
    imagePulledAt: NotRequired[datetime]
    tags: NotRequired[List[str]]

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
    evidenceDetail: NotRequired[str]
    evidenceRule: NotRequired[str]
    severity: NotRequired[str]

class ExploitObservedTypeDef(TypedDict):
    firstSeen: NotRequired[datetime]
    lastSeen: NotRequired[datetime]

class ExploitabilityDetailsTypeDef(TypedDict):
    lastKnownExploitAt: NotRequired[datetime]

class NumberFilterTypeDef(TypedDict):
    lowerInclusive: NotRequired[float]
    upperInclusive: NotRequired[float]

class PortRangeFilterTypeDef(TypedDict):
    beginInclusive: NotRequired[int]
    endInclusive: NotRequired[int]

FreeTrialInfoTypeDef = TypedDict(
    "FreeTrialInfoTypeDef",
    {
        "end": datetime,
        "start": datetime,
        "status": FreeTrialStatusType,
        "type": FreeTrialTypeType,
    },
)

class GetCisScanReportRequestTypeDef(TypedDict):
    scanArn: str
    reportFormat: NotRequired[CisReportFormatType]
    targetAccounts: NotRequired[Sequence[str]]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetEncryptionKeyRequestTypeDef(TypedDict):
    resourceType: ResourceTypeType
    scanType: ScanTypeType

class GetFindingsReportStatusRequestTypeDef(TypedDict):
    reportId: NotRequired[str]

class GetMemberRequestTypeDef(TypedDict):
    accountId: str

class MemberTypeDef(TypedDict):
    accountId: NotRequired[str]
    delegatedAdminAccountId: NotRequired[str]
    relationshipStatus: NotRequired[RelationshipStatusType]
    updatedAt: NotRequired[datetime]

class GetSbomExportRequestTypeDef(TypedDict):
    reportId: str

class LambdaFunctionMetadataTypeDef(TypedDict):
    functionName: NotRequired[str]
    functionTags: NotRequired[Dict[str, str]]
    layers: NotRequired[List[str]]
    runtime: NotRequired[RuntimeType]

class ListAccountPermissionsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    service: NotRequired[ServiceType]

class PermissionTypeDef(TypedDict):
    operation: OperationType
    service: ServiceType

class ListDelegatedAdminAccountsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListFiltersRequestTypeDef(TypedDict):
    action: NotRequired[FilterActionType]
    arns: NotRequired[Sequence[str]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class SortCriteriaTypeDef(TypedDict):
    field: SortFieldType
    sortOrder: SortOrderType

class ListMembersRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    onlyAssociated: NotRequired[bool]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListUsageTotalsRequestTypeDef(TypedDict):
    accountIds: NotRequired[Sequence[str]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

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
    arch: NotRequired[str]
    epoch: NotRequired[int]
    filePath: NotRequired[str]
    fixedInVersion: NotRequired[str]
    packageManager: NotRequired[PackageManagerType]
    release: NotRequired[str]
    remediation: NotRequired[str]
    sourceLambdaLayerArn: NotRequired[str]
    sourceLayerHash: NotRequired[str]

class RecommendationTypeDef(TypedDict):
    Url: NotRequired[str]
    text: NotRequired[str]

class ResetEncryptionKeyRequestTypeDef(TypedDict):
    resourceType: ResourceTypeType
    scanType: ScanTypeType

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
    errorChecks: NotRequired[int]
    failedChecks: NotRequired[int]
    informationalChecks: NotRequired[int]
    notApplicableChecks: NotRequired[int]
    notEvaluatedChecks: NotRequired[int]
    successfulChecks: NotRequired[int]
    totalChecks: NotRequired[int]
    unknownChecks: NotRequired[int]

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
    resourceType: ResourceTypeType
    scanType: ScanTypeType

class UpdateOrgEc2DeepInspectionConfigurationRequestTypeDef(TypedDict):
    orgPackagePaths: Sequence[str]

UsageTypeDef = TypedDict(
    "UsageTypeDef",
    {
        "currency": NotRequired[Literal["USD"]],
        "estimatedMonthlyCost": NotRequired[float],
        "total": NotRequired[float],
        "type": NotRequired[UsageTypeType],
    },
)

class AccountAggregationResponseTypeDef(TypedDict):
    accountId: NotRequired[str]
    exploitAvailableCount: NotRequired[int]
    fixAvailableCount: NotRequired[int]
    severityCounts: NotRequired[SeverityCountsTypeDef]

class AmiAggregationResponseTypeDef(TypedDict):
    ami: str
    accountId: NotRequired[str]
    affectedInstances: NotRequired[int]
    severityCounts: NotRequired[SeverityCountsTypeDef]

class AwsEcrContainerAggregationResponseTypeDef(TypedDict):
    resourceId: str
    accountId: NotRequired[str]
    architecture: NotRequired[str]
    imageSha: NotRequired[str]
    imageTags: NotRequired[List[str]]
    repository: NotRequired[str]
    severityCounts: NotRequired[SeverityCountsTypeDef]

class Ec2InstanceAggregationResponseTypeDef(TypedDict):
    instanceId: str
    accountId: NotRequired[str]
    ami: NotRequired[str]
    instanceTags: NotRequired[Dict[str, str]]
    networkFindings: NotRequired[int]
    operatingSystem: NotRequired[str]
    severityCounts: NotRequired[SeverityCountsTypeDef]

class FindingTypeAggregationResponseTypeDef(TypedDict):
    accountId: NotRequired[str]
    exploitAvailableCount: NotRequired[int]
    fixAvailableCount: NotRequired[int]
    severityCounts: NotRequired[SeverityCountsTypeDef]

class ImageLayerAggregationResponseTypeDef(TypedDict):
    accountId: str
    layerHash: str
    repository: str
    resourceId: str
    severityCounts: NotRequired[SeverityCountsTypeDef]

class LambdaFunctionAggregationResponseTypeDef(TypedDict):
    resourceId: str
    accountId: NotRequired[str]
    functionName: NotRequired[str]
    lambdaTags: NotRequired[Dict[str, str]]
    lastModifiedAt: NotRequired[datetime]
    runtime: NotRequired[str]
    severityCounts: NotRequired[SeverityCountsTypeDef]

class LambdaLayerAggregationResponseTypeDef(TypedDict):
    accountId: str
    functionName: str
    layerArn: str
    resourceId: str
    severityCounts: NotRequired[SeverityCountsTypeDef]

class PackageAggregationResponseTypeDef(TypedDict):
    packageName: str
    accountId: NotRequired[str]
    severityCounts: NotRequired[SeverityCountsTypeDef]

class RepositoryAggregationResponseTypeDef(TypedDict):
    repository: str
    accountId: NotRequired[str]
    affectedImages: NotRequired[int]
    severityCounts: NotRequired[SeverityCountsTypeDef]

class TitleAggregationResponseTypeDef(TypedDict):
    title: str
    accountId: NotRequired[str]
    severityCounts: NotRequired[SeverityCountsTypeDef]
    vulnerabilityId: NotRequired[str]

ResourceStateTypeDef = TypedDict(
    "ResourceStateTypeDef",
    {
        "ec2": StateTypeDef,
        "ecr": StateTypeDef,
        "lambda": NotRequired[StateTypeDef],
        "lambdaCode": NotRequired[StateTypeDef],
    },
)

class AccountTypeDef(TypedDict):
    accountId: str
    resourceStatus: ResourceStatusTypeDef
    status: StatusType

class FailedAccountTypeDef(TypedDict):
    accountId: str
    errorCode: ErrorCodeType
    errorMessage: str
    resourceStatus: NotRequired[ResourceStatusTypeDef]
    status: NotRequired[StatusType]

class AmiAggregationTypeDef(TypedDict):
    amis: NotRequired[Sequence[StringFilterTypeDef]]
    sortBy: NotRequired[AmiSortByType]
    sortOrder: NotRequired[SortOrderType]

class AwsEcrContainerAggregationTypeDef(TypedDict):
    architectures: NotRequired[Sequence[StringFilterTypeDef]]
    imageShas: NotRequired[Sequence[StringFilterTypeDef]]
    imageTags: NotRequired[Sequence[StringFilterTypeDef]]
    repositories: NotRequired[Sequence[StringFilterTypeDef]]
    resourceIds: NotRequired[Sequence[StringFilterTypeDef]]
    sortBy: NotRequired[AwsEcrContainerSortByType]
    sortOrder: NotRequired[SortOrderType]

class ImageLayerAggregationTypeDef(TypedDict):
    layerHashes: NotRequired[Sequence[StringFilterTypeDef]]
    repositories: NotRequired[Sequence[StringFilterTypeDef]]
    resourceIds: NotRequired[Sequence[StringFilterTypeDef]]
    sortBy: NotRequired[ImageLayerSortByType]
    sortOrder: NotRequired[SortOrderType]

class LambdaLayerAggregationTypeDef(TypedDict):
    functionNames: NotRequired[Sequence[StringFilterTypeDef]]
    layerArns: NotRequired[Sequence[StringFilterTypeDef]]
    resourceIds: NotRequired[Sequence[StringFilterTypeDef]]
    sortBy: NotRequired[LambdaLayerSortByType]
    sortOrder: NotRequired[SortOrderType]

class PackageAggregationTypeDef(TypedDict):
    packageNames: NotRequired[Sequence[StringFilterTypeDef]]
    sortBy: NotRequired[PackageSortByType]
    sortOrder: NotRequired[SortOrderType]

class RepositoryAggregationTypeDef(TypedDict):
    repositories: NotRequired[Sequence[StringFilterTypeDef]]
    sortBy: NotRequired[RepositorySortByType]
    sortOrder: NotRequired[SortOrderType]

class TitleAggregationTypeDef(TypedDict):
    findingType: NotRequired[AggregationFindingTypeType]
    resourceType: NotRequired[AggregationResourceTypeType]
    sortBy: NotRequired[TitleSortByType]
    sortOrder: NotRequired[SortOrderType]
    titles: NotRequired[Sequence[StringFilterTypeDef]]
    vulnerabilityIds: NotRequired[Sequence[StringFilterTypeDef]]

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
    status: CisReportStatusType
    url: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEc2DeepInspectionConfigurationResponseTypeDef(TypedDict):
    errorMessage: str
    orgPackagePaths: List[str]
    packagePaths: List[str]
    status: Ec2DeepInspectionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetEncryptionKeyResponseTypeDef(TypedDict):
    kmsKeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCisScanConfigurationResponseTypeDef(TypedDict):
    scanConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEc2DeepInspectionConfigurationResponseTypeDef(TypedDict):
    errorMessage: str
    orgPackagePaths: List[str]
    packagePaths: List[str]
    status: Ec2DeepInspectionStatusType
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

class AwsLambdaFunctionDetailsTypeDef(TypedDict):
    codeSha256: str
    executionRoleArn: str
    functionName: str
    runtime: RuntimeType
    version: str
    architectures: NotRequired[List[ArchitectureType]]
    lastModifiedAt: NotRequired[datetime]
    layers: NotRequired[List[str]]
    packageType: NotRequired[PackageTypeType]
    vpcConfig: NotRequired[LambdaVpcConfigTypeDef]

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
    cisRuleDetails: BlobTypeDef
    ruleId: str
    status: CisRuleStatusType

class CisCheckAggregationTypeDef(TypedDict):
    scanArn: str
    accountId: NotRequired[str]
    checkDescription: NotRequired[str]
    checkId: NotRequired[str]
    level: NotRequired[CisSecurityLevelType]
    platform: NotRequired[str]
    statusCounts: NotRequired[StatusCountsTypeDef]
    title: NotRequired[str]

class CisTargetResourceAggregationTypeDef(TypedDict):
    scanArn: str
    accountId: NotRequired[str]
    platform: NotRequired[str]
    statusCounts: NotRequired[StatusCountsTypeDef]
    targetResourceId: NotRequired[str]
    targetResourceTags: NotRequired[Dict[str, List[str]]]
    targetStatus: NotRequired[CisTargetStatusType]
    targetStatusReason: NotRequired[CisTargetStatusReasonType]

class CisDateFilterTypeDef(TypedDict):
    earliestScanStartTime: NotRequired[TimestampTypeDef]
    latestScanStartTime: NotRequired[TimestampTypeDef]

class CoverageDateFilterTypeDef(TypedDict):
    endInclusive: NotRequired[TimestampTypeDef]
    startInclusive: NotRequired[TimestampTypeDef]

class DateFilterTypeDef(TypedDict):
    endInclusive: NotRequired[TimestampTypeDef]
    startInclusive: NotRequired[TimestampTypeDef]

class CisScanTypeDef(TypedDict):
    scanArn: str
    scanConfigurationArn: str
    failedChecks: NotRequired[int]
    scanDate: NotRequired[datetime]
    scanName: NotRequired[str]
    scheduledBy: NotRequired[str]
    securityLevel: NotRequired[CisSecurityLevelType]
    status: NotRequired[CisScanStatusType]
    targets: NotRequired[CisTargetsTypeDef]
    totalChecks: NotRequired[int]

class CisScanResultDetailsFilterCriteriaTypeDef(TypedDict):
    checkIdFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    findingArnFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    findingStatusFilters: NotRequired[Sequence[CisFindingStatusFilterTypeDef]]
    securityLevelFilters: NotRequired[Sequence[CisSecurityLevelFilterTypeDef]]
    titleFilters: NotRequired[Sequence[CisStringFilterTypeDef]]

class CisScanResultsAggregatedByChecksFilterCriteriaTypeDef(TypedDict):
    accountIdFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    checkIdFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    failedResourcesFilters: NotRequired[Sequence[CisNumberFilterTypeDef]]
    platformFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    securityLevelFilters: NotRequired[Sequence[CisSecurityLevelFilterTypeDef]]
    titleFilters: NotRequired[Sequence[CisStringFilterTypeDef]]

class GetCisScanResultDetailsResponseTypeDef(TypedDict):
    scanResultDetails: List[CisScanResultDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef(TypedDict):
    accountIdFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    checkIdFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    failedChecksFilters: NotRequired[Sequence[CisNumberFilterTypeDef]]
    platformFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    statusFilters: NotRequired[Sequence[CisResultStatusFilterTypeDef]]
    targetResourceIdFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    targetResourceTagFilters: NotRequired[Sequence[TagFilterTypeDef]]
    targetStatusFilters: NotRequired[Sequence[CisTargetStatusFilterTypeDef]]
    targetStatusReasonFilters: NotRequired[Sequence[CisTargetStatusReasonFilterTypeDef]]

class ListCisScanConfigurationsFilterCriteriaTypeDef(TypedDict):
    scanConfigurationArnFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    scanNameFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    targetResourceTagFilters: NotRequired[Sequence[TagFilterTypeDef]]

class CodeVulnerabilityDetailsTypeDef(TypedDict):
    cwes: List[str]
    detectorId: str
    detectorName: str
    filePath: CodeFilePathTypeDef
    detectorTags: NotRequired[List[str]]
    referenceUrls: NotRequired[List[str]]
    ruleId: NotRequired[str]
    sourceLambdaLayerArn: NotRequired[str]

class CodeSnippetResultTypeDef(TypedDict):
    codeSnippet: NotRequired[List[CodeLineTypeDef]]
    endLine: NotRequired[int]
    findingArn: NotRequired[str]
    startLine: NotRequired[int]
    suggestedFixes: NotRequired[List[SuggestedFixTypeDef]]

class ListCoverageStatisticsResponseTypeDef(TypedDict):
    countsByGroup: List[CountsTypeDef]
    totalCounts: int
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CvssScoreDetailsTypeDef(TypedDict):
    score: float
    scoreSource: str
    scoringVector: str
    version: str
    adjustments: NotRequired[List[CvssScoreAdjustmentTypeDef]]
    cvssSource: NotRequired[str]

class DailyScheduleTypeDef(TypedDict):
    startTime: TimeTypeDef

class MonthlyScheduleTypeDef(TypedDict):
    day: DayType
    startTime: TimeTypeDef

class WeeklyScheduleOutputTypeDef(TypedDict):
    days: List[DayType]
    startTime: TimeTypeDef

class WeeklyScheduleTypeDef(TypedDict):
    days: Sequence[DayType]
    startTime: TimeTypeDef

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
    instanceIds: NotRequired[Sequence[StringFilterTypeDef]]
    instanceTags: NotRequired[Sequence[MapFilterTypeDef]]
    operatingSystems: NotRequired[Sequence[StringFilterTypeDef]]
    sortBy: NotRequired[Ec2InstanceSortByType]
    sortOrder: NotRequired[SortOrderType]

class LambdaFunctionAggregationTypeDef(TypedDict):
    functionNames: NotRequired[Sequence[StringFilterTypeDef]]
    functionTags: NotRequired[Sequence[MapFilterTypeDef]]
    resourceIds: NotRequired[Sequence[StringFilterTypeDef]]
    runtimes: NotRequired[Sequence[StringFilterTypeDef]]
    sortBy: NotRequired[LambdaFunctionSortByType]
    sortOrder: NotRequired[SortOrderType]

class EcrConfigurationStateTypeDef(TypedDict):
    rescanDurationState: NotRequired[EcrRescanDurationStateTypeDef]

class UpdateConfigurationRequestTypeDef(TypedDict):
    ec2Configuration: NotRequired[Ec2ConfigurationTypeDef]
    ecrConfiguration: NotRequired[EcrConfigurationTypeDef]

class FindingDetailTypeDef(TypedDict):
    cisaData: NotRequired[CisaDataTypeDef]
    cwes: NotRequired[List[str]]
    epssScore: NotRequired[float]
    evidences: NotRequired[List[EvidenceTypeDef]]
    exploitObserved: NotRequired[ExploitObservedTypeDef]
    findingArn: NotRequired[str]
    referenceUrls: NotRequired[List[str]]
    riskScore: NotRequired[int]
    tools: NotRequired[List[str]]
    ttps: NotRequired[List[str]]

VulnerabilityTypeDef = TypedDict(
    "VulnerabilityTypeDef",
    {
        "id": str,
        "atigData": NotRequired[AtigDataTypeDef],
        "cisaData": NotRequired[CisaDataTypeDef],
        "cvss2": NotRequired[Cvss2TypeDef],
        "cvss3": NotRequired[Cvss3TypeDef],
        "cwes": NotRequired[List[str]],
        "description": NotRequired[str],
        "detectionPlatforms": NotRequired[List[str]],
        "epss": NotRequired[EpssTypeDef],
        "exploitObserved": NotRequired[ExploitObservedTypeDef],
        "referenceUrls": NotRequired[List[str]],
        "relatedVulnerabilities": NotRequired[List[str]],
        "source": NotRequired[Literal["NVD"]],
        "sourceUrl": NotRequired[str],
        "vendorCreatedAt": NotRequired[datetime],
        "vendorSeverity": NotRequired[str],
        "vendorUpdatedAt": NotRequired[datetime],
    },
)

class PackageFilterTypeDef(TypedDict):
    architecture: NotRequired[StringFilterTypeDef]
    epoch: NotRequired[NumberFilterTypeDef]
    filePath: NotRequired[StringFilterTypeDef]
    name: NotRequired[StringFilterTypeDef]
    release: NotRequired[StringFilterTypeDef]
    sourceLambdaLayerArn: NotRequired[StringFilterTypeDef]
    sourceLayerHash: NotRequired[StringFilterTypeDef]
    version: NotRequired[StringFilterTypeDef]

class FreeTrialAccountInfoTypeDef(TypedDict):
    accountId: str
    freeTrialInfo: List[FreeTrialInfoTypeDef]

class ListAccountPermissionsRequestPaginateTypeDef(TypedDict):
    service: NotRequired[ServiceType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDelegatedAdminAccountsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFiltersRequestPaginateTypeDef(TypedDict):
    action: NotRequired[FilterActionType]
    arns: NotRequired[Sequence[str]]
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

class ResourceScanMetadataTypeDef(TypedDict):
    ec2: NotRequired[Ec2MetadataTypeDef]
    ecrImage: NotRequired[EcrContainerImageMetadataTypeDef]
    ecrRepository: NotRequired[EcrRepositoryMetadataTypeDef]
    lambdaFunction: NotRequired[LambdaFunctionMetadataTypeDef]

class ListAccountPermissionsResponseTypeDef(TypedDict):
    permissions: List[PermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class NetworkPathTypeDef(TypedDict):
    steps: NotRequired[List[StepTypeDef]]

class PackageVulnerabilityDetailsTypeDef(TypedDict):
    source: str
    vulnerabilityId: str
    cvss: NotRequired[List[CvssScoreTypeDef]]
    referenceUrls: NotRequired[List[str]]
    relatedVulnerabilities: NotRequired[List[str]]
    sourceUrl: NotRequired[str]
    vendorCreatedAt: NotRequired[datetime]
    vendorSeverity: NotRequired[str]
    vendorUpdatedAt: NotRequired[datetime]
    vulnerablePackages: NotRequired[List[VulnerablePackageTypeDef]]

class RemediationTypeDef(TypedDict):
    recommendation: NotRequired[RecommendationTypeDef]

class ResourceFilterCriteriaOutputTypeDef(TypedDict):
    accountId: NotRequired[List[ResourceStringFilterTypeDef]]
    ec2InstanceTags: NotRequired[List[ResourceMapFilterTypeDef]]
    ecrImageTags: NotRequired[List[ResourceStringFilterTypeDef]]
    ecrRepositoryName: NotRequired[List[ResourceStringFilterTypeDef]]
    lambdaFunctionName: NotRequired[List[ResourceStringFilterTypeDef]]
    lambdaFunctionTags: NotRequired[List[ResourceMapFilterTypeDef]]
    resourceId: NotRequired[List[ResourceStringFilterTypeDef]]
    resourceType: NotRequired[List[ResourceStringFilterTypeDef]]

class ResourceFilterCriteriaTypeDef(TypedDict):
    accountId: NotRequired[Sequence[ResourceStringFilterTypeDef]]
    ec2InstanceTags: NotRequired[Sequence[ResourceMapFilterTypeDef]]
    ecrImageTags: NotRequired[Sequence[ResourceStringFilterTypeDef]]
    ecrRepositoryName: NotRequired[Sequence[ResourceStringFilterTypeDef]]
    lambdaFunctionName: NotRequired[Sequence[ResourceStringFilterTypeDef]]
    lambdaFunctionTags: NotRequired[Sequence[ResourceMapFilterTypeDef]]
    resourceId: NotRequired[Sequence[ResourceStringFilterTypeDef]]
    resourceType: NotRequired[Sequence[ResourceStringFilterTypeDef]]

class SearchVulnerabilitiesRequestPaginateTypeDef(TypedDict):
    filterCriteria: SearchVulnerabilitiesFilterCriteriaTypeDef
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchVulnerabilitiesRequestTypeDef(TypedDict):
    filterCriteria: SearchVulnerabilitiesFilterCriteriaTypeDef
    nextToken: NotRequired[str]

class StartCisSessionRequestTypeDef(TypedDict):
    message: StartCisSessionMessageTypeDef
    scanJobId: str

class StopCisSessionMessageTypeDef(TypedDict):
    progress: StopCisMessageProgressTypeDef
    status: StopCisSessionStatusType
    benchmarkProfile: NotRequired[str]
    benchmarkVersion: NotRequired[str]
    computePlatform: NotRequired[ComputePlatformTypeDef]
    reason: NotRequired[str]

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
    lambdaFunctionAggregation: NotRequired[LambdaFunctionAggregationResponseTypeDef]
    lambdaLayerAggregation: NotRequired[LambdaLayerAggregationResponseTypeDef]
    packageAggregation: NotRequired[PackageAggregationResponseTypeDef]
    repositoryAggregation: NotRequired[RepositoryAggregationResponseTypeDef]
    titleAggregation: NotRequired[TitleAggregationResponseTypeDef]

class AccountStateTypeDef(TypedDict):
    accountId: str
    resourceState: ResourceStateTypeDef
    state: StateTypeDef

class DisableResponseTypeDef(TypedDict):
    accounts: List[AccountTypeDef]
    failedAccounts: List[FailedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EnableResponseTypeDef(TypedDict):
    accounts: List[AccountTypeDef]
    failedAccounts: List[FailedAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceDetailsTypeDef(TypedDict):
    awsEc2Instance: NotRequired[AwsEc2InstanceDetailsTypeDef]
    awsEcrContainerImage: NotRequired[AwsEcrContainerImageDetailsTypeDef]
    awsLambdaFunction: NotRequired[AwsLambdaFunctionDetailsTypeDef]

class SendCisSessionTelemetryRequestTypeDef(TypedDict):
    messages: Sequence[CisSessionMessageTypeDef]
    scanJobId: str
    sessionToken: str

class ListCisScanResultsAggregatedByChecksResponseTypeDef(TypedDict):
    checkAggregations: List[CisCheckAggregationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListCisScanResultsAggregatedByTargetResourceResponseTypeDef(TypedDict):
    targetResourceAggregations: List[CisTargetResourceAggregationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListCisScansFilterCriteriaTypeDef(TypedDict):
    failedChecksFilters: NotRequired[Sequence[CisNumberFilterTypeDef]]
    scanArnFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    scanAtFilters: NotRequired[Sequence[CisDateFilterTypeDef]]
    scanConfigurationArnFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    scanNameFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    scanStatusFilters: NotRequired[Sequence[CisScanStatusFilterTypeDef]]
    scheduledByFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    targetAccountIdFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    targetResourceIdFilters: NotRequired[Sequence[CisStringFilterTypeDef]]
    targetResourceTagFilters: NotRequired[Sequence[TagFilterTypeDef]]

class CoverageFilterCriteriaTypeDef(TypedDict):
    accountId: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    ec2InstanceTags: NotRequired[Sequence[CoverageMapFilterTypeDef]]
    ecrImageTags: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    ecrRepositoryName: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    imagePulledAt: NotRequired[Sequence[CoverageDateFilterTypeDef]]
    lambdaFunctionName: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    lambdaFunctionRuntime: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    lambdaFunctionTags: NotRequired[Sequence[CoverageMapFilterTypeDef]]
    lastScannedAt: NotRequired[Sequence[CoverageDateFilterTypeDef]]
    resourceId: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    resourceType: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    scanMode: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    scanStatusCode: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    scanStatusReason: NotRequired[Sequence[CoverageStringFilterTypeDef]]
    scanType: NotRequired[Sequence[CoverageStringFilterTypeDef]]

class ListCisScansResponseTypeDef(TypedDict):
    scans: List[CisScanTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetCisScanResultDetailsRequestPaginateTypeDef(TypedDict):
    accountId: str
    scanArn: str
    targetResourceId: str
    filterCriteria: NotRequired[CisScanResultDetailsFilterCriteriaTypeDef]
    sortBy: NotRequired[CisScanResultDetailsSortByType]
    sortOrder: NotRequired[CisSortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetCisScanResultDetailsRequestTypeDef(TypedDict):
    accountId: str
    scanArn: str
    targetResourceId: str
    filterCriteria: NotRequired[CisScanResultDetailsFilterCriteriaTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sortBy: NotRequired[CisScanResultDetailsSortByType]
    sortOrder: NotRequired[CisSortOrderType]

class ListCisScanResultsAggregatedByChecksRequestPaginateTypeDef(TypedDict):
    scanArn: str
    filterCriteria: NotRequired[CisScanResultsAggregatedByChecksFilterCriteriaTypeDef]
    sortBy: NotRequired[CisScanResultsAggregatedByChecksSortByType]
    sortOrder: NotRequired[CisSortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCisScanResultsAggregatedByChecksRequestTypeDef(TypedDict):
    scanArn: str
    filterCriteria: NotRequired[CisScanResultsAggregatedByChecksFilterCriteriaTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sortBy: NotRequired[CisScanResultsAggregatedByChecksSortByType]
    sortOrder: NotRequired[CisSortOrderType]

class ListCisScanResultsAggregatedByTargetResourceRequestPaginateTypeDef(TypedDict):
    scanArn: str
    filterCriteria: NotRequired[CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef]
    sortBy: NotRequired[CisScanResultsAggregatedByTargetResourceSortByType]
    sortOrder: NotRequired[CisSortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCisScanResultsAggregatedByTargetResourceRequestTypeDef(TypedDict):
    scanArn: str
    filterCriteria: NotRequired[CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sortBy: NotRequired[CisScanResultsAggregatedByTargetResourceSortByType]
    sortOrder: NotRequired[CisSortOrderType]

class ListCisScanConfigurationsRequestPaginateTypeDef(TypedDict):
    filterCriteria: NotRequired[ListCisScanConfigurationsFilterCriteriaTypeDef]
    sortBy: NotRequired[CisScanConfigurationsSortByType]
    sortOrder: NotRequired[CisSortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCisScanConfigurationsRequestTypeDef(TypedDict):
    filterCriteria: NotRequired[ListCisScanConfigurationsFilterCriteriaTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sortBy: NotRequired[CisScanConfigurationsSortByType]
    sortOrder: NotRequired[CisSortOrderType]

class BatchGetCodeSnippetResponseTypeDef(TypedDict):
    codeSnippetResults: List[CodeSnippetResultTypeDef]
    errors: List[CodeSnippetErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InspectorScoreDetailsTypeDef(TypedDict):
    adjustedCvss: NotRequired[CvssScoreDetailsTypeDef]

class ScheduleOutputTypeDef(TypedDict):
    daily: NotRequired[DailyScheduleTypeDef]
    monthly: NotRequired[MonthlyScheduleTypeDef]
    oneTime: NotRequired[Dict[str, Any]]
    weekly: NotRequired[WeeklyScheduleOutputTypeDef]

class ScheduleTypeDef(TypedDict):
    daily: NotRequired[DailyScheduleTypeDef]
    monthly: NotRequired[MonthlyScheduleTypeDef]
    oneTime: NotRequired[Mapping[str, Any]]
    weekly: NotRequired[WeeklyScheduleTypeDef]

class AggregationRequestTypeDef(TypedDict):
    accountAggregation: NotRequired[AccountAggregationTypeDef]
    amiAggregation: NotRequired[AmiAggregationTypeDef]
    awsEcrContainerAggregation: NotRequired[AwsEcrContainerAggregationTypeDef]
    ec2InstanceAggregation: NotRequired[Ec2InstanceAggregationTypeDef]
    findingTypeAggregation: NotRequired[FindingTypeAggregationTypeDef]
    imageLayerAggregation: NotRequired[ImageLayerAggregationTypeDef]
    lambdaFunctionAggregation: NotRequired[LambdaFunctionAggregationTypeDef]
    lambdaLayerAggregation: NotRequired[LambdaLayerAggregationTypeDef]
    packageAggregation: NotRequired[PackageAggregationTypeDef]
    repositoryAggregation: NotRequired[RepositoryAggregationTypeDef]
    titleAggregation: NotRequired[TitleAggregationTypeDef]

class GetConfigurationResponseTypeDef(TypedDict):
    ec2Configuration: Ec2ConfigurationStateTypeDef
    ecrConfiguration: EcrConfigurationStateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetFindingDetailsResponseTypeDef(TypedDict):
    errors: List[FindingDetailsErrorTypeDef]
    findingDetails: List[FindingDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchVulnerabilitiesResponseTypeDef(TypedDict):
    vulnerabilities: List[VulnerabilityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class FilterCriteriaOutputTypeDef(TypedDict):
    awsAccountId: NotRequired[List[StringFilterTypeDef]]
    codeVulnerabilityDetectorName: NotRequired[List[StringFilterTypeDef]]
    codeVulnerabilityDetectorTags: NotRequired[List[StringFilterTypeDef]]
    codeVulnerabilityFilePath: NotRequired[List[StringFilterTypeDef]]
    componentId: NotRequired[List[StringFilterTypeDef]]
    componentType: NotRequired[List[StringFilterTypeDef]]
    ec2InstanceImageId: NotRequired[List[StringFilterTypeDef]]
    ec2InstanceSubnetId: NotRequired[List[StringFilterTypeDef]]
    ec2InstanceVpcId: NotRequired[List[StringFilterTypeDef]]
    ecrImageArchitecture: NotRequired[List[StringFilterTypeDef]]
    ecrImageHash: NotRequired[List[StringFilterTypeDef]]
    ecrImagePushedAt: NotRequired[List[DateFilterOutputTypeDef]]
    ecrImageRegistry: NotRequired[List[StringFilterTypeDef]]
    ecrImageRepositoryName: NotRequired[List[StringFilterTypeDef]]
    ecrImageTags: NotRequired[List[StringFilterTypeDef]]
    epssScore: NotRequired[List[NumberFilterTypeDef]]
    exploitAvailable: NotRequired[List[StringFilterTypeDef]]
    findingArn: NotRequired[List[StringFilterTypeDef]]
    findingStatus: NotRequired[List[StringFilterTypeDef]]
    findingType: NotRequired[List[StringFilterTypeDef]]
    firstObservedAt: NotRequired[List[DateFilterOutputTypeDef]]
    fixAvailable: NotRequired[List[StringFilterTypeDef]]
    inspectorScore: NotRequired[List[NumberFilterTypeDef]]
    lambdaFunctionExecutionRoleArn: NotRequired[List[StringFilterTypeDef]]
    lambdaFunctionLastModifiedAt: NotRequired[List[DateFilterOutputTypeDef]]
    lambdaFunctionLayers: NotRequired[List[StringFilterTypeDef]]
    lambdaFunctionName: NotRequired[List[StringFilterTypeDef]]
    lambdaFunctionRuntime: NotRequired[List[StringFilterTypeDef]]
    lastObservedAt: NotRequired[List[DateFilterOutputTypeDef]]
    networkProtocol: NotRequired[List[StringFilterTypeDef]]
    portRange: NotRequired[List[PortRangeFilterTypeDef]]
    relatedVulnerabilities: NotRequired[List[StringFilterTypeDef]]
    resourceId: NotRequired[List[StringFilterTypeDef]]
    resourceTags: NotRequired[List[MapFilterTypeDef]]
    resourceType: NotRequired[List[StringFilterTypeDef]]
    severity: NotRequired[List[StringFilterTypeDef]]
    title: NotRequired[List[StringFilterTypeDef]]
    updatedAt: NotRequired[List[DateFilterOutputTypeDef]]
    vendorSeverity: NotRequired[List[StringFilterTypeDef]]
    vulnerabilityId: NotRequired[List[StringFilterTypeDef]]
    vulnerabilitySource: NotRequired[List[StringFilterTypeDef]]
    vulnerablePackages: NotRequired[List[PackageFilterTypeDef]]

class FilterCriteriaTypeDef(TypedDict):
    awsAccountId: NotRequired[Sequence[StringFilterTypeDef]]
    codeVulnerabilityDetectorName: NotRequired[Sequence[StringFilterTypeDef]]
    codeVulnerabilityDetectorTags: NotRequired[Sequence[StringFilterTypeDef]]
    codeVulnerabilityFilePath: NotRequired[Sequence[StringFilterTypeDef]]
    componentId: NotRequired[Sequence[StringFilterTypeDef]]
    componentType: NotRequired[Sequence[StringFilterTypeDef]]
    ec2InstanceImageId: NotRequired[Sequence[StringFilterTypeDef]]
    ec2InstanceSubnetId: NotRequired[Sequence[StringFilterTypeDef]]
    ec2InstanceVpcId: NotRequired[Sequence[StringFilterTypeDef]]
    ecrImageArchitecture: NotRequired[Sequence[StringFilterTypeDef]]
    ecrImageHash: NotRequired[Sequence[StringFilterTypeDef]]
    ecrImagePushedAt: NotRequired[Sequence[DateFilterTypeDef]]
    ecrImageRegistry: NotRequired[Sequence[StringFilterTypeDef]]
    ecrImageRepositoryName: NotRequired[Sequence[StringFilterTypeDef]]
    ecrImageTags: NotRequired[Sequence[StringFilterTypeDef]]
    epssScore: NotRequired[Sequence[NumberFilterTypeDef]]
    exploitAvailable: NotRequired[Sequence[StringFilterTypeDef]]
    findingArn: NotRequired[Sequence[StringFilterTypeDef]]
    findingStatus: NotRequired[Sequence[StringFilterTypeDef]]
    findingType: NotRequired[Sequence[StringFilterTypeDef]]
    firstObservedAt: NotRequired[Sequence[DateFilterTypeDef]]
    fixAvailable: NotRequired[Sequence[StringFilterTypeDef]]
    inspectorScore: NotRequired[Sequence[NumberFilterTypeDef]]
    lambdaFunctionExecutionRoleArn: NotRequired[Sequence[StringFilterTypeDef]]
    lambdaFunctionLastModifiedAt: NotRequired[Sequence[DateFilterTypeDef]]
    lambdaFunctionLayers: NotRequired[Sequence[StringFilterTypeDef]]
    lambdaFunctionName: NotRequired[Sequence[StringFilterTypeDef]]
    lambdaFunctionRuntime: NotRequired[Sequence[StringFilterTypeDef]]
    lastObservedAt: NotRequired[Sequence[DateFilterTypeDef]]
    networkProtocol: NotRequired[Sequence[StringFilterTypeDef]]
    portRange: NotRequired[Sequence[PortRangeFilterTypeDef]]
    relatedVulnerabilities: NotRequired[Sequence[StringFilterTypeDef]]
    resourceId: NotRequired[Sequence[StringFilterTypeDef]]
    resourceTags: NotRequired[Sequence[MapFilterTypeDef]]
    resourceType: NotRequired[Sequence[StringFilterTypeDef]]
    severity: NotRequired[Sequence[StringFilterTypeDef]]
    title: NotRequired[Sequence[StringFilterTypeDef]]
    updatedAt: NotRequired[Sequence[DateFilterTypeDef]]
    vendorSeverity: NotRequired[Sequence[StringFilterTypeDef]]
    vulnerabilityId: NotRequired[Sequence[StringFilterTypeDef]]
    vulnerabilitySource: NotRequired[Sequence[StringFilterTypeDef]]
    vulnerablePackages: NotRequired[Sequence[PackageFilterTypeDef]]

class BatchGetFreeTrialInfoResponseTypeDef(TypedDict):
    accounts: List[FreeTrialAccountInfoTypeDef]
    failedAccounts: List[FreeTrialInfoErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CoveredResourceTypeDef(TypedDict):
    accountId: str
    resourceId: str
    resourceType: CoverageResourceTypeType
    scanType: ScanTypeType
    lastScannedAt: NotRequired[datetime]
    resourceMetadata: NotRequired[ResourceScanMetadataTypeDef]
    scanMode: NotRequired[ScanModeType]
    scanStatus: NotRequired[ScanStatusTypeDef]

class NetworkReachabilityDetailsTypeDef(TypedDict):
    networkPath: NetworkPathTypeDef
    openPortRange: PortRangeTypeDef
    protocol: NetworkProtocolType

GetSbomExportResponseTypeDef = TypedDict(
    "GetSbomExportResponseTypeDef",
    {
        "errorCode": ReportingErrorCodeType,
        "errorMessage": str,
        "filterCriteria": ResourceFilterCriteriaOutputTypeDef,
        "format": SbomReportFormatType,
        "reportId": str,
        "s3Destination": DestinationTypeDef,
        "status": ExternalReportStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResourceFilterCriteriaUnionTypeDef = Union[
    ResourceFilterCriteriaTypeDef, ResourceFilterCriteriaOutputTypeDef
]

class StopCisSessionRequestTypeDef(TypedDict):
    message: StopCisSessionMessageTypeDef
    scanJobId: str
    sessionToken: str

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

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "id": str,
        "type": ResourceTypeType,
        "details": NotRequired[ResourceDetailsTypeDef],
        "partition": NotRequired[str],
        "region": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

class ListCisScansRequestPaginateTypeDef(TypedDict):
    detailLevel: NotRequired[ListCisScansDetailLevelType]
    filterCriteria: NotRequired[ListCisScansFilterCriteriaTypeDef]
    sortBy: NotRequired[ListCisScansSortByType]
    sortOrder: NotRequired[CisSortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCisScansRequestTypeDef(TypedDict):
    detailLevel: NotRequired[ListCisScansDetailLevelType]
    filterCriteria: NotRequired[ListCisScansFilterCriteriaTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sortBy: NotRequired[ListCisScansSortByType]
    sortOrder: NotRequired[CisSortOrderType]

class ListCoverageRequestPaginateTypeDef(TypedDict):
    filterCriteria: NotRequired[CoverageFilterCriteriaTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCoverageRequestTypeDef(TypedDict):
    filterCriteria: NotRequired[CoverageFilterCriteriaTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListCoverageStatisticsRequestPaginateTypeDef(TypedDict):
    filterCriteria: NotRequired[CoverageFilterCriteriaTypeDef]
    groupBy: NotRequired[GroupKeyType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCoverageStatisticsRequestTypeDef(TypedDict):
    filterCriteria: NotRequired[CoverageFilterCriteriaTypeDef]
    groupBy: NotRequired[GroupKeyType]
    nextToken: NotRequired[str]

class CisScanConfigurationTypeDef(TypedDict):
    scanConfigurationArn: str
    ownerId: NotRequired[str]
    scanName: NotRequired[str]
    schedule: NotRequired[ScheduleOutputTypeDef]
    securityLevel: NotRequired[CisSecurityLevelType]
    tags: NotRequired[Dict[str, str]]
    targets: NotRequired[CisTargetsTypeDef]

ScheduleUnionTypeDef = Union[ScheduleTypeDef, ScheduleOutputTypeDef]

class ListFindingAggregationsRequestPaginateTypeDef(TypedDict):
    aggregationType: AggregationTypeType
    accountIds: NotRequired[Sequence[StringFilterTypeDef]]
    aggregationRequest: NotRequired[AggregationRequestTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFindingAggregationsRequestTypeDef(TypedDict):
    aggregationType: AggregationTypeType
    accountIds: NotRequired[Sequence[StringFilterTypeDef]]
    aggregationRequest: NotRequired[AggregationRequestTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class FilterTypeDef(TypedDict):
    action: FilterActionType
    arn: str
    createdAt: datetime
    criteria: FilterCriteriaOutputTypeDef
    name: str
    ownerId: str
    updatedAt: datetime
    description: NotRequired[str]
    reason: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class GetFindingsReportStatusResponseTypeDef(TypedDict):
    destination: DestinationTypeDef
    errorCode: ReportingErrorCodeType
    errorMessage: str
    filterCriteria: FilterCriteriaOutputTypeDef
    reportId: str
    status: ExternalReportStatusType
    ResponseMetadata: ResponseMetadataTypeDef

FilterCriteriaUnionTypeDef = Union[FilterCriteriaTypeDef, FilterCriteriaOutputTypeDef]

class ListCoverageResponseTypeDef(TypedDict):
    coveredResources: List[CoveredResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateSbomExportRequestTypeDef(TypedDict):
    reportFormat: SbomReportFormatType
    s3Destination: DestinationTypeDef
    resourceFilterCriteria: NotRequired[ResourceFilterCriteriaUnionTypeDef]

FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "awsAccountId": str,
        "description": str,
        "findingArn": str,
        "firstObservedAt": datetime,
        "lastObservedAt": datetime,
        "remediation": RemediationTypeDef,
        "resources": List[ResourceTypeDef],
        "severity": SeverityType,
        "status": FindingStatusType,
        "type": FindingTypeType,
        "codeVulnerabilityDetails": NotRequired[CodeVulnerabilityDetailsTypeDef],
        "epss": NotRequired[EpssDetailsTypeDef],
        "exploitAvailable": NotRequired[ExploitAvailableType],
        "exploitabilityDetails": NotRequired[ExploitabilityDetailsTypeDef],
        "fixAvailable": NotRequired[FixAvailableType],
        "inspectorScore": NotRequired[float],
        "inspectorScoreDetails": NotRequired[InspectorScoreDetailsTypeDef],
        "networkReachabilityDetails": NotRequired[NetworkReachabilityDetailsTypeDef],
        "packageVulnerabilityDetails": NotRequired[PackageVulnerabilityDetailsTypeDef],
        "title": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)

class ListCisScanConfigurationsResponseTypeDef(TypedDict):
    scanConfigurations: List[CisScanConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateCisScanConfigurationRequestTypeDef(TypedDict):
    scanName: str
    schedule: ScheduleUnionTypeDef
    securityLevel: CisSecurityLevelType
    targets: CreateCisTargetsTypeDef
    tags: NotRequired[Mapping[str, str]]

class UpdateCisScanConfigurationRequestTypeDef(TypedDict):
    scanConfigurationArn: str
    scanName: NotRequired[str]
    schedule: NotRequired[ScheduleUnionTypeDef]
    securityLevel: NotRequired[CisSecurityLevelType]
    targets: NotRequired[UpdateCisTargetsTypeDef]

class ListFiltersResponseTypeDef(TypedDict):
    filters: List[FilterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateFilterRequestTypeDef(TypedDict):
    action: FilterActionType
    filterCriteria: FilterCriteriaUnionTypeDef
    name: str
    description: NotRequired[str]
    reason: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateFindingsReportRequestTypeDef(TypedDict):
    reportFormat: ReportFormatType
    s3Destination: DestinationTypeDef
    filterCriteria: NotRequired[FilterCriteriaUnionTypeDef]

class ListFindingsRequestPaginateTypeDef(TypedDict):
    filterCriteria: NotRequired[FilterCriteriaUnionTypeDef]
    sortCriteria: NotRequired[SortCriteriaTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFindingsRequestTypeDef(TypedDict):
    filterCriteria: NotRequired[FilterCriteriaUnionTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sortCriteria: NotRequired[SortCriteriaTypeDef]

class UpdateFilterRequestTypeDef(TypedDict):
    filterArn: str
    action: NotRequired[FilterActionType]
    description: NotRequired[str]
    filterCriteria: NotRequired[FilterCriteriaUnionTypeDef]
    name: NotRequired[str]
    reason: NotRequired[str]

class ListFindingsResponseTypeDef(TypedDict):
    findings: List[FindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
