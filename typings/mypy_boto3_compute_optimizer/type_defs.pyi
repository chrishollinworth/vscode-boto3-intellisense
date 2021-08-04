"""
Type annotations for compute-optimizer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_compute_optimizer.type_defs import AutoScalingGroupConfigurationTypeDef

    data: AutoScalingGroupConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    EBSFindingType,
    EBSMetricNameType,
    ExportableAutoScalingGroupFieldType,
    ExportableInstanceFieldType,
    ExportableLambdaFunctionFieldType,
    ExportableVolumeFieldType,
    FilterNameType,
    FindingReasonCodeType,
    FindingType,
    InstanceRecommendationFindingReasonCodeType,
    JobFilterNameType,
    JobStatusType,
    LambdaFunctionMemoryMetricStatisticType,
    LambdaFunctionMetricNameType,
    LambdaFunctionMetricStatisticType,
    LambdaFunctionRecommendationFilterNameType,
    LambdaFunctionRecommendationFindingReasonCodeType,
    LambdaFunctionRecommendationFindingType,
    MetricNameType,
    MetricStatisticType,
    PlatformDifferenceType,
    RecommendationSourceTypeType,
    ResourceTypeType,
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
    "AutoScalingGroupConfigurationTypeDef",
    "AutoScalingGroupRecommendationOptionTypeDef",
    "AutoScalingGroupRecommendationTypeDef",
    "DescribeRecommendationExportJobsRequestRequestTypeDef",
    "DescribeRecommendationExportJobsResponseTypeDef",
    "EBSFilterTypeDef",
    "EBSUtilizationMetricTypeDef",
    "ExportAutoScalingGroupRecommendationsRequestRequestTypeDef",
    "ExportAutoScalingGroupRecommendationsResponseTypeDef",
    "ExportDestinationTypeDef",
    "ExportEBSVolumeRecommendationsRequestRequestTypeDef",
    "ExportEBSVolumeRecommendationsResponseTypeDef",
    "ExportEC2InstanceRecommendationsRequestRequestTypeDef",
    "ExportEC2InstanceRecommendationsResponseTypeDef",
    "ExportLambdaFunctionRecommendationsRequestRequestTypeDef",
    "ExportLambdaFunctionRecommendationsResponseTypeDef",
    "FilterTypeDef",
    "GetAutoScalingGroupRecommendationsRequestRequestTypeDef",
    "GetAutoScalingGroupRecommendationsResponseTypeDef",
    "GetEBSVolumeRecommendationsRequestRequestTypeDef",
    "GetEBSVolumeRecommendationsResponseTypeDef",
    "GetEC2InstanceRecommendationsRequestRequestTypeDef",
    "GetEC2InstanceRecommendationsResponseTypeDef",
    "GetEC2RecommendationProjectedMetricsRequestRequestTypeDef",
    "GetEC2RecommendationProjectedMetricsResponseTypeDef",
    "GetEnrollmentStatusResponseTypeDef",
    "GetLambdaFunctionRecommendationsRequestRequestTypeDef",
    "GetLambdaFunctionRecommendationsResponseTypeDef",
    "GetRecommendationErrorTypeDef",
    "GetRecommendationSummariesRequestRequestTypeDef",
    "GetRecommendationSummariesResponseTypeDef",
    "InstanceRecommendationOptionTypeDef",
    "InstanceRecommendationTypeDef",
    "JobFilterTypeDef",
    "LambdaFunctionMemoryProjectedMetricTypeDef",
    "LambdaFunctionMemoryRecommendationOptionTypeDef",
    "LambdaFunctionRecommendationFilterTypeDef",
    "LambdaFunctionRecommendationTypeDef",
    "LambdaFunctionUtilizationMetricTypeDef",
    "ProjectedMetricTypeDef",
    "ReasonCodeSummaryTypeDef",
    "RecommendationExportJobTypeDef",
    "RecommendationSourceTypeDef",
    "RecommendationSummaryTypeDef",
    "RecommendedOptionProjectedMetricTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationConfigTypeDef",
    "S3DestinationTypeDef",
    "SummaryTypeDef",
    "UpdateEnrollmentStatusRequestRequestTypeDef",
    "UpdateEnrollmentStatusResponseTypeDef",
    "UtilizationMetricTypeDef",
    "VolumeConfigurationTypeDef",
    "VolumeRecommendationOptionTypeDef",
    "VolumeRecommendationTypeDef",
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
    },
    total=False,
)

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

GetEC2RecommendationProjectedMetricsRequestRequestTypeDef = TypedDict(
    "GetEC2RecommendationProjectedMetricsRequestRequestTypeDef",
    {
        "instanceArn": str,
        "stat": MetricStatisticType,
        "period": int,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)

GetEC2RecommendationProjectedMetricsResponseTypeDef = TypedDict(
    "GetEC2RecommendationProjectedMetricsResponseTypeDef",
    {
        "recommendedOptionProjectedMetrics": List["RecommendedOptionProjectedMetricTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnrollmentStatusResponseTypeDef = TypedDict(
    "GetEnrollmentStatusResponseTypeDef",
    {
        "status": StatusType,
        "statusReason": str,
        "memberAccountsEnrolled": bool,
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

GetRecommendationErrorTypeDef = TypedDict(
    "GetRecommendationErrorTypeDef",
    {
        "identifier": str,
        "code": str,
        "message": str,
    },
    total=False,
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

InstanceRecommendationOptionTypeDef = TypedDict(
    "InstanceRecommendationOptionTypeDef",
    {
        "instanceType": str,
        "projectedUtilizationMetrics": List["UtilizationMetricTypeDef"],
        "platformDifferences": List[PlatformDifferenceType],
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
        "finding": FindingType,
        "findingReasonCodes": List[InstanceRecommendationFindingReasonCodeType],
        "utilizationMetrics": List["UtilizationMetricTypeDef"],
        "lookBackPeriodInDays": float,
        "recommendationOptions": List["InstanceRecommendationOptionTypeDef"],
        "recommendationSources": List["RecommendationSourceTypeDef"],
        "lastRefreshTimestamp": datetime,
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

ProjectedMetricTypeDef = TypedDict(
    "ProjectedMetricTypeDef",
    {
        "name": MetricNameType,
        "timestamps": List[datetime],
        "values": List[float],
    },
    total=False,
)

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

SummaryTypeDef = TypedDict(
    "SummaryTypeDef",
    {
        "name": FindingType,
        "value": float,
        "reasonCodeSummaries": List["ReasonCodeSummaryTypeDef"],
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
    },
    total=False,
)

VolumeRecommendationOptionTypeDef = TypedDict(
    "VolumeRecommendationOptionTypeDef",
    {
        "configuration": "VolumeConfigurationTypeDef",
        "performanceRisk": float,
        "rank": int,
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
    },
    total=False,
)
