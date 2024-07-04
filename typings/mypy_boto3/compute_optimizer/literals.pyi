"""
Type annotations for compute-optimizer service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/literals.html)

Usage::

    ```python
    from mypy_boto3_compute_optimizer.literals import AutoScalingConfigurationType

    data: AutoScalingConfigurationType = "TargetTrackingScalingCpu"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AutoScalingConfigurationType",
    "CpuVendorArchitectureType",
    "CurrencyType",
    "CurrentPerformanceRiskType",
    "CustomizableMetricHeadroomType",
    "CustomizableMetricNameType",
    "CustomizableMetricThresholdType",
    "DescribeRecommendationExportJobsPaginatorName",
    "EBSFilterNameType",
    "EBSFindingType",
    "EBSMetricNameType",
    "EBSSavingsEstimationModeSourceType",
    "ECSSavingsEstimationModeSourceType",
    "ECSServiceLaunchTypeType",
    "ECSServiceMetricNameType",
    "ECSServiceMetricStatisticType",
    "ECSServiceRecommendationFilterNameType",
    "ECSServiceRecommendationFindingReasonCodeType",
    "ECSServiceRecommendationFindingType",
    "EnhancedInfrastructureMetricsType",
    "EnrollmentFilterNameType",
    "ExportableAutoScalingGroupFieldType",
    "ExportableECSServiceFieldType",
    "ExportableInstanceFieldType",
    "ExportableLambdaFunctionFieldType",
    "ExportableLicenseFieldType",
    "ExportableRDSDBFieldType",
    "ExportableVolumeFieldType",
    "ExternalMetricStatusCodeType",
    "ExternalMetricsSourceType",
    "FileFormatType",
    "FilterNameType",
    "FindingReasonCodeType",
    "FindingType",
    "GetEnrollmentStatusesForOrganizationPaginatorName",
    "GetLambdaFunctionRecommendationsPaginatorName",
    "GetRecommendationPreferencesPaginatorName",
    "GetRecommendationSummariesPaginatorName",
    "IdleType",
    "InferredWorkloadTypeType",
    "InferredWorkloadTypesPreferenceType",
    "InstanceIdleType",
    "InstanceRecommendationFindingReasonCodeType",
    "InstanceSavingsEstimationModeSourceType",
    "InstanceStateType",
    "JobFilterNameType",
    "JobStatusType",
    "LambdaFunctionMemoryMetricNameType",
    "LambdaFunctionMemoryMetricStatisticType",
    "LambdaFunctionMetricNameType",
    "LambdaFunctionMetricStatisticType",
    "LambdaFunctionRecommendationFilterNameType",
    "LambdaFunctionRecommendationFindingReasonCodeType",
    "LambdaFunctionRecommendationFindingType",
    "LambdaSavingsEstimationModeSourceType",
    "LicenseEditionType",
    "LicenseFindingReasonCodeType",
    "LicenseFindingType",
    "LicenseModelType",
    "LicenseNameType",
    "LicenseRecommendationFilterNameType",
    "LookBackPeriodPreferenceType",
    "MetricNameType",
    "MetricSourceProviderType",
    "MetricStatisticType",
    "MigrationEffortType",
    "PlatformDifferenceType",
    "PreferredResourceNameType",
    "RDSDBMetricNameType",
    "RDSDBMetricStatisticType",
    "RDSDBRecommendationFilterNameType",
    "RDSInstanceFindingReasonCodeType",
    "RDSInstanceFindingType",
    "RDSSavingsEstimationModeSourceType",
    "RDSStorageFindingReasonCodeType",
    "RDSStorageFindingType",
    "RecommendationPreferenceNameType",
    "RecommendationSourceTypeType",
    "ResourceTypeType",
    "SavingsEstimationModeType",
    "ScopeNameType",
    "StatusType",
)

AutoScalingConfigurationType = Literal["TargetTrackingScalingCpu", "TargetTrackingScalingMemory"]
CpuVendorArchitectureType = Literal["AWS_ARM64", "CURRENT"]
CurrencyType = Literal["CNY", "USD"]
CurrentPerformanceRiskType = Literal["High", "Low", "Medium", "VeryLow"]
CustomizableMetricHeadroomType = Literal["PERCENT_0", "PERCENT_10", "PERCENT_20", "PERCENT_30"]
CustomizableMetricNameType = Literal["CpuUtilization", "MemoryUtilization"]
CustomizableMetricThresholdType = Literal["P90", "P95", "P99_5"]
DescribeRecommendationExportJobsPaginatorName = Literal["describe_recommendation_export_jobs"]
EBSFilterNameType = Literal["Finding"]
EBSFindingType = Literal["NotOptimized", "Optimized"]
EBSMetricNameType = Literal[
    "VolumeReadBytesPerSecond",
    "VolumeReadOpsPerSecond",
    "VolumeWriteBytesPerSecond",
    "VolumeWriteOpsPerSecond",
]
EBSSavingsEstimationModeSourceType = Literal[
    "CostExplorerRightsizing", "CostOptimizationHub", "PublicPricing"
]
ECSSavingsEstimationModeSourceType = Literal[
    "CostExplorerRightsizing", "CostOptimizationHub", "PublicPricing"
]
ECSServiceLaunchTypeType = Literal["EC2", "Fargate"]
ECSServiceMetricNameType = Literal["Cpu", "Memory"]
ECSServiceMetricStatisticType = Literal["Average", "Maximum"]
ECSServiceRecommendationFilterNameType = Literal["Finding", "FindingReasonCode"]
ECSServiceRecommendationFindingReasonCodeType = Literal[
    "CPUOverprovisioned", "CPUUnderprovisioned", "MemoryOverprovisioned", "MemoryUnderprovisioned"
]
ECSServiceRecommendationFindingType = Literal["Optimized", "Overprovisioned", "Underprovisioned"]
EnhancedInfrastructureMetricsType = Literal["Active", "Inactive"]
EnrollmentFilterNameType = Literal["Status"]
ExportableAutoScalingGroupFieldType = Literal[
    "AccountId",
    "AutoScalingGroupArn",
    "AutoScalingGroupName",
    "CurrentConfigurationDesiredCapacity",
    "CurrentConfigurationInstanceType",
    "CurrentConfigurationMaxSize",
    "CurrentConfigurationMinSize",
    "CurrentInstanceGpuInfo",
    "CurrentMemory",
    "CurrentNetwork",
    "CurrentOnDemandPrice",
    "CurrentPerformanceRisk",
    "CurrentStandardOneYearNoUpfrontReservedPrice",
    "CurrentStandardThreeYearNoUpfrontReservedPrice",
    "CurrentStorage",
    "CurrentVCpus",
    "EffectiveRecommendationPreferencesCpuVendorArchitectures",
    "EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics",
    "EffectiveRecommendationPreferencesInferredWorkloadTypes",
    "EffectiveRecommendationPreferencesLookBackPeriod",
    "EffectiveRecommendationPreferencesPreferredResources",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "Finding",
    "InferredWorkloadTypes",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsConfigurationDesiredCapacity",
    "RecommendationOptionsConfigurationInstanceType",
    "RecommendationOptionsConfigurationMaxSize",
    "RecommendationOptionsConfigurationMinSize",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    "RecommendationOptionsInstanceGpuInfo",
    "RecommendationOptionsMemory",
    "RecommendationOptionsMigrationEffort",
    "RecommendationOptionsNetwork",
    "RecommendationOptionsOnDemandPrice",
    "RecommendationOptionsPerformanceRisk",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsGpuMemoryPercentageMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsGpuPercentageMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
    "RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "RecommendationOptionsStandardOneYearNoUpfrontReservedPrice",
    "RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice",
    "RecommendationOptionsStorage",
    "RecommendationOptionsVcpus",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsDiskReadBytesPerSecondMaximum",
    "UtilizationMetricsDiskReadOpsPerSecondMaximum",
    "UtilizationMetricsDiskWriteBytesPerSecondMaximum",
    "UtilizationMetricsDiskWriteOpsPerSecondMaximum",
    "UtilizationMetricsEbsReadBytesPerSecondMaximum",
    "UtilizationMetricsEbsReadOpsPerSecondMaximum",
    "UtilizationMetricsEbsWriteBytesPerSecondMaximum",
    "UtilizationMetricsEbsWriteOpsPerSecondMaximum",
    "UtilizationMetricsGpuMemoryPercentageMaximum",
    "UtilizationMetricsGpuPercentageMaximum",
    "UtilizationMetricsMemoryMaximum",
    "UtilizationMetricsNetworkInBytesPerSecondMaximum",
    "UtilizationMetricsNetworkOutBytesPerSecondMaximum",
    "UtilizationMetricsNetworkPacketsInPerSecondMaximum",
    "UtilizationMetricsNetworkPacketsOutPerSecondMaximum",
]
ExportableECSServiceFieldType = Literal[
    "AccountId",
    "CurrentPerformanceRisk",
    "CurrentServiceConfigurationAutoScalingConfiguration",
    "CurrentServiceConfigurationCpu",
    "CurrentServiceConfigurationMemory",
    "CurrentServiceConfigurationTaskDefinitionArn",
    "CurrentServiceContainerConfigurations",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "Finding",
    "FindingReasonCodes",
    "LastRefreshTimestamp",
    "LaunchType",
    "LookbackPeriodInDays",
    "RecommendationOptionsContainerRecommendations",
    "RecommendationOptionsCpu",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    "RecommendationOptionsMemory",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
    "RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "ServiceArn",
    "Tags",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsMemoryMaximum",
]
ExportableInstanceFieldType = Literal[
    "AccountId",
    "CurrentInstanceGpuInfo",
    "CurrentInstanceType",
    "CurrentMemory",
    "CurrentNetwork",
    "CurrentOnDemandPrice",
    "CurrentPerformanceRisk",
    "CurrentStandardOneYearNoUpfrontReservedPrice",
    "CurrentStandardThreeYearNoUpfrontReservedPrice",
    "CurrentStorage",
    "CurrentVCpus",
    "EffectiveRecommendationPreferencesCpuVendorArchitectures",
    "EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics",
    "EffectiveRecommendationPreferencesExternalMetricsSource",
    "EffectiveRecommendationPreferencesInferredWorkloadTypes",
    "EffectiveRecommendationPreferencesLookBackPeriod",
    "EffectiveRecommendationPreferencesPreferredResources",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "EffectiveRecommendationPreferencesUtilizationPreferences",
    "ExternalMetricStatusCode",
    "ExternalMetricStatusReason",
    "Finding",
    "FindingReasonCodes",
    "Idle",
    "InferredWorkloadTypes",
    "InstanceArn",
    "InstanceName",
    "InstanceState",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    "RecommendationOptionsInstanceGpuInfo",
    "RecommendationOptionsInstanceType",
    "RecommendationOptionsMemory",
    "RecommendationOptionsMigrationEffort",
    "RecommendationOptionsNetwork",
    "RecommendationOptionsOnDemandPrice",
    "RecommendationOptionsPerformanceRisk",
    "RecommendationOptionsPlatformDifferences",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsGpuMemoryPercentageMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsGpuPercentageMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
    "RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "RecommendationOptionsStandardOneYearNoUpfrontReservedPrice",
    "RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice",
    "RecommendationOptionsStorage",
    "RecommendationOptionsVcpus",
    "RecommendationsSourcesRecommendationSourceArn",
    "RecommendationsSourcesRecommendationSourceType",
    "Tags",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsDiskReadBytesPerSecondMaximum",
    "UtilizationMetricsDiskReadOpsPerSecondMaximum",
    "UtilizationMetricsDiskWriteBytesPerSecondMaximum",
    "UtilizationMetricsDiskWriteOpsPerSecondMaximum",
    "UtilizationMetricsEbsReadBytesPerSecondMaximum",
    "UtilizationMetricsEbsReadOpsPerSecondMaximum",
    "UtilizationMetricsEbsWriteBytesPerSecondMaximum",
    "UtilizationMetricsEbsWriteOpsPerSecondMaximum",
    "UtilizationMetricsGpuMemoryPercentageMaximum",
    "UtilizationMetricsGpuPercentageMaximum",
    "UtilizationMetricsMemoryMaximum",
    "UtilizationMetricsNetworkInBytesPerSecondMaximum",
    "UtilizationMetricsNetworkOutBytesPerSecondMaximum",
    "UtilizationMetricsNetworkPacketsInPerSecondMaximum",
    "UtilizationMetricsNetworkPacketsOutPerSecondMaximum",
]
ExportableLambdaFunctionFieldType = Literal[
    "AccountId",
    "CurrentConfigurationMemorySize",
    "CurrentConfigurationTimeout",
    "CurrentCostAverage",
    "CurrentCostTotal",
    "CurrentPerformanceRisk",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "Finding",
    "FindingReasonCodes",
    "FunctionArn",
    "FunctionVersion",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "NumberOfInvocations",
    "RecommendationOptionsConfigurationMemorySize",
    "RecommendationOptionsCostHigh",
    "RecommendationOptionsCostLow",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    "RecommendationOptionsProjectedUtilizationMetricsDurationExpected",
    "RecommendationOptionsProjectedUtilizationMetricsDurationLowerBound",
    "RecommendationOptionsProjectedUtilizationMetricsDurationUpperBound",
    "RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "Tags",
    "UtilizationMetricsDurationAverage",
    "UtilizationMetricsDurationMaximum",
    "UtilizationMetricsMemoryAverage",
    "UtilizationMetricsMemoryMaximum",
]
ExportableLicenseFieldType = Literal[
    "AccountId",
    "CurrentLicenseConfigurationInstanceType",
    "CurrentLicenseConfigurationLicenseEdition",
    "CurrentLicenseConfigurationLicenseModel",
    "CurrentLicenseConfigurationLicenseName",
    "CurrentLicenseConfigurationLicenseVersion",
    "CurrentLicenseConfigurationMetricsSource",
    "CurrentLicenseConfigurationNumberOfCores",
    "CurrentLicenseConfigurationOperatingSystem",
    "Finding",
    "FindingReasonCodes",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "RecommendationOptionsLicenseEdition",
    "RecommendationOptionsLicenseModel",
    "RecommendationOptionsOperatingSystem",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "ResourceArn",
    "Tags",
]
ExportableRDSDBFieldType = Literal[
    "AccountId",
    "CurrentDBInstanceClass",
    "CurrentInstanceOnDemandHourlyPrice",
    "CurrentStorageConfigurationAllocatedStorage",
    "CurrentStorageConfigurationIOPS",
    "CurrentStorageConfigurationMaxAllocatedStorage",
    "CurrentStorageConfigurationStorageThroughput",
    "CurrentStorageConfigurationStorageType",
    "CurrentStorageOnDemandMonthlyPrice",
    "EffectiveRecommendationPreferencesCpuVendorArchitectures",
    "EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics",
    "EffectiveRecommendationPreferencesLookBackPeriod",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "Engine",
    "EngineVersion",
    "Idle",
    "InstanceFinding",
    "InstanceFindingReasonCodes",
    "InstanceRecommendationOptionsDBInstanceClass",
    "InstanceRecommendationOptionsEstimatedMonthlySavingsCurrency",
    "InstanceRecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "InstanceRecommendationOptionsEstimatedMonthlySavingsValue",
    "InstanceRecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    "InstanceRecommendationOptionsInstanceOnDemandHourlyPrice",
    "InstanceRecommendationOptionsPerformanceRisk",
    "InstanceRecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "InstanceRecommendationOptionsRank",
    "InstanceRecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "InstanceRecommendationOptionsSavingsOpportunityPercentage",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "MultiAZDBInstance",
    "ResourceArn",
    "StorageFinding",
    "StorageFindingReasonCodes",
    "StorageRecommendationOptionsAllocatedStorage",
    "StorageRecommendationOptionsEstimatedMonthlySavingsCurrency",
    "StorageRecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "StorageRecommendationOptionsEstimatedMonthlySavingsValue",
    "StorageRecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    "StorageRecommendationOptionsIOPS",
    "StorageRecommendationOptionsMaxAllocatedStorage",
    "StorageRecommendationOptionsOnDemandMonthlyPrice",
    "StorageRecommendationOptionsRank",
    "StorageRecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "StorageRecommendationOptionsSavingsOpportunityPercentage",
    "StorageRecommendationOptionsStorageThroughput",
    "StorageRecommendationOptionsStorageType",
    "Tags",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsDatabaseConnectionsMaximum",
    "UtilizationMetricsEBSVolumeReadIOPSMaximum",
    "UtilizationMetricsEBSVolumeReadThroughputMaximum",
    "UtilizationMetricsEBSVolumeStorageSpaceUtilizationMaximum",
    "UtilizationMetricsEBSVolumeWriteIOPSMaximum",
    "UtilizationMetricsEBSVolumeWriteThroughputMaximum",
    "UtilizationMetricsMemoryMaximum",
    "UtilizationMetricsNetworkReceiveThroughputMaximum",
    "UtilizationMetricsNetworkTransmitThroughputMaximum",
]
ExportableVolumeFieldType = Literal[
    "AccountId",
    "CurrentConfigurationRootVolume",
    "CurrentConfigurationVolumeBaselineIOPS",
    "CurrentConfigurationVolumeBaselineThroughput",
    "CurrentConfigurationVolumeBurstIOPS",
    "CurrentConfigurationVolumeBurstThroughput",
    "CurrentConfigurationVolumeSize",
    "CurrentConfigurationVolumeType",
    "CurrentMonthlyPrice",
    "CurrentPerformanceRisk",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "Finding",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsConfigurationVolumeBaselineIOPS",
    "RecommendationOptionsConfigurationVolumeBaselineThroughput",
    "RecommendationOptionsConfigurationVolumeBurstIOPS",
    "RecommendationOptionsConfigurationVolumeBurstThroughput",
    "RecommendationOptionsConfigurationVolumeSize",
    "RecommendationOptionsConfigurationVolumeType",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    "RecommendationOptionsMonthlyPrice",
    "RecommendationOptionsPerformanceRisk",
    "RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "RootVolume",
    "Tags",
    "UtilizationMetricsVolumeReadBytesPerSecondMaximum",
    "UtilizationMetricsVolumeReadOpsPerSecondMaximum",
    "UtilizationMetricsVolumeWriteBytesPerSecondMaximum",
    "UtilizationMetricsVolumeWriteOpsPerSecondMaximum",
    "VolumeArn",
]
ExternalMetricStatusCodeType = Literal[
    "DATADOG_INTEGRATION_ERROR",
    "DYNATRACE_INTEGRATION_ERROR",
    "INSTANA_INTEGRATION_ERROR",
    "INSUFFICIENT_DATADOG_METRICS",
    "INSUFFICIENT_DYNATRACE_METRICS",
    "INSUFFICIENT_INSTANA_METRICS",
    "INSUFFICIENT_NEWRELIC_METRICS",
    "INTEGRATION_SUCCESS",
    "NEWRELIC_INTEGRATION_ERROR",
    "NO_EXTERNAL_METRIC_SET",
]
ExternalMetricsSourceType = Literal["Datadog", "Dynatrace", "Instana", "NewRelic"]
FileFormatType = Literal["Csv"]
FilterNameType = Literal[
    "Finding", "FindingReasonCodes", "InferredWorkloadTypes", "RecommendationSourceType"
]
FindingReasonCodeType = Literal["MemoryOverprovisioned", "MemoryUnderprovisioned"]
FindingType = Literal["NotOptimized", "Optimized", "Overprovisioned", "Underprovisioned"]
GetEnrollmentStatusesForOrganizationPaginatorName = Literal[
    "get_enrollment_statuses_for_organization"
]
GetLambdaFunctionRecommendationsPaginatorName = Literal["get_lambda_function_recommendations"]
GetRecommendationPreferencesPaginatorName = Literal["get_recommendation_preferences"]
GetRecommendationSummariesPaginatorName = Literal["get_recommendation_summaries"]
IdleType = Literal["False", "True"]
InferredWorkloadTypeType = Literal[
    "AmazonEmr",
    "ApacheCassandra",
    "ApacheHadoop",
    "Kafka",
    "Memcached",
    "Nginx",
    "PostgreSql",
    "Redis",
    "SQLServer",
]
InferredWorkloadTypesPreferenceType = Literal["Active", "Inactive"]
InstanceIdleType = Literal["False", "True"]
InstanceRecommendationFindingReasonCodeType = Literal[
    "CPUOverprovisioned",
    "CPUUnderprovisioned",
    "DiskIOPSOverprovisioned",
    "DiskIOPSUnderprovisioned",
    "DiskThroughputOverprovisioned",
    "DiskThroughputUnderprovisioned",
    "EBSIOPSOverprovisioned",
    "EBSIOPSUnderprovisioned",
    "EBSThroughputOverprovisioned",
    "EBSThroughputUnderprovisioned",
    "GPUMemoryOverprovisioned",
    "GPUMemoryUnderprovisioned",
    "GPUOverprovisioned",
    "GPUUnderprovisioned",
    "MemoryOverprovisioned",
    "MemoryUnderprovisioned",
    "NetworkBandwidthOverprovisioned",
    "NetworkBandwidthUnderprovisioned",
    "NetworkPPSOverprovisioned",
    "NetworkPPSUnderprovisioned",
]
InstanceSavingsEstimationModeSourceType = Literal[
    "CostExplorerRightsizing", "CostOptimizationHub", "PublicPricing"
]
InstanceStateType = Literal[
    "pending", "running", "shutting-down", "stopped", "stopping", "terminated"
]
JobFilterNameType = Literal["JobStatus", "ResourceType"]
JobStatusType = Literal["Complete", "Failed", "InProgress", "Queued"]
LambdaFunctionMemoryMetricNameType = Literal["Duration"]
LambdaFunctionMemoryMetricStatisticType = Literal["Expected", "LowerBound", "UpperBound"]
LambdaFunctionMetricNameType = Literal["Duration", "Memory"]
LambdaFunctionMetricStatisticType = Literal["Average", "Maximum"]
LambdaFunctionRecommendationFilterNameType = Literal["Finding", "FindingReasonCode"]
LambdaFunctionRecommendationFindingReasonCodeType = Literal[
    "Inconclusive", "InsufficientData", "MemoryOverprovisioned", "MemoryUnderprovisioned"
]
LambdaFunctionRecommendationFindingType = Literal["NotOptimized", "Optimized", "Unavailable"]
LambdaSavingsEstimationModeSourceType = Literal[
    "CostExplorerRightsizing", "CostOptimizationHub", "PublicPricing"
]
LicenseEditionType = Literal["Enterprise", "Free", "NoLicenseEditionFound", "Standard"]
LicenseFindingReasonCodeType = Literal[
    "CloudWatchApplicationInsightsError",
    "InvalidCloudWatchApplicationInsightsSetup",
    "LicenseOverprovisioned",
    "Optimized",
]
LicenseFindingType = Literal["InsufficientMetrics", "NotOptimized", "Optimized"]
LicenseModelType = Literal["BringYourOwnLicense", "LicenseIncluded"]
LicenseNameType = Literal["SQLServer"]
LicenseRecommendationFilterNameType = Literal["Finding", "FindingReasonCode", "LicenseName"]
LookBackPeriodPreferenceType = Literal["DAYS_14", "DAYS_32", "DAYS_93"]
MetricNameType = Literal[
    "Cpu",
    "DISK_READ_BYTES_PER_SECOND",
    "DISK_READ_OPS_PER_SECOND",
    "DISK_WRITE_BYTES_PER_SECOND",
    "DISK_WRITE_OPS_PER_SECOND",
    "EBS_READ_BYTES_PER_SECOND",
    "EBS_READ_OPS_PER_SECOND",
    "EBS_WRITE_BYTES_PER_SECOND",
    "EBS_WRITE_OPS_PER_SECOND",
    "GPU_MEMORY_PERCENTAGE",
    "GPU_PERCENTAGE",
    "Memory",
    "NETWORK_IN_BYTES_PER_SECOND",
    "NETWORK_OUT_BYTES_PER_SECOND",
    "NETWORK_PACKETS_IN_PER_SECOND",
    "NETWORK_PACKETS_OUT_PER_SECOND",
]
MetricSourceProviderType = Literal["CloudWatchApplicationInsights"]
MetricStatisticType = Literal["Average", "Maximum"]
MigrationEffortType = Literal["High", "Low", "Medium", "VeryLow"]
PlatformDifferenceType = Literal[
    "Architecture",
    "Hypervisor",
    "InstanceStoreAvailability",
    "NetworkInterface",
    "StorageInterface",
    "VirtualizationType",
]
PreferredResourceNameType = Literal["Ec2InstanceTypes"]
RDSDBMetricNameType = Literal[
    "CPU",
    "DatabaseConnections",
    "EBSVolumeReadIOPS",
    "EBSVolumeReadThroughput",
    "EBSVolumeStorageSpaceUtilization",
    "EBSVolumeWriteIOPS",
    "EBSVolumeWriteThroughput",
    "Memory",
    "NetworkReceiveThroughput",
    "NetworkTransmitThroughput",
]
RDSDBMetricStatisticType = Literal["Average", "Maximum", "Minimum"]
RDSDBRecommendationFilterNameType = Literal[
    "Idle",
    "InstanceFinding",
    "InstanceFindingReasonCode",
    "StorageFinding",
    "StorageFindingReasonCode",
]
RDSInstanceFindingReasonCodeType = Literal[
    "CPUOverprovisioned",
    "CPUUnderprovisioned",
    "EBSIOPSOverprovisioned",
    "EBSThroughputOverprovisioned",
    "EBSThroughputUnderprovisioned",
    "NetworkBandwidthOverprovisioned",
    "NetworkBandwidthUnderprovisioned",
    "NewEngineVersionAvailable",
    "NewGenerationDBInstanceClassAvailable",
]
RDSInstanceFindingType = Literal["Optimized", "Overprovisioned", "Underprovisioned"]
RDSSavingsEstimationModeSourceType = Literal[
    "CostExplorerRightsizing", "CostOptimizationHub", "PublicPricing"
]
RDSStorageFindingReasonCodeType = Literal[
    "EBSVolumeAllocatedStorageUnderprovisioned",
    "EBSVolumeIOPSOverprovisioned",
    "EBSVolumeThroughputOverprovisioned",
    "EBSVolumeThroughputUnderprovisioned",
    "NewGenerationStorageTypeAvailable",
]
RDSStorageFindingType = Literal["Optimized", "Overprovisioned", "Underprovisioned"]
RecommendationPreferenceNameType = Literal[
    "EnhancedInfrastructureMetrics",
    "ExternalMetricsPreference",
    "InferredWorkloadTypes",
    "LookBackPeriodPreference",
    "PreferredResources",
    "UtilizationPreferences",
]
RecommendationSourceTypeType = Literal[
    "AutoScalingGroup",
    "EbsVolume",
    "Ec2Instance",
    "EcsService",
    "LambdaFunction",
    "License",
    "RdsDBInstance",
    "RdsDBInstanceStorage",
]
ResourceTypeType = Literal[
    "AutoScalingGroup",
    "EbsVolume",
    "Ec2Instance",
    "EcsService",
    "LambdaFunction",
    "License",
    "NotApplicable",
    "RdsDBInstance",
]
SavingsEstimationModeType = Literal["AfterDiscounts", "BeforeDiscounts"]
ScopeNameType = Literal["AccountId", "Organization", "ResourceArn"]
StatusType = Literal["Active", "Failed", "Inactive", "Pending"]
