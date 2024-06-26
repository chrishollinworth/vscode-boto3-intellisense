"""
Type annotations for inspector2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_inspector2.type_defs import AccountAggregationResponseTypeDef

    data: AccountAggregationResponseTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountAggregationResponseTypeDef",
    "AccountAggregationTypeDef",
    "AccountStateTypeDef",
    "AccountTypeDef",
    "AggregationRequestTypeDef",
    "AggregationResponseTypeDef",
    "AmiAggregationResponseTypeDef",
    "AmiAggregationTypeDef",
    "AssociateMemberRequestRequestTypeDef",
    "AssociateMemberResponseTypeDef",
    "AtigDataTypeDef",
    "AutoEnableTypeDef",
    "AwsEc2InstanceDetailsTypeDef",
    "AwsEcrContainerAggregationResponseTypeDef",
    "AwsEcrContainerAggregationTypeDef",
    "AwsEcrContainerImageDetailsTypeDef",
    "AwsLambdaFunctionDetailsTypeDef",
    "BatchGetAccountStatusRequestRequestTypeDef",
    "BatchGetAccountStatusResponseTypeDef",
    "BatchGetCodeSnippetRequestRequestTypeDef",
    "BatchGetCodeSnippetResponseTypeDef",
    "BatchGetFindingDetailsRequestRequestTypeDef",
    "BatchGetFindingDetailsResponseTypeDef",
    "BatchGetFreeTrialInfoRequestRequestTypeDef",
    "BatchGetFreeTrialInfoResponseTypeDef",
    "BatchGetMemberEc2DeepInspectionStatusRequestRequestTypeDef",
    "BatchGetMemberEc2DeepInspectionStatusResponseTypeDef",
    "BatchUpdateMemberEc2DeepInspectionStatusRequestRequestTypeDef",
    "BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef",
    "CancelFindingsReportRequestRequestTypeDef",
    "CancelFindingsReportResponseTypeDef",
    "CancelSbomExportRequestRequestTypeDef",
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
    "CreateCisScanConfigurationRequestRequestTypeDef",
    "CreateCisScanConfigurationResponseTypeDef",
    "CreateCisTargetsTypeDef",
    "CreateFilterRequestRequestTypeDef",
    "CreateFilterResponseTypeDef",
    "CreateFindingsReportRequestRequestTypeDef",
    "CreateFindingsReportResponseTypeDef",
    "CreateSbomExportRequestRequestTypeDef",
    "CreateSbomExportResponseTypeDef",
    "Cvss2TypeDef",
    "Cvss3TypeDef",
    "CvssScoreAdjustmentTypeDef",
    "CvssScoreDetailsTypeDef",
    "CvssScoreTypeDef",
    "DailyScheduleTypeDef",
    "DateFilterTypeDef",
    "DelegatedAdminAccountTypeDef",
    "DelegatedAdminTypeDef",
    "DeleteCisScanConfigurationRequestRequestTypeDef",
    "DeleteCisScanConfigurationResponseTypeDef",
    "DeleteFilterRequestRequestTypeDef",
    "DeleteFilterResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DestinationTypeDef",
    "DisableDelegatedAdminAccountRequestRequestTypeDef",
    "DisableDelegatedAdminAccountResponseTypeDef",
    "DisableRequestRequestTypeDef",
    "DisableResponseTypeDef",
    "DisassociateMemberRequestRequestTypeDef",
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
    "EnableDelegatedAdminAccountRequestRequestTypeDef",
    "EnableDelegatedAdminAccountResponseTypeDef",
    "EnableRequestRequestTypeDef",
    "EnableResponseTypeDef",
    "EpssDetailsTypeDef",
    "EpssTypeDef",
    "EvidenceTypeDef",
    "ExploitObservedTypeDef",
    "ExploitabilityDetailsTypeDef",
    "FailedAccountTypeDef",
    "FailedMemberAccountEc2DeepInspectionStatusStateTypeDef",
    "FilterCriteriaTypeDef",
    "FilterTypeDef",
    "FindingDetailTypeDef",
    "FindingDetailsErrorTypeDef",
    "FindingTypeAggregationResponseTypeDef",
    "FindingTypeAggregationTypeDef",
    "FindingTypeDef",
    "FreeTrialAccountInfoTypeDef",
    "FreeTrialInfoErrorTypeDef",
    "FreeTrialInfoTypeDef",
    "GetCisScanReportRequestRequestTypeDef",
    "GetCisScanReportResponseTypeDef",
    "GetCisScanResultDetailsRequestRequestTypeDef",
    "GetCisScanResultDetailsResponseTypeDef",
    "GetConfigurationResponseTypeDef",
    "GetDelegatedAdminAccountResponseTypeDef",
    "GetEc2DeepInspectionConfigurationResponseTypeDef",
    "GetEncryptionKeyRequestRequestTypeDef",
    "GetEncryptionKeyResponseTypeDef",
    "GetFindingsReportStatusRequestRequestTypeDef",
    "GetFindingsReportStatusResponseTypeDef",
    "GetMemberRequestRequestTypeDef",
    "GetMemberResponseTypeDef",
    "GetSbomExportRequestRequestTypeDef",
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
    "ListAccountPermissionsRequestRequestTypeDef",
    "ListAccountPermissionsResponseTypeDef",
    "ListCisScanConfigurationsFilterCriteriaTypeDef",
    "ListCisScanConfigurationsRequestRequestTypeDef",
    "ListCisScanConfigurationsResponseTypeDef",
    "ListCisScanResultsAggregatedByChecksRequestRequestTypeDef",
    "ListCisScanResultsAggregatedByChecksResponseTypeDef",
    "ListCisScanResultsAggregatedByTargetResourceRequestRequestTypeDef",
    "ListCisScanResultsAggregatedByTargetResourceResponseTypeDef",
    "ListCisScansFilterCriteriaTypeDef",
    "ListCisScansRequestRequestTypeDef",
    "ListCisScansResponseTypeDef",
    "ListCoverageRequestRequestTypeDef",
    "ListCoverageResponseTypeDef",
    "ListCoverageStatisticsRequestRequestTypeDef",
    "ListCoverageStatisticsResponseTypeDef",
    "ListDelegatedAdminAccountsRequestRequestTypeDef",
    "ListDelegatedAdminAccountsResponseTypeDef",
    "ListFiltersRequestRequestTypeDef",
    "ListFiltersResponseTypeDef",
    "ListFindingAggregationsRequestRequestTypeDef",
    "ListFindingAggregationsResponseTypeDef",
    "ListFindingsRequestRequestTypeDef",
    "ListFindingsResponseTypeDef",
    "ListMembersRequestRequestTypeDef",
    "ListMembersResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsageTotalsRequestRequestTypeDef",
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
    "ResetEncryptionKeyRequestRequestTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceFilterCriteriaTypeDef",
    "ResourceMapFilterTypeDef",
    "ResourceScanMetadataTypeDef",
    "ResourceStateTypeDef",
    "ResourceStatusTypeDef",
    "ResourceStringFilterTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "ScanStatusTypeDef",
    "ScheduleTypeDef",
    "SearchVulnerabilitiesFilterCriteriaTypeDef",
    "SearchVulnerabilitiesRequestRequestTypeDef",
    "SearchVulnerabilitiesResponseTypeDef",
    "SendCisSessionHealthRequestRequestTypeDef",
    "SendCisSessionTelemetryRequestRequestTypeDef",
    "SeverityCountsTypeDef",
    "SortCriteriaTypeDef",
    "StartCisSessionMessageTypeDef",
    "StartCisSessionRequestRequestTypeDef",
    "StateTypeDef",
    "StatusCountsTypeDef",
    "StepTypeDef",
    "StopCisMessageProgressTypeDef",
    "StopCisSessionMessageTypeDef",
    "StopCisSessionRequestRequestTypeDef",
    "StringFilterTypeDef",
    "SuggestedFixTypeDef",
    "TagFilterTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TimeTypeDef",
    "TitleAggregationResponseTypeDef",
    "TitleAggregationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCisScanConfigurationRequestRequestTypeDef",
    "UpdateCisScanConfigurationResponseTypeDef",
    "UpdateCisTargetsTypeDef",
    "UpdateConfigurationRequestRequestTypeDef",
    "UpdateEc2DeepInspectionConfigurationRequestRequestTypeDef",
    "UpdateEc2DeepInspectionConfigurationResponseTypeDef",
    "UpdateEncryptionKeyRequestRequestTypeDef",
    "UpdateFilterRequestRequestTypeDef",
    "UpdateFilterResponseTypeDef",
    "UpdateOrgEc2DeepInspectionConfigurationRequestRequestTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    "UpdateOrganizationConfigurationResponseTypeDef",
    "UsageTotalTypeDef",
    "UsageTypeDef",
    "VulnerabilityTypeDef",
    "VulnerablePackageTypeDef",
    "WeeklyScheduleTypeDef",
)

AccountAggregationResponseTypeDef = TypedDict(
    "AccountAggregationResponseTypeDef",
    {
        "accountId": str,
        "severityCounts": "SeverityCountsTypeDef",
    },
    total=False,
)

AccountAggregationTypeDef = TypedDict(
    "AccountAggregationTypeDef",
    {
        "findingType": AggregationFindingTypeType,
        "resourceType": AggregationResourceTypeType,
        "sortBy": AccountSortByType,
        "sortOrder": SortOrderType,
    },
    total=False,
)

AccountStateTypeDef = TypedDict(
    "AccountStateTypeDef",
    {
        "accountId": str,
        "resourceState": "ResourceStateTypeDef",
        "state": "StateTypeDef",
    },
)

AccountTypeDef = TypedDict(
    "AccountTypeDef",
    {
        "accountId": str,
        "resourceStatus": "ResourceStatusTypeDef",
        "status": StatusType,
    },
)

AggregationRequestTypeDef = TypedDict(
    "AggregationRequestTypeDef",
    {
        "accountAggregation": "AccountAggregationTypeDef",
        "amiAggregation": "AmiAggregationTypeDef",
        "awsEcrContainerAggregation": "AwsEcrContainerAggregationTypeDef",
        "ec2InstanceAggregation": "Ec2InstanceAggregationTypeDef",
        "findingTypeAggregation": "FindingTypeAggregationTypeDef",
        "imageLayerAggregation": "ImageLayerAggregationTypeDef",
        "lambdaFunctionAggregation": "LambdaFunctionAggregationTypeDef",
        "lambdaLayerAggregation": "LambdaLayerAggregationTypeDef",
        "packageAggregation": "PackageAggregationTypeDef",
        "repositoryAggregation": "RepositoryAggregationTypeDef",
        "titleAggregation": "TitleAggregationTypeDef",
    },
    total=False,
)

AggregationResponseTypeDef = TypedDict(
    "AggregationResponseTypeDef",
    {
        "accountAggregation": "AccountAggregationResponseTypeDef",
        "amiAggregation": "AmiAggregationResponseTypeDef",
        "awsEcrContainerAggregation": "AwsEcrContainerAggregationResponseTypeDef",
        "ec2InstanceAggregation": "Ec2InstanceAggregationResponseTypeDef",
        "findingTypeAggregation": "FindingTypeAggregationResponseTypeDef",
        "imageLayerAggregation": "ImageLayerAggregationResponseTypeDef",
        "lambdaFunctionAggregation": "LambdaFunctionAggregationResponseTypeDef",
        "lambdaLayerAggregation": "LambdaLayerAggregationResponseTypeDef",
        "packageAggregation": "PackageAggregationResponseTypeDef",
        "repositoryAggregation": "RepositoryAggregationResponseTypeDef",
        "titleAggregation": "TitleAggregationResponseTypeDef",
    },
    total=False,
)

_RequiredAmiAggregationResponseTypeDef = TypedDict(
    "_RequiredAmiAggregationResponseTypeDef",
    {
        "ami": str,
    },
)
_OptionalAmiAggregationResponseTypeDef = TypedDict(
    "_OptionalAmiAggregationResponseTypeDef",
    {
        "accountId": str,
        "affectedInstances": int,
        "severityCounts": "SeverityCountsTypeDef",
    },
    total=False,
)

class AmiAggregationResponseTypeDef(
    _RequiredAmiAggregationResponseTypeDef, _OptionalAmiAggregationResponseTypeDef
):
    pass

AmiAggregationTypeDef = TypedDict(
    "AmiAggregationTypeDef",
    {
        "amis": List["StringFilterTypeDef"],
        "sortBy": AmiSortByType,
        "sortOrder": SortOrderType,
    },
    total=False,
)

AssociateMemberRequestRequestTypeDef = TypedDict(
    "AssociateMemberRequestRequestTypeDef",
    {
        "accountId": str,
    },
)

AssociateMemberResponseTypeDef = TypedDict(
    "AssociateMemberResponseTypeDef",
    {
        "accountId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AtigDataTypeDef = TypedDict(
    "AtigDataTypeDef",
    {
        "firstSeen": datetime,
        "lastSeen": datetime,
        "targets": List[str],
        "ttps": List[str],
    },
    total=False,
)

_RequiredAutoEnableTypeDef = TypedDict(
    "_RequiredAutoEnableTypeDef",
    {
        "ec2": bool,
        "ecr": bool,
    },
)
_OptionalAutoEnableTypeDef = TypedDict(
    "_OptionalAutoEnableTypeDef",
    {
        "lambda": bool,
        "lambdaCode": bool,
    },
    total=False,
)

class AutoEnableTypeDef(_RequiredAutoEnableTypeDef, _OptionalAutoEnableTypeDef):
    pass

AwsEc2InstanceDetailsTypeDef = TypedDict(
    "AwsEc2InstanceDetailsTypeDef",
    {
        "iamInstanceProfileArn": str,
        "imageId": str,
        "ipV4Addresses": List[str],
        "ipV6Addresses": List[str],
        "keyName": str,
        "launchedAt": datetime,
        "platform": str,
        "subnetId": str,
        "type": str,
        "vpcId": str,
    },
    total=False,
)

_RequiredAwsEcrContainerAggregationResponseTypeDef = TypedDict(
    "_RequiredAwsEcrContainerAggregationResponseTypeDef",
    {
        "resourceId": str,
    },
)
_OptionalAwsEcrContainerAggregationResponseTypeDef = TypedDict(
    "_OptionalAwsEcrContainerAggregationResponseTypeDef",
    {
        "accountId": str,
        "architecture": str,
        "imageSha": str,
        "imageTags": List[str],
        "repository": str,
        "severityCounts": "SeverityCountsTypeDef",
    },
    total=False,
)

class AwsEcrContainerAggregationResponseTypeDef(
    _RequiredAwsEcrContainerAggregationResponseTypeDef,
    _OptionalAwsEcrContainerAggregationResponseTypeDef,
):
    pass

AwsEcrContainerAggregationTypeDef = TypedDict(
    "AwsEcrContainerAggregationTypeDef",
    {
        "architectures": List["StringFilterTypeDef"],
        "imageShas": List["StringFilterTypeDef"],
        "imageTags": List["StringFilterTypeDef"],
        "repositories": List["StringFilterTypeDef"],
        "resourceIds": List["StringFilterTypeDef"],
        "sortBy": AwsEcrContainerSortByType,
        "sortOrder": SortOrderType,
    },
    total=False,
)

_RequiredAwsEcrContainerImageDetailsTypeDef = TypedDict(
    "_RequiredAwsEcrContainerImageDetailsTypeDef",
    {
        "imageHash": str,
        "registry": str,
        "repositoryName": str,
    },
)
_OptionalAwsEcrContainerImageDetailsTypeDef = TypedDict(
    "_OptionalAwsEcrContainerImageDetailsTypeDef",
    {
        "architecture": str,
        "author": str,
        "imageTags": List[str],
        "platform": str,
        "pushedAt": datetime,
    },
    total=False,
)

class AwsEcrContainerImageDetailsTypeDef(
    _RequiredAwsEcrContainerImageDetailsTypeDef, _OptionalAwsEcrContainerImageDetailsTypeDef
):
    pass

_RequiredAwsLambdaFunctionDetailsTypeDef = TypedDict(
    "_RequiredAwsLambdaFunctionDetailsTypeDef",
    {
        "codeSha256": str,
        "executionRoleArn": str,
        "functionName": str,
        "runtime": RuntimeType,
        "version": str,
    },
)
_OptionalAwsLambdaFunctionDetailsTypeDef = TypedDict(
    "_OptionalAwsLambdaFunctionDetailsTypeDef",
    {
        "architectures": List[ArchitectureType],
        "lastModifiedAt": datetime,
        "layers": List[str],
        "packageType": PackageTypeType,
        "vpcConfig": "LambdaVpcConfigTypeDef",
    },
    total=False,
)

class AwsLambdaFunctionDetailsTypeDef(
    _RequiredAwsLambdaFunctionDetailsTypeDef, _OptionalAwsLambdaFunctionDetailsTypeDef
):
    pass

BatchGetAccountStatusRequestRequestTypeDef = TypedDict(
    "BatchGetAccountStatusRequestRequestTypeDef",
    {
        "accountIds": List[str],
    },
    total=False,
)

BatchGetAccountStatusResponseTypeDef = TypedDict(
    "BatchGetAccountStatusResponseTypeDef",
    {
        "accounts": List["AccountStateTypeDef"],
        "failedAccounts": List["FailedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetCodeSnippetRequestRequestTypeDef = TypedDict(
    "BatchGetCodeSnippetRequestRequestTypeDef",
    {
        "findingArns": List[str],
    },
)

BatchGetCodeSnippetResponseTypeDef = TypedDict(
    "BatchGetCodeSnippetResponseTypeDef",
    {
        "codeSnippetResults": List["CodeSnippetResultTypeDef"],
        "errors": List["CodeSnippetErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetFindingDetailsRequestRequestTypeDef = TypedDict(
    "BatchGetFindingDetailsRequestRequestTypeDef",
    {
        "findingArns": List[str],
    },
)

BatchGetFindingDetailsResponseTypeDef = TypedDict(
    "BatchGetFindingDetailsResponseTypeDef",
    {
        "errors": List["FindingDetailsErrorTypeDef"],
        "findingDetails": List["FindingDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetFreeTrialInfoRequestRequestTypeDef = TypedDict(
    "BatchGetFreeTrialInfoRequestRequestTypeDef",
    {
        "accountIds": List[str],
    },
)

BatchGetFreeTrialInfoResponseTypeDef = TypedDict(
    "BatchGetFreeTrialInfoResponseTypeDef",
    {
        "accounts": List["FreeTrialAccountInfoTypeDef"],
        "failedAccounts": List["FreeTrialInfoErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetMemberEc2DeepInspectionStatusRequestRequestTypeDef = TypedDict(
    "BatchGetMemberEc2DeepInspectionStatusRequestRequestTypeDef",
    {
        "accountIds": List[str],
    },
    total=False,
)

BatchGetMemberEc2DeepInspectionStatusResponseTypeDef = TypedDict(
    "BatchGetMemberEc2DeepInspectionStatusResponseTypeDef",
    {
        "accountIds": List["MemberAccountEc2DeepInspectionStatusStateTypeDef"],
        "failedAccountIds": List["FailedMemberAccountEc2DeepInspectionStatusStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdateMemberEc2DeepInspectionStatusRequestRequestTypeDef = TypedDict(
    "BatchUpdateMemberEc2DeepInspectionStatusRequestRequestTypeDef",
    {
        "accountIds": List["MemberAccountEc2DeepInspectionStatusTypeDef"],
    },
)

BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef = TypedDict(
    "BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef",
    {
        "accountIds": List["MemberAccountEc2DeepInspectionStatusStateTypeDef"],
        "failedAccountIds": List["FailedMemberAccountEc2DeepInspectionStatusStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelFindingsReportRequestRequestTypeDef = TypedDict(
    "CancelFindingsReportRequestRequestTypeDef",
    {
        "reportId": str,
    },
)

CancelFindingsReportResponseTypeDef = TypedDict(
    "CancelFindingsReportResponseTypeDef",
    {
        "reportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelSbomExportRequestRequestTypeDef = TypedDict(
    "CancelSbomExportRequestRequestTypeDef",
    {
        "reportId": str,
    },
)

CancelSbomExportResponseTypeDef = TypedDict(
    "CancelSbomExportResponseTypeDef",
    {
        "reportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCisCheckAggregationTypeDef = TypedDict(
    "_RequiredCisCheckAggregationTypeDef",
    {
        "scanArn": str,
    },
)
_OptionalCisCheckAggregationTypeDef = TypedDict(
    "_OptionalCisCheckAggregationTypeDef",
    {
        "accountId": str,
        "checkDescription": str,
        "checkId": str,
        "level": CisSecurityLevelType,
        "platform": str,
        "statusCounts": "StatusCountsTypeDef",
        "title": str,
    },
    total=False,
)

class CisCheckAggregationTypeDef(
    _RequiredCisCheckAggregationTypeDef, _OptionalCisCheckAggregationTypeDef
):
    pass

CisDateFilterTypeDef = TypedDict(
    "CisDateFilterTypeDef",
    {
        "earliestScanStartTime": Union[datetime, str],
        "latestScanStartTime": Union[datetime, str],
    },
    total=False,
)

CisFindingStatusFilterTypeDef = TypedDict(
    "CisFindingStatusFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "value": CisFindingStatusType,
    },
)

CisNumberFilterTypeDef = TypedDict(
    "CisNumberFilterTypeDef",
    {
        "lowerInclusive": int,
        "upperInclusive": int,
    },
    total=False,
)

CisResultStatusFilterTypeDef = TypedDict(
    "CisResultStatusFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "value": CisResultStatusType,
    },
)

_RequiredCisScanConfigurationTypeDef = TypedDict(
    "_RequiredCisScanConfigurationTypeDef",
    {
        "scanConfigurationArn": str,
    },
)
_OptionalCisScanConfigurationTypeDef = TypedDict(
    "_OptionalCisScanConfigurationTypeDef",
    {
        "ownerId": str,
        "scanName": str,
        "schedule": "ScheduleTypeDef",
        "securityLevel": CisSecurityLevelType,
        "tags": Dict[str, str],
        "targets": "CisTargetsTypeDef",
    },
    total=False,
)

class CisScanConfigurationTypeDef(
    _RequiredCisScanConfigurationTypeDef, _OptionalCisScanConfigurationTypeDef
):
    pass

CisScanResultDetailsFilterCriteriaTypeDef = TypedDict(
    "CisScanResultDetailsFilterCriteriaTypeDef",
    {
        "checkIdFilters": List["CisStringFilterTypeDef"],
        "findingArnFilters": List["CisStringFilterTypeDef"],
        "findingStatusFilters": List["CisFindingStatusFilterTypeDef"],
        "securityLevelFilters": List["CisSecurityLevelFilterTypeDef"],
        "titleFilters": List["CisStringFilterTypeDef"],
    },
    total=False,
)

_RequiredCisScanResultDetailsTypeDef = TypedDict(
    "_RequiredCisScanResultDetailsTypeDef",
    {
        "scanArn": str,
    },
)
_OptionalCisScanResultDetailsTypeDef = TypedDict(
    "_OptionalCisScanResultDetailsTypeDef",
    {
        "accountId": str,
        "checkDescription": str,
        "checkId": str,
        "findingArn": str,
        "level": CisSecurityLevelType,
        "platform": str,
        "remediation": str,
        "status": CisFindingStatusType,
        "statusReason": str,
        "targetResourceId": str,
        "title": str,
    },
    total=False,
)

class CisScanResultDetailsTypeDef(
    _RequiredCisScanResultDetailsTypeDef, _OptionalCisScanResultDetailsTypeDef
):
    pass

CisScanResultsAggregatedByChecksFilterCriteriaTypeDef = TypedDict(
    "CisScanResultsAggregatedByChecksFilterCriteriaTypeDef",
    {
        "accountIdFilters": List["CisStringFilterTypeDef"],
        "checkIdFilters": List["CisStringFilterTypeDef"],
        "failedResourcesFilters": List["CisNumberFilterTypeDef"],
        "platformFilters": List["CisStringFilterTypeDef"],
        "securityLevelFilters": List["CisSecurityLevelFilterTypeDef"],
        "titleFilters": List["CisStringFilterTypeDef"],
    },
    total=False,
)

CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef = TypedDict(
    "CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef",
    {
        "accountIdFilters": List["CisStringFilterTypeDef"],
        "checkIdFilters": List["CisStringFilterTypeDef"],
        "failedChecksFilters": List["CisNumberFilterTypeDef"],
        "platformFilters": List["CisStringFilterTypeDef"],
        "statusFilters": List["CisResultStatusFilterTypeDef"],
        "targetResourceIdFilters": List["CisStringFilterTypeDef"],
        "targetResourceTagFilters": List["TagFilterTypeDef"],
        "targetStatusFilters": List["CisTargetStatusFilterTypeDef"],
        "targetStatusReasonFilters": List["CisTargetStatusReasonFilterTypeDef"],
    },
    total=False,
)

CisScanStatusFilterTypeDef = TypedDict(
    "CisScanStatusFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "value": CisScanStatusType,
    },
)

_RequiredCisScanTypeDef = TypedDict(
    "_RequiredCisScanTypeDef",
    {
        "scanArn": str,
        "scanConfigurationArn": str,
    },
)
_OptionalCisScanTypeDef = TypedDict(
    "_OptionalCisScanTypeDef",
    {
        "failedChecks": int,
        "scanDate": datetime,
        "scanName": str,
        "scheduledBy": str,
        "securityLevel": CisSecurityLevelType,
        "status": CisScanStatusType,
        "targets": "CisTargetsTypeDef",
        "totalChecks": int,
    },
    total=False,
)

class CisScanTypeDef(_RequiredCisScanTypeDef, _OptionalCisScanTypeDef):
    pass

CisSecurityLevelFilterTypeDef = TypedDict(
    "CisSecurityLevelFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "value": CisSecurityLevelType,
    },
)

CisSessionMessageTypeDef = TypedDict(
    "CisSessionMessageTypeDef",
    {
        "cisRuleDetails": Union[bytes, IO[bytes], StreamingBody],
        "ruleId": str,
        "status": CisRuleStatusType,
    },
)

CisStringFilterTypeDef = TypedDict(
    "CisStringFilterTypeDef",
    {
        "comparison": CisStringComparisonType,
        "value": str,
    },
)

_RequiredCisTargetResourceAggregationTypeDef = TypedDict(
    "_RequiredCisTargetResourceAggregationTypeDef",
    {
        "scanArn": str,
    },
)
_OptionalCisTargetResourceAggregationTypeDef = TypedDict(
    "_OptionalCisTargetResourceAggregationTypeDef",
    {
        "accountId": str,
        "platform": str,
        "statusCounts": "StatusCountsTypeDef",
        "targetResourceId": str,
        "targetResourceTags": Dict[str, List[str]],
        "targetStatus": CisTargetStatusType,
        "targetStatusReason": CisTargetStatusReasonType,
    },
    total=False,
)

class CisTargetResourceAggregationTypeDef(
    _RequiredCisTargetResourceAggregationTypeDef, _OptionalCisTargetResourceAggregationTypeDef
):
    pass

CisTargetStatusFilterTypeDef = TypedDict(
    "CisTargetStatusFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "value": CisTargetStatusType,
    },
)

CisTargetStatusReasonFilterTypeDef = TypedDict(
    "CisTargetStatusReasonFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "value": CisTargetStatusReasonType,
    },
)

CisTargetsTypeDef = TypedDict(
    "CisTargetsTypeDef",
    {
        "accountIds": List[str],
        "targetResourceTags": Dict[str, List[str]],
    },
    total=False,
)

CisaDataTypeDef = TypedDict(
    "CisaDataTypeDef",
    {
        "action": str,
        "dateAdded": datetime,
        "dateDue": datetime,
    },
    total=False,
)

CodeFilePathTypeDef = TypedDict(
    "CodeFilePathTypeDef",
    {
        "endLine": int,
        "fileName": str,
        "filePath": str,
        "startLine": int,
    },
)

CodeLineTypeDef = TypedDict(
    "CodeLineTypeDef",
    {
        "content": str,
        "lineNumber": int,
    },
)

CodeSnippetErrorTypeDef = TypedDict(
    "CodeSnippetErrorTypeDef",
    {
        "errorCode": CodeSnippetErrorCodeType,
        "errorMessage": str,
        "findingArn": str,
    },
)

CodeSnippetResultTypeDef = TypedDict(
    "CodeSnippetResultTypeDef",
    {
        "codeSnippet": List["CodeLineTypeDef"],
        "endLine": int,
        "findingArn": str,
        "startLine": int,
        "suggestedFixes": List["SuggestedFixTypeDef"],
    },
    total=False,
)

_RequiredCodeVulnerabilityDetailsTypeDef = TypedDict(
    "_RequiredCodeVulnerabilityDetailsTypeDef",
    {
        "cwes": List[str],
        "detectorId": str,
        "detectorName": str,
        "filePath": "CodeFilePathTypeDef",
    },
)
_OptionalCodeVulnerabilityDetailsTypeDef = TypedDict(
    "_OptionalCodeVulnerabilityDetailsTypeDef",
    {
        "detectorTags": List[str],
        "referenceUrls": List[str],
        "ruleId": str,
        "sourceLambdaLayerArn": str,
    },
    total=False,
)

class CodeVulnerabilityDetailsTypeDef(
    _RequiredCodeVulnerabilityDetailsTypeDef, _OptionalCodeVulnerabilityDetailsTypeDef
):
    pass

ComputePlatformTypeDef = TypedDict(
    "ComputePlatformTypeDef",
    {
        "product": str,
        "vendor": str,
        "version": str,
    },
    total=False,
)

CountsTypeDef = TypedDict(
    "CountsTypeDef",
    {
        "count": int,
        "groupKey": GroupKeyType,
    },
    total=False,
)

CoverageDateFilterTypeDef = TypedDict(
    "CoverageDateFilterTypeDef",
    {
        "endInclusive": Union[datetime, str],
        "startInclusive": Union[datetime, str],
    },
    total=False,
)

CoverageFilterCriteriaTypeDef = TypedDict(
    "CoverageFilterCriteriaTypeDef",
    {
        "accountId": List["CoverageStringFilterTypeDef"],
        "ec2InstanceTags": List["CoverageMapFilterTypeDef"],
        "ecrImageTags": List["CoverageStringFilterTypeDef"],
        "ecrRepositoryName": List["CoverageStringFilterTypeDef"],
        "imagePulledAt": List["CoverageDateFilterTypeDef"],
        "lambdaFunctionName": List["CoverageStringFilterTypeDef"],
        "lambdaFunctionRuntime": List["CoverageStringFilterTypeDef"],
        "lambdaFunctionTags": List["CoverageMapFilterTypeDef"],
        "lastScannedAt": List["CoverageDateFilterTypeDef"],
        "resourceId": List["CoverageStringFilterTypeDef"],
        "resourceType": List["CoverageStringFilterTypeDef"],
        "scanMode": List["CoverageStringFilterTypeDef"],
        "scanStatusCode": List["CoverageStringFilterTypeDef"],
        "scanStatusReason": List["CoverageStringFilterTypeDef"],
        "scanType": List["CoverageStringFilterTypeDef"],
    },
    total=False,
)

_RequiredCoverageMapFilterTypeDef = TypedDict(
    "_RequiredCoverageMapFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "key": str,
    },
)
_OptionalCoverageMapFilterTypeDef = TypedDict(
    "_OptionalCoverageMapFilterTypeDef",
    {
        "value": str,
    },
    total=False,
)

class CoverageMapFilterTypeDef(
    _RequiredCoverageMapFilterTypeDef, _OptionalCoverageMapFilterTypeDef
):
    pass

CoverageStringFilterTypeDef = TypedDict(
    "CoverageStringFilterTypeDef",
    {
        "comparison": CoverageStringComparisonType,
        "value": str,
    },
)

_RequiredCoveredResourceTypeDef = TypedDict(
    "_RequiredCoveredResourceTypeDef",
    {
        "accountId": str,
        "resourceId": str,
        "resourceType": CoverageResourceTypeType,
        "scanType": ScanTypeType,
    },
)
_OptionalCoveredResourceTypeDef = TypedDict(
    "_OptionalCoveredResourceTypeDef",
    {
        "lastScannedAt": datetime,
        "resourceMetadata": "ResourceScanMetadataTypeDef",
        "scanMode": ScanModeType,
        "scanStatus": "ScanStatusTypeDef",
    },
    total=False,
)

class CoveredResourceTypeDef(_RequiredCoveredResourceTypeDef, _OptionalCoveredResourceTypeDef):
    pass

_RequiredCreateCisScanConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCisScanConfigurationRequestRequestTypeDef",
    {
        "scanName": str,
        "schedule": "ScheduleTypeDef",
        "securityLevel": CisSecurityLevelType,
        "targets": "CreateCisTargetsTypeDef",
    },
)
_OptionalCreateCisScanConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCisScanConfigurationRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateCisScanConfigurationRequestRequestTypeDef(
    _RequiredCreateCisScanConfigurationRequestRequestTypeDef,
    _OptionalCreateCisScanConfigurationRequestRequestTypeDef,
):
    pass

CreateCisScanConfigurationResponseTypeDef = TypedDict(
    "CreateCisScanConfigurationResponseTypeDef",
    {
        "scanConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCisTargetsTypeDef = TypedDict(
    "CreateCisTargetsTypeDef",
    {
        "accountIds": List[str],
        "targetResourceTags": Dict[str, List[str]],
    },
)

_RequiredCreateFilterRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFilterRequestRequestTypeDef",
    {
        "action": FilterActionType,
        "filterCriteria": "FilterCriteriaTypeDef",
        "name": str,
    },
)
_OptionalCreateFilterRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFilterRequestRequestTypeDef",
    {
        "description": str,
        "reason": str,
        "tags": Dict[str, str],
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
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFindingsReportRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFindingsReportRequestRequestTypeDef",
    {
        "reportFormat": ReportFormatType,
        "s3Destination": "DestinationTypeDef",
    },
)
_OptionalCreateFindingsReportRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFindingsReportRequestRequestTypeDef",
    {
        "filterCriteria": "FilterCriteriaTypeDef",
    },
    total=False,
)

class CreateFindingsReportRequestRequestTypeDef(
    _RequiredCreateFindingsReportRequestRequestTypeDef,
    _OptionalCreateFindingsReportRequestRequestTypeDef,
):
    pass

CreateFindingsReportResponseTypeDef = TypedDict(
    "CreateFindingsReportResponseTypeDef",
    {
        "reportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSbomExportRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSbomExportRequestRequestTypeDef",
    {
        "reportFormat": SbomReportFormatType,
        "s3Destination": "DestinationTypeDef",
    },
)
_OptionalCreateSbomExportRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSbomExportRequestRequestTypeDef",
    {
        "resourceFilterCriteria": "ResourceFilterCriteriaTypeDef",
    },
    total=False,
)

class CreateSbomExportRequestRequestTypeDef(
    _RequiredCreateSbomExportRequestRequestTypeDef, _OptionalCreateSbomExportRequestRequestTypeDef
):
    pass

CreateSbomExportResponseTypeDef = TypedDict(
    "CreateSbomExportResponseTypeDef",
    {
        "reportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

Cvss2TypeDef = TypedDict(
    "Cvss2TypeDef",
    {
        "baseScore": float,
        "scoringVector": str,
    },
    total=False,
)

Cvss3TypeDef = TypedDict(
    "Cvss3TypeDef",
    {
        "baseScore": float,
        "scoringVector": str,
    },
    total=False,
)

CvssScoreAdjustmentTypeDef = TypedDict(
    "CvssScoreAdjustmentTypeDef",
    {
        "metric": str,
        "reason": str,
    },
)

_RequiredCvssScoreDetailsTypeDef = TypedDict(
    "_RequiredCvssScoreDetailsTypeDef",
    {
        "score": float,
        "scoreSource": str,
        "scoringVector": str,
        "version": str,
    },
)
_OptionalCvssScoreDetailsTypeDef = TypedDict(
    "_OptionalCvssScoreDetailsTypeDef",
    {
        "adjustments": List["CvssScoreAdjustmentTypeDef"],
        "cvssSource": str,
    },
    total=False,
)

class CvssScoreDetailsTypeDef(_RequiredCvssScoreDetailsTypeDef, _OptionalCvssScoreDetailsTypeDef):
    pass

CvssScoreTypeDef = TypedDict(
    "CvssScoreTypeDef",
    {
        "baseScore": float,
        "scoringVector": str,
        "source": str,
        "version": str,
    },
)

DailyScheduleTypeDef = TypedDict(
    "DailyScheduleTypeDef",
    {
        "startTime": "TimeTypeDef",
    },
)

DateFilterTypeDef = TypedDict(
    "DateFilterTypeDef",
    {
        "endInclusive": Union[datetime, str],
        "startInclusive": Union[datetime, str],
    },
    total=False,
)

DelegatedAdminAccountTypeDef = TypedDict(
    "DelegatedAdminAccountTypeDef",
    {
        "accountId": str,
        "status": DelegatedAdminStatusType,
    },
    total=False,
)

DelegatedAdminTypeDef = TypedDict(
    "DelegatedAdminTypeDef",
    {
        "accountId": str,
        "relationshipStatus": RelationshipStatusType,
    },
    total=False,
)

DeleteCisScanConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteCisScanConfigurationRequestRequestTypeDef",
    {
        "scanConfigurationArn": str,
    },
)

DeleteCisScanConfigurationResponseTypeDef = TypedDict(
    "DeleteCisScanConfigurationResponseTypeDef",
    {
        "scanConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFilterRequestRequestTypeDef = TypedDict(
    "DeleteFilterRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteFilterResponseTypeDef = TypedDict(
    "DeleteFilterResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "autoEnable": "AutoEnableTypeDef",
        "maxAccountLimitReached": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDestinationTypeDef = TypedDict(
    "_RequiredDestinationTypeDef",
    {
        "bucketName": str,
        "kmsKeyArn": str,
    },
)
_OptionalDestinationTypeDef = TypedDict(
    "_OptionalDestinationTypeDef",
    {
        "keyPrefix": str,
    },
    total=False,
)

class DestinationTypeDef(_RequiredDestinationTypeDef, _OptionalDestinationTypeDef):
    pass

DisableDelegatedAdminAccountRequestRequestTypeDef = TypedDict(
    "DisableDelegatedAdminAccountRequestRequestTypeDef",
    {
        "delegatedAdminAccountId": str,
    },
)

DisableDelegatedAdminAccountResponseTypeDef = TypedDict(
    "DisableDelegatedAdminAccountResponseTypeDef",
    {
        "delegatedAdminAccountId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableRequestRequestTypeDef = TypedDict(
    "DisableRequestRequestTypeDef",
    {
        "accountIds": List[str],
        "resourceTypes": List[ResourceScanTypeType],
    },
    total=False,
)

DisableResponseTypeDef = TypedDict(
    "DisableResponseTypeDef",
    {
        "accounts": List["AccountTypeDef"],
        "failedAccounts": List["FailedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateMemberRequestRequestTypeDef = TypedDict(
    "DisassociateMemberRequestRequestTypeDef",
    {
        "accountId": str,
    },
)

DisassociateMemberResponseTypeDef = TypedDict(
    "DisassociateMemberResponseTypeDef",
    {
        "accountId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

Ec2ConfigurationStateTypeDef = TypedDict(
    "Ec2ConfigurationStateTypeDef",
    {
        "scanModeState": "Ec2ScanModeStateTypeDef",
    },
    total=False,
)

Ec2ConfigurationTypeDef = TypedDict(
    "Ec2ConfigurationTypeDef",
    {
        "scanMode": Ec2ScanModeType,
    },
)

_RequiredEc2InstanceAggregationResponseTypeDef = TypedDict(
    "_RequiredEc2InstanceAggregationResponseTypeDef",
    {
        "instanceId": str,
    },
)
_OptionalEc2InstanceAggregationResponseTypeDef = TypedDict(
    "_OptionalEc2InstanceAggregationResponseTypeDef",
    {
        "accountId": str,
        "ami": str,
        "instanceTags": Dict[str, str],
        "networkFindings": int,
        "operatingSystem": str,
        "severityCounts": "SeverityCountsTypeDef",
    },
    total=False,
)

class Ec2InstanceAggregationResponseTypeDef(
    _RequiredEc2InstanceAggregationResponseTypeDef, _OptionalEc2InstanceAggregationResponseTypeDef
):
    pass

Ec2InstanceAggregationTypeDef = TypedDict(
    "Ec2InstanceAggregationTypeDef",
    {
        "amis": List["StringFilterTypeDef"],
        "instanceIds": List["StringFilterTypeDef"],
        "instanceTags": List["MapFilterTypeDef"],
        "operatingSystems": List["StringFilterTypeDef"],
        "sortBy": Ec2InstanceSortByType,
        "sortOrder": SortOrderType,
    },
    total=False,
)

Ec2MetadataTypeDef = TypedDict(
    "Ec2MetadataTypeDef",
    {
        "amiId": str,
        "platform": Ec2PlatformType,
        "tags": Dict[str, str],
    },
    total=False,
)

Ec2ScanModeStateTypeDef = TypedDict(
    "Ec2ScanModeStateTypeDef",
    {
        "scanMode": Ec2ScanModeType,
        "scanModeStatus": Ec2ScanModeStatusType,
    },
    total=False,
)

EcrConfigurationStateTypeDef = TypedDict(
    "EcrConfigurationStateTypeDef",
    {
        "rescanDurationState": "EcrRescanDurationStateTypeDef",
    },
    total=False,
)

_RequiredEcrConfigurationTypeDef = TypedDict(
    "_RequiredEcrConfigurationTypeDef",
    {
        "rescanDuration": EcrRescanDurationType,
    },
)
_OptionalEcrConfigurationTypeDef = TypedDict(
    "_OptionalEcrConfigurationTypeDef",
    {
        "pullDateRescanDuration": EcrPullDateRescanDurationType,
    },
    total=False,
)

class EcrConfigurationTypeDef(_RequiredEcrConfigurationTypeDef, _OptionalEcrConfigurationTypeDef):
    pass

EcrContainerImageMetadataTypeDef = TypedDict(
    "EcrContainerImageMetadataTypeDef",
    {
        "imagePulledAt": datetime,
        "tags": List[str],
    },
    total=False,
)

EcrRepositoryMetadataTypeDef = TypedDict(
    "EcrRepositoryMetadataTypeDef",
    {
        "name": str,
        "scanFrequency": EcrScanFrequencyType,
    },
    total=False,
)

EcrRescanDurationStateTypeDef = TypedDict(
    "EcrRescanDurationStateTypeDef",
    {
        "pullDateRescanDuration": EcrPullDateRescanDurationType,
        "rescanDuration": EcrRescanDurationType,
        "status": EcrRescanDurationStatusType,
        "updatedAt": datetime,
    },
    total=False,
)

_RequiredEnableDelegatedAdminAccountRequestRequestTypeDef = TypedDict(
    "_RequiredEnableDelegatedAdminAccountRequestRequestTypeDef",
    {
        "delegatedAdminAccountId": str,
    },
)
_OptionalEnableDelegatedAdminAccountRequestRequestTypeDef = TypedDict(
    "_OptionalEnableDelegatedAdminAccountRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class EnableDelegatedAdminAccountRequestRequestTypeDef(
    _RequiredEnableDelegatedAdminAccountRequestRequestTypeDef,
    _OptionalEnableDelegatedAdminAccountRequestRequestTypeDef,
):
    pass

EnableDelegatedAdminAccountResponseTypeDef = TypedDict(
    "EnableDelegatedAdminAccountResponseTypeDef",
    {
        "delegatedAdminAccountId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnableRequestRequestTypeDef = TypedDict(
    "_RequiredEnableRequestRequestTypeDef",
    {
        "resourceTypes": List[ResourceScanTypeType],
    },
)
_OptionalEnableRequestRequestTypeDef = TypedDict(
    "_OptionalEnableRequestRequestTypeDef",
    {
        "accountIds": List[str],
        "clientToken": str,
    },
    total=False,
)

class EnableRequestRequestTypeDef(
    _RequiredEnableRequestRequestTypeDef, _OptionalEnableRequestRequestTypeDef
):
    pass

EnableResponseTypeDef = TypedDict(
    "EnableResponseTypeDef",
    {
        "accounts": List["AccountTypeDef"],
        "failedAccounts": List["FailedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EpssDetailsTypeDef = TypedDict(
    "EpssDetailsTypeDef",
    {
        "score": float,
    },
    total=False,
)

EpssTypeDef = TypedDict(
    "EpssTypeDef",
    {
        "score": float,
    },
    total=False,
)

EvidenceTypeDef = TypedDict(
    "EvidenceTypeDef",
    {
        "evidenceDetail": str,
        "evidenceRule": str,
        "severity": str,
    },
    total=False,
)

ExploitObservedTypeDef = TypedDict(
    "ExploitObservedTypeDef",
    {
        "firstSeen": datetime,
        "lastSeen": datetime,
    },
    total=False,
)

ExploitabilityDetailsTypeDef = TypedDict(
    "ExploitabilityDetailsTypeDef",
    {
        "lastKnownExploitAt": datetime,
    },
    total=False,
)

_RequiredFailedAccountTypeDef = TypedDict(
    "_RequiredFailedAccountTypeDef",
    {
        "accountId": str,
        "errorCode": ErrorCodeType,
        "errorMessage": str,
    },
)
_OptionalFailedAccountTypeDef = TypedDict(
    "_OptionalFailedAccountTypeDef",
    {
        "resourceStatus": "ResourceStatusTypeDef",
        "status": StatusType,
    },
    total=False,
)

class FailedAccountTypeDef(_RequiredFailedAccountTypeDef, _OptionalFailedAccountTypeDef):
    pass

_RequiredFailedMemberAccountEc2DeepInspectionStatusStateTypeDef = TypedDict(
    "_RequiredFailedMemberAccountEc2DeepInspectionStatusStateTypeDef",
    {
        "accountId": str,
    },
)
_OptionalFailedMemberAccountEc2DeepInspectionStatusStateTypeDef = TypedDict(
    "_OptionalFailedMemberAccountEc2DeepInspectionStatusStateTypeDef",
    {
        "ec2ScanStatus": StatusType,
        "errorMessage": str,
    },
    total=False,
)

class FailedMemberAccountEc2DeepInspectionStatusStateTypeDef(
    _RequiredFailedMemberAccountEc2DeepInspectionStatusStateTypeDef,
    _OptionalFailedMemberAccountEc2DeepInspectionStatusStateTypeDef,
):
    pass

FilterCriteriaTypeDef = TypedDict(
    "FilterCriteriaTypeDef",
    {
        "awsAccountId": List["StringFilterTypeDef"],
        "codeVulnerabilityDetectorName": List["StringFilterTypeDef"],
        "codeVulnerabilityDetectorTags": List["StringFilterTypeDef"],
        "codeVulnerabilityFilePath": List["StringFilterTypeDef"],
        "componentId": List["StringFilterTypeDef"],
        "componentType": List["StringFilterTypeDef"],
        "ec2InstanceImageId": List["StringFilterTypeDef"],
        "ec2InstanceSubnetId": List["StringFilterTypeDef"],
        "ec2InstanceVpcId": List["StringFilterTypeDef"],
        "ecrImageArchitecture": List["StringFilterTypeDef"],
        "ecrImageHash": List["StringFilterTypeDef"],
        "ecrImagePushedAt": List["DateFilterTypeDef"],
        "ecrImageRegistry": List["StringFilterTypeDef"],
        "ecrImageRepositoryName": List["StringFilterTypeDef"],
        "ecrImageTags": List["StringFilterTypeDef"],
        "epssScore": List["NumberFilterTypeDef"],
        "exploitAvailable": List["StringFilterTypeDef"],
        "findingArn": List["StringFilterTypeDef"],
        "findingStatus": List["StringFilterTypeDef"],
        "findingType": List["StringFilterTypeDef"],
        "firstObservedAt": List["DateFilterTypeDef"],
        "fixAvailable": List["StringFilterTypeDef"],
        "inspectorScore": List["NumberFilterTypeDef"],
        "lambdaFunctionExecutionRoleArn": List["StringFilterTypeDef"],
        "lambdaFunctionLastModifiedAt": List["DateFilterTypeDef"],
        "lambdaFunctionLayers": List["StringFilterTypeDef"],
        "lambdaFunctionName": List["StringFilterTypeDef"],
        "lambdaFunctionRuntime": List["StringFilterTypeDef"],
        "lastObservedAt": List["DateFilterTypeDef"],
        "networkProtocol": List["StringFilterTypeDef"],
        "portRange": List["PortRangeFilterTypeDef"],
        "relatedVulnerabilities": List["StringFilterTypeDef"],
        "resourceId": List["StringFilterTypeDef"],
        "resourceTags": List["MapFilterTypeDef"],
        "resourceType": List["StringFilterTypeDef"],
        "severity": List["StringFilterTypeDef"],
        "title": List["StringFilterTypeDef"],
        "updatedAt": List["DateFilterTypeDef"],
        "vendorSeverity": List["StringFilterTypeDef"],
        "vulnerabilityId": List["StringFilterTypeDef"],
        "vulnerabilitySource": List["StringFilterTypeDef"],
        "vulnerablePackages": List["PackageFilterTypeDef"],
    },
    total=False,
)

_RequiredFilterTypeDef = TypedDict(
    "_RequiredFilterTypeDef",
    {
        "action": FilterActionType,
        "arn": str,
        "createdAt": datetime,
        "criteria": "FilterCriteriaTypeDef",
        "name": str,
        "ownerId": str,
        "updatedAt": datetime,
    },
)
_OptionalFilterTypeDef = TypedDict(
    "_OptionalFilterTypeDef",
    {
        "description": str,
        "reason": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class FilterTypeDef(_RequiredFilterTypeDef, _OptionalFilterTypeDef):
    pass

FindingDetailTypeDef = TypedDict(
    "FindingDetailTypeDef",
    {
        "cisaData": "CisaDataTypeDef",
        "cwes": List[str],
        "epssScore": float,
        "evidences": List["EvidenceTypeDef"],
        "exploitObserved": "ExploitObservedTypeDef",
        "findingArn": str,
        "referenceUrls": List[str],
        "riskScore": int,
        "tools": List[str],
        "ttps": List[str],
    },
    total=False,
)

FindingDetailsErrorTypeDef = TypedDict(
    "FindingDetailsErrorTypeDef",
    {
        "errorCode": FindingDetailsErrorCodeType,
        "errorMessage": str,
        "findingArn": str,
    },
)

FindingTypeAggregationResponseTypeDef = TypedDict(
    "FindingTypeAggregationResponseTypeDef",
    {
        "accountId": str,
        "severityCounts": "SeverityCountsTypeDef",
    },
    total=False,
)

FindingTypeAggregationTypeDef = TypedDict(
    "FindingTypeAggregationTypeDef",
    {
        "findingType": AggregationFindingTypeType,
        "resourceType": AggregationResourceTypeType,
        "sortBy": FindingTypeSortByType,
        "sortOrder": SortOrderType,
    },
    total=False,
)

_RequiredFindingTypeDef = TypedDict(
    "_RequiredFindingTypeDef",
    {
        "awsAccountId": str,
        "description": str,
        "findingArn": str,
        "firstObservedAt": datetime,
        "lastObservedAt": datetime,
        "remediation": "RemediationTypeDef",
        "resources": List["ResourceTypeDef"],
        "severity": SeverityType,
        "status": FindingStatusType,
        "type": FindingTypeType,
    },
)
_OptionalFindingTypeDef = TypedDict(
    "_OptionalFindingTypeDef",
    {
        "codeVulnerabilityDetails": "CodeVulnerabilityDetailsTypeDef",
        "epss": "EpssDetailsTypeDef",
        "exploitAvailable": ExploitAvailableType,
        "exploitabilityDetails": "ExploitabilityDetailsTypeDef",
        "fixAvailable": FixAvailableType,
        "inspectorScore": float,
        "inspectorScoreDetails": "InspectorScoreDetailsTypeDef",
        "networkReachabilityDetails": "NetworkReachabilityDetailsTypeDef",
        "packageVulnerabilityDetails": "PackageVulnerabilityDetailsTypeDef",
        "title": str,
        "updatedAt": datetime,
    },
    total=False,
)

class FindingTypeDef(_RequiredFindingTypeDef, _OptionalFindingTypeDef):
    pass

FreeTrialAccountInfoTypeDef = TypedDict(
    "FreeTrialAccountInfoTypeDef",
    {
        "accountId": str,
        "freeTrialInfo": List["FreeTrialInfoTypeDef"],
    },
)

FreeTrialInfoErrorTypeDef = TypedDict(
    "FreeTrialInfoErrorTypeDef",
    {
        "accountId": str,
        "code": FreeTrialInfoErrorCodeType,
        "message": str,
    },
)

FreeTrialInfoTypeDef = TypedDict(
    "FreeTrialInfoTypeDef",
    {
        "end": datetime,
        "start": datetime,
        "status": FreeTrialStatusType,
        "type": FreeTrialTypeType,
    },
)

_RequiredGetCisScanReportRequestRequestTypeDef = TypedDict(
    "_RequiredGetCisScanReportRequestRequestTypeDef",
    {
        "scanArn": str,
    },
)
_OptionalGetCisScanReportRequestRequestTypeDef = TypedDict(
    "_OptionalGetCisScanReportRequestRequestTypeDef",
    {
        "reportFormat": CisReportFormatType,
        "targetAccounts": List[str],
    },
    total=False,
)

class GetCisScanReportRequestRequestTypeDef(
    _RequiredGetCisScanReportRequestRequestTypeDef, _OptionalGetCisScanReportRequestRequestTypeDef
):
    pass

GetCisScanReportResponseTypeDef = TypedDict(
    "GetCisScanReportResponseTypeDef",
    {
        "status": CisReportStatusType,
        "url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCisScanResultDetailsRequestRequestTypeDef = TypedDict(
    "_RequiredGetCisScanResultDetailsRequestRequestTypeDef",
    {
        "accountId": str,
        "scanArn": str,
        "targetResourceId": str,
    },
)
_OptionalGetCisScanResultDetailsRequestRequestTypeDef = TypedDict(
    "_OptionalGetCisScanResultDetailsRequestRequestTypeDef",
    {
        "filterCriteria": "CisScanResultDetailsFilterCriteriaTypeDef",
        "maxResults": int,
        "nextToken": str,
        "sortBy": CisScanResultDetailsSortByType,
        "sortOrder": CisSortOrderType,
    },
    total=False,
)

class GetCisScanResultDetailsRequestRequestTypeDef(
    _RequiredGetCisScanResultDetailsRequestRequestTypeDef,
    _OptionalGetCisScanResultDetailsRequestRequestTypeDef,
):
    pass

GetCisScanResultDetailsResponseTypeDef = TypedDict(
    "GetCisScanResultDetailsResponseTypeDef",
    {
        "nextToken": str,
        "scanResultDetails": List["CisScanResultDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConfigurationResponseTypeDef = TypedDict(
    "GetConfigurationResponseTypeDef",
    {
        "ec2Configuration": "Ec2ConfigurationStateTypeDef",
        "ecrConfiguration": "EcrConfigurationStateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDelegatedAdminAccountResponseTypeDef = TypedDict(
    "GetDelegatedAdminAccountResponseTypeDef",
    {
        "delegatedAdmin": "DelegatedAdminTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEc2DeepInspectionConfigurationResponseTypeDef = TypedDict(
    "GetEc2DeepInspectionConfigurationResponseTypeDef",
    {
        "errorMessage": str,
        "orgPackagePaths": List[str],
        "packagePaths": List[str],
        "status": Ec2DeepInspectionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEncryptionKeyRequestRequestTypeDef = TypedDict(
    "GetEncryptionKeyRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "scanType": ScanTypeType,
    },
)

GetEncryptionKeyResponseTypeDef = TypedDict(
    "GetEncryptionKeyResponseTypeDef",
    {
        "kmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFindingsReportStatusRequestRequestTypeDef = TypedDict(
    "GetFindingsReportStatusRequestRequestTypeDef",
    {
        "reportId": str,
    },
    total=False,
)

GetFindingsReportStatusResponseTypeDef = TypedDict(
    "GetFindingsReportStatusResponseTypeDef",
    {
        "destination": "DestinationTypeDef",
        "errorCode": ReportingErrorCodeType,
        "errorMessage": str,
        "filterCriteria": "FilterCriteriaTypeDef",
        "reportId": str,
        "status": ExternalReportStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMemberRequestRequestTypeDef = TypedDict(
    "GetMemberRequestRequestTypeDef",
    {
        "accountId": str,
    },
)

GetMemberResponseTypeDef = TypedDict(
    "GetMemberResponseTypeDef",
    {
        "member": "MemberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSbomExportRequestRequestTypeDef = TypedDict(
    "GetSbomExportRequestRequestTypeDef",
    {
        "reportId": str,
    },
)

GetSbomExportResponseTypeDef = TypedDict(
    "GetSbomExportResponseTypeDef",
    {
        "errorCode": ReportingErrorCodeType,
        "errorMessage": str,
        "filterCriteria": "ResourceFilterCriteriaTypeDef",
        "format": SbomReportFormatType,
        "reportId": str,
        "s3Destination": "DestinationTypeDef",
        "status": ExternalReportStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImageLayerAggregationResponseTypeDef = TypedDict(
    "_RequiredImageLayerAggregationResponseTypeDef",
    {
        "accountId": str,
        "layerHash": str,
        "repository": str,
        "resourceId": str,
    },
)
_OptionalImageLayerAggregationResponseTypeDef = TypedDict(
    "_OptionalImageLayerAggregationResponseTypeDef",
    {
        "severityCounts": "SeverityCountsTypeDef",
    },
    total=False,
)

class ImageLayerAggregationResponseTypeDef(
    _RequiredImageLayerAggregationResponseTypeDef, _OptionalImageLayerAggregationResponseTypeDef
):
    pass

ImageLayerAggregationTypeDef = TypedDict(
    "ImageLayerAggregationTypeDef",
    {
        "layerHashes": List["StringFilterTypeDef"],
        "repositories": List["StringFilterTypeDef"],
        "resourceIds": List["StringFilterTypeDef"],
        "sortBy": ImageLayerSortByType,
        "sortOrder": SortOrderType,
    },
    total=False,
)

InspectorScoreDetailsTypeDef = TypedDict(
    "InspectorScoreDetailsTypeDef",
    {
        "adjustedCvss": "CvssScoreDetailsTypeDef",
    },
    total=False,
)

_RequiredLambdaFunctionAggregationResponseTypeDef = TypedDict(
    "_RequiredLambdaFunctionAggregationResponseTypeDef",
    {
        "resourceId": str,
    },
)
_OptionalLambdaFunctionAggregationResponseTypeDef = TypedDict(
    "_OptionalLambdaFunctionAggregationResponseTypeDef",
    {
        "accountId": str,
        "functionName": str,
        "lambdaTags": Dict[str, str],
        "lastModifiedAt": datetime,
        "runtime": str,
        "severityCounts": "SeverityCountsTypeDef",
    },
    total=False,
)

class LambdaFunctionAggregationResponseTypeDef(
    _RequiredLambdaFunctionAggregationResponseTypeDef,
    _OptionalLambdaFunctionAggregationResponseTypeDef,
):
    pass

LambdaFunctionAggregationTypeDef = TypedDict(
    "LambdaFunctionAggregationTypeDef",
    {
        "functionNames": List["StringFilterTypeDef"],
        "functionTags": List["MapFilterTypeDef"],
        "resourceIds": List["StringFilterTypeDef"],
        "runtimes": List["StringFilterTypeDef"],
        "sortBy": LambdaFunctionSortByType,
        "sortOrder": SortOrderType,
    },
    total=False,
)

LambdaFunctionMetadataTypeDef = TypedDict(
    "LambdaFunctionMetadataTypeDef",
    {
        "functionName": str,
        "functionTags": Dict[str, str],
        "layers": List[str],
        "runtime": RuntimeType,
    },
    total=False,
)

_RequiredLambdaLayerAggregationResponseTypeDef = TypedDict(
    "_RequiredLambdaLayerAggregationResponseTypeDef",
    {
        "accountId": str,
        "functionName": str,
        "layerArn": str,
        "resourceId": str,
    },
)
_OptionalLambdaLayerAggregationResponseTypeDef = TypedDict(
    "_OptionalLambdaLayerAggregationResponseTypeDef",
    {
        "severityCounts": "SeverityCountsTypeDef",
    },
    total=False,
)

class LambdaLayerAggregationResponseTypeDef(
    _RequiredLambdaLayerAggregationResponseTypeDef, _OptionalLambdaLayerAggregationResponseTypeDef
):
    pass

LambdaLayerAggregationTypeDef = TypedDict(
    "LambdaLayerAggregationTypeDef",
    {
        "functionNames": List["StringFilterTypeDef"],
        "layerArns": List["StringFilterTypeDef"],
        "resourceIds": List["StringFilterTypeDef"],
        "sortBy": LambdaLayerSortByType,
        "sortOrder": SortOrderType,
    },
    total=False,
)

LambdaVpcConfigTypeDef = TypedDict(
    "LambdaVpcConfigTypeDef",
    {
        "securityGroupIds": List[str],
        "subnetIds": List[str],
        "vpcId": str,
    },
    total=False,
)

ListAccountPermissionsRequestRequestTypeDef = TypedDict(
    "ListAccountPermissionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "service": ServiceType,
    },
    total=False,
)

ListAccountPermissionsResponseTypeDef = TypedDict(
    "ListAccountPermissionsResponseTypeDef",
    {
        "nextToken": str,
        "permissions": List["PermissionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCisScanConfigurationsFilterCriteriaTypeDef = TypedDict(
    "ListCisScanConfigurationsFilterCriteriaTypeDef",
    {
        "scanConfigurationArnFilters": List["CisStringFilterTypeDef"],
        "scanNameFilters": List["CisStringFilterTypeDef"],
        "targetResourceTagFilters": List["TagFilterTypeDef"],
    },
    total=False,
)

ListCisScanConfigurationsRequestRequestTypeDef = TypedDict(
    "ListCisScanConfigurationsRequestRequestTypeDef",
    {
        "filterCriteria": "ListCisScanConfigurationsFilterCriteriaTypeDef",
        "maxResults": int,
        "nextToken": str,
        "sortBy": CisScanConfigurationsSortByType,
        "sortOrder": CisSortOrderType,
    },
    total=False,
)

ListCisScanConfigurationsResponseTypeDef = TypedDict(
    "ListCisScanConfigurationsResponseTypeDef",
    {
        "nextToken": str,
        "scanConfigurations": List["CisScanConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCisScanResultsAggregatedByChecksRequestRequestTypeDef = TypedDict(
    "_RequiredListCisScanResultsAggregatedByChecksRequestRequestTypeDef",
    {
        "scanArn": str,
    },
)
_OptionalListCisScanResultsAggregatedByChecksRequestRequestTypeDef = TypedDict(
    "_OptionalListCisScanResultsAggregatedByChecksRequestRequestTypeDef",
    {
        "filterCriteria": "CisScanResultsAggregatedByChecksFilterCriteriaTypeDef",
        "maxResults": int,
        "nextToken": str,
        "sortBy": CisScanResultsAggregatedByChecksSortByType,
        "sortOrder": CisSortOrderType,
    },
    total=False,
)

class ListCisScanResultsAggregatedByChecksRequestRequestTypeDef(
    _RequiredListCisScanResultsAggregatedByChecksRequestRequestTypeDef,
    _OptionalListCisScanResultsAggregatedByChecksRequestRequestTypeDef,
):
    pass

ListCisScanResultsAggregatedByChecksResponseTypeDef = TypedDict(
    "ListCisScanResultsAggregatedByChecksResponseTypeDef",
    {
        "checkAggregations": List["CisCheckAggregationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCisScanResultsAggregatedByTargetResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListCisScanResultsAggregatedByTargetResourceRequestRequestTypeDef",
    {
        "scanArn": str,
    },
)
_OptionalListCisScanResultsAggregatedByTargetResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListCisScanResultsAggregatedByTargetResourceRequestRequestTypeDef",
    {
        "filterCriteria": "CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef",
        "maxResults": int,
        "nextToken": str,
        "sortBy": CisScanResultsAggregatedByTargetResourceSortByType,
        "sortOrder": CisSortOrderType,
    },
    total=False,
)

class ListCisScanResultsAggregatedByTargetResourceRequestRequestTypeDef(
    _RequiredListCisScanResultsAggregatedByTargetResourceRequestRequestTypeDef,
    _OptionalListCisScanResultsAggregatedByTargetResourceRequestRequestTypeDef,
):
    pass

ListCisScanResultsAggregatedByTargetResourceResponseTypeDef = TypedDict(
    "ListCisScanResultsAggregatedByTargetResourceResponseTypeDef",
    {
        "nextToken": str,
        "targetResourceAggregations": List["CisTargetResourceAggregationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCisScansFilterCriteriaTypeDef = TypedDict(
    "ListCisScansFilterCriteriaTypeDef",
    {
        "failedChecksFilters": List["CisNumberFilterTypeDef"],
        "scanArnFilters": List["CisStringFilterTypeDef"],
        "scanAtFilters": List["CisDateFilterTypeDef"],
        "scanConfigurationArnFilters": List["CisStringFilterTypeDef"],
        "scanNameFilters": List["CisStringFilterTypeDef"],
        "scanStatusFilters": List["CisScanStatusFilterTypeDef"],
        "scheduledByFilters": List["CisStringFilterTypeDef"],
        "targetAccountIdFilters": List["CisStringFilterTypeDef"],
        "targetResourceIdFilters": List["CisStringFilterTypeDef"],
        "targetResourceTagFilters": List["TagFilterTypeDef"],
    },
    total=False,
)

ListCisScansRequestRequestTypeDef = TypedDict(
    "ListCisScansRequestRequestTypeDef",
    {
        "detailLevel": ListCisScansDetailLevelType,
        "filterCriteria": "ListCisScansFilterCriteriaTypeDef",
        "maxResults": int,
        "nextToken": str,
        "sortBy": ListCisScansSortByType,
        "sortOrder": CisSortOrderType,
    },
    total=False,
)

ListCisScansResponseTypeDef = TypedDict(
    "ListCisScansResponseTypeDef",
    {
        "nextToken": str,
        "scans": List["CisScanTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCoverageRequestRequestTypeDef = TypedDict(
    "ListCoverageRequestRequestTypeDef",
    {
        "filterCriteria": "CoverageFilterCriteriaTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListCoverageResponseTypeDef = TypedDict(
    "ListCoverageResponseTypeDef",
    {
        "coveredResources": List["CoveredResourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCoverageStatisticsRequestRequestTypeDef = TypedDict(
    "ListCoverageStatisticsRequestRequestTypeDef",
    {
        "filterCriteria": "CoverageFilterCriteriaTypeDef",
        "groupBy": GroupKeyType,
        "nextToken": str,
    },
    total=False,
)

ListCoverageStatisticsResponseTypeDef = TypedDict(
    "ListCoverageStatisticsResponseTypeDef",
    {
        "countsByGroup": List["CountsTypeDef"],
        "nextToken": str,
        "totalCounts": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDelegatedAdminAccountsRequestRequestTypeDef = TypedDict(
    "ListDelegatedAdminAccountsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListDelegatedAdminAccountsResponseTypeDef = TypedDict(
    "ListDelegatedAdminAccountsResponseTypeDef",
    {
        "delegatedAdminAccounts": List["DelegatedAdminAccountTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFiltersRequestRequestTypeDef = TypedDict(
    "ListFiltersRequestRequestTypeDef",
    {
        "action": FilterActionType,
        "arns": List[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListFiltersResponseTypeDef = TypedDict(
    "ListFiltersResponseTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFindingAggregationsRequestRequestTypeDef = TypedDict(
    "_RequiredListFindingAggregationsRequestRequestTypeDef",
    {
        "aggregationType": AggregationTypeType,
    },
)
_OptionalListFindingAggregationsRequestRequestTypeDef = TypedDict(
    "_OptionalListFindingAggregationsRequestRequestTypeDef",
    {
        "accountIds": List["StringFilterTypeDef"],
        "aggregationRequest": "AggregationRequestTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListFindingAggregationsRequestRequestTypeDef(
    _RequiredListFindingAggregationsRequestRequestTypeDef,
    _OptionalListFindingAggregationsRequestRequestTypeDef,
):
    pass

ListFindingAggregationsResponseTypeDef = TypedDict(
    "ListFindingAggregationsResponseTypeDef",
    {
        "aggregationType": AggregationTypeType,
        "nextToken": str,
        "responses": List["AggregationResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFindingsRequestRequestTypeDef = TypedDict(
    "ListFindingsRequestRequestTypeDef",
    {
        "filterCriteria": "FilterCriteriaTypeDef",
        "maxResults": int,
        "nextToken": str,
        "sortCriteria": "SortCriteriaTypeDef",
    },
    total=False,
)

ListFindingsResponseTypeDef = TypedDict(
    "ListFindingsResponseTypeDef",
    {
        "findings": List["FindingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMembersRequestRequestTypeDef = TypedDict(
    "ListMembersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "onlyAssociated": bool,
    },
    total=False,
)

ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef",
    {
        "members": List["MemberTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUsageTotalsRequestRequestTypeDef = TypedDict(
    "ListUsageTotalsRequestRequestTypeDef",
    {
        "accountIds": List[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListUsageTotalsResponseTypeDef = TypedDict(
    "ListUsageTotalsResponseTypeDef",
    {
        "nextToken": str,
        "totals": List["UsageTotalTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMapFilterTypeDef = TypedDict(
    "_RequiredMapFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "key": str,
    },
)
_OptionalMapFilterTypeDef = TypedDict(
    "_OptionalMapFilterTypeDef",
    {
        "value": str,
    },
    total=False,
)

class MapFilterTypeDef(_RequiredMapFilterTypeDef, _OptionalMapFilterTypeDef):
    pass

_RequiredMemberAccountEc2DeepInspectionStatusStateTypeDef = TypedDict(
    "_RequiredMemberAccountEc2DeepInspectionStatusStateTypeDef",
    {
        "accountId": str,
    },
)
_OptionalMemberAccountEc2DeepInspectionStatusStateTypeDef = TypedDict(
    "_OptionalMemberAccountEc2DeepInspectionStatusStateTypeDef",
    {
        "errorMessage": str,
        "status": Ec2DeepInspectionStatusType,
    },
    total=False,
)

class MemberAccountEc2DeepInspectionStatusStateTypeDef(
    _RequiredMemberAccountEc2DeepInspectionStatusStateTypeDef,
    _OptionalMemberAccountEc2DeepInspectionStatusStateTypeDef,
):
    pass

MemberAccountEc2DeepInspectionStatusTypeDef = TypedDict(
    "MemberAccountEc2DeepInspectionStatusTypeDef",
    {
        "accountId": str,
        "activateDeepInspection": bool,
    },
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "accountId": str,
        "delegatedAdminAccountId": str,
        "relationshipStatus": RelationshipStatusType,
        "updatedAt": datetime,
    },
    total=False,
)

MonthlyScheduleTypeDef = TypedDict(
    "MonthlyScheduleTypeDef",
    {
        "day": DayType,
        "startTime": "TimeTypeDef",
    },
)

NetworkPathTypeDef = TypedDict(
    "NetworkPathTypeDef",
    {
        "steps": List["StepTypeDef"],
    },
    total=False,
)

NetworkReachabilityDetailsTypeDef = TypedDict(
    "NetworkReachabilityDetailsTypeDef",
    {
        "networkPath": "NetworkPathTypeDef",
        "openPortRange": "PortRangeTypeDef",
        "protocol": NetworkProtocolType,
    },
)

NumberFilterTypeDef = TypedDict(
    "NumberFilterTypeDef",
    {
        "lowerInclusive": float,
        "upperInclusive": float,
    },
    total=False,
)

_RequiredPackageAggregationResponseTypeDef = TypedDict(
    "_RequiredPackageAggregationResponseTypeDef",
    {
        "packageName": str,
    },
)
_OptionalPackageAggregationResponseTypeDef = TypedDict(
    "_OptionalPackageAggregationResponseTypeDef",
    {
        "accountId": str,
        "severityCounts": "SeverityCountsTypeDef",
    },
    total=False,
)

class PackageAggregationResponseTypeDef(
    _RequiredPackageAggregationResponseTypeDef, _OptionalPackageAggregationResponseTypeDef
):
    pass

PackageAggregationTypeDef = TypedDict(
    "PackageAggregationTypeDef",
    {
        "packageNames": List["StringFilterTypeDef"],
        "sortBy": PackageSortByType,
        "sortOrder": SortOrderType,
    },
    total=False,
)

PackageFilterTypeDef = TypedDict(
    "PackageFilterTypeDef",
    {
        "architecture": "StringFilterTypeDef",
        "epoch": "NumberFilterTypeDef",
        "name": "StringFilterTypeDef",
        "release": "StringFilterTypeDef",
        "sourceLambdaLayerArn": "StringFilterTypeDef",
        "sourceLayerHash": "StringFilterTypeDef",
        "version": "StringFilterTypeDef",
    },
    total=False,
)

_RequiredPackageVulnerabilityDetailsTypeDef = TypedDict(
    "_RequiredPackageVulnerabilityDetailsTypeDef",
    {
        "source": str,
        "vulnerabilityId": str,
    },
)
_OptionalPackageVulnerabilityDetailsTypeDef = TypedDict(
    "_OptionalPackageVulnerabilityDetailsTypeDef",
    {
        "cvss": List["CvssScoreTypeDef"],
        "referenceUrls": List[str],
        "relatedVulnerabilities": List[str],
        "sourceUrl": str,
        "vendorCreatedAt": datetime,
        "vendorSeverity": str,
        "vendorUpdatedAt": datetime,
        "vulnerablePackages": List["VulnerablePackageTypeDef"],
    },
    total=False,
)

class PackageVulnerabilityDetailsTypeDef(
    _RequiredPackageVulnerabilityDetailsTypeDef, _OptionalPackageVulnerabilityDetailsTypeDef
):
    pass

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
        "operation": OperationType,
        "service": ServiceType,
    },
)

PortRangeFilterTypeDef = TypedDict(
    "PortRangeFilterTypeDef",
    {
        "beginInclusive": int,
        "endInclusive": int,
    },
    total=False,
)

PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "begin": int,
        "end": int,
    },
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "Url": str,
        "text": str,
    },
    total=False,
)

RemediationTypeDef = TypedDict(
    "RemediationTypeDef",
    {
        "recommendation": "RecommendationTypeDef",
    },
    total=False,
)

_RequiredRepositoryAggregationResponseTypeDef = TypedDict(
    "_RequiredRepositoryAggregationResponseTypeDef",
    {
        "repository": str,
    },
)
_OptionalRepositoryAggregationResponseTypeDef = TypedDict(
    "_OptionalRepositoryAggregationResponseTypeDef",
    {
        "accountId": str,
        "affectedImages": int,
        "severityCounts": "SeverityCountsTypeDef",
    },
    total=False,
)

class RepositoryAggregationResponseTypeDef(
    _RequiredRepositoryAggregationResponseTypeDef, _OptionalRepositoryAggregationResponseTypeDef
):
    pass

RepositoryAggregationTypeDef = TypedDict(
    "RepositoryAggregationTypeDef",
    {
        "repositories": List["StringFilterTypeDef"],
        "sortBy": RepositorySortByType,
        "sortOrder": SortOrderType,
    },
    total=False,
)

ResetEncryptionKeyRequestRequestTypeDef = TypedDict(
    "ResetEncryptionKeyRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "scanType": ScanTypeType,
    },
)

ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "awsEc2Instance": "AwsEc2InstanceDetailsTypeDef",
        "awsEcrContainerImage": "AwsEcrContainerImageDetailsTypeDef",
        "awsLambdaFunction": "AwsLambdaFunctionDetailsTypeDef",
    },
    total=False,
)

ResourceFilterCriteriaTypeDef = TypedDict(
    "ResourceFilterCriteriaTypeDef",
    {
        "accountId": List["ResourceStringFilterTypeDef"],
        "ec2InstanceTags": List["ResourceMapFilterTypeDef"],
        "ecrImageTags": List["ResourceStringFilterTypeDef"],
        "ecrRepositoryName": List["ResourceStringFilterTypeDef"],
        "lambdaFunctionName": List["ResourceStringFilterTypeDef"],
        "lambdaFunctionTags": List["ResourceMapFilterTypeDef"],
        "resourceId": List["ResourceStringFilterTypeDef"],
        "resourceType": List["ResourceStringFilterTypeDef"],
    },
    total=False,
)

_RequiredResourceMapFilterTypeDef = TypedDict(
    "_RequiredResourceMapFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "key": str,
    },
)
_OptionalResourceMapFilterTypeDef = TypedDict(
    "_OptionalResourceMapFilterTypeDef",
    {
        "value": str,
    },
    total=False,
)

class ResourceMapFilterTypeDef(
    _RequiredResourceMapFilterTypeDef, _OptionalResourceMapFilterTypeDef
):
    pass

ResourceScanMetadataTypeDef = TypedDict(
    "ResourceScanMetadataTypeDef",
    {
        "ec2": "Ec2MetadataTypeDef",
        "ecrImage": "EcrContainerImageMetadataTypeDef",
        "ecrRepository": "EcrRepositoryMetadataTypeDef",
        "lambdaFunction": "LambdaFunctionMetadataTypeDef",
    },
    total=False,
)

_RequiredResourceStateTypeDef = TypedDict(
    "_RequiredResourceStateTypeDef",
    {
        "ec2": "StateTypeDef",
        "ecr": "StateTypeDef",
    },
)
_OptionalResourceStateTypeDef = TypedDict(
    "_OptionalResourceStateTypeDef",
    {
        "lambda": "StateTypeDef",
        "lambdaCode": "StateTypeDef",
    },
    total=False,
)

class ResourceStateTypeDef(_RequiredResourceStateTypeDef, _OptionalResourceStateTypeDef):
    pass

_RequiredResourceStatusTypeDef = TypedDict(
    "_RequiredResourceStatusTypeDef",
    {
        "ec2": StatusType,
        "ecr": StatusType,
    },
)
_OptionalResourceStatusTypeDef = TypedDict(
    "_OptionalResourceStatusTypeDef",
    {
        "lambda": StatusType,
        "lambdaCode": StatusType,
    },
    total=False,
)

class ResourceStatusTypeDef(_RequiredResourceStatusTypeDef, _OptionalResourceStatusTypeDef):
    pass

ResourceStringFilterTypeDef = TypedDict(
    "ResourceStringFilterTypeDef",
    {
        "comparison": ResourceStringComparisonType,
        "value": str,
    },
)

_RequiredResourceTypeDef = TypedDict(
    "_RequiredResourceTypeDef",
    {
        "id": str,
        "type": ResourceTypeType,
    },
)
_OptionalResourceTypeDef = TypedDict(
    "_OptionalResourceTypeDef",
    {
        "details": "ResourceDetailsTypeDef",
        "partition": str,
        "region": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class ResourceTypeDef(_RequiredResourceTypeDef, _OptionalResourceTypeDef):
    pass

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

ScanStatusTypeDef = TypedDict(
    "ScanStatusTypeDef",
    {
        "reason": ScanStatusReasonType,
        "statusCode": ScanStatusCodeType,
    },
)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "daily": "DailyScheduleTypeDef",
        "monthly": "MonthlyScheduleTypeDef",
        "oneTime": Dict[str, Any],
        "weekly": "WeeklyScheduleTypeDef",
    },
    total=False,
)

SearchVulnerabilitiesFilterCriteriaTypeDef = TypedDict(
    "SearchVulnerabilitiesFilterCriteriaTypeDef",
    {
        "vulnerabilityIds": List[str],
    },
)

_RequiredSearchVulnerabilitiesRequestRequestTypeDef = TypedDict(
    "_RequiredSearchVulnerabilitiesRequestRequestTypeDef",
    {
        "filterCriteria": "SearchVulnerabilitiesFilterCriteriaTypeDef",
    },
)
_OptionalSearchVulnerabilitiesRequestRequestTypeDef = TypedDict(
    "_OptionalSearchVulnerabilitiesRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class SearchVulnerabilitiesRequestRequestTypeDef(
    _RequiredSearchVulnerabilitiesRequestRequestTypeDef,
    _OptionalSearchVulnerabilitiesRequestRequestTypeDef,
):
    pass

SearchVulnerabilitiesResponseTypeDef = TypedDict(
    "SearchVulnerabilitiesResponseTypeDef",
    {
        "nextToken": str,
        "vulnerabilities": List["VulnerabilityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SendCisSessionHealthRequestRequestTypeDef = TypedDict(
    "SendCisSessionHealthRequestRequestTypeDef",
    {
        "scanJobId": str,
        "sessionToken": str,
    },
)

SendCisSessionTelemetryRequestRequestTypeDef = TypedDict(
    "SendCisSessionTelemetryRequestRequestTypeDef",
    {
        "messages": List["CisSessionMessageTypeDef"],
        "scanJobId": str,
        "sessionToken": str,
    },
)

SeverityCountsTypeDef = TypedDict(
    "SeverityCountsTypeDef",
    {
        "all": int,
        "critical": int,
        "high": int,
        "medium": int,
    },
    total=False,
)

SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef",
    {
        "field": SortFieldType,
        "sortOrder": SortOrderType,
    },
)

StartCisSessionMessageTypeDef = TypedDict(
    "StartCisSessionMessageTypeDef",
    {
        "sessionToken": str,
    },
)

StartCisSessionRequestRequestTypeDef = TypedDict(
    "StartCisSessionRequestRequestTypeDef",
    {
        "message": "StartCisSessionMessageTypeDef",
        "scanJobId": str,
    },
)

StateTypeDef = TypedDict(
    "StateTypeDef",
    {
        "errorCode": ErrorCodeType,
        "errorMessage": str,
        "status": StatusType,
    },
)

StatusCountsTypeDef = TypedDict(
    "StatusCountsTypeDef",
    {
        "failed": int,
        "passed": int,
        "skipped": int,
    },
    total=False,
)

StepTypeDef = TypedDict(
    "StepTypeDef",
    {
        "componentId": str,
        "componentType": str,
    },
)

StopCisMessageProgressTypeDef = TypedDict(
    "StopCisMessageProgressTypeDef",
    {
        "errorChecks": int,
        "failedChecks": int,
        "informationalChecks": int,
        "notApplicableChecks": int,
        "notEvaluatedChecks": int,
        "successfulChecks": int,
        "totalChecks": int,
        "unknownChecks": int,
    },
    total=False,
)

_RequiredStopCisSessionMessageTypeDef = TypedDict(
    "_RequiredStopCisSessionMessageTypeDef",
    {
        "progress": "StopCisMessageProgressTypeDef",
        "status": StopCisSessionStatusType,
    },
)
_OptionalStopCisSessionMessageTypeDef = TypedDict(
    "_OptionalStopCisSessionMessageTypeDef",
    {
        "benchmarkProfile": str,
        "benchmarkVersion": str,
        "computePlatform": "ComputePlatformTypeDef",
        "reason": str,
    },
    total=False,
)

class StopCisSessionMessageTypeDef(
    _RequiredStopCisSessionMessageTypeDef, _OptionalStopCisSessionMessageTypeDef
):
    pass

StopCisSessionRequestRequestTypeDef = TypedDict(
    "StopCisSessionRequestRequestTypeDef",
    {
        "message": "StopCisSessionMessageTypeDef",
        "scanJobId": str,
        "sessionToken": str,
    },
)

StringFilterTypeDef = TypedDict(
    "StringFilterTypeDef",
    {
        "comparison": StringComparisonType,
        "value": str,
    },
)

SuggestedFixTypeDef = TypedDict(
    "SuggestedFixTypeDef",
    {
        "code": str,
        "description": str,
    },
    total=False,
)

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "key": str,
        "value": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TimeTypeDef = TypedDict(
    "TimeTypeDef",
    {
        "timeOfDay": str,
        "timezone": str,
    },
)

_RequiredTitleAggregationResponseTypeDef = TypedDict(
    "_RequiredTitleAggregationResponseTypeDef",
    {
        "title": str,
    },
)
_OptionalTitleAggregationResponseTypeDef = TypedDict(
    "_OptionalTitleAggregationResponseTypeDef",
    {
        "accountId": str,
        "severityCounts": "SeverityCountsTypeDef",
        "vulnerabilityId": str,
    },
    total=False,
)

class TitleAggregationResponseTypeDef(
    _RequiredTitleAggregationResponseTypeDef, _OptionalTitleAggregationResponseTypeDef
):
    pass

TitleAggregationTypeDef = TypedDict(
    "TitleAggregationTypeDef",
    {
        "findingType": AggregationFindingTypeType,
        "resourceType": AggregationResourceTypeType,
        "sortBy": TitleSortByType,
        "sortOrder": SortOrderType,
        "titles": List["StringFilterTypeDef"],
        "vulnerabilityIds": List["StringFilterTypeDef"],
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateCisScanConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCisScanConfigurationRequestRequestTypeDef",
    {
        "scanConfigurationArn": str,
    },
)
_OptionalUpdateCisScanConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCisScanConfigurationRequestRequestTypeDef",
    {
        "scanName": str,
        "schedule": "ScheduleTypeDef",
        "securityLevel": CisSecurityLevelType,
        "targets": "UpdateCisTargetsTypeDef",
    },
    total=False,
)

class UpdateCisScanConfigurationRequestRequestTypeDef(
    _RequiredUpdateCisScanConfigurationRequestRequestTypeDef,
    _OptionalUpdateCisScanConfigurationRequestRequestTypeDef,
):
    pass

UpdateCisScanConfigurationResponseTypeDef = TypedDict(
    "UpdateCisScanConfigurationResponseTypeDef",
    {
        "scanConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCisTargetsTypeDef = TypedDict(
    "UpdateCisTargetsTypeDef",
    {
        "accountIds": List[str],
        "targetResourceTags": Dict[str, List[str]],
    },
    total=False,
)

UpdateConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationRequestRequestTypeDef",
    {
        "ec2Configuration": "Ec2ConfigurationTypeDef",
        "ecrConfiguration": "EcrConfigurationTypeDef",
    },
    total=False,
)

UpdateEc2DeepInspectionConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateEc2DeepInspectionConfigurationRequestRequestTypeDef",
    {
        "activateDeepInspection": bool,
        "packagePaths": List[str],
    },
    total=False,
)

UpdateEc2DeepInspectionConfigurationResponseTypeDef = TypedDict(
    "UpdateEc2DeepInspectionConfigurationResponseTypeDef",
    {
        "errorMessage": str,
        "orgPackagePaths": List[str],
        "packagePaths": List[str],
        "status": Ec2DeepInspectionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEncryptionKeyRequestRequestTypeDef = TypedDict(
    "UpdateEncryptionKeyRequestRequestTypeDef",
    {
        "kmsKeyId": str,
        "resourceType": ResourceTypeType,
        "scanType": ScanTypeType,
    },
)

_RequiredUpdateFilterRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFilterRequestRequestTypeDef",
    {
        "filterArn": str,
    },
)
_OptionalUpdateFilterRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFilterRequestRequestTypeDef",
    {
        "action": FilterActionType,
        "description": str,
        "filterCriteria": "FilterCriteriaTypeDef",
        "name": str,
        "reason": str,
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
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateOrgEc2DeepInspectionConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateOrgEc2DeepInspectionConfigurationRequestRequestTypeDef",
    {
        "orgPackagePaths": List[str],
    },
)

UpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "autoEnable": "AutoEnableTypeDef",
    },
)

UpdateOrganizationConfigurationResponseTypeDef = TypedDict(
    "UpdateOrganizationConfigurationResponseTypeDef",
    {
        "autoEnable": "AutoEnableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsageTotalTypeDef = TypedDict(
    "UsageTotalTypeDef",
    {
        "accountId": str,
        "usage": List["UsageTypeDef"],
    },
    total=False,
)

UsageTypeDef = TypedDict(
    "UsageTypeDef",
    {
        "currency": Literal["USD"],
        "estimatedMonthlyCost": float,
        "total": float,
        "type": UsageTypeType,
    },
    total=False,
)

_RequiredVulnerabilityTypeDef = TypedDict(
    "_RequiredVulnerabilityTypeDef",
    {
        "id": str,
    },
)
_OptionalVulnerabilityTypeDef = TypedDict(
    "_OptionalVulnerabilityTypeDef",
    {
        "atigData": "AtigDataTypeDef",
        "cisaData": "CisaDataTypeDef",
        "cvss2": "Cvss2TypeDef",
        "cvss3": "Cvss3TypeDef",
        "cwes": List[str],
        "description": str,
        "detectionPlatforms": List[str],
        "epss": "EpssTypeDef",
        "exploitObserved": "ExploitObservedTypeDef",
        "referenceUrls": List[str],
        "relatedVulnerabilities": List[str],
        "source": Literal["NVD"],
        "sourceUrl": str,
        "vendorCreatedAt": datetime,
        "vendorSeverity": str,
        "vendorUpdatedAt": datetime,
    },
    total=False,
)

class VulnerabilityTypeDef(_RequiredVulnerabilityTypeDef, _OptionalVulnerabilityTypeDef):
    pass

_RequiredVulnerablePackageTypeDef = TypedDict(
    "_RequiredVulnerablePackageTypeDef",
    {
        "name": str,
        "version": str,
    },
)
_OptionalVulnerablePackageTypeDef = TypedDict(
    "_OptionalVulnerablePackageTypeDef",
    {
        "arch": str,
        "epoch": int,
        "filePath": str,
        "fixedInVersion": str,
        "packageManager": PackageManagerType,
        "release": str,
        "remediation": str,
        "sourceLambdaLayerArn": str,
        "sourceLayerHash": str,
    },
    total=False,
)

class VulnerablePackageTypeDef(
    _RequiredVulnerablePackageTypeDef, _OptionalVulnerablePackageTypeDef
):
    pass

WeeklyScheduleTypeDef = TypedDict(
    "WeeklyScheduleTypeDef",
    {
        "days": List[DayType],
        "startTime": "TimeTypeDef",
    },
)
