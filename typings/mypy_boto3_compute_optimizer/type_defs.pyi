"""
Type annotations for compute-optimizer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_compute_optimizer.type_defs import AccountEnrollmentStatusTypeDef

    data: AccountEnrollmentStatusTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AutoScalingConfigurationType,
    CpuVendorArchitectureType,
    CurrencyType,
    CurrentPerformanceRiskType,
    EBSFindingType,
    EBSMetricNameType,
    ECSServiceLaunchTypeType,
    ECSServiceMetricNameType,
    ECSServiceMetricStatisticType,
    ECSServiceRecommendationFilterNameType,
    ECSServiceRecommendationFindingReasonCodeType,
    ECSServiceRecommendationFindingType,
    EnhancedInfrastructureMetricsType,
    ExportableAutoScalingGroupFieldType,
    ExportableECSServiceFieldType,
    ExportableInstanceFieldType,
    ExportableLambdaFunctionFieldType,
    ExportableLicenseFieldType,
    ExportableVolumeFieldType,
    ExternalMetricsSourceType,
    ExternalMetricStatusCodeType,
    FilterNameType,
    FindingReasonCodeType,
    FindingType,
    InferredWorkloadTypesPreferenceType,
    InferredWorkloadTypeType,
    InstanceIdleType,
    InstanceRecommendationFindingReasonCodeType,
    InstanceStateType,
    JobFilterNameType,
    JobStatusType,
    LambdaFunctionMemoryMetricStatisticType,
    LambdaFunctionMetricNameType,
    LambdaFunctionMetricStatisticType,
    LambdaFunctionRecommendationFilterNameType,
    LambdaFunctionRecommendationFindingReasonCodeType,
    LambdaFunctionRecommendationFindingType,
    LicenseEditionType,
    LicenseFindingReasonCodeType,
    LicenseFindingType,
    LicenseModelType,
    LicenseRecommendationFilterNameType,
    MetricNameType,
    MetricStatisticType,
    MigrationEffortType,
    PlatformDifferenceType,
    RecommendationPreferenceNameType,
    RecommendationSourceTypeType,
    ResourceTypeType,
    ScopeNameType,
    StatusType,
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
    "AccountEnrollmentStatusTypeDef",
    "AutoScalingGroupConfigurationTypeDef",
    "AutoScalingGroupRecommendationOptionTypeDef",
    "AutoScalingGroupRecommendationTypeDef",
    "ContainerConfigurationTypeDef",
    "ContainerRecommendationTypeDef",
    "CurrentPerformanceRiskRatingsTypeDef",
    "DeleteRecommendationPreferencesRequestRequestTypeDef",
    "DescribeRecommendationExportJobsRequestRequestTypeDef",
    "DescribeRecommendationExportJobsResponseTypeDef",
    "EBSFilterTypeDef",
    "EBSUtilizationMetricTypeDef",
    "ECSServiceProjectedMetricTypeDef",
    "ECSServiceProjectedUtilizationMetricTypeDef",
    "ECSServiceRecommendationFilterTypeDef",
    "ECSServiceRecommendationOptionTypeDef",
    "ECSServiceRecommendationTypeDef",
    "ECSServiceRecommendedOptionProjectedMetricTypeDef",
    "ECSServiceUtilizationMetricTypeDef",
    "EffectiveRecommendationPreferencesTypeDef",
    "EnrollmentFilterTypeDef",
    "EstimatedMonthlySavingsTypeDef",
    "ExportAutoScalingGroupRecommendationsRequestRequestTypeDef",
    "ExportAutoScalingGroupRecommendationsResponseTypeDef",
    "ExportDestinationTypeDef",
    "ExportEBSVolumeRecommendationsRequestRequestTypeDef",
    "ExportEBSVolumeRecommendationsResponseTypeDef",
    "ExportEC2InstanceRecommendationsRequestRequestTypeDef",
    "ExportEC2InstanceRecommendationsResponseTypeDef",
    "ExportECSServiceRecommendationsRequestRequestTypeDef",
    "ExportECSServiceRecommendationsResponseTypeDef",
    "ExportLambdaFunctionRecommendationsRequestRequestTypeDef",
    "ExportLambdaFunctionRecommendationsResponseTypeDef",
    "ExportLicenseRecommendationsRequestRequestTypeDef",
    "ExportLicenseRecommendationsResponseTypeDef",
    "ExternalMetricStatusTypeDef",
    "ExternalMetricsPreferenceTypeDef",
    "FilterTypeDef",
    "GetAutoScalingGroupRecommendationsRequestRequestTypeDef",
    "GetAutoScalingGroupRecommendationsResponseTypeDef",
    "GetEBSVolumeRecommendationsRequestRequestTypeDef",
    "GetEBSVolumeRecommendationsResponseTypeDef",
    "GetEC2InstanceRecommendationsRequestRequestTypeDef",
    "GetEC2InstanceRecommendationsResponseTypeDef",
    "GetEC2RecommendationProjectedMetricsRequestRequestTypeDef",
    "GetEC2RecommendationProjectedMetricsResponseTypeDef",
    "GetECSServiceRecommendationProjectedMetricsRequestRequestTypeDef",
    "GetECSServiceRecommendationProjectedMetricsResponseTypeDef",
    "GetECSServiceRecommendationsRequestRequestTypeDef",
    "GetECSServiceRecommendationsResponseTypeDef",
    "GetEffectiveRecommendationPreferencesRequestRequestTypeDef",
    "GetEffectiveRecommendationPreferencesResponseTypeDef",
    "GetEnrollmentStatusResponseTypeDef",
    "GetEnrollmentStatusesForOrganizationRequestRequestTypeDef",
    "GetEnrollmentStatusesForOrganizationResponseTypeDef",
    "GetLambdaFunctionRecommendationsRequestRequestTypeDef",
    "GetLambdaFunctionRecommendationsResponseTypeDef",
    "GetLicenseRecommendationsRequestRequestTypeDef",
    "GetLicenseRecommendationsResponseTypeDef",
    "GetRecommendationErrorTypeDef",
    "GetRecommendationPreferencesRequestRequestTypeDef",
    "GetRecommendationPreferencesResponseTypeDef",
    "GetRecommendationSummariesRequestRequestTypeDef",
    "GetRecommendationSummariesResponseTypeDef",
    "GpuInfoTypeDef",
    "GpuTypeDef",
    "InferredWorkloadSavingTypeDef",
    "InstanceRecommendationOptionTypeDef",
    "InstanceRecommendationTypeDef",
    "JobFilterTypeDef",
    "LambdaFunctionMemoryProjectedMetricTypeDef",
    "LambdaFunctionMemoryRecommendationOptionTypeDef",
    "LambdaFunctionRecommendationFilterTypeDef",
    "LambdaFunctionRecommendationTypeDef",
    "LambdaFunctionUtilizationMetricTypeDef",
    "LicenseConfigurationTypeDef",
    "LicenseRecommendationFilterTypeDef",
    "LicenseRecommendationOptionTypeDef",
    "LicenseRecommendationTypeDef",
    "MemorySizeConfigurationTypeDef",
    "MetricSourceTypeDef",
    "PaginatorConfigTypeDef",
    "ProjectedMetricTypeDef",
    "PutRecommendationPreferencesRequestRequestTypeDef",
    "ReasonCodeSummaryTypeDef",
    "RecommendationExportJobTypeDef",
    "RecommendationPreferencesDetailTypeDef",
    "RecommendationPreferencesTypeDef",
    "RecommendationSourceTypeDef",
    "RecommendationSummaryTypeDef",
    "RecommendedOptionProjectedMetricTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationConfigTypeDef",
    "S3DestinationTypeDef",
    "SavingsOpportunityTypeDef",
    "ScopeTypeDef",
    "ServiceConfigurationTypeDef",
    "SummaryTypeDef",
    "TagTypeDef",
    "UpdateEnrollmentStatusRequestRequestTypeDef",
    "UpdateEnrollmentStatusResponseTypeDef",
    "UtilizationMetricTypeDef",
    "VolumeConfigurationTypeDef",
    "VolumeRecommendationOptionTypeDef",
    "VolumeRecommendationTypeDef",
)

AccountEnrollmentStatusTypeDef = TypedDict(
    "AccountEnrollmentStatusTypeDef",
    {
        "accountId": str,
        "status": StatusType,
        "statusReason": str,
        "lastUpdatedTimestamp": datetime,
    },
    total=False,
)

AutoScalingGroupConfigurationTypeDef = TypedDict(
    "AutoScalingGroupConfigurationTypeDef",
    {
        "desiredCapacity": int,
        "minSize": int,
        "maxSize": int,
        "instanceType": str,
    },
    total=False,
)

AutoScalingGroupRecommendationOptionTypeDef = TypedDict(
    "AutoScalingGroupRecommendationOptionTypeDef",
    {
        "configuration": "AutoScalingGroupConfigurationTypeDef",
        "projectedUtilizationMetrics": List["UtilizationMetricTypeDef"],
        "performanceRisk": float,
        "rank": int,
        "savingsOpportunity": "SavingsOpportunityTypeDef",
        "migrationEffort": MigrationEffortType,
        "instanceGpuInfo": "GpuInfoTypeDef",
    },
    total=False,
)

AutoScalingGroupRecommendationTypeDef = TypedDict(
    "AutoScalingGroupRecommendationTypeDef",
    {
        "accountId": str,
        "autoScalingGroupArn": str,
        "autoScalingGroupName": str,
        "finding": FindingType,
        "utilizationMetrics": List["UtilizationMetricTypeDef"],
        "lookBackPeriodInDays": float,
        "currentConfiguration": "AutoScalingGroupConfigurationTypeDef",
        "recommendationOptions": List["AutoScalingGroupRecommendationOptionTypeDef"],
        "lastRefreshTimestamp": datetime,
        "currentPerformanceRisk": CurrentPerformanceRiskType,
        "effectiveRecommendationPreferences": "EffectiveRecommendationPreferencesTypeDef",
        "inferredWorkloadTypes": List[InferredWorkloadTypeType],
        "currentInstanceGpuInfo": "GpuInfoTypeDef",
    },
    total=False,
)

ContainerConfigurationTypeDef = TypedDict(
    "ContainerConfigurationTypeDef",
    {
        "containerName": str,
        "memorySizeConfiguration": "MemorySizeConfigurationTypeDef",
        "cpu": int,
    },
    total=False,
)

ContainerRecommendationTypeDef = TypedDict(
    "ContainerRecommendationTypeDef",
    {
        "containerName": str,
        "memorySizeConfiguration": "MemorySizeConfigurationTypeDef",
        "cpu": int,
    },
    total=False,
)

CurrentPerformanceRiskRatingsTypeDef = TypedDict(
    "CurrentPerformanceRiskRatingsTypeDef",
    {
        "high": int,
        "medium": int,
        "low": int,
        "veryLow": int,
    },
    total=False,
)

_RequiredDeleteRecommendationPreferencesRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRecommendationPreferencesRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "recommendationPreferenceNames": List[RecommendationPreferenceNameType],
    },
)
_OptionalDeleteRecommendationPreferencesRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRecommendationPreferencesRequestRequestTypeDef",
    {
        "scope": "ScopeTypeDef",
    },
    total=False,
)

class DeleteRecommendationPreferencesRequestRequestTypeDef(
    _RequiredDeleteRecommendationPreferencesRequestRequestTypeDef,
    _OptionalDeleteRecommendationPreferencesRequestRequestTypeDef,
):
    pass

DescribeRecommendationExportJobsRequestRequestTypeDef = TypedDict(
    "DescribeRecommendationExportJobsRequestRequestTypeDef",
    {
        "jobIds": List[str],
        "filters": List["JobFilterTypeDef"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

DescribeRecommendationExportJobsResponseTypeDef = TypedDict(
    "DescribeRecommendationExportJobsResponseTypeDef",
    {
        "recommendationExportJobs": List["RecommendationExportJobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EBSFilterTypeDef = TypedDict(
    "EBSFilterTypeDef",
    {
        "name": Literal["Finding"],
        "values": List[str],
    },
    total=False,
)

EBSUtilizationMetricTypeDef = TypedDict(
    "EBSUtilizationMetricTypeDef",
    {
        "name": EBSMetricNameType,
        "statistic": MetricStatisticType,
        "value": float,
    },
    total=False,
)

ECSServiceProjectedMetricTypeDef = TypedDict(
    "ECSServiceProjectedMetricTypeDef",
    {
        "name": ECSServiceMetricNameType,
        "timestamps": List[datetime],
        "upperBoundValues": List[float],
        "lowerBoundValues": List[float],
    },
    total=False,
)

ECSServiceProjectedUtilizationMetricTypeDef = TypedDict(
    "ECSServiceProjectedUtilizationMetricTypeDef",
    {
        "name": ECSServiceMetricNameType,
        "statistic": ECSServiceMetricStatisticType,
        "lowerBoundValue": float,
        "upperBoundValue": float,
    },
    total=False,
)

ECSServiceRecommendationFilterTypeDef = TypedDict(
    "ECSServiceRecommendationFilterTypeDef",
    {
        "name": ECSServiceRecommendationFilterNameType,
        "values": List[str],
    },
    total=False,
)

ECSServiceRecommendationOptionTypeDef = TypedDict(
    "ECSServiceRecommendationOptionTypeDef",
    {
        "memory": int,
        "cpu": int,
        "savingsOpportunity": "SavingsOpportunityTypeDef",
        "projectedUtilizationMetrics": List["ECSServiceProjectedUtilizationMetricTypeDef"],
        "containerRecommendations": List["ContainerRecommendationTypeDef"],
    },
    total=False,
)

ECSServiceRecommendationTypeDef = TypedDict(
    "ECSServiceRecommendationTypeDef",
    {
        "serviceArn": str,
        "accountId": str,
        "currentServiceConfiguration": "ServiceConfigurationTypeDef",
        "utilizationMetrics": List["ECSServiceUtilizationMetricTypeDef"],
        "lookbackPeriodInDays": float,
        "launchType": ECSServiceLaunchTypeType,
        "lastRefreshTimestamp": datetime,
        "finding": ECSServiceRecommendationFindingType,
        "findingReasonCodes": List[ECSServiceRecommendationFindingReasonCodeType],
        "serviceRecommendationOptions": List["ECSServiceRecommendationOptionTypeDef"],
        "currentPerformanceRisk": CurrentPerformanceRiskType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

ECSServiceRecommendedOptionProjectedMetricTypeDef = TypedDict(
    "ECSServiceRecommendedOptionProjectedMetricTypeDef",
    {
        "recommendedCpuUnits": int,
        "recommendedMemorySize": int,
        "projectedMetrics": List["ECSServiceProjectedMetricTypeDef"],
    },
    total=False,
)

ECSServiceUtilizationMetricTypeDef = TypedDict(
    "ECSServiceUtilizationMetricTypeDef",
    {
        "name": ECSServiceMetricNameType,
        "statistic": ECSServiceMetricStatisticType,
        "value": float,
    },
    total=False,
)

EffectiveRecommendationPreferencesTypeDef = TypedDict(
    "EffectiveRecommendationPreferencesTypeDef",
    {
        "cpuVendorArchitectures": List[CpuVendorArchitectureType],
        "enhancedInfrastructureMetrics": EnhancedInfrastructureMetricsType,
        "inferredWorkloadTypes": InferredWorkloadTypesPreferenceType,
        "externalMetricsPreference": "ExternalMetricsPreferenceTypeDef",
    },
    total=False,
)

EnrollmentFilterTypeDef = TypedDict(
    "EnrollmentFilterTypeDef",
    {
        "name": Literal["Status"],
        "values": List[str],
    },
    total=False,
)

EstimatedMonthlySavingsTypeDef = TypedDict(
    "EstimatedMonthlySavingsTypeDef",
    {
        "currency": CurrencyType,
        "value": float,
    },
    total=False,
)

_RequiredExportAutoScalingGroupRecommendationsRequestRequestTypeDef = TypedDict(
    "_RequiredExportAutoScalingGroupRecommendationsRequestRequestTypeDef",
    {
        "s3DestinationConfig": "S3DestinationConfigTypeDef",
    },
)
_OptionalExportAutoScalingGroupRecommendationsRequestRequestTypeDef = TypedDict(
    "_OptionalExportAutoScalingGroupRecommendationsRequestRequestTypeDef",
    {
        "accountIds": List[str],
        "filters": List["FilterTypeDef"],
        "fieldsToExport": List[ExportableAutoScalingGroupFieldType],
        "fileFormat": Literal["Csv"],
        "includeMemberAccounts": bool,
        "recommendationPreferences": "RecommendationPreferencesTypeDef",
    },
    total=False,
)

class ExportAutoScalingGroupRecommendationsRequestRequestTypeDef(
    _RequiredExportAutoScalingGroupRecommendationsRequestRequestTypeDef,
    _OptionalExportAutoScalingGroupRecommendationsRequestRequestTypeDef,
):
    pass

ExportAutoScalingGroupRecommendationsResponseTypeDef = TypedDict(
    "ExportAutoScalingGroupRecommendationsResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": "S3DestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportDestinationTypeDef = TypedDict(
    "ExportDestinationTypeDef",
    {
        "s3": "S3DestinationTypeDef",
    },
    total=False,
)

_RequiredExportEBSVolumeRecommendationsRequestRequestTypeDef = TypedDict(
    "_RequiredExportEBSVolumeRecommendationsRequestRequestTypeDef",
    {
        "s3DestinationConfig": "S3DestinationConfigTypeDef",
    },
)
_OptionalExportEBSVolumeRecommendationsRequestRequestTypeDef = TypedDict(
    "_OptionalExportEBSVolumeRecommendationsRequestRequestTypeDef",
    {
        "accountIds": List[str],
        "filters": List["EBSFilterTypeDef"],
        "fieldsToExport": List[ExportableVolumeFieldType],
        "fileFormat": Literal["Csv"],
        "includeMemberAccounts": bool,
    },
    total=False,
)

class ExportEBSVolumeRecommendationsRequestRequestTypeDef(
    _RequiredExportEBSVolumeRecommendationsRequestRequestTypeDef,
    _OptionalExportEBSVolumeRecommendationsRequestRequestTypeDef,
):
    pass

ExportEBSVolumeRecommendationsResponseTypeDef = TypedDict(
    "ExportEBSVolumeRecommendationsResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": "S3DestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportEC2InstanceRecommendationsRequestRequestTypeDef = TypedDict(
    "_RequiredExportEC2InstanceRecommendationsRequestRequestTypeDef",
    {
        "s3DestinationConfig": "S3DestinationConfigTypeDef",
    },
)
_OptionalExportEC2InstanceRecommendationsRequestRequestTypeDef = TypedDict(
    "_OptionalExportEC2InstanceRecommendationsRequestRequestTypeDef",
    {
        "accountIds": List[str],
        "filters": List["FilterTypeDef"],
        "fieldsToExport": List[ExportableInstanceFieldType],
        "fileFormat": Literal["Csv"],
        "includeMemberAccounts": bool,
        "recommendationPreferences": "RecommendationPreferencesTypeDef",
    },
    total=False,
)

class ExportEC2InstanceRecommendationsRequestRequestTypeDef(
    _RequiredExportEC2InstanceRecommendationsRequestRequestTypeDef,
    _OptionalExportEC2InstanceRecommendationsRequestRequestTypeDef,
):
    pass

ExportEC2InstanceRecommendationsResponseTypeDef = TypedDict(
    "ExportEC2InstanceRecommendationsResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": "S3DestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportECSServiceRecommendationsRequestRequestTypeDef = TypedDict(
    "_RequiredExportECSServiceRecommendationsRequestRequestTypeDef",
    {
        "s3DestinationConfig": "S3DestinationConfigTypeDef",
    },
)
_OptionalExportECSServiceRecommendationsRequestRequestTypeDef = TypedDict(
    "_OptionalExportECSServiceRecommendationsRequestRequestTypeDef",
    {
        "accountIds": List[str],
        "filters": List["ECSServiceRecommendationFilterTypeDef"],
        "fieldsToExport": List[ExportableECSServiceFieldType],
        "fileFormat": Literal["Csv"],
        "includeMemberAccounts": bool,
    },
    total=False,
)

class ExportECSServiceRecommendationsRequestRequestTypeDef(
    _RequiredExportECSServiceRecommendationsRequestRequestTypeDef,
    _OptionalExportECSServiceRecommendationsRequestRequestTypeDef,
):
    pass

ExportECSServiceRecommendationsResponseTypeDef = TypedDict(
    "ExportECSServiceRecommendationsResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": "S3DestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportLambdaFunctionRecommendationsRequestRequestTypeDef = TypedDict(
    "_RequiredExportLambdaFunctionRecommendationsRequestRequestTypeDef",
    {
        "s3DestinationConfig": "S3DestinationConfigTypeDef",
    },
)
_OptionalExportLambdaFunctionRecommendationsRequestRequestTypeDef = TypedDict(
    "_OptionalExportLambdaFunctionRecommendationsRequestRequestTypeDef",
    {
        "accountIds": List[str],
        "filters": List["LambdaFunctionRecommendationFilterTypeDef"],
        "fieldsToExport": List[ExportableLambdaFunctionFieldType],
        "fileFormat": Literal["Csv"],
        "includeMemberAccounts": bool,
    },
    total=False,
)

class ExportLambdaFunctionRecommendationsRequestRequestTypeDef(
    _RequiredExportLambdaFunctionRecommendationsRequestRequestTypeDef,
    _OptionalExportLambdaFunctionRecommendationsRequestRequestTypeDef,
):
    pass

ExportLambdaFunctionRecommendationsResponseTypeDef = TypedDict(
    "ExportLambdaFunctionRecommendationsResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": "S3DestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportLicenseRecommendationsRequestRequestTypeDef = TypedDict(
    "_RequiredExportLicenseRecommendationsRequestRequestTypeDef",
    {
        "s3DestinationConfig": "S3DestinationConfigTypeDef",
    },
)
_OptionalExportLicenseRecommendationsRequestRequestTypeDef = TypedDict(
    "_OptionalExportLicenseRecommendationsRequestRequestTypeDef",
    {
        "accountIds": List[str],
        "filters": List["LicenseRecommendationFilterTypeDef"],
        "fieldsToExport": List[ExportableLicenseFieldType],
        "fileFormat": Literal["Csv"],
        "includeMemberAccounts": bool,
    },
    total=False,
)

class ExportLicenseRecommendationsRequestRequestTypeDef(
    _RequiredExportLicenseRecommendationsRequestRequestTypeDef,
    _OptionalExportLicenseRecommendationsRequestRequestTypeDef,
):
    pass

ExportLicenseRecommendationsResponseTypeDef = TypedDict(
    "ExportLicenseRecommendationsResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": "S3DestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExternalMetricStatusTypeDef = TypedDict(
    "ExternalMetricStatusTypeDef",
    {
        "statusCode": ExternalMetricStatusCodeType,
        "statusReason": str,
    },
    total=False,
)

ExternalMetricsPreferenceTypeDef = TypedDict(
    "ExternalMetricsPreferenceTypeDef",
    {
        "source": ExternalMetricsSourceType,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": FilterNameType,
        "values": List[str],
    },
    total=False,
)

GetAutoScalingGroupRecommendationsRequestRequestTypeDef = TypedDict(
    "GetAutoScalingGroupRecommendationsRequestRequestTypeDef",
    {
        "accountIds": List[str],
        "autoScalingGroupArns": List[str],
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
        "recommendationPreferences": "RecommendationPreferencesTypeDef",
    },
    total=False,
)

GetAutoScalingGroupRecommendationsResponseTypeDef = TypedDict(
    "GetAutoScalingGroupRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "autoScalingGroupRecommendations": List["AutoScalingGroupRecommendationTypeDef"],
        "errors": List["GetRecommendationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEBSVolumeRecommendationsRequestRequestTypeDef = TypedDict(
    "GetEBSVolumeRecommendationsRequestRequestTypeDef",
    {
        "volumeArns": List[str],
        "nextToken": str,
        "maxResults": int,
        "filters": List["EBSFilterTypeDef"],
        "accountIds": List[str],
    },
    total=False,
)

GetEBSVolumeRecommendationsResponseTypeDef = TypedDict(
    "GetEBSVolumeRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "volumeRecommendations": List["VolumeRecommendationTypeDef"],
        "errors": List["GetRecommendationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEC2InstanceRecommendationsRequestRequestTypeDef = TypedDict(
    "GetEC2InstanceRecommendationsRequestRequestTypeDef",
    {
        "instanceArns": List[str],
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
        "accountIds": List[str],
        "recommendationPreferences": "RecommendationPreferencesTypeDef",
    },
    total=False,
)

GetEC2InstanceRecommendationsResponseTypeDef = TypedDict(
    "GetEC2InstanceRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "instanceRecommendations": List["InstanceRecommendationTypeDef"],
        "errors": List["GetRecommendationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetEC2RecommendationProjectedMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredGetEC2RecommendationProjectedMetricsRequestRequestTypeDef",
    {
        "instanceArn": str,
        "stat": MetricStatisticType,
        "period": int,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalGetEC2RecommendationProjectedMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalGetEC2RecommendationProjectedMetricsRequestRequestTypeDef",
    {
        "recommendationPreferences": "RecommendationPreferencesTypeDef",
    },
    total=False,
)

class GetEC2RecommendationProjectedMetricsRequestRequestTypeDef(
    _RequiredGetEC2RecommendationProjectedMetricsRequestRequestTypeDef,
    _OptionalGetEC2RecommendationProjectedMetricsRequestRequestTypeDef,
):
    pass

GetEC2RecommendationProjectedMetricsResponseTypeDef = TypedDict(
    "GetEC2RecommendationProjectedMetricsResponseTypeDef",
    {
        "recommendedOptionProjectedMetrics": List["RecommendedOptionProjectedMetricTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetECSServiceRecommendationProjectedMetricsRequestRequestTypeDef = TypedDict(
    "GetECSServiceRecommendationProjectedMetricsRequestRequestTypeDef",
    {
        "serviceArn": str,
        "stat": MetricStatisticType,
        "period": int,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)

GetECSServiceRecommendationProjectedMetricsResponseTypeDef = TypedDict(
    "GetECSServiceRecommendationProjectedMetricsResponseTypeDef",
    {
        "recommendedOptionProjectedMetrics": List[
            "ECSServiceRecommendedOptionProjectedMetricTypeDef"
        ],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetECSServiceRecommendationsRequestRequestTypeDef = TypedDict(
    "GetECSServiceRecommendationsRequestRequestTypeDef",
    {
        "serviceArns": List[str],
        "nextToken": str,
        "maxResults": int,
        "filters": List["ECSServiceRecommendationFilterTypeDef"],
        "accountIds": List[str],
    },
    total=False,
)

GetECSServiceRecommendationsResponseTypeDef = TypedDict(
    "GetECSServiceRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "ecsServiceRecommendations": List["ECSServiceRecommendationTypeDef"],
        "errors": List["GetRecommendationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEffectiveRecommendationPreferencesRequestRequestTypeDef = TypedDict(
    "GetEffectiveRecommendationPreferencesRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

GetEffectiveRecommendationPreferencesResponseTypeDef = TypedDict(
    "GetEffectiveRecommendationPreferencesResponseTypeDef",
    {
        "enhancedInfrastructureMetrics": EnhancedInfrastructureMetricsType,
        "externalMetricsPreference": "ExternalMetricsPreferenceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnrollmentStatusResponseTypeDef = TypedDict(
    "GetEnrollmentStatusResponseTypeDef",
    {
        "status": StatusType,
        "statusReason": str,
        "memberAccountsEnrolled": bool,
        "lastUpdatedTimestamp": datetime,
        "numberOfMemberAccountsOptedIn": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnrollmentStatusesForOrganizationRequestRequestTypeDef = TypedDict(
    "GetEnrollmentStatusesForOrganizationRequestRequestTypeDef",
    {
        "filters": List["EnrollmentFilterTypeDef"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetEnrollmentStatusesForOrganizationResponseTypeDef = TypedDict(
    "GetEnrollmentStatusesForOrganizationResponseTypeDef",
    {
        "accountEnrollmentStatuses": List["AccountEnrollmentStatusTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLambdaFunctionRecommendationsRequestRequestTypeDef = TypedDict(
    "GetLambdaFunctionRecommendationsRequestRequestTypeDef",
    {
        "functionArns": List[str],
        "accountIds": List[str],
        "filters": List["LambdaFunctionRecommendationFilterTypeDef"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetLambdaFunctionRecommendationsResponseTypeDef = TypedDict(
    "GetLambdaFunctionRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "lambdaFunctionRecommendations": List["LambdaFunctionRecommendationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLicenseRecommendationsRequestRequestTypeDef = TypedDict(
    "GetLicenseRecommendationsRequestRequestTypeDef",
    {
        "resourceArns": List[str],
        "nextToken": str,
        "maxResults": int,
        "filters": List["LicenseRecommendationFilterTypeDef"],
        "accountIds": List[str],
    },
    total=False,
)

GetLicenseRecommendationsResponseTypeDef = TypedDict(
    "GetLicenseRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "licenseRecommendations": List["LicenseRecommendationTypeDef"],
        "errors": List["GetRecommendationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommendationErrorTypeDef = TypedDict(
    "GetRecommendationErrorTypeDef",
    {
        "identifier": str,
        "code": str,
        "message": str,
    },
    total=False,
)

_RequiredGetRecommendationPreferencesRequestRequestTypeDef = TypedDict(
    "_RequiredGetRecommendationPreferencesRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
    },
)
_OptionalGetRecommendationPreferencesRequestRequestTypeDef = TypedDict(
    "_OptionalGetRecommendationPreferencesRequestRequestTypeDef",
    {
        "scope": "ScopeTypeDef",
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetRecommendationPreferencesRequestRequestTypeDef(
    _RequiredGetRecommendationPreferencesRequestRequestTypeDef,
    _OptionalGetRecommendationPreferencesRequestRequestTypeDef,
):
    pass

GetRecommendationPreferencesResponseTypeDef = TypedDict(
    "GetRecommendationPreferencesResponseTypeDef",
    {
        "nextToken": str,
        "recommendationPreferencesDetails": List["RecommendationPreferencesDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommendationSummariesRequestRequestTypeDef = TypedDict(
    "GetRecommendationSummariesRequestRequestTypeDef",
    {
        "accountIds": List[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetRecommendationSummariesResponseTypeDef = TypedDict(
    "GetRecommendationSummariesResponseTypeDef",
    {
        "nextToken": str,
        "recommendationSummaries": List["RecommendationSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GpuInfoTypeDef = TypedDict(
    "GpuInfoTypeDef",
    {
        "gpus": List["GpuTypeDef"],
    },
    total=False,
)

GpuTypeDef = TypedDict(
    "GpuTypeDef",
    {
        "gpuCount": int,
        "gpuMemorySizeInMiB": int,
    },
    total=False,
)

InferredWorkloadSavingTypeDef = TypedDict(
    "InferredWorkloadSavingTypeDef",
    {
        "inferredWorkloadTypes": List[InferredWorkloadTypeType],
        "estimatedMonthlySavings": "EstimatedMonthlySavingsTypeDef",
    },
    total=False,
)

InstanceRecommendationOptionTypeDef = TypedDict(
    "InstanceRecommendationOptionTypeDef",
    {
        "instanceType": str,
        "projectedUtilizationMetrics": List["UtilizationMetricTypeDef"],
        "platformDifferences": List[PlatformDifferenceType],
        "performanceRisk": float,
        "rank": int,
        "savingsOpportunity": "SavingsOpportunityTypeDef",
        "migrationEffort": MigrationEffortType,
        "instanceGpuInfo": "GpuInfoTypeDef",
    },
    total=False,
)

InstanceRecommendationTypeDef = TypedDict(
    "InstanceRecommendationTypeDef",
    {
        "instanceArn": str,
        "accountId": str,
        "instanceName": str,
        "currentInstanceType": str,
        "finding": FindingType,
        "findingReasonCodes": List[InstanceRecommendationFindingReasonCodeType],
        "utilizationMetrics": List["UtilizationMetricTypeDef"],
        "lookBackPeriodInDays": float,
        "recommendationOptions": List["InstanceRecommendationOptionTypeDef"],
        "recommendationSources": List["RecommendationSourceTypeDef"],
        "lastRefreshTimestamp": datetime,
        "currentPerformanceRisk": CurrentPerformanceRiskType,
        "effectiveRecommendationPreferences": "EffectiveRecommendationPreferencesTypeDef",
        "inferredWorkloadTypes": List[InferredWorkloadTypeType],
        "instanceState": InstanceStateType,
        "tags": List["TagTypeDef"],
        "externalMetricStatus": "ExternalMetricStatusTypeDef",
        "currentInstanceGpuInfo": "GpuInfoTypeDef",
        "idle": InstanceIdleType,
    },
    total=False,
)

JobFilterTypeDef = TypedDict(
    "JobFilterTypeDef",
    {
        "name": JobFilterNameType,
        "values": List[str],
    },
    total=False,
)

LambdaFunctionMemoryProjectedMetricTypeDef = TypedDict(
    "LambdaFunctionMemoryProjectedMetricTypeDef",
    {
        "name": Literal["Duration"],
        "statistic": LambdaFunctionMemoryMetricStatisticType,
        "value": float,
    },
    total=False,
)

LambdaFunctionMemoryRecommendationOptionTypeDef = TypedDict(
    "LambdaFunctionMemoryRecommendationOptionTypeDef",
    {
        "rank": int,
        "memorySize": int,
        "projectedUtilizationMetrics": List["LambdaFunctionMemoryProjectedMetricTypeDef"],
        "savingsOpportunity": "SavingsOpportunityTypeDef",
    },
    total=False,
)

LambdaFunctionRecommendationFilterTypeDef = TypedDict(
    "LambdaFunctionRecommendationFilterTypeDef",
    {
        "name": LambdaFunctionRecommendationFilterNameType,
        "values": List[str],
    },
    total=False,
)

LambdaFunctionRecommendationTypeDef = TypedDict(
    "LambdaFunctionRecommendationTypeDef",
    {
        "functionArn": str,
        "functionVersion": str,
        "accountId": str,
        "currentMemorySize": int,
        "numberOfInvocations": int,
        "utilizationMetrics": List["LambdaFunctionUtilizationMetricTypeDef"],
        "lookbackPeriodInDays": float,
        "lastRefreshTimestamp": datetime,
        "finding": LambdaFunctionRecommendationFindingType,
        "findingReasonCodes": List[LambdaFunctionRecommendationFindingReasonCodeType],
        "memorySizeRecommendationOptions": List["LambdaFunctionMemoryRecommendationOptionTypeDef"],
        "currentPerformanceRisk": CurrentPerformanceRiskType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

LambdaFunctionUtilizationMetricTypeDef = TypedDict(
    "LambdaFunctionUtilizationMetricTypeDef",
    {
        "name": LambdaFunctionMetricNameType,
        "statistic": LambdaFunctionMetricStatisticType,
        "value": float,
    },
    total=False,
)

LicenseConfigurationTypeDef = TypedDict(
    "LicenseConfigurationTypeDef",
    {
        "numberOfCores": int,
        "instanceType": str,
        "operatingSystem": str,
        "licenseEdition": LicenseEditionType,
        "licenseName": Literal["SQLServer"],
        "licenseModel": LicenseModelType,
        "licenseVersion": str,
        "metricsSource": List["MetricSourceTypeDef"],
    },
    total=False,
)

LicenseRecommendationFilterTypeDef = TypedDict(
    "LicenseRecommendationFilterTypeDef",
    {
        "name": LicenseRecommendationFilterNameType,
        "values": List[str],
    },
    total=False,
)

LicenseRecommendationOptionTypeDef = TypedDict(
    "LicenseRecommendationOptionTypeDef",
    {
        "rank": int,
        "operatingSystem": str,
        "licenseEdition": LicenseEditionType,
        "licenseModel": LicenseModelType,
        "savingsOpportunity": "SavingsOpportunityTypeDef",
    },
    total=False,
)

LicenseRecommendationTypeDef = TypedDict(
    "LicenseRecommendationTypeDef",
    {
        "resourceArn": str,
        "accountId": str,
        "currentLicenseConfiguration": "LicenseConfigurationTypeDef",
        "lookbackPeriodInDays": float,
        "lastRefreshTimestamp": datetime,
        "finding": LicenseFindingType,
        "findingReasonCodes": List[LicenseFindingReasonCodeType],
        "licenseRecommendationOptions": List["LicenseRecommendationOptionTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

MemorySizeConfigurationTypeDef = TypedDict(
    "MemorySizeConfigurationTypeDef",
    {
        "memory": int,
        "memoryReservation": int,
    },
    total=False,
)

MetricSourceTypeDef = TypedDict(
    "MetricSourceTypeDef",
    {
        "provider": Literal["CloudWatchApplicationInsights"],
        "providerArn": str,
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

ProjectedMetricTypeDef = TypedDict(
    "ProjectedMetricTypeDef",
    {
        "name": MetricNameType,
        "timestamps": List[datetime],
        "values": List[float],
    },
    total=False,
)

_RequiredPutRecommendationPreferencesRequestRequestTypeDef = TypedDict(
    "_RequiredPutRecommendationPreferencesRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
    },
)
_OptionalPutRecommendationPreferencesRequestRequestTypeDef = TypedDict(
    "_OptionalPutRecommendationPreferencesRequestRequestTypeDef",
    {
        "scope": "ScopeTypeDef",
        "enhancedInfrastructureMetrics": EnhancedInfrastructureMetricsType,
        "inferredWorkloadTypes": InferredWorkloadTypesPreferenceType,
        "externalMetricsPreference": "ExternalMetricsPreferenceTypeDef",
    },
    total=False,
)

class PutRecommendationPreferencesRequestRequestTypeDef(
    _RequiredPutRecommendationPreferencesRequestRequestTypeDef,
    _OptionalPutRecommendationPreferencesRequestRequestTypeDef,
):
    pass

ReasonCodeSummaryTypeDef = TypedDict(
    "ReasonCodeSummaryTypeDef",
    {
        "name": FindingReasonCodeType,
        "value": float,
    },
    total=False,
)

RecommendationExportJobTypeDef = TypedDict(
    "RecommendationExportJobTypeDef",
    {
        "jobId": str,
        "destination": "ExportDestinationTypeDef",
        "resourceType": ResourceTypeType,
        "status": JobStatusType,
        "creationTimestamp": datetime,
        "lastUpdatedTimestamp": datetime,
        "failureReason": str,
    },
    total=False,
)

RecommendationPreferencesDetailTypeDef = TypedDict(
    "RecommendationPreferencesDetailTypeDef",
    {
        "scope": "ScopeTypeDef",
        "resourceType": ResourceTypeType,
        "enhancedInfrastructureMetrics": EnhancedInfrastructureMetricsType,
        "inferredWorkloadTypes": InferredWorkloadTypesPreferenceType,
        "externalMetricsPreference": "ExternalMetricsPreferenceTypeDef",
    },
    total=False,
)

RecommendationPreferencesTypeDef = TypedDict(
    "RecommendationPreferencesTypeDef",
    {
        "cpuVendorArchitectures": List[CpuVendorArchitectureType],
    },
    total=False,
)

RecommendationSourceTypeDef = TypedDict(
    "RecommendationSourceTypeDef",
    {
        "recommendationSourceArn": str,
        "recommendationSourceType": RecommendationSourceTypeType,
    },
    total=False,
)

RecommendationSummaryTypeDef = TypedDict(
    "RecommendationSummaryTypeDef",
    {
        "summaries": List["SummaryTypeDef"],
        "recommendationResourceType": RecommendationSourceTypeType,
        "accountId": str,
        "savingsOpportunity": "SavingsOpportunityTypeDef",
        "currentPerformanceRiskRatings": "CurrentPerformanceRiskRatingsTypeDef",
        "inferredWorkloadSavings": List["InferredWorkloadSavingTypeDef"],
    },
    total=False,
)

RecommendedOptionProjectedMetricTypeDef = TypedDict(
    "RecommendedOptionProjectedMetricTypeDef",
    {
        "recommendedInstanceType": str,
        "rank": int,
        "projectedMetrics": List["ProjectedMetricTypeDef"],
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

S3DestinationConfigTypeDef = TypedDict(
    "S3DestinationConfigTypeDef",
    {
        "bucket": str,
        "keyPrefix": str,
    },
    total=False,
)

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "bucket": str,
        "key": str,
        "metadataKey": str,
    },
    total=False,
)

SavingsOpportunityTypeDef = TypedDict(
    "SavingsOpportunityTypeDef",
    {
        "savingsOpportunityPercentage": float,
        "estimatedMonthlySavings": "EstimatedMonthlySavingsTypeDef",
    },
    total=False,
)

ScopeTypeDef = TypedDict(
    "ScopeTypeDef",
    {
        "name": ScopeNameType,
        "value": str,
    },
    total=False,
)

ServiceConfigurationTypeDef = TypedDict(
    "ServiceConfigurationTypeDef",
    {
        "memory": int,
        "cpu": int,
        "containerConfigurations": List["ContainerConfigurationTypeDef"],
        "autoScalingConfiguration": AutoScalingConfigurationType,
        "taskDefinitionArn": str,
    },
    total=False,
)

SummaryTypeDef = TypedDict(
    "SummaryTypeDef",
    {
        "name": FindingType,
        "value": float,
        "reasonCodeSummaries": List["ReasonCodeSummaryTypeDef"],
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

_RequiredUpdateEnrollmentStatusRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEnrollmentStatusRequestRequestTypeDef",
    {
        "status": StatusType,
    },
)
_OptionalUpdateEnrollmentStatusRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEnrollmentStatusRequestRequestTypeDef",
    {
        "includeMemberAccounts": bool,
    },
    total=False,
)

class UpdateEnrollmentStatusRequestRequestTypeDef(
    _RequiredUpdateEnrollmentStatusRequestRequestTypeDef,
    _OptionalUpdateEnrollmentStatusRequestRequestTypeDef,
):
    pass

UpdateEnrollmentStatusResponseTypeDef = TypedDict(
    "UpdateEnrollmentStatusResponseTypeDef",
    {
        "status": StatusType,
        "statusReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UtilizationMetricTypeDef = TypedDict(
    "UtilizationMetricTypeDef",
    {
        "name": MetricNameType,
        "statistic": MetricStatisticType,
        "value": float,
    },
    total=False,
)

VolumeConfigurationTypeDef = TypedDict(
    "VolumeConfigurationTypeDef",
    {
        "volumeType": str,
        "volumeSize": int,
        "volumeBaselineIOPS": int,
        "volumeBurstIOPS": int,
        "volumeBaselineThroughput": int,
        "volumeBurstThroughput": int,
        "rootVolume": bool,
    },
    total=False,
)

VolumeRecommendationOptionTypeDef = TypedDict(
    "VolumeRecommendationOptionTypeDef",
    {
        "configuration": "VolumeConfigurationTypeDef",
        "performanceRisk": float,
        "rank": int,
        "savingsOpportunity": "SavingsOpportunityTypeDef",
    },
    total=False,
)

VolumeRecommendationTypeDef = TypedDict(
    "VolumeRecommendationTypeDef",
    {
        "volumeArn": str,
        "accountId": str,
        "currentConfiguration": "VolumeConfigurationTypeDef",
        "finding": EBSFindingType,
        "utilizationMetrics": List["EBSUtilizationMetricTypeDef"],
        "lookBackPeriodInDays": float,
        "volumeRecommendationOptions": List["VolumeRecommendationOptionTypeDef"],
        "lastRefreshTimestamp": datetime,
        "currentPerformanceRisk": CurrentPerformanceRiskType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)
