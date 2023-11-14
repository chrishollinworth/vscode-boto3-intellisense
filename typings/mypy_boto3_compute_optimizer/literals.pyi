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
    "DescribeRecommendationExportJobsPaginatorName",
    "EBSFilterNameType",
    "EBSFindingType",
    "EBSMetricNameType",
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
    "InferredWorkloadTypeType",
    "InferredWorkloadTypesPreferenceType",
    "InstanceIdleType",
    "InstanceRecommendationFindingReasonCodeType",
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
    "LicenseEditionType",
    "LicenseFindingReasonCodeType",
    "LicenseFindingType",
    "LicenseModelType",
    "LicenseNameType",
    "LicenseRecommendationFilterNameType",
    "MetricNameType",
    "MetricSourceProviderType",
    "MetricStatisticType",
    "MigrationEffortType",
    "PlatformDifferenceType",
    "RecommendationPreferenceNameType",
    "RecommendationSourceTypeType",
    "ResourceTypeType",
    "ScopeNameType",
    "StatusType",
)

AutoScalingConfigurationType = Literal["TargetTrackingScalingCpu", "TargetTrackingScalingMemory"]
CpuVendorArchitectureType = Literal["AWS_ARM64", "CURRENT"]
CurrencyType = Literal["CNY", "USD"]
CurrentPerformanceRiskType = Literal["High", "Low", "Medium", "VeryLow"]
DescribeRecommendationExportJobsPaginatorName = Literal["describe_recommendation_export_jobs"]
EBSFilterNameType = Literal["Finding"]
EBSFindingType = Literal["NotOptimized", "Optimized"]
EBSMetricNameType = Literal[
    "VolumeReadBytesPerSecond",
    "VolumeReadOpsPerSecond",
    "VolumeWriteBytesPerSecond",
    "VolumeWriteOpsPerSecond",
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
    "Finding",
    "InferredWorkloadTypes",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsConfigurationDesiredCapacity",
    "RecommendationOptionsConfigurationInstanceType",
    "RecommendationOptionsConfigurationMaxSize",
    "RecommendationOptionsConfigurationMinSize",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
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
    "Finding",
    "FindingReasonCodes",
    "LastRefreshTimestamp",
    "LaunchType",
    "LookbackPeriodInDays",
    "RecommendationOptionsContainerRecommendations",
    "RecommendationOptionsCpu",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "RecommendationOptionsMemory",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
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
    "RecommendationOptionsEstimatedMonthlySavingsValue",
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
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "RecommendationOptionsProjectedUtilizationMetricsDurationExpected",
    "RecommendationOptionsProjectedUtilizationMetricsDurationLowerBound",
    "RecommendationOptionsProjectedUtilizationMetricsDurationUpperBound",
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
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "RecommendationOptionsMonthlyPrice",
    "RecommendationOptionsPerformanceRisk",
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
RecommendationPreferenceNameType = Literal[
    "EnhancedInfrastructureMetrics", "ExternalMetricsPreference", "InferredWorkloadTypes"
]
RecommendationSourceTypeType = Literal[
    "AutoScalingGroup", "EbsVolume", "Ec2Instance", "EcsService", "LambdaFunction", "License"
]
ResourceTypeType = Literal[
    "AutoScalingGroup",
    "EbsVolume",
    "Ec2Instance",
    "EcsService",
    "LambdaFunction",
    "License",
    "NotApplicable",
]
ScopeNameType = Literal["AccountId", "Organization", "ResourceArn"]
StatusType = Literal["Active", "Failed", "Inactive", "Pending"]
