"""
Type annotations for compute-optimizer service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_compute_optimizer.type_defs import AccountEnrollmentStatusTypeDef

    data: AccountEnrollmentStatusTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AllocationStrategyType,
    AsgTypeType,
    AutoScalingConfigurationType,
    CpuVendorArchitectureType,
    CurrencyType,
    CurrentPerformanceRiskType,
    CustomizableMetricHeadroomType,
    CustomizableMetricNameType,
    CustomizableMetricThresholdType,
    DimensionType,
    EBSFindingType,
    EBSMetricNameType,
    EBSSavingsEstimationModeSourceType,
    ECSSavingsEstimationModeSourceType,
    ECSServiceLaunchTypeType,
    ECSServiceMetricNameType,
    ECSServiceMetricStatisticType,
    ECSServiceRecommendationFilterNameType,
    ECSServiceRecommendationFindingReasonCodeType,
    ECSServiceRecommendationFindingType,
    EnhancedInfrastructureMetricsType,
    ExportableAutoScalingGroupFieldType,
    ExportableECSServiceFieldType,
    ExportableIdleFieldType,
    ExportableInstanceFieldType,
    ExportableLambdaFunctionFieldType,
    ExportableLicenseFieldType,
    ExportableRDSDBFieldType,
    ExportableVolumeFieldType,
    ExternalMetricsSourceType,
    ExternalMetricStatusCodeType,
    FilterNameType,
    FindingReasonCodeType,
    FindingType,
    IdleFindingType,
    IdleMetricNameType,
    IdleRecommendationFilterNameType,
    IdleRecommendationResourceTypeType,
    IdleType,
    InferredWorkloadTypesPreferenceType,
    InferredWorkloadTypeType,
    InstanceIdleType,
    InstanceRecommendationFindingReasonCodeType,
    InstanceSavingsEstimationModeSourceType,
    InstanceStateType,
    JobFilterNameType,
    JobStatusType,
    LambdaFunctionMemoryMetricStatisticType,
    LambdaFunctionMetricNameType,
    LambdaFunctionMetricStatisticType,
    LambdaFunctionRecommendationFilterNameType,
    LambdaFunctionRecommendationFindingReasonCodeType,
    LambdaFunctionRecommendationFindingType,
    LambdaSavingsEstimationModeSourceType,
    LicenseEditionType,
    LicenseFindingReasonCodeType,
    LicenseFindingType,
    LicenseModelType,
    LicenseRecommendationFilterNameType,
    LookBackPeriodPreferenceType,
    MetricNameType,
    MetricStatisticType,
    MigrationEffortType,
    OrderType,
    PlatformDifferenceType,
    RDSCurrentInstancePerformanceRiskType,
    RDSDBMetricNameType,
    RDSDBMetricStatisticType,
    RDSDBRecommendationFilterNameType,
    RDSInstanceFindingReasonCodeType,
    RDSInstanceFindingType,
    RDSSavingsEstimationModeSourceType,
    RDSStorageFindingReasonCodeType,
    RDSStorageFindingType,
    RecommendationPreferenceNameType,
    RecommendationSourceTypeType,
    ResourceTypeType,
    SavingsEstimationModeType,
    ScopeNameType,
    StatusType,
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
    "AccountEnrollmentStatusTypeDef",
    "AutoScalingGroupConfigurationTypeDef",
    "AutoScalingGroupEstimatedMonthlySavingsTypeDef",
    "AutoScalingGroupRecommendationOptionTypeDef",
    "AutoScalingGroupRecommendationTypeDef",
    "AutoScalingGroupSavingsOpportunityAfterDiscountsTypeDef",
    "ContainerConfigurationTypeDef",
    "ContainerRecommendationTypeDef",
    "CurrentPerformanceRiskRatingsTypeDef",
    "CustomizableMetricParametersTypeDef",
    "DBStorageConfigurationTypeDef",
    "DeleteRecommendationPreferencesRequestTypeDef",
    "DescribeRecommendationExportJobsRequestPaginateTypeDef",
    "DescribeRecommendationExportJobsRequestTypeDef",
    "DescribeRecommendationExportJobsResponseTypeDef",
    "EBSEffectiveRecommendationPreferencesTypeDef",
    "EBSEstimatedMonthlySavingsTypeDef",
    "EBSFilterTypeDef",
    "EBSSavingsEstimationModeTypeDef",
    "EBSSavingsOpportunityAfterDiscountsTypeDef",
    "EBSUtilizationMetricTypeDef",
    "ECSEffectiveRecommendationPreferencesTypeDef",
    "ECSEstimatedMonthlySavingsTypeDef",
    "ECSSavingsEstimationModeTypeDef",
    "ECSSavingsOpportunityAfterDiscountsTypeDef",
    "ECSServiceProjectedMetricTypeDef",
    "ECSServiceProjectedUtilizationMetricTypeDef",
    "ECSServiceRecommendationFilterTypeDef",
    "ECSServiceRecommendationOptionTypeDef",
    "ECSServiceRecommendationTypeDef",
    "ECSServiceRecommendedOptionProjectedMetricTypeDef",
    "ECSServiceUtilizationMetricTypeDef",
    "EffectivePreferredResourceTypeDef",
    "EffectiveRecommendationPreferencesTypeDef",
    "EnrollmentFilterTypeDef",
    "EstimatedMonthlySavingsTypeDef",
    "ExportAutoScalingGroupRecommendationsRequestTypeDef",
    "ExportAutoScalingGroupRecommendationsResponseTypeDef",
    "ExportDestinationTypeDef",
    "ExportEBSVolumeRecommendationsRequestTypeDef",
    "ExportEBSVolumeRecommendationsResponseTypeDef",
    "ExportEC2InstanceRecommendationsRequestTypeDef",
    "ExportEC2InstanceRecommendationsResponseTypeDef",
    "ExportECSServiceRecommendationsRequestTypeDef",
    "ExportECSServiceRecommendationsResponseTypeDef",
    "ExportIdleRecommendationsRequestTypeDef",
    "ExportIdleRecommendationsResponseTypeDef",
    "ExportLambdaFunctionRecommendationsRequestTypeDef",
    "ExportLambdaFunctionRecommendationsResponseTypeDef",
    "ExportLicenseRecommendationsRequestTypeDef",
    "ExportLicenseRecommendationsResponseTypeDef",
    "ExportRDSDatabaseRecommendationsRequestTypeDef",
    "ExportRDSDatabaseRecommendationsResponseTypeDef",
    "ExternalMetricStatusTypeDef",
    "ExternalMetricsPreferenceTypeDef",
    "FilterTypeDef",
    "GetAutoScalingGroupRecommendationsRequestTypeDef",
    "GetAutoScalingGroupRecommendationsResponseTypeDef",
    "GetEBSVolumeRecommendationsRequestTypeDef",
    "GetEBSVolumeRecommendationsResponseTypeDef",
    "GetEC2InstanceRecommendationsRequestTypeDef",
    "GetEC2InstanceRecommendationsResponseTypeDef",
    "GetEC2RecommendationProjectedMetricsRequestTypeDef",
    "GetEC2RecommendationProjectedMetricsResponseTypeDef",
    "GetECSServiceRecommendationProjectedMetricsRequestTypeDef",
    "GetECSServiceRecommendationProjectedMetricsResponseTypeDef",
    "GetECSServiceRecommendationsRequestTypeDef",
    "GetECSServiceRecommendationsResponseTypeDef",
    "GetEffectiveRecommendationPreferencesRequestTypeDef",
    "GetEffectiveRecommendationPreferencesResponseTypeDef",
    "GetEnrollmentStatusResponseTypeDef",
    "GetEnrollmentStatusesForOrganizationRequestPaginateTypeDef",
    "GetEnrollmentStatusesForOrganizationRequestTypeDef",
    "GetEnrollmentStatusesForOrganizationResponseTypeDef",
    "GetIdleRecommendationsRequestTypeDef",
    "GetIdleRecommendationsResponseTypeDef",
    "GetLambdaFunctionRecommendationsRequestPaginateTypeDef",
    "GetLambdaFunctionRecommendationsRequestTypeDef",
    "GetLambdaFunctionRecommendationsResponseTypeDef",
    "GetLicenseRecommendationsRequestTypeDef",
    "GetLicenseRecommendationsResponseTypeDef",
    "GetRDSDatabaseRecommendationProjectedMetricsRequestTypeDef",
    "GetRDSDatabaseRecommendationProjectedMetricsResponseTypeDef",
    "GetRDSDatabaseRecommendationsRequestTypeDef",
    "GetRDSDatabaseRecommendationsResponseTypeDef",
    "GetRecommendationErrorTypeDef",
    "GetRecommendationPreferencesRequestPaginateTypeDef",
    "GetRecommendationPreferencesRequestTypeDef",
    "GetRecommendationPreferencesResponseTypeDef",
    "GetRecommendationSummariesRequestPaginateTypeDef",
    "GetRecommendationSummariesRequestTypeDef",
    "GetRecommendationSummariesResponseTypeDef",
    "GpuInfoTypeDef",
    "GpuTypeDef",
    "IdleEstimatedMonthlySavingsTypeDef",
    "IdleRecommendationErrorTypeDef",
    "IdleRecommendationFilterTypeDef",
    "IdleRecommendationTypeDef",
    "IdleSavingsOpportunityAfterDiscountsTypeDef",
    "IdleSavingsOpportunityTypeDef",
    "IdleSummaryTypeDef",
    "IdleUtilizationMetricTypeDef",
    "InferredWorkloadSavingTypeDef",
    "InstanceEstimatedMonthlySavingsTypeDef",
    "InstanceRecommendationOptionTypeDef",
    "InstanceRecommendationTypeDef",
    "InstanceSavingsEstimationModeTypeDef",
    "InstanceSavingsOpportunityAfterDiscountsTypeDef",
    "JobFilterTypeDef",
    "LambdaEffectiveRecommendationPreferencesTypeDef",
    "LambdaEstimatedMonthlySavingsTypeDef",
    "LambdaFunctionMemoryProjectedMetricTypeDef",
    "LambdaFunctionMemoryRecommendationOptionTypeDef",
    "LambdaFunctionRecommendationFilterTypeDef",
    "LambdaFunctionRecommendationTypeDef",
    "LambdaFunctionUtilizationMetricTypeDef",
    "LambdaSavingsEstimationModeTypeDef",
    "LambdaSavingsOpportunityAfterDiscountsTypeDef",
    "LicenseConfigurationTypeDef",
    "LicenseRecommendationFilterTypeDef",
    "LicenseRecommendationOptionTypeDef",
    "LicenseRecommendationTypeDef",
    "MemorySizeConfigurationTypeDef",
    "MetricSourceTypeDef",
    "OrderByTypeDef",
    "PaginatorConfigTypeDef",
    "PreferredResourceTypeDef",
    "ProjectedMetricTypeDef",
    "PutRecommendationPreferencesRequestTypeDef",
    "RDSDBInstanceRecommendationOptionTypeDef",
    "RDSDBRecommendationFilterTypeDef",
    "RDSDBRecommendationTypeDef",
    "RDSDBStorageRecommendationOptionTypeDef",
    "RDSDBUtilizationMetricTypeDef",
    "RDSDatabaseProjectedMetricTypeDef",
    "RDSDatabaseRecommendedOptionProjectedMetricTypeDef",
    "RDSEffectiveRecommendationPreferencesTypeDef",
    "RDSInstanceEstimatedMonthlySavingsTypeDef",
    "RDSInstanceSavingsOpportunityAfterDiscountsTypeDef",
    "RDSSavingsEstimationModeTypeDef",
    "RDSStorageEstimatedMonthlySavingsTypeDef",
    "RDSStorageSavingsOpportunityAfterDiscountsTypeDef",
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
    "TimestampTypeDef",
    "UpdateEnrollmentStatusRequestTypeDef",
    "UpdateEnrollmentStatusResponseTypeDef",
    "UtilizationMetricTypeDef",
    "UtilizationPreferenceTypeDef",
    "VolumeConfigurationTypeDef",
    "VolumeRecommendationOptionTypeDef",
    "VolumeRecommendationTypeDef",
)

class AccountEnrollmentStatusTypeDef(TypedDict):
    accountId: NotRequired[str]
    status: NotRequired[StatusType]
    statusReason: NotRequired[str]
    lastUpdatedTimestamp: NotRequired[datetime]

AutoScalingGroupConfigurationTypeDef = TypedDict(
    "AutoScalingGroupConfigurationTypeDef",
    {
        "desiredCapacity": NotRequired[int],
        "minSize": NotRequired[int],
        "maxSize": NotRequired[int],
        "instanceType": NotRequired[str],
        "allocationStrategy": NotRequired[AllocationStrategyType],
        "estimatedInstanceHourReductionPercentage": NotRequired[float],
        "type": NotRequired[AsgTypeType],
        "mixedInstanceTypes": NotRequired[List[str]],
    },
)

class AutoScalingGroupEstimatedMonthlySavingsTypeDef(TypedDict):
    currency: NotRequired[CurrencyType]
    value: NotRequired[float]

class UtilizationMetricTypeDef(TypedDict):
    name: NotRequired[MetricNameType]
    statistic: NotRequired[MetricStatisticType]
    value: NotRequired[float]

class MemorySizeConfigurationTypeDef(TypedDict):
    memory: NotRequired[int]
    memoryReservation: NotRequired[int]

class CurrentPerformanceRiskRatingsTypeDef(TypedDict):
    high: NotRequired[int]
    medium: NotRequired[int]
    low: NotRequired[int]
    veryLow: NotRequired[int]

class CustomizableMetricParametersTypeDef(TypedDict):
    threshold: NotRequired[CustomizableMetricThresholdType]
    headroom: NotRequired[CustomizableMetricHeadroomType]

class DBStorageConfigurationTypeDef(TypedDict):
    storageType: NotRequired[str]
    allocatedStorage: NotRequired[int]
    iops: NotRequired[int]
    maxAllocatedStorage: NotRequired[int]
    storageThroughput: NotRequired[int]

class ScopeTypeDef(TypedDict):
    name: NotRequired[ScopeNameType]
    value: NotRequired[str]

class JobFilterTypeDef(TypedDict):
    name: NotRequired[JobFilterNameType]
    values: NotRequired[Sequence[str]]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class EBSSavingsEstimationModeTypeDef(TypedDict):
    source: NotRequired[EBSSavingsEstimationModeSourceType]

class EBSEstimatedMonthlySavingsTypeDef(TypedDict):
    currency: NotRequired[CurrencyType]
    value: NotRequired[float]

class EBSFilterTypeDef(TypedDict):
    name: NotRequired[Literal["Finding"]]
    values: NotRequired[Sequence[str]]

class EBSUtilizationMetricTypeDef(TypedDict):
    name: NotRequired[EBSMetricNameType]
    statistic: NotRequired[MetricStatisticType]
    value: NotRequired[float]

class ECSSavingsEstimationModeTypeDef(TypedDict):
    source: NotRequired[ECSSavingsEstimationModeSourceType]

class ECSEstimatedMonthlySavingsTypeDef(TypedDict):
    currency: NotRequired[CurrencyType]
    value: NotRequired[float]

class ECSServiceProjectedMetricTypeDef(TypedDict):
    name: NotRequired[ECSServiceMetricNameType]
    timestamps: NotRequired[List[datetime]]
    upperBoundValues: NotRequired[List[float]]
    lowerBoundValues: NotRequired[List[float]]

class ECSServiceProjectedUtilizationMetricTypeDef(TypedDict):
    name: NotRequired[ECSServiceMetricNameType]
    statistic: NotRequired[ECSServiceMetricStatisticType]
    lowerBoundValue: NotRequired[float]
    upperBoundValue: NotRequired[float]

class ECSServiceRecommendationFilterTypeDef(TypedDict):
    name: NotRequired[ECSServiceRecommendationFilterNameType]
    values: NotRequired[Sequence[str]]

class ECSServiceUtilizationMetricTypeDef(TypedDict):
    name: NotRequired[ECSServiceMetricNameType]
    statistic: NotRequired[ECSServiceMetricStatisticType]
    value: NotRequired[float]

class TagTypeDef(TypedDict):
    key: NotRequired[str]
    value: NotRequired[str]

class EffectivePreferredResourceTypeDef(TypedDict):
    name: NotRequired[Literal["Ec2InstanceTypes"]]
    includeList: NotRequired[List[str]]
    effectiveIncludeList: NotRequired[List[str]]
    excludeList: NotRequired[List[str]]

class ExternalMetricsPreferenceTypeDef(TypedDict):
    source: NotRequired[ExternalMetricsSourceType]

class InstanceSavingsEstimationModeTypeDef(TypedDict):
    source: NotRequired[InstanceSavingsEstimationModeSourceType]

class EnrollmentFilterTypeDef(TypedDict):
    name: NotRequired[Literal["Status"]]
    values: NotRequired[Sequence[str]]

class EstimatedMonthlySavingsTypeDef(TypedDict):
    currency: NotRequired[CurrencyType]
    value: NotRequired[float]

class FilterTypeDef(TypedDict):
    name: NotRequired[FilterNameType]
    values: NotRequired[Sequence[str]]

class RecommendationPreferencesTypeDef(TypedDict):
    cpuVendorArchitectures: NotRequired[Sequence[CpuVendorArchitectureType]]

class S3DestinationConfigTypeDef(TypedDict):
    bucket: NotRequired[str]
    keyPrefix: NotRequired[str]

class S3DestinationTypeDef(TypedDict):
    bucket: NotRequired[str]
    key: NotRequired[str]
    metadataKey: NotRequired[str]

class IdleRecommendationFilterTypeDef(TypedDict):
    name: NotRequired[IdleRecommendationFilterNameType]
    values: NotRequired[Sequence[str]]

class LambdaFunctionRecommendationFilterTypeDef(TypedDict):
    name: NotRequired[LambdaFunctionRecommendationFilterNameType]
    values: NotRequired[Sequence[str]]

class LicenseRecommendationFilterTypeDef(TypedDict):
    name: NotRequired[LicenseRecommendationFilterNameType]
    values: NotRequired[Sequence[str]]

class RDSDBRecommendationFilterTypeDef(TypedDict):
    name: NotRequired[RDSDBRecommendationFilterNameType]
    values: NotRequired[Sequence[str]]

class ExternalMetricStatusTypeDef(TypedDict):
    statusCode: NotRequired[ExternalMetricStatusCodeType]
    statusReason: NotRequired[str]

class GetRecommendationErrorTypeDef(TypedDict):
    identifier: NotRequired[str]
    code: NotRequired[str]
    message: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class GetEffectiveRecommendationPreferencesRequestTypeDef(TypedDict):
    resourceArn: str

class OrderByTypeDef(TypedDict):
    dimension: NotRequired[DimensionType]
    order: NotRequired[OrderType]

class IdleRecommendationErrorTypeDef(TypedDict):
    identifier: NotRequired[str]
    code: NotRequired[str]
    message: NotRequired[str]
    resourceType: NotRequired[IdleRecommendationResourceTypeType]

class GetRecommendationSummariesRequestTypeDef(TypedDict):
    accountIds: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class GpuTypeDef(TypedDict):
    gpuCount: NotRequired[int]
    gpuMemorySizeInMiB: NotRequired[int]

class IdleEstimatedMonthlySavingsTypeDef(TypedDict):
    currency: NotRequired[CurrencyType]
    value: NotRequired[float]

class IdleUtilizationMetricTypeDef(TypedDict):
    name: NotRequired[IdleMetricNameType]
    statistic: NotRequired[MetricStatisticType]
    value: NotRequired[float]

class IdleSummaryTypeDef(TypedDict):
    name: NotRequired[IdleFindingType]
    value: NotRequired[float]

class InstanceEstimatedMonthlySavingsTypeDef(TypedDict):
    currency: NotRequired[CurrencyType]
    value: NotRequired[float]

class RecommendationSourceTypeDef(TypedDict):
    recommendationSourceArn: NotRequired[str]
    recommendationSourceType: NotRequired[RecommendationSourceTypeType]

class LambdaSavingsEstimationModeTypeDef(TypedDict):
    source: NotRequired[LambdaSavingsEstimationModeSourceType]

class LambdaEstimatedMonthlySavingsTypeDef(TypedDict):
    currency: NotRequired[CurrencyType]
    value: NotRequired[float]

class LambdaFunctionMemoryProjectedMetricTypeDef(TypedDict):
    name: NotRequired[Literal["Duration"]]
    statistic: NotRequired[LambdaFunctionMemoryMetricStatisticType]
    value: NotRequired[float]

class LambdaFunctionUtilizationMetricTypeDef(TypedDict):
    name: NotRequired[LambdaFunctionMetricNameType]
    statistic: NotRequired[LambdaFunctionMetricStatisticType]
    value: NotRequired[float]

class MetricSourceTypeDef(TypedDict):
    provider: NotRequired[Literal["CloudWatchApplicationInsights"]]
    providerArn: NotRequired[str]

class PreferredResourceTypeDef(TypedDict):
    name: NotRequired[Literal["Ec2InstanceTypes"]]
    includeList: NotRequired[Sequence[str]]
    excludeList: NotRequired[Sequence[str]]

class ProjectedMetricTypeDef(TypedDict):
    name: NotRequired[MetricNameType]
    timestamps: NotRequired[List[datetime]]
    values: NotRequired[List[float]]

class RDSDBUtilizationMetricTypeDef(TypedDict):
    name: NotRequired[RDSDBMetricNameType]
    statistic: NotRequired[RDSDBMetricStatisticType]
    value: NotRequired[float]

class RDSDatabaseProjectedMetricTypeDef(TypedDict):
    name: NotRequired[RDSDBMetricNameType]
    timestamps: NotRequired[List[datetime]]
    values: NotRequired[List[float]]

class RDSSavingsEstimationModeTypeDef(TypedDict):
    source: NotRequired[RDSSavingsEstimationModeSourceType]

class RDSInstanceEstimatedMonthlySavingsTypeDef(TypedDict):
    currency: NotRequired[CurrencyType]
    value: NotRequired[float]

class RDSStorageEstimatedMonthlySavingsTypeDef(TypedDict):
    currency: NotRequired[CurrencyType]
    value: NotRequired[float]

class ReasonCodeSummaryTypeDef(TypedDict):
    name: NotRequired[FindingReasonCodeType]
    value: NotRequired[float]

class UpdateEnrollmentStatusRequestTypeDef(TypedDict):
    status: StatusType
    includeMemberAccounts: NotRequired[bool]

class VolumeConfigurationTypeDef(TypedDict):
    volumeType: NotRequired[str]
    volumeSize: NotRequired[int]
    volumeBaselineIOPS: NotRequired[int]
    volumeBurstIOPS: NotRequired[int]
    volumeBaselineThroughput: NotRequired[int]
    volumeBurstThroughput: NotRequired[int]
    rootVolume: NotRequired[bool]

class AutoScalingGroupSavingsOpportunityAfterDiscountsTypeDef(TypedDict):
    savingsOpportunityPercentage: NotRequired[float]
    estimatedMonthlySavings: NotRequired[AutoScalingGroupEstimatedMonthlySavingsTypeDef]

class ContainerConfigurationTypeDef(TypedDict):
    containerName: NotRequired[str]
    memorySizeConfiguration: NotRequired[MemorySizeConfigurationTypeDef]
    cpu: NotRequired[int]

class ContainerRecommendationTypeDef(TypedDict):
    containerName: NotRequired[str]
    memorySizeConfiguration: NotRequired[MemorySizeConfigurationTypeDef]
    cpu: NotRequired[int]

class UtilizationPreferenceTypeDef(TypedDict):
    metricName: NotRequired[CustomizableMetricNameType]
    metricParameters: NotRequired[CustomizableMetricParametersTypeDef]

class DeleteRecommendationPreferencesRequestTypeDef(TypedDict):
    resourceType: ResourceTypeType
    recommendationPreferenceNames: Sequence[RecommendationPreferenceNameType]
    scope: NotRequired[ScopeTypeDef]

class GetRecommendationPreferencesRequestTypeDef(TypedDict):
    resourceType: ResourceTypeType
    scope: NotRequired[ScopeTypeDef]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class DescribeRecommendationExportJobsRequestTypeDef(TypedDict):
    jobIds: NotRequired[Sequence[str]]
    filters: NotRequired[Sequence[JobFilterTypeDef]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class DescribeRecommendationExportJobsRequestPaginateTypeDef(TypedDict):
    jobIds: NotRequired[Sequence[str]]
    filters: NotRequired[Sequence[JobFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetRecommendationPreferencesRequestPaginateTypeDef(TypedDict):
    resourceType: ResourceTypeType
    scope: NotRequired[ScopeTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetRecommendationSummariesRequestPaginateTypeDef(TypedDict):
    accountIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetEnrollmentStatusResponseTypeDef(TypedDict):
    status: StatusType
    statusReason: str
    memberAccountsEnrolled: bool
    lastUpdatedTimestamp: datetime
    numberOfMemberAccountsOptedIn: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnrollmentStatusesForOrganizationResponseTypeDef(TypedDict):
    accountEnrollmentStatuses: List[AccountEnrollmentStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateEnrollmentStatusResponseTypeDef(TypedDict):
    status: StatusType
    statusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class EBSEffectiveRecommendationPreferencesTypeDef(TypedDict):
    savingsEstimationMode: NotRequired[EBSSavingsEstimationModeTypeDef]

class EBSSavingsOpportunityAfterDiscountsTypeDef(TypedDict):
    savingsOpportunityPercentage: NotRequired[float]
    estimatedMonthlySavings: NotRequired[EBSEstimatedMonthlySavingsTypeDef]

class GetEBSVolumeRecommendationsRequestTypeDef(TypedDict):
    volumeArns: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    filters: NotRequired[Sequence[EBSFilterTypeDef]]
    accountIds: NotRequired[Sequence[str]]

class ECSEffectiveRecommendationPreferencesTypeDef(TypedDict):
    savingsEstimationMode: NotRequired[ECSSavingsEstimationModeTypeDef]

class ECSSavingsOpportunityAfterDiscountsTypeDef(TypedDict):
    savingsOpportunityPercentage: NotRequired[float]
    estimatedMonthlySavings: NotRequired[ECSEstimatedMonthlySavingsTypeDef]

class ECSServiceRecommendedOptionProjectedMetricTypeDef(TypedDict):
    recommendedCpuUnits: NotRequired[int]
    recommendedMemorySize: NotRequired[int]
    projectedMetrics: NotRequired[List[ECSServiceProjectedMetricTypeDef]]

class GetECSServiceRecommendationsRequestTypeDef(TypedDict):
    serviceArns: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    filters: NotRequired[Sequence[ECSServiceRecommendationFilterTypeDef]]
    accountIds: NotRequired[Sequence[str]]

class GetEnrollmentStatusesForOrganizationRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[EnrollmentFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetEnrollmentStatusesForOrganizationRequestTypeDef(TypedDict):
    filters: NotRequired[Sequence[EnrollmentFilterTypeDef]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class InferredWorkloadSavingTypeDef(TypedDict):
    inferredWorkloadTypes: NotRequired[List[InferredWorkloadTypeType]]
    estimatedMonthlySavings: NotRequired[EstimatedMonthlySavingsTypeDef]

class SavingsOpportunityTypeDef(TypedDict):
    savingsOpportunityPercentage: NotRequired[float]
    estimatedMonthlySavings: NotRequired[EstimatedMonthlySavingsTypeDef]

class GetAutoScalingGroupRecommendationsRequestTypeDef(TypedDict):
    accountIds: NotRequired[Sequence[str]]
    autoScalingGroupArns: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    filters: NotRequired[Sequence[FilterTypeDef]]
    recommendationPreferences: NotRequired[RecommendationPreferencesTypeDef]

class GetEC2InstanceRecommendationsRequestTypeDef(TypedDict):
    instanceArns: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    filters: NotRequired[Sequence[FilterTypeDef]]
    accountIds: NotRequired[Sequence[str]]
    recommendationPreferences: NotRequired[RecommendationPreferencesTypeDef]

class ExportAutoScalingGroupRecommendationsRequestTypeDef(TypedDict):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: NotRequired[Sequence[str]]
    filters: NotRequired[Sequence[FilterTypeDef]]
    fieldsToExport: NotRequired[Sequence[ExportableAutoScalingGroupFieldType]]
    fileFormat: NotRequired[Literal["Csv"]]
    includeMemberAccounts: NotRequired[bool]
    recommendationPreferences: NotRequired[RecommendationPreferencesTypeDef]

class ExportEBSVolumeRecommendationsRequestTypeDef(TypedDict):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: NotRequired[Sequence[str]]
    filters: NotRequired[Sequence[EBSFilterTypeDef]]
    fieldsToExport: NotRequired[Sequence[ExportableVolumeFieldType]]
    fileFormat: NotRequired[Literal["Csv"]]
    includeMemberAccounts: NotRequired[bool]

class ExportEC2InstanceRecommendationsRequestTypeDef(TypedDict):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: NotRequired[Sequence[str]]
    filters: NotRequired[Sequence[FilterTypeDef]]
    fieldsToExport: NotRequired[Sequence[ExportableInstanceFieldType]]
    fileFormat: NotRequired[Literal["Csv"]]
    includeMemberAccounts: NotRequired[bool]
    recommendationPreferences: NotRequired[RecommendationPreferencesTypeDef]

class ExportECSServiceRecommendationsRequestTypeDef(TypedDict):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: NotRequired[Sequence[str]]
    filters: NotRequired[Sequence[ECSServiceRecommendationFilterTypeDef]]
    fieldsToExport: NotRequired[Sequence[ExportableECSServiceFieldType]]
    fileFormat: NotRequired[Literal["Csv"]]
    includeMemberAccounts: NotRequired[bool]

class ExportAutoScalingGroupRecommendationsResponseTypeDef(TypedDict):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportDestinationTypeDef(TypedDict):
    s3: NotRequired[S3DestinationTypeDef]

class ExportEBSVolumeRecommendationsResponseTypeDef(TypedDict):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportEC2InstanceRecommendationsResponseTypeDef(TypedDict):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportECSServiceRecommendationsResponseTypeDef(TypedDict):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportIdleRecommendationsResponseTypeDef(TypedDict):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportLambdaFunctionRecommendationsResponseTypeDef(TypedDict):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportLicenseRecommendationsResponseTypeDef(TypedDict):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportRDSDatabaseRecommendationsResponseTypeDef(TypedDict):
    jobId: str
    s3Destination: S3DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportIdleRecommendationsRequestTypeDef(TypedDict):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: NotRequired[Sequence[str]]
    filters: NotRequired[Sequence[IdleRecommendationFilterTypeDef]]
    fieldsToExport: NotRequired[Sequence[ExportableIdleFieldType]]
    fileFormat: NotRequired[Literal["Csv"]]
    includeMemberAccounts: NotRequired[bool]

class ExportLambdaFunctionRecommendationsRequestTypeDef(TypedDict):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: NotRequired[Sequence[str]]
    filters: NotRequired[Sequence[LambdaFunctionRecommendationFilterTypeDef]]
    fieldsToExport: NotRequired[Sequence[ExportableLambdaFunctionFieldType]]
    fileFormat: NotRequired[Literal["Csv"]]
    includeMemberAccounts: NotRequired[bool]

class GetLambdaFunctionRecommendationsRequestPaginateTypeDef(TypedDict):
    functionArns: NotRequired[Sequence[str]]
    accountIds: NotRequired[Sequence[str]]
    filters: NotRequired[Sequence[LambdaFunctionRecommendationFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetLambdaFunctionRecommendationsRequestTypeDef(TypedDict):
    functionArns: NotRequired[Sequence[str]]
    accountIds: NotRequired[Sequence[str]]
    filters: NotRequired[Sequence[LambdaFunctionRecommendationFilterTypeDef]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ExportLicenseRecommendationsRequestTypeDef(TypedDict):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: NotRequired[Sequence[str]]
    filters: NotRequired[Sequence[LicenseRecommendationFilterTypeDef]]
    fieldsToExport: NotRequired[Sequence[ExportableLicenseFieldType]]
    fileFormat: NotRequired[Literal["Csv"]]
    includeMemberAccounts: NotRequired[bool]

class GetLicenseRecommendationsRequestTypeDef(TypedDict):
    resourceArns: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    filters: NotRequired[Sequence[LicenseRecommendationFilterTypeDef]]
    accountIds: NotRequired[Sequence[str]]

class ExportRDSDatabaseRecommendationsRequestTypeDef(TypedDict):
    s3DestinationConfig: S3DestinationConfigTypeDef
    accountIds: NotRequired[Sequence[str]]
    filters: NotRequired[Sequence[RDSDBRecommendationFilterTypeDef]]
    fieldsToExport: NotRequired[Sequence[ExportableRDSDBFieldType]]
    fileFormat: NotRequired[Literal["Csv"]]
    includeMemberAccounts: NotRequired[bool]
    recommendationPreferences: NotRequired[RecommendationPreferencesTypeDef]

class GetRDSDatabaseRecommendationsRequestTypeDef(TypedDict):
    resourceArns: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    filters: NotRequired[Sequence[RDSDBRecommendationFilterTypeDef]]
    accountIds: NotRequired[Sequence[str]]
    recommendationPreferences: NotRequired[RecommendationPreferencesTypeDef]

class GetEC2RecommendationProjectedMetricsRequestTypeDef(TypedDict):
    instanceArn: str
    stat: MetricStatisticType
    period: int
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    recommendationPreferences: NotRequired[RecommendationPreferencesTypeDef]

class GetECSServiceRecommendationProjectedMetricsRequestTypeDef(TypedDict):
    serviceArn: str
    stat: MetricStatisticType
    period: int
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef

class GetRDSDatabaseRecommendationProjectedMetricsRequestTypeDef(TypedDict):
    resourceArn: str
    stat: MetricStatisticType
    period: int
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    recommendationPreferences: NotRequired[RecommendationPreferencesTypeDef]

class GetIdleRecommendationsRequestTypeDef(TypedDict):
    resourceArns: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    filters: NotRequired[Sequence[IdleRecommendationFilterTypeDef]]
    accountIds: NotRequired[Sequence[str]]
    orderBy: NotRequired[OrderByTypeDef]

class GpuInfoTypeDef(TypedDict):
    gpus: NotRequired[List[GpuTypeDef]]

class IdleSavingsOpportunityAfterDiscountsTypeDef(TypedDict):
    savingsOpportunityPercentage: NotRequired[float]
    estimatedMonthlySavings: NotRequired[IdleEstimatedMonthlySavingsTypeDef]

class IdleSavingsOpportunityTypeDef(TypedDict):
    savingsOpportunityPercentage: NotRequired[float]
    estimatedMonthlySavings: NotRequired[IdleEstimatedMonthlySavingsTypeDef]

class InstanceSavingsOpportunityAfterDiscountsTypeDef(TypedDict):
    savingsOpportunityPercentage: NotRequired[float]
    estimatedMonthlySavings: NotRequired[InstanceEstimatedMonthlySavingsTypeDef]

class LambdaEffectiveRecommendationPreferencesTypeDef(TypedDict):
    savingsEstimationMode: NotRequired[LambdaSavingsEstimationModeTypeDef]

class LambdaSavingsOpportunityAfterDiscountsTypeDef(TypedDict):
    savingsOpportunityPercentage: NotRequired[float]
    estimatedMonthlySavings: NotRequired[LambdaEstimatedMonthlySavingsTypeDef]

class LicenseConfigurationTypeDef(TypedDict):
    numberOfCores: NotRequired[int]
    instanceType: NotRequired[str]
    operatingSystem: NotRequired[str]
    licenseEdition: NotRequired[LicenseEditionType]
    licenseName: NotRequired[Literal["SQLServer"]]
    licenseModel: NotRequired[LicenseModelType]
    licenseVersion: NotRequired[str]
    metricsSource: NotRequired[List[MetricSourceTypeDef]]

class RecommendedOptionProjectedMetricTypeDef(TypedDict):
    recommendedInstanceType: NotRequired[str]
    rank: NotRequired[int]
    projectedMetrics: NotRequired[List[ProjectedMetricTypeDef]]

class RDSDatabaseRecommendedOptionProjectedMetricTypeDef(TypedDict):
    recommendedDBInstanceClass: NotRequired[str]
    rank: NotRequired[int]
    projectedMetrics: NotRequired[List[RDSDatabaseProjectedMetricTypeDef]]

class RDSEffectiveRecommendationPreferencesTypeDef(TypedDict):
    cpuVendorArchitectures: NotRequired[List[CpuVendorArchitectureType]]
    enhancedInfrastructureMetrics: NotRequired[EnhancedInfrastructureMetricsType]
    lookBackPeriod: NotRequired[LookBackPeriodPreferenceType]
    savingsEstimationMode: NotRequired[RDSSavingsEstimationModeTypeDef]

class RDSInstanceSavingsOpportunityAfterDiscountsTypeDef(TypedDict):
    savingsOpportunityPercentage: NotRequired[float]
    estimatedMonthlySavings: NotRequired[RDSInstanceEstimatedMonthlySavingsTypeDef]

class RDSStorageSavingsOpportunityAfterDiscountsTypeDef(TypedDict):
    savingsOpportunityPercentage: NotRequired[float]
    estimatedMonthlySavings: NotRequired[RDSStorageEstimatedMonthlySavingsTypeDef]

class SummaryTypeDef(TypedDict):
    name: NotRequired[FindingType]
    value: NotRequired[float]
    reasonCodeSummaries: NotRequired[List[ReasonCodeSummaryTypeDef]]

class ServiceConfigurationTypeDef(TypedDict):
    memory: NotRequired[int]
    cpu: NotRequired[int]
    containerConfigurations: NotRequired[List[ContainerConfigurationTypeDef]]
    autoScalingConfiguration: NotRequired[AutoScalingConfigurationType]
    taskDefinitionArn: NotRequired[str]

class EffectiveRecommendationPreferencesTypeDef(TypedDict):
    cpuVendorArchitectures: NotRequired[List[CpuVendorArchitectureType]]
    enhancedInfrastructureMetrics: NotRequired[EnhancedInfrastructureMetricsType]
    inferredWorkloadTypes: NotRequired[InferredWorkloadTypesPreferenceType]
    externalMetricsPreference: NotRequired[ExternalMetricsPreferenceTypeDef]
    lookBackPeriod: NotRequired[LookBackPeriodPreferenceType]
    utilizationPreferences: NotRequired[List[UtilizationPreferenceTypeDef]]
    preferredResources: NotRequired[List[EffectivePreferredResourceTypeDef]]
    savingsEstimationMode: NotRequired[InstanceSavingsEstimationModeTypeDef]

class GetEffectiveRecommendationPreferencesResponseTypeDef(TypedDict):
    enhancedInfrastructureMetrics: EnhancedInfrastructureMetricsType
    externalMetricsPreference: ExternalMetricsPreferenceTypeDef
    lookBackPeriod: LookBackPeriodPreferenceType
    utilizationPreferences: List[UtilizationPreferenceTypeDef]
    preferredResources: List[EffectivePreferredResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutRecommendationPreferencesRequestTypeDef(TypedDict):
    resourceType: ResourceTypeType
    scope: NotRequired[ScopeTypeDef]
    enhancedInfrastructureMetrics: NotRequired[EnhancedInfrastructureMetricsType]
    inferredWorkloadTypes: NotRequired[InferredWorkloadTypesPreferenceType]
    externalMetricsPreference: NotRequired[ExternalMetricsPreferenceTypeDef]
    lookBackPeriod: NotRequired[LookBackPeriodPreferenceType]
    utilizationPreferences: NotRequired[Sequence[UtilizationPreferenceTypeDef]]
    preferredResources: NotRequired[Sequence[PreferredResourceTypeDef]]
    savingsEstimationMode: NotRequired[SavingsEstimationModeType]

class RecommendationPreferencesDetailTypeDef(TypedDict):
    scope: NotRequired[ScopeTypeDef]
    resourceType: NotRequired[ResourceTypeType]
    enhancedInfrastructureMetrics: NotRequired[EnhancedInfrastructureMetricsType]
    inferredWorkloadTypes: NotRequired[InferredWorkloadTypesPreferenceType]
    externalMetricsPreference: NotRequired[ExternalMetricsPreferenceTypeDef]
    lookBackPeriod: NotRequired[LookBackPeriodPreferenceType]
    utilizationPreferences: NotRequired[List[UtilizationPreferenceTypeDef]]
    preferredResources: NotRequired[List[EffectivePreferredResourceTypeDef]]
    savingsEstimationMode: NotRequired[SavingsEstimationModeType]

class GetECSServiceRecommendationProjectedMetricsResponseTypeDef(TypedDict):
    recommendedOptionProjectedMetrics: List[ECSServiceRecommendedOptionProjectedMetricTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ECSServiceRecommendationOptionTypeDef(TypedDict):
    memory: NotRequired[int]
    cpu: NotRequired[int]
    savingsOpportunity: NotRequired[SavingsOpportunityTypeDef]
    savingsOpportunityAfterDiscounts: NotRequired[ECSSavingsOpportunityAfterDiscountsTypeDef]
    projectedUtilizationMetrics: NotRequired[List[ECSServiceProjectedUtilizationMetricTypeDef]]
    containerRecommendations: NotRequired[List[ContainerRecommendationTypeDef]]

class LicenseRecommendationOptionTypeDef(TypedDict):
    rank: NotRequired[int]
    operatingSystem: NotRequired[str]
    licenseEdition: NotRequired[LicenseEditionType]
    licenseModel: NotRequired[LicenseModelType]
    savingsOpportunity: NotRequired[SavingsOpportunityTypeDef]

class VolumeRecommendationOptionTypeDef(TypedDict):
    configuration: NotRequired[VolumeConfigurationTypeDef]
    performanceRisk: NotRequired[float]
    rank: NotRequired[int]
    savingsOpportunity: NotRequired[SavingsOpportunityTypeDef]
    savingsOpportunityAfterDiscounts: NotRequired[EBSSavingsOpportunityAfterDiscountsTypeDef]

class RecommendationExportJobTypeDef(TypedDict):
    jobId: NotRequired[str]
    destination: NotRequired[ExportDestinationTypeDef]
    resourceType: NotRequired[ResourceTypeType]
    status: NotRequired[JobStatusType]
    creationTimestamp: NotRequired[datetime]
    lastUpdatedTimestamp: NotRequired[datetime]
    failureReason: NotRequired[str]

class AutoScalingGroupRecommendationOptionTypeDef(TypedDict):
    configuration: NotRequired[AutoScalingGroupConfigurationTypeDef]
    instanceGpuInfo: NotRequired[GpuInfoTypeDef]
    projectedUtilizationMetrics: NotRequired[List[UtilizationMetricTypeDef]]
    performanceRisk: NotRequired[float]
    rank: NotRequired[int]
    savingsOpportunity: NotRequired[SavingsOpportunityTypeDef]
    savingsOpportunityAfterDiscounts: NotRequired[
        AutoScalingGroupSavingsOpportunityAfterDiscountsTypeDef
    ]
    migrationEffort: NotRequired[MigrationEffortType]

class IdleRecommendationTypeDef(TypedDict):
    resourceArn: NotRequired[str]
    resourceId: NotRequired[str]
    resourceType: NotRequired[IdleRecommendationResourceTypeType]
    accountId: NotRequired[str]
    finding: NotRequired[IdleFindingType]
    findingDescription: NotRequired[str]
    savingsOpportunity: NotRequired[IdleSavingsOpportunityTypeDef]
    savingsOpportunityAfterDiscounts: NotRequired[IdleSavingsOpportunityAfterDiscountsTypeDef]
    utilizationMetrics: NotRequired[List[IdleUtilizationMetricTypeDef]]
    lookBackPeriodInDays: NotRequired[float]
    lastRefreshTimestamp: NotRequired[datetime]
    tags: NotRequired[List[TagTypeDef]]

class InstanceRecommendationOptionTypeDef(TypedDict):
    instanceType: NotRequired[str]
    instanceGpuInfo: NotRequired[GpuInfoTypeDef]
    projectedUtilizationMetrics: NotRequired[List[UtilizationMetricTypeDef]]
    platformDifferences: NotRequired[List[PlatformDifferenceType]]
    performanceRisk: NotRequired[float]
    rank: NotRequired[int]
    savingsOpportunity: NotRequired[SavingsOpportunityTypeDef]
    savingsOpportunityAfterDiscounts: NotRequired[InstanceSavingsOpportunityAfterDiscountsTypeDef]
    migrationEffort: NotRequired[MigrationEffortType]

class LambdaFunctionMemoryRecommendationOptionTypeDef(TypedDict):
    rank: NotRequired[int]
    memorySize: NotRequired[int]
    projectedUtilizationMetrics: NotRequired[List[LambdaFunctionMemoryProjectedMetricTypeDef]]
    savingsOpportunity: NotRequired[SavingsOpportunityTypeDef]
    savingsOpportunityAfterDiscounts: NotRequired[LambdaSavingsOpportunityAfterDiscountsTypeDef]

class GetEC2RecommendationProjectedMetricsResponseTypeDef(TypedDict):
    recommendedOptionProjectedMetrics: List[RecommendedOptionProjectedMetricTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRDSDatabaseRecommendationProjectedMetricsResponseTypeDef(TypedDict):
    recommendedOptionProjectedMetrics: List[RDSDatabaseRecommendedOptionProjectedMetricTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RDSDBInstanceRecommendationOptionTypeDef(TypedDict):
    dbInstanceClass: NotRequired[str]
    projectedUtilizationMetrics: NotRequired[List[RDSDBUtilizationMetricTypeDef]]
    performanceRisk: NotRequired[float]
    rank: NotRequired[int]
    savingsOpportunity: NotRequired[SavingsOpportunityTypeDef]
    savingsOpportunityAfterDiscounts: NotRequired[
        RDSInstanceSavingsOpportunityAfterDiscountsTypeDef
    ]

class RDSDBStorageRecommendationOptionTypeDef(TypedDict):
    storageConfiguration: NotRequired[DBStorageConfigurationTypeDef]
    rank: NotRequired[int]
    savingsOpportunity: NotRequired[SavingsOpportunityTypeDef]
    savingsOpportunityAfterDiscounts: NotRequired[RDSStorageSavingsOpportunityAfterDiscountsTypeDef]

class RecommendationSummaryTypeDef(TypedDict):
    summaries: NotRequired[List[SummaryTypeDef]]
    idleSummaries: NotRequired[List[IdleSummaryTypeDef]]
    recommendationResourceType: NotRequired[RecommendationSourceTypeType]
    accountId: NotRequired[str]
    savingsOpportunity: NotRequired[SavingsOpportunityTypeDef]
    idleSavingsOpportunity: NotRequired[SavingsOpportunityTypeDef]
    aggregatedSavingsOpportunity: NotRequired[SavingsOpportunityTypeDef]
    currentPerformanceRiskRatings: NotRequired[CurrentPerformanceRiskRatingsTypeDef]
    inferredWorkloadSavings: NotRequired[List[InferredWorkloadSavingTypeDef]]

class GetRecommendationPreferencesResponseTypeDef(TypedDict):
    recommendationPreferencesDetails: List[RecommendationPreferencesDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ECSServiceRecommendationTypeDef(TypedDict):
    serviceArn: NotRequired[str]
    accountId: NotRequired[str]
    currentServiceConfiguration: NotRequired[ServiceConfigurationTypeDef]
    utilizationMetrics: NotRequired[List[ECSServiceUtilizationMetricTypeDef]]
    lookbackPeriodInDays: NotRequired[float]
    launchType: NotRequired[ECSServiceLaunchTypeType]
    lastRefreshTimestamp: NotRequired[datetime]
    finding: NotRequired[ECSServiceRecommendationFindingType]
    findingReasonCodes: NotRequired[List[ECSServiceRecommendationFindingReasonCodeType]]
    serviceRecommendationOptions: NotRequired[List[ECSServiceRecommendationOptionTypeDef]]
    currentPerformanceRisk: NotRequired[CurrentPerformanceRiskType]
    effectiveRecommendationPreferences: NotRequired[ECSEffectiveRecommendationPreferencesTypeDef]
    tags: NotRequired[List[TagTypeDef]]

class LicenseRecommendationTypeDef(TypedDict):
    resourceArn: NotRequired[str]
    accountId: NotRequired[str]
    currentLicenseConfiguration: NotRequired[LicenseConfigurationTypeDef]
    lookbackPeriodInDays: NotRequired[float]
    lastRefreshTimestamp: NotRequired[datetime]
    finding: NotRequired[LicenseFindingType]
    findingReasonCodes: NotRequired[List[LicenseFindingReasonCodeType]]
    licenseRecommendationOptions: NotRequired[List[LicenseRecommendationOptionTypeDef]]
    tags: NotRequired[List[TagTypeDef]]

class VolumeRecommendationTypeDef(TypedDict):
    volumeArn: NotRequired[str]
    accountId: NotRequired[str]
    currentConfiguration: NotRequired[VolumeConfigurationTypeDef]
    finding: NotRequired[EBSFindingType]
    utilizationMetrics: NotRequired[List[EBSUtilizationMetricTypeDef]]
    lookBackPeriodInDays: NotRequired[float]
    volumeRecommendationOptions: NotRequired[List[VolumeRecommendationOptionTypeDef]]
    lastRefreshTimestamp: NotRequired[datetime]
    currentPerformanceRisk: NotRequired[CurrentPerformanceRiskType]
    effectiveRecommendationPreferences: NotRequired[EBSEffectiveRecommendationPreferencesTypeDef]
    tags: NotRequired[List[TagTypeDef]]

class DescribeRecommendationExportJobsResponseTypeDef(TypedDict):
    recommendationExportJobs: List[RecommendationExportJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AutoScalingGroupRecommendationTypeDef(TypedDict):
    accountId: NotRequired[str]
    autoScalingGroupArn: NotRequired[str]
    autoScalingGroupName: NotRequired[str]
    finding: NotRequired[FindingType]
    utilizationMetrics: NotRequired[List[UtilizationMetricTypeDef]]
    lookBackPeriodInDays: NotRequired[float]
    currentConfiguration: NotRequired[AutoScalingGroupConfigurationTypeDef]
    currentInstanceGpuInfo: NotRequired[GpuInfoTypeDef]
    recommendationOptions: NotRequired[List[AutoScalingGroupRecommendationOptionTypeDef]]
    lastRefreshTimestamp: NotRequired[datetime]
    currentPerformanceRisk: NotRequired[CurrentPerformanceRiskType]
    effectiveRecommendationPreferences: NotRequired[EffectiveRecommendationPreferencesTypeDef]
    inferredWorkloadTypes: NotRequired[List[InferredWorkloadTypeType]]

class GetIdleRecommendationsResponseTypeDef(TypedDict):
    idleRecommendations: List[IdleRecommendationTypeDef]
    errors: List[IdleRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class InstanceRecommendationTypeDef(TypedDict):
    instanceArn: NotRequired[str]
    accountId: NotRequired[str]
    instanceName: NotRequired[str]
    currentInstanceType: NotRequired[str]
    finding: NotRequired[FindingType]
    findingReasonCodes: NotRequired[List[InstanceRecommendationFindingReasonCodeType]]
    utilizationMetrics: NotRequired[List[UtilizationMetricTypeDef]]
    lookBackPeriodInDays: NotRequired[float]
    recommendationOptions: NotRequired[List[InstanceRecommendationOptionTypeDef]]
    recommendationSources: NotRequired[List[RecommendationSourceTypeDef]]
    lastRefreshTimestamp: NotRequired[datetime]
    currentPerformanceRisk: NotRequired[CurrentPerformanceRiskType]
    effectiveRecommendationPreferences: NotRequired[EffectiveRecommendationPreferencesTypeDef]
    inferredWorkloadTypes: NotRequired[List[InferredWorkloadTypeType]]
    instanceState: NotRequired[InstanceStateType]
    tags: NotRequired[List[TagTypeDef]]
    externalMetricStatus: NotRequired[ExternalMetricStatusTypeDef]
    currentInstanceGpuInfo: NotRequired[GpuInfoTypeDef]
    idle: NotRequired[InstanceIdleType]

class LambdaFunctionRecommendationTypeDef(TypedDict):
    functionArn: NotRequired[str]
    functionVersion: NotRequired[str]
    accountId: NotRequired[str]
    currentMemorySize: NotRequired[int]
    numberOfInvocations: NotRequired[int]
    utilizationMetrics: NotRequired[List[LambdaFunctionUtilizationMetricTypeDef]]
    lookbackPeriodInDays: NotRequired[float]
    lastRefreshTimestamp: NotRequired[datetime]
    finding: NotRequired[LambdaFunctionRecommendationFindingType]
    findingReasonCodes: NotRequired[List[LambdaFunctionRecommendationFindingReasonCodeType]]
    memorySizeRecommendationOptions: NotRequired[
        List[LambdaFunctionMemoryRecommendationOptionTypeDef]
    ]
    currentPerformanceRisk: NotRequired[CurrentPerformanceRiskType]
    effectiveRecommendationPreferences: NotRequired[LambdaEffectiveRecommendationPreferencesTypeDef]
    tags: NotRequired[List[TagTypeDef]]

class RDSDBRecommendationTypeDef(TypedDict):
    resourceArn: NotRequired[str]
    accountId: NotRequired[str]
    engine: NotRequired[str]
    engineVersion: NotRequired[str]
    promotionTier: NotRequired[int]
    currentDBInstanceClass: NotRequired[str]
    currentStorageConfiguration: NotRequired[DBStorageConfigurationTypeDef]
    dbClusterIdentifier: NotRequired[str]
    idle: NotRequired[IdleType]
    instanceFinding: NotRequired[RDSInstanceFindingType]
    storageFinding: NotRequired[RDSStorageFindingType]
    instanceFindingReasonCodes: NotRequired[List[RDSInstanceFindingReasonCodeType]]
    currentInstancePerformanceRisk: NotRequired[RDSCurrentInstancePerformanceRiskType]
    storageFindingReasonCodes: NotRequired[List[RDSStorageFindingReasonCodeType]]
    instanceRecommendationOptions: NotRequired[List[RDSDBInstanceRecommendationOptionTypeDef]]
    storageRecommendationOptions: NotRequired[List[RDSDBStorageRecommendationOptionTypeDef]]
    utilizationMetrics: NotRequired[List[RDSDBUtilizationMetricTypeDef]]
    effectiveRecommendationPreferences: NotRequired[RDSEffectiveRecommendationPreferencesTypeDef]
    lookbackPeriodInDays: NotRequired[float]
    lastRefreshTimestamp: NotRequired[datetime]
    tags: NotRequired[List[TagTypeDef]]

class GetRecommendationSummariesResponseTypeDef(TypedDict):
    recommendationSummaries: List[RecommendationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetECSServiceRecommendationsResponseTypeDef(TypedDict):
    ecsServiceRecommendations: List[ECSServiceRecommendationTypeDef]
    errors: List[GetRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetLicenseRecommendationsResponseTypeDef(TypedDict):
    licenseRecommendations: List[LicenseRecommendationTypeDef]
    errors: List[GetRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetEBSVolumeRecommendationsResponseTypeDef(TypedDict):
    volumeRecommendations: List[VolumeRecommendationTypeDef]
    errors: List[GetRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetAutoScalingGroupRecommendationsResponseTypeDef(TypedDict):
    autoScalingGroupRecommendations: List[AutoScalingGroupRecommendationTypeDef]
    errors: List[GetRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetEC2InstanceRecommendationsResponseTypeDef(TypedDict):
    instanceRecommendations: List[InstanceRecommendationTypeDef]
    errors: List[GetRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetLambdaFunctionRecommendationsResponseTypeDef(TypedDict):
    lambdaFunctionRecommendations: List[LambdaFunctionRecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetRDSDatabaseRecommendationsResponseTypeDef(TypedDict):
    rdsDBRecommendations: List[RDSDBRecommendationTypeDef]
    errors: List[GetRecommendationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
