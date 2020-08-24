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
    "ExportDestinationTypeDef",
    "GetRecommendationErrorTypeDef",
    "InstanceRecommendationOptionTypeDef",
    "InstanceRecommendationTypeDef",
    "ProjectedMetricTypeDef",
    "RecommendationExportJobTypeDef",
    "RecommendationSourceTypeDef",
    "RecommendationSummaryTypeDef",
    "RecommendedOptionProjectedMetricTypeDef",
    "S3DestinationTypeDef",
    "SummaryTypeDef",
    "UtilizationMetricTypeDef",
    "DescribeRecommendationExportJobsResponseTypeDef",
    "ExportAutoScalingGroupRecommendationsResponseTypeDef",
    "ExportEC2InstanceRecommendationsResponseTypeDef",
    "FilterTypeDef",
    "GetAutoScalingGroupRecommendationsResponseTypeDef",
    "GetEC2InstanceRecommendationsResponseTypeDef",
    "GetEC2RecommendationProjectedMetricsResponseTypeDef",
    "GetEnrollmentStatusResponseTypeDef",
    "GetRecommendationSummariesResponseTypeDef",
    "JobFilterTypeDef",
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

ProjectedMetricTypeDef = TypedDict(
    "ProjectedMetricTypeDef",
    {"name": Literal["Cpu", "Memory"], "timestamps": List[datetime], "values": List[float]},
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
        "recommendationSourceType": Literal["Ec2Instance", "AutoScalingGroup"],
    },
    total=False,
)

RecommendationSummaryTypeDef = TypedDict(
    "RecommendationSummaryTypeDef",
    {
        "summaries": List["SummaryTypeDef"],
        "recommendationResourceType": Literal["Ec2Instance", "AutoScalingGroup"],
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
    },
    total=False,
)

UtilizationMetricTypeDef = TypedDict(
    "UtilizationMetricTypeDef",
    {"name": Literal["Cpu", "Memory"], "statistic": Literal["Maximum", "Average"], "value": float},
    total=False,
)

DescribeRecommendationExportJobsResponseTypeDef = TypedDict(
    "DescribeRecommendationExportJobsResponseTypeDef",
    {"recommendationExportJobs": List["RecommendationExportJobTypeDef"], "nextToken": str},
    total=False,
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

S3DestinationConfigTypeDef = TypedDict(
    "S3DestinationConfigTypeDef", {"bucket": str, "keyPrefix": str}, total=False
)

UpdateEnrollmentStatusResponseTypeDef = TypedDict(
    "UpdateEnrollmentStatusResponseTypeDef",
    {"status": Literal["Active", "Inactive", "Pending", "Failed"], "statusReason": str},
    total=False,
)
