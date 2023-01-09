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
    "ExportableVolumeFieldType",
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
    "InstanceRecommendationFindingReasonCodeType",
    "JobFilterNameType",
    "JobStatusType",
    "LambdaFunctionMemoryMetricNameType",
    "LambdaFunctionMemoryMetricStatisticType",
    "LambdaFunctionMetricNameType",
    "LambdaFunctionMetricStatisticType",
    "LambdaFunctionRecommendationFilterNameType",
    "LambdaFunctionRecommendationFindingReasonCodeType",
    "LambdaFunctionRecommendationFindingType",
    "MetricNameType",
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
    "RecommendationOptionsMemory",
    "RecommendationOptionsMigrationEffort",
    "RecommendationOptionsNetwork",
    "RecommendationOptionsOnDemandPrice",
    "RecommendationOptionsPerformanceRisk",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
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
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsMemoryMaximum",
]
ExportableInstanceFieldType = Literal[
    "AccountId",
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
    "Finding",
    "FindingReasonCodes",
    "InferredWorkloadTypes",
    "InstanceArn",
    "InstanceName",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "RecommendationOptionsInstanceType",
    "RecommendationOptionsMemory",
    "RecommendationOptionsMigrationEffort",
    "RecommendationOptionsNetwork",
    "RecommendationOptionsOnDemandPrice",
    "RecommendationOptionsPerformanceRisk",
    "RecommendationOptionsPlatformDifferences",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "RecommendationOptionsStandardOneYearNoUpfrontReservedPrice",
    "RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice",
    "RecommendationOptionsStorage",
    "RecommendationOptionsVcpus",
    "RecommendationsSourcesRecommendationSourceArn",
    "RecommendationsSourcesRecommendationSourceType",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsDiskReadBytesPerSecondMaximum",
    "UtilizationMetricsDiskReadOpsPerSecondMaximum",
    "UtilizationMetricsDiskWriteBytesPerSecondMaximum",
    "UtilizationMetricsDiskWriteOpsPerSecondMaximum",
    "UtilizationMetricsEbsReadBytesPerSecondMaximum",
    "UtilizationMetricsEbsReadOpsPerSecondMaximum",
    "UtilizationMetricsEbsWriteBytesPerSecondMaximum",
    "UtilizationMetricsEbsWriteOpsPerSecondMaximum",
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
    "UtilizationMetricsDurationAverage",
    "UtilizationMetricsDurationMaximum",
    "UtilizationMetricsMemoryAverage",
    "UtilizationMetricsMemoryMaximum",
]
ExportableVolumeFieldType = Literal[
    "AccountId",
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
    "UtilizationMetricsVolumeReadBytesPerSecondMaximum",
    "UtilizationMetricsVolumeReadOpsPerSecondMaximum",
    "UtilizationMetricsVolumeWriteBytesPerSecondMaximum",
    "UtilizationMetricsVolumeWriteOpsPerSecondMaximum",
    "VolumeArn",
]
ExternalMetricsSourceType = Literal["Datadog", "Dynatrace", "Instana", "NewRelic"]
FileFormatType = Literal["Csv"]
FilterNameType = Literal["Finding", "FindingReasonCodes", "RecommendationSourceType"]
FindingReasonCodeType = Literal["MemoryOverprovisioned", "MemoryUnderprovisioned"]
FindingType = Literal["NotOptimized", "Optimized", "Overprovisioned", "Underprovisioned"]
GetEnrollmentStatusesForOrganizationPaginatorName = Literal[
    "get_enrollment_statuses_for_organization"
]
GetLambdaFunctionRecommendationsPaginatorName = Literal["get_lambda_function_recommendations"]
GetRecommendationPreferencesPaginatorName = Literal["get_recommendation_preferences"]
GetRecommendationSummariesPaginatorName = Literal["get_recommendation_summaries"]
InferredWorkloadTypeType = Literal[
    "AmazonEmr", "ApacheCassandra", "ApacheHadoop", "Memcached", "Nginx", "PostgreSql", "Redis"
]
InferredWorkloadTypesPreferenceType = Literal["Active", "Inactive"]
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
    "MemoryOverprovisioned",
    "MemoryUnderprovisioned",
    "NetworkBandwidthOverprovisioned",
    "NetworkBandwidthUnderprovisioned",
    "NetworkPPSOverprovisioned",
    "NetworkPPSUnderprovisioned",
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
    "Memory",
    "NETWORK_IN_BYTES_PER_SECOND",
    "NETWORK_OUT_BYTES_PER_SECOND",
    "NETWORK_PACKETS_IN_PER_SECOND",
    "NETWORK_PACKETS_OUT_PER_SECOND",
]
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
    "AutoScalingGroup", "EbsVolume", "Ec2Instance", "EcsService", "LambdaFunction"
]
ResourceTypeType = Literal[
    "AutoScalingGroup", "EbsVolume", "Ec2Instance", "EcsService", "LambdaFunction", "NotApplicable"
]
ScopeNameType = Literal["AccountId", "Organization", "ResourceArn"]
StatusType = Literal["Active", "Failed", "Inactive", "Pending"]
