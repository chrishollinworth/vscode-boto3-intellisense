"""
Main interface for compute-optimizer service type definitions.

Usage::

    ```python
    from mypy_boto3_compute_optimizer.type_defs import AutoScalingGroupConfigurationTypeDef

    data: AutoScalingGroupConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AutoScalingGroupConfigurationTypeDef",
    "AutoScalingGroupRecommendationOptionTypeDef",
    "AutoScalingGroupRecommendationTypeDef",
    "EBSUtilizationMetricTypeDef",
    "ExportDestinationTypeDef",
    "GetRecommendationErrorTypeDef",
    "InstanceRecommendationOptionTypeDef",
    "InstanceRecommendationTypeDef",
    "LambdaFunctionMemoryProjectedMetricTypeDef",
    "LambdaFunctionMemoryRecommendationOptionTypeDef",
    "LambdaFunctionRecommendationTypeDef",
    "LambdaFunctionUtilizationMetricTypeDef",
    "ProjectedMetricTypeDef",
    "ReasonCodeSummaryTypeDef",
    "RecommendationExportJobTypeDef",
    "RecommendationSourceTypeDef",
    "RecommendationSummaryTypeDef",
    "RecommendedOptionProjectedMetricTypeDef",
    "S3DestinationTypeDef",
    "SummaryTypeDef",
    "UtilizationMetricTypeDef",
    "VolumeConfigurationTypeDef",
    "VolumeRecommendationOptionTypeDef",
    "VolumeRecommendationTypeDef",
    "DescribeRecommendationExportJobsResponseTypeDef",
    "EBSFilterTypeDef",
    "ExportAutoScalingGroupRecommendationsResponseTypeDef",
    "ExportEC2InstanceRecommendationsResponseTypeDef",
    "FilterTypeDef",
    "GetAutoScalingGroupRecommendationsResponseTypeDef",
    "GetEBSVolumeRecommendationsResponseTypeDef",
    "GetEC2InstanceRecommendationsResponseTypeDef",
    "GetEC2RecommendationProjectedMetricsResponseTypeDef",
    "GetEnrollmentStatusResponseTypeDef",
    "GetLambdaFunctionRecommendationsResponseTypeDef",
    "GetRecommendationSummariesResponseTypeDef",
    "JobFilterTypeDef",
    "LambdaFunctionRecommendationFilterTypeDef",
    "S3DestinationConfigTypeDef",
    "UpdateEnrollmentStatusResponseTypeDef",
)

AutoScalingGroupConfigurationTypeDef = TypedDict(
    "AutoScalingGroupConfigurationTypeDef",
    {"desiredCapacity": int, "minSize": int, "maxSize": int, "instanceType": str},
    total=False,
)

AutoScalingGroupRecommendationOptionTypeDef = TypedDict(
    "AutoScalingGroupRecommendationOptionTypeDef",
    {
        "configuration": "AutoScalingGroupConfigurationTypeDef",
        "projectedUtilizationMetrics": List["UtilizationMetricTypeDef"],
        "performanceRisk": float,
        "rank": int,
    },
    total=False,
)

AutoScalingGroupRecommendationTypeDef = TypedDict(
    "AutoScalingGroupRecommendationTypeDef",
    {
        "accountId": str,
        "autoScalingGroupArn": str,
        "autoScalingGroupName": str,
        "finding": Literal["Underprovisioned", "Overprovisioned", "Optimized", "NotOptimized"],
        "utilizationMetrics": List["UtilizationMetricTypeDef"],
        "lookBackPeriodInDays": float,
        "currentConfiguration": "AutoScalingGroupConfigurationTypeDef",
        "recommendationOptions": List["AutoScalingGroupRecommendationOptionTypeDef"],
        "lastRefreshTimestamp": datetime,
    },
    total=False,
)

EBSUtilizationMetricTypeDef = TypedDict(
    "EBSUtilizationMetricTypeDef",
    {
        "name": Literal[
            "VolumeReadOpsPerSecond",
            "VolumeWriteOpsPerSecond",
            "VolumeReadBytesPerSecond",
            "VolumeWriteBytesPerSecond",
        ],
        "statistic": Literal["Maximum", "Average"],
        "value": float,
    },
    total=False,
)

ExportDestinationTypeDef = TypedDict(
    "ExportDestinationTypeDef", {"s3": "S3DestinationTypeDef"}, total=False
)

GetRecommendationErrorTypeDef = TypedDict(
    "GetRecommendationErrorTypeDef", {"identifier": str, "code": str, "message": str}, total=False
)

InstanceRecommendationOptionTypeDef = TypedDict(
    "InstanceRecommendationOptionTypeDef",
    {
        "instanceType": str,
        "projectedUtilizationMetrics": List["UtilizationMetricTypeDef"],
        "performanceRisk": float,
        "rank": int,
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
        "finding": Literal["Underprovisioned", "Overprovisioned", "Optimized", "NotOptimized"],
        "utilizationMetrics": List["UtilizationMetricTypeDef"],
        "lookBackPeriodInDays": float,
        "recommendationOptions": List["InstanceRecommendationOptionTypeDef"],
        "recommendationSources": List["RecommendationSourceTypeDef"],
        "lastRefreshTimestamp": datetime,
    },
    total=False,
)

LambdaFunctionMemoryProjectedMetricTypeDef = TypedDict(
    "LambdaFunctionMemoryProjectedMetricTypeDef",
    {
        "name": Literal["Duration"],
        "statistic": Literal["LowerBound", "UpperBound", "Expected"],
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
        "finding": Literal["Optimized", "NotOptimized", "Unavailable"],
        "findingReasonCodes": List[
            Literal[
                "MemoryOverprovisioned",
                "MemoryUnderprovisioned",
                "InsufficientData",
                "Inconclusive",
            ]
        ],
        "memorySizeRecommendationOptions": List["LambdaFunctionMemoryRecommendationOptionTypeDef"],
    },
    total=False,
)

LambdaFunctionUtilizationMetricTypeDef = TypedDict(
    "LambdaFunctionUtilizationMetricTypeDef",
    {
        "name": Literal["Duration", "Memory"],
        "statistic": Literal["Maximum", "Average"],
        "value": float,
    },
    total=False,
)

ProjectedMetricTypeDef = TypedDict(
    "ProjectedMetricTypeDef",
    {
        "name": Literal[
            "Cpu",
            "Memory",
            "EBS_READ_OPS_PER_SECOND",
            "EBS_WRITE_OPS_PER_SECOND",
            "EBS_READ_BYTES_PER_SECOND",
            "EBS_WRITE_BYTES_PER_SECOND",
        ],
        "timestamps": List[datetime],
        "values": List[float],
    },
    total=False,
)

ReasonCodeSummaryTypeDef = TypedDict(
    "ReasonCodeSummaryTypeDef",
    {"name": Literal["MemoryOverprovisioned", "MemoryUnderprovisioned"], "value": float},
    total=False,
)

RecommendationExportJobTypeDef = TypedDict(
    "RecommendationExportJobTypeDef",
    {
        "jobId": str,
        "destination": "ExportDestinationTypeDef",
        "resourceType": Literal["Ec2Instance", "AutoScalingGroup"],
        "status": Literal["Queued", "InProgress", "Complete", "Failed"],
        "creationTimestamp": datetime,
        "lastUpdatedTimestamp": datetime,
        "failureReason": str,
    },
    total=False,
)

RecommendationSourceTypeDef = TypedDict(
    "RecommendationSourceTypeDef",
    {
        "recommendationSourceArn": str,
        "recommendationSourceType": Literal[
            "Ec2Instance", "AutoScalingGroup", "EbsVolume", "LambdaFunction"
        ],
    },
    total=False,
)

RecommendationSummaryTypeDef = TypedDict(
    "RecommendationSummaryTypeDef",
    {
        "summaries": List["SummaryTypeDef"],
        "recommendationResourceType": Literal[
            "Ec2Instance", "AutoScalingGroup", "EbsVolume", "LambdaFunction"
        ],
        "accountId": str,
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

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef", {"bucket": str, "key": str, "metadataKey": str}, total=False
)

SummaryTypeDef = TypedDict(
    "SummaryTypeDef",
    {
        "name": Literal["Underprovisioned", "Overprovisioned", "Optimized", "NotOptimized"],
        "value": float,
        "reasonCodeSummaries": List["ReasonCodeSummaryTypeDef"],
    },
    total=False,
)

UtilizationMetricTypeDef = TypedDict(
    "UtilizationMetricTypeDef",
    {
        "name": Literal[
            "Cpu",
            "Memory",
            "EBS_READ_OPS_PER_SECOND",
            "EBS_WRITE_OPS_PER_SECOND",
            "EBS_READ_BYTES_PER_SECOND",
            "EBS_WRITE_BYTES_PER_SECOND",
        ],
        "statistic": Literal["Maximum", "Average"],
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
    },
    total=False,
)

VolumeRecommendationOptionTypeDef = TypedDict(
    "VolumeRecommendationOptionTypeDef",
    {"configuration": "VolumeConfigurationTypeDef", "performanceRisk": float, "rank": int},
    total=False,
)

VolumeRecommendationTypeDef = TypedDict(
    "VolumeRecommendationTypeDef",
    {
        "volumeArn": str,
        "accountId": str,
        "currentConfiguration": "VolumeConfigurationTypeDef",
        "finding": Literal["Optimized", "NotOptimized"],
        "utilizationMetrics": List["EBSUtilizationMetricTypeDef"],
        "lookBackPeriodInDays": float,
        "volumeRecommendationOptions": List["VolumeRecommendationOptionTypeDef"],
        "lastRefreshTimestamp": datetime,
    },
    total=False,
)

DescribeRecommendationExportJobsResponseTypeDef = TypedDict(
    "DescribeRecommendationExportJobsResponseTypeDef",
    {"recommendationExportJobs": List["RecommendationExportJobTypeDef"], "nextToken": str},
    total=False,
)

EBSFilterTypeDef = TypedDict(
    "EBSFilterTypeDef", {"name": Literal["Finding"], "values": List[str]}, total=False
)

ExportAutoScalingGroupRecommendationsResponseTypeDef = TypedDict(
    "ExportAutoScalingGroupRecommendationsResponseTypeDef",
    {"jobId": str, "s3Destination": "S3DestinationTypeDef"},
    total=False,
)

ExportEC2InstanceRecommendationsResponseTypeDef = TypedDict(
    "ExportEC2InstanceRecommendationsResponseTypeDef",
    {"jobId": str, "s3Destination": "S3DestinationTypeDef"},
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {"name": Literal["Finding", "RecommendationSourceType"], "values": List[str]},
    total=False,
)

GetAutoScalingGroupRecommendationsResponseTypeDef = TypedDict(
    "GetAutoScalingGroupRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "autoScalingGroupRecommendations": List["AutoScalingGroupRecommendationTypeDef"],
        "errors": List["GetRecommendationErrorTypeDef"],
    },
    total=False,
)

GetEBSVolumeRecommendationsResponseTypeDef = TypedDict(
    "GetEBSVolumeRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "volumeRecommendations": List["VolumeRecommendationTypeDef"],
        "errors": List["GetRecommendationErrorTypeDef"],
    },
    total=False,
)

GetEC2InstanceRecommendationsResponseTypeDef = TypedDict(
    "GetEC2InstanceRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "instanceRecommendations": List["InstanceRecommendationTypeDef"],
        "errors": List["GetRecommendationErrorTypeDef"],
    },
    total=False,
)

GetEC2RecommendationProjectedMetricsResponseTypeDef = TypedDict(
    "GetEC2RecommendationProjectedMetricsResponseTypeDef",
    {"recommendedOptionProjectedMetrics": List["RecommendedOptionProjectedMetricTypeDef"]},
    total=False,
)

GetEnrollmentStatusResponseTypeDef = TypedDict(
    "GetEnrollmentStatusResponseTypeDef",
    {
        "status": Literal["Active", "Inactive", "Pending", "Failed"],
        "statusReason": str,
        "memberAccountsEnrolled": bool,
    },
    total=False,
)

GetLambdaFunctionRecommendationsResponseTypeDef = TypedDict(
    "GetLambdaFunctionRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "lambdaFunctionRecommendations": List["LambdaFunctionRecommendationTypeDef"],
    },
    total=False,
)

GetRecommendationSummariesResponseTypeDef = TypedDict(
    "GetRecommendationSummariesResponseTypeDef",
    {"nextToken": str, "recommendationSummaries": List["RecommendationSummaryTypeDef"]},
    total=False,
)

JobFilterTypeDef = TypedDict(
    "JobFilterTypeDef",
    {"name": Literal["ResourceType", "JobStatus"], "values": List[str]},
    total=False,
)

LambdaFunctionRecommendationFilterTypeDef = TypedDict(
    "LambdaFunctionRecommendationFilterTypeDef",
    {"name": Literal["Finding", "FindingReasonCode"], "values": List[str]},
    total=False,
)

S3DestinationConfigTypeDef = TypedDict(
    "S3DestinationConfigTypeDef", {"bucket": str, "keyPrefix": str}, total=False
)

UpdateEnrollmentStatusResponseTypeDef = TypedDict(
    "UpdateEnrollmentStatusResponseTypeDef",
    {"status": Literal["Active", "Inactive", "Pending", "Failed"], "statusReason": str},
    total=False,
)
