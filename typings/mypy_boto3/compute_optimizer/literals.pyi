"""
Type annotations for compute-optimizer service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/literals.html)

Usage::

    ```python
    from mypy_boto3_compute_optimizer.literals import EBSFilterNameType

    data: EBSFilterNameType = "Finding"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "EBSFilterNameType",
    "EBSFindingType",
    "EBSMetricNameType",
    "ExportableAutoScalingGroupFieldType",
    "ExportableInstanceFieldType",
    "ExportableLambdaFunctionFieldType",
    "ExportableVolumeFieldType",
    "FileFormatType",
    "FilterNameType",
    "FindingReasonCodeType",
    "FindingType",
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
    "PlatformDifferenceType",
    "RecommendationSourceTypeType",
    "ResourceTypeType",
    "StatusType",
)

EBSFilterNameType = Literal["Finding"]
EBSFindingType = Literal["NotOptimized", "Optimized"]
EBSMetricNameType = Literal[
    "VolumeReadBytesPerSecond",
    "VolumeReadOpsPerSecond",
    "VolumeWriteBytesPerSecond",
    "VolumeWriteOpsPerSecond",
]
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
    "CurrentStandardOneYearNoUpfrontReservedPrice",
    "CurrentStandardThreeYearNoUpfrontReservedPrice",
    "CurrentStorage",
    "CurrentVCpus",
    "Finding",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsConfigurationDesiredCapacity",
    "RecommendationOptionsConfigurationInstanceType",
    "RecommendationOptionsConfigurationMaxSize",
    "RecommendationOptionsConfigurationMinSize",
    "RecommendationOptionsMemory",
    "RecommendationOptionsNetwork",
    "RecommendationOptionsOnDemandPrice",
    "RecommendationOptionsPerformanceRisk",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
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
ExportableInstanceFieldType = Literal[
    "AccountId",
    "CurrentInstanceType",
    "CurrentMemory",
    "CurrentNetwork",
    "CurrentOnDemandPrice",
    "CurrentStandardOneYearNoUpfrontReservedPrice",
    "CurrentStandardThreeYearNoUpfrontReservedPrice",
    "CurrentStorage",
    "CurrentVCpus",
    "Finding",
    "FindingReasonCodes",
    "InstanceArn",
    "InstanceName",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsInstanceType",
    "RecommendationOptionsMemory",
    "RecommendationOptionsNetwork",
    "RecommendationOptionsOnDemandPrice",
    "RecommendationOptionsPerformanceRisk",
    "RecommendationOptionsPlatformDifferences",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
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
    "RecommendationOptionsProjectedUtilizationMetricsDurationExpected",
    "RecommendationOptionsProjectedUtilizationMetricsDurationLowerBound",
    "RecommendationOptionsProjectedUtilizationMetricsDurationUpperBound",
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
    "Finding",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsConfigurationVolumeBaselineIOPS",
    "RecommendationOptionsConfigurationVolumeBaselineThroughput",
    "RecommendationOptionsConfigurationVolumeBurstIOPS",
    "RecommendationOptionsConfigurationVolumeBurstThroughput",
    "RecommendationOptionsConfigurationVolumeSize",
    "RecommendationOptionsConfigurationVolumeType",
    "RecommendationOptionsMonthlyPrice",
    "RecommendationOptionsPerformanceRisk",
    "UtilizationMetricsVolumeReadBytesPerSecondMaximum",
    "UtilizationMetricsVolumeReadOpsPerSecondMaximum",
    "UtilizationMetricsVolumeWriteBytesPerSecondMaximum",
    "UtilizationMetricsVolumeWriteOpsPerSecondMaximum",
    "VolumeArn",
]
FileFormatType = Literal["Csv"]
FilterNameType = Literal["Finding", "FindingReasonCodes", "RecommendationSourceType"]
FindingReasonCodeType = Literal["MemoryOverprovisioned", "MemoryUnderprovisioned"]
FindingType = Literal["NotOptimized", "Optimized", "Overprovisioned", "Underprovisioned"]
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
PlatformDifferenceType = Literal[
    "Hypervisor",
    "InstanceStoreAvailability",
    "NetworkInterface",
    "StorageInterface",
    "VirtualizationType",
]
RecommendationSourceTypeType = Literal[
    "AutoScalingGroup", "EbsVolume", "Ec2Instance", "LambdaFunction"
]
ResourceTypeType = Literal["AutoScalingGroup", "EbsVolume", "Ec2Instance", "LambdaFunction"]
StatusType = Literal["Active", "Failed", "Inactive", "Pending"]
